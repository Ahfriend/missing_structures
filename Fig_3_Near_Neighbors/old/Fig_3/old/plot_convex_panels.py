import sys
sys.path.append('/work/alonh/AUTO_FLOW')

from convex_hull_layers_function_10 import plot_convex 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
convex_inputs_file = '/work/alonh/Missing_structures/convex_inputes.txt'
with open(convex_inputs_file ,'r') as f:
  lines = f.readlines()

cwd = os.getcwd()
abc = ['a','b','c','d','e','f']
fig = plt.figure(figsize=(6.4,8))
ticks_len = []
for i,line in enumerate(lines):
  print line
  #if i > 0: break
  ax = plt.subplot(3,2,i+1)
  #ax.axis('off')
  plt.box('off')
  splited_line = line.split()
  path = splited_line[0]
  input_file = splited_line[1]
  os.chdir(path)
  A_atom,proto_atom = input_file.split("_")[:2]

  #plt.yticks()
  
  for j,tick in enumerate(ax.yaxis.get_major_ticks()):
    if j ==1 or j==2 or j==3:
      tick.label1On = True
    else:
      tick.label1On = False



  ax.set_xticks([0,0.5,1])
  ax.set_xticklabels([0,0.5,1])
  ax.tick_params(axis=u'both', which=u'both',length=0)
 
  ax.annotate(s=A_atom+' '+proto_atom,xy=(0.66,0.05),xycoords='axes fraction',fontsize=16,fontweight='bold') 
  ax.annotate(s=abc[i],xy =(-0.1,0.85) ,xycoords='axes fraction',fontsize=16,fontweight='bold',ha='right' ) # letters for each graph


  plt.xlim(-0.1,1.6)
  #plt.ylim(,0.25)

  plot_convex(ax,[input_file],proto_atom,A_atom,title=None,out_file=None,graph_num=2,ptable=True)

print 'ticks_len:'
for i in ticks_len:
  print i

os.chdir(cwd)
plt.savefig('fig_3.png',dpi=1000)
