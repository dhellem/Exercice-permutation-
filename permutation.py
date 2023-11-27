def permutations (liste):
    l=len (liste)
    if l<=1:
        return 0
    permutation=1
    for i in range(1,l+1):
        permutation *= i
    return permutation
    
liste =[3,4,34,1,6]
print (permutations(liste))