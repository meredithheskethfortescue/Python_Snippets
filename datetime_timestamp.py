"""Generate a timestamp to tag filenames"""
from datetime import datetime

timestamp = datetime.today().strftime('%Y-%m-%d_%H-%M')
