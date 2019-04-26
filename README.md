# Installation:

## PyGame

```shell
$ sudo apt-get install git python3-dev python3-setuptools python3-numpy python3-opengl \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev             \
    libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev        \
    libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont             \
    xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf libfreetype6-dev
$ git clone https://github.com/pygame/pygame -b 1.9.6
$ cd pygame
$ python3 setup.py build
$ sudo python3 setup.py install
```

## Others dependencies

```shell
$ pip3 install --user -r requirements.txt
```
