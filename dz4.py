text = input().strip() 
text_l = text.split('.') 
text_l = '!'.join(text_l).split('!') 
text_l = '?'.join(text_l).split('?') 
for i in range(1, len(text_l)+1): 
print(i, text_l[i-1]+'.')