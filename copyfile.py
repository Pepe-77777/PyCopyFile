import sys
import shutil
import os

if (len(sys.argv) < 3):
    print("[Error!] Args do not exist!")

elif os.path.exists(sys.argv[1]) == False:
    print("[Error!] The file inside the Args 1 parameter does not exist!")

elif os.path.exists(sys.argv[2]) == True:
    print("[Error!] The file inside the Args 2 parameter already exists!")

else:
    shutil.copyfile(sys.argv[1], sys.argv[2])
    print("Done! Copied", sys.argv[1], "to", sys.argv[2])