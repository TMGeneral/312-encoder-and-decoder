inputCode = input("1655313161203121321504353124547\n")
trueIn = ""
inUnicode = False
bracketType = "open"
u = ""
trueIn = "000" + inputCode.replace("4", "11").replace("5", "22").replace("6", "33").replace("00", "998").replace("0", "000")
print(trueIn)
a = 0
b = ""
decoded = ""
capitalization = ""
capsDelay = 1
capSkip = 0
capsCheck = ["71","72","73"]
for i in range(len(trueIn)):
	try:
		j = trueIn[i+capSkip]
    except:
        break
    if a != 2:
        b += j
        a += 1
    else:
        b += j
        a = 0
        code = [111,112,113,121,122,123,131,132,133,211,212,213,221,222,223,231,232,233,311,312,313,321,322,323,331,332,181,182,183,281,282,283,381,382,383,118,117,227,337,127,217,237,317,711,712,713,721,722,723,171,272,373,811,812,813,821,822,823,000,999,998]
        characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0",".","?","!",",","-",";",":","@","#","/","%","¤","\\","'",'"',"(","+","_","*","÷","=","^"," ",")","\n"]
        if int(b) in code:
            ind = code.index(int(b))
            if ind == 60 or (ind == 58 and capitalization != "73"):
                capitalization = trueIn[i+capSkip+1:i+capSkip+3]
                if capitalization in capsCheck:
                    capSkip += 2
                else:
                    capitalization = ""
            if not inUnicode:
                if ind == 51:
                    if bracketType == "open":
                        bracketType = "close"
                    else:
                        ind = 59
                        bracketType = "open"
                if capitalization == "71":
                    decoded += characters[ind].upper()
                    if capsDelay == 1:
                        capsDelay -= 1
                    else:
                        capsDelay = 1
                        capitalization = ""
                elif capitalization == "72":
                    decoded += characters[ind].upper()
                    if capsDelay == 1:
                        capsDelay -= 1
                    else:
                        if ind > 25:
                            capsDelay = 1
                            capitalization = ""
                elif capitalization == "73":
                    decoded += characters[ind].upper()
                    if capsDelay == 1:
                        capsDelay -= 1
                    else:
                        if ind == 36 or ind == 37 or ind == 38 or ind == 42 or ind == 51 or ind == 59:
                            capsDelay = 1
                            capitalization == ""
                else:
                    decoded += characters[ind]
            else:
                u += characters[ind].upper()
        elif int(b) == 791:
            if not inUnicode:
                inUnicode = True
            else:
                inUnicode = False
                u = (8-len(u)) * "0" + u
                buffer = rf"\U{u}"
                decoded += buffer.encode().decode('unicode_escape')
        else:
            decoded += "\U00100000"
        b = ""
print(decoded[1:])
