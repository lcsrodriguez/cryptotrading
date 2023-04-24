import glob
import matplotlib.pyplot as plt
import warnings
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly_resampler import FigureResampler, FigureWidgetResampler
import missingno as msn
import talib as ta
import sys
import time
import os
import tqdm
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, TimeSeriesSplit
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from xgboost import *
import pandas_ta as tap
import xgboost
import time
import datetime
from backtesting import Backtest, Strategy
from backtesting.lib import crossover, resample_apply

# Setting default parameters
plt.rcParams["figure.figsize"] = [12, 5] # Figure sizes for Matplotlib 
plt.rcParams["axes.prop_cycle"] = plt.cycler(color=["blue", "green", "red", "orange", "purple", "magenta"]) # Color for plotting

# Silencing all warnings for a better UX
warnings.filterwarnings("ignore")


class Utils:
    """
    Class Utils containing several global variables (as arrays, dictionnaries), functions, static methods
    to handle the dataset in one unique way
    """

    # Folders
    DATA_FOLDER = "../data"
    ASSETS_FOLDER = "../assets"

    # Column labels
    OHLC = ["Open", "High", "Low", "Close"]
    OHLCV = OHLC + ["Volume"]
    TRADING_ACTIVITY = ["Count"]
    VWAP = ["VWAP"]
    TARGET = ["Target"]
    ALL_COLUMNS = TRADING_ACTIVITY + OHLCV + VWAP

    # Data filenames
    DATA_FILENAMES = glob.glob(f"{DATA_FOLDER}/*.csv")

    # Asset details
    ASSET_DETAILS = pd.read_csv(filepath_or_buffer=f"{DATA_FOLDER}/asset_details.csv", index_col="Asset_ID")
    
    # Asset ids
    ASSET_IDS = sorted(list(ASSET_DETAILS.index))

    # Asset names
    ASSET_NAMES = sorted(list(ASSET_DETAILS["Asset_Name"].to_numpy()))

    # Filenames hashmap for better user handling
    FILENAMES = {
        "ASSET_DETAILS": f"{DATA_FOLDER}/asset_details.csv",
        "TRAIN_2": f"{DATA_FOLDER}/supplemental_train.csv",
        "TRAIN": f"{DATA_FOLDER}/train.csv",
        "TEST": f"{DATA_FOLDER}/example_test.csv"
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
    
    @staticmethod
    def get_daytime_range(x: int) -> int:
        """
        Function returning a coded version of daytime range
        """
        if (x > 4) and (x <= 8):
            return 0 # Early Morning
        elif (x > 8) and (x <= 12 ):
            return 1 # Morning
        elif (x > 12) and (x <= 16):
            return 2 # Noon
        elif (x > 16) and (x <= 20) :
            return 3 # Eve
        elif (x > 20) and (x <= 24):
            return 4 # Night
        elif (x <= 4):
            return 5 # Night
        
    @staticmethod
    def rsi(df: pd.DataFrame, periods = 10, ema = True) -> pd.Series:
        """
        Returns a pd.Series with the Relative Strength Index (RSI)
        ==> Technical analysis indicator (see report)
        """
        # Computing the Close price delta
        close_delta = df["Close"].diff()

        # Make two series: one for lower closes and one for higher closes
        up = close_delta.clip(lower=0)
        down = -1 * close_delta.clip(upper=0)
        
        if ema == True:
            # Use exponential moving average
            ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
            ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
        else:
            # Use simple moving average
            ma_up = up.rolling(window = periods, adjust=False).mean()
            ma_down = down.rolling(window = periods, adjust=False).mean()
        
        # Computing the RSI
        rsi = ma_up / ma_down
        rsi = 100 - (100/(1 + rsi))
        return rsi
    
    @staticmethod
    def get_preds_time_interval(preds_: pd.DataFrame) -> dict:
        """
        Function returning start and end datetimes from predictions
        """
        i = list(preds_.index)
        return {"start_dt": i[0], "end_dt": i[-1]}