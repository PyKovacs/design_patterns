from __future__ import annotations
from typing import Protocol

from materials import WoodenStatuesFactory, StoneStatuesFactory, MetalStatuesFactory
from gods import JesusStatue, BuddhaStatue, VishnuStatue


class ReligiousStatueFactory(Protocol):
    def create_statue_jesus(self) -> JesusStatue:
        raise NotImplementedError

    def create_statue_buddha(self) -> BuddhaStatue:
        raise NotImplementedError

    def create_statue_vishnu(self) -> VishnuStatue:
        raise NotImplementedError
    

def get_jesus_statue(factory: ReligiousStatueFactory) -> None:
    statue = factory.create_statue_jesus()
    print(statue.turn_water_to_wine())

def get_buddha_statue(factory: ReligiousStatueFactory) -> None:
    statue = factory.create_statue_buddha()
    print(statue.grant_skill())

def get_vishnu_statue(factory: ReligiousStatueFactory) -> None:
    statue = factory.create_statue_vishnu()
    print(statue.protect())

def main():
    # try different combinations
    get_buddha_statue(MetalStatuesFactory())
    get_vishnu_statue(WoodenStatuesFactory())
    get_jesus_statue(StoneStatuesFactory())

if __name__ == "__main__":
    main()