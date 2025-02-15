# import psutil
# import subprocess
# from utils import send_email
# from Config import CPU_THRESHOLD

# # List of system processes that should not be killed
# SYSTEM_PROCESSES = ["wininit.exe", "services.exe", "smss.exe", "csrss.exe", 
#                     "winlogon.exe", "lsass.exe", "System Idle Process", "system"]

# def get_high_cpu_process():
#     """ Identify the process consuming more than the CPU threshold. """
#     high_cpu_process = None
#     max_cpu_usage = CPU_THRESHOLD

#     for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
#         try:
#             cpu_usage = process.info['cpu_percent']
#             if cpu_usage > max_cpu_usage:
#                 high_cpu_process = process
#                 max_cpu_usage = cpu_usage
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             continue  

#     return (high_cpu_process, max_cpu_usage) if high_cpu_process else (None, None)

# def is_system_process(process):
#     """ Check if a process is a system process. """
#     try:
#         return process.name().lower() in SYSTEM_PROCESSES or "system" in process.username().lower()
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         return False  

# def restart_process(process):
#     """ Restart an application process. """
#     try:
#         process_name = process.name()
#         pid = process.pid
#         print(f"Restarting application process: {process_name} (PID: {pid})")
        
#         process.terminate()
#         process.wait()

#         subprocess.Popen([process_name], shell=True)
#         print(f"Restarted: {process_name}")

#     except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
#         print(f"Failed to restart process: {e}")

# def handle_process():
#     """ Handle high CPU usage process accordingly. """
#     process, cpu_usage = get_high_cpu_process()
    
#     if process is None:
#         print("✅ No high CPU process detected.")
#         return

#     process_name = process.info['name']
#     pid = process.info['pid']
#     print(f"🚨 High CPU usage detected: {process_name} ({cpu_usage}%)")

#     if is_system_process(process):
#         print("📧 Sending email alert (System Process).")
#         send_email(process_name, cpu_usage)

#     elif process_name.endswith(".exe"):  
#         restart_process(process)

#     else:
#         try:
#             print(f"❌ Killing unknown process: {process_name} (PID: {pid})")
#             process.terminate()
#             process.wait(timeout=5)  
#             print(f"✅ Successfully killed: {process_name} (PID: {pid})")
#         except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
#             print(f"⚠️ Failed to terminate {process_name}: {e}")


import psutil
import subprocess
from utils import send_email
from Config import CPU_THRESHOLD

# System processes that should be ignored
SYSTEM_PROCESSES = ["wininit.exe", "services.exe", "smss.exe", "csrss.exe", 
                    "winlogon.exe", "lsass.exe", "System Idle Process", "system"]

def get_high_cpu_process():
    """ Identify the process consuming more than the CPU threshold. """
    high_cpu_process = None
    max_cpu_usage = CPU_THRESHOLD

    for process in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
        try:
            process_name = process.info['name']
            cpu_usage = process.info['cpu_percent']

            # 🚨 Ignore "System Idle Process" and "System"
            if process_name.lower() in ["system idle process", "system"]:
                continue  

            if cpu_usage > max_cpu_usage:
                high_cpu_process = process
                max_cpu_usage = cpu_usage
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  

    return (high_cpu_process, max_cpu_usage) if high_cpu_process else (None, None)

def is_system_process(process):
    """ Check if a process is a system process. """
    try:
        return process.name().lower() in SYSTEM_PROCESSES or "system" in process.username().lower()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return False  

def restart_process(process):
    """ Restart an application process. """
    try:
        process_name = process.name()
        pid = process.pid
        print(f"🔄 Restarting application process: {process_name} (PID: {pid})")
        
        # Terminate the process
        process.terminate()
        process.wait()

        # Restart the process
        subprocess.Popen([process_name], shell=True)
        print(f"✅ Successfully restarted: {process_name}")

    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        print(f"❌ Failed to restart process: {e}")

def handle_process():
    """ Handle high CPU usage process accordingly. """
    process, cpu_usage = get_high_cpu_process()
    
    if process is None:
        print("✅ No high CPU process detected.")
        return

    process_name = process.info['name']
    pid = process.info['pid']
    print(f"🚨 High CPU usage detected: {process_name} ({cpu_usage}%)")

    if is_system_process(process):
        print("📧 Sending email alert (System Process).")
        send_email(process_name, cpu_usage)

    elif process_name.endswith(".exe"):  # Application process
        print(f"🔄 Restarting application: {process_name}")
        restart_process(process)

    else:  # Unknown process
        try:
            print(f"❌ Killing unknown process: {process_name} (PID: {pid})")
            process.terminate()
            process.wait(timeout=5)  
            print(f"✅ Successfully killed: {process_name} (PID: {pid})")
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"⚠️ Failed to terminate {process_name}: {e}")

