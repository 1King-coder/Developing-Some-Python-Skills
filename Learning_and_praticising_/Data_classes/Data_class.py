import inspect
from dataclasses import dataclass, field
from pprint import pprint


@dataclass(frozen=True, order=True)
class SomeCoolStuff:
    id: int = field()
    text: str = field(default="")
    replies_to_it: list[int] = field(default_factory=list,
                                     compare=False,
                                     hash=False,
                                     repr=False)


def main():
    cool_stuff = SomeCoolStuff(1101, "Crazy and cool stuff", [1, 2, 3])
    print(cool_stuff)


if __name__ == "__main__":
    print()
    main()
    print()
