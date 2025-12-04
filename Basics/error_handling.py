def ask_for_input():

    # Loop until the user provides a valid number
    
    while True:
        
        try:
            n = int(input("Enter a number : "))
            
        # Runs if conversion fails (user did not enter a number)  
        except: 
            print("OOPS ! That's not a number")

        # Runs only when there is no error in try block
        else:   
            print("That's correct")
            break   # Exit the loop because valid input is received

        # This block always runs whether an error occurred or not
        finally:  
            print("I will always run at the end")
            
    print("The number entered : ",n)
    
ask_for_input()

"""
This program demonstrates the use of try–except–else–finally in Python.

try:
    → Code that might cause an error is written here.
except:
    → Runs only if an error occurs in the try block.
else:
    → Runs only when no error occurs in the try block (skipped if except runs).
finally:
    → Always runs whether an error happens or not.
       Mostly used for cleanup tasks (closing files, releasing resources, etc.)

Key points to remember:
• Only one of except or else will run — never both.
• finally always runs at the end — whether try succeeded or failed.
• Use try–except only around code that might fail, not for everything.
• Use else when you want to run some code only if no error occurred.
• Use finally when something must run no matter what.

This avoids program crashes and gives better control over error handling.
"""
