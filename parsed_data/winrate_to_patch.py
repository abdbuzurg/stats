import csv
import matplotlib.pyplot as plt

for i in range(21):
    matches = []
    if (i < 10): patch = "70" + str(i)
    if (i > 9): patch = "7" + str(i)
    with open("./winrates/parsed_winrates"+ patch +".csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            del row["patch"]
            matches.append(row)

    winrates = []
    heroes = []
    for i in range(len(matches)):
        hero = matches[i]["hero"]
        if (hero not in heroes):
            heroes.append(hero)
            if (matches[i]["radiant_win"] == "TRUE"):
                winrate = {"hero": hero, "won": 1, "matches_played": 1}
            else:
                winrate = {"hero": hero, "won": 0, "matches_played": 1}

            winrates.append(winrate)
        else: 
            index = heroes.index(hero)
            if (matches[i]["radiant_win"] == "TRUE"):
                winrates[index]["won"] += 1

            winrates[index]["matches_played"] += 1

    winrate = [{"hero": rate["hero"], "winrate": rate["won"]/rate["matches_played"]} for rate in winrates]
    winrate = sorted(winrate, key=lambda x: x["winrate"], reverse=True)
    heroes = [name["hero"] for name in winrate]
    rate = [rate["winrate"] for rate in winrate]
    fig, ax = plt.subplots(figsize=(160,20))
    plt.bar(heroes, rate)
    print("saving file winrate" + patch)
    plt.savefig('winrate'+ patch + '.png')

    banrates = []
    banrate_heroes = []
    with open("./banrates/parsed_banrates"+ patch +".csv") as File:
        reader = csv.DictReader(File)
        for row in reader:
            if not (row["hero"] in banrate_heroes):
                banrate_heroes.append(row["hero"])
                banrates.append({"hero": row["hero"], "ban": 1})
            else:
                banrates[banrate_heroes.index(row["hero"])]["ban"] += 1

    banrates = sorted(banrates, key=lambda x: x["ban"], reverse=True)
    heroes = [name["hero"] for name in banrates]
    rate = [rate["ban"] for rate in banrates]

    fig, ax = plt.subplots(figsize=(160,20))
    plt.bar(heroes, rate)
    print("saving file banrate" + patch)
    plt.savefig('banrate'+ patch + '.png')