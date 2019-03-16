from time import sleep
a = str(input("Enter The Name Of The Image That has To  Be Encrypted : "))
b = ".jpg"
c = a+b
fo = open(c,"rb")
image = fo.read()
fo.close()
image = bytearray(image)
key = int(input("Enter The Key To Encrypt The Image (0-255) : "))
for i,j in enumerate(image):
    image[i] = j^key
a = str(input("Enter The Name Of The Image Where It Has To Be Saved After Encrpytion : "))
c = a+b
print("")
for i in range(10):
    print(">>   "),
    sleep(2)
fo = open(c,"wb")
fo.write(image)
fo.close()
print("")
print("Encryption Has Been Done")