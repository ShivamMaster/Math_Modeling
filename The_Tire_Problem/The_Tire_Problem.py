import math
import numpy as np
from scipy.stats import norm


# Define varibles for user to input thier needed numbers
mean = 46000   # Mean life of a tire
std_dev = 8600  # Standard Deviation of life of a tire 
lower_bound = 0  # Minimum Miles Driven under the guarantee from the company
upper_bound = 40000  # Maximum Miles Driven under the guarantee from the company
details = True    # Whether or not to print the details/calculations of the program



# Probability of each number:

def calculate_probability(mean: float, std_dev: float, number: int) -> float:

    # Checking if the standard deviation is valid
    if std_dev <= 0:
        raise ValueError("Standard deviation should be positive.")

    # Calculating the z-score
    z_score = (number - mean) / std_dev

    # Calculating the probability using the cumulative distribution function (CDF)
    probability = (1 + math.erf(z_score / math.sqrt(2))) / 2

    return probability

probabilities = []
for number in range(1, 40001):
    probability = calculate_probability(mean, std_dev, number)
    probabilities.append(probability)


    
    
    
    
# Refund Amount:

# Calulated the refund amount for each number
def calculate_result(number):
    return (40000 - number) * 120 / 40000

# Create a loop to iterate over the numbers from 1 to 40000
for number in range(1, 40001):
    result = calculate_result(number)
    
    





# Calcuating the cost for the manufactoring company (our company)
def cost(number):
    return (probability * 100 * calculate_result(number))





# Printing for numbers 1 to 40000

if details == True:
    print("Probabilities:")
    for number, probability in enumerate(probabilities, start=1):
        print(f"Number: {number}, Probability: {probability * 100}, Refund {calculate_result(number)}, Cost {cost(number)}")
    






# Average cost for each tire (not including the probability of when a tire will fail)
total_cost = 0
for number, probability in enumerate(probabilities, start=1):
  cost_amount = cost(number)
  total_cost += cost_amount

average_cost_raw = total_cost/40000
if details == True:
    print("The raw average cost of a tire, when not including when the tires are likely to fail is {}".format(average_cost_raw))







# Finding Area Under Normal Curve to predict the tire fail rate


def find_area_under_normal_curve(mean, std_dev, lower_bound, upper_bound):
  

  # Calculate the cumulative distribution function (CDF) at the two bounds.
  cdf_lower = norm.cdf(lower_bound, loc=mean, scale=std_dev)
  cdf_upper = norm.cdf(upper_bound, loc=mean, scale=std_dev)

  # The area under the curve between the two bounds is the difference between the two CDF values.
  area = cdf_upper - cdf_lower

  return area

area = find_area_under_normal_curve(mean, std_dev, lower_bound, upper_bound)

if details == True:
    print("The area under the normal distribution curve between {} and {} is {}".format(lower_bound, upper_bound, area))






# General Cost for the Company:

general_cost = average_cost_raw * area


print("The program will generally cost the company ${} for every tire sold".format(general_cost))

