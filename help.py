import os

help = []

def get_help():
    """
    Sets the list of available casino game submodules.

    This function scans the "casino_games" directory for Python files, dynamically 
    imports each module, and checks if the module has a 'game_title' attribute.
    If the attribute exists, the game's title along with its command name is added 
    to the formatted list.

    Returns:
        None
    """
    #global help
    help_text = r"""
   ___         
 _|\  \__                          === HELP MENU ===
|\   ____\      Welcome to Terminal Monopoly!                           
\ \  \___|_         
 \ \_____  \    This help screen will assist you with all the commands
  \|____|\  \   available in the TerminalMonopoly interface. 
    ____\_\  \  
   |\___    __\
   \|___|\__\_|                                       
        \|__|               

"""
    max_len = 0
    for file in os.listdir("modules_directory"):
        if file.endswith(".py"):
            file = file[:-3]
            i = __import__('modules_directory.' + file, fromlist=[''])
            if(hasattr(i, 'help_text')):
                message = i.help_text.ljust(37, '.')
                help_text += f"{message}\n"
                if max_len < len(message):
                    max_len = len(message)
    
    buffer = " " * max_len
    help_text += fr"""
{buffer}   ___
{buffer} _|\  \__
{buffer}|\   ____\
{buffer}\ \  \___|_
{buffer} \ \_____  \ 
{buffer}  \|____|\  \
{buffer}    ____\_\  \
{buffer}   |\___    __\
{buffer}   \|___|\__\_|
{buffer}        \|__| """
    return help_text

if __name__ == "__main__":
    help = get_help()
    print(help)