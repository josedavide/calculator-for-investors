from sqlalchemy import func, desc
from models import Company, Financial


class Repository:
    def __init__(self, database):
        self.db = database

    def initialize_database(self):
        self.db.init_db()

    def load_data(self, companies, financials):
        with self.db.Session() as session:
            for company in companies:
                registry = Company(**company)
                session.add(registry)

            for financial in financials:
                registry = Financial(**financial)
                session.add(registry)
            session.commit()

    def add_new_company(self, company, financial):
        with self.db.Session() as session:
            registry = Company(**company)
            session.add(registry)

            registry = Financial(**financial)
            session.add(registry)
            session.commit()

    def find_companies_by_name(self, company_name):
        with self.db.Session() as session:
            query = session.query(Company)
            query_result = query.filter(Company.name.like('%' + company_name + '%')).all()

        return query_result

    def list_all_companies(self):
        with self.db.Session() as session:
            companies = session.query(Company).order_by(Company.ticker).all()

        return companies

    def find_financial_info_by_ticker(self, ticker):
        with self.db.Session() as session:
            query = session.query(Financial)
            query_result = query.filter(Financial.ticker == ticker).first()

        return query_result

    def update_financial_info(self, financial_info):
        with self.db.Session() as session:
            query = session.query(Financial)
            query_filter = query.filter(Financial.ticker == financial_info["ticker"])
            query_filter.update(financial_info)
            session.commit()

    def delete_company_by_ticker(self, ticker):
        with self.db.Session() as session:
            query = session.query(Financial)
            query_filter = query.filter(Financial.ticker == ticker)
            query_filter.delete()
            query = session.query(Company)
            query_filter = query.filter(Company.ticker == ticker)
            query_filter.delete()
            session.commit()

    def get_top_by_nd_ebitda(self, limit):
        division = Financial.net_debt / func.nullif(Financial.ebitda, 0)
        return self._query_calculate_and_order_by_desc(division, limit)

    def get_top_by_roe(self, limit):
        division = Financial.net_profit / func.nullif(Financial.equity, 0)
        return self._query_calculate_and_order_by_desc(division, limit)

    def get_top_by_roa(self, limit):
        division = Financial.net_profit / func.nullif(Financial.assets, 0)
        return self._query_calculate_and_order_by_desc(division, limit)

    def _query_calculate_and_order_by_desc(self, division, limit):
        with self.db.Session() as session:
            order_by_clause = desc(func.coalesce(division, 0))
            query = session.query(Financial.ticker, division).order_by(order_by_clause).limit(limit)
            return query.all()




