def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x<0 else 1
    x *= sign
    rlt = 0
    while x!=0:
        res = x%10
        rlt = rlt*10 + res
        print 'res =' + str(res)
        print 'rlt =' + str(rlt)
        # if((_rlt - res)/10 != rlt):
        #     return 0
        if rlt>2147483647 : 
            return 0
        x = x/10
    return sign*rlt

print reverse(-987)

    