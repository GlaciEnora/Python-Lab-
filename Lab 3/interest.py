def simp_intr(p, t, r = 11.5):
    return (p*r*t)/1200

def comp_intr(p, t, r = 11.5):
    return p*(1+((r*12)/(100*t)))**(t/12)
