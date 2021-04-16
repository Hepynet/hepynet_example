docker run -it --rm \
    -v $(git rev-parse --show-toplevel):/work \
    -v <data direcotry>:/data \
    -w /work \
    starp/hepynet_root_io:v0.1 bash
