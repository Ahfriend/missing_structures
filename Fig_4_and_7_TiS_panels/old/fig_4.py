import sys 
sys.path.append('/work/alonh/AUTO_FLOW')
from convex_hull_layers_groups_extended_func import convex_panles_periodic_table

inputFiles = '/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S/Ti_S/Figs/extented_convex/Ti_S_convex_input.txt' 
A_atom = 'Ti'
P_atom = 'S'
convex_panles_periodic_table(inputFiles,A_atom,P_atom)
