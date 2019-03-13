# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import List, Tuple
from dataclasses import dataclass, asdict

from dataclasses_fromdict import from_dict

@dataclass
class Point:
    x: int
    y: int


@dataclass
class PointList:
     items: List[Point]


@dataclass
class Line:
     items: Tuple[Point, Point]


@dataclass
class Points:
     items: Tuple[Point, ...]


def test_simple():
    p = Point(10, 20)
    d = asdict(p)
    assert d == {'x': 10, 'y': 20}
    assert from_dict(d, Point) == p

def test_generic_list():
    pl = PointList([Point(0, 0), Point(10, 4)])
    d = asdict(pl)
    assert d == {'items': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}
    assert from_dict(d, PointList) == pl

def test_generic_tuple():
    l = Line((Point(0, 0), Point(10, 4)))
    d = asdict(l)
    assert d == {'items':({'x': 0, 'y': 0}, {'x': 10, 'y': 4})}
    assert from_dict(d, Line) == l

def test_generic_vartuple():
    ps = Points((Point(0, 0), Point(10, 4), Point(20, 8)))
    d = asdict(ps)
    assert d == {'items':({'x': 0, 'y': 0}, {'x': 10, 'y': 4}, {'x': 20, 'y': 8})}
    assert from_dict(d, Points) == ps
