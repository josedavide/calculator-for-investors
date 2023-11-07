class UiController:


    #def __init__(self):

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
            self.show_not_implemented()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_READ):
            self.show_not_implemented()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_UPDATE):
            self.show_not_implemented()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_DELETE):
            self.show_not_implemented()
        elif option == Main._menu_option_code(const.CRUD_MENU, const.CRUD_LIST_ALL):
            self.show_not_implemented()

        return option

    def manage_top_ten_menu(self):
        option = Main._show_top_ten_menu_and_get_option()
        if option == Main._menu_option_code(const.TOP_TEN_MENU, const.TOP_TEN_LIST_BY_EBITDA):
            self.show_not_implemented()
        elif option == Main._menu_option_code(const.TOP_TEN_MENU, const.TOP_TEN_LIST_BY_ROE):
            self.show_not_implemented()
        elif option == Main._menu_option_code(const.TOP_TEN_MENU, const.TOP_TEN_LIST_BY_ROA):
            self.show_not_implemented()

        return option


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
        print()
        print("Enter an option:")
        option = input()
        if any(option == number for number, _ in menu_options.values()):
            return option
        else:
            print("Invalid option!")
            print()
            return Main._show_menu_and_get_option(menu_content)

    @staticmethod
    def _show_menu(menu_title, options):
        print(menu_title)
        for (number, description) in options.values():
            print(number, description)

    @staticmethod
    def _menu_option_code(menu, option):
        return menu[1][option][0]

    def get_company_info(self):
        print("Enter ticker (in the format 'MOON'):")
        ticker = input()
        print("Enter company (in the format 'Moon Corp'):")
        name = input()
        print("Enter industries (in the format 'Technology'):")
        sector = input()

        return {'ticker': ticker, 'name': name, 'sector': sector}

    '''
        return {'ticker': ticker,
                'ebitda': safe_float(ebitda),
                'sales': safe_float(sales),
                'net_profit': safe_float(net_profit),
                'market_price': safe_float(market_price),
                'net_debt': safe_float(net_debt),
                'assets': safe_float(assets),
                'equity': safe_float(equity),
                'cash_equivalents': safe_float(cash_equivalents),
                'liabilities': safe_float(liabilities)}
    '''

    def create_company(self):
        company = get_company_info()
        financial = get_financial_info(company['ticker'])

        repository.add_new_company(company, financial)

    def show_not_implemented(self):
        print("Not implemented!")
        print()
