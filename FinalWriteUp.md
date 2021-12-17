# Final Write Up

This project gave us an insight into big data analytics, and how important it is when analyzing large sets of data. In comparison to single analytics, the tools that are given to us to determine large sets of data are useful in terms of understanding how the stock market fluctuates, and what could potentially be used when analyzing the data itself if it were a stock portfolio, instead of predicting the price of the data.

Since we were using a large set of data, and running most of these models on our local machines, we set up placeholders to determine whether these models would work. When running the actual project itself, we replaced them with our actual datasets as a final run. 

The primary tools that we used to analyze the data itself were Linear Regression, LSTM, and a CNN to determine which was the best model in analyzing the stock market and determining whether it would be predictable. We determined that these models are not the best at determining the accuracy of the data itself, but would be useful in showing the differences between the inaccuracies, and modeling this data off of what would be a better comparison of stock market data itself. Since our original goal of seeing whether we could predict the stock market with a variety of machine learning methods were completed, we analyzed a little further and determined that the best way to use stock market data would be if it were a portfolio of stocks, then clustered using K-Means and PCA in order to reduce and dimensionalize the sectors of stocks themselves. By showing the difference between how K-Means can cluster the data, and how PCA could potentially visualize these clusters, it is possible for better algorithms to show that the moving averages of these stocks as a time series show similarities between each other as a group. Adding these to your stock portfolio can thus increase your profitability if an individual were to know how their stocks ran as a cluster in comparison to others over time. 


Viewing our Project in Separate Notebooks is as follows:

1. project-info.ipynb - This shows our base project info
2. Prototype.ipynb - This shows the prototype of how we were to section off data, along with why big data is important in comparison to running against single stocks
3. yFinanceRetrieval.ipynb - This is a script we wrote, since retreiving the data was a lengthy process
4. Normalizing the Data.ipynb - Shows examples of noramlizing the data
5. LSTM, Linear Regression, and CNN.ipynb - Culmination of our findings and work

Our datasets that we used were primarily from Yahoo Finance, and small prototypes were done on the larger datasets.

**A Timeline of our Work is as follows**
11/12/2021 (Taylor)
Worked up searching for big datasets on the project
Cleaning up the data and looking for attributes that would be most beneficial for a general price prediction:
PE
PB Div
PEG
Research Machine Learning Methods that could be used to forecast the data
Potential Linear Regression
Start the initial creation of a dashboard using Dash.Py
Began the Jupyter notebook for cleaning data

Date 11/14/2021 (Taylor)
Finalized the dataset to be used
Added the Github repository
Note: (The data on local system still needs to be cleaned. The Jupyter notebook will be updated to reflect this afterwards)
Started the Jupyter Notebook
Note: The Jupyter notebook has the base infrastructure and notes needed to begin the project
Dashboard
Created a base outline using Dash.Py for data visualization
Data visualization can also be implemented in the Jupyter Notebook itself 
If time permitted, a base visualization could be used with the outline created in Dash.Py

11/19/2021 (Franz)
Finalized collection of data with usage of stock market dataset and yahoo finance data
Finished python script to pull financial data for our nasdaq traded etfs and stocks directly from yahoo finance using the yahoo finance package https://pypi.org/project/yfinance/. Code for it is in the jupyter notebook ‘yFinanceRetrieval’
Pulled data and published and pushed entire dataset to GitHub
Updated ‘Main’ notebook and loaded in the dataset of stocks and etfs in lists of panda dataframes 
Researched how to best split up our stock dataset
Split up stock dataset into three categories
I: Stocks 25 years and older
II: Stocks < 25 years but first traded before 2008
III: Stocks traded after 2009 and before 2018
We omitted stocks that were first traded in 2018 or later from the dataset as we need solidly sized trading history to train and test on

In Progress (Franz)
Solving the problem of special character filename changes when reading in csvs with panda
Research about best split of etfs, if even a split is applicable
Apply first ML models to data and get an idea of general trend and discoveries of significant variables

11/20/2021 (Taylor)
Starting adding small base prototypes to a linear regression model
Ran small algorithms to determine normalization within the stock market data if used on a large dataset
Researched splitting the algorithms in a variety of sectors, instead of as a single line

11/29/2021 (Taylor)
Starting to organize the ETF folder of all the stocks into a single .csv
Starting to organize the stock folder of all stocks into a single .csv
Began the SparkContext to look through the data, applying ML methods to it
Started the dash.py to incorporate charts, but need the following to actually implement it:
Data of every single stock
Data of every single etf

Note: The dataset that we are using currently contains data that is modeled by ‘open’ ‘high’ ‘low’ ‘close’. These should be the models that are primarily being used, so they should be the variables that are considered when we are modeling. To do this, I figured out we can take the difference between the open and close, high and low, and this can be modeled as the change over time between each stock price. 


12/02/2021 (Taylor)
Met with Professor Mahdi regarding updating Projects
Created a Base Prototype on a smaller sample of stocks to determine the scalability of the project
Determined that linear regression and clustering would be the best format for the data analysis 
Started obtaining data on time series modeling and forecasting to apply to the larger dataset

12/02/2021 (Franz & Taylor)
Started the base notebook for Linear Regression, LSTM, and CNN
Ran some of the smaller simulations on these models
(Franz) started making a small visualization in Maya that would show this

12/07/2021 (Taylor)
Began to select stocks randomly from a set of given stocks
Stock representation of S&P 500 represents a “portfolio” where volatility can be analyzed by selecting 1% of the given stocks. 
It is noted that 1% is selected, since the stocks analyzed are from a larger time frame
Started the time series analysis on a set of the given stocks

12/09/2021 (Taylor)
(Ran into some difficulties here - some of the components aren’t loading correctly when using dash_bootstrap_components)
May need to load the graphs differently, or show statically on Jupyter notebooks
Created a Python virtual environment in case the components aren’t working as a back up

12/10/2021 (Taylor & Franz)
Started adding components of PCA analysis to stocks
Researched how to do KNN on stock sectors to group and bin them in their corresponding categories
Added more functionality graphs to the Jupyter notebooks to display the values of stocks, etc. 
Both of us are working on adding our final touches and optimizing this code this week

12/17/2021 (Taylor & Franz)
Finalized the LSTM, Linear Regression, and CNN on the actual notebooks, and tuned them on larger datasets
Finalized the chart in Maya as a last data visualization
Finalized the write ups 
