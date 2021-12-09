from time import sleep
### Part 1 ###
with open("data.txt", "r") as f:
    lines = f.readlines()
    count = 0
    num_data = []
    for line in lines:
        num_data.append(int(line))
    for idx in range(0, len(lines)-1):
        if(num_data[idx+1]>num_data[idx]):  
            count += 1
    print(count)

### Part 2 ###
with open("data.txt", "r") as f:
    lines = f.readlines()
    count = 0
    num_data = []
    for line in lines:
        num_data.append(int(line))
    for idx in range(1, len(num_data)-2):
        curr = num_data[idx] + num_data[idx+1] + num_data[idx+2]
        prev = num_data[idx-1] + num_data[idx] + num_data[idx+1]

        if(curr > prev):  
            count += 1
    print(count)

        