import streamlit as st
import yaml
import pandas as pd

# App
st.set_page_config(
    page_title="🔍 WL Checker",
    layout="wide",
)

# Params
params_path = "params.yaml"


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


config = read_params(params_path)

# Title
st.title("🔍 WL Checker")

# DF
wl_sheet = config["data"]["wl_addy"]
wl_df = pd.read_csv(wl_sheet)
wl_df["address"] = wl_df["address"].str.lower()

wallet_address = st.text_input(
    label="Your wallet address",
    placeholder="Enter your wallet address",
    max_chars=42,
)

if wallet_address:
    # Read Data
    try:
        if any(wallet_address.lower() == wl_df["address"]):
            message = ":clap: Congrats. You are in the whitelist."
        else:
            message = ":crying_cat_face: Sorry. You are not in the whitelist."

        # creating a single-element container
        placeholder = st.empty()

        # Empty Placeholder Filled
        with placeholder.container():
            if wallet_address:
                st.subheader(message)

        # Note
        st.markdown("#")
        st.markdown("#")
        st.caption(
            """
            Holders of LQDR Crew, Pop Pussies, Oath Fanatics, Cursed Circus, theNFTs, Pixel Pirate, Pirate Life, Liquicats and Tour de Berance NFTs are whitelisted.

            If you think you should be whitelisted and cannot find your address let us know.
            """
        )

    except Exception as e:
        print(e)
        st.markdown("Error Please Try Again")
