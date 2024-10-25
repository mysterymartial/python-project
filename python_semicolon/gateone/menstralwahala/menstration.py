from datetime import datetime, timedelta

start_day = input("Enter the starting date of your menstrual period (DD/MM/YYYY): ")
period_of_flow = int(input("Enter the number of days your period lasts: "))
menstrual_cycle_days = int(input("Enter the number of days in your menstrual cycle: "))


user_date = datetime.strptime(start_day, "%d/%m/%Y")


end_of_period = user_date + timedelta(days=period_of_flow - 1)


OVULATION_CONST = 14
ovulation_day = user_date + timedelta(days=menstrual_cycle_days - OVULATION_CONST + 4)


start_of_unsafe_period = ovulation_day - timedelta(days=6)
end_of_unsafe_period = ovulation_day + timedelta(days=2)


next_period_date = user_date + timedelta(days=menstrual_cycle_days)


safe_period_before_unsafe = (user_date, start_of_unsafe_period - timedelta(days=1))
safe_period_after_unsafe = (end_of_unsafe_period + timedelta(days=1), next_period_date - timedelta(days=1))


print(f"Your period lasts from {user_date.strftime('%d/%m/%Y')} to {end_of_period.strftime('%d/%m/%Y')}.")
print(f"Your ovulation day is {ovulation_day.strftime('%d/%m/%Y')}.")
print(f"Your unsafe period starts from {start_of_unsafe_period.strftime('%d/%m/%Y')} and ends at {end_of_unsafe_period.strftime('%d/%m/%Y')}.")
print(f"Safe days before the unsafe period are from {safe_period_before_unsafe[0].strftime('%d/%m/%Y')} to {safe_period_before_unsafe[1].strftime('%d/%m/%Y')}.")
print(f"Safe days after the unsafe period are from {safe_period_after_unsafe[0].strftime('%d/%m/%Y')} to {safe_period_after_unsafe[1].strftime('%d/%m/%Y')}.")
print(f"Your next period starts on {next_period_date.strftime('%d/%m/%Y')}.")



