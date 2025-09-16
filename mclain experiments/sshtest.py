import paramiko
import getpass

# --- User-provided information ---
hostname = 'your_remote_machine_ip'
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
command = 'your_command_here'  # e.g., 'ls -l', 'hostname'

# --- SSH client setup ---
try:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print(f"Connecting to {hostname}...")
    client.connect(hostname, username=username, password=password)
    print("Connection successful.")

    # --- Execute command ---
    print(f"Executing command: '{command}'")
    stdin, stdout, stderr = client.exec_command(command)

    # --- Print output ---
    print("\n--- Command Output (stdout) ---")
    for line in stdout:
        print(line.strip())

    print("\n--- Command Errors (stderr) ---")
    for line in stderr:
        print(line.strip())

except paramiko.AuthenticationException:
    print("Authentication failed. Please check your username and password.")
except paramiko.SSHException as ssh_ex:
    print(f"SSH error: {ssh_ex}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # --- Close the connection ---
    if 'client' in locals():
        client.close()
        print("\nConnection closed.")