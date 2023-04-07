# Notebooks

The current implementation of this research project is divided into several Jupyter Notebooks:

1. **`processing.ipynb`**: Initial imports, pre-processing, data cleaning & clean on-disk saving (CSV/Parquet)
2. **`eda_visualization.ipynb`**: EDA & Data Visualization to enhance the processing part
3. **`bitcoin_trading.ipynb`**: Implementation of a Bitcoin (*BTC*) trading strategy
3. **`ethereum_trading.ipynb`**: Implementation of a Ethereum (*ETH*) trading strategy **using Transfer Learning**.

The Python script **`src/Utils.py`** contains necessary global variables, functions and methods used in these notebooks.

## Code snippet

One need to include the following Python code cell at the beginning of every new Jupyter Notebook added in this folder `notebooks/`.

```python
import sys, os, ipynbname
NOTEBOOK_NAME = f"{ipynbname.name()}.ipynb"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(NOTEBOOK_NAME), os.path.pardir)))
```