file_path = "input.txt"

def count_xmas_one(lines: list[list[str]]) -> int:
    res = 0
    target = "xmas".upper()

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            # form the substrings
            rowString,colString = "",""
            fwdDiagString,bwdDiagString = "",""

            for i in range(4):
                # pass
                if c <= len(lines)-4:
                    rowString += lines[r][c+i].upper()
                if r <= len(lines) -4:
                    colString += lines[r+i][c].upper()
                if r <= len(lines)-4 and c <= len(lines[0])-4:
                    fwdDiagString += lines[r+i][c+i].upper()
                if c >= 3 and r <= len(lines)-4:
                    bwdDiagString += lines[r+i][c-i].upper()


            if rowString == target or rowString[::-1] == target:
                res += 1
            if colString == target or colString[::-1] == target:
                res += 1
            if fwdDiagString == target or fwdDiagString[::-1] == target:
                res += 1
            if bwdDiagString == target or bwdDiagString[::-1] == target:
                res += 1

    return res

def count_xmas_two(lines:list[list[str]]) -> int:
    res = 0
    target = "mas".upper()
    for r in range(1,len(lines)-1):
        for c in range(1,len(lines[0])-1):
            if lines[r][c] != "A":
                continue
                
            negativeSlopeCross = lines[r-1][c-1] + lines[r][c] + lines[r+1][c+1]
            positiveSlopeCross = lines[r+1][c-1] + lines[r][c] + lines[r-1][c+1]

            is_negativeSlope = negativeSlopeCross == target or negativeSlopeCross[::-1] == target
            is_positiveSlope = positiveSlopeCross == target or positiveSlopeCross[::-1] == target

            if is_negativeSlope and is_positiveSlope:
                res += 1

    return res

def count_xmas():
    try:
        with open(file_path,"r") as f:
            contents = f.readlines()
            lines = [list(line.strip()) for line in contents]
            # print(f"Rows{len(lines)},Cols: {len(lines[0])}")
            return count_xmas_two(lines)
    except Exception as e:
        print(f"Something went wrong: {e}")

print(count_xmas())
