import numpy as np
import scipy.stats as stats

def probability(number, mean, standard_deviation):
  """Calculates the probability of a specific number occurring from 1-40000 on a bell curve, given that the mean = 46,000 and standard deviation is 8600.

  Args:
    number: The number to calculate the probability for.
    mean: The mean of the bell curve.
    standard_deviation: The standard deviation of the bell curve.

  Returns:
    The probability of the number occurring.
  """

  z_score = (number - mean) / standard_deviation
  return stats.norm.cdf(z_score)

Num1 = 1

while Num1 < 40001:
  probability = probability(Num1, 46000, 8600)
  
  # Print the probability.
  print(probability)
  Num1 += 1
