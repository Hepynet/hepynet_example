# **Hepynet Example (v0.4.2)**

Minimal example to show to work with [**hepynet v0.4.2**](https://github.com/Hepynet/hepynet)

## **Introduction**

Goal of the hepynet: perform DNN related high energy physics analysis tasks with simple config files

- for **ATLAS Analysis**: include supports for various ATLAS analysis jobs

- **Config Driven**: all tasks defined by a simple config file

- **Python Based**: codes are written in Python, which is the mainstream language for DNN studies

This repository setup the workspace to make use of **hepynet**.

## **Setup**

- **Method 1** - With [Conda](https://www.anaconda.com/) (**Recommended**)

  ```bash
  conda create -n hepynet python=3.8
  conda activate hepynet
  pip install hepynet
  ```

- **Method 2** - Direct install (**Not recommended**)

  ```bash
  pip install hepynet
  ```

- **Method 3** - With Docker

  Install [Docker](https://www.docker.com/) if not installed.

  Replace the following items in the docker starting scripts:

  - data directory: path to the directory, where you save the input data

  - version: hepynet version, for example v0.4.1

  On every startup

  - **Linux Command Line**

    ```bash
    source docker/start_docker_example_linux.sh
    ```

  - **Windows PowerShell**

    ```bash
    . docker/start_docker_example_win.bat
    ```

  - **Windows file explorer**

    double-click docker/start_docker_example_win.bat

  Note: if the Docker image is not installed yet, this will automatically pull the required image from [Docker Hub](https://hub.docker.com/)

## **GPU support**

- You can refer to [Tensorflow GPU support](https://www.tensorflow.org/install/gpu) to set up environment to use GPU for training

- This is **NOT** mandatory, CPU alone is enough to run hepynet

## **Preparations**

- **Prepare pandas DataFrame as inputs**

  - use [uproot](https://uproot.readthedocs.io/en/latest/#) to convert ROOT files to pandas DaraFrame, see examples under root_to_pd

- **Prepare job config files**

  all config files are put under share folder, there are 3 types of config files you should prepare/modify

  - **cross_platform.pc_meta.yaml**

    You can specify the data folder (where you keep the input files) here

  - **train configs**: configs for a model training job

  - **apply configs**: configs for a model applying job

  please refer to [config_preparing.md](docs/config_preparing.md) for more details

## **Example run on lxplus**

- **Copy example ROOT files**

  ```bash
  git clone --recursive git@github.com:Hepynet/hepynet_example.git
  cd hepynet_example
  mkdir -p data/ntuples
  cp /afs/cern.ch/work/y/yangz/public/shared_files/hepynet_example/root_files/*  data/ntuples
  ```

  The example inputs are two signal samples at two close mass points (250/300 GeV).
  One used as signal and the other used as background for usage demonstration.

- **Convert ROOT files to hepynet inputs**

  follow [instructions](root_to_pd/README.md) to convert files

  ```bash
  source root_to_pd/setup_env.sh
  ```

## **Run Hepynet**

perform training

```bash
conda activate hepynet
hepynet share/example/train_dnn.yaml
```

applying model to evaluate

```bash
hepynet share/example/apply_dnn.yaml
```
