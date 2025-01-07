import sys
sys.path.append('/work/alonh/AUTO_FLOW')
sys.path.append('/work/alonh/Missing_structures/tables/new_stable_compounds_mp_aflow')
from convex_hull_layers_function_accumlate_3_1 import plot_convex 
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
fig = plt.figure(figsize=(6.4,4.096))

# X-axis title
fig.text(0.5, 0.02,'$y$/($x$+$y$)' , ha='center', va='center', fontsize=8)

# Y-axis title
fig.text(0.01, 0.5, 'formation energy [eV/Atom]', ha='center', va='center', rotation='vertical', fontsize=8) 

ticks_len = []
for i,line in enumerate(lines):
  #if i > 0: break
  if i == 1:
    legend_on = True
  else:
    legend_on = False  

  ax = plt.subplot(2,4,i+1)
  #ax.axis('off')
  #plt.box('off')
   # Set color for each spine
  ax.spines['left'].set_edgecolor('gray')
  ax.spines['bottom'].set_edgecolor('gray')
  ax.spines['right'].set_edgecolor('gray')
  ax.spines['top'].set_visible(False)

 
  splited_line = line.split()
  path = splited_line[0]
  input_file_1 = splited_line[1]
  input_file_2 = splited_line[2]
  input_file_3 = splited_line[3]
  input_file_4 = splited_line[4] # all files
  plt.xticks()
  #y_ticks = plt.yticks()
  #print ('y_ticks: ',y_ticks)

  try:
    input_file_5 = splited_line[5]  # aflow 
  except: 
    input_file_5 = None

  os.chdir(path)
  A_atom,proto_atom = input_file_1.split("_")[:2]

  plt.xticks([0,0.5,1],[0,0.5,1])
  mpl.rcParams['axes.linewidth'] = 1.0 #set the value globally

  ax.tick_params(axis=u'both', which=u'both',length=2,labelsize=6)

  ax.annotate(text=A_atom+proto_atom,xy=(0.66,0.05),xycoords='axes fraction',fontsize=7,fontweight='bold') 
  ax.annotate(text=abc[i],xy =(-0.1,0.96) ,xycoords='axes fraction',fontsize=8,fontweight='bold' ) # letters for each graph

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
   
  if i ==3:
    leg = plt.legend(loc='upper right',bbox_to_anchor=(1.3,1.),scatterpoints=1,fontsize=5,frameon='False')


  # Get the current y-ticks
  y_ticks = ax.get_yticks()

  print ('y_ticks: ',y_ticks)

  # Get the y-tick locations for indices 2 to 5
  if i ==1:
    selected_ticks = y_ticks[1:5]
  else:
    selected_ticks = y_ticks[1:6]

  # Set the y-axis ticks to the lowest values
  ax.set_yticks(selected_ticks)

  # Set the y-axis tick labels to the lowest values
  ax.set_yticklabels([str(round(value,2)) for value in selected_ticks])

# Control white space
plt.subplots_adjust( top=1,bottom=0.08,left=0.07,right=0.95, wspace=0.3,  hspace=None)
#save fig
os.chdir(cwd)
plt.savefig('fig_8_4x2.png',dpi=400)
plt.savefig('fig_8_4x2.pdf',dpi=400,format='pdf')

