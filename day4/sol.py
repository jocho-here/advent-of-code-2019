def valid_passwords(lrange, rrange):
    rtn_val = []

    for i in range(lrange, rrange+1):
        curr_int_str = str(i)
        never_decrease = True
        double = False

        for index, d in enumerate(curr_int_str[1:]):
            if int(d) < int(curr_int_str[index]):
                never_decrease = False
            elif int(d) == int(curr_int_str[index]):
                double = True

        if never_decrease and double:
            rtn_val.append(i)

    return rtn_val
            
lrange, rrange = [int(num) for num in open('input.txt', 'r').readline().strip().split('-')]
pws = valid_passwords(lrange, rrange)

print(pws)
print(len(pws))
