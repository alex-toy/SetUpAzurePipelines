from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import os
import pandas as pd
# from sklearn.externals import joblib
import joblib
from sklearn.preprocessing import StandardScaler

try:
    clf = joblib.load("boston_housing_prediction.joblib")
    print(clf)
except:
    print( "Model not loaded")



