import os 
import numpy as np

class Monkey:
  items = []
  operation = ''
  div = -1
  trueMonkey = -1
  falseMonkey = -1
  inspectCounter = 0

  def __init__(self, items, operation, div, trueMonkey, falseMonkey):
    self.items = items
    self.operation = operation
    self.div = div
    self.trueMonkey = trueMonkey
    self.falseMonkey = falseMonkey

  def doOperation(self, item):
    old = item
    return eval(self.operation)
  
  def inspect(self, item, part):
    self.inspectCounter += 1
    item = self.doOperation(item)
    item = item // 3 if part == 1 else item % superMod # Kuss geht raus an Geib
    if (item % self.div) == 0:
      ms[self.trueMonkey].items.append(item)
    else:
      ms[self.falseMonkey].items.append(item)


dir = os.path.dirname(os.path.realpath(__file__))
lines = []

def createMonkeys():
  ms = []
  for i in range(0, len(lines), 7):
    items = [int(item.replace(',', '')) for item in lines[i+1].split(' ')[2:]]
    operation = lines[i+2].split('= ')[1]
    div = int(lines[i+3].split(' ')[3])
    trueMonkey = int(lines[i+4].split(' ')[5])
    falseMonkey = int(lines[i+5].split(' ')[5])
    ms.append(Monkey(items, operation, div, trueMonkey, falseMonkey)) 
  return ms

def inspects(part, rounds, ms):
  for j in range(rounds):
    if j % 1000 == 0 or j == 20:
      print("round:", j)
      print(getMonkeyBuissness(ms))
    for m in ms:
      for m.item in m.items:
        m.inspect(m.item, part)
      m.items = []    
  print(getMonkeyBuissness(ms))

def getMonkeyBuissness(ms):
  for i in range(len(ms)):
    print(i, ms[i].inspectCounter, ms[i].items)

  ics = sorted([m.inspectCounter for m in ms], reverse=True)
  monkeyBusiness = ics[0] * ics[1]
  return monkeyBusiness

########### Start ############
with open(dir + "/input.txt", "r") as f:
    for line in f:
      lines.append(line.strip())

# ## Teil 1 ##
ms = createMonkeys()
inspects(1, 20, ms)


## Teil 2 ##
ms = createMonkeys()
superMod = 1
for m in ms:
  superMod *= m.div
inspects(2, 10000, ms)
