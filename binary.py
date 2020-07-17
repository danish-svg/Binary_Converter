binary = {}
with open("edited.txt","r+") as f:
    for line in f:
        key,value = line.split()
        binary[key] = value
        
binary[' '] = '00100000'
def txt2bin():
    global binary
    text = input("Enter the word or sentence which you wanna convert in binary :")
    binry = ''
    for i in text:
        binry += str(binary[i])
    print(binry)

def bin2txt():
    global binary
    key_list = list(binary.keys()) 
    val_list = list(binary.values()) 
    onez = input("Enter or paste the binary you wanna convert into \ntext :")
    text = ''
    s = 0
    e = 8
    le = len(onez)//8
    if len(onez)>=8:
        for i in range(le):
            seta = onez[s:e]
            if seta in list(binary.values()):
                letter = key_list[val_list.index(seta)]
                text += letter
                s += 8
                e += 8
            else:
                print("The binary you have entered doesn't exist in our list.\nTry again...")
    else:
        print("Your binary lenght is less than 8 !!!")
    print(text)
    
    

while True:
    print('''
<<<Welcome to Binary Converter>>>
    
    <1 : Text to Binary>
    <2 : Binary to text>
    ''')
    ch = input("Enter your choice <1 or 2> :")
    if ch=='1':
        txt2bin()
    elif ch=='2':
        bin2txt()
    else:
        print("You entered something out of options 1 and 2.")
    again = input("\n<Enter r to run again> | <Any other key(except power button) to quit> :")
    if again=='r' or again=='R':
        continue
    else:
        print("Exiting...\n")
        break