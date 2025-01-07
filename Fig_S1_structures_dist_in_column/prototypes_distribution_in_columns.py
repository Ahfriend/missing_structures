def prototypes_distribution_in_columns(input_file,proto_atom,A_atom):
  import re
  import sys
  sys.path.append('/work/alonh/ICSD_STAT/functions')
  from Atomes_number_symbol_conversion import Atomes_number_symbol_conversion
  from col_atom_affilation import col_atom_affilation
  import matplotlib as mpl
  mpl.use('Agg')
  import matplotlib.pyplot as plt
  import numpy as np
  from operator import itemgetter

  with open(input_file,'r') as f:
    lines = f.readlines()

  for line in lines:
    end_index = -1
    if re.match('Points on the convex:',line):
      end_index =  lines.index(line)
      end_index = end_index - 2
  lines = lines[1:end_index]
  
  splited_lines = map(lambda x:x.split(),lines) 
  proto_id_dleta_list = []
  for line in splited_lines:

    # check if prototype is already in the list proto_id_dleta_list
    proto_characters = [line[1],line[7],line[8]] #ratio, pearson, symmetry
    checker = filter(lambda x:x[0]==proto_characters,proto_id_dleta_list)       
    if checker != []:
       continue 

    # catch all the ids of the same proto
    lines_same_proto = filter(lambda x:proto_characters == [x[1],x[7],x[8]],splited_lines)
    ids_same_proto = map(lambda x:x[4],lines_same_proto)
    proto_id_dleta_list.append([proto_characters,ids_same_proto,float(line[-1])])
 
  sorted_proto_id_dleta_list = sorted(proto_id_dleta_list, key=itemgetter(-1))

  graph_data = []
  for i,entry in enumerate(sorted_proto_id_dleta_list):
    print i, entry
    ids = entry[1]
    columns = []

    for id in ids:
      compound = id.split('_')[0]
      print compound
      elements = re.findall('\d*(\D*)',compound)
      elements = elements[0:2]
      
      A_element = filter(lambda x:x != proto_atom , elements)[0]
      A_element_number = Atomes_number_symbol_conversion(A_element)
      column = col_atom_affilation(str(A_element_number)) 
      columns.append(column)
      graph_data.append([column,i])
    print columns

# Preperation for a plot

  for i in graph_data:
    print i
  x=map(lambda t:t[0],graph_data)
  y=map(lambda t:t[1],graph_data)
  plt.scatter(x,y,s=10,marker=u's',linewidths=0)
  plt.plot([0,52],[4.5,4.5],'g--',linewidth=0.5,label = '0.0eV')	
  plt.plot([0,52],[51.5,51.5],'c--',linewidth=0.5,label ='0.1eV') # 0.1eV
  plt.plot([0,52],[87.5,87.5],'--',linewidth=0.5, c='orange',label = '0.2eV') # 0.2eV
  plt.plot([0,52],[114.5,114.5],'y--',linewidth=0.5,label = '0.3eV') # 0.3eV 
  
  plt.plot([4,4],[-2,145],'-',c='purple',linewidth=0.5) # element column indication
  plt.legend(loc=1)
  plt.ylabel('structure type')
  plt.xlabel('periodic column number')
  #plt.ylim(-1,25)
  #plt.xlim(1,19)
  plt.title(A_atom+proto_atom)
  plt.savefig('structure_in_columns.png',dpi =400)

if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser(prog = "plot disntace from convex vs ptabel column",description='')
  parser.add_argument('-i',required=True,help='convex plot output ',dest='inputfiles')
  parser.add_argument('-ap',required=True,help='proto atom' ,dest='proto')
  parser.add_argument('-a',required=True,help='The A atom as in AxOy ',dest='Aatom')
  args= parser.parse_args()

  input_file = args.inputfiles
  proto_atom = args.proto
  A_atom = args.Aatom

  prototypes_distribution_in_columns(input_file,proto_atom,A_atom)
