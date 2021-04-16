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

## **Prepare Example ROOT Files**

On lxplus:

    """bash
    cd <data dir>
    mkdir -p example_analysis/ntuples
    cp /afs/cern.ch/work/y/yangz/public/shared_files/hepynet_example/root_files 
    """
