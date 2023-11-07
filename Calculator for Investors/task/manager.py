import csv
from database import Database
from models import Company, Financial
from repository import Repository


class Manager:

    def __init__(self):
        self.repository = Repository(Database())

    def initialize_database(self):
        try:
            self.repository.initialize_database()
            self.repository.load_data(
                    Manager._read_csv_companies(),
                    Manager._read_csv_financial())
        except Exception as e:
            raise

    def create_company(self, company, financial):
        self.repository.add_new_company(company, financial)

    def find_companies_by_name(self, company_name):
        found_companies = self.repository.find_companies_by_name(company_name)
        companies_list = [(company.ticker, company.name) for company in found_companies]
        return companies_list

    def get_financial_indicators_by_ticker(self, ticker):
        financial = self.find_company_financial_by_ticker(ticker)
        if financial is None:
            return None
        else:
            return Manager.get_financial_indicators(financial)

    @staticmethod
    def get_financial_indicators(financial):
        if financial is None:
            return []
        return financial.get_indicators()

    def find_company_financial_by_ticker(self, ticker):
        financial_info = self.repository.find_financial_info_by_ticker(ticker)
        return financial_info

    def update_financial_info_by_ticker(self, financial_info):
        self.repository.update_financial_info(financial_info)

    def delete_company_by_ticker(self, ticker):
        self.repository.delete_company_by_ticker(ticker)

    def list_all_companies(self):
        all_companies = self.repository.list_all_companies()
        companies_list = [(company.ticker, company.name, company.sector) for company in all_companies]
        return companies_list

    def get_top_10_by_nd_ebitda(self):
        return self.repository.get_top_by_nd_ebitda(10)

    def get_top_10_by_roe(self):
        return self.repository.get_top_by_roe(10)

    def get_top_10_by_roa(self):
        return self.repository.get_top_by_roa(10)


    @staticmethod
    def _read_csv_companies():
        with open('companies.csv', 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            companies = list(csv_reader)

        return companies

    @staticmethod
    def _read_csv_financial():
        with open('financial.csv', 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            financials = list(csv_reader)

        return financials
