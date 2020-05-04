import json
import random

options = ["R", "R'", "R2", "U", "U'", "U2", "F", "F'", "F2",
           "L", "L'", "L2", "D", "D'", "D2", "B", "B'", "B2"]

groups = [["R", "R'", "R2"], ["U", "U'", "U2"], ["F", "F'", "F2"],
          ["L", "L'", "L2"], ["D", "D'", "D2"], ["B", "B'", "B2"]]


def subtract(l1, l2):  # l1 - l2
    l = l1.copy()
    for i in l2:
        l.remove(i)

    return l


def add_scramble(scramble):
    with open("scrambles.json", "r") as f:
        content = json.load(f)

    content[scramble] = None

    with open("scrambles.json", "w") as f:
        json.dump(content, f)


def has_duplicate(scramble):
    with open("scrambles.json", "r") as f:
        content = json.load(f)

    return scramble in content.keys()


def generate_scramble(min_len=15, max_len=25):
    global options
    global groups
    scramble = ""
    lenght = random.randint(min_len, max_len)

    # 1. move
    new = random.choice(options)
    scramble += new+" "
    prev = new

    for _ in range(lenght-1):  # all other moves
        for x in range(6):  # [0,1,2,3,4,5]
            if prev in groups[x]:
                to_choice = subtract(options, groups[x])
                new = random.choice(to_choice)
                scramble += new+" "
                prev = new

    if has_duplicate(scramble) == True:
        generate_scramble(min_len, max_len)  # generate new scramble
    else:
        add_scramble(scramble)  # append created scramble to json file


# when javascript runs this file, it will automatically create a scramble and write it to the json file
generate_scramble()
