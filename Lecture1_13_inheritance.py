class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


# class NandGate(BinaryGate):
#     def __init__(self, n):
#         BinaryGate.__init__(self, n)
#     def performGateLogic(self):
#         a = self.getPinA()
#         b = self.getPinB()
#         if a == 1 and b == 1:
#             return 0
#         else:
#             return 1
#
# class NorGate(BinaryGate):
#     def __init__(self, n):
#         BinaryGate.__init__(self, n)
#     def performGateLogic(self):
#         a = self.getPinA()
#         b = self.getPinB()
#         if a == 1 or b == 1:
#             return 0
#         else:
#             return 1
class NandGate(AndGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1
class NorGate(OrGate):
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

def main():
   # g1 = AndGate("G1")
   # g2 = AndGate("G2")
   # g3 = OrGate("G3")
   # g4 = NotGate("G4")
   # c1 = Connector(g1,g3)
   # c2 = Connector(g2,g3)
   # c3 = Connector(g3,g4)
   # print(g4.getOutput())

   # prove equality
    for i in range(2):
        if i == 0:
            gt1 = AndGate('Gate 1')
            gt2 = AndGate('Gate 2')
            gt3 = NorGate('Gate 3')
        elif i == 1:
            gt1 = NandGate('Gate 1')
            gt2 = NandGate('Gate 2')
            gt3 = AndGate('Gate 3')
        c1 = Connector(gt1, gt3)
        c2 = Connector(gt2, gt3)
        if i == 0:
            x1 = gt3.getOutput()
        elif i == 1:
            x2 = gt3.getOutput()
    if x1 != x2:
        print('Not Equal')
    else:
        print('Equal')


main()
