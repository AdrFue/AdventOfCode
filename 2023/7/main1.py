import os 
from pprint import pprint

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[1], "r") as f:
    for line in f:
    	lines.append(line.strip())

data = [line.split() for line in lines]

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
    data[i][0] = d[0].replace("J", "B")
    data[i][0] = d[0].replace("T", "A")

# card type
for i, d in enumerate(data): 
    ls=dict()
    for letter in d[0]:
        if letter in ls:   
            ls[letter]+=1
        else:
            ls[letter]=1

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
ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10 
}
for i in range(9, 1, -1):
    ranks[str(i)] = i
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