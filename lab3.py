def find_dominator(arr):
    if not arr:
        return -1
    
    candidate = None
    count = 0
    
    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    if candidate is not None:
        occurrence = arr.count(candidate)
        if occurrence > len(arr) // 2:
            return candidate
    
    return -1

example = [3,4,3,2,3,1,3,3]
print(find_dominator(example))  

