from .Utils import *


# Defining the strategy
class RsiOscillator(Strategy):
    """
    Class Strategy
    """
    upper_bound = 70
    lower_bound = 30
    rsi_window = 3

    # Do as much initial computation as possible
    def init(self):
        """
        """
        self.daily_rsi = self.I(tap.rsi, pd.Series(self.data.Close), self.rsi_window)
    
    # Step through bars one by one
    # Note that multiple buys are a thing here
    def next(self):
        #print(len(self.data.df))
        price = self.data.df.iloc[-1]
        #print(type(price))
        
        print(len(self.daily_rsi))
        # Use the history (thanks to the I (indicator function)) + 
        # Use the prediction for the l (future lag) next 10 iterations from now on 
        # To do so, we are taking the current_dt and adding the delta (l: future lag to get a dataframe/series
        # with our different predicted models (binary target and/or another ))
        # For instance, check whether we have an increasing/decreasing trend for the next values
        
        current_dt = price.name
        #print(current_dt, price["Close"])
        #print("---")
        self.hello_world()
        if crossover(self.daily_rsi, self.upper_bound):
            self.position.close()
        # Check crossover
        elif crossover(self.lower_bound, self.daily_rsi):
            self.buy()


def MovingAverage(closes:pd.Series, n:int) -> pd.Series:
    return pd.Series(closes).rolling(n).mean()
            
            
class SmaCross(Strategy):
    sma_fast = 12
    sma_slow = 24
    
    def init(self):
        self.sma1 = self.I(MovingAverage, self.data.Close, self.sma_fast)
        self.sma2 = self.I(MovingAverage, self.data.Close, self.sma_slow)

    def next(self):
        if self.position and crossover(self.sma1, self.sma2):
            self.buy()
        elif self.position and crossover(self.sma2, self.sma1):
            self.position.close()

class Custom(Strategy):
    def init(self):
        """
        Initialize the strategy
        """
        # To pass additional data, write it here or overload the Backtest class to pass 
        # via the _strategy member, any additional information
        
        #self.sma1 = self.I(MovingAverage, self.data.Close, 12)
        #self.sma2 = self.I(MovingAverage, self.data.Close, 24)
        #self.daily_rsi = self.I(tap.rsi, pd.Series(self.data.Close), 3)
        self.HORIZON_LAG_FUTURE = 10
        self.ONLY_PREDS_COLUMNS = [str(k) for k in list(range(1, self.HORIZON_LAG_FUTURE + 1))]
        pass

    def next(self):
        """
        Main strategy runtime method
        Main method where strategy decisions upon data precomputed in Strategy.init() take place.
        """
        
        # Getting last bar (OHLCV) + Indicators
        current_bar = self.data.df.iloc[-1]
        
        # Getting current datetime
        current_dt = current_bar.name
        #print(f"Processing --> {current_dt}")
        
        # Getting predictions for the next 10 times
        current_preds = self.preds.loc[current_dt][self.ONLY_PREDS_COLUMNS]
        
        # Computing potential future trends for short and long terms
        short_term = current_preds[:self.HORIZON_LAG_FUTURE//2].sum() # For the 5 first next times
        long_term = current_preds[self.HORIZON_LAG_FUTURE//2:].sum() # For the 5 last next times
        
        # Computing number of UP/DOWN predictions on whole time horizon
        whole_term_up = np.array(short_term + long_term) # For the 10 next times (aggregation ==> sum)
        whole_term_down = len(self.ONLY_PREDS_COLUMNS) - np.array(whole_term_up)
        #print(f"U{whole_term_up}/D{whole_term_down}")
        
        # Implementation of the trading strategy
        # TODO
        if whole_term_up > 5:
            #print("BUY")
            self.buy()
        elif whole_term_down > 7:
            #print("SELL")
            self.position.close()
        
        """
        # SMA crossover
        if crossover(self.sma1, self.sma2):
            print("C1")
        elif crossover(self.sma2, self.sma1):
            print("C2")
        """