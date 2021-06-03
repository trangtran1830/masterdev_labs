import numpy as np
import time
import math
from numpy import random
import matplotlib.pyplot as plt

class Solution(object):
	#Solution 1
	#XOR all bits together to find the unique number.
	def singleNumber1(self, nums):
		a = 0
		for i in nums:
			a ^= i
		return a

	#Solution 2
	#2∗(a+b+c)−(a+a+b+b+c)=c2∗(a+b+c)−(a+a+b+b+c)=c        
	def singleNumber2(self, nums):
		return 2*sum(set(nums)) - sum(nums)

	def statistic(self, samples):
		print('Mean:', np.mean(samples))
		print('Variance:', np.var(samples))
		print('Standard Deviation:', np.std(samples))
		print('Median:', np.median(samples))
		print('Min:', np.min(samples))
		print('Max:', np.max(samples))
		print('Q1:', np.quantile(samples, 0.25))
		print('Q3:', np.quantile(samples, 0.75))
		plt.figure()
		plt.hist(samples)
		plt.show() 


def test_case():
	test_case_length = random.randint(20000, 50000)
	samples =[]
	i = 0
	if test_case_length % 2 == 0:
		test_case_length += 1
	unique = random.randint(1, test_case_length)
	for x in range(test_case_length):
		if x != unique:
			if i % 2 == 0:
				samples.append(x)
			samples.append(samples[i-1])
			i += 1
	samples.append(unique)
	return samples




def runtime(solution):
    time_list = []
    
    solution = Solution()
    for i in range(1000):
        start_time = time.time()
        samples = test_case()

        if(solution == 0):
        	print(solution.singleNumber1(samples))
        elif(solution == 1):
        	print(solution.singleNumber2(samples))

        end_time = time.time()
        time_list.append((time.time() - start_time)*1000)
    solution.statistic(time_list)



if __name__ == '__main__':
	runtime(0)
	
