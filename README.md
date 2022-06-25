# Zip password cracker
## How to use

#### Clone the project (or just copy-paste)
```bash
  sudo git clone https://github.com/Gurguii/Zip-password-cracker
```
#### Go to the project directory 
```bash
  cd Zip-password-cracker
```
#### Run the script
```bash
  python3 zipcracker.py -f <zipfile> -w <wordlist>
```
#### Notes
Optionally you can add the -l/--line <number> option, which will tell the script to start in given line number.  

I'm not sure if it's much better in terms of performance since the way this works is by skiping <number> lines and then start checking for the password.  

I found this useful since whenever you end the script by pressing ctrl+c it will tell the line it was at, so you can "continue" that bruteforcing later on if you want to.
