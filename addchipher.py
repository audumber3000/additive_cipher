class thod():

    def ad_thod(self):

        print("Be ready with your chipher-text!")
        print("---------------------------------------------------------")
        print("@ NOTE = PLEASE ENTER CAPS LETTERS")
        k = input("Enter you chipher-text :")
        print("---------------------------------------------------------")
        strplain = " "

        for j in range(0, 26):
             plain = []
             text = " "
             for i in range(0 , len(k)):

                  b = (ord(k[i])-65)
                  z = (b-j)%26
                  y = (chr(z + 65))
                  plain.append(y)
             for x in plain:
                 text += x

             print(f'Encrypted Cipher-text:{text}')







print("welcome to Cipher Breaking Algorithem")
ad = thod()
print("Are you here to Break the Security ?  \n1.yes  \n2.No")

p = int(input())

if(p==1):
    ad.ad_thod()
else:
    print("Thank-you , you choose to Quit.")


