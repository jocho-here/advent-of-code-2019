def valid_passwords(lrange, rrange):
    rtn_val = []

    for i in range(lrange, rrange+1):
        curr_int_str = str(i)
        never_decrease = True
        double = False
        double_i = -1

        for index, d in enumerate(curr_int_str[1:]):
            if int(d) < int(curr_int_str[index]):
                never_decrease = False
                break
            elif int(d) == int(curr_int_str[index]):
                if not double and double_i == -1:
                    double = True
                    double_i = index
                elif double_i == index - 1:
                    double = False
                    double_i = index
            else:
                double_i = -1

        if never_decrease and double:
            rtn_val.append(i)

    return rtn_val
            
#file_name = 'small_input.txt'
file_name = 'input.txt'
lrange, rrange = [int(num) for num in open(file_name, 'r').readline().strip().split('-')]
pws = valid_passwords(lrange, rrange)

#print(pws)
print(len(pws))
