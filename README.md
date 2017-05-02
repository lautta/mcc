# mcc
Project 2 - Minimum Coin Change<br><br>

Make sure these files are in the same directory:<br>
- mcc.py<br>
- mcc_algos.py<br>
- mcc_tests.py<br>
- test.txt for default testing, if desired<br>
- whatever .txt file you wish the test<br>

For correctness testing with file input/output:<br>
- Usage: python mcc.py { all || changeslow || changegreedy || changedp } { filename.txt }<br>
- For example, to run all algorithms on Amount.txt, run the command: python mcc.py all Amount.txt
- This will create a new file everytime<br><br>

- Each algorithm can be individually processed by using the name instead of all
- For example, to run changeslow on Amount.txt, run the command: python mcc.py changeslow Amount.txt
- This will create a new file if one does not exist or append the results to the existing file<br><br>

- If no filename argument is provided, mcc.py will run all three algorithms on test.txt<br><br>

- Results will be output to filenamechanges.txt<br>

- Note: If a filename argument is given, then either all, changeslow, changegreedy or changedp is required<br><br>

Please note that changeslow will have difficulty running coin.txt because of the last problem set<br>

For runtime and other extensive testing:<br>
- Usage: python mcc_testing.py
