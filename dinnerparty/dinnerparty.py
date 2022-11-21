# Block1
import random

print("Enter the number of friends joining (including you):")
numberOfFrends = int(input(">"))
print("")

if numberOfFrends < 1:
    print("No one is joining for the party")
else:
    # Block2
    frendsDict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for a in range(0, numberOfFrends):
        frendsDict[input(">")] = 0
    print("")
    # Block3
    print("Enter the total amount")
    totalSum = float(input(">"))
    print("")
    # Block4
    luckyEntity = False
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    if input(">") == "Yes":
        luckyEntity = random.choice([*frendsDict])
        print(f"{luckyEntity} is the lucky one!")
    else:
        print("No one is going to be lucky.")
    print("")
    #Block5
    if str(luckyEntity) == "False":
        for a in frendsDict:
            frendsDict[a] = round(totalSum / len(frendsDict), 2)
    else:
        for a in frendsDict:
            if a != luckyEntity:
                frendsDict[a] = round(totalSum / (len(frendsDict)-1), 2)
    print(frendsDict)

