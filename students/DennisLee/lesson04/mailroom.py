#!/usr/bin/env python3

# Initial donor list and the amounts they have donated
donor_history = {
            'Red Herring': [65820.5, 31126.37, 15000],
            'Papa Smurf': [210.64, 1000],
            'Pat Panda': [55324.4],
            'Karl-Heinz Berthold': [3545.2, 10579.31],
            'Mama Murphy': [156316.99, 8500.3, 12054.33],
            'Daphne Dastardly': [82]
        }

def manage_donors():
    """
    Display the menu of choices for donor management.

    :return:  None.
    """
    # create a dictionary of menu items, menu text, and menu caller functions
    choices = {'1': ("Send a Thank You", send_thank_you), 
               '2': ("Create a Report", create_a_report),
               '3': ("Quit", exit_screen)}
    
    response = ''
    while response != '3':  # Show menu forever until user exits
        # Print the menu list (with numbered choices)
        print()
        for i in choices:
            print(i, choices[i][0])

        # Get the selection number
        response = ''
        while not response in choices:
            response = input("Type your selection: ").strip()

        choices[response][1]()  # Call helper function

def exit_screen():
    """
    Simply print an exit message.

    :return:  None.
    """
    print("\nExiting.\n")
    return

def send_thank_you():
    """
    Add new donations for new or existing donors, and send a thank-you
    letter.

    :return:  None.
    """
    # Get the donor name, show all donors, or quit
    response = input(
      "\nType the full donor name (or 'list' to show all donors, or 'quit'): "
      ).strip()

    if response.lower() in ('', 'quit'):
        exit_screen()
        return

    elif response.lower() == 'list':
        print("\nLIST OF DONORS:")
        for donor in donor_history:
            print(donor)
        send_thank_you()  # Try getting a donor name again

    else:
        while True:  # Get the donation amount
            donation = input(
                    f"Type amount donated by '{response}' (or type 'quit'): "
                    ).strip().lower()
            if donation == 'quit':
                exit_screen()
                return
            # Make sure the donation amount is a valid, positive number
            elif donation.strip('0123456789.') == '' and len(
                    donation) > 0 and donation.count('.') <= 1 and float(
                    donation) > 0.0:
                break

        # Add the donation to the master donor history and print the letter
        donation = float(donation)
        donor_history.setdefault(response, [])
        donor_history[response].append(donation)
        print(create_form_letter(response, donation))

def create_a_report():
    """
    Print out statistics for the entire donor list.

    :return:  None.
    """
    print('\n')
    print('Donor name                |         Total given | '
            + 'Number of gifts |        Average gift')
    print('--------------------------|---------------------|-'
            + '----------------|--------------------')
    for individual_donor, donations in donor_history.items():
        total_donation = sum(donations)
        number_of_gifts = len(donations)
        average_donation = 1.0 * total_donation / number_of_gifts
        print('{:<25s} | ${:>18,.2f} | {:>15d} | ${:>18,.2f}'.format(
                individual_donor, total_donation,
                number_of_gifts, average_donation))

def create_form_letter(donor_name, donor_amount):
    """
    Create the form letter using the donor name and amount.

    :donor_name:  The name of the donor.

    :donor_amount:  The amount given by the donor this time.

    :return:  A string containing the filled-in form letter.
    """
    str = """\n\n\n
            From:     Random Worthy Cause Foundation
            To:       {0:s}
            Subject:  Your generous donation

            Dear {0:s},

            We want to express our genuine gratitude for your donation of
            ${1:,.2f} to the Random Worthy Cause Foundation.  To show our
            appreciation, we have enclosed a set of address labels
            and a custom tote bag that lets people know that you are a
            generous supporter of our cause.
            
            Thank you again, and please think of us the next time you want
            to give to a worthy cause.

            Sincerely,



            Mister E. Partner
            Random Worthy Cause Foundation
            """
    
    return str.format(donor_name, donor_amount)

if __name__ == "__main__":
    manage_donors()
