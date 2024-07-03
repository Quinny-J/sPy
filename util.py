# I'm still learning python. 
# Made by @Quinny-J
# 03/07/2024

# References 
# Flask - https://flask.palletsprojects.com/en/3.0.x/
# Socket - https://docs.python.org/3/library/socket.html

# Class is being used to store multiple vars in a catagory in this case strings
class statusColors:
    OKCYAN = '\033[96m' # Python likes ANSI :)
    WARN = '\033[91m'
    WHITE = '\033[0m'

# Class is being used to store multiple vars in a catagory in this case fstrings
class statusMsg:
    UI = f'\033[0m[{statusColors.OKCYAN}UI{statusColors.WHITE}]'
    OK = f'\033[0m[{statusColors.OKCYAN}OK{statusColors.WHITE}]'
    WARN = f'\033[0m[{statusColors.WARN}WARN{statusColors.WHITE}]'
    OPEN = f'\033[0m[{statusColors.OKCYAN}OPEN{statusColors.WHITE}]'
    CLOSED = f'\033[0m[{statusColors.WARN}CLOSED{statusColors.WHITE}]'