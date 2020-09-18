FROM tensorflow/tensorflow:1.12.0-devel-gpu-py3
MAINTAINER NINA <varneyn1@udayton.edu.edu>




RUN apt-get update && apt install -y --fix-missing --no-install-recommends wget\
        g++ \
        vim \
        git \
	libx11-dev \
	xorg-dev \
	libglu1-mesa-dev \
	cmake \ 
	gcc 

RUN apt-get install -y python3-setuptools
RUN apt remove -y cmake
RUN pip3 install cmake 
RUN pip3 install -U scikit-learn scipy numpy 
#RUN pip3 install psutil
#COPY . /pointnet2

RUN pip3 install sklearn_pandas \
      open3d-python \
      laspy \
      opencv-python \
      ipdb \
      Pillow

RUN pip3 install tensorflow-gpu==1.12.0
#WORKDIR /pointnet2/tf_ops
#RUN mkdir -p build && \
#     cd build && \
#     cmake -DCMAKE_C_COMPILER=/usr/bin/gcc .. && \
#     make


    

# Install laspy, pathlib
#RUN apt install -y --fix-missing --no-install-recommends python3-pip
#RUN pip3 install laspy numpy sklearn open3d-python ipdb

# Set working directory
WORKDIR /kpconv
