import csv
import time
import random

def switch(x):
    return {
        1: "radiant",
        2: "dire",
        3: "dire",
        4: "radiant",
        5: "dire",
        6: "radiant",
        7: "dire",
        8: "radiant",
        9: "radiant",
        10: "dire"
    }[x]

def winner(side, win):
    if (side == "radiant"):
        if (win == "TRUE"):
            return "TRUE"
        else: 
            return "FALSE"
    
    if (side == "dire"):
        if (win == "TRUE"):
            return "FALSE"
        else: 
            return "TRUE"

heroes = []
with open('heroes.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        del row["name"]
        del row["legs"]
        del row["primary_attr"]
        del row["attack_type"]
        del row["roles"]
        # print(row)
        heroes.append(row)

picks_picks = []
picks_bans = []

with open("picks_bans.csv") as File:
    reader = csv.DictReader(File)
    k = 1
    for row in reader:
        if row["is_pick"] == "TRUE":
            k += 1
            if k > 10:           
                k = 1

            picks_picks.append({ "match_id": row["match_id"], "hero_id": row["hero_id"], "side": switch(k) })
        else:
            picks_bans.append({ "match_id": row["match_id"], "hero_id": row["hero_id"] })


# print(picks_bans)
match_patch = []
with open("match_patch.csv") as File:
    reader = csv.DictReader(File)
    for row in reader:
        match_patch.append(row)

match_win = []
with open("matches.csv") as File:
    reader = csv.DictReader(File)
    for row in reader:
        match_win.append({"match_id": row["match_id"],  "radiant_win": row["radiant_win"]})


matches_id_for_patch = [element["match_id"] for element in match_patch]
matches_id_for_win = [element["match_id"] for element in match_win]
hero_ids = [element["id"] for element in heroes]
matches = []
# print(len(heroes), len(picks_bans), len(match_win), len(match_patch))
current_time = time.localtime(time.time())
print("Forming the list for heroes that's have been picked")
print("Started at {0}:{1}:{2}".format(current_time.tm_hour,current_time.tm_min, current_time.tm_sec))
k = 0
for i in range(0, len(picks_picks)):
    match_id = picks_picks[i]["match_id"]
    if (match_id in matches_id_for_patch and match_id in matches_id_for_win):
        index_for_patch = matches_id_for_patch.index(match_id)
        index_for_win = matches_id_for_win.index(match_id)
        index_of_hero = hero_ids.index(picks_picks[i]["hero_id"])

        match = { 
            "hero": heroes[index_of_hero]["localized_name"], 
            "radiant_win": winner(picks_picks[i]["side"], match_win[index_for_win]["radiant_win"]),
            "patch": match_patch[index_for_patch]["patch"], 
        }
        if (i / len(picks_picks) > 0.2 and k == 0): 
            print("20 percent done")
            current_time = time.localtime(time.time())
            print("Started at {0}:{1}:{2}".format(current_time.tm_hour,current_time.tm_min, current_time.tm_sec))
            k += 1
        if (i / len(picks_picks) > 0.4 and k == 1): 
            print("40 percent done")
            current_time = time.localtime(time.time())
            print("Started at {0}:{1}:{2}".format(current_time.tm_hour,current_time.tm_min, current_time.tm_sec))
            k += 1
        if (i / len(picks_picks) > 0.6 and k == 2): 
            print("60 percent done")
            current_time = time.localtime(time.time())
            print("Started at {0}:{1}:{2}".format(current_time.tm_hour,current_time.tm_min, current_time.tm_sec))
            k += 1
        if (i / len(picks_picks) > 0.8 and k == 3): 
            print("80 percent done")
            current_time = time.localtime(time.time())
            print("Started at {0}:{1}:{2}".format(current_time.tm_hour,current_time.tm_min, current_time.tm_sec))
            k += 1
        matches.append(match)

i = 0
current_patch = matches[i]["patch"]
current_patch = list(current_patch)
del current_patch[1]
current_patch = ''.join(current_patch)
print("Starting the creation of CSVs for picked heroes in specific patch")
print("Initiating csv about the patch " + current_patch)
current_time = time.localtime(time.time())
print("Starting {0}:{1}:{2}".format(current_time.tm_hour,current_time.tm_min, current_time.tm_sec))

while i < len(matches):
    
    with open("parsed_winrates" + current_patch + ".csv", mode = "w") as File:
        fieldnames = matches[0].keys()
        writer = csv.DictWriter(File, fieldnames=fieldnames)

        writer.writeheader()
        j = 0
        for k in range(i, len(matches)):
            patch = matches[k]["patch"]
            patch = list(patch)
            del patch[1]
            patch = ''.join(patch)
            if (patch == current_patch): 
                writer.writerow({"hero": matches[k]["hero"], "radiant_win":matches[k]["radiant_win"] })
                j += 1
                
            else:
                print("Finishing the csv about patch " + current_patch)
                current_patch = matches[k]["patch"]
                current_patch = list(current_patch)
                del current_patch[1]
                current_patch = ''.join(current_patch)
                print("Initiating csv about the patch {0}".format(current_patch))
                current_time = time.localtime(time.time())
                print("Starting {0}:{1}:{2}".format(current_time.tm_hour,current_time.tm_min, current_time.tm_sec))
                break
        
        i += j

