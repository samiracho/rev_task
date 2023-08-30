from datetime import datetime, date

def check_date(today, input_date):
    """Check if the date is previous to today's date."""
    try:
      parsed_date = datetime.strptime(input_date, "%Y-%m-%d").date()
      return parsed_date < today
    except Exception as exception:
      return False

def days_to_birthday(today, birth_date):
    """Function that calculates the days left for next birthday."""
    diff1 = date(today.year, birth_date.month, birth_date.day)
    diff2 = date(today.year+1, birth_date.month, birth_date.day)
    if diff1 >= today:
        return (diff1-today).days
    return (diff2-today).days