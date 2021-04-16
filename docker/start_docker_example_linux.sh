docker run -it --rm \
  --gpus all \
  -v $(git rev-parse --show-toplevel):/work \
  -v <data directory>:/data \
  -w /work \
  starp/hepynet:<version>
