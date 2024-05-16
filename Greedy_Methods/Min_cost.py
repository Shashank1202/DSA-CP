'''Problem Link:|
https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
'''


if __name__== '__main__':
    v=49
    coins= [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    ans=[]
    n=len(coins)
    for i in range(n-1, -1, -1):
        while v>=coins[i]:
            v-=coins[i]
            ans.append(coins[i])
    print("The number of coins required is  :", len(ans))
    print("The coins that are require are ")
    for i in range(len(ans)):
        print(ans[i])
