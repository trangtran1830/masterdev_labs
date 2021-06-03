import numpy as np
from matplotlib import pyplot as plt
from numpy import random

def estimate():
	circle_points = 0
	square_points = 0
	number_sample = 10000
	samples = []
	for i in range(0, number_sample):
		rand_x = random.uniform(-1, 1)
		rand_y = random.uniform(-1, 1)
		origin_dist = rand_x**2 + rand_y**2
		if origin_dist <= 1:
			circle_points+= 1
		square_points+=1
		pi = 4 * circle_points / square_points
		samples.append(pi)
	statistic(samples)


def statistic(samples):
	print('Mean:', np.mean(samples))
	print('Variance:', np.var(samples))
	print('Standard Deviation:', np.std(samples))
	print('Median:', np.median(samples))
	print('Min:', np.min(samples))
	print('Max:', np.max(samples))
	print('Q1:', np.quantile(samples, 0.25))
	print('Q3:', np.quantile(samples, 0.75))
	plt.hist(samples, bins=[3.139, 3.140, 3.141, 3.142, 3.143, 3.144, 3.145])
	plt.show()

def main():
    estimate()

if __name__ == '__main__':
    main()