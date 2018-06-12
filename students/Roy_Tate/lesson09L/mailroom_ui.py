#!/usr/bin/python3


# Author/Student:  Roy Tate (githubtater)


class MailroomUI:

    def __init__(self):
        pass


    def menu_selection(prompt, arg_dict, response):
        try:
            arg_dict[response]['function']()
        except KeyError as e:
            print('22Invalid response: ' + str(e) + '\nTry again.')
        except ValueError as e:
            print('99Invalid entry: ' + str(e) + '\nTry again.')

    def main_menu(self):
        main_menu_args = {
            '1':{'option': 'Send a thank you', 'function': self.send_thank_you},
            '2':{'option': 'Print report', 'function': self.print_report},
            '3':{'option': 'Email all donors', 'function': self.email_all},
            '4':{'option': 'Exit', 'function': self.die}
        }

        while True:
            for k, v in sorted(main_menu_args.items()):
                print(k, v['option'])
            response = input('Enter your selection: ').strip()
            self.menu_selection(main_menu_args, response)



    def die(self):
        print('\nExiting.')
        exit(0)

    def send_thank_you(self):
        thank_you_args = {
            '1':{'option': 'Enter a dono', 'function': self.get_donation_amount},
            '2':{'option': 'Back to the Main Menu', 'function': self.main_menu},
            'list':{'option': 'Print a list of all donors', 'function': self.print_list},
        }
        for k, v in sorted(thank_you_args.items()):
            print(k, v['option'])
        response = input('Enter your selection: ').strip()
        self.menu_selection(thank_you_args, response)

    def print_report(self):
        print('Print_Report selected')

    def email_all(self):
        print('email_all selected')

    def get_donation_amount(self):
        donation_amount = input('Enter the amount of the donation: ')

    def print_list(self):
        print('PRINT_LIST selected')


if __name__=="__main__":
    x = MailroomUI()
    x.main_menu()

x = MailroomUI()
