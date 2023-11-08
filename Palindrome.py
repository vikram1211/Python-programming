class Solution:
     def isPalindrome(self, x):
          y=str(x)
          z=y[::-1]
          if y==z:
               return True
          else:
               return False
sol=Solution()
x=int(input("enter the number "))
if sol.isPalindrome(x):
     print("the number is a palindrome")
else:
     print("the number is not a palindrome")       

