import pandas as pd
import re
a =  ['Ti3S','Ti3S4','TiS2','Cu3S2'] 
a = pd.DataFrame(a,columns =['compounds'])
b = pd.DataFrame(map(lambda x: ''.join(re.findall('([A-Z]+[a-z]*)[0-9]*',x)) ,a['compounds']))
print (a)
print (b)
