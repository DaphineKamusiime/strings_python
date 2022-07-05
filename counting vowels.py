
name=input('enter your name')
count=0
for i in name:
   if i=='a'or i=='e' or i=='o' or i=='u' or i=='i':
       count=count+1
print('vowels =', count)

password1=input('enter a new password  ')
password2=input('re-enter password  ')
if password1==password2:
    print('thank you')
    if password1. islower() or password2. islower():
        print('they must be in the sanew case ')
    else:
        print('incorrect')        