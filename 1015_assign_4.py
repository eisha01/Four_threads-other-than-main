
import threading
import time
entered_input = False


def Input_thread():
    time.sleep(5)
    
    if entered_input == True:
        exit(0)
    else:
        print("timeout try running again")
        exit(0)

def Reverse_thread():
    print("The reverse of the string that you have entered is:"+ str(my_string)[::-1])


def Capitalize_thread():
    print("After capitalizing the string:"+ my_string.capitalize())

def Shift_thread(string, shift):
   shifted_string = ""
   for letter in string:
        shifted_string += chr((ord(letter) - 97 + shift) % 26 + 97)
        return shifted_string
   
def main():
        print("all the functions have been implemented ")
t = threading.Thread(target=Input_thread)
t2=threading.Thread(target=Reverse_thread)
t3=threading.Thread(target=Capitalize_thread)
t4=threading.Thread(target=Shift_thread,args=("eisha",2))




t.start()
print("enter string to start implementing functions: ")
my_string = str(input())
entered_input = True

print("the string that you have entered is:"+ str(my_string))
t.join(timeout=5)

t2.start()
t2.join()
time.sleep(3)
t3.start()
t3.join
time.sleep(3)
t4.start()
print(Shift_thread("eisha", 2))
t4.join()

if __name__ == "__main__":
    main()

exit(0)

