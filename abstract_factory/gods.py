from typing import Protocol

# Jesus
class JesusStatue(Protocol):
    def turn_water_to_wine(self) -> str:
        pass

class WoodenJesusStatue:
    def turn_water_to_wine(self) -> str:
        return 'Wooden Jesus can turn your water to wine!'
    
class StoneJesusStatue:
    def turn_water_to_wine(self) -> str:
        return 'Stone Jesus can turn your water to rum!'

class MetalJesusStatue:
    def turn_water_to_wine(self) -> str:
        return 'Metal Jesus can turn your water to absinth!'

# Buddha
class BuddhaStatue(Protocol):
    def grant_skill(self) -> str:
        pass

class WoodenBuddhaStatue:
    def grant_skill(self) -> str:
        return 'Wooden Buddha can make you walk on water!'
    
class StoneBuddhaStatue:
    def grant_skill(self) -> str:
        return 'Stone Buddha can make you levitate!'

class MetalBuddhaStatue:
    def grant_skill(self) -> str:
        return 'Metal Buddha can make you invisible!'
    
#Vishnu
class VishnuStatue(Protocol):
    def protect(self) -> str:
        pass

class WoodenVishnuStatue:
    def protect(self) -> str:
        return 'Wooden Vishnu can protect you!'
    
class StoneVishnuStatue:
    def protect(self) -> str:
        return 'Stone Vishnu can protect your home and family!'

class MetalVishnuStatue:
    def protect(self) -> str:
        return 'Metal Vishnu can protect everyone you love!'
    