def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l]= n % 2
        n //= 2
        l += 1
<<<<<<< HEAD
        #aca estoy agregando comentario desde mi pc
=======
        #aca estoy agregando comentario desde github
>>>>>>> 5cedf33f3e31aa70d08d466e89651b751064236e
    for p in range(1, l//2): # <--- ACA ESTÁ EL CAMBIO!!!
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return =)
