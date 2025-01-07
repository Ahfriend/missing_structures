
def plot_convex(ax,input_file,proto_atom,A_atom,title=None,out_file=None,graph_num=None,proto_graph=None,ptable=None,on_convex_only=None):
  '''
  v11_1 adding arrows to stable compounds

  '''

  import sys
  sys.path.append('/work/alonh/Spin_Conf')
  sys.path.append('/work/alonh/AUTO_FLOW/Functions')
  sys.path.append('/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S/scripts')
  sys.path.append('/work/alonh/Periodic_table/Periodic_table_templat/')
  from periodic_table_function_for_convex import plot_table
  import numpy as np
  from getEtot import getEtot

  import auto_flow_functions as aff
  import matplotlib as mpl
  mpl.use('Agg')
  from mpl_toolkits.axes_grid1.inset_locator import inset_axes
  from periodic_table_function_for_convex import plot_table

  import matplotlib.pyplot as plt
  from scipy.spatial import ConvexHull
  from operator import itemgetter
  import argparse
  from operator import itemgetter
  import re
  #from AFLUX_test import are_protos_in_aflow
  import logging
  import os


  with open(input_file[0],'r') as f:
    lines = f.readlines()

  inputFiles = []
  group_names = []
  atoms_couples = []
  graphNs = []
  name_color_dict = {}
  colorKey = {}
  indexKey = {}
  faceKey = {}
  for line in lines:
    print ('line',line)
    if re.match('#',line)!= None: continue
    splited_line = line.split()
    print('splited_line:',splited_line)
    file = splited_line[0]
    name = splited_line[1] 
    atoms = name.split('_')
    atom = atoms[0]
    sec_atom = atoms[-1] 
    graphN = splited_line[2]
    color = splited_line[3] 
    marker = splited_line[4]    
    face = splited_line[5]
    # make group name - color dictioanry
    name_color_dict.update({name:color})
  
    # make atom - color dictionary     
    if proto_graph==None:
      if atom == proto_atom:
         colorKey.update({atom:'gainsboro'})
      elif atom == A_atom:
         colorKey.update({atom:'orange'})
      else:
         colorKey.update({atom:color})

    elif proto_graph==True:
      if sec_atom == A_atom:
         colorKey.update({atom:'gainsboro'})
      elif sec_atom == proto_atom:
         colorKey.update({sec_atom:'orange'})
      else:
         colorKey.update({sec_atom:color})
   
    # make group name - index dictioanry
    indexKey.update({name:marker})
    faceKey.update({name:face}) 
    inputFiles.append(file)
    group_names.append(name)
    graphNs.append(int(graphN))

    group_names_dict = dict(map(lambda x:(group_names.index(x),x),group_names))
   
    atoms_couples.append(name.split("_"))

  if title == None:
    titel = A_atom+' '+proto_atom+' convex hull'

  system = str(A_atom+'x'+proto_atom+'y')


#colors for the legend
  #colors = ['r','g','b','m','c','orange','y','purple','b','m','c','k','y','r']
  #markers = ['o','^','>','x','*','x','x','x','^','>','<','*','8','x']

  def make_ratio_energy_list(inputFile,proto_atom):
# read the input file:
    with open(inputFile) as f:
      lines = f.readlines()

    energy_list = []
    ratio_list = []
    ratio_energy_list = []
    runs_with_error = []

# go over VASP runs and extract total energy and stoichiometry.
    for line in lines:
      if re.match("#",line):
        continue
      z = line.split()
      job_path = z[0]   
    # extract energy  
      try:
        Etot = getEtot(job_path)[0]
      except:
        runs_with_error.append(z[0])
        continue
    #read poscar
      title,scaler,a,atomsCount,Direct,R,atomTypes = aff.readPoscar(job_path+'/POSCAR')
      atomsList=[]
    # read atoms from poscar
      for i in R:
        atomsList.append(i[3])
    # assigning y to proto atom and x to A atom
      if len(atomsCount) == 2:
        for atom in atomTypes:
          if atom == proto_atom:
            y = atomsList.count(atom)  # proto atom
          else:
            x = atomsList.count(atom) # A atom
      elif len(atomsCount) == 1:
        if atomTypes[0] == proto_atom:
          x = 0
          y = 1
        else:
          y = 0
          x = 1 

      Etot_norm = Etot/sum(atomsCount) 


      ratio = (float(y)/(float(x)+float(y)))
      ratio_energy_list.append([ratio,Etot_norm,job_path])
    return ratio_energy_list



