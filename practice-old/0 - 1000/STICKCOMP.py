# cook your dish here
T = int(input())
for _ in range(T):
    
    n = int(input())
    nums = list(map(int, input().split()))
    res = nums[0]
    
    for i in range(n-1):
        if res < nums[i+1]:
            # res = nums[i]
            # continue
        # else:
            res = nums[i+1]

    for j in range(n):
        if res == nums[j]:
            final_res = j+1
            break
                
    # print(res)
    print(final_res)
            