import math

def sum_versions(data):
    pos = 0
    result = 0
    while pos < len(data) and int(data[pos:]):
        version, type_id, length, val = read_next(data[pos:])
        pos += length
        result += version
    return result

def evaluate(data):
    pos = 0
    result = 0
    while pos < len(data) and int(data[pos:]):
        version, type_id, length, val = read_next(data[pos:])
        pos += length
        if type_id != 4:
            packets, length = read_packets_or_bits(data[pos:], val[0], val[1])
            result = operation(type_id, packets)
            pos += length
    return result

def read_next(data):
    version = int(data[0:3], 2)
    type_id = int(data[3:6], 2)
    pos = 6
    if type_id == 4: # literal value
        number = ''
        while data[pos] == '1':
            number += data[pos+1:pos+5]
            pos += 5
        number += data[pos+1:pos+5]
        number = int(number, 2)
        return version, type_id, pos+5, number
    else: # operator
        if data[pos] == '1': # 11-bit
            isSubpackets = True # number of sub-packets immediately contained
            sub_packets = int(data[pos+1:pos+12], 2)
            return version, type_id, pos+12, (sub_packets, isSubpackets)
        else: # 15-bit
            isSubpackets = False # total length in bits
            sub_length = int(data[pos+1:pos+16], 2)
            return version, type_id, pos+16, (sub_length, isSubpackets)

def read_packets_or_bits(data, num, isSubpackets):
    pos = 0
    packets = []
    if isSubpackets: # 11-bit
        for _ in range(num): 
            version, type_id, length, val = read_next(data[pos:])
            pos += length
            if type_id != 4:
                sub_packets, length = read_packets_or_bits(data[pos:],  val[0], val[1])
                val = operation(type_id, sub_packets)
                pos += length
            packets.append(val)
    else: # 15-bit
        while pos < num:
            version, type_id, length, val = read_next(data[pos:])
            pos += length
            if type_id != 4:
                sub_packets, length = read_packets_or_bits(data[pos:],  val[0], val[1])
                val = operation(type_id, sub_packets)
                pos += length
            packets.append(val)
    return packets, pos

def operation(op, packets):
    packets = [int(p) for p in packets]
    if op == 0:
        return sum(packets)
    if op == 1:
        return math.prod(packets)
    if op == 2:
        return min(packets)
    if op == 3:
        return max(packets)
    if op == 5:
        return int(packets[0] > packets[1])
    if op == 6:
        return int(packets[0] < packets[1])
    if op == 7:
        return int(packets[0] == packets[1])


def calc():
    with open('transmission.txt') as file:
        data = file.read()
    binary_string = bin(int(data, 16))[2:].zfill(len(data)*4)
    # what do you get if you add up all versions?
    print('Sum all versions: {}'.format(sum_versions(binary_string)))
    # what do you get if you evaluate the expression represented?
    print('Evaluate: {}'.format(evaluate(binary_string)))


calc()
