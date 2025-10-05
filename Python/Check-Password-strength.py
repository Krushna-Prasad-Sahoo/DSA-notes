"""
You are tasked with building a system to evaluate the strength of a given password. A password can earn up to 4 points, one for each of the following criteria:

The password length is at least 8 characters.
The password contains at least one uppercase letter (A-Z).
The password contains at least one lowercase letter (a-z).
The password contains at least one digit (0-9).
You must implement a function assess_password_strength(password) that uses nested helper functions to check each of these criteria and returns the total score.

Input Format
A single string password representing the password to be evaluated.
The password will contain only ASCII printable characters.

Output Format
Print a single integer — the strength score (between 0 and 4).
Sample 1:
Input: StrongP@ss1
Output: 4
"""

-----SOLUTION-----
def assess_password_strength(password):
    cnt=0

# Nested function to check length
    def check_length(pwd):
        nonlocal cnt
        if len(pwd)>=8:
            cnt+=1
        
    # Nested function to check for uppercase
    def has_uppercase(pwd):
        nonlocal cnt
        for i in pwd:
            if i.isupper():
                cnt+=1
                break
        
    # Nested function to check for lowercase
    def has_lowercase(pwd):
        nonlocal cnt
        for i in pwd:
            if i.islower():
                cnt+=1
                break

# Nested function to check for digits
    def has_digit(pwd):
        nonlocal cnt
        for i in pwd:
            if i.isdigit():
                cnt+=1
                break
    check_length(password)
    has_digit(password)
    has_lowercase(password)
    has_uppercase(password)
    return cnt

if __name__ == "__main__":
    password = input()
    print(assess_password_strength(password))
