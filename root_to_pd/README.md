# **Example to Convert ROOT Files to pandas Dataframe**

## **Basics**

- **uproot**

  used to convert ROOT files to Dataframe

- **pandas & numpy**

  two major packages to process inputs data

- **tags to be added to the Dataframe**

  besides the input features, you should include at least the following columns:

  - sample_name : name to identify the sample
  - is_mc : whether the event is from MC sample
  - is_sig : whether the event is signal

  you can also add other tags to be used as cut before training

## **Setup Environment for Hepynet Inputs Dumping**

- With [Conda](https://www.anaconda.com/) (**Recommended**)

  ```bash
  source root_to_pd/setup_env.sh
  ```

## **Run the Example Script**

  ```bash
  python root_to_pd/convert_ntuples.py
  ```
