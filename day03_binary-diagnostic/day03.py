# What is the power consumption of the submarine?
def calc1():
    gamma = ''
    epsilon= ''
    data = [list(i) for i in open("input.txt")]
    for j in list(zip(*data)): # transpose
        if j.count('0') > j.count('1'):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    print('power consumption: {}'.format(int(gamma, 2) * int(epsilon, 2)))

# What is the life support rating of the submarine?
def calc2():
    data = [list(i) for i in open("input.txt")]
    oxygen = calc(data, 0, '0', '1', '1')
    co2 = calc(data, 0, '1', '0', '0')
    print('life support rating: {}'.format(int(oxygen, 2) * int(co2, 2)))
 
def calc(data, count, zero_common, one_common, equal_common):
    data_t = list(zip(*data)) # transpose
    column = count
    if data_t[column].count('0') > data_t[column].count('1'):
        data = [i for i in data if i[column] == zero_common] # recreate list
    elif data_t[column].count('0') < data_t[column].count('1'):
        data = [i for i in data if i[column] == one_common]
    elif  data_t[column].count('0') == data_t[column].count('1'):
        data = [i for i in data if i[column] == equal_common]  
    if len(data) > 1:
        column += 1
        return calc(data, column, zero_common, one_common, equal_common)
    else:
        return "".join(str(i) for i in data[0])

calc1()
calc2()