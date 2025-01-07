import sys
sys.path.append('/work/alonh/AUTO_FLOW')
from convex_hull_layers_function_15_1 import plot_convex 
#from make_n_f_neighbor_list import split_to_near_all_systems
#split_to_near_all_systems() # update the near and far list and list of islands for TiS,CuS, and TaSe
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import dropbox
from dropbox.files import WriteMode

convex_inputs_file = '/work/alonh/Missing_structures/Figs/V3/Fig_3_Near_Neighbors/convex_inputes.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()


cwd = os.getcwd()
abc = ['a','b','c','d','e','f','g','h']
fig = plt.figure(figsize=(6.4,10))

# y-axis title
fig.text(0.0,0.4,'formation energy [eV/Atom]',fontsize=8, rotation='vertical')       

# x-axis title
fig.text(0.45, 0.0,'$y$/($x$+$y$)',fontsize=8)

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

#  if i==2:
#    ax.annotate(text='formation energy [eV/Atom]',xy =(-0.3,-0.6) ,xycoords='axes fraction',fontsize=8,rotation=90 )
#  if i==6:
#    ax.annotate(text='$y$/($x$+$y$)',xy =(0.9,-0.25) ,xycoords='axes fraction',fontsize=8)

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

  ax.annotate(text=A_atom+proto_atom,xy=(0.75,0.05),xycoords='axes fraction',fontsize=7,fontweight='bold') 
  ax.annotate(text=abc[i],xy =(-0.05,0.85) ,xycoords='axes fraction',fontsize=8,fontweight='bold',ha='right', color='gray' ) # letters for each graph
 
  plt.xlim(-1.,0.1)
  #plt.ylim(,0.25)
  plt.xticks([])
  plt.yticks([])

  axins, axins_1 = plot_convex(ax,[input_file],proto_atom,A_atom,title=None,out_file=None,graph_num=3,ptable=True,convex_width=65,leg_pos=(1.4,1.6),near_neighbor=True,ylim = None)

  # Adding arrows new to new stable compounds.  
  #if i == 0: #TixSy
  #  axins.annotate("NbS$_{3}$", xy=(0.75,-1.14), xytext=(0.77,-1.75),xycoords='data',arrowprops=dict(arrowstyle="->",color='m'),color='m',fontsize=8)
  if i == 1:
    axins.annotate("Nb$_{3}$Se$_{4}$", xy=(0.571,-0.763), xytext=(0.0,-0.763),xycoords='data',arrowprops=dict(arrowstyle="->",color='m'),color='m',fontsize=10,fontweight='bold')
  if i == 5:
    axins.annotate(text = "TiSe", xy=(0.5,-1.45), xytext=(0.0,-1.1),xycoords='data',arrowprops=dict(arrowstyle="->",color='m'),color='m',fontsize=10,fontweight='bold')
    axins.annotate(text = "Nb$_{3}$Se$_{4}$", xy=(0.571,-1.52), xytext=(0.0,-1.6),xycoords='data',arrowprops=dict(arrowstyle="->",color='m'),color='m',fontsize=10,fontweight='bold')
    axins.annotate(text = "Sc$_{2}$Se$_{3}$", xy=(0.6,-1.53), xytext=(0.5,-.5),xycoords='data',arrowprops=dict(arrowstyle="->",color='m'),color='m',fontsize=10,fontweight='bold')

  if i == 6:
    axins.annotate(text = "ZnS", xy=(0.5,-0.249), xytext=(0.8, -.25),xycoords='data',arrowprops=dict(arrowstyle="->",color='m'),color='m',fontsize=10,fontweight='bold')
  if i == 7:
    axins.annotate(text = "AgSe", xy=(0.5,-0.124), xytext=(0.8, -.125),xycoords='data',arrowprops=dict(arrowstyle="->",color='m'),color='m',fontsize=10,fontweight='bold')

for i in ticks_len:
  print (i)

plt.subplots_adjust(left=0.08, bottom=0.04, right=1.03, top=1, wspace=None, hspace=None)

os.chdir(cwd)

# Save the figure to a file
local_file_path = 'fig_3.1.png'
fig.savefig(local_file_path)

plt.savefig(local_file_path,dpi=400)