# read all the data lists and conect them to one list.

  all_points = []
  for i,file in enumerate(inputFiles):

     ratio_energy_list = make_ratio_energy_list(file,proto_atom)
     
   # adding the group number
     ratio_energy_list = list(map(lambda x:[float(x[0]),float(x[1]),x[2],i],ratio_energy_list))

   # accumulating all data to a one list:
     all_points = all_points + ratio_energy_list


# check if appears in aflow and create a dictioanry.
  icsd_ids = []
  for i in all_points:

    path = i[2]
    icsd_id =  re.findall('/(([A-Z]+[a-z]*\d+)+?_ICSD_\d+)',path)
    print ('icsd_id: ',icsd_id)
    if icsd_id !=[]:
        id = icsd_id[0][0]
        i.append(id)
 
    elif icsd_id ==[]:
        icsd_id = [('Not_ICSD_origin','')]
        i.append('Not_ICSD_origin')
    
    icsd_ids.append(icsd_id[0][0])
  # the flow check didn't work so I removed it 28.5.24  
  #in_aflow = np.array(are_protos_in_aflow([proto_atom,A_atom],icsd_ids))
  #in_aflow_dict = dict(list(map(lambda x:[x[0],x[3]],in_aflow)))
  for i in all_points:
    #if i[4] != None:
    #  try:
    #    in_aflow =  in_aflow_dict[i[4]]
    #    i.append(in_aflow)
    #  except:
    #    i.append(None)
    #    continue
    #elif i[4] == None:
      i.append(None) 

# assigning to each point object its A_atom and proto_atom:
  for i in all_points:
    print (i)
    id = i[4]  
    if id != 'not_ICSD_origin':
       formula = id.split('_')[0]
     #print formula
       atoms = re.findall('(\D+)',formula)
       if len(atoms) == 1:
         i.append('')
         i.append('')
       elif atoms[0] == proto_atom:
         i.append(atoms[1])
         i.append(atoms[0])
       elif atoms[1] == proto_atom:
         i.append(atoms[0])
         i.append(atoms[1])
       elif atoms[0]== A_atom: 
         i.append(atoms[0])
         i.append(atoms[1])
       elif atoms[1]== A_atom:
         i.append(atoms[1])
         i.append(atoms[0])  
       elif atoms[0]!= A_atom and atoms[0]!= proto_atom and atoms[1]!= A_atom and atoms[1]!= proto_atom:
         if atoms[0] == 'S' or atoms[0] == 'Se':
           i.append(atoms[1])
           i.append(atoms[0])
         elif atoms[1] == 'S' or atoms[1] == 'Se':
           i.append(atoms[0])
           i.append(atoms[1])
     # can add situation where none of the prototype atoms

# find min energy for A and B i.e. ratio = 0 and 1
  all_A = list(filter(lambda x:x[0]==0.0,all_points))
  print ('all_A: ', all_A) 
  min_A = sorted(all_A, key=itemgetter(1))[0]
  all_B = list(filter(lambda x:x[0]==1.0,all_points))
  print ('all_B: ', all_B)
  min_B = sorted(all_B, key=itemgetter(1))[0]

# shift all point 
  def line_equation(x1,x2,y1,y2):
    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1
    return a,b

  x1 = min_A[0]
  x2 = min_B[0]
  y1 = min_A[1]
  y2 = min_B[1]
  a,b = line_equation(x1,x2,y1,y2)


  new_all_points = list(map(lambda x:[x[0],x[1]-(a*x[0]+b),x[2],x[3],x[4],x[5],x[6],x[7]],all_points))
  points_for_hull = list(map(lambda x:[x[0],x[1]],new_all_points)) # points in foramte to calculate convex hull.

# calcualte convex Hull
  hull = ConvexHull(points_for_hull)
  points = hull.points

# indices of the points on the convex. these include closed convex and counter clock wise
  vertices = list(hull.vertices)
