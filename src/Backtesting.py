from .Utils import *
from .Strategies import *


class BT(Backtest):
    def __init__(self, predictions_: pd.DataFrame, *args, **kwargs):
        """
        """
        print("Initializing the backtest instance ...")
        super().__init__(*args, **kwargs)
        self._strategy.hello_world = lambda x: x == 1
        self._strategy.preds = predictions_
    
    def run(self, *args, **kwargs):
        """
        """
        print("Running the backtest procedure ...")
        return super().run(*args, **kwargs)