'''
This is the code of  S015:ABC文字列  on paiza.jp
'''


k, s, t = map(int, input().split(' ')) #Standard Data

# Generate level k string.
def level_k(k):
    if k <=1:
        return 'ABC'
    else:
        return 'A'+level_k(k-1)+'B'+level_k(k-1)+'C'

# generate the section of the level k string.
def ABC(k, s, t):
    if s == t:
        return level_k(k)[s-1]
    elif k<=15: #make sure from s to t will be completely included in level_k(k-1)
        return level_k(k)[s-1:t]
    else:
        M = 3*(2**(k-1))-1 #midpoint
        if s == M: #special case 1
            return 'B'+level_k(k-1)[s-M:t-M]
        if t == M: #special case 2
            return level_k(k-1)[s-M:]+'B'
        if s < M and M < t: #final general case
            return level_k(k-1)[s-M:]+'B'+level_k(k-1)[:t-M]
        if s>M: #recusive case 1: the demand string section is included in the latter half
            if t < 2*M-1:
                return ABC(k-1, s-M, t-M)
            if t == 2*M-1:
                return ABC(k-1, s-M, t-M-1)+'C'
        if t<M: #recusive case 2: teh demand string section is inclued in the former half
            if s>1:
                return ABC(k-1, s-1, t-1)
            if s == 1:
                return 'A'+ABC(k-1, s, t-1)

out_put = ABC(k, s, t)
print(out_put)
