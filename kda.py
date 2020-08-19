import csv

match_win = []
with open("matches.csv") as File:
    reader = csv.DictReader(File)
    for row in reader:
        match_win.append({"match_id": row["match_id"],  "radiant_win": row["radiant_win"]})

player_kda = []
with open("player_matches.csv") as File:
    reader = csv.DictReader(File)
    for row in reader:
        avarage = int(row["kills"]) - int(row["deaths"]) + int(row["assists"])
        player_kda.append({"match_id": row["match_id"],  "avarage_kda": avarage})

# print(player_kda)
matches_id_for_win = [element["match_id"] for element in match_win]
i = 0
with open("kda_win.csv", mode="w") as File:
    fieldnames = ["KDA", "radiant_win"]
    writer = csv.DictWriter(File, fieldnames=fieldnames)
    k = 0
    while i < len(player_kda):
        if (i / len(player_kda) > 0.2 and k == 0):
            k += 1
            print("20 percent done")
        if (i / len(player_kda) > 0.4 and k == 1):
            k += 1
            print("40 percent done")
        if (i / len(player_kda) > 0.6 and k == 2):
            k += 1
            print("60 percent done")
        if (i / len(player_kda) > 0.8 and k == 3):
            k += 1
            print("80 percent done")
        if (player_kda[i]["match_id"] in matches_id_for_win):
            index_of_win = matches_id_for_win.index(player_kda[i]["match_id"])
            win = match_win[index_of_win]["radiant_win"]
            row = { "KDA": player_kda[i]["avarage_kda"], "radiant_win": win}
            # print(row)
            writer.writerow(row)
        
        i += 1