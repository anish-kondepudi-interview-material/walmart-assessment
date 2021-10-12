# Reads & Parses input file into groups sorted by size and order
def parseInput(filename):
    groups = []
    with open(filename) as file:
        i = 0
        while (line := file.readline().rstrip()):
            line = line.split()
            group = (line[0], int(line[1]), i:=i-1)
            groups.append(group)
    return sorted(groups, reverse=True, key=lambda x: (x[1],x[2]))

# Returns list of rows sorted by satisfaction (best to worst)
def getRowOrder(rows, row_space):
    middleRow = rows//2
    rowOrder = [middleRow]
    for i in range(1,rows//4 + row_space):
        if (row := middleRow+2*i) < rows:
            rowOrder.append(row)
        if (row := middleRow-2*i) >= 0:
            rowOrder.append(row)
    return rowOrder

# Finds most optimal movie layout (Fits as many groups into each row)
def getGroupsOrder(groups, cols, col_space):
    visited = set()
    res = []
    for i, group in enumerate(groups):
        if group in visited: continue
        colBlock = [group]
        counter = group[1]
        for j in range(i+1,len(groups)):
            group = groups[j]
            groupSize = group[1]
            if group in visited: continue
            if counter+groupSize+col_space > cols: continue
            counter += groupSize+col_space
            visited.add(group)
            colBlock.append(group)
        res.append(colBlock)
    return res

# Reformats optimal movie layout into expect format
def findArangment(rows, groupsOrder, rowOrder):
    if rows > 26:
        raise ValueError('There cannot be more than 26 rows.')

    rowMap = {}
    for i in range(10):
        rowMap[i] = chr(i+ord('A'))

    output = []
    for groups, row in zip(groupsOrder, rowOrder):
        i = 0
        for group in groups:
            groupID, groupSize = group[0], group[1]
            groupOutput = groupID + " "
            for j in range(groupSize):
                groupOutput += rowMap[row]+str(i)+","
                i += 1
            i += 3
            output.append(groupOutput[:-1])

    return output

# Creates Output File
def writeOutput(filename, output):
    with open(filename, 'w') as file:
        for line in output:
            file.write("%s\n" % line)