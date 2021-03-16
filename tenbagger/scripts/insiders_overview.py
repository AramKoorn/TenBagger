import pandas as pd
import numpy as np


def clean_insider(col):

    df[col] = df[col].str.replace('+', '')
    df[col] = df[col].str.replace(',', '')
    df[col] = df[col].str.replace('$', '')

    df[col] = df[col].astype('float')


def overview():

    x = 2
    pd.set_option("expand_frame_repr", False)

    df = pd.read_html('http://openinsider.com/')[10]
    clean_cols = ['Qty', 'Price', 'Value']

    pass


if __name__ == '__main__':
    overview()
    x = 2