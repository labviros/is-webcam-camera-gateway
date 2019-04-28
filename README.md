# Installation:

## PyGame

It's recommended to compile PyGame from source. To do so, follow the commands bellow.

```shell
$ sudo apt-get update
$ sudo apt-get install -y --no-install-recommends    \
    git python3-dev python3-setuptools python3-numpy \
    libsdl-image1.2-dev libsmpeg-dev libsdl1.2-dev  
$ git clone https://github.com/pygame/pygame -b 1.9.6
$ cd pygame
$ python3 setup.py build
$ sudo python3 setup.py install
```

## Others dependencies

```shell
$ pip3 install --user -r requirements.txt
```
