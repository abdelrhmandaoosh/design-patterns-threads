from typing import Any


class washing:
    def wash(self):
        print("washing")
class rinsing:
    def rins(self):
        print("rinsing")
class spinning:
    def spin(self) :
        print("spinning")

class WashingMachine:
    def __init__(self) :
        self.washing = washing()
        self.rinsing= rinsing()
        self.spinning = spinning()
if __name__ == "__main__" :
    WashingMachine=WashingMachine()
    WashingMachine.startWashingMachine()