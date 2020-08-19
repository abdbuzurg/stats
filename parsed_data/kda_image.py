import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

kda_lose = []
kda_win = []
with open("kda_win.csv") as File:
    reader = csv.DictReader(File)

    for row in reader:
        if row["radiant_win"] == "True":
           kda_win.append(int(row["KDA"]))
        else:
            kda_lose.append(int(row["KDA"]))

kda_lose.sort(reverse=True)
mean = sum(kda_lose) / len(kda_lose)
variance = 0
for number in range(len(kda_lose)):
    variance += (number - mean) ** 2

variance /= len(kda_lose) - 1
sd = math.sqrt(variance)
fig, ax = plt.subplots(figsize=(40,20))
x = np.linspace(mean - 3 * sd, mean + 3*sd, 100)
plt.plot(x, stats.norm.pdf(x, mean, sd))
plt.savefig("lose_kda.png")

kda_win.sort(reverse=True)
mean = sum(kda_win) / len(kda_win)
variance = 0
for number in range(len(kda_win)):
    variance += (number - mean) ** 2

variance /= len(kda_win) - 1
sd = math.sqrt(variance)
fig, ax = plt.subplots(figsize=(40,20))
x = np.linspace(mean - 3 * sd, mean + 3*sd, 100)
plt.plot(x, stats.norm.pdf(x, mean, sd))
plt.savefig("win_kda.png")

