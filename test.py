s = str(int("101101111110101011101111111111110111111"))
mod = 109 + 7
lis = s.split('0')
ans = 0
for i in lis:
    length = len(i) 
    ans += (length*(length+1))//2
    
print(ans%mod)