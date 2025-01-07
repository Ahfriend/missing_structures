'''
changes:
using onvex_hull_layers_function_11 that plot the convex in an ofset
in order to be able to plot a fram to the convex only.

'''

import sys
sys.path.append('../Fig_1')

from convex_function_fig_1_and_2 import plot_convex 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
convex_inputs_file = '/work/alonh/Missing_structures/Figs/V3/Fig_2/fig_2_convex_inputes.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['(a)','(b)','(c)','(d)']
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

  ax.set_xticks([])
  ax.set_yticks([])


  plt.xlim(-0.1,1.6)

 
  ax = plot_convex(ax,[input_file],proto_atom,A_atom,title=None,out_file=None,graph_num=1,proto_graph=True,ptable=None,on_convex_only=None)
#----------- Graph title ------------------------
  plt.annotate(text=A_atom+proto_atom,xy=(0.0,1.1),xycoords='axes fraction',fontsize=7,fontweight='bold')

  plt.annotate(text=abc[i],xy =(-0.1,1.1) ,xycoords='axes fraction',fontsize=8,color='black')


#----------- New compound annotation ------------
  if i == 0:
    ax.annotate("ZrS", xy=(0.475, -1.39), xytext =(0.08,-1.45),xycoords='data',arrowprops=dict(arrowstyle="->",color='c'),color = 'c', fontsize = 12,fontweight='bold')
  
#-------------- Axis titles ------------------------
plt.annotate(text='formation energy [eV/Atom]',xy =(0.0,0.4) ,xycoords='figure fraction',fontsize=8,rotation=90 )
plt.annotate(text='$y$/($x$+$y$)',xy =(0.5,0.01) ,xycoords='figure fraction',fontsize=8)

#--------------  Changes white space --------------- 
plt.subplots_adjust(left=0.07, right=1.12, top=1.17, bottom=0.07, wspace=-0.1, hspace=-0.2)

os.chdir(cwd)
plt.savefig('fig_2.png',dpi=400)
plt.savefig('fig_2.pdf',format='pdf')






