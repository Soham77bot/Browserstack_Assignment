# BrowserStack Automation Assignment

## Overview
This project automates scraping articles from a target website across multiple browsers using **BrowserStack Cloud**.  
It includes features such as:

- Running parallel tests on multiple browsers (Chrome, Firefox, Edge, Safari) on Windows and Mac.
- Scraping article titles and content.
- Translating Spanish text to English using `googletrans`.
- Identifying repeated words in translated titles (words appearing ≥ 2 times).
- Saving results in a structured JSON file (`output.json`).

---

## File Structure
BrowserStack-Automation/
│
├── main.py # Main script that runs tests, translation, repeated-word analysis
├── browserstack_runner.py # Parallel BrowserStack test runner
├── scraper.py # Web scraping logic
├── requirements.txt # Python dependencies
├── output.json # Sample output
├── README.md # Project information
└── .gitignore # Files to ignore in Git

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/BrowserStack-Automation.git
cd BrowserStack-Automation

2. Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

USAGE:
1. Set your Browserstack credentials in environment variables
export BROWSERSTACK_USERNAME=<your_username>
export BROWSERSTACK_ACCESS_KEY=<your_access_key>

2. Run the main script
python main.py

3. Results will be printed in the console and saved to output.json.

