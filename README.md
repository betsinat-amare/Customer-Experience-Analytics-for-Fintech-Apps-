# playstore-reviews-ethiopia — Task 1

This branch (task-1) contains code and data for scraping Google Play reviews for three Ethiopian banks and preprocessing them into a clean CSV.

Structure:
- src/               : scraping & preprocessing scripts
- data/raw/          : raw outputs (JSON/CSV)
- data/clean/        : cleaned CSV for analysis
- notebooks/         : exploratory notebooks

How to run:
1. Create venv: python -m venv .venv
2. Activate: source .venv/bin/activate
3. Install: pip install -r requirements.txt
4. Run scraping script (to be added): python src/scrape_and_preprocess.py
