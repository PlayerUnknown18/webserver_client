import asyncio
import websockets
import json
import time
from datetime import datetime

FILE_NAME = input("please enter the name of the json file name<>.jsonc </>")
DUMMY_FILE_NAME = "dummy.jsonc"


def open_as_json(path):
    with open(path,"r") as fin:
        json_data = json.loads(fin.read())
        return json_data["packets"],json_data["time"],json_data["satellite"],json_data["type"]


def write_response_tofile(packet,response):
    with open("w", "response.txt") as fout:
        fout.write(packet + ":" + response)

]
def reset_json():
    dummy_file_data = ""
    with open("r", DUMMY_FILE_NAME) as fin:
        dummy_file_data = fin.read()

    with open("w", FILE_NAME) as fout:
        fout.write(dummy_file_data)


def send_packets():
    json_data,time_to_send,satellite,telecomand = open_as_json(FILE_NAME)
    while True:
        if datetime.now().strftime("%d-%m-%Y %H:%M:%S") == datetime.datetime.strptime(time_to_send, "%d-%m-%Y %H:%M:%S"):
            break
            
    for i in range(len(json_data)):
        print(json_data[i])
        print("Message sacssesfully sent!")

        for i in range(4):
            response = requests.post(f"http://localhost:5000/:4444/:{satellite}/sendPacket?endnode=",
                                    data = {"packet":json_data[i]})

            if len(response.text) == telecomand:
                print("got an ack")
                write_response_tofile(str(json_data[i]),response.text)
                break

            time.sleep(3)
    
    reset_json()
    
            


def main():
    while True:
        packets, , = open_as_json(FILE_NAME)
        if len(packets) >= 1:
            send_packets()


main()