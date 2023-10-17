# try:
#     You do your operation over here
# 
# except ErrorType1:
#     To catch if exception of type ErrorType1 will occour
#     
# except ErrorType2:
#     To catch if exception of type ErrorType2 will occour
# 
# except:
#     We could have also just said except: if we weren't sure what exception would occur.
# else:
#     If no exception, this block will get executed


def askinput():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")
        val = int(input("Try again-Please enter an integer: "))
    else:
        print("Looks like entered integer value is correct in try block!")
    finally:
        print("Finally, I executed!")
    print(val)

askinput()

