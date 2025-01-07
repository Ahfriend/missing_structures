import sys
import os
sys.path.append('/work/alonh/AUTO_FLOW/Functions')
from check_job_termination_and_create_txt_files_1 import status
import re
input = 'all_compound_proto_dir_files.txt'


with open(input,'r') as f:
 lines = f.readlines()

convex_out = open('on_the_convex_all.txt','w')
above_convex = open('above_the_convex_all.txt','w')
for line in lines:
  path,tag = line.split()
  print ('=========='+tag+'=========')
  convex_out.write('=========='+tag+'=========\n')
  above_convex.write('=========='+tag+'=========\n')
  with open(path+'/convex_data.txt') as f:
    data_lines = f.readlines()
   
  flag_convex = None
  flag_above = None
  
  for data_line in data_lines:
     if re.match('Points on the convex:',data_line):
        flag_convex = True
        continue 
     elif re.match('Points with delta of 0.1 eV from the Hull:',data_line):
        flag_above = True
        flag_convex = None
        continue

     if flag_convex == True:
        print (data_line)
        convex_out.write(data_line)
     elif flag_above == True:
        print (data_line)
        above_convex.write(data_line)


