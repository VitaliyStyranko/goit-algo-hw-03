from datetime import datetime


def get_days_from_today(date):

    current_date = datetime.today()

    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        difference_date = (input_date - current_date).days
        return difference_date

    except ValueError:
        print("Invalid date")


days_str = '2024-01-02'
diff_days = get_days_from_today(days_str)
print(f"The difference betweem current and input days is: {diff_days}")