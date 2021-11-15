"""
Author:Neha Singh
Project Introduction:

## Set the directory as under before running the code
## Keep the program file and the dataset in the same directory
"""

from itertools import permutations
from itertools import combinations

## Defining all the Functions

## Find the count of unique items and make a dictionery
def uniquelist(final_data):
    mylist = []
    for i in final_data:
        for j in range(len(i)):
            mylist.append(i[j])
    uniquelist = set(mylist)
    uniquelist = sorted(uniquelist)
    return uniquelist, mylist


## Performing Iteration 1
def iteration1(mylist, uniquelist):
    firstdict = {}
    for i in uniquelist:
        firstdict[i] = mylist.count(i)
    return firstdict


## Eliminate those items not satisfying minimum support
def support_eliminate(firstdict):
    keylist = list(firstdict.keys())
    valuelist = list(firstdict.values())
    mydict2 = {}
    # support_dict = {}
    count = 0

    for i in valuelist:
        support = round(i * 100 / total_trxns, 2)
        count += 1

        # print(support, min_sup)
        if support >= min_sup:
            # firstdict.pop(keylist[count])
            mydict2[keylist[count - 1]] = i
            # support_dict[keylist[count-1]] = support
    return mydict2

## Creating combinations of items in Iteration 1
def create_combinations1(mydict2, n):
    comb = combinations(list(mydict2.keys()), n)
    up_comb = []
    for i in comb:
        up_comb.append(i)

    return up_comb

## Performing Iteration 2
def iter2(final_data, up_comb):
    updated_dict = {}
    for i in range(len(final_data)):
        c2=0
        for j in range(len(up_comb)):
            if (up_comb[j][0] and up_comb[j][1]) in final_data[i]:
                c2+=1
                updated_dict[up_comb[j]] = c2
    return updated_dict

## Creating combinations of items in Iteration 2
def create_combinations2(targlist, n):
    comb = combinations(targlist, n)
    up_comb = []
    for i in comb:
        up_comb.append(i)

    return up_comb


## Performing Iteration 3
def iter3(final_data, combs_3):
    updated_dict3 = {}
    for i in range(len(final_data)):
        c2=0
        for j in range(len(combs_3)):
            if (combs_3[j][0] and combs_3[j][1] and combs_3[j][2]) in final_data[i]:
              c2= c2+1
              updated_dict3[combs_3[j]] = c2

    return updated_dict3


## List of Frequent itemsets and Association rules
def assoc_rules(highkey, highval):
    support_dict = {}
    count = 0
    item_set = set(highkey)

    comb2s = combinations(highkey, 2)
    for i in comb2s:
        print("Association Rule for Pair - ", i)
        print("__Rule__", "__Confidence__")
        i = tuple(sorted(i))
        left_item = i
        right_item = tuple(item_set - set(i))

        # print(left_item, "=>" ,right_item)

        denom2 = sup_elim2[i]
        conf = (highval // denom2) * 100

        if conf >= min_conf:
            print(left_item, "=>", right_item, conf, "This Rule is Acceptable")
        else:
            print(left_item, "=>", right_item, conf, "This Rule is Rejected")

    comb1s = highkey
    for i in comb1s:
        print("Association Rule for Pair - ", i)
        print("__Rule__", "__Confidence__")

        left_item = i
        right_item = tuple(item_set - set(i))
        denom1 = sup_elim1[i]
        conf1 = highval * 100 // denom1

        # print(left_item, right_item)
        if conf1 >= min_conf:
            print(left_item, "=>", right_item, conf1, "This Rule is Acceptable")
        else:
            print(left_item, "=>", right_item, conf1, "This Rule is Rejected")
    print()



## Main program to run Algorithm using the functions defined

print("\n","Welcome to Neha's Apriori Algorithm Implementation. ", '\n',
      "This program will take input data of transactions from you and ", '\n',
      "give you the most frequent association rules with your product lines in return. ", '\n',
      "This can give you an idea about what products sell in a combination following them can maximize your profit. ", "\n")


filename = input("Enter File name with '.txt' extension:")
fileobject = open(filename, "r", encoding="UTF-8",errors="surrogateescape")
input_data = fileobject.readlines()

## Transforming the dataset
final_data = []
for lines in range(1,len(input_data)):
    input_data[lines] = input_data[lines].replace("\n","")
    final_data.append(input_data[lines].split(','))

## Transforming final_data
for i in range(len(final_data)):
  final_data[i] = final_data[i][1:]

print("\n","This is the dataset you entered:", "\n", "\n", final_data, '\n')

## Declaring all the required variables
min_sup = int(input("Enter Minimum Support:"))
print("\n")
min_conf = int(input("Enter Minimum Confidence:"))
print("\n")

total_trxns = len(final_data)

uniques, full_list = uniquelist(final_data)

iteration1 = iteration1(full_list, uniques)

sup_elim1 = support_eliminate(iteration1)

print("\n","This is the result after first iteration:", "\n", "\n", sup_elim1, '\n')

new_combs = create_combinations1(sup_elim1, 2)

iteration2 = iter2(final_data, new_combs)

sup_elim2 = support_eliminate(iteration2)

print("\n","This is the result after second iteration:", "\n", "\n", sup_elim2, '\n')

mylist2iter = list(sup_elim2.keys())

##used this to put unique pairs in tuple to make it in a single list
listafter2 = []
for i in range(len(mylist2iter)):
    listafter2.append(mylist2iter[i][0])
    listafter2.append(mylist2iter[i][1])

listafter2 = set(listafter2)

combs_3 = create_combinations2(listafter2, 3)

iteration3 = iter3(final_data, combs_3)

sup_elim3 = support_eliminate(iteration3)

print("\n","This is the result after third iteration:", "\n", "\n", sup_elim3, '\n')


highkey = tuple(sorted(list(iteration3.keys())[list(iteration3.values()).index(max(iteration3.values()))]))
highval = max(iteration3.values())

assoc_rules(highkey, highval)

