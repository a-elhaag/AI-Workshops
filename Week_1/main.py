# Feel free to uncomment and play

# # 1. Printing  
# print("Welcome\"\n\t\\ to the Python for AI Workshop!")  

# ! ------------------------------------------------------
# 2. Input  
# name = input("What is your name? ") 
# # my_friend_name = input("What is your friend's name? ")
# print(f"Hello, {name}\nhow is {my_friend_name} doing?")  
# first_number = input("Enter the first number: ")
# second_number = input("Enter the second number: ")
# print(f"The sum of {first_number} and {second_number} is {float(first_number) + float(second_number)}")


# # ! ------------------------------------------------------  
# # 3. Variables  
# age = 25  # Integer "int"
# height = 5.9  # Float "float"
# strings = "Hello, World!" # String "str" 
# is_adult = True  # Boolean True or False "bool"
# bool_val= 5>6
# print(bool_val)

# # ! ------------------------------------------------------
# 4. Lists and Dictionary  
# my_list = [1, 7,2, 3, 4, 5]  
# my_list.append(6)
# my_list.remove(2)
# my_list.pop(0)
# my_list.insert(1, 7)
# my_list.sort()
# print(my_list)

# my_dict = {'name': 'Alice', 'age': 25, 25: 'Hello, World!'}  

# # ! ------------------------------------------------------ 
# # 5. Tuples and Sets  
# my_tuple = (1, 2, 3) 
# my_tuple = my_tuple + (4, 5)
# print(my_tuple)
# my_set = {1, 2, 3, 4, 5}  

# # ! ------------------------------------------------------
# # 6. Difference between Lists, Tuples, and Sets  
# print("Lists are mutable and ordered.")  
# print("Tuples are immutable and ordered.")  
# print("Sets are mutable and unordered.")  

# # ! ------------------------------------------------------ 
# # 7. If Conditions  
# age = 20
# if age > 20:
#     print("You are older than 20.")  

# # ! ------------------------------------------------------  
# 8. If-Else and Elif  
# height = 5.9
# if height > 6:  
#     print("You are tall.")  
# elif height == 5.9:  # Elif is short for "else if"
#     print("You are of average height.")  
# else:  
#     print("You are short.")  

# # ! ------------------------------------------------------ 
# # 9. Working with Loops  
# my_list = [1, 2, 3]
# for i in my_list:  # For each item in the list      # Same as foreach in C#
#     print(f"List item: {i}")  
# import time  
# i = 0  # Initialize a counter
# while i < 3:  
#     print(f"While loop iteration: {i}") 
#     i += 1  # Increment the counter # i = i + 1
     

# # ! ------------------------------------------------------  
# 10. Functions and Parameters  
# def greet_person(person_name):  
#     print(f"Hello, {person_name}!")  
  
# greet_person('Alice')  

# # ! ------------------------------------------------------
# 11. Working with Built-in Functions  
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))  
# print(sum(my_list))  

# # ! ------------------------------------------------------ 
# # 12. Splitting Code Across Multiple Files  
# # Assuming we have another Python file named 'helper.py' with function `def helper_func():`  
# # from helper import helper_func  
# # helper_func()  

# # ! ------------------------------------------------------ 
# 13. Working with External Libraries (NumPy and Matplotlib)  
# # Matplotlib example  
# plt.plot(arr, 'r--')  # Plot the array with red dashed line
# plt.title("NumPy Array Plot")  
# plt.xlabel("X-")
# plt.ylabel("Y-")
# plt.grid(True)  # Add grid lines
# plt.show()  

# # ! ------------------------------------------------------  
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

