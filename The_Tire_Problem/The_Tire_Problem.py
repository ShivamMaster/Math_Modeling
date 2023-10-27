import math
import numpy as np
from scipy.stats import norm


# Define varibles for user to input thier needed numbers
mean = 46000
std_dev = 8600



# Probailities of each number:

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
print("Probabilities:")
for number, probability in enumerate(probabilities, start=1):
    print(f"Number: {number}, Probability: {probability * 100}, Refund {calculate_result(number)}, Cost {cost(number)}")
    






# Average cost for each tire
total_cost = 0
for number, probability in enumerate(probabilities, start=1):
  cost_amount = cost(number)
  total_cost += cost_amount

print(total_cost/40000)