# mcc
## Project 2 - Minimum Coin Change

#### Make sure these files are in the same directory:
- mcc.py
- mcc_algos.py
- mcc_tests.py
- test.txt for default testing, if desired
- whatever .txt file you wish the test

#### For correctness testing with file input/output:

Usage: python mcc.py { all || changeslow || changegreedy || changedp } { filename.txt }
- For example, to run all algorithms on Amount.txt:
	- run the command: python mcc.py all Amount.txt
- This will create a new file everytime.

Each algorithm can be individually processed by using the algorithm name instead of all
- For example, to run changeslow on Amount.txt:
	- run the command: python mcc.py changeslow Amount.txt
- This will create a new file if one does not exist or append the results to the existing file.

If no filename argument is provided, mcc.py will run all three algorithms on test.txt.

Results for every command will be output to filenamechanges.txt. Please note that changeslow will have difficulty writing solutions for coin.txt because of the last problem set.

Note: If a filename argument is given, then either all, changeslow, changegreedy or changedp is required. 

#### For runtime and other extensive testing:
- Usage: python mcc_testing.py
