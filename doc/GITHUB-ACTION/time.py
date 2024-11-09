import datetime

def display_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

display_time()
