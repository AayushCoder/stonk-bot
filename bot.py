import argparse

parser = argparse.ArgumentParser(description="Trade some stonks with your Robinhood account (no account information is stored)")
parser.add_argument("--user", "-u", type=str, help="Robinhood account username.")
parser.add_argument("--password", "-p", type=str, help="Robinhood account password.")

args = parser.parse_args()
