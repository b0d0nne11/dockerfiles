FROM hypriot/rpi-alpine:3.6
MAINTAINER Brendan O'Donnell <brendan@odonnell.xyz>

ENV PATH /usr/local/bin:$PATH

# Install run-time dependancies
RUN set -ex \
    && apk add --no-cache curl-dev openssl-dev libgcc

# Install cpuminer
RUN set -ex \
    && apk add --no-cache --virtual .build git gcc musl-dev autoconf automake make g++ \
    \
    && mkdir -p /usr/src/veriumMiner \
    && git clone git://github.com/b0d0nne11/veriumMiner.git /usr/src/veriumMiner \
    && cd /usr/src/veriumMiner \
    && git checkout -q brendan/use-less-memory \
    \
    && ./autogen.sh \
    && ./configure CFLAGS="-O2 -march=native -mfpu=neon" --with-crypto --with-curl \
    && make \
    && make install \
    \
    && rm -rf /usr/src/ \
    && apk del .build

ENV WorkerName=WorkerName
ENV WorkerPass=WorkerPass

CMD cpuminer -n 1048576 -o stratum+tcp://us.vrm.mining-pool.ovh:3032 -u ${WorkerName} -p ${WorkerPass} --threads 3
