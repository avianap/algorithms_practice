

def find_permutations_location(short_str, long_str):
    """Find all the permutations of a smaller string "short_str" inside a longer string "long_str"

    Args:
        short_str (string): string that is shorter than long_str
        long_str (string): string that is longer than short_str

    Returns:
        list: a list of the starting locations of each permutation match of short_str in long_str
    """
    locations = []

    for location in range(len(long_str)-len(short_str)):
        a_copy = short_str
        for checks in range(len(short_str)):
            if long_str[location+checks] in a_copy:
                a_copy = a_copy.replace(long_str[location + checks],'',1)
                if len(a_copy) == 0:
                    locations.append(location)
            else:
                break

    return locations
# Python function to print permutations of a given list 
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
       print('item {}'.format(m))
       print('whole list {}'.format(lst))
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 

       # Generating all permutations where m is first 
       # element 
       print('permuting {}'.format(remLst))
       for p in permutation(remLst): 
           print('current l {}'.format(l))
           l.append([m] + p) 
           print('added to l: {}'.format([m]+p))
           print('new l {}'.format(l))
    return l 
  
  
# Driver program to test above function 
data = list('123') 
for p in permutation(data): 
    print p 

short_str = 'abbc'
long_str = 'bbcaacbbacaaaaaa'
x = find_permutations_location(short_str, long_str)
print(short_str)
print(long_str)
print(x)

        
