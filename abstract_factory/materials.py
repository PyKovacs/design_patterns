from __future__ import annotations
import gods


class WoodenStatuesFactory:
    def create_statue_jesus(self) -> gods.JesusStatue:
        return gods.WoodenJesusStatue()

    def create_statue_buddha(self) -> gods.BuddhaStatue:
        return gods.WoodenBuddhaStatue()

    def create_statue_vishnu(self) -> gods.VishnuStatue:
        return gods.WoodenVishnuStatue()
    
class StoneStatuesFactory:
    def create_statue_jesus(self) -> gods.JesusStatue:
        return gods.StoneJesusStatue()

    def create_statue_buddha(self) -> gods.BuddhaStatue:
        return gods.StoneBuddhaStatue()

    def create_statue_vishnu(self) -> gods.VishnuStatue:
        return gods.StoneVishnuStatue()
    
class MetalStatuesFactory:
    def create_statue_jesus(self) -> gods.JesusStatue:
        return gods.MetalJesusStatue()

    def create_statue_buddha(self) -> gods.BuddhaStatue:
        return gods.MetalBuddhaStatue()

    def create_statue_vishnu(self) -> gods.VishnuStatue:
        return gods.MetalVishnuStatue()