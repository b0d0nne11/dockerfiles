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
ENV WEEWX_SDR_REF=d25aec7
RUN set -ex \
    && apk add --no-cache --virtual .build git \
    \
    && mkdir -p /usr/src/weewx-sdr \
    && git clone git://github.com/b0d0nne11/weewx-sdr.git /usr/src/weewx-sdr \
    && cd /usr/src/weewx-sdr \
    && git checkout ${WEEWX_SDR_REF} \
    \
    && /home/weewx/bin/wee_extension --install /usr/src/weewx-sdr \
    \
    && rm -rf /usr/src/ \
    && apk del .build

# Install Adafruit_Python_GPIO
ENV ADAFRUIT_GPIO_REF=22a1ff4
RUN set -ex \
    && apk add --no-cache --virtual .build git gcc musl-dev python2-dev linux-headers \
    \
    && mkdir -p /usr/src/Adafruit_Python_GPIO \
    && git clone git://github.com/adafruit/Adafruit_Python_GPIO.git /usr/src/Adafruit_Python_GPIO \
    && cd /usr/src/Adafruit_Python_GPIO \
    && git checkout ${ADAFRUIT_GPIO_REF} \
    \
    && python setup.py install \
    \
    && rm -rf /usr/src/ \
    && apk del .build

# Install Adafruit_Python_BME280
ENV ADAFRUIT_BME280_REF=68dda31
RUN set -ex \
    && apk add --no-cache --virtual .build git \
    \
    && mkdir -p /usr/src/Adafruit_Python_BME280 \
    && git clone git://github.com/adafruit/Adafruit_Python_BME280.git /usr/src/Adafruit_Python_BME280 \
    && cd /usr/src/Adafruit_Python_BME280 \
    && git checkout ${ADAFRUIT_BME280_REF} \
    \
    && python setup.py install \
    \
    && rm -rf /usr/src/ \
    && apk del .build

COPY weewx.conf /home/weewx/weewx.conf
COPY skin.conf /home/weewx/skins/Standard/skin.conf
COPY bme280.py /home/weewx/bin/user/bme280.py

WORKDIR /home/weewx
CMD bin/weewxd weewx.conf
