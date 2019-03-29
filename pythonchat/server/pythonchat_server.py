# pythonchat server
# Greg McLeod
# !/usr/bin/env python
"""server main
"""
__author__ = "Greg McLeod"
__version__ = "1.0"
__maintainer__ = "Greg McLeod"
__email__ = "mcle0463@algonquincollge.com"
__status__ = "Dev"


import asyncio
import json
import logging
import websockets
import data_object

# global data object will be manipulated by multiple clients in final version
data_obj = data_object.DataObject()


def get_rows():
    """reload data"""
    data_obj.get_rows()


def print_data():
    """update text area"""
    return data_obj.print_data()


def create_record(record_data):
    """create a new record"""
    data_obj.create_record(record_data)


def select_record(record_selection):
    """select a new record"""
    data_obj.select_record(record_selection)


def display_one_record():
    """show only one record"""
    return data_obj.display_record()


def edit_record(record_data):
    """edit a record"""
    data_obj.edit_record(record_data)


def delete_record():
    """delete a record"""
    data_obj.delete_record()


async def handle_requests(websocket, path):
    """the function is the WS client send handler and is called
        each time a client connects"""
    # Greg McLeod
    send_data = ""
    request = await websocket.recv()
    print(request)
    request = json.loads(request)
    print(request)
    print("recieved in server\ncommand:" +
          request['command'] + "\ndata:" + request['data'] + "\nselection:" + str(request['selection']))
    if(request['command'] == "delete_record"):
        delete_record()
        send_data = data_obj.print_data()
    elif(request['command'] == "edit_record"):
        edit_record(request['data'])
    elif(request['command'] == "display_one_record"):
        send_data = display_one_record()
    elif(request['command'] == "select_record"):
        select_record(request['selection'])
    elif(request['command'] == "create_record"):
        create_record(request['data'])
        send_data = data_obj.print_data()
    elif(request['command'] == "print_data"):
        send_data = data_obj.print_data()
    elif(request['command'] == "edit_record"):
        edit_record(request['data'])
        send_data = data_obj.print_data()

    print("sending:" + send_data + "from server\n")
    await websocket.send(send_data)

# server main
data_obj.get_rows()
start_server = websockets.serve(handle_requests, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
