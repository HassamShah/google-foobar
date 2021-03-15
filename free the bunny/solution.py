from itertools import combinations

def answer(num_buns, num_required):
    buns = [[] for i in range(num_buns)]
    if num_required == 0:
        return buns
    start = 0
    for c in combinations(buns, num_buns - num_required + 1):
        for item in c:
            item.append(start)
        start += 1
    return buns
dodge the laser
def floor_root_2(x):
    sqrt_2 = long("41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157273501384623091229702492483605585073721264412149709993583141322266592750559275579995050115278206")
    ten_power = long("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
    ret = long((x*(x+1))/2)
    if x <= 10:
        for i in range(x):
            ret += long((sqrt_2*(i+1))/ten_power)
        return ret
    last_term = long((sqrt_2 * x) / ten_power)
    ret += (x * last_term ) - long((last_term * (last_term + 1))/2) - floor_root_2(last_term)
    return ret
    
def answer(str_n):
    return str(floor_root_2(long(str_n)))
