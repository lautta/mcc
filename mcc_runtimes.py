# MCC runtime testing with csv file writing

import random
import csv
from timeit import default_timer as timer
from mcc_algos import *


def runtime(algo_type, V, start, end):
	times = []
	for i in range(start, end + 1):
		total = 0
		start = timer()
		algo_type(V, i)
		end = timer()
		total += end - start
		times.append((i, total))
	return times


def get_runtimes():
	V1 = [1, 2, 6, 12, 24, 48, 60]
	V2 = [1, 5, 10, 25, 50]
	V3 = [1, 6, 13, 37, 150]
	
	write_times('alg1_V1_1-35.csv', runtime(changeslow, V1, 1, 35))
	write_times('alg1_V2_1-35.csv', runtime(changeslow, V2, 1, 35))
	write_times('alg1_V3_1-35.csv', runtime(changeslow, V3, 1, 35))
	
	write_times('alg3_V1_1-50.csv', runtime(changedp, V1, 1, 50))
	write_times('alg3_V2_1-50.csv', runtime(changedp, V2, 1, 50))
	write_times('alg3_V3_1-50.csv', runtime(changedp, V3, 1, 50))
	
	write_times('alg3_V1_2000-2200.csv', runtime(changedp, V1, 2000, 2200))
	write_times('alg3_V2_2000-2200.csv', runtime(changedp, V2, 2000, 2200))
	write_times('alg3_V3_2000-2200.csv', runtime(changedp, V3, 2000, 2200))
	
	print('Wrote csv runtime files...')


def write_times(filename, array):
    with open(filename, 'wb') as output:
        file_writer = csv.writer(output)
        for row in array:
            file_writer.writerow(row)


if __name__ == '__main__':
    get_runtimes()
