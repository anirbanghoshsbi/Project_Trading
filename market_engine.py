import pandas as pd
import numpy as np


# ===============================
# Indicator Calculations
# ===============================

def calculate_ema(series, period):
    return series.ewm(span=period, adjust=False).mean()


def calculate_macd(df):
    ema12 = calculate_ema(df["close"], 12)
    ema26 = calculate_ema(df["close"], 26)
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    histogram = macd - signal
    return macd, signal, histogram


def calculate_impulse(df):
    """
    Elder Impulse System:
    - EMA(13) slope
    - MACD histogram direction
    """
    df["ema13"] = calculate_ema(df["close"], 13)
    _, _, hist = calculate_macd(df)

    df["ema_slope"] = df["ema13"].diff()
    df["hist_slope"] = hist.diff()

    impulse = []

    for i in range(len(df)):
        if df["ema_slope"].iloc[i] > 0 and df["hist_slope"].iloc[i] > 0:
            impulse.append("green")
        elif df["ema_slope"].iloc[i] < 0 and df["hist_slope"].iloc[i] < 0:
            impulse.append("red")
        else:
            impulse.append("blue")

    df["impulse"] = impulse
    return df


# ===============================
# Your Nifty Rule Engine
# ===============================

def evaluate_market(file_path):
    """
    Reads CSV with columns:
    date, open, high, low, close
    """

    df = pd.read_csv(file_path)
    df = df.sort_values("date")

    # Calculate EMAs
    df["ema9"] = calculate_ema(df["close"], 9)
    df["ema20"] = calculate_ema(df["close"], 20)
    df["ema50"] = calculate_ema(df["close"], 50)

    # Calculate Impulse
    df = calculate_impulse(df)

    latest = df.iloc[-1]

    close = latest["close"]
    ema9 = latest["ema9"]
    ema20 = latest["ema20"]
    ema50 = latest["ema50"]
    impulse = latest["impulse"]

    # ===============================
    # Apply YOUR Shorting Rules
    # ===============================

    decision = {
        "close": round(close, 2),
        "ema9": round(ema9, 2),
        "ema20": round(ema20, 2),
        "ema50": round(ema50, 2),
        "impulse": impulse,
        "action": "DO NOTHING"
    }

    # Rule 1: Never short on green bar
    if impulse == "green" and close > ema9:
        decision["action"] = "LONG SETUP VALID"
    # Rule 2: Short only if impulse red AND close below EMA9
    elif impulse == "red" and close < ema9:
        decision["action"] = "SHORT SETUP VALID"

    # Else: no action
    else:
        decision["action"] = "NO ACTION"

    return decision
