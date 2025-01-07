'''
Runs all the script that creates the figures for the paper.
'''
import os
from sys import path
Errors = []
# Fig 1
path.append('/work/alonh/Missing_structures/Figs/V3/Fig_1')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_1')
try:
  import fig_1_plot_convex_panels_v4
except:
  Errors.append('Fig_1')  

# Fig 2

path.append('/work/alonh/Missing_structures/Figs/V3/Fig_2')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_2')
try:
 import fig_2_plot_convex_panels_v4
except:
  Errors.append('Fig_2')
 
# Fig 3
path.append('/work/alonh/Missing_structures/Figs/V3/Fig_3_Near_Neighbors')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_3_Near_Neighbors')
try:
  import plot_convex_panels
except:
  Errors.append('Fig_3')

# Fig 4 & 7
path.append('/work/alonh/Missing_structures/Figs/V3/Fig_4_and_7_TiS_panels')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_4_and_7_TiS_panels')
try:
  import fig_4
except:
  Errors.append('Fig_4')
 
# Fig 5
path.append('/work/alonh/Missing_structures/Figs/V3/Fig_5_TaS_panels')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_5_TaS_panels')
try:
  import fig_5
except:
   Errors.append('Fig_5')

# Fig 6
path.append('/work/alonh/Missing_structures/Figs/V3/Fig_6_CuS_panels')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_6_CuS_panels')
try:
  import fig_6
except:
  Errors.append('Fig_6')


# Fig 7 - See Fig 4

# Fig 8 
path.append('/work/alonh/Missing_structures/Figs/V3/Fig_8_structures_dist_in_column')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_8_structures_dist_in_column')
try:
  import strucutre_distribution_in_columns_1
except:
  Errors.append('Fig_8')

# Fig 9 
path.append('/work/alonh/Missing_structures/Figs/V3/Fig_9_mp_aflow_comparison')
os.chdir('/work/alonh/Missing_structures/Figs/V3/Fig_9_mp_aflow_comparison')
try:
  import mp_aflow_plot_convex_panels_4_test
except:
  Errors.append('Fig_9')

print ('Figure with errors:')
for i in Errors:
  print (i)
