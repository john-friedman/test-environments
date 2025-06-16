# test-datamule.py
from datamule import Portfolio
portfolio = Portfolio('apple')
portfolio.download_submissions(ticker='AAPL', submission_type='10-K')
