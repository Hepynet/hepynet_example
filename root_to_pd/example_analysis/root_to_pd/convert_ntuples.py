import pathlib
import sys

import pandas as pd
import psutil
import uproot

MB = 1024 * 1024
GB = MB * 1024

# setups
data_dir = ""
ntup_dir = pathlib.Path(f"{data_dir}/example_analysis/ntuples")
df_dir = pathlib.Path(f"{data_dir}/example_analysis/data_frames")
df_dir.mkdir(parents=True, exist_ok=True)

feature_list = [
    "is_mm",
    "lept_0_pt",
    "lept_1_pt",
    "ll_pt",
    "ll_m",
    "ll_dphi",
    "jet_0_pt",
    "jet_1_pt",
    "n_jet",
    "n_bjet",
    "met",
    "met_sumet",
    "met_sig",
    "weight",
]

bkg_names = ["background"]
sig_names = ["signal"]

# convert to pandas DataFrame
def process_sample(sample_name, sample_path, is_sig, is_mc, channel, camp=None):
    print(f"Processing: {sample_name}")
    sample_dfs = list()
    for chunk_pd in uproot.iterate(
        f"{sample_path}:ntup",
        feature_list,
        cut=f"(ll_m >= 200) & ({channel} == 1)",
        library="pd",
        step_size="200 MB",
    ):
        mem_available = psutil.virtual_memory().available / GB
        mem_total = psutil.virtual_memory().total / GB
        print(
            f"RAM usage {mem_available:.02f} / {mem_total:.02f} GB",
            end="\r",
            flush=True,
        )
        # convert float64 to float32
        f64_cols = chunk_pd.select_dtypes(include="float64").columns
        chunk_pd[f64_cols] = chunk_pd[f64_cols].astype("float32")
        # add tags
        chunk_pd = chunk_pd.assign(sample_name=sample_name)
        chunk_pd = chunk_pd.assign(camp=camp)
        chunk_pd = chunk_pd.assign(is_sig=is_sig)
        chunk_pd = chunk_pd.assign(is_mc=is_mc)
        # update df list
        sample_dfs.append(chunk_pd)
    sys.stdout.write("\033[K")
    return sample_dfs


## mm channel
df_list = list()
save_dir = df_dir / "mm"
save_dir.mkdir(parents=True, exist_ok=True)
### bkg
for bkg_name in bkg_names:
    root_path = ntup_dir / f"{bkg_name}.root"
    df_list += process_sample(bkg_name, root_path, False, True, "is_mm", camp="run2")
### sig
for sig_name in sig_names:
    root_path = ntup_dir / f"{sig_name}.root"
    df_list += process_sample(sig_name, root_path, True, True, "is_mm", camp="run2")
### dump
df = pd.concat(df_list, ignore_index=True)
save_path = save_dir / "example_input.feather"
print(f"## Saving to {save_path}")
df.to_feather(save_path)  # feather is recommended format
