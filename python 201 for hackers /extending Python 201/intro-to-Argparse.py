# Argparse is used to create command line interface "CLI" for python scripts/codes 




''' run this code using this in terminal:
            python3 intro-to-Argparse.py Gaurav 10 
OR
            python3 intro-to-Argparse.py Gaurav 10 --blackhat
            python3 intro-to-Argparse.py Gaurav 10 -bh
            python3 intro-to-Argparse.py Gaurav 10 -ht wh  

    to know more about this arg:
            python3 intro-to-Argparse.py --help


#required= True,   --> this make it a required feild to put -bh in the   python3 intro-to-Argparse.py Gaurav 10 
#required= True,   --> this make it a required feild to put -wh in the   python3 intro-to-Argparse.py Gaurav 10 


'''
import argparse

parser = argparse.ArgumentParser(description="Example Python CLI")

parser.add_argument("hacker_name", help="Enter the hacker name", type=str)
parser.add_argument("hacker_power", help="Enter the hacker power", type=int)

parser.add_argument("-bh", "--blackhat", default=False, action="store_true")
parser.add_argument("-wh", "--whitehat", default=False, action="store_true")
parser.add_argument("-gh", "--greyhat", default=False, action="store_true")

choices = {"wh": "whitehat", "bh": "blackhat", "gh": "greyhat"}
parser.add_argument("-ht", "--hackertype", choices=choices.keys(), help="Choose hacker type", default="wh")

args = parser.parse_args()
args.hackertype = choices[args.hackertype] if args.hackertype in choices else None
print(args)

print("\n---------------------------------------------")
print("hackers name = {}".format(args.hacker_name))
print("\n---------------------------------------------")

if args.blackhat:
    hacker_type = "blackhat"
elif args.whitehat:
    hacker_type = "whitehat"
elif args.greyhat:
    hacker_type = "greyhat"
else:
    hacker_type = "unknown"

print("{} is a {} type of hacker".format(args.hacker_name, hacker_type))
