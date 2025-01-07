import sys
sys.path.append('/work/alonh/AUTO_FLOW')
from convex_hull_layers_function_15 import plot_convex 
from make_n_f_neighbor_list import split_to_near_all_systems
split_to_near_all_systems() # update the near and far list and list of islands for TiS,CuS, and TaSe
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
convex_inputs_file = '/work/alonh/Missing_structures/Figs/V3/Fig_3_Near_Neighbors/convex_inputes.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['a','b','c','d','e','f','g','h']
fig = plt.figure(figsize=(6.4,10))
ticks_len = []
for i,line in enumerate(lines):
  #if i!= 6: continue
  ax = plt.subplot(4,2,i+1)
  ax.axis('off')
  plt.box('off')
  splited_line = line.split()
  path = splited_line[0]
  input_file = splited_line[1]
  os.chdir(path)
  A_atom,proto_atom = input_file.split("_")[:2]

  if i==2:
    ax.annotate(s='total energy [eV/Atom]',xy =(-0.23,0.-1.) ,xycoords='axes fraction',fontsize=12,rotation=90 )
  if i==6:
    ax.annotate(s='ratio $y$/($x$+$y$)',xy =(0.7,-0.25) ,xycoords='axes fraction',fontsize=12)

  # ylim
  if i ==0: ylim =(-2,0.2)
  elif i ==1: ylim = (-1,0.2)
  elif i ==2: ylim = (-0.35,0.2)
  elif i ==3: ylim = (-0.18,0.2)
  elif i ==4: ylim = (-1.5,0.2)
  elif i ==5: ylim = (-1.75,0.2)
  elif i ==6: ylim = (-0.3,0.2)
  elif i ==7: ylim = (-0.18,0.2)
  else: ylim ==None   

  ax.annotate(s=A_atom+proto_atom,xy=(0.75,0.05),xycoords='axes fraction',fontsize=16,fontweight='bold') 
  ax.annotate(s=abc[i],xy =(-0.05,0.85) ,xycoords='axes fraction',fontsize=16,fontweight='bold',ha='right' ) # letters for each graph
 
  plt.xlim(-1.,0.1)
  #plt.ylim(,0.25)
  plt.xticks([])
  plt.yticks([])

  plot_convex(ax,[input_file],proto_atom,A_atom,title=None,out_file=None,graph_num=3,ptable=True,convex_width=65,leg_pos=(1.4,1.6),near_neighbor=True,ylim = None)

plt.subplots_adjust(left=None, bottom=None, right=0.95, top=0.95, wspace=None, hspace=None)
for i in ticks_len:
  print (i)

os.chdir(cwd)
plt.savefig('fig_3_dpi_400.png',dpi=400)
plt.savefig('fig_3.eps',format ='eps')
