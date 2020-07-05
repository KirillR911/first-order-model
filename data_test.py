from frames_dataset import FramesDataset
import yaml
from matplotlib import pyplot as plt
with open("config/tth-data.yaml") as f:
    config = yaml.load(f)
d  = FramesDataset(is_train= True,**config['dataset_params'])
t = d[0]
plt.imshow(t['source'].reshape((256,256,3)))
plt.show()
plt.imshow(t['target'].reshape((256,256,3)))
plt.show()
plt.imshow(t['driving'].reshape((256,256,3)))
plt.show()