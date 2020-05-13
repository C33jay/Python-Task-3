
# coding: utf-8

# In[5]:


#Imports library
import random

#Function that generates random number
def Random_Number_generator(lowerLimit , upperLimit):
    Random_number = random.randint(lowerLimit, upperLimit)
    return Random_number



#Main program
print("Welcome to Miki Number Guessing Game")
print("Select a level.")
print("1. Easy")
print("2. Medium")
print("3. Hard")

#Prompts user to select a level
Select_level = input("Choose a Level: ").lower()
            
            
if Select_level == "easy":
    
    print("*** Easy Level  ***")
    print("In this level, you are expected to guess a number between 1 and 10. You have 6 chances. Goodluck!")
    
    
    Random_Number=Random_Number_generator(1,10)
    guess_count =0
    guess_chances = 6
    
     
    while guess_count < guess_chances:
        try:
            guess=int(input("Make a Guess: "))
            guess_count +=1
            if guess == int(Random_Number):
                print("You got it right!")
                break
            else:
                print("That was wrong!")
                print("You have " + str(guess_chances - guess_count)   + " chances left")
        except: 
                ValueError
                print("Wrong input! Enter a number.")
    else:
        print("Game Over!")
elif Select_level=="medium":
    print("***Medium Level  ***")
    print("In this level, you are expected to guess a number between 1 and 20. You have 4 chances. Goodluck!")
    
    
    Random_Number=Random_Number_generator(1,20)
    guess_count =0
    guess_chances = 4
   
    
    while guess_count < guess_chances:
        try:
            guess=int(input("Make a Guess: "))
            guess_count +=1
            if guess == Random_Number:
                print("You got it right!")
                break
            else:
                print("That was wrong!")
                print("You have " + str(guess_chances - guess_count) + " chances left")
        except:
                ValueError
                print("Wrong input! Enter a  number.")
    else:
        print("Game Over!")
elif Select_level =="hard":
    print("*** Hard Level  ***")
    print("In this level, you are expected to guess a number between 1 and 50. You have 3 chances. Goodluck!")
    
    
    Random_Number=Random_Number_generator(1,50)
    guess_count =0
    guess_chances = 3
    
    
    while guess_count < guess_chances:
        try:
            guess=int(input("Make a Guess: "))
            guess_count +=1
             
            
            if guess == Random_Number:
                print("You got it right!")
                break
            else:
                print("That was wrong!")
                print("You have " + str(guess_chances - guess_count) + " chances left")
        except:
            ValueError
            print("Wrong input! Enter a number.")
    else:
        print("Game Over!")

