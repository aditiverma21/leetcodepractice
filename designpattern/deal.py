from abc import ABC, abstractmethod

class DealInformation:
    def transaction(self,deals):
        print("Complete deal Information")
        for deal in deals:
            print(f"Transaction Info for deal: {deal.id} on client {deal.clientname} at {deal.date}")
            print(f" Transaction amount {deal.transaction()}")


#If we make the Base class as abstract class then its secure from being instantiated
class Deal(ABC):
    def __init__(self,id,clientname,date):
        self.id = id
        self.clientname = clientname
        self.date = date

    @abstractmethod
    def transaction(self):
        pass


class Swapdeal(Deal):
    def __init__(self,id,clientname,date,swapamount):
        super().__init__(id,clientname,date)
        self.swapamount = swapamount

    def transaction(self):
        return self.swapamount + 3000

class Creditdeal(Deal):
    def __init__(self,id,clientname,date,prin_amount,period):
        super().__init__(id,clientname,date)
        self.prin_amount = prin_amount
        self.period = period

    def transaction(self):
        if self.period==1:
            return self.prin_amount + (self.prin_amount* 0.2)
        elif self.period==3:
            return  self.prin_amount + (self.prin_amount * 0.3)
        elif self.period ==5:
            return self.prin_amount + (self.prin_amount * 0.5)
        else:
            print(" The Time period is not valid for investment")

class RateSwap(Swapdeal):
    def __init__(self,id,clientname,date,swapamount,rate):
        super().__init__(id,clientname,date,swapamount)
        self.rate = rate

    def transaction(self):
        fixed = super().transaction()
        return fixed + self.rate
