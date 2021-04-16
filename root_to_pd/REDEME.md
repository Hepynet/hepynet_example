# **Example to Convert ROOT Files to pandas Dataframe**

## **Basic Concepts**

- **uproot**

  used to convert ROOT files to Dataframe

- **pandas & numpy**

  two major packages to process inputs data

- **tags to be added to the Dataframe**

  besides the input features, you should also include following columns:

  - sample_name : name to identify the sample
  - camp : campaign of the sample, mc16a/mc16d/mc16e/run2?
  - is_mc : whether the event is from MC sample
  - is_sig : whether the event is signal



## **Setup Environment for Hepynet Inputs Dumping**

- **Method 1** - With [Conda](https://www.anaconda.com/) (**Recommended**)

  ```bash
  source root_to_pd/setup_env.sh
  ```

- **Method 2** - With Docker (For multi-OS users)

  Install [Docker](https://www.docker.com/) if not installed.

  Replace the following items in the docker starting scripts:

  - data directory: path to the directory, where you save the input data

  ### **Run the Example Script**

  ```bash
  python root_to_pd/convert_ntuples.py
  ```

## **Run Hepynet**

perform training

```bash
hepynet share/example/train_dnn.yaml
```

applying model to evaluate

```bash
hepynet share/example/apply_dnn.yaml
```

