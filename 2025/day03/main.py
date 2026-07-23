file_path = "input.txt"

def part_one(bank: list[int]):
    curr_max = 0
    for i in range(len(bank)-1):
        # handle duplicates using set
        s = set()
        for j in range(i+1,len(bank)):
            num = bank[i]*10 + bank[j]
            if num not in s:
                curr_max = max(curr_max,num)
                s.add(num)
    
    return curr_max
    
def part_two(bank: list[int]):
    rem_digits = 12
    num = 0
    i = 0
    while i < len(bank) and rem_digits > 0:
        rem_options = len(bank[i:])
        
        # if the remaining digits equals remaining options, use all remaining digits
        if rem_digits == rem_options:
            for digit in bank[i:]:
                num = num * 10 + digit
            return num 
            
        biggest = bank[i]
        biggest_index = i
        
        # Look ahead as far as we can while still having enough digits left
        # We can look at positions i, i+1, ..., i + (rem_options - rem_digits)
        for j in range(i, i + rem_options - rem_digits + 1):
            if bank[j] > biggest:
                biggest = bank[j]
                biggest_index = j
            if biggest == 9:  # Early exit optimization
                break
        
        # Add the biggest digit found
        num = num * 10 + biggest
        rem_digits -= 1
        
        # Continue from the position after the chosen digit
        i = biggest_index + 1
        
    return num
    
def max_joltage():
    try:
        with open(file_path,"r") as f:
            lines = f.readlines()
            res = 0
            for bank in lines:
                bankNums = [int(c) for c in bank.strip()]
                num = part_two(bankNums)
                print(f"Num = {num}")
                res += num
            return res
    except Exception as e:
        print(f"Something went wrong: {e}")

print(f"\nSolution = {max_joltage()}")