
def hashedprint(func):
    '''a decorator funtion'''
    def wrapper(*args,**kw):
        '''wrapping funtion '''
        print('##################################')
        ret = func(*args,**kw)
        print('##################################')
        return ret
    return wrapper


a,b = 2,5
@hashedprint # decorator funtion is calling 
def doin(a,b):
    print('this function is exicuting now')
    return a + b

print(doin(a,b))

#-------------------------------------------------------#
# The output as shown below
# ##################################
# this function is exicuting now
# ##################################
# 7