from PIL import Image
import os


li = os.listdir("data/vox/id2/orig")
for i in li: 
    im = Image.open(os.path.join("data/vox/id2/orig", i))
    im =im.resize((256,256))
    print(im.size)
    im.save(os.path.join("data/vox/id2/orig", i))