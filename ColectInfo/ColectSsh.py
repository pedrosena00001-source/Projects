#!/usr/bin/env python3

import asyncio, asyncssh, json, sys

def LoadHost(PathForExecute):
    try:
        with open(PathForExecute, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print("Invalid JSON syntax:", e)
        sys.exit(1)
    except FileNotFoundError:
        sys.exit("File Not Found, 'Host Archive Is Needed'")

    CheckIsList = isinstance(data, list)
    if CheckIsList != True:
        sys.exit("The List Of Host Is Invalid")
    elif data == []:
        sys.exit("Empty List")

    RequestForHost = ['ip', 'username', 'KeyPath']
    for x in data:
        for i in RequestForHost:
            if i in x:
               print(i, x['ip'], x['username'])



def Main():
     LoadHost('host.json')
Main()
