########################################################
# PROGRAM:  00Py_GRINGOTT_test_yfinance.py
# DATE:     02/04/202
# NOTE:     
########################################################

#### LINK INTERESSANTI ####
# https://towardsdatascience.com/historical-stock-price-data-in-python-a0b6dc826836

#### INIZIALIZZAZIONE ####

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
%matplotlib inline

#### CARICAMENTO DATI ####
# Get the data for the stock AAPL
data = yf.download('G','2016-01-01','2020-04-01')

# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show()