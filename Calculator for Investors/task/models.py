from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Float, String
from sqlalchemy.orm import validates
from base import Base


class Company(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String, default=None)
    sector = Column(String, default=None)

class Financial(Base):
    __tablename__ = 'financial'

    ticker = Column(String, primary_key=True)
    ebitda = Column(Float, default=None)
    sales = Column(Float, default=None)
    net_profit = Column(Float, default=None)
    market_price = Column(Float, default=None)
    net_debt = Column(Float, default=None)
    assets = Column(Float, default=None)
    equity = Column(Float, default=None)
    cash_equivalents = Column(Float, default=None)
    liabilities = Column(Float, default=None)

    def get_indicators(self):
        if self is None:
            return []
        indicators = [('P/E', Financial._indicator(self.market_price, self.net_profit)),
                      ('P/S', Financial._indicator(self.market_price, self.sales)),
                      ('P/B', Financial._indicator(self.market_price, self.assets)),
                      ('ND/EBITDA', Financial._indicator(self.net_debt, self.ebitda)),
                      ('ROE', Financial._indicator(self.net_profit, self.equity)),
                      ('ROA', Financial._indicator(self.net_profit, self.assets)),
                      ('L/A', Financial._indicator(self.liabilities, self.assets))]
        return indicators

    @staticmethod
    def _indicator(num, den):
        if (num is None
                or den is None
                or den == 0):
            return None
        else:
            return round(num / den, 2)


    @validates('ebitda', 'sales', 'net_profit', 'market_price',
               'net_debt', 'assets', 'equity', 'cash_equivalents',
               'liabilities')
    def validate_floats(self, key, value):
        try:
            return float(value) if value != '' else None
        except ValueError:
            return None