import pandas as pd
import numpy as np


def clean_insider(df, col):

    df[col] = df[col].str.replace('+', '')
    df[col] = df[col].str.replace(',', '')
    df[col] = df[col].str.replace('$', '')

    df[col] = df[col].astype('float')

    return df


def overview():

    pd.set_option("expand_frame_repr", False)

    df = pd.read_html('http://openinsider.com/')[10]
    clean_cols = ['Qty', 'Price', 'Value']

    for col in clean_cols:
        df = clean_insider(df, col)

    pass


if __name__ == '__main__':
    overview()
    x = 2