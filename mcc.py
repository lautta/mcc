# MCC correctness tests with file read/write

from mcc_algos import *
import sys


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
			(change_result, count_result) = algo_func(value, amount)
			change_result = ' '.join([str(i) for i in change_result])
			output.write('\n%s\n%s\n' % (change_result, count_result))
		output.write('\n')
	print('Wrote %s to %s file...' % (algo_name, filename))


if __name__ == '__main__':

	if len(sys.argv) > 3 or len(sys.argv) == 2:
		print('Usage: python mcc.py { all || changeslow || changegreedy || changedp } { filename.txt }')
		exit(1)
	elif len(sys.argv) == 3:
		input_file = str(sys.argv[2])
		output_file = input_file.split('.')[0] + 'change.txt'
		algorithm = str(sys.argv[1])
		v, a = read_problems(input_file)

		if algorithm == 'changeslow':
			write_results(output_file, changeslow, 'changeslow', v, a, 'ab+')
		elif algorithm == 'changegreedy':
			write_results(output_file, changegreedy, 'changegreedy', v, a, 'ab+')
		elif algorithm == 'changedp':
			write_results(output_file, changedp, 'changedp', v, a, 'ab+')
		elif algorithm == 'all':
			write_results(output_file, changeslow, 'changeslow', v, a, 'wb')
			write_results(output_file, changegreedy, 'changegreedy', v, a, 'ab')
			write_results(output_file, changedp, 'changedp', v, a, 'ab')
		else:
			print('%s not recognized.\nUsage: python mcc.py { all || changeslow || changegreedy || changedp } { filename.txt }' % algorithm)
	else:
		input_file = 'test.txt'
		output_file = input_file.split('.')[0] + 'change.txt'
		v, a = read_problems(input_file)
		write_results(output_file, changeslow, 'changeslow', v, a, 'wb')
		write_results(output_file, changegreedy, 'changegreedy', v, a, 'ab')
		write_results(output_file, changedp, 'changedp', v, a, 'ab')
		print('Wrote all three algorithms to %s' % output_file)
