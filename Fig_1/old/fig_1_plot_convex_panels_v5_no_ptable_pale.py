'''
changes:
using convex_hull_layers_function_11 that plot the convex in an ofset
in order to be able to plot a frame to the convex only.

v_5

trying to add arrows.

'''

import sys
sys.path.append('/work/alonh/AUTO_FLOW')

from convex_hull_layers_function_11_3_1 import plot_convex 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
convex_inputs_file = '/work/alonh/Missing_structures/Figs/V3/Fig_1/fig_1_convex_inputes_pale_colors.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['a','b','c','d']
fig = plt.figure(figsize=(6.4,6.4))
ticks_len = []
axes = []
for i,line in enumerate(lines):
  print (line)
  #if i  > 1: break
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

  ax.annotate(text=abc[i],xy =(-0.1,-0.05) ,xycoords='axes fraction',fontsize=10,fontweight='bold',color='gainsboro') # letters for each graph


#  if i == 1:
#    ax.annotate(s='Ti3S4',xy=(0.5,0.5),xycoords='axes fraction')

  plt.xlim(-0.1,1.6)


  axins = plot_convex(ax,[input_file],proto_atom,A_atom,title=None,out_file=None,graph_num=1,proto_graph=True,ptable=None,on_convex_only=None)
  #axins.tick_params(labelsize=4)

  plt.annotate(text=A_atom+proto_atom,xy=(0,1.2),xycoords='axes fraction',fontsize=16,fontweight='bold',color = 'silver')


####  TiS  #####
  if i == 1:
    #axins.annotate("Ti$_{3}$Se$_{4}$", xy=(0.571,-1.654), xytext=(0.75,-1.6),xycoords='data',arrowprops=dict(arrowstyle="->",color='c'),color='c')
    axins.annotate("new Ti$_{3}$S$_{4}$\ncompound", xy=(0.62,-1.654), xytext=(0.8,-1.6),xycoords='data',arrowprops=dict(arrowstyle="fancy",color='black'),color='black',fontsize=6)
    axins.plot(0.571,-1.6537322, marker='o', markersize=6, markeredgecolor='c', markerfacecolor='None')

#### CuS  #####
  if i == 0:   
    #axins.annotate("Cu$_{3}$Se$_{2}$", xy=(0.4,-0.217), xytext=(-0.05, -.24),xycoords='data',arrowprops=dict(arrowstyle="->",color='c'),color='c')
    axins.annotate("new Cu$_{3}$S$_{2}$\ncompound", xy=(0.37, -0.217), xytext =(-0.05, -0.25),xycoords='data',arrowprops=dict(arrowstyle="fancy",color='black'),color='black',fontsize=6 )
    axins.plot(0.4,-0.2168417, marker='o', markersize=6, markeredgecolor='c', markerfacecolor='None')

plt.annotate(text='formation energy [eV/Atom]',xy =(0.01,0.33) ,xycoords='figure fraction',fontsize=12,rotation=90,color='lightgray' )
plt.annotate(text='$y$/($x$+$y$)',xy =(0.4,0.01) ,xycoords='figure fraction',fontsize=12,color='lightgray')




os.chdir(cwd)

plt.savefig('fig_1_v5_no_ptable_dpi_400.png',dpi=400)
plt.savefig('fig_1_v5_no_ptable.eps')






