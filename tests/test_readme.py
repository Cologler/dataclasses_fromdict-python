# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def test_1():
    from dataclasses import dataclass, asdict
    from dataclasses_fromdict import from_dict

    @dataclass
    class Point:
        x: int
        y: int

    assert from_dict(asdict(Point(10, 20)), Point) == Point(10, 20)
