# MCC correctness tests with file read/write

from mcc_algos import *


def read_problems(filename):
	values = []
	amounts = []
	line_number = 0
	with open(filename, 'r') as input:
		for line in input:
			line_number += 1
			if line_number % 2 == 1:
				value = [int(number) for number in line.strip().split()]
				values.append(value)
			else:
				amounts.append(int(line))
	print('Read %s file...' % filename)
	return values, amounts


def write_results(filename, algo_func, algo_name, values, amounts, write_option):
	with open(filename, write_option) as output:
		output.write('Algorithm %s:\n' % algo_name)
		for value, amount in zip(values, amounts):
			output.write(' '.join([str(i) for i in value]))
			if algo_func == changeslow and amount - sum(value) > 70:
				output.write('\nERROR\nERROR\n')
			else:
				(change_result, count_result) = algo_func(value, amount)
				change_result = ' '.join([str(i) for i in change_result])
				output.write('\n%s\n%s\n' % (change_result, count_result))
		output.write('\n')


if __name__ == '__main__':
	input_file = 'coins.txt'
	output_file = 'coinschange.txt'

	v, a = read_problems(input_file)
	write_results(output_file, changeslow, 'changeslow', v, a, 'wb')
	write_results(output_file, changegreedy, 'changegreedy', v, a, 'ab')
	write_results(output_file, changedp, 'changedp', v, a, 'ab')

	print('Wrote %s file...' % output_file)