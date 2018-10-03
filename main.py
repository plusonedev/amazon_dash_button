import os, time, requests
from dotenv import load_dotenv
load_dotenv()

hostname = os.getenv('HOSTNAME')
cooldown_timer = int(os.getenv('COOLDOWN'))
ping_interval = int(os.getenv('PINGINTERVAL'))
text_numbers = os.getenv('RECIPIENTS').split(',')

def send_text(cell_number):
    
    end_point = os.getenv('ENDPOINT')
    data = {
        "To": cell_number,
        "From": os.getenv('FROM'),
        "Response": os.getenv('RESPONSE'),
        "Body": os.getenv('BODY')
    }
    r = requests.post(end_point, json=data)

while True:
    r = os.system('ping -c 1 ' + hostname + ' > /dev/null')
    if r == 0:
        print("button pressed!")
        for number in text_numbers:
            send_text(number)
        time.sleep(cooldown_timer)
    
    time.sleep(1)


