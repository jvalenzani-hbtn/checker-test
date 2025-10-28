# goal: read a file and count non-empty lines
def count_non_empty(path)   # <- missing colon (SyntaxError)
    count = 0
    with open(path, "r") as f:
        for line in f
            if line.strip() != "":
                count += 1
        return count

result = count_non_empty("notes.txt")
print(f"Lines: {result}"
#            ^ unmatched parenthesis (SyntaxError)
