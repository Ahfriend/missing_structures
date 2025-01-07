'''
changes:
using onvex_hull_layers_function_11 that plot the convex in an ofset
in order to be able to plot a fram to the convex only.

'''

import sys
sys.path.append('/work/alonh/AUTO_FLOW')

from convex_hull_layers_function_11 import plot_convex 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
convex_inputs_file = '/work/alonh/Missing_structures/Figs/V3/Fig_1/fig_1_convex_inputes.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['a','b','c','d']
fig = plt.figure(figsize=(6.4,6.4))
ticks_len = []
for i,line in enumerate(lines):
  print (line)
  #if i > 0: break
  ax = plt.subplot(2,2,i+1)
  ax.axis('off')
  plt.box('off')
  splited_line = line.split()
  path = splited_line[0]
  input_file = splited_line[1]
  os.chdir(path)
  A_atom,proto_atom = input_file.split("_")[:2]

  #plt.yticks()
  
  for j,tick in enumerate(ax.yaxis.get_major_ticks()):
    if j ==1 or j==2 or j==3:
      tick.label1On = False
    else:
      tick.label1On = False



  #ax.set_xticks([0,0.5,1])
  ax.set_xticks([])
  ax.set_yticks([])
  #ax.set_xticklabels([0,0.5,1])
  #ax.tick_params(axis=u'both', which=u'both',length=-2,bottom=False)
 
  #ax.annotate(s=A_atom+proto_atom,xy=(-0.1,0.05),xycoords='axes fraction',fontsize=16,fontweight='bold') 
  #ax.annotate(s=A_atom+"$_x$"+proto_atom+"$_y$",xy=(0.66,0.05),xycoords='axes fraction',fontsize=16,fontweight='bold')

  ax.annotate(s=abc[i],xy =(-0.1,0.9) ,xycoords='axes fraction',fontsize=16,fontweight='bold' ) # letters for each graph


  plt.xlim(-0.1,1.6)
  #plt.ylim(,0.25)

  plot_convex(ax,[input_file],proto_atom,A_atom,title=None,out_file=None,graph_num=1,proto_graph=True,ptable=True,on_convex_only=None)
  plt.annotate(s=A_atom+proto_atom,xy=(1.4,-2.05),xycoords='axes fraction',fontsize=16,fontweight='bold')

plt.annotate(s='total energy [eV/Atom]',xy =(0.01,0.33) ,xycoords='figure fraction',fontsize=12,rotation=90 )
plt.annotate(s='ratio $y$/($x$+$y$)',xy =(0.4,0.01) ,xycoords='figure fraction',fontsize=12)



os.chdir(cwd)
#plt.savefig('fig_1_dpi_200.png',dpi=200)
#plt.savefig('fig_1_dpi_300.png',dpi=300)
plt.savefig('fig_1_dpi_400.png',dpi=400)
plt.savefig('fig_1.eps')
#plt.savefig('fig_1.svg',type='svg',dpi=1000)
#plt.savefig('fig_1.jpg',type='jpg',dpi=1000,quality=95)
#plt.savefig('fig_1.eps',type='eps',dpi=1000)
#plt.savefig('fig_1.tiff',type='tiff',dpi=1000)





