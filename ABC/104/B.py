import  re
S = input()

if S[0] == 'A'  and S[1].islower() and S[2:-1].count('C') ==1 and S[-1].islower() and len(re.findall('[A-Z]', S[2:-1])) ==1:
    print('AC')
else:
    print('WA')
