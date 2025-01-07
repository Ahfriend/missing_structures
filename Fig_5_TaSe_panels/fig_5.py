import sys 
sys.path.append('/work/alonh/AUTO_FLOW')
from convex_hull_layers_groups_extended_func_0_1 import convex_panles_periodic_table

inputFiles = '/andata2/alonh/missing_structures/Ta_Se/Figs/extended_convex/Ta_Se_convex_input.txt' 
A_atom = 'Ta'
P_atom = 'Se'
convex_panles_periodic_table(inputFiles,A_atom,P_atom)
