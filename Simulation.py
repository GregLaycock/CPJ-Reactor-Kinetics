import Adjust_Kinetics
from PB_isothermal import *



def model_curves(Z):
    from numpy import linspace, array, append, squeeze, zeros
    from scipy.integrate import odeint

    plot_vals = {}
    F,components = add_component(Adjust_Kinetics.components)

  # Reactions( can be edited and rest will take care of itself. just remember to adjust paramters, limits and initials in Adjust_parameters.py!!!)


    reactions = Adjust_Kinetics.reactions

    # temperature curve parameters
    R = 8.314

    # initial temperatures
    T = Adjust_Kinetics.Specs['T']
    Qo = Adjust_Kinetics.Specs['Qo']
    Po = Adjust_Kinetics.Specs['Po']
    Fto = Adjust_Kinetics.Specs['Fto']
    M = Adjust_Kinetics.M
    D = Adjust_Kinetics.Specs['D']
    eps = Adjust_Kinetics.Specs['voidfrac']
    dp = Adjust_Kinetics.Specs['cat_part_diam']

# define ode function
    import numpy
    names = []
    initials = numpy.zeros(len(F))
    for i,name in enumerate(F):
        names.append(name)
        initials[i] = F[name]
    initials = list(initials)
    initials.append(Po)
    initials.append(Qo)


    def odesys(var,Z):
        Specs = Adjust_Kinetics.Specs
        Ft = 0
        F = {}
        for i,name in enumerate(names):
            F[name] = var[i]
        Nc = len(names)
        P = var[Nc]
        del_P = Pressure_drop(F,M,D,T,eps,dp,P)

        for i in range(Nc):
            Ft += var[i]

        Q = Qo*(Po/P)*(Ft/Fto)

        delta = Specs['pb']*Specs['A']*mol_bal(components, reactions, F,Q)   #dFi/dZ
        del_comps = numpy.zeros(len(names))

        for i, name in enumerate(names):
            del_comps[i] = delta[name]

        to_return = list(del_comps)
        to_return.append(del_P)

        return to_return

#   integrate differential equations

    solved = odeint(odesys, initials, Z)
    sol2 = solved.T
    F_vals = {}
    for i,name in enumerate(names):
        F_vals[name] = sol2[i]
    P_index = len(sol2) - 2
    plot_vals.update(F_vals)
    plot_vals['P'] = sol2[P_index]

    FT_vals = array([])
    for i,name in enumerate(F_vals):
        for j,val in enumerate(F_vals[name]):
            FT_vals[j] += val

    plot_vals['Q'] = Qo*(Po/plot_vals['P'])*(FT_vals/Fto)

    conversion = (Adjust_Kinetics.components[Adjust_Kinetics.converting] - F_vals[Adjust_Kinetics.converting])/Adjust_Kinetics.components[Adjust_Kinetics.converting]
    plot_vals['conversion'] = conversion
    return plot_vals


# defining optimization and plotting functions

def P_drop_curve(Z):
    curves = model_curves(Z)
    return curves['P']

def flow_curve(Z):
    curves = model_curves(Z)
    return curves['Q']


