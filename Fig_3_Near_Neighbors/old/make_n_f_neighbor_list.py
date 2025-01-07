def make_n_f_neighbor_list(A_atom,P_atom,A_S_job_list,out=None):
  '''
  The function splits the AS or ASe strucutre types to two list near and far
  '''
  import sys 
  sys.path.append('/work/alonh/ICSD_STAT/functions')
  from col_atom_affilation import col_atom_affilation
  from Atomes_number_symbol_conversion import Atomes_number_symbol_conversion
  import re
  with open(A_S_job_list) as f:
    lines = f.readlines()

  # find P_atom column number
  print (P_atom)
  print (Atomes_number_symbol_conversion((P_atom)))

  # find the P_atom's column number
  P_column = col_atom_affilation(str(Atomes_number_symbol_conversion(P_atom))) 

  # find the A_atom column number
  A_column = col_atom_affilation(str(Atomes_number_symbol_conversion(A_atom)))

  # Iterate over the A_S/Se jobs and decied if they are near or far neighbor
  nn = open(out+A_atom+'_'+P_atom+'_st_Ann_'+P_atom+'.txt','w')
  fn = open(out+A_atom+'_'+P_atom+'_st_Afn_'+P_atom+'.txt','w')
  for line in lines:
    print (line)
    iscd_id = line.split('/')[-2]
    compound = iscd_id.split('_')[0]
    print (compound)
    elements = re.findall('([A-Za-z]+)',compound)
    print (elements)
    for el in elements:
      if el == P_atom: continue
      
      column = col_atom_affilation(str(Atomes_number_symbol_conversion(el)))
      if abs(A_column - column)==0 or  abs(A_column - column)==1:
        nn.write(line)
      else:
        fn.write(line)
  nn.close()
  fn.close()
  return

def single_element_list(A_atom,P_atom, A_S_job_list,A_atom_st,out_path):
  '''
  Cuts from the AS structures list structure of desired element. 
  '''
  import re
  # open the AS list
  with open(A_S_job_list) as f:
    lines = f.readlines()
  
  # open file for creating new list
  new_list = out_path+'/'+A_atom+'_'+P_atom+'_st_'+A_atom_st+'_'+P_atom+'.txt'
  with open(new_list,'w') as f:        
    for line in lines:
      print (line)
      iscd_id = line.split('/')[-2]
      compound = iscd_id.split('_')[0]
      print (compound)
      elements = re.findall('([A-Za-z]+)',compound)
      print (elements)
      for el in elements:
        if el == A_atom_st:
          f.write(line)

  return 

def split_to_near_all_systems():
 
  A_S_job_list = '/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S/Ti_S/Ti_S_st_A_S.txt'
  A_atom = 'Ti'
  P_atom = 'S'
  out_path = '/work/alonh/AUTO_FLOW/Projects/Binary/missing_proto_S/Ti_S/'
  make_n_f_neighbor_list(A_atom,P_atom,A_S_job_list,out_path)    
  for A_atom_st in ['Cu','As']:
    single_element_list(A_atom,P_atom, A_S_job_list,A_atom_st,out_path)

  A_S_job_list = '/andata2/alonh/missing_structures/Cu_S/Cu_S_st_A_S.txt'
  A_atom = 'Cu'
  P_atom = 'S'
  out_path = '/andata2/alonh/missing_structures/Cu_S/'
  make_n_f_neighbor_list(A_atom,P_atom,A_S_job_list,out_path)
  for A_atom_st in ['Ti','P']:
    single_element_list(A_atom,P_atom, A_S_job_list,A_atom_st,out_path)


  A_S_job_list = '/andata2/alonh/missing_structures/Ta_Se/Ta_Se_st_A_Se.txt'
  A_atom = 'Ta'
  P_atom = 'Se'
  out_path = '/andata2/alonh/missing_structures/Ta_Se/'
  make_n_f_neighbor_list(A_atom,P_atom,A_S_job_list,out_path) 
  for A_atom_st in ['Cu','As']:
    single_element_list(A_atom,P_atom, A_S_job_list,A_atom_st,out_path)


  return


if __name__ == "__main__":
  A_S_job_list = 'Ti_S_st_A_S.txt'
  A_atom = 'Ti'
  P_atom = 'S'
  #make_n_f_neighbor_list(A_atom,P_atom,A_S_job_list)
  split_to_near_all_systems()

