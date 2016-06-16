import string;
limit = 100; #change limit to whatever is necessary
binaries = [];

#generate binaries according to limit
limit_byte = str(bin(limit)[2:]);
stacker = 1;
for lim in limit_byte:
    binaries.append(stacker);
    stacker *= 2;
    
print(binaries);

def generateCards(motherValue): # x will be the binary and the return value is an array with all numbers which are on the binary card
    if motherValue not in binaries:
        return "ERROR - X not a binary";
    returnValue = "";
    
    byte = str(bin(motherValue)[2:]);
    while len(byte) < len(binaries):
        byte = "0" + byte;
        
    index = byte.index("1");    
    
    for testedValue in range(1,limit + 1):
        testedValue_STRING = str(bin(testedValue)[2:]);
        while len(testedValue_STRING) < len(binaries):
           testedValue_STRING = "0" + testedValue_STRING;
        
        try:
            if testedValue_STRING[index] == "1":
               returnValue += "," + str(testedValue);
        except :
            pass;
       
    return returnValue[1:];
    
def printCard(x):
    splits = x.split(",");
    counting = 0;
    line = "";
    for word in splits:
        counting += 1;
        line += " " + word;
        if not counting%7:
            line += "\n";
    print(line);        
        
        
def prompt(number, c):
    print("Is your number one of those (y/n) ?");
    printCard(generateCards(number));
    input1 = str(input());

    if input1 == "y":
        c = c + number;
    print("\n");    
    return c;    
    



counter = 0;    
print("Think of a number between 1 and "+ str(limit) +"\n");
for bi in binaries:
    counter = prompt(bi,counter);

print("Your number is: " + str(counter));
