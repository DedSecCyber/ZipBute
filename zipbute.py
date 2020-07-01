import zipfile
import sys

print('''
       .__      ___.           __          
_______|__|_____\_ |__  __ ___/  |_  ____  
\___   /  \____ \| __ \|  |  \   __\/ __ \ 
 /    /|  |  |_> > \_\ \  |  /|  | \  ___/ 
/_____ \__|   __/|___  /____/ |__|  \___  >
      \/  |__|       \/                 \/ 
Zip File Password Cracker Ver.1
Programing by Thitigorn Pumma (Zero Hacker)''')

def usage():
    print("Command: " + sys.argv[0] + " <zipfile> <passfile>")

def main(files, passfile):
    count = 1

    with open(passfile,'rb') as text:
        for entry in text.readlines():
            password = entry.strip()
            try:
                with zipfile.ZipFile(files,'r') as zf:
                    zf.extractall(pwd=password)

                    data = zf.namelist()[0]
                    data_size = zf.getinfo(data).file_size
                    print("=" * 30)
                    print("[+] Password found! :  %s\n ~%s\n ~%s\n"% (password.decode('utf8'), data, data_size))
                    print("=" * 30)
                    break

            except:
                number = count
                print('[*] Cracking password...  %s' % (password.decode('utf8')))
                count += 1
                pass
   
if len(sys.argv) != 3:
    usage()

else:
    main(sys.argv[1], sys.argv[2])

