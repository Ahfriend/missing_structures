def prototypes_distribution_in_columns(ax,input_file,proto_atom,A_atom):
  print ('proto in columns:')
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
  Y= 37 # number of structre types to include in the table
  with open(input_file,'r') as f:
    lines = f.readlines()

  for line in lines:
    end_index = -1
    if re.match('Points on the convex:',line):
      end_index =  lines.index(line)
      end_index = end_index - 2
  lines = lines[1:end_index]
  
  splited_lines = list(map(lambda x:x.split(),lines))
  proto_id_dleta_list = []
  for line in splited_lines:

    # check if prototype is already in the list proto_id_dleta_list
    proto_characters = [line[1],line[7],line[8]] #ratio, pearson, symmetry
    checker = list(filter(lambda x:x[0]==proto_characters,proto_id_dleta_list))       
    if checker != []:
       continue 

    # catch all the ids of the same proto
    lines_same_proto = list(filter(lambda x:proto_characters == [x[1],x[7],x[8]],splited_lines))
    ids_same_proto = list(map(lambda x:x[4],lines_same_proto))
    proto_id_dleta_list.append([proto_characters,ids_same_proto,float(line[-1])])
 
  # sort list of structure types by distance for the convex line.
  sorted_proto_id_dleta_list = sorted(proto_id_dleta_list, key=itemgetter(-1))
 
  yticks = list(map(lambda x:x[0][0]+' '+x[0][1]+' '+x[0][2],sorted_proto_id_dleta_list))


  # find the i index of the last point which is on the covex i.e delts =0.0
  #print ('---------sorted_proto_id_dleta_list -----------')
  #for i in sorted_proto_id_dleta_list:
  #  print (i)

  print ('-----end----sorted_proto_id_dleta_list -----------')
  on_the_convex = list(filter(lambda x:x[-1]>0.0,sorted_proto_id_dleta_list))[0]
  print (on_the_convex)
  index = sorted_proto_id_dleta_list.index(on_the_convex)  
  zero_index = index-1
  # find 0.03 eV/atom index
  on_the_convex = list(filter(lambda x:x[-1]>0.03,sorted_proto_id_dleta_list))[0]
  index = sorted_proto_id_dleta_list.index(on_the_convex)
  index_005 = index-1
  print ('index_005: ', index_005) 

  # find tha A atom columns affilation
  graph_data = []
  for i,entry in enumerate(sorted_proto_id_dleta_list):
    #print entry
    ids = entry[1]
    columns = []

    for id in ids:
      
      compound = id.split('_')[0]
      elements = re.findall('\d*(\D*)',compound)
      elements = elements[0:2]
      print(elements)
      A_element = list(filter(lambda x:x != proto_atom , elements))[0]     
      A_element_number = Atomes_number_symbol_conversion(A_element)
      column = col_atom_affilation(str(A_element_number)) 
      #if A_element == A_atom:  
      #columns.append(column)
      graph_data.append([column,i,A_element_number])
  

  graph_data_matrix = []
  for j in range(0,55):
    matrix_line = []
    for i in range(0,20):
      k=0

      A_column = col_atom_affilation(str(Atomes_number_symbol_conversion(A_atom)))
      print ('i: ',i, 'column: ',A_column)

      if i == int(A_column):
        print ('indside if')
        k = 3
      print ('k:',k)
      for z in range(0,120):
        try:
          a = graph_data.index([i,j,z])  # if the indices are not in the list error will arise. 
          #print ('graph_data:',graph_data)
          if z == Atomes_number_symbol_conversion(A_atom): # 
            k=2
            break
          else:
            k=1
            continue

        except ValueError:
          if k==1: 
            continue
          else:
            k=0
            continue
       
      matrix_line.append(k)
    for i,s in enumerate(matrix_line):
      if (i == int(A_column)or i==int(A_column)+1 or i==int(A_column)-1) and s !=1 and s!=2:
        matrix_line[i]=3
    print (matrix_line)
    graph_data_matrix.append(matrix_line)

  graph_data_matrix = np.array(graph_data_matrix)
  #print (graph_data_matrix)
  cmap = mpl.colors.ListedColormap(['w','#AA99FF','#4b0070','#FF9CC3'])
  barprops = dict(aspect='auto', cmap=cmap, interpolation='nearest')
  ax.imshow(graph_data_matrix,**barprops)
  
  # Horizontal lines
  for i in range(0,Y):
    if i == zero_index:
      plt.plot([0,19],[i+0.55,i+0.55],'-',color='orange',linewidth = 1.5,label = '0.00 eV') 
    elif i == index_005:
      plt.plot([0,19],[i+0.55,i+0.55],'-',color='c',linewidth = 1.5,label = '0.06 eV')
    else:
      plt.plot([0,19],[i+0.55,i+0.55],'-',color='gray',linewidth = 0.5)

  # Vertical line

  for i in range(0,19):
    plt.plot([i-0.5,i-0.5],[-0.5,Y+.5],'-',color='gray',linewidth = 0.5)

  # Neighborhood frame

  
  #elment_column = {'Ti':4,'Cu':11,'Ta':5}
  #column = elment_column[A_atom]
  #plt.plot([column+1.5,column+1.5],[-0.5,Y+.5],'-',color='FireBrick',linewidth = 1.)
  #plt.plot([column-1.5,column-1.5],[-0.5,Y+.5],'-',color='FireBrick',linewidth = 1.)

  #ax#.set_xticks(np.arange(1,19,1))
  ax.set_yticks(np.arange(0,Y+5,1))
# ... and label them with the respective list entries
  xticks = range(1,19,4)
  #for i,tick in enumerate(xticks):
  #  if tick%2 ==0:
  #    xticks[i] =''
  #print 'xticks: ',xticks 
  #ax.set_xticklabels(xticks,fontsize=6)
  ax.set_yticklabels(yticks,fontsize=6)

  #plt.box(colors = 'gray')
  plt.legend(loc=7)
  #lt.grid(which=('both'))
  #plt.ylabel('structure type')
  #plt.xlabel('periodic column number')
  plt.ylim(-0.5,Y+.5)
  plt.xlim(0.5,18.5)

  plt.title(A_atom+proto_atom)
  #plt.savefig('structure_in_columns.png')

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
