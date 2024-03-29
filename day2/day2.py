def run_opcodes(opcodes):
    i = 4

    while i < len(opcodes):
        if opcodes[i] == 99:
            print('halt!', i)
            break

        num1_i = opcodes[i+1]
        num2_i = opcodes[i+2]
        result_i = opcodes[i+3]

        if opcodes[i] == 1:
            opcodes[result_i] = f'({opcodes[num1_i]} + {opcodes[num2_i]})'
            i += 4
        elif opcodes[i] == 2:
            opcodes[result_i] = f'({opcodes[num1_i]} * {opcodes[num2_i]})'
            i += 4
        else:
            i += 1

    return opcodes

file_name = 'input.txt'
nums_str = open(file_name, 'r').readline()
nums = [int(num) for num in nums_str.strip().split(',')]
nums[1] = 'x'
nums[2] = 'y'
nums[3] = 'x + y'
resulting_opcodes = run_opcodes([i for i in nums])
print(resulting_opcodes[0])
