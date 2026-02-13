# ==========================
# TELEGRAM CONFIG
# ==========================

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"


# ==========================
# OPENAI CONFIG (Behavior LLM)
# ==========================

OPENAI_KEY = "YOUR_OPENAI_API_KEY"
LLM_MODEL = "gpt-4o-mini"
LLM_TEMPERATURE = 0.2


# ==========================
# MARKET ENGINE SETTINGS
# ==========================

DATA_FILE = "nifty_daily.csv"
DECISION_TIME = "15:15"  # IST


# ==========================
# BEHAVIOR SETTINGS
# ==========================

PROFIT_PHASE_THRESHOLD = 50000     # 20-day rolling PnL
MAX_ALLOWED_DEVIATIONS_WEEK = 2
EQUITY_HIGH_LOOKBACK = 30          # days


# ==========================
# LOG FILES
# ==========================

TRADE_LOG_FILE = "trade_log.csv"
BEHAVIOR_LOG_FILE = "behavior_log.csv"

