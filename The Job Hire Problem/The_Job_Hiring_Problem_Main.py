import math
from random import randrange
import numpy as np
from scipy.stats import norm
import sys
import statistics



#Asks the user what method random sampling that they would like (select the first person that hit above a certain threshold or use the standard deviation and predict which on is the best based on probabilities)
# In this section of the Code, Sampling Method #1 is trying to pick the best applicant based on a minimum threshold that the user wants. So it would be the first applicant that has a score greater or equal to that number will be selected


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
    
    # Method #1 of picking the best applicant
    for i in range (1,21):
        applicant_name1 = f"Applicant{i}"  # Construct the applicant variable name dynamically
        if int(globals()[applicant_name1]) >= SamplingMethod1Threshold:  # Access the variable using its name
            print("According to this way of finding the applicant, we should hire " + applicant_name1)
            predicted_best_applicant = applicant_name1
            break
            

    highest_actual_score = max({Applicant1, Applicant2, Applicant3, Applicant4, Applicant5, Applicant6, Applicant7, Applicant8, Applicant9, Applicant10, Applicant11, Applicant12, Applicant13, Applicant14, Applicant15, Applicant16, Applicant17, Applicant18, Applicant19, Applicant20})
    print (highest_actual_score)
    for j in range (1,21):
        applicant_name2 = f"Applicant{j}"  # Construct the applicant variable name dynamically
        if int(globals()[applicant_name2]) >= highest_actual_score:  # Access the variable using its name
            print("The best applicant to hire was " + applicant_name2)
            actual_best_applicant = applicant_name2
    
    if actual_best_applicant == predicted_best_applicant:
        print ("Successful run")
    else:
        print ("Failed Run")
    
    





# Method #2
if SamplingMethod2Status == True:
   
    for k in range (1,6):
         applicant_name3 = f"Applicant{k}"  # Construct the applicant variable name dynamically
         if int(globals()[applicant_name3]) == 100:
             print("Immediately hire " + applicant_name3)
             break
         else:
             print (applicant_name3 + "has been rejected")



    # Defining various data points for making a custom CDF curve
    mean = statistics.mean({Applicant1, Applicant2, Applicant3, Applicant4, Applicant5})
    standard_deviation = statistics.stdev({Applicant1, Applicant2, Applicant3, Applicant4, Applicant5})
    lower_bound = 0
    upper_bound = 100
    
    print("The mean of the first 5 applicants is ", str(mean))
    print ("The standard deviation of the first 5 applicants is ", str(standard_deviation))


    # THE CURVE/Probilities

    # Create the x-values for the CDF curve
    num_points = 100000  # Number of points to use for the curve
    x = [i * (upper_bound - lower_bound) / (num_points - 1) for i in range(num_points)]

    # Create the CDF curve using norm.cdf
    cdf = [norm.cdf(value, loc=mean, scale=standard_deviation) for value in x]

    # Loop through applicants 6 to 20 and calculate their area under the curve
    for i in range(6, 21):
        applicant_score4 = int(globals()[f"Applicant{i}"])
        # Find the index in x corresponding to the score (linear search)
        score_index = (
            min(range(len(x)), key=lambda i: abs(x[i] - applicant_score4))
        )
        area = cdf[score_index]  # Area under the curve is the CDF value at the index
        print(f"Applicant {i}'s score: {applicant_score4}, Area under the curve: {area:.4f}")
        if area >= (standard_deviation + mean)/100:
            print ("Hire this applicant" + f"Applicant{i}")
            predicted_best_applicant = f"Applicant{i}"
            break
        
    highest_actual_score = max({Applicant1, Applicant2, Applicant3, Applicant4, Applicant5, Applicant6, Applicant7, Applicant8, Applicant9, Applicant10, Applicant11, Applicant12, Applicant13, Applicant14, Applicant15, Applicant16, Applicant17, Applicant18, Applicant19, Applicant20})
    print (highest_actual_score)
    for j in range (1,21):
        applicant_name2 = f"Applicant{j}"  # Construct the applicant variable name dynamically
        if int(globals()[applicant_name2]) >= highest_actual_score:  # Access the variable using its name
            print("The best applicant to hire was " + applicant_name2)
            actual_best_applicant = applicant_name2
    
    if actual_best_applicant == predicted_best_applicant:
        print ("Successful run")
    else:
        print ("Failed Run")
        
    
    



# Todo: 

# 2. With the part of the code that asks the user what method they want to use, maybe shorten the decision a little or maybe put some of the description in the comments. Or have multiple print commands (like some with the decription and then it was straight up ask which method they want)

# 4. Get it to loop through mutiple trials (we can ask the user how many trials that they want to run)
# 5. Record each trial data and have it spit it out and calcuate the sucess rate
# 6. Add an option that will ask the user if they want to see the applicant's scores for each trial 



