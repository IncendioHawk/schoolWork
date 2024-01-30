import os
from dotenv import load_dotenv
load_dotenv()

PASSWORD = os.getenv("PASSWORD")

def reverse(string: str) -> str:
    return string[::-1]

def checkPassword(str: str):
    return str.lower() == PASSWORD

def lenStrs(arr: list[str]):
    length = 0
    for str in arr:
        length += len(str)
    return length


def inputOutput(inp:str, string:str, value:str):
    return value if inp.lower() == string else ''

def oGoat(string: str):
    return inputOutput(string, 'goat', 'o')

