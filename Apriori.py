import csv
from itertools import combinations

file_path = input("Enter the path to your file: ")

transactions = []
with open(file_path, 'r') as file:
  reader = csv.reader(file)
  transactions = [row for row in reader]

def apriori(transactions, min_support):
  c1 = {}
  for transaction in transactions:
    for item in transaction:
      if item in c1:
        c1[item] += 1
      else:
        c1[item] = 1

  l1 = {key:value for key, value in c1.items() if value / len(transactions) >= min_support}
  l = [l1]
  k=2
  while len(l[k-2]) > 0:
    ck = {}
    for transaction in transactions:
      combos = combinations(transactions, k)
      for combo in combos:
        if combo in ck:
          ck[combo] += 1
        else:
          ck[combo] = 1
  
    lk = {key:value for key, value in ck.items() if value / len(transactions) >= min_support}
    l.append(lk)
    k += 1
  return [item for sublist in l for item in sublist.keys()]

def association_rules(frequent_itemsets, transactions, min_support):
  rules = []
  for itemset in frequent_itemset:
    for i in range(1, len(itemset)):
      antecedents = [x for x in combinations(itemset, i)]
      for antecedent in antecedent:
        consequent = tuple([item for item in itemset if item not in antecedent])
        antecedent_support = sum([1 for transaction in transactions if set(antecedent).issubset(set(transaction))])
        both_support = sum([1 for transaction in transactions if set(antecedent + consequent).issubset(set(transaction))])
        try:
          confidence = both_support / antecedent_support
          if confidence >= min_confidence:
            rules.append((antecedent, consequent))
        except ZeroDivisionError:
          pass
  return rules

min_support = 2 / len(transactions)
frequent_itemsets = apriori(transactions, min_support)
min_confidence = 0.75
rules = association_rules(frequent_itemsets, transactions, min_confidence)

for item in frequent_itemsets:
  print(item)
for rule in rules:
  print(f"{rule[0]} => {rule[1]}")
