import os, time, requests


hostname = 'x.x.x.x'

text_numbers = ['+15555555555']

def send_text(cell_number):
    
    end_point = 'https://your-api-endpoint'
    data = {
        "To": cell_number,
        "From": "+15555555555",
        "Response": "5555555555",
        "Body": "OH NO!! Mike is in the server room!!"
    }
    r = requests.post(end_point, json=data)

while True:
    r = os.system('ping -c 1 ' + hostname + ' > /dev/null')
    if r == 0:
        print("button pressed!")
        for number in text_numbers:
            send_text(number)
        time.sleep(20)
    
    time.sleep(1)