# find left and right vertices
  left = list(filter(lambda x: new_all_points[x][0]==0.0 and round(new_all_points[x][1],10)==0.0, vertices))[0]
  right =list(filter(lambda x: new_all_points[x][0]==1.0 and round(new_all_points[x][1],10)==0.0, vertices))[0]
  print('----- Here ------')
  print (left)
  left_index = vertices.index(left)
  right_index = vertices.index(right)


  if right_index > left_index:
    vertices = vertices[left_index:right_index+1]
  elif  left_index > right_index: 
    vertices = vertices[left_index:]+vertices[0:right_index+1]

#find  points above the hull and smaller than delta
  with_delta_above_hull =[]

  for point in new_all_points:
    ratio = point[0]
    energy = point[1]

    for i in range(len(vertices)-1):
      vertex = vertices[i]
      next_vertex = vertices[i+1]

      ver_ratio = new_all_points[vertex][0]
      next_ver_ratio = new_all_points[next_vertex][0]

      ver_energy = new_all_points[vertex][1]
      next_ver_energy = new_all_points[next_vertex][1]
      if i == 0:
        if ratio >= ver_ratio and ratio <= next_ver_ratio:
          #print ver_ratio,next_ver_ratio,ver_energy,next_ver_energy
          a1,b1 = line_equation(ver_ratio,next_ver_ratio,ver_energy,next_ver_energy)
          delta = (energy - (a1*ratio+b1))
          new_point = point+[delta]
          with_delta_above_hull.append(tuple(new_point))
    
      else:
        if ratio > ver_ratio and ratio <= next_ver_ratio:# and ratio <= 1.0:
          a1,b1 = line_equation(ver_ratio,next_ver_ratio,ver_energy,next_ver_energy)
          delta = (energy - (a1*ratio+b1))
          new_point = point+[delta]
          with_delta_above_hull.append(tuple(new_point))




#with_delta_above_hull=list(filter(lambda(x:x[7]>0.1,new_all_points)))
  with_delta_above_hull = list(set(with_delta_above_hull))
  with_delta_above_hull.sort() 
  with_delta_above_hull = np.array(with_delta_above_hull)

# plot convex line and pralel line with chosen energy delta from the convex.
  #for i in range(len(vertices)-1):
  
  #  s = np.array([vertices[i],vertices[i+1]])# The indecies of two points on the convex
  #  plt.plot(points[s ,0], points[s ,1], 'k-') # plot((x0,y0),(x1,y1))
  #  plt.plot(points[s ,0], points[s ,1]+[0.1,0.1], 'k--') # plot((x0,y0),(x1,y1))

  A_atoms = list(map(lambda x:x[6],new_all_points))
  A_atoms =list(set(A_atoms))


