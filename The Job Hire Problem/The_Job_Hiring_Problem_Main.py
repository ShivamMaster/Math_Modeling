import math
from random import randrange
import numpy as np
from scipy.stats import norm
import sys
import statistics



#Asks the user what method random sampling that they would like (select the first person that hit above a certain threshold or use the standard deviation and predict which on is the best based on probabilities)
# In this section of the Code, Sampling Method #1 is trying to pick the best applicant based on a minimum threshold that the user wants. So it would be the first applicant that has a score greater or equal to that number will be selected

print("Welcome to the Job Hiring Problem Program")
print("This program will help you decide which applicant to hire based on the scores that they have received")
print("Method 1: Select the first person that hits above a certain threshold")
print("Method 2: Use stats and normal distribution curves to figure out the best applicant")
SamplingMethod1 = input("Would you like do use Method 1? Type 'Y' for Yes and 'N' for No:   ")
print(SamplingMethod1)

if SamplingMethod1 in ("Y", "y"):
    SamplingMethod1Status = True
    SamplingMethod2Status = False
    SamplingMethod1Threshold = int(input("What would you like the minimum threshold to be for your applicants:  "))
elif SamplingMethod1 in ("N", "n"):
    SamplingMethod1Status = False
    SamplingMethod2 = input("Would you like do use Method 2? Type 'Y' for Yes and 'N' for No:   ")
    if SamplingMethod2 in ("Y", "y"):
        SamplingMethod2Status = True
        SamplingMethod1Status = False
        
    else:
        SamplingMethod2Status = False
        print("Error: You have not selected either methods. Please try again or contact Shivam regarding adding another method if you are not happy with the current 2 methods")
else:
    print ("Goodbye")
    sys.exit()


RunLoop = input ("How many times would you like to run the program?  ")
print(RunLoop)


Details = input("Would you like to see the details of the program? Type 'Y' for Yes and 'N' for No:   ")
if Details in ("Y", "y"):
    DetailsStatus = True
elif Details in ("N", "n"):
    DetailsStatus = False


for trial in range (int(RunLoop)):
    print ("Trial #", trial+1)
    
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
    if DetailsStatus == True:
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
        print ("The highest actual score for the applicants was ", str(highest_actual_score))
        for j in range (1,21):
            applicant_name2 = f"Applicant{j}"  # Construct the applicant variable name dynamically
            if int(globals()[applicant_name2]) >= highest_actual_score:  # Access the variable using its name
                print("The best applicant to hire was " + applicant_name2)
                actual_best_applicant = applicant_name2
        
        if actual_best_applicant == predicted_best_applicant:
            print ("This was a Successful run")
        else:
            print ("This was a Failed Run")
        
        





    # Method #2
    if SamplingMethod2Status == True:
    
        for k in range (1,6):
            applicant_name3 = f"Applicant{k}"  # Construct the applicant variable name dynamically
            if int(globals()[applicant_name3]) == 100:
                print("Immediately hire " + applicant_name3)
                break
            else:
                if DetailsStatus == True:
                    print (applicant_name3 + "has been rejected")



        # Defining various data points for making a custom CDF curve
        mean = statistics.mean({Applicant1, Applicant2, Applicant3, Applicant4, Applicant5})
        standard_deviation = statistics.stdev({Applicant1, Applicant2, Applicant3, Applicant4, Applicant5})
        lower_bound = 0
        upper_bound = 100
        
        if DetailsStatus == True:
            print("The mean of the first 5 applicants is ", str(mean))
            print ("The standard deviation of the first 5 applicants is ", str(standard_deviation))


        # THE CURVE/Probilities

        # Create the x-values for the CDF curve
        num_points = 1000  # Number of points to use for the curve
        x = [i * (upper_bound - lower_bound) / (num_points - 1) for i in range(num_points)]

        # Create the CDF curve using norm.cdf
        cdf = [norm.cdf(value, loc=mean, scale=standard_deviation) for value in x]

        # Loop through applicants 6 to 20 and calculate their area under the curve
        for a in range(6, 21):
            applicant_score4 = int(globals()[f"Applicant{a}"])
            # Find the index in x corresponding to the score (linear search)
            score_index = (
                min(range(len(x)), key=lambda i: abs(x[i] - applicant_score4))
            )
            area = cdf[score_index]  # Area under the curve is the CDF value at the index
            if DetailsStatus == True:
                print(f"Applicant {a}'s score: {applicant_score4}, Area under the curve: {area:.4f}")
            if area >= (standard_deviation + mean)/100:
                print ("Hire this applicant" + f"Applicant{a}")
                break
            applicant_name5 = "Applicant" + str(a)
            predicted_best_applicant5 = applicant_name5

            
        highest_actual_score = max({Applicant1, Applicant2, Applicant3, Applicant4, Applicant5, Applicant6, Applicant7, Applicant8, Applicant9, Applicant10, Applicant11, Applicant12, Applicant13, Applicant14, Applicant15, Applicant16, Applicant17, Applicant18, Applicant19, Applicant20})
        print ("The highest actual score for the applicants was ", str(highest_actual_score))
        predicted_best_applicant5 = None
        for j in range (1,21):
            applicant_name2 = f"Applicant{j}"  # Construct the applicant variable name dynamically
            if int(globals()[applicant_name2]) >= highest_actual_score:  # Access the variable using its name
                print("The best applicant to hire was " + applicant_name2)
                actual_best_applicant = applicant_name2
        
        if actual_best_applicant == predicted_best_applicant5:
            print ("This was a Successful run")
        else:
            print ("This was a Failed Run")
            
        
        





