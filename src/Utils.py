import glob
import matplotlib.pyplot as plt
import warnings
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Setting default parameters
plt.rcParams["figure.figsize"] = [12, 5] # Figure sizes for Matplotlib 
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["blue", "green", "red", "orange", "purple", "magenta"]) # Color for plotting

# Silencing all warnings for a better UX
warnings.filterwarnings("ignore")

class Utils:
    """Class Utils
    """

    # Column labels
    OHLC = ["Open", "High", "Low", "Close"]
    OHLCV = OHLC + ["Volume"]
    TRADING_ACTIVITY = ["Count"]
    VWAP = ["VWAP"]
    TARGET = ["Target"]

    # Data filenames
    DATA_FILENAMES = glob.glob("data/*.csv")

    # Asset details
    ASSET_DETAILS = pd.read_csv(filepath_or_buffer="data/asset_details.csv", index_col="Asset_ID")
    
    # Asset ids
    ASSET_IDS = sorted(list(ASSET_DETAILS.index))

    # Asset names
    ASSET_NAMES = sorted(list(ASSET_DETAILS["Asset_Name"].to_numpy()))

    # Filenames hashmap for better user handling
    FILENAMES = {
        "ASSET_DETAILS": "data/asset_details.csv",
        "TRAIN_2": "data/supplemental_train.csv",
        "TRAIN": "data/train.csv",
        "TEST": "data/example_test.csv"
    }

    @staticmethod
    def check_number_asset_files(complete_package: bool = False) -> bool:
        """Function checking whether we have the good number of files

        Args:
            complete_package (bool, optional): If we have downloaded all the Kaggle repo. Defaults to False.

        Returns:
            bool: Boolean result
        """
        if complete_package:
            return len(Utils.DATA_FILENAMES) == 5
        return len(Utils.DATA_FILENAMES) == 4

    @staticmethod
    def get_asset_id(asset_name: str) -> int:
        """
        Function returning the asset id from a given asset name
        """
        # Getting the list of asset names
        LIST_ASSET_NAMES = Utils.ASSET_DETAILS['Asset_Name'].to_numpy()
        
        # Checking if the asset name is correct
        if str(asset_name) not in LIST_ASSET_NAMES:
            raise Exception(f"The given asset name is unknown\nPlease use one from: {LIST_ASSET_NAMES}")
        
        # Returning the corresponding asset id
        return list(Utils.ASSET_DETAILS.index[Utils.ASSET_DETAILS["Asset_Name"] == str(asset_name)])[0]

    @staticmethod
    def get_asset_name(asset_id: int) -> str:
        """
        Function returning the asset name from a given asset id
        """
        if int(asset_id) not in Utils.ASSET_IDS:
            raise Exception(f"The given asset id is unknown\nPlease use one from: {Utils.ASSET_IDS}")
        
        return Utils.ASSET_DETAILS["Asset_Name"][asset_id]