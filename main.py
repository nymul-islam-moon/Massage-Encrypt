#phthon Massage encryption
import sys

while(True):
    option = input("Enter Your Option : ")
    if "encrypt" in option or "decrypt" in option:


        massage = input("Enter The Massage : ")

        key = int(input("Enter The Key : "))

        file1 = "QAZWSXEDCRFVTGBYHNUJMIKOLPabcdefghijklmnopqrstuvwxyz\ 1234567890!@#$%^&*()_+-=?/>.<,|':;~"

        if "encrypt" in option:

            encrypt = ""
            for i in massage:
                position = file1.find(i)
                newposition = int(position + key) % 89
                encrypt += file1[newposition]

            print(encrypt)

        else:
            decrypt = ""

            for i in massage:
                pos = file1.find(i)
                newpos = int(pos - key) % 89
                decrypt += file1[newpos]

            print(decrypt)

    else:
        sys.exit()
