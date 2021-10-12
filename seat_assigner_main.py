from seat_assigner_functions import *
import sys

ROWS = 10
COLS = 20
COL_SPACE = 3
ROW_SPACE = 1
INPUT_FILE = sys.argv[1]
OUTPUT_FILE = "output.txt"

groups = parseInput(INPUT_FILE)
rowOrder = getRowOrder(ROWS, ROW_SPACE)
groupsOrder = getGroupsOrder(groups, COLS, COL_SPACE)
output = findArangment(ROWS, groupsOrder, rowOrder)
writeOutput(OUTPUT_FILE, output)