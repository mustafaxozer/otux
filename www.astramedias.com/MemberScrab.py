import csv
import configparser
import traceback

from telethon.sync import TelegramClient
from telethon import types, utils, errors
from telethon.tl.functions import channels
from StartAdd import read_csv, write_csv


try:
    config = configparser.ConfigParser()
    config.read("config.ini")

    channel = config['Telegram']['from_channel']
    phone = utils.parse_phone(config['Telegram']['main_phone'])
    api = read_csv('api.csv')[0]


    client = TelegramClient(f"sessions/{phone}", *api)
    client.start(phone)


    rows = [
        ['ID', 'Name', 'Username', 'Phone']
    ]

    print("Member Scrabing Start Please Wait...")

    for participant in client.iter_participants(channel, aggressive=True):
        print(f"Member Scrab Live Counting {len(rows)}", end='\r')
        rows.append([
            participant.id,
            utils.get_display_name(participant),
            participant.username,
            participant.phone
        ])


    print()
    write_csv('MembersFile.csv', rows)
    print("All Member Scrabing Done Please Start The StartAdd File From This Folder For Member Adding")


finally:
    input()
