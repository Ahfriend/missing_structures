import sys
sys.path.append('/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S')
from prototypes_distribution_in_columns_2 import prototypes_distribution_in_columns
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6.4,4))

# TaxSey
ax = plt.subplot(1,2,1)
input_file = '/andata2/alonh/missing_structures/Ta_Se/extended_convex_data.txt'
proto_atom = 'Se'
A_atom = 'Ta'
prototypes_distribution_in_columns(ax,input_file,proto_atom,A_atom)
ax.get_legend().remove()

# TixSy
ax = plt.subplot(1,2,2)
input_file = '/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S/Ti_S/extended_convex_data.txt'
proto_atom = 'S'
A_atom = 'Ti'
prototypes_distribution_in_columns(ax,input_file,proto_atom,A_atom)

plt.subplots_adjust(wspace = 0.5)
plt.savefig('structure_in_columns.png',dpi=1000)

