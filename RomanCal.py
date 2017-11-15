import re

##-------dictionary to hold number and their respective roman numerals-------##
rom = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
       50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


mRegExRomNum = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
mRegExOperator = r'([+*/-]){1}'

##--------method to convert roman numeral to number -----##
def romanToNumeric(romanNumber):
    if(re.match(mRegExRomNum, romanNumber.strip(), re.IGNORECASE)):
        romanNumber = romanNumber.upper()
        FinalNumber=0
        for num, romvalue in rom.items():
            while romanNumber.startswith(romvalue):
                FinalNumber += num
                romanNumber = romanNumber[len(romvalue):]
               
        return FinalNumber


##--------method to convert number to roman numeral -----##
def numricToRoman(number):
    result = ""
    temp = int(number)
    if numberValidation(temp) == True:
        if temp ==0:
            return "Output--->> nulla (zero is not defined in Roman Numerals"
        for num, romval in rom.items():
            while temp >= num:
                result += romval
                temp -= num
               
        if temp != 0:
            result += romval
        #print(result)
        return result

##--------method to validate operator r -----##
def operatorValidation(operation):
    operation = str(operation).strip()
    if len(operation) == 0:
        print("you have entered no operator")
        return False
    if len(operation) > 1:
        print("typed more than once")
        return False
   
    if (re.match(mRegExOperator, operation, re.IGNORECASE)):
        return True
    else:
        print("Opeator is not given")
        return False


##--------method to validate numbers as only between 0 and 5000 can be calculated  -----##
def numberValidation(n):
    if(n<0 or n>4999 ):
        print("numbers out of range")
        return False
        
    else:
       return True	


##--------method to do calculations -----##
def romanCalc(romanNumber1,operation,romanNumber2):
    num1 = romanToNumeric(romanNumber1)
    num2 = romanToNumeric(romanNumber2)
    print("Numbers are--->>",romanNumber1,romanNumber2)
    if operatorValidation(operation):
        
        if operation == "+":
            calOutput = num1 + num2
            return numricToRoman(calOutput)
        elif operation == "-":
            calOutput = num1 - num2
            
            return numricToRoman(calOutput)
        elif operation == "/":
            try:
              calOutput = num1 / num2
              return numricToRoman(calOutput)
            except Exception as e:
                print("Exception",e)

        elif operation == "*":
            calOutput = num1 * num2
            return numricToRoman(calOutput)


print(romanCalc("v", "/", "v"))

mRomanNum1 = input("Please enter FIRST roman number ->") 
mRomanNum2 = input("Please enter SECOND roman number ->") 
mOperator = input("Please enter an Operation like +,-,\/,*  ->") 
print("Output--->>", romanCalc(mRomanNum1, mOperator, mRomanNum2))

