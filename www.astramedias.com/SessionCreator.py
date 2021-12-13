from telethon.sync import TelegramClient
from telethon import utils
from StartAdd import read_csv


done = False
try:
    phone_list = sum(read_csv('phone.csv'), start=[])
    api = read_csv('api.csv')[0]


    for unparsed_phone in phone_list:
        phone = utils.parse_phone(unparsed_phone)
        
        print(f"Session Login {phone}")
        client = TelegramClient(f"sessions/{phone}", *api)
        client.start(phone)

        client.disconnect()
        print()

    done = True


finally:
    input("All Number Login Done Now Please Start The MemberScrab File For Member Scrabing" if done else "This Number is Banned Please Delete This Number")
