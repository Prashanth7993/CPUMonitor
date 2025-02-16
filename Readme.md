# CPU Monitoring and Process Management System

## Overview
This project monitors CPU usage and manages processes accordingly. It:
- Detects when CPU usage exceeds 60%.
- Identifies the process consuming the most CPU.
- Takes appropriate action based on process type:
  - **System Process:** Sends an email alert.
  - **Application Process:** Restarts the process.
  - **Other Processes:** Kills the process.
- Ensures security with encrypted password storage.

## Features
- **CPU Monitoring**: Continuously checks CPU usage.
- **Process Handling**: Identifies and manages high CPU-consuming processes.
- **Secure Authentication**: Uses encryption to store email credentials securely.
- **Modular Design**: Organized code with separate modules for different functionalities.
- **Error Handling**: Handles process errors and permission issues gracefully.

---
## Installation
### Prerequisites
- Python 3.x
- Required Python libraries:
  ```sh
  pip install psutil cryptography
  ```

### Setup
1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd cpu-monitor
   ```
2. **Generate an encryption key & encrypt the email password:**
   ```sh
   python encrypt_password.py
   ```
3. **Run the CPU monitor:**
   ```sh
   python CPU_Monitor.py
   ```

---
## Project Structure
```
├── CPU_Monitor.py           # Main script to monitor CPU usage
├── config.py                # Configuration file for thresholds and email settings
├── process_utils.py         # Functions to handle processes (restart, kill, etc.)
├── utils.py                 # Utility functions (email sending, encryption, etc.)
├── encrypt_password.py      # Encrypts email password
├── decrypt_password.py      # Decrypts stored password
├── README.md                # Project documentation
```

---
## Usage
### Running the CPU Monitor
```sh
python CPU_Monitor.py
```
This script will:
- Check CPU usage every 5 seconds.
- Identify the process with the highest CPU usage.
- Take action based on the process type.

### Testing High CPU Usage
To simulate high CPU load, run:
```sh
python -c "while True: pass"
```

---
## Security
- The email password is **never stored in plain text**.
- Uses **cryptography.fernet** for encryption.
- Users must enter their email password manually to encrypt it.

---
## Troubleshooting
### Email Not Sending
- Ensure SMTP settings are correct in `config.py`.
- If using Gmail, enable **Less Secure Apps** or create an **App Password**.
- Check if the encryption key is correctly generated and stored.

### Process Not Restarting
- Ensure the process has restart permissions.
- Some system applications cannot be restarted programmatically.

---
## Contribution
Feel free to submit issues or create pull requests to improve the project.
