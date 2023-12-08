import os 
from pprint import pprint

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
    for line in f:
    	lines.append(line.strip())

# print("Lines:", lines)
data = [line.split() for line in lines]
# pprint(data)
# print("="*80)

data_t = {
    "FiveKind": [],
    "FourKind": [],
    "FullHouse": [],
    "ThreeKind": [],
    "TwoPair": [],
    "OnePair": [],
    "HighCard": []
}

# Mapping
for i, d in enumerate(data):
    data[i][0] = d[0].replace("A", "E")
    data[i][0] = d[0].replace("K", "D")
    data[i][0] = d[0].replace("Q", "C")
    data[i][0] = d[0].replace("J", "1")
    data[i][0] = d[0].replace("T", "A")

# card type + joker
for i, d in enumerate(data): 
    ls=dict()
    for letter in d[0]:
        if letter in ls:   
            ls[letter]+=1
        else:
            ls[letter]=1
    
    # joker
    jokers = ls.get("1")
    if jokers is None:
        jokers = 0
    else:
        jokers = int(jokers)
    
    if jokers > 1 and jokers != 5:
        ls = dict(sorted(ls.items(), key=lambda item: item[1], reverse=True))
        ls.pop('1', None)
        ls[list(ls.keys())[0]] = ls[list(ls.keys())[0]]+jokers

    if jokers == 1:
        max_key = max(ls, key=ls.get)
        ls[max_key] = ls.get(max_key)+1

    # card type
    if 5 in ls.values():
        data_t["FiveKind"].append(d[0])
        data[i].append("FiveKind")
    elif 4 in ls.values():
        data_t["FourKind"].append(d[0])
        data[i].append("FourKind")
    elif 3 in ls.values():
        if 2 in ls.values():
            data_t["FullHouse"].append(d[0])
            data[i].append("FullHouse")
        else:
            data_t["ThreeKind"].append(d[0])
            data[i].append("ThreeKind")
    elif 2 in ls.values():
        if len(ls) == 3:
            data_t["TwoPair"].append(d[0])
            data[i].append("TwoPair")
        else:
            data_t["OnePair"].append(d[0])
            data[i].append("OnePair")
    else:
        data_t["HighCard"].append(d[0])
        data[i].append("HighCard")
  
# ranking
cur_rank = len(data)
for key, types in data_t.items():
    type_s = sorted(types, reverse=True)
    for type in type_s:
        for i, d in enumerate(data):
            if d[0] == type:
                data[i].append(cur_rank)
                cur_rank -= 1

result1 = 0
for d in data:
    result1 += int(d[1]) * int(d[3])
                            
print(result1)
