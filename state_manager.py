import pandas as pd

def is_profit_phase():
    df = pd.read_csv("trade_log.csv")
    rolling_pnl = df["pnl"].tail(20).sum()
    return rolling_pnl > 50000  # set your threshold
