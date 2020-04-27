from typing import Any, Dict

import pandas as pd


def get_stock_data(data:pd.DataFrame, example_sp100: CS) -> Dict[str, Any]:
	# '~/Desktop/g`troiani~github/Securities-Analysis/data/01_raw/sp100' is the path to sp100 list.
	#what's the second parameter passed?

"""Node for retrieving list of stocks' data from yahoo finance API"""
	import time
	from yahoo_finance import Share
	import numpy as np
	import pandas as pd
	import pandas_datareader.data as web
	import datetime
	
	# read ticker symbols from a file to python symbol list
	symbol = []
	with open('~/Desktop/g`troiani~github/Securities-Analysis/data/01_raw/sp100') as f:
	    for line in f:
		symbol.append(line.strip())
	f.close

	# datetime is a Python module
	end = datetime.datetime.today()
	start = datetime.date(end.year-3,1,1)

	# set path for csv file
	path_out = '~/Desktop/g`troiani~github/Securities-Analysis/data/02_intermediate'

	# loop through the Russell3000's tickers
	i=0
	while i<len(symbol):
	    try:
		df = web.DataReader(symbol[i], 'yahoo', start, end)
		#df.insert(0,'Symbol',symbol[i])
		#df = df.drop(['Close'], axis=1)
		#df = df.drop(['Open'], axis=1)
		#df = df.drop(['High'], axis=1)
		#df = df.drop(['Low'], axis=1)
		#df = df.drop(['Volume'], axis=1)
		
		if i == 0:
		    df.to_csv(path_out+ str(symbol[i])+ '.csv',)
		    print (i, symbol[i],'data stored')
		    i=i+1
		else:
		    df.to_csv(path_out+str(symbol[i])+ '.csv',mode = 'a',)
		    print (i, symbol[i],'data stored')
		    i=i+1
	    except:
		print("No data could be stored")
		print (i,symbol[i])
		i=i+1
		continue




'''
from typing import Any, Dict

import pandas as pd

def split_data(data: pd.DataFrame, example_test_data_ratio: float) -> Dict[str, Any]:
    """Node for splitting the classical Iris data set into training and test
    sets, each split into features and labels.
    The split ratio parameter is taken from conf/project/parameters.yml.
    The data and the parameters will be loaded and provided to your function
    automatically when the pipeline is executed and it is time to run this node.
    """
    data.columns = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "target",
    ]
    classes = sorted(data["target"].unique())
    # One-hot encoding for the target variable
    data = pd.get_dummies(data, columns=["target"], prefix="", prefix_sep="")

    # Shuffle all the data
    data = data.sample(frac=1).reset_index(drop=True)

    # Split to training and testing data
    n = data.shape[0]
    n_test = int(n * example_test_data_ratio)
    training_data = data.iloc[n_test:, :].reset_index(drop=True)
    test_data = data.iloc[:n_test, :].reset_index(drop=True)

    # Split the data to features and labels
    train_data_x = training_data.loc[:, "sepal_length":"petal_width"]
    train_data_y = training_data[classes]
    test_data_x = test_data.loc[:, "sepal_length":"petal_width"]
    test_data_y = test_data[classes]

    # When returning many variables, it is a good practice to give them names:
    return dict(
        train_x=train_data_x,
        train_y=train_data_y,
        test_x=test_data_x,
        test_y=test_data_y,
    )
'''
