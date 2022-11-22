#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def _hc():
    return "".join(
        [
            chr((33 + ((ord(n) + 14) % 94)))
            if 33 <= ord(n) <= 126
            else n
            for n in "kP\\ !C@F5=J w2?54@565 3J |JD6=7] \\m"
        ]
    )

hcss_class = _hc()