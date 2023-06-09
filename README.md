# ML/DL Crypto Trading strategies


<img src="https://img.shields.io/static/v1?label=Range&message=Academic project&color=007bff"/>&nbsp;&nbsp;<img src="https://img.shields.io/static/v1?label=Languages&message=Python&color=ff0000"/>&nbsp;&nbsp;<img src="https://img.shields.io/static/v1?label=Restriction&message=YES&color=26c601"/>

![GitHub release (latest by date)](https://img.shields.io/github/v/release/lcsrodriguez/CuttingEdge-Milliman)  &nbsp;![python version | 3.10+](https://img.shields.io/badge/python%20version-3.10+-magenta) &nbsp; [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Workflows**: ![](https://img.shields.io/badge/Dependabot-enabled-blue)

**Project homepage**: [lcsrodriguez.github.io/qf/ml](https://lcsrodriguez.github.io/qf/ml)

## Overview

This academic project follows the below outline:

1. Personal skill development on crypto-currencies trading and algorithmic trading techniques
2. State-of-the-art of most common trading strategies on BTC
3. Implementation of a custom trading strategy on BTC
4. Backtest of the given trading strategy (on at least 200 trades)
5. Use of transfer learning to extend our strategy on other crypto-currencies

For ML/DL, we have used **XGBoost** and **LSTM** models to forecast future market movements (*binary classification*).


Academic project with financial datasets based on [G-Research Crypto Forecasting](https://www.kaggle.com/competitions/g-research-crypto-forecasting) Kaggle competition.


## Architecture

```
.
├── README.md
├── assets
│   ├── README.md
│   ├── csv
│   └── parquet
├── data
│   ├── asset_details.csv
│   ├── example_test.csv
│   ├── supplemental_train.csv
│   └── train.csv
├── main.ipynb
├── notebooks
│   ├── README.md
│   ├── bitcoin_trading.ipynb
│   ├── eda_visualization.ipynb
│   ├── ethereum_trading.ipynb
│   ├── models
│   └── processing.ipynb
├── out
│   ├── README.md
│   ├── backtests
│   └── models
├── requirements.txt
└── src
    ├── Backtesting.py
    ├── Strategies.py
    └── Utils.py
```

To reproduce on local machine the file architecture, please run:
`tree -L 2 -I 'site|*__|img'`

## Getting started

0. Clone the repository
```bash
git clone git@github.com:lcsrodriguez/cryptotrading.git
cd cryptotrading/
```

1. Download the pre-requirements modules
```bash
pip3 -r requirements.txt
```

2. Execute the Jupyter environment
```
jupyter-notebook .
```

## License

[See `LICENSE` file](LICENSE)

- **Arian NAJAFY ABRANDABADY - Lucas RODRIGUEZ - Bastien TRIDON**
- *Academic works (March - May 2023)*