FROM nvidia/cuda:12.1.0-devel-ubuntu22.04 AS build

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt -y update --no-install-recommends \
    && apt -y install --no-install-recommends \
    build-essential \
    git \
    python3-dev \
    python3-pip \
    libopenexr-dev \
    libxi-dev \
    libglfw3-dev \
    libglew-dev \
    libomp-dev \
    libxinerama-dev \
    libxcursor-dev \
    && apt autoremove -y \
    && apt clean -y \
	&& export DEBIAN_FRONTEND=dialog

COPY . /instant-ngp

WORKDIR /instant-ngp

RUN pip3 --no-cache-dir install -r ./requirements.txt \
    && git submodule sync --recursive \
    && git submodule update --init --recursive

RUN pip3 --no-cache-dir install cmake \
    && cmake -DNGP_BUILD_WITH_GUI=off ./ -B ./build \
    && cmake --build build --config RelWithDebInfo -j 16

FROM nvidia/cuda:12.1.0-base-ubuntu22.04

WORKDIR /instant-ngp

COPY --from=build /instant-ngp/build ./build
COPY --from=build /instant-ngp/scripts ./instant_ngp
COPY --from=build /instant-ngp/requirements.txt ./requirements.txt
COPY --from=build /instant-ngp/setup.py ./setup.py

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt -y update --no-install-recommends \
    && apt -y install --no-install-recommends python3 python3-pip \
    && pip3 --no-cache-dir install -r ./requirements.txt \
    && pip3 install . \
	&& apt autoremove -y \
    && apt clean -y \
	&& export DEBIAN_FRONTEND=dialog
