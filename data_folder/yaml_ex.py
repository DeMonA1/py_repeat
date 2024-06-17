import yaml


with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.safe_load(text)
data['details']
len(data['poems'])
data['poems'][1]['title']