import os
from datetime import datetime
import time
from notification import send_notification, params


def check_condition():
    current_time = datetime.now().time()
    current_date = datetime.now().strftime('%m.%d.%Y')
    if current_time.hour >= 18:
        
        folder_path = 'Saves'
        file_name = f'{current_date}.txt'
        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):
            pass
        else:
            send_notification(params)


def main():
    while True:
        check_condition()
        time.sleep(3600) #its run on log on of a user in task scheduler


main()