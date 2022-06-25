import zipfile
import sys
import signal
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",metavar="",help="Zip file to crack",required=True)
parser.add_argument("-w","--wordlist",metavar="",help="Wordlist to use",required=True)
parser.add_argument("-l","--line",metavar="",type=int,help="Line to start at")
args=parser.parse_args()

def signal_handler(s,f):
    file.close()
    print(f"\n[!]File closed at line {line} => {password.decode()}\n\n")

signal.signal(signal.SIGINT, signal_handler)

zipf = args.file
wlist = args.wordlist
done=False
zipObj = zipfile.ZipFile(zipf)
line=1

if args.line:
    line=args.line+1

print("Press ctrl+c to stop")

with open(wlist,'rb') as file:
    if args.line:
        for i in range(args.line):
            next(file)
    for password in file:
        try:
            zipObj.extractall(pwd=password.strip())
            print(f"\n[!] Password found at line {line} => {password.decode()}")
            done=True
            break
        except:
            line+=1
            continue

if done:
    sys.exit(0)
print("[-]Password not found")