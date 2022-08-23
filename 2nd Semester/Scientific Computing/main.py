def falsi(f, s, t, e, m):
    fs, ft = f(s), f(t)

    for i in range(m):
        r = (fs * t - ft * s) / (fs - ft)
        if abs(f(r)) <= e:
            break
        fr = f(r)

        if fr * ft > 0:
            t = r
            ft = fr
        elif fs * fr > 0:
            s = r
            fs = fr
        else:
            break
    return r

print(falsi(lambda x: x ** 3 - 2 * x - 5, 2.0, 3.0, 0.001, 100))
