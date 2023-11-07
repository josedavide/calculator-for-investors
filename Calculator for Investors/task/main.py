
import constants as const
from manager import Manager


class Main:

    def __init__(self):
        self.manager = Manager()

    def initialize_database(self):
        try:
            self.manager.initialize_database()
        except Exception as e:
            print("DB Initialization error:", e)
        #else:
        #    print("Database created successfully!")

    def manage_main_menu(self):
        while True:
            option = Main._show_main_menu_and_get_option()

            if option == Main._menu_option_code(const.MAIN_MENU, const.MAIN_EXIT):
                print('Have a nice day!')
                return 0
            elif option == Main._menu_option_code(const.MAIN_MENU, const.MAIN_CRUD):
                self.manage_crud_menu()
            elif option == Main._menu_option_code(const.MAIN_MENU, const.MAIN_TOP_TEN):
                self.manage_top_ten_menu()

    def manage_crud_menu(self):
        option = Main._show_crud_menu_and_get_option()
        if option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_CREATE):
            self.create_company()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_READ):
            self.read_company()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_UPDATE):
            self.update_company()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_DELETE):
            self.delete_company()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_LIST_ALL):
            self.list_all_companies()

        return option

    def manage_top_ten_menu(self):
        option = Main._show_top_ten_menu_and_get_option()
        if option == Main._menu_option_code(const.TOP_TEN_MENU, const.TOP_TEN_LIST_BY_EBITDA):
            top_10 = self.manager.get_top_10_by_nd_ebitda()
            print("TICKER ND/EBITDA")
            print('\n'.join([f"{ticker} {round(value, 2)}" for ticker, value in top_10]))
        elif option == Main._menu_option_code(const.TOP_TEN_MENU, const.TOP_TEN_LIST_BY_ROE):
            top_10 = self.manager.get_top_10_by_roe()
            print("TICKER ROE")
            print('\n'.join([f"{ticker} {round(value, 2)}" for ticker, value in top_10]))
        elif option == Main._menu_option_code(const.TOP_TEN_MENU, const.TOP_TEN_LIST_BY_ROA):
            top_10 = self.manager.get_top_10_by_roa()
            print("TICKER ROA")
            print('\n'.join([f"{ticker} {round(value, 2)}" for ticker, value in top_10]))

        return option

    def create_company(self):
        company = Main._get_company_info()
        financial = Main._get_financial_info(company['ticker'])

        self.manager.create_company(company, financial)
        print("Company created successfully!")

    def read_company(self):
        company = self._find_companies_to_select_one()
        if company is None:
            return
        ticker = company[0]
        company_name = company[1]
        indicators = self.manager.get_financial_indicators_by_ticker(ticker)
        print(ticker, company_name)
        print(''.join([f"{indicator} = {value}\n" for indicator, value in indicators]))

    def update_company(self):
        company = self._find_companies_to_select_one()
        if company is None:
            return
        financial_update = self._get_financial_info(company[0])
        self.manager.update_financial_info_by_ticker(financial_update)
        print("Company updated successfully!")

    def delete_company(self):
        company = self._find_companies_to_select_one()
        if company is None:
            return
        self.manager.delete_company_by_ticker(company[0])
        print("Company deleted successfully!")

    def _find_companies_to_select_one(self):
        company_name = input("Enter company name:\n")
        companies = self.manager.find_companies_by_name(company_name)
        if not companies:
            print("Company not found!")
            return None
        for index, company in enumerate(companies):
            print(index, company[1])
        company_index = int(input("Enter company number:\n"))
        return companies[company_index]

    def list_all_companies(self):
        companies = self.manager.list_all_companies()
        print("COMPANY LIST")
        print('\n'.join([f"{ticker} {company} {sector}" for ticker, company, sector in companies]))



    @staticmethod
    def _show_main_menu_and_get_option():
        return Main._show_menu_and_get_option(const.MAIN_MENU)

    @staticmethod
    def _show_crud_menu_and_get_option():
        return Main._show_menu_and_get_option(const.CRUD_MENU)

    @staticmethod
    def _show_top_ten_menu_and_get_option():
        return Main._show_menu_and_get_option(const.TOP_TEN_MENU)

    @staticmethod
    def _show_menu_and_get_option(menu_content):
        menu_title, menu_options = menu_content
        Main._show_menu(menu_title, menu_options)
        #print()
        print("Enter an option:")
        option = input()
        if any(option == number for number, _ in menu_options.values()):
            return option
        else:
            print("Invalid option!")
            #print()
            #return Main._show_menu_and_get_option(menu_content)

    @staticmethod
    def _show_menu(menu_title, options):
        print(menu_title)
        for (number, description) in options.values():
            print(number, description)

    @staticmethod
    def _menu_option_code(menu, option):
        return menu[1][option][0]

    @staticmethod
    def _get_company_info():
        print("Enter ticker (in the format 'MOON'):")
        ticker = input()
        print("Enter company (in the format 'Moon Corp'):")
        name = input()
        print("Enter industries (in the format 'Technology'):")
        sector = input()

        return {'ticker': ticker, 'name': name, 'sector': sector}

    @staticmethod
    def _get_financial_info(ticker):
        print("Enter ebitda (in the format '987654321'):")
        ebitda = input()
        print("Enter sales (in the format '987654321'):")
        sales = input()
        print("Enter net profit (in the format '987654321'):")
        net_profit = input()
        print("Enter market price (in the format '987654321'):")
        market_price = input()
        print("Enter net debt (in the format '987654321')::")
        net_debt = input()
        print("Enter assets (in the format '987654321'):")
        assets = input()
        print("Enter equity (in the format '987654321'):")
        equity = input()
        print("Enter cash equivalents (in the format '987654321'):")
        cash_equivalents = input()
        print("Enter liabilities (in the format '987654321'):")
        liabilities = input()

        return {'ticker': ticker,
                'ebitda': ebitda,
                'sales': sales,
                'net_profit': net_profit,
                'market_price': market_price,
                'net_debt': net_debt,
                'assets': assets,
                'equity': equity,
                'cash_equivalents': cash_equivalents,
                'liabilities': liabilities}

    def show_not_implemented(self):
        print("Not implemented!")
        print()



if __name__ == '__main__':
    print("Welcome to the Investor Program!")
    main = Main()
    main.initialize_database()
    main.manage_main_menu()
