ARG CLANG_IMAGE_TAG=llvm-clang-13.0.0
ARG PUID=1000
ARG GUID=1000
FROM ubuntu:20.04 AS llvm-clang-13.0.0
RUN apt update -y && DEBIAN_FRONTEND="noninteractive" apt install -y wget cmake g++ ninja-build patch tar python3-dev git

# install clang
COPY frama-clang/clang-mangle-fix.patch /pkm-api/
RUN cd /root && \
    wget -qO- https://github.com/llvm/llvm-project/archive/llvmorg-13.0.0.tar.gz | tar zxf - && \
    cd /root/llvm-project-llvmorg-13.0.0 && \
    patch -p1 < /pkm-api/clang-mangle-fix.patch && \
    mkdir build && \
    cd build && \
    cmake -G Ninja -DLLVM_ENABLE_PROJECTS=clang -DCMAKE_BUILD_TYPE=MinSizeRel /root/llvm-project-llvmorg-13.0.0/llvm && \
    cmake --build . && \
    cmake -DCMAKE_INSTALL_PREFIX=/opt/llvm-clang-13.0.0 -P cmake_install.cmake && \
    rm -rf /root/llvm-project-llvmorg-13.0.0
FROM $CLANG_IMAGE_TAG AS clang
FROM ubuntu:20.04 AS frama-clang
LABEL description="Frama-Clang for PKM"

# Note: line below is commented because focal is currently missing in OPAM PPA
# RUN add-apt-repository ppa:avsm/ppa && apt update -y && apt install -y opam
RUN apt update -y && \
    DEBIAN_FRONTEND="noninteractive" apt install -y wget && \
    wget -qO- https://deb.nodesource.com/setup_12.x | bash - && \
    DEBIAN_FRONTEND="noninteractive" apt install -y  cmake g++ clang python3-pip unzip python3-dev git \
        gcc tar autoconf automake autoconf-archive autotools-dev \
        libtool software-properties-common dos2unix \
        nodejs maven jq curl pkg-config libcairo2-dev libgnomecanvas2-dev \
        libgtksourceview-3.0-dev libgmp-dev graphviz opam

# install clang
COPY --from=clang /opt/llvm-clang-13.0.0 /opt/llvm-clang-13.0.0
ENV PATH="/opt/llvm-clang-13.0.0/bin:${PATH}"

ARG PUID
ARG GUID

# create a group and a user
# set user random seed for openssl
RUN groupadd -g ${GUID} frama-clang && \
    useradd -r -u ${PUID} -g frama-clang -d /pkm-api frama-clang && \
    mkdir -m 700 /pkm-api && \
    head -c 64 /dev/urandom > /pkm-api/.rnd && \
    chown frama-clang:frama-clang /pkm-api

USER frama-clang
WORKDIR /pkm-api

# initialize OPAM and install OCaml libraries
RUN opam init --shell-setup --bare --disable-sandboxing -y
SHELL ["/bin/bash", "-l", "-c"]
RUN opam switch -y create ocaml-base-compiler.4.08.1 && \
    opam install -y depext && \
    opam depext lablgtk3 lablgtk3-sourceview3 && \ 
    opam install -y lablgtk3 lablgtk3-sourceview3 && \
    opam pin -y add ocamlgraph 1.8.8 && \
    opam pin -y add why3 1.2.1 && \
    opam install -y zarith alt-ergo yojson coq && \
    opam install -y ppx_deriving ppx_deriving_yojson

# install frama-c itself
COPY frama-c/frama-c-20.0+dev-DECODER-Calcium.tgz frama-c/json-printer.tgz /pkm-api/frama-c/
RUN tar -xzf frama-c/frama-c-20.0+dev-DECODER-Calcium.tgz && \
    cd frama-c-20.0+dev-DECODER-Calcium && \
    ./configure --prefix=/pkm-api/.opam/4.08.1 && \
    make clean && \
    make && \
    make install
ENV PATH="/pkm-api/.opam/4.08.1/bin:/pkm-api/.opam/ocaml-base-compiler.4.08.1/bin:${PATH}"
RUN tar -xzf frama-c/json-printer.tgz && \
    cd /pkm-api/json-printer && \
    make && \
    make install && \
    why3 config --detect

# install OpenAPI Generator
RUN mkdir /pkm-api/bin && \
    wget -O /pkm-api/bin/openapi-generator-cli.sh https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh && \
    chmod +x /pkm-api/bin/openapi-generator-cli.sh
ENV PATH="/pkm-api/bin:${PATH}"

# install pkm-api
COPY --chown=frama-clang:frama-clang openapi_gen.conf Apache-2.0.txt AGPL-3.0.txt package.json /pkm-api/
COPY --chown=frama-clang:frama-clang openapi_gen /pkm-api/openapi_gen
COPY --chown=frama-clang:frama-clang api /pkm-api/api
RUN mkdir /pkm-api/frama-clang
COPY --chown=frama-clang:frama-clang frama-clang/openapi_gen.conf /pkm-api/frama-clang
COPY --chown=frama-clang:frama-clang frama-clang/api /pkm-api/frama-clang/api
COPY --chown=frama-clang:frama-clang frama-clang/services /pkm-api/frama-clang/services
COPY --chown=frama-clang:frama-clang frama-clang/server_config.json /pkm-api/frama-clang/server_config.json
COPY --chown=frama-clang:frama-clang util /pkm-api/util
COPY --chown=frama-clang:frama-clang ssl /pkm-api/ssl

# generate PKM client SDK
RUN dos2unix ./openapi_gen/generate_client.sh && ./openapi_gen/generate_client.sh
ENV NODE_PATH="/pkm-api:${NODE_PATH}"

# generate Frama-Clang server and client SDK
RUN dos2unix ./openapi_gen/generate_server.sh && \
             ./openapi_gen/generate.sh frama-clang

# install nodejs packages dependencies
RUN cd /pkm-api/pkm_restful_api && npm install && \
    cd /pkm-api/frama-clang/server && npm install && \
    cd /pkm-api && npm install

# install SSL certificate of PKM server
USER root
RUN mkdir -p /usr/local/share/ca-certificates && \
    chmod 755 /usr/local/share/ca-certificates && \
    cp -f /pkm-api/ssl/pkm_docker.crt /usr/local/share/ca-certificates && \
    chmod 644 /usr/local/share/ca-certificates/pkm_docker.crt && \
    update-ca-certificates
USER frama-clang

# prepare server initialization script
RUN dos2unix ./frama-clang/server/start_server.sh && chmod +x ./frama-clang/server/start_server.sh

EXPOSE 8082
CMD [ "./frama-clang/server/start_server.sh" ]
