# VNC-Password-Helper

A small python tool to help with resetting password over VNC via rescue

## To use:
1. Boot in rescue mode
2. Run reset.py and make sure VNC Windows is in focus within 1 second
3. Boot up the VM
4. Go into Control Panel and then the create password menu
5. Run ``py main.py`` and focus the password field within 1 second
6. Run ``py main.py -s`` and focus the confirm password field within 1 second
7. Press create
8. Success!

## main.py arguments

``py main.py`` to run and generate a random password (gets saved to password.txt as well as typed)

``py main.py -s`` to automatically type the password or text saved in password.txt

``py main.py MyPassword`` to write "MyPassword"

## Important note - reset.py

When you run the reset.py file it will pause for a moment allowing you to press the key which represents the character ``-``

If you are using a Swedish or Danish keyboard this will most likley be the ``+`` button. This is to work around a current bug were the character ``-`` won't type correctly.
