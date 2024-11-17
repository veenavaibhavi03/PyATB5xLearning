#match is same as switch in java
# applicable when python >13 version
#match  variable:
         # case pattern 1:
               #code block
        # case pattern 2:
                # code block

#write a program to ask the user which browser they want to run automation.

browser_input=input("Enter the browser name \n")
match browser_input:
    case "Firefox":
        print("Starting firefox")
    case "chrome":
        print("Starting chrome")
    case "safari":
        print("starting safari")
    case "Edge":
        print("starting edge")
    case _:
        print("Browser not found !")
