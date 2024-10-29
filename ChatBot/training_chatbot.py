import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import SGD
from keras.optimizers.schedules import ExponentialDecay
import random

