import numpy as np
import matplotlib.pyplot as plt
import statistics as sts

list_of_numbers = list()

for i in range(np.random.randint(10, 50)):
    list_of_numbers.append(np.random.randint(1, 99)) # Generating data of random numbers

list_of_numbers_array = np.asarray(list_of_numbers)

print(list_of_numbers)
print('Length of data:', len(list_of_numbers))

print('Mean of the data:', round(np.mean(list_of_numbers_array), 2)) # Mean

print('Median of the data:', np.median(list_of_numbers_array)) # Median

print('Mode of the data:', sts.mode(list_of_numbers_array)) # Mode

print('Variance of the data:', round(np.var(list_of_numbers_array), 2)) # Variance

print('Standard Deviation of the data:', round(np.std(list_of_numbers_array), 2)) # Standard Deviation

figure = plt.figure(figsize = (10, 8))
plt.boxplot(list_of_numbers) # Box Plot
plt.show()