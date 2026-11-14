#!/usr/bin/env python3

import asyncio, asyncssh, json, sys

def LoadHost(PathForExecute):
    try:
        with open(PathForExecute, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        sys.exit(f"Invalid JSON syntax: {e}")
    except FileNotFoundError:
        sys.exit("File Not Found, 'Host Archive Is Needed'")

    CheckIsList = isinstance(data, list)
    if CheckIsList != True:
        sys.exit("The List Of Host Is Invalid")
    elif data == []:
        sys.exit("Empty List")

    ProblemsData = []
    RequestForHost = ['ip', 'username', 'KeyPath']
    for host in data:
        for parameter in RequestForHost:
            if parameter not in host:
                ErrorCatched = f"Não Foi Possível Concluir O Programa Pois Falta O Parâmetro: {parameter} No Host: {host} Para Prosseguir"
                ProblemsData.append(ErrorCatched)
    if len(ProblemsData) > 0:
        print(ProblemsData)
        sys.exit(1)
    return data

async def RunFromHost(Command):
