from matplotlib.backends.backend_pdf import PdfPages
from time import time as tm
from Simulation import model_curves
from matplotlib import pyplot as plt
import Adjust_Kinetics
from numpy import linspace

length = Adjust_Kinetics.Specs['lengh']
Z = linspace(0,length,1000)
t = tm()
with PdfPages('all_curves_1.pdf') as pdf:

        #Plotting to pdf

        curves = model_curves(Z)


        title = 'Molar flow rates'

        from matplotlib.pyplot import *
        fig_P = figure()
        fig_P.suptitle('P drop curve')
        plot(Z, curves['P'], label='P(Kpa)')

        legend()

        fig_Q= figure()
        fig_Q.suptitle('Flow rates')
        plot(Z, curves['Q'], label='volumetric gas flow rate(m3/s)')

        legend()
        fig_species = figure()
        fig_species.suptitle(title)

        Nc = len(curves) - 3
        for i, name in enumerate(Adjust_Kinetics.components):
            plot(Z, curves[name], '--', label=name)

        legend()

        fig_conversion = figure()
        fig_conversion.suptitle('conversion of',Adjust_Kinetics.converting)
        plot(Z,curves['conversion'],'r-')
        plot.axis()

        pdf.savefig(fig_Q)
        pdf.savefig(fig_P)
        pdf.savefig(fig_species)
        pdf.savefig(fig_conversion)

        plt.close(fig_Q)
        plt.close(fig_P)
        plt.close(fig_species)
        plt.close(fig_conversion)

elapsed = tm() - t
print('*******************')
print('elapsed time (min) =', elapsed/60.)