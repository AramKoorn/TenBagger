import pandas as pd


class Bonds:
    def __init__(self, market):
        self.market = market
        self.symbol = self._get_symbol(self.market)

    @staticmethod
    def _get_symbol(market):

        allowed = ["germany", "us"]

        if market not in allowed:
            raise ValueError(
                f"You selected {market} but only one of {allowed} is allowed"
            )

        if market == "germany":
            symbol = "tmbmkde-10y"
        elif market == "us":
            symbol = "TMUBMUSD10Y"
        return symbol

    def get_info(self):
        df = pd.read_html(
            f"https://www.marketwatch.com/investing/bond/{self.symbol}?countrycode=bx&mod=over_search"
        )

        info = {}
        info["current_10_year"] = df[1]["Previous Close"].item()
        info["all_bonds"] = df[5]
        info["worldwide"] = df[-1]
        return info


if __name__ == "__main__":

    b = Bonds("germany")
    info = b.get_info()

    b = Bonds("us")
    info = b.get_info()
    info.keys()
