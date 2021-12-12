### Part 1
with open("data.txt","r") as f:
    lines = f.readlines()
    size = len(lines)
    length = len(lines[0])
    table = []
    for i in range(length-1):
        table.append(0)
    str_gamma = ''
    str_epsilon = ''
    for line in lines:
        for i in range(length-1):
            if line[i] == '1':
                table[i] += 1
    for t in table:
        if t > size/2:
            str_gamma += '1'
            str_epsilon += '0'
        else:
            str_gamma += '0'
            str_epsilon += '1'
    print(str_gamma)
    print(str_epsilon)
    print(int(str_gamma, 2)*int(str_epsilon, 2))
### Part 2
def check(list, place, sign):
    count = 0
    choice = '1'
    new_list = []
    if len(list) == 1:
        return str(list[0])
    for l in list:
        if l[0+place] == '1':
            count += 1
    if sign*count < len(list)/2*sign:
        choice = '0'
    if sign*count == len(list)/2*sign and sign == -1:
        choice = '0'
    for l in list:
        if l[0+place] == choice:
            new_list.append(l)
    place += 1
    return check(new_list, place,sign)



with open("data.txt","r") as f:
    lines = f.readlines()
    length = len(lines[0])
    place = 0
    sign = 1
    oxygen_generator_ratingprint = int(check(lines,place,sign), 2)
    sign = -1
    CO2_scrubber_rating = int(check(lines,place,sign), 2)
    print(oxygen_generator_ratingprint)
    print(CO2_scrubber_rating)
    print(oxygen_generator_ratingprint*CO2_scrubber_rating)


