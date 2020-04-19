def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l]= n % 2
        n //= 2
        l += 1
        #aca estoy agregando comentarioo
    for p in range(1, l//2): # <--- ACA ESTÁ EL CAMBIO!!!
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return =)
