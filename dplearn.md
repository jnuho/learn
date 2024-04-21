# Introduction

I try to implemnt https://github.com/gyuho/dplearn

## Set up

- WSL 사용설정 (윈도우 10,11)

```shell
# powershell as Admin
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 우분투 설치 (Microsoft Store)

# 재부팅 후 실행
wsl

# 버전 확인
wsl -l -v

# 커널 업데이트 파일 다운로드 및 설치
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

# 버전 업데이트
# 또는 wsl --set-version Ubuntu-22.04 2
wsl --set-version Ubuntu22.04 2


# 업데이트된 버전 상태확인
wsl -l -v
# stopped된 wsl 재실행
wsl

# 디폴트 버전 2 설정
wsl --set-default-version 2
```

- Python virtual environment setup
  - Downlod Python 3.11.9 (from Microsoft Store or from python.org)
  - `venv` for virtual python enviroment setup
  - `requirements.txt`

```python
sudo apt update
sudo apt install python3
sudo apt install python3-pip
pip install -r requirements.txt

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

```sh
DATASETS_DIR=./datasets \
  CATS_PARAM_PATH=./datasets/parameters-cats.npy \
  python3 -m unittest backend.worker.cats.model_test
```



- modify `model.py`

```python
# from scipy import ndimage
import imageio.v3 as iio
from skimage.transform import resize

# img = np.array(ndimage.imread(img_path, flatten=False))
# img_resized = scipy.misc.imresize(img, size=(num_px,num_px)).reshape((num_px*num_px*3,1))
img = np.array(iio.imread(img_path))
img_resized = resize(img, (num_px, num_px)).reshape((num_px*num_px*3,1))
```

- modify `model_test.py`

```python
    def test_classify(self):
        # parameters = np.load(param_path).item()
        parameters = np.load(param_path, allow_pickle=True).item()
```


- modify `Dockerfile-app`

```dockerfile
##########################
# FROM ubuntu:17.10
FROM ubuntu:22.04
##########################

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  # ...
  python3 \
```

- modify `Dockerfile-python3-cpu`

```dockerfile
FROM us-docker.pkg.dev/deeplearning-platform-release/gcr.io/tf2-cpu.2-15.py310

RUN apt-get install -y gcc-4.8 g++-4.8 \
  && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50 \
  && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 50

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
  # ...
  # gcc \
  gcc-4.8 \

  # python-pip \
  python3-dev \
  python3 \
```


- Build image

```sh
./scripts/docker/build-app.sh
./scripts/docker/build-python3-cpu.sh
```

- Run app
  - Open http://localhost:4200/cats and try other cat photos:

```sh
./scripts/docker/run-app.sh
./scripts/docker/run-worker-python3-cpu.sh

<<COMMENT
# to serve on port :80
./scripts/docker/run-reverse-proxy.sh
COMMENT
```


