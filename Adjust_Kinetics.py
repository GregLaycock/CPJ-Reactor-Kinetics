
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

Ft_o =0
for i,name in enumerate(components):
    Ft_o += components[name]

Specs = {'Qo':10,'Po':5,'T':373,'Fto':Ft_o, 'D':0.5,'pb':2}
# T is only important if we want to include non isothermal reactions or
#  if we have kinetics at different T than operating T
#  otherwise just spec it as 0 or whatever as long as k values are correct it wont matter

import math
Specs['A'] = Specs['D']**2 * math.pi/4.