code = [111,112,113,121,122,123,131,132,133,211,212,213,221,222,223,231,232,233,311,312,313,321,322,323,331,332,181,182,183,281,282,283,381,382,383,118,117,227,337,127,217,237,317,711,712,713,721,722,723,171,272,373,811,812,813,821,822,823,0,00,373,]
characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0",".","?","!",",","-",";",":","@","#","/","%","¤","\\","'",'"',"(","+","_","*","÷","=","^"," ","\n",")"]
sentenceStoppers = [".", "!", "?", "(", ")", "\""]
inputV = input("enter text to turn into 312 (double space for a line feed.)\n")
inputV.replace("  ","\n")
buffer = ""
squish = ""
outputV = ""
inUnicode = False
unicodeBuffer = ""
print(inputV)
inputV = inputV.lower()
for i in inputV:
    if i in characters:
        index = characters.index(i)
        buffer += str(code[index])
    else:
        buffer += "791"
        inUnicode = True
        unicodeBuffer = f"{ord(i):08X}"
        nonZero = False
        for i in unicodeBuffer:
            if not nonZero:
                if i != "0":
                    nonZero = True
                    index = characters.index(i)
                    buffer += str(code[index])
            else:
                index = characters.index(i)
                buffer += str(code[index])
        inUnicode = False
        buffer += "791"
outputV = buffer.replace("11", "4").replace("22", "5").replace("33", "6")
print(outputV)
