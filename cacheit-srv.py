#!/usr/bin/env python3
import sys
from aiohttp.web import main


entry_func = 'cacheit_srv.app:init'

if __name__ == '__main__':
    main(sys.argv[1:] + [entry_func])
