import sys 
sys.path.append('/work/alonh/AUTO_FLOW')
from convex_hull_layers_groups_extended_func import convex_panles_periodic_table

inputFiles = '/andata2/alonh/missing_structures/Cu_S/Figs/extended_convex/Cu_S_convex_input.txt' 
A_atom = 'Cu'
P_atom = 'S'
convex_panles_periodic_table(inputFiles,A_atom,P_atom)
