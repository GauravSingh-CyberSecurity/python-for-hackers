import subprocess
'''
for windows env:

import subprocess
subprocess.call("calc")
'''


'''
#for Linux

import subprocess
import sys

# Define the command based on the operating system
if sys.platform == "linux":
    command = "gnome-calculator"
elif sys.platform == "darwin":  # macOS
    command = "open -a Calculator"
else:
    print("Unsupported operating system")
    sys.exit(1)

# Run the command
subprocess.call(command, shell=True)

#we can use these modules to run other applications like malware in a device (i.e this is a part of trojan horse malwre)
'''


print("\n-----------------------------------------------------------------")


'''
#for windows:
out = subprocess.check_output(["cmd","/c","whoami"])
print("The output was: {}".format(out.decode()))
'''



# Run the command to get the current user (Linux/macOS way)
out = subprocess.check_output(["whoami"])
print("The output was: {}".format(out.decode()))

out = subprocess.check_output(["gnome-calculator"])
print("The output was: {}".format(out.decode()))