import re
def strength(s) :
    stren = 0
    if len(s) < 6 :
        return "wery weak password!!"
    elif len(s) >= 8:
        strength += 1
    
    if(re.search(r"[A-Z]",s)):
        strength += 1

    if(re.search(r"[a-z]",s)):
        strength += 1

    if(re.search(r"\d",s)):
        strength += 1

    if(re.search(r"[@#$%^&*()-=]",s)):
        strength += 1
    
    if strength <= 2:
        return "weak password"
    
    elif strength == 3 or strength == 4:
        return "Medium password"
    
    else :
        return "Strong Password"
