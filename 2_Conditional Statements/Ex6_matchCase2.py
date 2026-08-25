print("------2: match case----")

inp="abc"
match inp:
    case "mon":
        print("Day num 1")
    case "tue":
        print("Day num 2")
    case "wed":
        print("Day num 3")
    case "thr":
        print("Day num 4")
    case "fri":
        print("Day num 5")
    case "sat":
        print("Day num 6")
    case "sun":
        print("Day num 7")
    case _:
        print("Wrong Input")

print("-------")

match "sun":
    case "mon":
        print("Day num 1")
    case "tue":
        print("Day num 2")
    case "wed":
        print("Day num 3")
    case "thr":
        print("Day num 4")
    case "fri":
        print("Day num 5")
    case "sat":
        print("Day num 6")
    case "sun":
        print("Day num 7")
    case _:
        print("Wrong Input")


print("-----------")

match "MT":
    case "BI":
        print("Running BI code")
    case "MT":
        print("Running MT code")
    case "MS":
        print("Running MS code")
    case "CD":
        print("Running CD code")
    case "CW":
        print("Running CW code")
    case _:
        print("Wrong Input")