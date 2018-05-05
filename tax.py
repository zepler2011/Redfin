#!/usr/bin/env python

class PropertyTax():
    def __init__(self,
                 property_tax=None,
                 increase_rate=None):
        self.property_tax = property_tax
        self.increase_rate = increase_rate
        return

    def getAnnualPropertyTax(self, years=10):
        """ Get the property tax over the next 10 years
        """
        property_taxes = []
        property_tax = self.property_tax
        y = 0
        while y < years:
            property_taxes.append(property_tax)
            y += 1
            property_tax *= (1.0 + self.increase_rate)
        return property_taxes

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

    p = PropertyTax(property_tax=8800, increase_rate=0.012)
    property_taxes = p.getAnnualPropertyTax(years=10)
    return

if __name__=="__main__":
    main()
