file_path = "input.txt"

def is_valid(numString: str) -> bool:
    mid = len(numString) // 2
    return numString[:mid] != numString[mid:]

def is_valid_two(numString: str) -> bool:
    if len(set(numString)) == 1 and len(set(numString)) != len(numString):
        return False

    mid = len(numString) // 2
    if numString[:mid] == numString[mid:]:
        return False
    else:
        # sliding window until we see a non-unique character to determine the repeating pattern
        unique = set()
        r = 0
        is_valid = False
        for num in numString:
            if num not in unique:
                unique.add(num)
                r += 1
            else:
                break
                
        # at the end r points to the first duplicate character
        if len(unique) == len(numString):
            return True
            
        # loop in r-sized(possible duplicated subsring) chunks and compare the substrings
        prev_string = numString[:r]
        for i in range(r,len(numString),r):
            end = i+r
            # print(f"Index: {i},PrevString:{prev_string},Substring:{numString[i:end]}")
            if prev_string != numString[i:end]:
                is_valid = True
                break

            prev_string = numString[i:end]

        return is_valid

def sum_invalid_ids():
    res = 0
    try:
        with open(file_path,"r") as file:
            contents = file.read()
            ranges = contents.split(",")

            for r in ranges:
                start,end = map(int,r.strip().split("-"))
                for num in range(start,end+1):
                    # part one
                    # if not is_valid(str(num)):
                        # res += int(num)
                    # part two
                    if not is_valid_two(str(num)):
                        res += int(num)

            return res
    except Exception as e:
        print(f"Something went wrong: {e}")


print(sum_invalid_ids())
