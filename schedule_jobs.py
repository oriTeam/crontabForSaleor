import schedule
import time
from selenium_func.signup import signup
from selenium_func import buy
from selenium_func import fulfill

def signup_schedule():
    print("Signup working...")
    signup()

def buy_schedule():
    print("Buy working...")
    buy()

def fulfill_schedule():
    print("Fulfill working...")
    fulfill()


schedule.every(12).hours.do(signup_schedule)
schedule.every(2).minutes.do(buy_schedule)
schedule.every().day.at("21:30").do(fulfill_schedule)
# schedule.every(5).minutes.do(signup_schedule())
# schedule.every(3).minutes.do(signup_schedule())
# schedule.every(2).minutes.do(signup_schedule())

# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)