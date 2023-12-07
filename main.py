import os 
from pprint import pprint

dir = os.path.dirname(os.path.realpath(__file__))
file_name = ["\\input1Test.txt","\\input1.txt", "\\input2Test.txt", "\\input2.txt"]

lines = []
with open(dir + file_name[0], "r") as f:
    for line in f:
    	lines.append(line.strip())

print("Lines:", lines)
data = [line.split() for line in lines]
pprint(data)
print("="*80)

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
# for i, d in enumerate(data):
#     data[i][0] = d[0].replace("A", "E")
#     data[i][0] = d[0].replace("K", "D")
#     data[i][0] = d[0].replace("Q", "C")
#     data[i][0] = d[0].replace("T", "A")

# card type
for i, d in enumerate(data): 
    ls=dict()
    for letter in d[0]:
        if letter in ls:   
            ls[letter]+=1
        else:
            ls[letter]=1
    print(ls)
    if 5 in ls.values():
        print("FiveKind")
        data_t["FiveKind"].append(d[0])
        data[i].append("FiveKind")

    elif 4 in ls.values():
        print("FourKind")   
        data_t["FourKind"].append(d[0])
        data[i].append("FourKind")
    elif 3 in ls.values():
        if 2 in ls.values():
            print("FullHouse")
            data_t["FullHouse"].append(d[0])
            data[i].append("FullHouse")
        else:
            print("ThreeKind")
            data_t["ThreeKind"].append(d[0])
            data[i].append("ThreeKind")
    elif 2 in ls.values():
        if len(ls) == 3:
            print("TwoPair")
            data_t["TwoPair"].append(d[0])
            data[i].append("TwoPair")
        else:
            print("OnePair")
            data_t["OnePair"].append(d[0])
            data[i].append("OnePair")
    else:
        print("HighCard")
        data_t["HighCard"].append(d[0])
        data[i].append("HighCard")
    
    print(d[0])   

print("="*80)
pprint(data)
print("="*80)
pprint(data_t)
print("="*80)


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

# comp_list = ""
for key, value in data_t.items():
    data_t[key] = list(map(list, zip(*value))) 
pprint(data_t)

for key, values in data_t.items():
    print("Type = Values:", values)
    for value in values:
        print("Erste Buchstaben = value: ", value)
        found = 0
        for rank in ranks:
            for v in value:
                if rank == v:
                    found += 1
            if found == 1:
                print(1, rank, found)
                break
            if found > 1:
                print(2, rank, found)
                break
        if found == 1:
            break
                

# pprint(data)
# result1 = 0
# for d in data:
#     result1 += int(d[1]) * int(d[2])
                            
# print(result1)
