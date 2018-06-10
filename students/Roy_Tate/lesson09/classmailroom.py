#!/usr/bin/python3

## Author/student:  Roy Tate (githubtater)

from collections import defaultdict

class Donor:

    donor_dict = {}

    def __init__(self, name, amount):
        if not name:
            raise ValueError('Please provide a donor name.')
        if not amount:
            raise ValueError('Please provide a donation amount')
        self.name = name.title()
        self.donations = []
        self.add_donation(amount)

        # self.donor_dict[self._ln, self._fn] = [self._donations]
        # print(self.donor_dict)

    def __add__(self, other):
        new_donation = self.amount
        if isinstance(other, (int, float)):
            new_donation += other
        elif isinstance(other, Donor):
            new_donation += other.amount
        return Donor(new_donation)


    def __str__(self):
        return 'Donor name: {}  Donations: {}'.format(self.name, sum(self.donations))

    def __repr__(self):
        return 'Donor({}, {})'.format(self.name, sum(self.donations))

    def add_donation(self, new_donation):
        self.donations.append(round(new_donation, 2))

    @property
    def total_donations(self):
        return sum(self.donations)

    @property
    def average(self):
        return self.total_donations / self.num_gifts

    @property
    def num_gifts(self):
        return len(self.donations)

    @property
    def letter(self):
        text = '''\n
                From:    A Charity Thankful For Your Kindness
                To:      {0}
                Subject:  This Year's Challenge!

                Dear {0},

                First, we would like to thank you for your continued generosity throughout the 
                years. Without contributions like yours, the good things that we are able to do 
                simply would not be possible. 

                Your contributions to date have totaled ${1:.2f}. 
                
                This years challenge is to see if you can donate more than your current total
                in one year. This would effectively double your current donations to the 
                organization!  Remember, it is for a good cause!

                Sincerely,

                The good guys at the best organization'''

        return text.format(self.name, sum(self.donations))

donor = Donor('roy tate',100)
donor.add_donation(2637)
donor.add_donation(2234)
donor.add_donation(18822353)
print(donor)
print(donor.letter)


class DonorCollection:

    def __init__(self):
        self.donors = {}

    def __repr__(self):
        return 'DonorCollection()'

    @property
    def print_all(self):
        format_str = '{:<20}{:<20}{:<20}'
        header = format_str.format('Donor Name', 'Donations(sum)', '# of Donations')
        for donor in self.donors:
            header += format_str.format(donor.name, sum(donor.donations), len(donor.donations))

        return header

    @property
    def generate_email_file(self):
        pass


dc = DonorCollection()