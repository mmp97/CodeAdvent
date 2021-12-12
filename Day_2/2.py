### Part 1
with open("data.txt","r") as f:
    lines = f.readlines()
    x = 0
    y = 0
    for line in lines:
        l = line.split(None, 1)
        match l[0]:
            case 'up':  
                y -= int(l[1])
            case 'down':
                y += int(l[1])
            case 'forward':
                x += int(l[1])
    print(x*y)
### Part 2
with open("data.txt","r") as f:
    lines = f.readlines()
    x = 0
    y = 0
    aim = 0
    for line in lines:
        l = line.split(None, 1)
        match l[0]:
            case 'up':  
                aim -= int(l[1])
            case 'down':
                aim += int(l[1])
            case 'forward':
                x += int(l[1])
                y += int(l[1])*aim
    print(x*y)
