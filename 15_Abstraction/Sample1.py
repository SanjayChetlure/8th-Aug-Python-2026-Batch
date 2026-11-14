from abc import ABC, abstractmethod

class Account(ABC):      #Incomplete/abstract class

    @abstractmethod
    def CD(self):          #Incomplete/abstract method
        pass

    @abstractmethod         #Incomplete/abstract method
    def CW(self):
        pass

    @abstractmethod         #Incomplete/abstract method
    def BI(self):
        pass

#Sub class
class SavingAcc(Account):

    def CD(self):
        print("Running Cash Deposit code")

    def CW(self):
        print("Running Cash Withdrawal code")

    def BI(self):
        print("Running Balance Inquiry code")



s=SavingAcc()
s.CD()
s.CW()
s.BI()