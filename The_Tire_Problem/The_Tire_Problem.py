import math

def calculate_probability(mean: float, std_dev: float, number: int) -> float:
    """
    Calculates the probability of a number on a bell curve given the mean and standard deviation.

    Parameters:
    - mean: float
        The mean value of the bell curve.
    - std_dev: float
        The standard deviation of the bell curve.
    - number: int
        The number for which the probability is to be calculated.

    Returns:
    - float:
        The probability of the number on the bell curve.

    Raises:
    - ValueError:
        Raises an error if the standard deviation is zero or negative.
    """

    # Checking if the standard deviation is valid
    if std_dev <= 0:
        raise ValueError("Standard deviation should be positive.")

    # Calculating the z-score
    z_score = (number - mean) / std_dev

    # Calculating the probability using the cumulative distribution function (CDF)
    probability = (1 + math.erf(z_score / math.sqrt(2))) / 2

    return probability

# Example usage:
mean = 46000
std_dev = 8600

# # Calculating the probability for a specific number
# number = 40000
# probability = calculate_probability(mean, std_dev, number)
# print(f"The probability of the number {number} on the bell curve is {probability}.")

# Calculating the probabilities for numbers 1 to 40000

    
    
# Refund Amount

# Define the function to calculate the result of the math operation
def calculate_result(number):
    return (40000 - number) * 120 / 40000

# Create a loop to iterate over the numbers from 1 to 40000
for number in range(1, 40001):

    # Calculate the result of the math operation for the current number
    result = calculate_result(number)
    
    
    
    
probabilities = []
for number in range(1, 40001):
    probability = calculate_probability(mean, std_dev, number)
    probabilities.append(probability)


def cost(number):
    return (probability * 100 * calculate_result(number))


# Printing for numbers 1 to 40000
print("Probabilities:")
for number, probability in enumerate(probabilities, start=1):
    print(f"Number: {number}, Probability: {probability * 100}, Refund {calculate_result(number)}, Cost {cost(number)}")
    

# all_costs = []
# for number, probability in enumerate(probabilities, start=1):
#     all_costs.append(cost(number))

# print("Total number of costs:", len(all_costs))

total_cost = 0
for number, probability in enumerate(probabilities, start=1):
  cost_amount = cost(number)
  total_cost += cost_amount

print(total_cost)