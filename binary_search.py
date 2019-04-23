
def sqrtRecurSearch(item, upper_bound, lower_bound = 0):
    midPoint = (upper_bound+lower_bound)/2
    if abs((midPoint)**2-item) <= .001:
        return(midPoint)
    else:
        if (midPoint)**2-item > .001:
            return sqrtRecurSearch(item = item, upper_bound = midPoint, lower_bound =  lower_bound)
        else:
            return sqrtRecurSearch(item = item, upper_bound = upper_bound, lower_bound = midPoint) 

x=4
print(sqrtRecurSearch(item=x, upper_bound = x))
x=9
print(sqrtRecurSearch(item=x, upper_bound = x))
x=3
print(sqrtRecurSearch(item=x, upper_bound = x))


def sqrtSearch(x):
    found = False
    lower = 0
    upper = x

    while not found:
        mid = (upper + lower)/2
        if abs((mid**2)-x) <= .001:
            found = True
        elif (mid**2)-x > .001:
            upper = mid
        else:
            lower = mid

    return mid

print(sqrtSearch(4))
print(sqrtSearch(9))
print(sqrtSearch(3))
