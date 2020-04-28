# !/usr/bin/python
# coding=utf-8
import re

def decompress(compressed_content):
    from compress import symbols

    # your code inside this "decompress" function
    for symbol in symbols:
        compressed_content = compressed_content.replace(symbols[symbol],symbol)
    return compressed_content
    