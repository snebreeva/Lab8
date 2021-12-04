def kbig(nums, k):
    def sett(lis):
        print("oh shit here we go again")
        for i, a in enumerate(lis):
            
            for j, b in enumerate(lis):
                
                if j == i:
                    print(a, b)
                    continue

                                
                elif lis.index(a) == len(lis) - 1:
                    print(lis.index(a), 666, len(lis) - 1)
                    return lis
                
                elif a == b:
                    print(0000000000)
                    lis.remove(a)
                    
                    return sett(lis)
                else:
                    print(111, a, b)

    
    num_set = sett(nums)

    
    while k - 1 != 0:
        print(num_set)
        num_set.remove(max(num_set))
        k -= 1
    return max(num_set)

if __name__ == "__main__":
    a = [4, 4, 4, 52, 1, 2, 3]
    
    print(kbig(a, 5))
