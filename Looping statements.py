'''Looping statements in Python are used to repeat a block of code multiple times.
             
                          
              "for Loop vs while Loop"

Feature  	  for Loop	                                                    while Loop

Use Case	When you know in advance                                       When you don’t know 
            how many times to loop                                         how many times to loop                     
                
           
Syntax	    for variable in sequence:	                                   while condition:
                 

Condition       Automatically handled by range() or sequence length        Manually written as a condition
Checking	         
         
            
Best For	Iterating over lists, strings, ranges, etc.             	   Looping until a condition becomes false

'''



# For Loops


# Calculating Total Price from a Shopping Cart

cart_prices = [120,150,160,90]
total = 0

for price in cart_prices:
    total += price
    
print(total)     

#  Counting How Many Times a Word Appears

sentence = "python is easy and python is fun"
word_count = 0

for word in sentence.split():
    if word == "easy":
        word_count += 1
                     
print(word_count)        


# Checking Student Pass/Fail Status

students = {"Abhi" : 80,"Raj" : 70,"jack" : 30}

for name,marks in students.items():    # .items() returns pairs of (key, value) → (name, marks)
    if marks >35:
        print(f"{name},Passed")
    else:
        print(f"{name},Failed")
        


# Renaming Files in a Folder (with placeholders)

files = ["image1.jpg","image2.jpg","image3.jpg"]

for index,file in enumerate(files,start=1):
    new_name = f"Abhi_pic_{index}.jpg"
    print(f"renaming {file} to {new_name}")







# While Loops


# ATM Pin Attempts (Max 3 Tries)


# correct_pin = "1289"
# tries = 0

# while tries<3:
#     entered = input("Enter ATM pin: ")
#     if entered == correct_pin:
#         print("Access is granted")
#         break
#     else:
#         print("Access denied")
#         tries += 1
# if tries == 3:
#     print("Card blocked")



# basic

count = 0
while count < 5 :
    print(count)
    count += 1
   
        
# Countdown using while

# i = 5
# while i > 0:
#     print(i)
#     i -= 1
# print("done")

 # while loop with continue
 
# n = 0
# while n < 5:

#     n += 1
#     if n == 3:
#        continue
#     print(n)
    
    
#  while loop with break

a = 0
while a < 10:
    a += 1
    if a == 7:
        break
    print(a)