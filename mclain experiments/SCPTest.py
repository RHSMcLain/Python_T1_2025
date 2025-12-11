import paramiko
import getpass
import time
import threading
import sys
from scp import SCPClient
import os


# --- User-provided information ---
# hosts = ['hslab-mm-01', 
hosts = ['hslab-mm-02', 
         'hslab-mm-03', 
         'hslab-mm-04', 
         'hslab-mm-05', 
         'hslab-mm-06', 
         'hslab-mm-07', 
         'hslab-mm-08', 
         'hslab-mm-09', 
         'hslab-mm-10', 
         'hslab-mm-11', 
         'hslab-mm-12', 
         'hslab-mm-13', 
         'hslab-mm-14', 
         'hslab-mm-15', 
         'hslab-mm-16', 
         'hslab-mm-17', 
         'hslab-mm-18', 
         'hslab-mm-19', 
         'hslab-mm-20', 
         'hslab-mm-21', 
         'hslab-mm-22', 
         'hslab-mm-23', 
         'hslab-mm-24']
hosts = ['hslab-mm-08']
# hostname = 'hslab-mm-09.local'
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# The sudo command to be executed.
# This example will get a listing of the root directory.
# This should be replaced with the command you need to run.
filename = 'Arduino IDE.app'
sudo_command = f'sudo mv -r "/Users/Shared/{filename}" "/Applications/{filename}"'
print(f'sudo command is {sudo_command}')
# --- SSH client setup ---
def connectAndRun(hostname):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print(f"Connecting to {hostname} as {username}...")
        client.connect(hostname, username=username, password=password)
        # print("Connection successful.")

        # --- Execute the sudo command ---
        # We use invoke_shell() to create an interactive shell, which is better
        # for commands that require a password prompt.
        # print(f"Executing command: '{sudo_command}'")
        shell = client.invoke_shell()
        
        # Send the sudo command to the shell
        shell.send(sudo_command + '\n')
        
        # Wait for the password prompt. This part can be tricky and may need
        # to be adjusted with more complex logic for different systems.
        # We will read the shell output in chunks and look for the prompt.
        time.sleep(1) # Give it a moment to send the prompt
        
        output = shell.recv(1024).decode('utf-8')
        # print("Received output before sending password:", output)

        # If the password prompt is found, send the password
        if 'password' in output.lower():
            # print("Password prompt detected. Sending password...")
            shell.send(password + '\n')
            time.sleep(1) # Wait for the command to finish
            
            # Read the final output from the shell
            final_output = shell.recv(9999).decode('utf-8')
            # print("\n--- Command Output ---")
            # print(final_output)

        else:
            # If no password prompt, the command might have run directly or failed
            # print("No password prompt detected. The command might have failed or does not require a password.")
            # print("\n--- Command Output ---")
            # print(output)
            time.sleep(1)
            # Read any remaining output
            final_output = shell.recv(9999).decode('utf-8')
            # print(final_output)

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username and password.")
    except paramiko.SSHException as ssh_ex:
        print(f"SSH error: {ssh_ex}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # --- Close the connection ---
        if 'client' in locals():
            client.close()
            print("\nConnection closed.")
def scp_file_with_password(host, filename):
    """
    Prompts for a password, connects via SSH, and copies a file using SCP.
    """
    LOCAL_FILE_PATH = f'/Applications/{filename}'
    #LOCAL_FILE_PATH = '/Users/amclain/Downloads/arduino-ide_2.3.6_macOS_arm64.dmg'
    REMOTE_DESTINATION_PATH = "/Users/Shared/"
    PORT = 22
    try:
        # 1. Request credentials securely
        print(f"Connecting to {host} as user {username}...")
        
        # 2. Setup SSH Client
        ssh_client = paramiko.SSHClient()

        # Automatically add the remote host key if it's not already in the known_hosts file
        # WARNING: This is less secure than manually verifying and adding the key.
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 3. Connect to the remote server
        ssh_client.connect(
            hostname=host,
            port=PORT,
            username=username,
            password=password,
            timeout=10 # Set a connection timeout
        )

        print("Successfully connected to the remote server.")

        # 4. Use SCPClient for file transfer
        with SCPClient(ssh_client.get_transport()) as scp:
            # The 'put' method copies a file from local to remote
            print(f"Copying '{LOCAL_FILE_PATH}' to '{REMOTE_DESTINATION_PATH}'...")
            scp.put(LOCAL_FILE_PATH, remote_path=REMOTE_DESTINATION_PATH, recursive=True)
            
            print("File copied successfully!")

    except paramiko.AuthenticationException:
        print(f"Error: Authentication failed for user {username} on {host}. Check username and password.")
        sys.exit(1)
    except paramiko.SSHException as e:
        print(f"Error connecting or during SSH session: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: Local file not found at '{LOCAL_FILE_PATH}'")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        # 5. Close the SSH connection
        if 'ssh_client' in locals() and ssh_client:
            ssh_client.close()
            # print("Connection closed.")

def transferAndCopy(host, filename):
    scp_file_with_password(host, filename)
    #connectAndRun(host)


#---------------------Main Code------
if __name__ == "__main__":
    ext = ""
    counter = 0
    for n in range(1):
        print(counter)
        counter += 1
        threads = []
        #create a thread for each hostname
        ext = ""
            #we're running it twice, once adding .local to all of them, and once without
        for hostname in hosts:
            hostname = hostname + ext
            thread = threading.Thread(target=transferAndCopy, args=(hostname,filename,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        ext = ".local" #on the second run through, it changes 
    
    print("\n[SUCCESS] All threads have finished processing.")
    
