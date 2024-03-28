''' Types of Debugging

Static analysis - reading the program without execution
Source code analysis - automatic check for known bugs
Tracing or print debugging - print("1"),print("2"),print("3")
Remote debugging - debug from a different remote system
Post-mortem debugging - debug based on crash and error logs

we need to accept that debugging is very hard and frustating
    tracing root causes of a bug is complex

    can be easy to find the effect , but not the cause of bug
    can be hard to reproduce the bug or issue
    interdependecies can cause a 'fix' to result in new bug
    it can take longer to debug than to create a bug(writing a code that caused the bug in the first place)

print() can be a useful strategy , but there are limitations to this approach

now lets see a method in python to perform a more robust debugging


so we are using PDB (python debugger ) for more efficient debugging

pdb is an inbuilt module in python
'''

import pdb

test = "test"
print(test)

breakpoint()

# python3 -m pdb debug_scripts.py  (if we execute this command in vscode terminal this will load the pdb even before executing the script)


print(test)
print("here")

for i in range(10):
    print(i)



''' Wrap up and next steps:

    Practise, practise, practise
    practice reading and understand more advanced scripts and tooling
    practice modifying , improving and porting existing scripts and tools
    as well as create your own scripts and tooling/tools

    aim to apply your knowledge to hacking task and understand how to extend python 
    beyond standalone small scripts, eg: aim to re-impliment the projects we discussed in this course
    and build your understanding to create your own custom scripts and tools.

    when performing security testing/ VAPT you should
    Approach testing from a programmers perspective
    think about how certaing function might have been implemented and how it could potentially go wrong
    '''










'''
Python is a versatile language that is commonly used in various areas of cybersecurity, including hacking, ethical hacking, vulnerability assessment and penetration testing 
(VAPT), security testing, bug hunting, and capture the flag (CTF) competitions. Here's how Python is used in each of these areas:

1. Hacking: Python is used by hackers for writing custom tools and scripts to exploit vulnerabilities, create malware, perform reconnaissance, and automate attacks. 
Its ease of use and readability make it a popular choice for hacking activities.

2. Ethical Hacking: Ethical hackers, also known as white hat hackers, use Python to identify and exploit vulnerabilities in systems and networks to improve their security. 
Python is used to write tools for network scanning, vulnerability assessment, and penetration testing.

3. Vulnerability Assessment and Penetration Testing (VAPT): Python is extensively used in VAPT for automating tasks such as scanning for vulnerabilities, testing for common 
security issues, and performing penetration tests on web applications and networks.

4. Security Testing: Python is used in security testing to automate the testing of software and systems for security vulnerabilities and weaknesses. It is used to write 
scripts for conducting security audits, analyzing logs, and testing the security of applications.

5. Bug Hunting: Bug hunters use Python to automate the process of finding and reporting software bugs and vulnerabilities. Python scripts can be used to scan web applications
and services for security flaws and report them to the developers.

6. Capture the Flag (CTF) Competitions: In CTF competitions, participants use Python to solve challenges that require exploiting vulnerabilities, reverse engineering, 
cryptography, and other security-related tasks. Python's versatility and libraries make it a valuable tool in CTF competitions.

Overall, Python's simplicity, readability, and extensive library support make it a preferred choice for cybersecurity professionals and enthusiasts in various hacking and 
security-related activities.


if you see a computer engineer say they hate programming , it basically means they hate debugging
'''