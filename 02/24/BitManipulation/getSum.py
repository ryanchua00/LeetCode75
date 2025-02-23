class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 001100  010101
        # 001000
        # 010101
        # 011101
        carry = (a & b) << 1
        curr = a ^ b
        while carry & curr != 0:
            temp = carry
            temp2 = curr
            carry = (temp & temp2) << 1
            curr = temp ^ temp2

        return carry | curr
    '''
    010100
    011110
    carry = 101000
    curr =  001010

    temp = 101000
    temp2= 001010


    '''
