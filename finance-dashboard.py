"""
finance-dashboard.py: A Big Data Visualization of the Stocks from previous years
"""

__author__ = "Taylor D. Gabatino"
__copyright__ = "Copyright 2021, UH Manoa"
__version__ = "1.0"
__maintainer__ = "Taylor D. Gabatino"
__email__ = "tgabatin@hawaii.edu"
__status__ = "Production"

# Import Statements ------------------------------------------
import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output, Statement
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# Ability to run the application locally
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
app.title = 'Big Data Stock Analytics'

##################################
# Reading in the files
##################################


