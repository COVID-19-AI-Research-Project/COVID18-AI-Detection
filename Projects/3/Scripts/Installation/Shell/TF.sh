#!/bin/bash

FMSG="- Python libraries and Tensorflow installation terminated"

read -p "? This script will install the COVID-19 AI Classification's required Python libraries and Tensorflow on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    echo "- GeniSysAI installing Python libraries and Tensorflow"

    pip3 install numpy
    pip3 install pickle-mixin
    pip3 install os-sys
    pip3 install times
    pip3 install h5py
    pip3 install random2
    pip3 install tensorboard==2.1.0
    pip3 install tensorflow==2.1.0
    pip3 install tensorflow-gpu==2.1.0

    exit 0

else
    echo $FMSG;
    exit 1
fi