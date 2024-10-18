import random
from datetime import datetime, timedelta


def generate_random_date():
    start_date = datetime.now()
    random_days = random.randint(1, 30)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%d.%m.%Y")
