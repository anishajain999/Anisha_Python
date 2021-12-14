import random
words = ['assignment','python','programming','condition', 'development', 'characters','different', 'newsletter', 'concrete', 'customer', 'analyse', 'target', 'economics', 'discussion', 'reminds', 'overconfident', 'delivery' ,'passion', 'hospitality', 'absent', 'intelligence']
print(len(words))

name = input("Enter your name: ")
print(f"Hi! {name} Good Luck")

print("Guess the Word")

word = random.choice(words)
l = word
# print(l)

word = list(word)
# w = []
for i in word:
    # w.append(i)
    # print(i)    
    j = random.randint(0, len(word)-1)
    word[j] = '_'
    # print(j)
    
i=0
while (i<7):
    for w in word:
        print(w)
    # print(word)
    
    if '_' in word:
        guess = input("guess a character: ")
        if len(guess) >1:
            print('invalid')
            break
        if guess not in l:
            i+=1

        for j in range(len(word)):
            # print(word[j], l[j])
            if word[j]=='_' and guess==l[j]:
                word[j]=guess       
    
    else:
        print("you win")
        break
else:
    print("you loose")