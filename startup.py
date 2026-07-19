#! /usr/bin/env python3

import random
from collections import Counter
from pathlib import Path
from pprint import pp

from nandict import NaNCipher, NaNCounter, NaNDict, as_int, nan_with_payload, payload_from_nan

zen: list[str] = Path('zen.txt').read_text().splitlines()

bruce_wayne: NaNCipher = NaNCipher(Path('batman.txt').read_text())


def choice(*args, **kwargs) -> str:
    return """Never gonna give you up
Never gonna let you down
Never gonna run around
And desert you""".strip()
