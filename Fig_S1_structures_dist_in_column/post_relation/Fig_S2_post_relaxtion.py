import sys
#sys.path.append('/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S')
sys.path.append('/work/alonh/Missing_structures/Figs/V3/Fig_S1_structures_dist_in_column/')

from prototypes_distribution_in_columns_3_1 import prototypes_distribution_in_columns
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#update the extended convex

exteded_convex_path = '/work/alonh/Missing_structures/tables/extended_convex_relaxed_sym/post_relaxtion'

# 
def xtick(ax):
  plt.xticks(range(1,19,2),size=6)
  ax.xaxis.set_minor_locator(MultipleLocator(2)) 
  return

fig = plt.figure(figsize=(6.4,4))

# TixSy
print ("========== TixSy ==============")

ax = plt.subplot(1,3,1)
input_file = exteded_convex_path+'/Ti_S_exteded_convex_after_relaxtion.txt'
proto_atom = 'S'
A_atom = 'Ti'
prototypes_distribution_in_columns(ax,input_file,proto_atom,A_atom)
ax.get_legend().remove()
xtick(ax)
plt.ylabel('structure type')



# TaxSey
print ("========== TaxSey ==============")
ax = plt.subplot(1,3,2)
input_file = exteded_convex_path+'/Ta_Se_extended_convex.txt'
proto_atom = 'Se'
A_atom = 'Ta'
prototypes_distribution_in_columns(ax,input_file,proto_atom,A_atom)
ax.get_legend().remove()
xtick(ax)
plt.xlabel('periodic table column number')


# CuS

ax = plt.subplot(1,3,3)

input_file = exteded_convex_path+'/Cu_S_extended_convex.txt'
proto_atom = 'S'
A_atom = 'Cu'
prototypes_distribution_in_columns(ax,input_file,proto_atom,A_atom)
xtick(ax)
plt.legend(loc=1,bbox_to_anchor=(1.05, 1.55555))


plt.subplots_adjust(left=0.15, bottom=None, right=None, top=0.85, wspace=None, hspace=None)

plt.subplots_adjust(wspace = 0.8)
plt.suptitle('After relaxation',size =16)
plt.savefig('structure_in_columns_1_dpi_400.png',dpi=400)
#plt.savefig('structure_in_columns_1.pdf',format ='pdf')
plt.savefig('structure_in_columns_1.eps',format ='eps')


