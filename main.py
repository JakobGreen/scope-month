#!/usr/bin/env python2
"""
Parse arguments and start the webdriver
"""
import argparse
import json

from src.webdriver import ScopeMonthWebDriver

def parse_args():
    """ Parse the arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("--headless", help="Run the browser in the background", action="store_true")
    parser.add_argument("--config", help="Config file (defaults to local ./config.json)")
    parser.add_argument("--browser", help="Which browser should be used",
                        type=str, choices=["chrome", "firefox"], default="firefox")

    return parser.parse_args()

def main():
    """ Start the webdriver after parsing the args"""
    args = parse_args()
    config_file = args.config or "config.json"
    with open(config_file) as config_data:
        config = json.load(config_data)

    webdriver = ScopeMonthWebDriver(config, args.browser, args.headless)
    webdriver.run()

if __name__ == "__main__":
    main()

