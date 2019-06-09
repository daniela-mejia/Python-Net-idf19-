
def mystery(data, pos, n):
    result = set()
    for i in range(0,n):
        for j in range (0,n):
            result.add(data[i+pos][j+pos])
    print  (result)
    
    
def main():
    data =  [[8,2,7,8,2,1], [1,5,1,7,4,7],[5,9,6,7,3,2],[7,8,7,7,7,9],[4,2,6,9,2,3],[2,2,8,1,1,3]]
    pos = 3
    n = 3
    mystery (data, pos, n)  
    print(' ')

main()