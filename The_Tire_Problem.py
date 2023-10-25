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

# Calculating the probability for a specific number
number = 40000
probability = calculate_probability(mean, std_dev, number)
print(f"The probability of the number {number} on the bell curve is {probability}.")

# Calculating the probabilities for numbers 1 to 40000
probabilities = []
for number in range(1, 40001):
    probability = calculate_probability(mean, std_dev, number)
    probabilities.append(probability)

# Printing the probabilities for numbers 1 to 40000
print("Probabilities:")
for number, probability in enumerate(probabilities, start=1):
    print(f"Number: {number}, Probability: {probability}")