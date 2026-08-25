
print("-------1: Example of match case--------")

num=2
match num:
    case 1:
        print("Today is mon")
    case 2:
        print("Today is tue")
    case 3:
        print("Today is wed")
    case 4:
        print("Today is thr")
    case 5:
        print("Today is fri")
    case 6:
        print("Today is sat")
    case 7:
        print("Today is sun")
    case _:
        print("Invalid Input")


print("-------")

match 3:
    case 1:
        print("Today is mon")
    case 2:
        print("Today is tue")
    case 3:
        print("Today is wed")
    case 4:
        print("Today is thr")
    case 5:
        print("Today is fri")
    case 6:
        print("Today is sat")
    case 7:
        print("Today is sun")
    case _:
        print("Invalid Input")
