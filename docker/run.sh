# run simply with ---mount
# docker run -it --mount type=bind,source=${PWD}/VDCT,target=/home/hopekr/VDCT huong-ubuntu sh
# https://hub.docker.com/r/weliveindetail/frama-clang
docker run --privileged --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --security-opt apparmor=unconfined \
           --name frama_clang -v $(pwd):/home -t huong/frama-clang:v1