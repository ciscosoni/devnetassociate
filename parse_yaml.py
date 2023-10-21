import yaml
from yaml import load, load_all

data = open('/Users/surajsoni/Desktop/DevNet Associate/Codes/sample.yml', 'r')

doc = load(data, Loader=yaml.FullLoader)

print(doc)