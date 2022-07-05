subject=input('enter your fav subject')
for letter in subject:
    print(letter,end='-')

poem=('if you can use noyhing Lord, then use me')
print(poem)
start=int(input('enter a starting number'))    
end=int(input('enter an ending number'))
print(poem[start:end])

wordd=input('Enter a word: ')
length=len(wordd)
num=1
for i in wordd:
    position=length-num
    letter =wordd[position]
    print(letter)
    num=num+1



