import numpy as np

np.random.seed(4151)

#Part 1

#Problem 1.3

# Compute the number of votes for candidate A given a binomial distribution with n=30 and p=0.6
# Divide votes by 30 for p-hat


successes = np.random.binomial(n=30, p=0.6)
print(f"P-hat = {successes/30}")
print(f"Confidence interval: {0.6-1.96*(0.6*0.4/30)**0.5} <= p <= {0.6+1.96*(0.6*0.4/30)**0.5}")

#Problem 1.5

# Create a factorial function in order to be able to compute the CDF for a binomial distribution

def factorial(n):
    if n == 1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

sum=0

# Store the value of 500! since it might take a while to compute

# I'm looking for P(X<=500), so I need to take the sum from i = 0 to i = N of (N choose i)*(p^i)*(1-p)^(N-i)

N_factorial = factorial(500)

for i in range(501):
    sum+=(N_factorial)/(factorial(i)*factorial(500-i))*(0.6**i)*(0.4**(500-i))
print(sum)

# Problem 1.6

# We sample from a binomial distribution with n=1000 and p=0.6 to find 
p_hat = np.random.binomial(n=1000, p=0.6)/1000
print(f"p-hat = {p_hat}")

# Probelm 1.7

p_normal_guess = np.random.normal(p_hat, p_hat*(1-p_hat)/1000)
print(f"Initial guess {p_normal_guess}")
p_normal_guesses = np.random.normal(p_hat, p_hat*(1-p_hat)/1000, size=1000)
print(f"Average of 1000 guesses: {np.mean(p_normal_guesses)}")

# Part 1 Bonus

