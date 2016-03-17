# scope-month
Keysight Scope Month automated single entry using Selenium.

## Setup

### Install Python Dependencies
After cloning and navigating to this repository install the python depencies.
Only Python2.7 is supported.

    $ pip install -r requirements.txt

### Edit config.json
With a text editor **edit the config.json** file and fill out your information. The fields should be fairly self explanatory.
The only field that requires specific values is "oscope_need" which can be "never", "3 months", or "12 months".

### Add a timer (optional)
Within the systemd directory a systemd service and timer file have already been created.
You will need to edit the service file to reflect the directory you clone this repository into.
After you have editted the service file you need to copy them into the correct location.
    
    $ cp systemd/scope-month.* ~/.config/systemd/user/

Then you should be able to start and enable the timer and be good to go.
    
    $ systemctl --user enable scope-month.timer
    $ systemctl --user start scope-month.timer

Just remember to remove these files and disable the timer after scope month has ended.

### Running manually
If you decide you don't want to use the systemd service files you can manually run main.py
    
    $ ./main.py
    
To see the options of main.py
    
    $ ./main.py --help

### Profit???
Hopefully you win yourself a nice o-scope. Keep in mind that automated multi-entry violates the rules of the contest.
I don't believe this violates the rules of the contest but I could be wrong.
