import math
import numpy as np
from scipy.stats import norm


# Define varibles for user to input thier needed numbers
mean = 46000   # Mean life of a tire
std_dev = 8600  # Standard Deviation of life of a tire
details = True    # Whether or not to print the details/calculations of the program
lower_bound = 0  # Minimum Miles Driven under the guarantee from the company
upper_bound = 40000  # Maximum Miles Driven under the guarantee from the company


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

# Find the difference between each of the calculated probabilities
probability_differences = []
for i in range(len(probabilities) - 1):
    probability_difference = probabilities[i + 1] - probabilities[i]
    probability_differences.append(probability_difference)


# Refund Amount:

# Calulated the refund amount for each number
def calculate_result(number):
    return ((40000 - number) * 120 / 40000)


# Create a loop to iterate over the numbers from 1 to 40000
for number in range(1, 40001):
    result = calculate_result(number)


# Cost:

# Calcuating the cost for the manufactoring company (our company)
def cost(number):
    return (probability * calculate_result(number))


# Final/Main Printing on the Terminal (Part 1):
# Printing all the detail for numbers 1 to 40000
if details == True:
    print("Probabilities:")
    for number, probability in enumerate(probabilities, start=1):
        print(
            f"Mile Number: {number}, Probability: {probability_difference}, Refund {calculate_result(number)}, Cost {cost(number)}")


# Final/Main Printing on the Terminal (Part 2):


# Sum all of the costs
total_cost = 0
for number in range(1, 40001):
    total_cost += cost(number)


# Print the total cost
print("The average cost for the company is ${} per tire for a failed tire".format(
    total_cost/40000))


# Final/Main Printing on the Terminal (Part 3):


# Finding Area Under Normal Curve to predict the tire fail rate


def find_area_under_normal_curve(mean, std_dev, lower_bound, upper_bound):

    # Calculate the cumulative distribution function (CDF) at the two bounds.
    cdf_lower = norm.cdf(lower_bound, loc=mean, scale=std_dev)
    cdf_upper = norm.cdf(upper_bound, loc=mean, scale=std_dev)

    # The area under the curve between the two bounds is the difference between the two CDF values.
    area = cdf_upper - cdf_lower

    return area


area = find_area_under_normal_curve(mean, std_dev, lower_bound, upper_bound)


final = (total_cost/40000)*area

# Print the average cost for all tires sold
print("The average cost for the company is ${} per tire for all tires sold".format(final))
