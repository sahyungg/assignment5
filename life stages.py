age = int(input("Age: "))

if age <= 12:
    print("Kid")
else:
    if age <= 17:
        print("Teen")
    else:
        if age == 18:
            print("Debut")
        else:
            if age >= 19:
                print("Adult")