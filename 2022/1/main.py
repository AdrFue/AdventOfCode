## Teil 1 ##

import os 
dir = os.path.dirname(os.path.realpath(__file__))
values = [[]]
count = 0

def findMax(lvaluesSum):
  lmax = -1
  lindex = 0
  for i in range(len(lvaluesSum)):
    if lvaluesSum[i] > lmax:
      lmax = lvaluesSum[i]
      lindex = i
  return lindex

with open(dir + "/cal.txt", "r") as f:
    for line in f:
        values[count].append(line)
        if len(line) == 1:
          count += 1
          values.append([])

# replace \n of all values in the list
for i in range(len(values)):
  for j in range(len(values[i])):
    values[i][j] = values[i][j].replace('\n', '')
    if values[i][j] == '':
      values[i].pop(j)

print(values)

# sum all lists in values
sum = 0
valuesSum = []
for v in values:
  for i in v:
    sum += int(i)
  valuesSum.append(sum)
  sum = 0

print(valuesSum)

## Teil 2 ##

sumTotal = 0
# hässlichster code ever
curMax = findMax(valuesSum)
print(valuesSum[curMax])
sumTotal += valuesSum[curMax]
valuesSum.pop(curMax)

curMax = findMax(valuesSum)
print(valuesSum[curMax])
sumTotal += valuesSum[curMax]
valuesSum.pop(curMax)

curMax = findMax(valuesSum)
print(valuesSum[curMax])
sumTotal += valuesSum[curMax]
valuesSum.pop(curMax)

print(sumTotal)

