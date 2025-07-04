import sys
import logging
from pathlib import Path

# Ensure logs directory exists
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Configure custom logger
logger = logging.getLogger("study_planner")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(LOG_DIR / "errors.log")
fh.setFormatter(logging.Formatter(
    "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

logger.addHandler(fh)
logger.addHandler(sh)

def error_message_detail(exc: Exception, error_detail=sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    msg = f"Error in [{filename}] at line {line_no}: {str(exc)}"
    logger.error(msg, exc_info=True)
    return msg
