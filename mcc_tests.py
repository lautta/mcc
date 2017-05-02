# MCC runtime testing with csv file writing


import csv
from timeit import default_timer as timer
from mcc_algos import *


def runtime(algo_type, V, low, high, runs):
	times = []
	for i in range(low, high + 1):
		total = 0
		for j in range(runs):
			start = timer()
			algo_type(V, i)
			end = timer()
			total += end - start

		average = total / runs
		times.append((i, average))
	return times


def minimum(algo_type, V, low, high):
	mins = []
	for i in range(low, high + 1):
		(min_change, min_count) = algo_type(V, i)
		mins.append((i, min_count))
	return mins


def get_data():
	V1 = [1, 2, 6, 12, 24, 48, 60]
	V2 = [1, 5, 10, 25, 50]
	V3 = [1, 6, 13, 37, 150]

	# Minimum coins for each A
	write_data('alg1_V1_1-35.csv', minimum(changeslow, V1, 1, 35))
	write_data('alg1_V2_1-35.csv', minimum(changeslow, V2, 1, 35))
	write_data('alg1_V3_1-35.csv', minimum(changeslow, V3, 1, 35))
	
	write_data('alg2_V1_1-50.csv', minimum(changegreedy, V1, 1, 50))
	write_data('alg2_V2_1-50.csv', minimum(changegreedy, V2, 1, 50))
	write_data('alg2_V3_1-50.csv', minimum(changegreedy, V3, 1, 50))
	
	write_data('alg2_V1_2000-2200.csv', minimum(changegreedy, V1, 2000, 2200))
	write_data('alg2_V2_2000-2200.csv', minimum(changegreedy, V2, 2000, 2200))
	write_data('alg2_V3_2000-2200.csv', minimum(changegreedy, V3, 2000, 2200))
	
	write_data('alg3_V1_1-50.csv', minimum(changedp, V1, 1, 50))
	write_data('alg3_V2_1-50.csv', minimum(changedp, V2, 1, 50))
	write_data('alg3_V3_1-50.csv', minimum(changedp, V3, 1, 50))
	
	write_data('alg3_V1_2000-2200.csv', minimum(changedp, V1, 2000, 2200))
	write_data('alg3_V2_2000-2200.csv', minimum(changedp, V2, 2000, 2200))
	write_data('alg3_V3_2000-2200.csv', minimum(changedp, V3, 2000, 2200))

	# Runtimes for each
	write_data('alg1_V2_runtimes.csv', runtime(changeslow, V2, 1, 35, 1))
	write_data('alg2_V2_runtimes.csv', runtime(changegreedy, V2, 1, 50, 5))
	write_data('alg3_V2_runtimes.csv', runtime(changedp, V2, 1, 50, 5))

	print('Wrote csv files...')


def write_data(filename, array):
	with open(filename, 'wb') as output:
		file_writer = csv.writer(output)
		for row in array:
			file_writer.writerow(row)


if __name__ == '__main__':
	get_data()
