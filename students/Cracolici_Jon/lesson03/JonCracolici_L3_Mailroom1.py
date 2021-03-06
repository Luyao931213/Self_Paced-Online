#Jon Cracolici
#Lesson 03 Mailroom 1
#UW Python Cert

#Below are the functions my program uses

def initialize_database():
    """This function intializes the database when called."""
    d1 = ['William Gates, III', 653784.49, 2, 326892.24]
    d2 = ['Mark Zuckerberg', 16396.10 , 3, 5465.37]
    d3 = ['Jeff Bezos', 877.33, 1, 877.33]
    d4 = ['Paul Allen', 708.42, 3, 236.14]
    dB = [d1, d2, d3, d4]
    return dB
#	

def newdonor(name, dB):
    """Creates a new donor in the database and requests donation amount."""
    donation = float(input("How much did {} donate?".format(name)))
    newdonor = [name, donation, 1, donation]
    dB.append(newdonor)
    return name, donation
#

def update_donor(name, dB):
    """Updates an existing donor in the database with a new donation."""
    for item in dB:
        if item[0] == str(name):
            newdonation = float(input("How much did {} donate? ".format(name)))
            print(item)
            print(type(item[1]))
            item[1] += float(newdonation)
            item[2] += 1
            item[3] = item[1]/item[2]
            break
    return name, newdonation
#
def show_current_names(dB):
    """Displays the names of all previous donors."""
    names = [ item[0] for item in dB]
    #print(names)
    lastname = names.pop(len(names)-1)
    #print(names)
    #print(lastname)
    l = len(names)
    display = "The current donors are "+(l*" {},").format(*names)+" and {}.".format(lastname)
    return display
#
def note_gen(n):
    """Creates a thank you note and prints it to screen."""
    name = n[0]
    donation = n[1]
    print("Dear {},".format(name)+"\nThank you for your generous donation of ${:.02f}. Please rest assured that we will use at least \n95% of your contribution to feed the homeless to wolves. We could not do this work without you. \nSincerely, \nThe Billionaires' Club".format(donation))
#

def create_report(dB):
    """This creates a sorted summary report of all donors."""
    dB.sort(key=lambda x: x[1], reverse=True)
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    for donor in dB:
        print('{:26}${:>13.2f}{:>12} ${:>12.2f}'.format(*donor))
#
#
#Now here is the program the user will interact with. Please note that there are print statements 
#commented out because I found them helpful to track the control flow.
if __name__=="__main__":
    dB = initialize_database()
    task = 'Start'
    print(task)
    print('Welcome to our mailroom app!')
    print('Please select your action from the following options')
    print('Send a Thank You')
    print('Create a Report')
    print('Quit')
    
    while task != ('Quit' or 'quit'):
        task = input('Please select a task. ')
        if task == 'Quit':
            print(task)
        while task == 'Send a Thank You':
            currentnames = [ item[0] for item in dB]
            donorname = str(input('What donor would you like to send a note to? '))
            print(donorname)
            if donorname == ('Quit' or 'quit'):
                task = 'Start'
            elif donorname == ('List' or 'list'):
                print(show_current_names(dB))
            elif donorname  in [ item[0] for item in dB]: #this is the trouble spot. how to recognize a name inside a list?
                note_gen(update_donor(donorname,dB)) 
                task = 'Start'
            elif donorname not in dB:
                note_gen(new_donor(donorname,dB))
                task = 'Start'
        if task == 'Create a Report':
            create_report(dB)
            task = 'Start'
