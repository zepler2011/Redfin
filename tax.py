#!/usr/bin/env python

class Mortgage():
    def __init__(self,
                 total_amount=None,
                 interest=None,
                 adr=None):
        self.total_amount = total_amount  # not used now
        self.interest = interest          # interest amount
        self.decrease_rate = adr          # a percentage that decrease
        return

    def getAnnualInterest(self, years=10):
        interests = []
        annual_interest = self.interest
        y = 0
        while y < years:
            interests.append(annual_interest)
            y += 1
            annual_interest *= (1.0 - self.decrease_rate)
        return interests

class IncomeTax():
    def __init__(self,
                 mortgage=None,
                 gross_income=None,
                 property_tax=None,
                 mortgage_interest=None,
                 gross_income_annual_increase_rate=None,
                 property_tax_annual_increase_rate=None):
        pass
    def getTaxableIncome(self): # internal
        pass
    def getTaxRate(self):       # internal
        pass

    def getAnnualTax(self, years=10):
        """ return a list, each item for a year
        """
        pass

def main():
    m = Mortgage(total_amount=370000, interest=15000, adr=0.1)
    interests = m.getAnnualInterest(years=10)
    return

if __name__=="__main__":
    main()
