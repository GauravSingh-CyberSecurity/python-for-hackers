'''
echo -ne jesus | sha256sum

a54e71f0e17f5aaf7946e66ab42cf3b1fd4e61d60581736c9f0eb1c3f794eb7c

python3 sha256-password-cracking.py  a54e71f0e17f5aaf7946e66ab42cf3b1fd4e61d60581736c9f0eb1c3f794eb7c



echo -ne justin | sha256sum
python3 sha256-password-cracking.py  102cf10b5286bad9fcfe5e275ace3ddd7dcc23931fb0ca93dc223daf9877cabd

run this out of virtual env
'''


from pwn import *
import sys

if len(sys.argv) != 2:
    print("invalid arguments!")
    print(">> {} <sha256sum>".format(sys.argv[0]))
    exit()

wanted_hash = sys.argv[1]
password_file = "/home/gaurav/Downloads/rockyou.txt"
attempts = 0

with log.progress("Attempting to back: {}! \n".format(wanted_hash)) as p:
    with open(password_file, "r", encoding='latin-1') as password_list:
        for password in password_list:
            password = password.strip("\n").encode('latin-1')
            password_hash = sha256sumhex(password)
            p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
            if password_hash == wanted_hash:
                p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
                exit()
            attempts += 1
    p.failure('Password hash not found!')
