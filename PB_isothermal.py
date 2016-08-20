def add_component(lib):
    "add_component({'comp_name':C0})"
    F={}
    components=[]
    F.update(lib)
    for i,val in enumerate(F):
        components.append(val)
    return F,components

def c(F,Q):
    C = {}
    for i, val in enumerate(F):
        C[val] = F[val]/Q
    return C

def rate(tup, F,Q):
    stoic = tup[0]
    order = tup[1]
    C = c(F,Q)
    k = tup[2]
    comps = list(stoic.keys())
    r = k

    if 'auto' in stoic.keys():
        r *= C[stoic['auto']]**order

    for i in comps:
        if 'double' in stoic.keys() or 'half' in stoic.keys():            # to implement double and half only occuring in absence of ps
            if C['ps'] <= 0.01:
                r*= C[i]**order
            else:
                r == 0

        if i != 'auto':
            if stoic[i] <= 0:
                r *= C[i]**order
            else:
                pass
        else:
            pass

    return r


def mol_bal(components, reactions, F,Q):
    delta = {}
    for i in components:
        delta[i] = 0
        for j in reactions:
            rxn_rate = rate(j, F,Q)
            stoic = j[0]

            if i in stoic.keys():
                delta[i] += rxn_rate*stoic[i]

            else:
                pass

    return delta
