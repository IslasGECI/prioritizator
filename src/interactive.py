from prioritizator import Matcher
from random import randint

DATA_PATH = "data/task_list.csv"
PAGES = 5
TASKS_PER_PAGE = 25
WHITE_WINS = 1
DRAW = 0.5
WHITE_LOSES = 0

white_id = input(f"White: Page: {randint(1,PAGES)}, Issue: {randint(1,TASKS_PER_PAGE)}\nID?> ")
black_id = input(f"Black: Page: {randint(1,PAGES)}, Issue: {randint(1,TASKS_PER_PAGE)}\nID?> ")
outcome = input(f"White wins = 1, Draw = 0.5, Black wins = 0\nOutcome?> ")
matcher = Matcher(DATA_PATH)
matcher.match(white_id=white_id, black_id=black_id, outcome=WHITE_LOSES)
