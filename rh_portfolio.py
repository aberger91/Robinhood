from Robinhood import Robinhood
from getpass import getpass

if __name__ == '__main__':
    username = 'abberger1'
    password = getpass('Password: ')

    rh = Robinhood()
    rh.login(username=username,
             password=password)
    hist = rh.historical_portfolio('day', '5minute', 'trading')
    print(hist.text)
