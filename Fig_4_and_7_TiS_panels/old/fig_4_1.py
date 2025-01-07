import sys 
sys.path.append('/work/alonh/AUTO_FLOW')
from convex_hull_layers_groups_extended_func_1 import convex_panles_periodic_table
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pickle

inputFiles = '/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S/Ti_S/Figs/extented_convex/Ti_S_convex_input.txt' 
A_atom = 'Ti'
P_atom = 'S'
figs = two_graphs_axins = convex_panles_periodic_table(inputFiles,A_atom,P_atom)



#fig = figs[1]
#two_graphs_axins[1][3].annotate("AsTi$_{3}$", xy=(0.25,-0.913), xytext=(0.0, -1.5),xycoords='data',arrowprops=dict(arrowstyle="->",color='c'),color='c',fontsize=8)


#plt.savefig('test')
