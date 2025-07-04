from datetime import datetime, timedelta

def today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")

def add_days(start_date: str, days: int) -> str:
    dt = datetime.strptime(start_date, "%Y-%m-%d")
    return (dt + timedelta(days=days)).strftime("%Y-%m-%d")
