import csv
import matplotlib.pyplot as plt

def win(match):
    if match == "FALSE": 
        return -1
    else: 
        return 1

def never_should_happen(order):
    wrong_order = ["1","2","3","8","9","10","11","16","17", "20", "21"]
    return order in wrong_order
        

order = {}
with open("pick_order.csv") as File:
    reader = csv.DictReader(File)

    for row in reader:
        if not never_should_happen(row["order"]):
            if order.get(row["order"], False) is False:
                order[row["order"]] = {}
                if row["win"] == "TRUE":
                    order[row["order"]][row["role"]] = 1
                else:
                    order[row["order"]][row["role"]] = -1
            else: 
                if (row["win"] == "TRUE"):
                    if order[row["order"]].get(row["role"], False) is False:
                        order[row["order"]][row["role"]] = 1 
                    else:
                        order[row["order"]][row["role"]] += 1
                else:
                    if order[row["order"]].get(row["role"], False) is False:
                        order[row["order"]][row["role"]] = 1 
                    else:
                        order[row["order"]][row["role"]] += 1

pick_order = list(order.keys())
support_role = [order[pick]["support"] for pick in pick_order]
core_role = [order[pick]["core"] for pick in pick_order]

fig, ax = plt.subplots(figsize=(40,20))
plt.bar(pick_order, support_role)
plt.savefig("support_pick_oder.png")

fig, ax = plt.subplots(figsize=(40,20))
plt.bar(pick_order, core_role)
plt.savefig("core_pick_oder.png")


