def isPalindrome(x):
    return str(x)==str(x)[::-1] 
    
print("On 123",isPalindrome(123))
print("On 424",isPalindrome(424))
print("On -121",isPalindrome(-121))
print("On 232",isPalindrome(232))

print("On 999",isPalindrome(999))
print("On -333",isPalindrome(-333))
print("On 9929",isPalindrome(9929))
print("On 20202",isPalindrome(20202))

print("On -3953",isPalindrome(-3953))
print("On -2",isPalindrome(-2))
print("On 9",isPalindrome(9))
print("On 88998",isPalindrome(88998))

print("On 100",isPalindrome(100))
print("On 3459",isPalindrome(3459))
print("On 19941",isPalindrome(19941))
print("On O4",isPalindrome(04))
