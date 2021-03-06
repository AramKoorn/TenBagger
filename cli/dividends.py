from tenbagger.scripts.dividends import run
import yaml


if __name__ == "__main__":
    with open(r'configs/dividends.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    df = run(config)
    print(df)