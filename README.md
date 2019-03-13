# dataclasses_fromdict

## Usage

``` py
from dataclasses import dataclass, asdict
from dataclasses_fromdict import from_dict

@dataclass
class Point:
    x: int
    y: int

assert from_dict(asdict(Point(10, 20)), Point) == Point(10, 20)
```

## Support

* generic list
* generic tuple
* generic var tuple

## Other Libraries

* [dacite](https://github.com/konradhalas/dacite) - nice job, I should search on github before start this project 😂
