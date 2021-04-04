from prioritizator import Matcher
from random import randint

DATA_PATH = "data/task_list.csv"
PAGES = 4
TASKS_PER_PAGE = 25

white_id = int(input(f"White: Page: {randint(1,PAGES)}, Issue: {randint(1,TASKS_PER_PAGE)}\nID?> "))
black_id = int(input(f"Black: Page: {randint(1,PAGES)}, Issue: {randint(1,TASKS_PER_PAGE)}\nID?> "))
outcome = float(input("White wins = 1, Draw = 0.5, Black wins = 0\nOutcome?> "))
matcher = Matcher(DATA_PATH)
matcher.match(white_id=white_id, black_id=black_id, outcome=outcome)
