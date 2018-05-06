#!/usr/bin/env python

from datetime import datetime

# https://www.forbes.com/sites/robertberger/2017/12/17/the-new-2018-federal-income-tax-brackets-rates
_TAX_BRACKET = {
    "2018": {
              19050 : 0.1,
              77400 : 0.12,
             165000 : 0.22,
             315000 : 0.24,
             400000 : 0.32,
             600000 : 0.35,
        1000000000L : 0.37   # 1 billion as ceiling limit :)
    }
}

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

class GrossIncome():
    def __init__(self,
                 gross_income,
                 increase_rate=None):
        self.gross_income = gross_income
        self.increase_rate = increase_rate
        return

    def getGrossIncome(self, years=10):
        gross_incomes = []
        gross_income = self.gross_income
        y = 0
        while y < years:
            gross_incomes.append(gross_income)
            y += 1
            gross_income *= (1.0 + self.increase_rate)
        return gross_incomes

class IncomeTax():
    def __init__(self,
                 gross_income,
                 mortgage,
                 property_tax,
                 years):

        self.gross_income = gross_income
        self.mortgage = mortgage
        self.property_tax = property_tax
        self.this_year = datetime.now().strftime('%Y')
        self.bracket = _TAX_BRACKET[self.this_year]
        self.years = years
        return

    def getTaxableIncome(self): # internal
        """
        @return: taxables: list of taxable over the years
        """
        # Deduction is mortgage interest plus property_tax
        interests = self.mortgage.getAnnualInterest(years=self.years)
        property_taxes = self.property_tax.getAnnualPropertyTax(years=self.years)
        deductions = []
        for i in xrange(self.years):
            d = interests[i] + property_taxes[i]
            deductions.append(d)

        # calculate gross income over the years
        gross_incomes = self.gross_income.getGrossIncome(years=self.years)

        taxables = []
        for i in xrange(self.years):
            t = gross_incomes[i] - deductions[i]
            if t < 0:
                t = 0
            taxables.append(t)
        return taxables

    def calculateOneYearTax(self, income):
        floor = 0
        tax = 0
        for (ceiling, rate) in sorted(self.bracket.items()):
            if income < ceiling:
                tax += (income - floor) * rate
                break
            tax += (ceiling - floor) * rate
            floor = ceiling
        return tax

    def calculateTaxes(self, taxables):       # internal
        taxes = []
        for income in taxables:
            t = self.calculateOneYearTax(income)
            taxes.append(t)
        return taxes

    def getTaxes(self):
        """ return a list, each item for a year
        """
        taxables = self.getTaxableIncome()
        return self.calculateTaxes(taxables)

def main():
    m = Mortgage(total_amount=370000, interest=15000, adr=0.1)
    p = PropertyTax(property_tax=8800, increase_rate=0.012)
    g = GrossIncome(gross_income=200000, increase_rate=0.02)

    years = 10
    tax = IncomeTax(g, m, p, years)
    print tax.getTaxes()
    return

if __name__=="__main__":
    main()
