
reactions = [({'HCL': -1, 'LDH': -1}, 1, 1),
             ({'HCL': 1, 'pas': -1, 'rad': 1,'auto': 'HCL'}, 1, 1),
             ({'pas': -1, 'HCL': 1, 'rad': 1}, 1, 1),
             ({'rad': -1, 'ps': -1}, 1, 1),
             ({'rad': -1, 'dp': 1}, 1, 1),
             ({'rad': -1, 'xl': 1}, 1, 1),
             ({'rad': -1, 'half': 2}, 2, 1),         # half
             ({'rad': -2, 'double': 1}, 1, 1)]       # double


components = {'HCL': 0,      # With initial
              'rad': 0,
              'dp': 0,
              'xl': 0,
              'double': 0,
              'half': 0,
              'none': 1}

converting = 'Co'

Ft_o =0
for i,name in enumerate(components):
    Ft_o += components[name]

Specs = {'Qo':10,'Po':5,'T':373,'Fto':Ft_o, 'D':0.5,'pb':2,'lengh':2,'cat_pat_diam':0.001,'voidfrac':0.4}

# T is only important if we want to include non isothermal reactions or
#  if we have kinetics at different T than operating T
#  otherwise just spec it as 0 or whatever as long as k values are correct it wont matter

import math
Specs['A'] = Specs['D']**2 * math.pi/4.

#component viscosity relations##

A = {'xy':-19.763 ,'pa': -19.763 ,'ma': -19.763 ,'O2':44.224 ,'CO2':11.811 ,'inert':42.606 ,'H2O':-36.826 }
B = {'xy':2.8022e-1 ,'pa':2.8022e-1,'ma':2.8022e-1 ,'O2':5.6200e-01 ,'CO2':4.9838E-01 ,'inert':4.7500e-1 ,'H2O':4.2900e-1 }
C = {'xy': -5.9293e-5,'pa':-5.9293e-5 ,'ma':-5.9293e-5,'O2':-1.1300e-04 ,'CO2':-1.0851e-04 ,'inert':-9.8800e-05 ,'H2O':-1.6200e-5 }


# molar masses of components

M = {'comp1':10,'comp2':2}