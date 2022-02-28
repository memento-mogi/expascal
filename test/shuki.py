import objective

def shuki(pas):
    ln = 5
    p = pas.tolist()[0]
#    print(p)
    lis = p[:ln]
    before = p[1]
    t = 1
    buf = p[1:(ln+1)]
    print(buf)
    counter = 0
    for i in p[ln+1:]:
        if buf == lis:
            if (t%3) == 0:
                print(t)
                counter += 1
        if counter >= 10:
            break;
        t += 1
        buf = buf[1:]
        buf.append(i)
        
pask = objective.Pascal(3, 1000, 0)
tri = pask.get_contents()
for i in range(100):
    print(i)
    shuki(tri[i])
    print("")

