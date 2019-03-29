# pythonchat
# Greg McLeod
# !/usr/bin/env python
"""controller class
"""
__author__ = "Greg McLeod"
__version__ = "1.0"
__maintainer__ = "Greg McLeod"
__email__ = "mcle0463@algonquincollge.com"
__status__ = "Dev"

import sys
import csv
import asyncio
import websockets
import json


class Controller:
    def __init__(self):
        # def __init__(self, data_obj):
        self.state_data = {'command': '',
                           'data': '', 'selection': 0}

    def get_rows(self):
        # reload data
        # print("Button1\n")
        self.state_data['command'] = 'get_rows'
        asyncio.get_event_loop().run_until_complete(self.process(self.state_data))
        # self.data.get_rows()

    def print_data(self):
        # update text area
        self.state_data['command'] = 'print_data'
        return asyncio.get_event_loop().run_until_complete(self.process(self.state_data))

    def create_record(self, record_data):
        # create a new record
        self.state_data['command'] = 'create_record'
        self.state_data['data'] = record_data
        asyncio.get_event_loop().run_until_complete(
            self.process(self.state_data))

    def select_record(self, record_selection):
        # select a new record
        self.state_data['command'] = 'select_record'
        self.state_data['selection'] = record_selection
        asyncio.get_event_loop().run_until_complete(self.process(self.state_data))

    def display_one_record(self):
        # show only one record
        self.state_data['command'] = 'display_one_record'
        return asyncio.get_event_loop().run_until_complete(self.process(self.state_data))

    def edit_record(self, record_data):
        # edit a record
        self.state_data['command'] = 'edit_record'
        self.state_data['data'] = record_data
        asyncio.get_event_loop().run_until_complete(self.process(self.state_data))

    def delete_record(self):
        # delete a record
        self.state_data['command'] = 'delete_record'
        asyncio.get_event_loop().run_until_complete(self.process(self.state_data))

    def quit_pythonchat(self):
        # quit - can remove this function
        print("Exiting...\n")

    async def process(self, command):
        # use json to send
        # Greg McLeod
        y = json.dumps(command)
        async with websockets.connect(
                'ws://localhost:8765') as websocket:
            print("Sending:" + y + "from client")
            await websocket.send(y)
            incomming_data = await websocket.recv()
            return incomming_data
