def dp_frog_jump(arr, n, dp):
    if n == 0:
        return 0
    
    if dp[n] != -1:
        return dp[n]
    if n > 1:
        right = dp_frog_jump(arr, n - 2, dp) + abs(arr[n] - arr[n-2])

    else:
        right = float('inf')

    left = dp_frog_jump(arr, n-1, dp) + abs(arr[n] - arr[n-1])
        
    dp[n] = min(left, right)
    return dp[n]
  
  
  
  if __name__ == '__main__':
    
    integer_input = input()
    n = int(integer_input)
    
    lst = input()
    arr = lst.split()
    ## converting to integers
    for i in range(len(arr)):
      arr[i] = int(arr[i])

    ## initializing the dp array.
    dp = [-1] * (n+1)
    answer = dp_frog_jump(arr, n, dp)
    print(answer)
