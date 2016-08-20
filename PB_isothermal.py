import Adjust_Kinetics

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



#########################################################from CRO funcs######################
def pp(component,F,P):      #KPA
    mf = mol_frac(component,F)
    partial = P*mf

    return partial

def Q(F, P, T):
    'm3/hr'
    R = 8.314
    F_tot =  FT(F)
    Q_val = F_tot*R*T/P
    return Q_val

def FT(F):
    FT_val = 0
    for i in F:
        FT_val += F[i]

    return FT_val

def mol_frac(component,F):
    FT_val = FT(F)
    F_val = F[component]
    mf = F_val/FT_val
    return mf
def mass_flow(F,M):
    mf = 0
    for i in F:
        mf += F[i] * M[i]
    return mf

def pho(F,T,P,M):
    mt = 0
    for i in F:
        ni = F[i]
        mi = F[i] * M[i]
        mt += mi

    p = mt/Q(F,P,T)
    return p

def G(F, M):
    'units of kg/hr.m2'
    mf = mass_flow(F, M)
    A = Adjust_Kinetics.Specs['A']
    val = mf/A
    return val

def Mu(T):
    'gives viscosity in kg/m.hr or pa.hr'

    A = Adjust_Kinetics.A
    B = Adjust_Kinetics.B
    C = Adjust_Kinetics.C

    f = {}
    for i in A:
        if A[i] != 'interp':
            val = A[i] + B[i]*T + C[i]*T**2
            f[i] = val*(10**(-7)) * 3600 # kg/m.sec *3600 sec/hr ---> kg/m.hr
        else:
            pass
    return f


def Mu_avg(F, T):
    mu_av = 0
    for i in F:
        mf = mol_frac(i, F)
        mu_i = mf * Mu(T)[i]
        mu_av += mu_i

    return mu_av



def Pressure_drop(F,M,D,T,eps,dp,P):

    'units are important here(empiracle equation)! G, F have units in /hr so /3600 '
    g = G(F, M, D)/3600   #/sec
    mu = Mu_avg(F, T)/3600  # kg/mhr ---> kg/ms
    p = pho(F,T,P,M)
    delta_P = (- g/(p*dp)) * ((1-eps)/eps**3) * (150* mu*(1-eps)/dp + 1.75*g)   # in PA
    val = delta_P/1000.                                                            # in kpa
    return val