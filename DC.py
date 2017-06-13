'''---------------------------------------------------------------------'''
def adler_check_sum(x):
    ls=[]
    for c in x:
        ls.append(ord(c))

    R=1+ls[0]
    L=R

    for i in range (1,len(ls)):
        R=(R+ls[i])%65521
        L=(R+L)%65521

    checksum=R+L*65536
    return hex(checksum)


def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]
'''---------------------------------------------------------------------'''
'''Main'''
def main():

    print("Menu:")
    print("1-Getting checksums for a give string")
    print("2-Checking revieved data is correct")
    print("3-Exit")
    print("help- For menu")

    while True:
        menu=input("Enter option:")
        if(menu=='1'):

            '''Input'''

            words=input("Enter the sting of data:")
            dw_size=int(input("Enter the data word size:"))
            dw=[]
            checksums=[]

            '''Process'''

            for chunk in chunks(words,dw_size):

                dw.append(chunk)



            for d in dw:
                checksums.append(adler_check_sum(d))

            print(dw)
            print(checksums)

        elif(menu=='2'):
            words=input("Enter the sting of codeword:")
            checksum=('0x'+(input("Enter the check sum:")))
            if(checksum==adler_check_sum(words)):
                print("No Error")
            else:
                print("Error")
        elif(menu=='help'):
            print("Menu:")
            print("1-Getting checksums for a give string")
            print("2-Checking revieved data is correct")
            print("3-Exit")
            print("help- For menu")
        elif(menu=='3'):
            break
'''---------------------------------------------------------------------'''
'''Main call'''
main()
