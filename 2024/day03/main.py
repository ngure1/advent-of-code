import re

file_path = "input.txt"
regex = r'mul\(\d+,\d+\)'
regex_two = r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)'


def sum_mul_instructions_one():
    res = 0
    try:
        with open(file_path,"r") as file:
            contents = file.read()
            instructions = re.findall(regex,contents)
            for instruction in instructions:
                left,right = instruction[4:-1].strip().split(",")
                res += (int(left.strip())*int(right.strip()))
            # with open("output.txt","w") as f:
            #     f.write(" ".join(instructions))
   
    except Exception as e:
        print("Something went wrong: ",e)
    return res
    
def sum_mul_instructions_two():
    res = 0
    is_enabled = True
    try:
        with open(file_path,"r") as file:
            contents = file.read()
            instructions = re.findall(regex_two,contents)
            for instruction in instructions:
                if instruction == "do()":
                    is_enabled = True
                elif instruction == "don't()":
                    is_enabled = False
                elif is_enabled:
                    left,right = instruction[4:-1].strip().split(",")
                    res += (int(left.strip())*int(right.strip()))
   
    except Exception as e:
        print("Something went wrong: ",e)
    return res
        
# print(sum_mul_instructions_one())
print(sum_mul_instructions_two())