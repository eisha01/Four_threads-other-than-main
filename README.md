# Four_threads-other-than-main
create four threads other than main thread.
1. Input thread
2. Reverse thread
3. Capital thread
4. Shift thread

Input thread will take string input from user, reverse thread will reverse the string and output it,
capital thread will capitalize the characters of string and output it and shift thread will shift each
characters of the string two time (e.g. a will become c) and output it.
# 1-INPUT THREAD:
we have used The time.sleep() function is used in threading to pause the execution of a thread for a specified number of seconds.And then we have used The join() method is used in Python's threading module to block the execution of the main thread until the thread on which the join() method is called has completed.

# 4-SHIFTING THREAD:
This code will create a new thread that will run the shift_thread function in the background. The shift_thread function takes a string and a shift value as arguments and returns a new string with each letter shifted by the specified number of places.
For example, if the input string is "hello" and the shift value is 1, the function will return "ifmmp". 

