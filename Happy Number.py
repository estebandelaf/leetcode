# Write an algorithm to determine if a number is "happy".
# https://leetcode.com/problems/happy-number

class Solution :
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n) :
        if n < 1 or not isinstance(n, int) :
            return False
        resultados = []
        while True :
            n = self.getSumaCuadrados(n)
            if n == 1 or n in resultados :
                break
            resultados.append(n)
        if n == 1 :
            return True
        else :
            return False
    def getSumaCuadrados(self, n) :
        suma = 0
        while n > 0 :
            number = n%10
            n -= number
            n /= 10
            suma += number * number
        return suma

if __name__ == "__main__" :
    s = Solution()
    for i in range(1,100) :
        if s.isHappy(i) :
            print (i, "is happy number")
