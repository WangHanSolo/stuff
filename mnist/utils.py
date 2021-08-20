import numpy as np
import gzip

def load_imgs():
    image_file = '/home/han/datasets/train-images-idx3-ubyte.gz'

    f = gzip.open(image_file, 'r')
    magic_number = int.from_bytes(f.read(4),'big')
    num_imgs = int.from_bytes(f.read(4), 'big')
    dim1 = int.from_bytes(f.read(4), 'big')
    dim2 = int.from_bytes(f.read(4), 'big')
    buf = f.read(dim1 * dim2 * num_imgs)
    img_data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    img_data = img_data.reshape(num_imgs, dim1, dim2, 1)
    return img_data

def load_labels():
    label_file = '/home/han/datasets/train-labels-idx1-ubyte.gz'

    f = gzip.open(label_file,'r')
    magic_number = int.from_bytes(f.read(4), 'big')
    num_labels = int.from_bytes(f.read(4), 'big')
    buf = f.read(num_labels)
    label_data = np.frombuffer(buf, dtype=np.byte).astype(np.uint8)

    return label_data