#########  Plot graphs:  #########
  if graph_num == None:  
    start = 0
    end = 4 
  else:
    start = graph_num
    end = graph_num+1

  # plot the convex in a sub axes
  axins = inset_axes(ax,
                width="75%", # width = 30% of parent_bbox
                height="60%", # height : 1 inch
                loc=3) # location lower left
  #plt.xlim(0,1)
  axins.spines['right'].set_color('gray')
  axins.spines['left'].set_color('gray')
  axins.spines['bottom'].set_color('gray')
  axins.spines['top'].set_visible(False)
  
  axins.tick_params(axis='x', color='gray')
  axins.tick_params(axis='y', color='gray')
 
  # Remove the axes
  ax.set_axisbelow(False) 


  # plot the 'global' convex and it plus 0.1eV
  for i in range(len(vertices)-1):
    s = np.array([vertices[i],vertices[i+1]])# The indecies of two points on the convex
    plt.plot(points[s ,0], points[s ,1], '-',color='gray',linewidth=0.75) # plot((x0,y0),(x1,y1))
    plt.plot(points[s ,0], points[s ,1]+[0.03,0.03], '--',color='gray',linewidth =0.75) # plot((x0,y0),(x1,y1))
 
  # adjast the y limits:
  ymin = min(points[:,1])
  plt.ylim(ymin-0.05*(abs(ymin)+0.15),0.15)

 
  if on_convex_only != True:  
      convex_points = new_all_points
  elif on_convex_only == True:  
      convex_points =np.array( map(lambda vertex: new_all_points[vertex],vertices))

  #for N in range(start,end):
  legend_names = []
  for j,group_name in enumerate(group_names): # runs on the diffrent gourp elements groups
    splited_name = group_name.split('_')
    if len(splited_name) ==2:
     #legened_name = splited_name[0]+"$_x$"+splited_name[1]+"$_y$"    
     legened_name = splited_name[0]+splited_name[1]

    else:
     legened_name = splited_name[0]
    legend_names.append(legened_name)
   
    if j<2: continue
    elif j ==2:
      group = filter(lambda x:int(x[3])==0 or int(x[3])==1 or  int(x[3])==2 ,convex_points)
    else:
      group = filter(lambda x:int(x[3])==j ,convex_points)
   
    if group == []: continue
    group = list(map(lambda x:[x[0],x[1]],group))
    group = np.array(group,dtype='f')

    if graph_num != None:
      if graphNs[j]==graph_num or graphNs[j]==0:          
          print('color: ',group_name,name_color_dict[group_name])
          for l,k in zip(faceKey,name_color_dict,):
            print(l,faceKey[l],name_color_dict[k])
          z='none'
          print (group_name,faceKey[group_name],'color: ', name_color_dict[group_name])
          plt.scatter(group[:,0],group[:,1],s=25,color=name_color_dict[group_name],fc=faceKey[group_name],marker=indexKey[group_name],label = legend_names[j])
    
    elif graph_num == None:
          plt.scatter(group[:,0],group[:,1],s=25,color=name_color_dict[group_name],fc=faceKey[group_name],marker=indexKey[group_name],label = legend_names[j])
    

  plt.legend(ncol=3,loc='upper left', borderpad=0.1, handlelength=0.5,bbox_to_anchor=(0, 1.1),scatterpoints=1,fontsize=7,labelcolor='gray',frameon = False)  # first size was 1.4, 1.6


  if title != None:
       plt.title(titel)

  # Ticks font size
  plt.xticks(fontsize=6,)
  plt.yticks(fontsize=6,)

  # Change the color of the tick lines
  ax.tick_params(axis='x', color='gray')
  ax.tick_params(axis='y', color='gray')

  # plot periodic table legend
  if ptable == True:
    axins_1 = inset_axes(ax,
                width="55%", # width = 30% of parent_bbox
                height="30%", # height : 1 inch
                loc=2)

    plot_table(axins_1,colorKey)

  new_to_aflow = np.array(list(filter(lambda x:x[5]== 'False' ,new_all_points)))


# read ICSD data file
  ICSD_file = '/andata/alonh/ICSD_STAT/2015_Data/uniary_and_binary_icsd.txt'
  with open(ICSD_file,'r') as f:
    lines = f.readlines()

# create dictiona IDs:[pearson,#symmetry]
  ICSD_splited = list(map(lambda x:x.split(),lines))
  ICSD_dict = dict(list(map(lambda x:[x[6],[x[2],x[5]]],ICSD_splited)))
  

# output file:

   #  delete

     
  if ptable == True:	
  	return axins, axins_1
  else:
        return axins


if __name__ == "__main__":
  import matplotlib as mpl
  mpl.use('Agg')
  import matplotlib.pyplot as plt


  import argparse
  parser = argparse.ArgumentParser(prog = "check convergance",description='check if VASP jobs have converged')
  parser.add_argument('-i',required=True,help='Text file contains job paths ',action='append',dest='inputfiles')

#parser.add_argument('-i2',help='Text file contains ',default =None,dest='inputfile_2'
  parser.add_argument('-ap',required=True,help='proto atom will presnted on right side of the figure ',dest='proto')
  parser.add_argument('-a',required=True,help='The A atom in AxOy ',dest='Aatom')
  parser.add_argument('-t','--titel',help='enter graph titel ',dest='titel',default=None)
  parser.add_argument('-f','--file_name',help='graph file name ',dest='file',default=None)
  parser.add_argument('-n',help='graph number ',dest='graph_num',default=None,type=int)
  parser.add_argument('-pt',help='plot small ptable: yes or no ',dest='ptable',default=True,type=bool)



  args= parser.parse_args()
  input_file = args.inputfiles
  proto_atom = args.proto
  A_atom = args.Aatom
  titel = args.titel
  n = args.graph_num  

  #ax = plt.figure()
  ax = plt.subplot()
  plot_convex(ax,input_file,proto_atom,A_atom,graph_num=n,title=None,out_file=None)
    
  plt.savefig('test.png',dpi=1000)



