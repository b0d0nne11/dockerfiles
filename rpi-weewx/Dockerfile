FROM hypriot/rpi-alpine:3.6
MAINTAINER Brendan O'Donnell <brendan@odonnell.xyz>

ENV PATH /usr/local/bin:$PATH

# Install run-time dependancies
RUN set -ex \
    && apk add --no-cache python2 libusb-dev freetype-dev jpeg-dev sqlite

# Install weewx
ENV WEEWX_REF=v3.7.1
RUN set -ex \
    && apk add --no-cache --virtual .build git gcc musl-dev python2-dev py2-pip \
    \
    && pip install --no-cache-dir configobj Cheetah pillow pyusb pyephem \
    \
    && mkdir -p /usr/src/weewx \
    && git clone git://github.com/weewx/weewx.git /usr/src/weewx \
    && cd /usr/src/weewx \
    && git checkout ${WEEWX_REF} \
    \
    && ./setup.py build \
    && ./setup.py install --no-prompt \
    \
    && rm -rf /usr/src/ \
    && apk del .build

# Install rtl-sdr
ENV RTL_SDR_REF=18bf269
RUN set -ex \
    && apk add --no-cache --virtual .build git gcc musl-dev make cmake \
    \
    && mkdir -p /usr/src/rtl-sdr \
    && git clone git://git.osmocom.org/rtl-sdr.git /usr/src/rtl-sdr \
    && cd /usr/src/rtl-sdr \
    && git checkout ${RTL_SDR_REF} \
    \
    && mkdir build \
    && cd build \
    && cmake ../ \
    && make \
    && make install \
    \
    && rm -rf /usr/src/ \
    && apk del .build

# Install rtl_433
ENV RTL_433_REF=c6e79a3
RUN set -ex \
    && apk add --no-cache --virtual .build git gcc musl-dev make cmake \
    \
    && mkdir -p /usr/src/rtl_433 \
    && git clone git://github.com/merbanan/rtl_433.git /usr/src/rtl_433 \
    && cd /usr/src/rtl_433 \
    && git checkout ${RTL_433_REF} \
    \
    && mkdir build \
    && cd build \
    && cmake ../ \
    && make \
    && make install \
    \
    && rm -rf /usr/src/ \
    && apk del .build

# Install weewx-sdr
ENV WEEWX_SDR_REF=fca976c
RUN set -ex \
    && apk add --no-cache --virtual .build git \
    \
    && mkdir -p /usr/src/weewx-sdr \
    && git clone git://github.com/matthewwall/weewx-sdr.git /usr/src/weewx-sdr \
    && cd /usr/src/weewx-sdr \
    && git checkout ${WEEEX_SDR_REF} \
    \
    && /home/weewx/bin/wee_extension --install /usr/src/weewx-sdr \
    \
    && rm -rf /usr/src/ \
    && apk del .build

COPY weewx.conf /home/weewx/weewx.conf
COPY skin.conf /home/weewx/skins/Standard/skin.conf

WORKDIR /home/weewx
CMD bin/weewxd weewx.conf