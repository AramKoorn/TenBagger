import pandas as pd
import datetime
import yaml

def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))


# # Python program to print
# # colored text and background
# def print_format_table():
#     """
#     prints table of formatted text format options
#     """
#     for style in range(8):
#         for fg in range(10, 38):
#             s1 = ''
#             for bg in range(40, 48):
#                 format = ';'.join([str(style), str(fg), str(bg)])
#                 s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
#             print(s1)
#         print('\n')
#
#
# print_format_table()


def format_insiders(ticker):

    url = f'http://openinsider.com/search?q={ticker}'
    df = pd.read_html(url)[11]

    remove_col = ['X', '1d', '1w', '1m', '6m']
    df = df.drop(columns=remove_col)

    # df['Price'] = color_config['PriceColors']['green'] + df['Price'] + color_config['PriceColors']['green']
    # df['Trade Type'].unique()

    return df


if __name__ == "__main__":

    with open(r'configs/ColorCodes.yaml') as file:
        color_config = yaml.load(file, Loader=yaml.FullLoader)

    ticker = 'IBM'
    df = format_insiders(ticker)