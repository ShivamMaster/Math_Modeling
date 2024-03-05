import math
from random import randrange
import numpy as np
from scipy.stats import norm
import sys



#Asks the user what method random sampling that they would like (select the first person that hit above a certain threshold or use the standard deviation and predict which on is the best based on probabilities)
# In this section of the Code, Sampling Method #1 is trying to pick the best applicant based on a minimum threshold that the user wants. So it would be the first applicant that has a score greater or equal to that number will be selected



# name = input("What is your name? ")
# age = int(input("How old are you? "))  # Convert number to integer

# print("Hello, " + name + "! You are " + str(age) + " years old.")

SamplingMethod1 = input("Would you like do use the method of selecting the first person that hits above a certain threshold? Type 'Y' for Yes and 'N' for No:   ")
print(SamplingMethod1)

if SamplingMethod1 in ("Y", "y"):
    SamplingMethod1Status = True
    SamplingMethod1Threshold = int(input("What would you like the minimum threshold to be for your applicants:  "))
elif SamplingMethod1 in ("N", "n"):
    SamplingMethod1Status = False
    SamplingMethod2 = input("Would you like do use the method of basically auto-rejecting applicant #1 and then using stats and normal distribution curves to figure out the best applicant? Type 'Y' for Yes and 'N' for No:   ")
    if SamplingMethod2 in ("Y", "y"):
        SamplingMethod2Status = True
        
    else:
        SamplingMethod2Status = False
        print("Error: You have not selected either methods. Please try again or contact Shivam regarding adding another method if you are not happy with the current 2 methods")
else:
    print ("Goodbye")
    sys.exit()







# Random Assigns the scores of the Applicants:
Applicant1 = randrange(1,100)
Applicant2 = randrange(1,100)
Applicant3 = randrange(1,100)
Applicant4 = randrange(1,100)
Applicant5 = randrange(1,100)
Applicant6 = randrange(1,100)
Applicant7 = randrange(1,100)
Applicant8 = randrange(1,100)
Applicant9 = randrange(1,100)
Applicant10 = randrange(1,100)
Applicant11 = randrange(1,100)
Applicant12 = randrange(1,100)
Applicant13 = randrange(1,100)
Applicant14 = randrange(1,100)
Applicant15 = randrange(1,100)
Applicant16 = randrange(1,100)
Applicant17 = randrange(1,100)
Applicant18 = randrange(1,100)
Applicant19 = randrange(1,100)
Applicant20 = randrange(1,100)





# Printed the Applicant's scores to make it easier to track
print("Applicant 1's score is:", Applicant1)
print("Applicant 2's score is:", Applicant2)
print("Applicant 3's score is:", Applicant3)  
print("Applicant 4's score is:", Applicant4)
print("Applicant 5's score is:", Applicant5)
print("Applicant 6's score is:", Applicant6)
print("Applicant 7's score is:", Applicant7)
print("Applicant 8's score is:", Applicant8)
print("Applicant 9's score is:", Applicant9)  
print("Applicant 10's score is:", Applicant10)
print("Applicant 11's score is:", Applicant11)
print("Applicant 12's score is:", Applicant12)
print("Applicant 13's score is:", Applicant13)
print("Applicant 14's score is:", Applicant14)
print("Applicant 15's score is:", Applicant15)  
print("Applicant 16's score is:", Applicant16)
print("Applicant 17's score is:", Applicant17)
print("Applicant 18's score is:", Applicant18)
print("Applicant 19's score is:", Applicant19)
print("Applicant 20's score is:", Applicant20)




#Method #1
if SamplingMethod1Status == True:
    for i in range (1,21):
        applicant_name = f"Applicant{i}"  # Construct the applicant variable name dynamically
        if int(globals()[applicant_name]) >= SamplingMethod1Threshold:  # Access the variable using its name
            print("Hire" + applicant_name)
            break
        





# # Method #2
# if SamplingMethod2Status == True:
#     # Applicant #1's decision
#     if Applicant_1 == 100:
#         print("Applicant 1 has been selected do not care about no else")
#     else:
#         print ("Applicant 1 has not been selected and has been reject :(")







