###function that checks password criteria
def strong_pass(user_password):
    import re
    hasUpper=re.compile(r'[A-Z]')
    hasLower=re.compile(r'[a-z]')
    hasDigit=re.compile(r'[0-9]')
    hasSomethingElse=re.compile(r'[-+!@#$%^&*_.,]')
    para1=hasUpper.search(user_password)
    para2=hasLower.search(user_password)
    para3=hasDigit.search(user_password)
    para4=hasSomethingElse.search(user_password)
    if len(user_password)<8:
        print('Your password is too short, need to be at least 8 char long')
    elif para1==None:
        print('Your password dont have upper cases, you have a weak password')
    elif para2==None:
        print('Your password dont have lower cases, you have a weak password')
    elif para3==None:
        print('Your password dont have digits, you have a weak password')
    elif para4==None:
        print('Your password dont have characters such as -+!@#$%^&*_.,, you have a weak password')
    else:
        print('You have a strong password, but you should consider using a long password consisting of multiple words with few typing errors ;)')

while True:
    print('Do you want to check your password strenght? (Y-yes, N-no)')
    answer=input()
    if answer=='Y':
        password=input('Please insert your password\n')
        strong_pass(password)
    elif answer=='N':
        break #better option than exit()
    else:
        print('Y means YES, N means NO, '+answer+' means nothing to this python script!')#protection against bad input
