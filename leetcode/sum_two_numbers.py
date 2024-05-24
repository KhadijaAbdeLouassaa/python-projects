
def sum_two_nums(arr, target):
    for i in range(len(arr)):
        
        for j in range(i+1,len(arr)):
            
            if arr[i] + arr[j] == target:
                return i,j
                
                
arr = [-3,4,3,90]
target = 94    
print(sum_two_nums(arr, target))
            