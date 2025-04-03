import streamlit as st
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler

st.title("Northwest India Weather Prediction")
lookback = st.slider("Lookback days", 10, 50, 30)
# [Add model training and prediction code here, show plots with st.line_chart]
