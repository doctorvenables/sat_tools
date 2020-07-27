import os
import yaml
#satyamlPath = '/usr/local/bin/python3/dist-packages/satellites/satyaml'
satyamlPath = '/home/doctorvenables/gr-satellites/python/satyaml/'
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
