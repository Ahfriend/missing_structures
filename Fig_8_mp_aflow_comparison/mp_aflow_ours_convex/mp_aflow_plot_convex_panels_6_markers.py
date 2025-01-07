import sys
sys.path.append('/work/alonh/AUTO_FLOW')
sys.path.append('/work/alonh/Missing_structures/tables/new_stable_compounds_mp_aflow')
from convex_hull_layers_function_accumlate_3 import plot_convex 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
convex_inputs_file = 'mp_aflow_compare_four_files.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['a','b','c','d','e','f','g','h']
fig = plt.figure(figsize=(6.4,10.0))
ticks_len = []
for i,line in enumerate(lines):
  #if i!=4: continue
  if i == 1:
    legend_on = True
  else:
    legend_on = False  

  ax = plt.subplot(4,2,i+1)
  #ax.axis('off')
  plt.box('off')
 
  ax.annotate(text='total energy [eV/Atom]',xy =(0.0,0.4) ,xycoords='figure fraction',fontsize=12,rotation=90 )
  ax.annotate(text='ratio $y$/($x$+$y$)',xy =(0.425,0.03) ,xycoords='figure fraction',fontsize=12)


  splited_line = line.split()
  path = splited_line[0]
  input_file_1 = splited_line[1]
  input_file_2 = splited_line[2]
  input_file_3 = splited_line[3]
  input_file_4 = splited_line[4] # all files
  plt.xticks()
  plt.yticks()

  try:
    input_file_5 = splited_line[5]  # aflow 
  except: 
    input_file_5 = None

  os.chdir(path)
  A_atom,proto_atom = input_file_1.split("_")[:2]

  #ax.patches.Patch(edgecolor=None, facecolor=None, color='white', linewidth=0.0, linestyle=None, antialiased=None, hatch=None, fill=True, capstyle=None, joinstyle=None)
  #matplotlib.axes.Axes.set_frame_on
  ax.set_frame_on(False)

  for j,tick in enumerate(ax.yaxis.get_major_ticks()):
    if j ==1 or j==2 or j==3:
      tick.label1On = True
      if i == 3 and j == 3:
         tick.label1On = False 
    else:
      tick.label1On = False
  

  plt.xticks([0,0.5,1],[0,0.5,1])
  mpl.rcParams['axes.linewidth'] = 0.0 #set the value globally

  #ax.set_xticks([0,0.5,1])
  #ax.set_xticklabels([0,0.5,1])
  ax.tick_params(axis=u'both', which=u'both',length=0)
 
  ax.annotate(text=A_atom+proto_atom,xy=(0.66,0.05),xycoords='axes fraction',fontsize=16,fontweight='bold') 
  ax.annotate(text=abc[i],xy =(-0.1,0.9) ,xycoords='axes fraction',fontsize=16,fontweight='bold' ) # letters for each graph


  plt.xlim(-0.1,1.6)


  ax = plot_convex(ax,[input_file_1],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,linestyle='--',no_dots=True,convex_color='g',convex_label = 'ICSD',convex_line_width=3.5,legend = legend_on  )
  ax = plot_convex(ax,[input_file_2],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,linestyle='-',no_dots=True,convex_color='c',convex_label = 'current study',convex_line_width=2.0,legend = legend_on)
  ax = plot_convex(ax,[input_file_3],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,linestyle='--',no_dots=True,convex_color='orange',convex_label='mp',convex_line_width=2.0,legend = legend_on)

  try:
    ax = plot_convex(ax,[input_file_5],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,linestyle='--',no_dots=True,convex_color='m',convex_label='aflow',convex_line_width=1.0,legend = legend_on)
  except:
    pass
  #all
  ax = plot_convex(ax,[input_file_4],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,linestyle='',no_dots=True,convex_color='m',convex_label=None,convex_line_width=0.0,new_sto=True)
   
  if i ==1:
    leg = plt.legend(loc='upper right',bbox_to_anchor=(1.25,1.),scatterpoints=1,fontsize=8,frameon='False')


os.chdir(cwd)
plt.savefig('fig_9.png',dpi=400)
plt.savefig('fig_9.eps',format='eps')

