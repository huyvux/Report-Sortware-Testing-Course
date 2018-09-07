# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
# 
# Implement the Luhn Checksum algorithm as described above.

# is_luhn_valid takes a credit card number as input and verifies 
# whether it is valid or not. If it is valid, it returns True, 
# otherwise it returns False.

def digits_of(n):
    return [int(d) for d in str(n)]

def is_luhn_valid(n):
    digits = digits_of(n)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        test = digits_of(d*2)
        checksum += sum(test)
    checksum = checksum % 10
    return checksum == 0
    
def test():
    is_true = is_luhn_valid( 4532015112830366 )
    assert is_true
    #is_true = is_luhn_valid( 4532015112830363 )
    #assert is_true
    is_true = is_luhn_valid( 45320151 )
    assert is_true
    pass

test()