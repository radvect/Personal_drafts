import paramiko
import time


def reboot_server(hostname, username, password):
    while True:
        try:
            print("SSH start")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname, username=username, password=password)
            print("Success")

            # Reboot the server
            print("Reboot")
            stdin, stdout, stderr = client.exec_command("sudo reboot")
            # Wait for the command to complete
            time.sleep(5)

            # Close the SSH connection
            client.close()
            break  # Exit the loop if reboot is successful
        except paramiko.AuthenticationException:
            print("Fail.")
            time.sleep(5)
        except paramiko.SSHException as e:
            print(f"SSH failed: {str(e)}. Retrying in 5 seconds")
            time.sleep(5)



hostname = ""
username = ""
password = ""

reboot_server(hostname, username, password)
