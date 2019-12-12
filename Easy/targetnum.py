nums = [2,3,5,6,7,11,15,30]

#  nums = [1,2,4,4,13]  target = 8
target = 13

# given a target number return a PAIR of numbers that equal the target number (target)   
# ex: [2,11]  if no pair exists return -1

def twoPair(array, target):
    
    for i in range(len(array)):
        for j in range(1,len(array)):
            if array[i]+array[j]==target:
                return [array[i],array[j]]
            if array[i]+array[j]>target:
                break
    return None



def twoPairHash(a,target):
    numberNeeded={}
    for i in a:
        if i in numberNeeded:
            return [numberNeeded[i], i]
        else:
            numberNeeded[target-i]=i
    return None
print(twoPairHash(nums, target))