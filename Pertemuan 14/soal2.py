def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Kalimat :"))
if(is_palindrome(a)==True):
    print("palindrome")
else:
    print("bukan palindrome")