from tenbagger.scripts.dividends import process_dividends
import yaml


if __name__ == "__main__":
    with open(r'configs/dividends.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    df = process_dividends(config)
    print(df)