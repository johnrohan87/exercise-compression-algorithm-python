# !/usr/bin/python
# coding=utf-8
import re

symbols = {
    "implementation": "🤯",
    "practicality": '🤩',
    "better": '😅',
    "than": '😘',
    "Although": "🥺"
}

def compress(content):

    compressed_content = ''

    # your code inside this "compress" function
    for symbol in symbols:
        content = content.replace(symbol,symbols[symbol])
    return content
    