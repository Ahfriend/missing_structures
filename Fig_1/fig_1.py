'''
changes:
using convex_hull_layers_function_11 that plot the convex in an ofset
in order to be able to plot a frame to the convex only.

v_5

trying to add arrows.

'''

import sys
#sys.path.append('/work/alonh/AUTO_FLOW')

from convex_function_fig_1_and_2 import plot_convex 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
convex_inputs_file = '/work/alonh/Missing_structures/Figs/V3/Fig_1/fig_1_convex_inputes.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['(a)','(b)','(c)','(d)']
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
 
  # Change font size for xticks and yticks
  ax.tick_params(axis='x', labelsize=7)
  ax.tick_params(axis='y', labelsize=8)


  plt.xlim(-0.1,1.6)

  axins = plot_convex(ax,[input_file],proto_atom,A_atom,title=None,out_file=None,graph_num=1,proto_graph=True,ptable=None,on_convex_only=None)
  
#----  Graph title for each graph e.g. TiS
  plt.annotate(A_atom+proto_atom,xy=(0.0,1.1),xycoords='axes fraction',fontsize=7,fontweight='bold',color = 'black')
  plt.annotate(text=abc[i],xy =(-0.1,1.1) ,xycoords='axes fraction',fontsize=8,color='black')        


#---- TiS  new sturcture annotation -------
  if i == 1:
    axins.annotate("Ti$_{3}$Se$_{4}$", xy=(0.62,-1.654), xytext=(0.8,-1.6),xycoords='data',arrowprops=dict(arrowstyle="->",color='c'),fontsize=10,color='c',fontweight='bold')

#-----  CuS new satructure annotation-------
  if i == 0:   
    axins.annotate("Cu$_{3}$Se$_{2}$", xy=(0.37, -0.217), xytext =(0.00, -0.2),xycoords='data',arrowprops=dict(arrowstyle="->",color='c'),fontsize=10,color='c',fontweight='bold')

#----- Axis titles ------------------------
plt.annotate(text='formation energy [eV/Atom]',xy =(0.0,0.4) ,xycoords='figure fraction',fontsize=8,rotation=90,color='black' )
plt.annotate(text='$y$/($x$+$y$)',xy =(0.5,0.01) ,xycoords='figure fraction',fontsize=8,color='black')


os.chdir(cwd)
plt.subplots_adjust(left=0.07, right=1.12, top=1.17, bottom=0.07, wspace=-0.1, hspace=-0.2)
plt.savefig('fig_1.png',dpi=400)
plt.savefig('fig_1.pdf')






