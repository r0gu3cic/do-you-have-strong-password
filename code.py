##Function that checks password
def strongPass(StrongPassword):
    import re
    hasUpper=re.compile(r'[A-Z]')
    hasLower=re.compile(r'[a-z]')
    hasDigit=re.compile(r'[0-9]')
    hasSomethingElse=re.compile(r'[-+!@#$%^&*_.,]') ##(-) se gleda kao od do pa mora na kraju ili na pocetku
    para1=hasUpper.search(StrongPassword)
    para2=hasLower.search(StrongPassword)
    para3=hasDigit.search(StrongPassword)
    para4=hasSomethingElse.search(StrongPassword)
    if len(StrongPassword)<8:
        print('Your password is too short, need to be at least 8 char long')
    elif para1==None:
        print('Your password dont have upper cases, you have WEAK password')
    elif para2==None:
        print('Your password dont have lower cases, you have WEAK password')
    elif para3==None:
        print('Your password dont have digits, you have WEAK password')
    elif para4==None:
        print('Your password dont have characters such as -+!@#$%^&*_.,, you have WEAK password')
    else:
        print('You have STRONG password')
        
while True:
    print('Do you want to check your password strenght? (Y-yes, N-no)')
    answer=input()
    if answer=='Y':
        password=input('Please insert your password\n')
        strongPass(password)
    elif answer=='N':
##        exit()
        break #better option than exit()
    else:
        print('Y means YES, N means NO, '+answer+' means nothing to me!') #protection 
