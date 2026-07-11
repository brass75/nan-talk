#! /usr/bin/env python3

from collections import Counter
from pathlib import Path
from pprint import pp
from random import choice

from nandict import NaNCipher, NaNCounter, NaNDict, as_int, nan_with_payload, payload_from_nan

zen: list[str] = Path('zen.txt').read_text().splitlines()
