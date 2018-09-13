k, s, t = map(int, input().split(' '))

def level_k(k):
    if k <=1:
        return 'ABC'
    else:
        return 'A'+level_k(k-1)+'B'+level_k(k-1)+'C'

def ABC(k, s, t):
    if s == t:
        return level_k(k)[s-1]
    elif k == 1:
        return level_k(k)[s-1:t]
    elif k<=6 and t-s>100:
            return level_k(k)
    else:
        M = 3*(2**(k-1))-1
        if s == M:
            return 'B'+level_k(k-1)[s-M:t-M]
        if t == M:
            return level_k(k-1)[s-M:]+'B'
        if s < M and M < t:
            return level_k(k-1)[s-M:]+'B'+level_k(k-1)[:t-M]
        if s>M:
            return ABC(k-1, s-M, t-M)
        if t<M:
            return ABC(k-1, s-1, t-1)

out_put = ABC(k, s, t)

print(level_k(7)[31:132])
print(out_put)
