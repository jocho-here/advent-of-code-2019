def get_fuels(file_name):
    fuel_total = 0

    with open(file_name, 'r') as f:
        nums = [int(num.strip()) for num in f.readlines()]
        
        for num in nums:
            fuel_total += get_fuels_rec_helper(num)

    return fuel_total

def get_fuels_rec_helper(num):
    if num < 9:
        return 0
    
    fuels = (num//3) - 2

    return fuels + get_fuels_rec_helper(fuels)

file_name = 'input-1.txt'
print(get_fuels(file_name))
