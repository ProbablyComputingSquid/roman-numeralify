####
# ROMAN NUMERAL FINDER (all original code by @ComputingSquid on replit @ProbablyComputingSquid on github)
# NO DEPENDENCIES!!!
# Supports numbers, including numbers with commas up to 1,399,999
# Use with credit please
# or dont, i don't really care, and I wouldn't know anyways
####

# constants (ansi codes)
ol = "\033[53m"
dl = u"\u033f" # unused, unicode combining overline 
BOLD = "\033[1m"
RESET = "\033[0m"
red = "\033[31;1;4m"
# end constants

# overline overlines text
def overline(text):
    return ol + text + RESET

print(f"{BOLD}ROMAN NUMERAL CONVERTER!!!{RESET} (wow) {red}SPQR{RESET}")
print("supports numbers up to 1,399,999")
print("Note: in order to make it look better, ANSI overline is used instead of unicode overline cause that's a bit broken. that means you can't copypaste outputs sry :(")
print("commands\nexit/quit: exits the program\nclear: clears the screen")
# romanIt() is main function
def romanIt():
    userInput = ""
    validInput = False
    while not validInput:
        try:
            userInput = str(input("Enter a non-zero positive integer (supports commas!!!)\n>>>"))
            userInput = userInput.replace(",","") # makes commas work
            if userInput.isdigit() and int(userInput) > 0:
                
                if int(userInput) > 1399999:
                    print("too big :( Try again with a smaller number") 
                else:
                    validInput = True
            elif userInput == "exit" or userInput == "quit" or userInput == "e":
                return "done"
            elif userInput == "clear":
                print(f"{BOLD}ROMAN NUMERAL CONVERTER!!!{RESET} (wow) {red}SPQR{RESET}")
                print("supports numbers up to 1,399,999")
                print("\033[H\033[J")
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, get good")
    
    parsing = int(userInput)
    output = ""
    while parsing > 0:
        if False:
            pass
        elif parsing >= 1000000:
            parsing -= 10**6
            output+=overline("M")
        elif parsing >= 900000:
            parsing -= 900000
            output += overline("CM")
        elif parsing >= 500000:
            parsing-=500000
            output += overline("D")
        elif parsing >= 400000:
            parsing -= 400000
            output += overline("CD")
        elif parsing >= 100000:
            parsing -= 100000
            output += overline("C")
        elif parsing >= 90000:
            parsing -= 90000
            output += overline("XC")
        elif parsing >= 50000:
            parsing -= 50000
            output += overline("L")
        elif parsing >=40000:
            parsing -= 40000
            output += overline("XL")
        elif parsing >= 10000:
            parsing -= 10000
            output += overline("X")
        elif parsing >= 9000:
            parsing -= 9000
            output += overline("IX")
        elif parsing >= 5000:
            parsing -= 5000
            output += overline("V")
        elif parsing >= 4000:
            parsing -= 4000
            output += overline("IV")
        elif parsing >= 1000:
            parsing -= 1000
            output+="M"
        elif parsing >= 900:
            parsing -= 900
            output+="DM"
        elif parsing >= 500:
            parsing-=500
            output +="D"
        elif parsing >= 400:
            parsing -= 400
            output += "CD"
        elif parsing >= 100:
            parsing -=100
            output += "C"
        elif parsing >= 90:
            parsing -= 90
            output += "XC"
        elif parsing >= 50:
            parsing -= 50
            output += "L"
        elif parsing >= 40:
            parsing -= 40
            output += "XL"
        elif parsing >= 10:
            parsing -= 10
            output += "X"
        elif parsing == 9:
            parsing -= 9
            output += "IX"
        elif parsing >= 5:
            parsing -= 5
            output += "V"
        elif parsing == 4:
            parsing -= 4
            output += "IV"
        elif parsing >= 1:
            parsing -= 1
            output += "I"
        else:
            print("An error has occurred.\nPlease contact HR and tell them to fire the dev responsible for this error")
            break
    
    print(f"Output: {output}")


while True:
    if romanIt() == "done":
        print("Thanks for using roman numeral converter!")
        break
