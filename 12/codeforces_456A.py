def func():    
    n = int(input())
    
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    
    lst = sorted(lst, key=lambda x:x[0])
    
    res = 'Poor Alex'
    for i in range(n-1):
        if lst[i+1][0] > lst[i][0] and lst[i+1][1] < lst[i][1]:
            res = 'Happy Alex'
            break
        
    print(res)
    
if __name__ == '__main__':
    func()