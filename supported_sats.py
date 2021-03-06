import os
import yaml
#Use this Path if gr-satellites is installed to the default location with 'sudo make install'
satyamlPath = '/usr/local/lib/python3/dist-packages/satellites/satyaml/'

#Use this path if gr-satellites is not installed with 'sudo make install' but has been cloned
#You may need to edit this path...
#satyamlPath = '/home/doctorvenables/gr-satellites/python/satyaml/'
requiredData = ["norad","name","data"]
outputFile = os.path.expanduser("~")+'/supported_satellites.txt'
for filename in os.listdir(satyamlPath):
  with open(outputFile, "a+") as output:
    if filename.endswith('.yml'):
#      print(filename)
      file_path=satyamlPath+filename
      with open(file_path) as file:
        yaml_data = yaml.load(file, Loader=yaml.SafeLoader)
        str_to_print=''
        for key in requiredData:
          keyData = str(yaml_data[key])
#        print(key + " : " + keyData)
          str_to_print = str_to_print + keyData + ","
#      continue
      output.write(str_to_print+"\n")
      continue
    else:
      continue
