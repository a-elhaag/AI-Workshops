# 1. Printing  
print("Welcome to the Python for AI Workshop!")  

# ! ------------------------------------------------------
# 2. Input  
name = input("What is your name? ")  
print(f"Hello, {name}!")  

# ! ------------------------------------------------------  
# 3. Variables  
age = 25  
height = 5.9  
strings = "Hello, World!"

# ! ------------------------------------------------------
# 4. Lists and Dictionary  
my_list = [1, 2, 3, 4, 5]  
my_dict = {'name': 'Alice', 'age': 25}  

# ! ------------------------------------------------------ 
# 5. Tuples and Sets  
my_tuple = (1, 2, 3)  
my_set = {1, 2, 3, 4, 5}  

# ! ------------------------------------------------------
# 6. Difference between Lists, Tuples, and Sets  
print("Lists are mutable and ordered.")  
print("Tuples are immutable and ordered.")  
print("Sets are mutable and unordered.")  

# ! ------------------------------------------------------ 
# 7. If Conditions  
if age > 20:  
    print("You are older than 20.")  

# ! ------------------------------------------------------  
# 8. If-Else and Elif  
if height > 6:  
    print("You are tall.")  
elif height == 5.9:  
    print("You are of average height.")  
else:  
    print("You are short.")  

# ! ------------------------------------------------------ 
# 9. Working with Loops  
for i in my_list:  
    print(f"List item: {i}")  
  
i = 0  


while i < 3:  
    print(f"While loop iteration: {i}")  
    i += 1  

# ! ------------------------------------------------------  
# 10. Functions and Parameters  
def greet_person(person_name):  
    print(f"Hello, {person_name}!")  
  
greet_person(name)  

# ! ------------------------------------------------------
# 11. Working with Built-in Functions  
print(len(my_list))  
print(sum(my_list))  

  
# 12. Splitting Code Across Multiple Files  
# Assuming we have another Python file named 'helper.py' with function `def helper_func():`  
# from helper import helper_func  
# helper_func()  

# ! ------------------------------------------------------ 
# 13. Working with External Libraries (NumPy and Matplotlib)  
import numpy as np  
import matplotlib.pyplot as plt  
  
# NumPy example  
arr = np.array([1, 2, 3, 4, 5])  
print(f"NumPy array: {arr}")  
  
# Matplotlib example  
plt.plot(arr)  
plt.title("NumPy Array Plot")  
plt.show()  

# ! ------------------------------------------------------  
# 14. Rule-Based Chatbot  
def chatbot_response(user_input):  
    if "hello" in user_input.lower():  
        return "Hi there!"  
    elif "how are you" in user_input.lower():  
        return "I'm good, thank you!"  
    else:  
        return "I don't understand that."  
  
user_input = input("You: ")  
print(f"Chatbot: {chatbot_response(user_input)}")  

# ! ------------------------------------------------------   
# Cool Features  
print(f"Your name is {name} and you are {age} years old.")  
 
is_adult = True if age >= 18 else False  
print(f"Is adult: {is_adult}")  
