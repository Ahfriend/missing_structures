'''
Changed convex_hull_layers_groups_extended_func_2 from 1. There is
'''
import sys 
sys.path.append('/work/alonh/AUTO_FLOW')
from convex_hull_layers_groups_extended_func_2_2 import convex_panles_periodic_table
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pickle

inputFiles = '/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S/Ti_S/Figs/extented_convex/Ti_S_convex_input.txt' 
A_atom = 'Ti'
P_atom = 'S'
figs = two_graphs_axins = convex_panles_periodic_table(inputFiles,A_atom,P_atom)


