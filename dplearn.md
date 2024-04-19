# Introduction

I try to implemnt https://github.com/gyuho/dplearn

# Environment

## Python

- Version: Python 3.11.9
- `venv` for virtual python enviroment setup
- `requirements.txt`

```python
# From dev environment, store all installed pacakges
pip freeze > requirements.txt

# In production environment
pip install -r requirements.txt
```

```
# deep learning packages
numpy==1.26.4
h5py==3.10.0
matplotlib==3.8.3
scipy==1.12.0
pillow==10.2.0
imageio==2.34.0
scikit-image==0.23.1

glog==0.3.1
```


- Train Cat 5-layer Deep Neural Network:

in WSL envrionemnt:

```sh

sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip install -r requirements.txt


DATASETS_DIR=./datasets \
  CATS_PARAM_PATH=./datasets/parameters-cats.npy \
  python3 -m unittest backend.worker.cats.model_test
```



- update deprecated codes (model.py, model_test.py)

FROM

```python
from scipy import ndimage

img = np.array(ndimage.imread(img_path, flatten=False))
img_resized = scipy.misc.imresize(img, size=(num_px,num_px)).reshape((num_px*num_px*3,1))

```

TO:

```python
import imageio.v3 as iio
from skimage.transform import resize

img = np.array(iio.imread(img_path))
img_resized = resize(img, (num_px, num_px)).reshape((num_px*num_px*3,1))
```


- edit function call parameter
  - model_test.py


```python
    def test_classify(self):
        # ...
        parameters = np.load(param_path, allow_pickle=True).item()
```

