from concurrent.futures import ThreadPoolExecutor
from scraper import scrape_articles
import json

def run_test(browser_config):
    print(f"Running on {browser_config['sessionName']}")
    articles = scrape_articles(browser_config)
    return browser_config["sessionName"], articles


def run_parallel_tests():

    browsers = [
        {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "os": "Windows",
            "osVersion": "11",
            "sessionName": "Chrome Windows Test"
        },
        {
            "browserName": "Firefox",
            "browserVersion": "latest",
            "os": "Windows",
            "osVersion": "11",
            "sessionName": "Firefox Windows Test"
        },
        {
            "browserName": "Edge",
            "browserVersion": "latest",
            "os": "Windows",
            "osVersion": "11",
            "sessionName": "Edge Windows Test"
        },
        {
            "browserName": "Chrome",
            "browserVersion": "latest",
            "os": "OS X",
            "osVersion": "Monterey",
            "sessionName": "Chrome Mac Test"
        },
        {
            "browserName": "Safari",
            "browserVersion": "latest",
            "os": "OS X",
            "osVersion": "Monterey",
            "sessionName": "Safari Mac Test"
        }
    ]

    results_dict = {}

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(run_test, browsers))

    for session_name, articles in results:
        results_dict[session_name] = articles

    # Save to JSON file
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(results_dict, f, indent=4, ensure_ascii=False)

    print("\nSaved results to output.json")

    return results_dict