n = int(input("N-->"))

if n > 0:
    with open("popular-names.txt") as data:
        lines = data.readlines()
        for line in lines[-n:]:
            print(line.rstrip())

# tail -n 2 popular-names.txt