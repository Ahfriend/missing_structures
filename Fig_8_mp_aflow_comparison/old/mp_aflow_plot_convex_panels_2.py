import sys
sys.path.append('/work/alonh/AUTO_FLOW')

from convex_hull_layers_function_accumlate_1 import plot_convex 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
convex_inputs_file = 'mp_aflow_compare_four_files.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['a','b','c','d','e','f','g','h']
fig = plt.figure(figsize=(6.4,10.0))
ticks_len = []
for i,line in enumerate(lines):
  print (line)
  if i > 0: break
  ax = plt.subplot(4,2,i+1)
  #ax.axis('off')
  plt.box('off')
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

  #plt.yticks()
  
  for j,tick in enumerate(ax.yaxis.get_major_ticks()):
    if j ==1 or j==2 or j==3:
      tick.label1On = True
    else:
      tick.label1On = False

  plt.xticks([0,0.5,1],[0,0.5,1])
  mpl.rcParams['axes.linewidth'] = 0.0 #set the value globally

  #ax.set_xticks([0,0.5,1])
  #ax.set_xticklabels([0,0.5,1])
  ax.tick_params(axis=u'both', which=u'both',length=0)
 
  ax.annotate(s=A_atom+' '+proto_atom,xy=(0.66,0.05),xycoords='axes fraction',fontsize=16,fontweight='bold') 
  ax.annotate(s=abc[i],xy =(-0.1,0.9) ,xycoords='axes fraction',fontsize=16,fontweight='bold' ) # letters for each graph


  plt.xlim(-0.1,1.6)
  #plt.ylim(,0.25)

  ax = plot_convex(ax,[input_file_1],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,dash_convex = False,no_dots=True,convex_color='b',convex_label = 'ICSD',convex_line_width=3.0)
  #ax = plot_convex(ax,[input_file_2],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,dash_convex = False,no_dots=True,convex_color='c',convex_label = 'our',convex_line_width=2.0)
  #ax = plot_convex(ax,[input_file_3],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,dash_convex = False,no_dots=True,convex_color='g',convex_label='mp',convex_line_width=1.0)
  ##ax = plot_convex(ax,[input_file_4],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,dash_convex = False,no_dots=True,convex_color='m',convex_label='all',convex_line_width=1.0)
  #try:
    #ax = plot_convex(ax,[input_file_5],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,dash_convex = False,no_dots=True,convex_label='aflow',convex_line_width=0.5)
  #except:
   # pass
  ##all
  #ax = plot_convex(ax,[input_file_4],proto_atom,A_atom,proto_graph=True,ptable=False,on_convex_only=True,dash_convex = False,no_dots=True,convex_color='m',convex_label=None,convex_line_width=0.0)
 
  

os.chdir(cwd)
plt.savefig('test.png',dpi=200)
