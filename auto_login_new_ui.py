import atomac
import time
import sys
import datetime
import os
from appscript import app

password = 'Test!123'
country_name_dict = {'France': '33185642659', 'Germany': '49691131126', 'Netherlands': '31201127373', 'United Kingdom': '441210430002', 'United States': '18552030004', 'Canada': '8774030001', 'Ireland': '353116000015', 'Spain': '34500000021', 'Switzerland': '41220000172'}


def wait_until_loggedin(timeout_seconds):
    print '----- wait_until_loggedin()'
    while True:
        wins = automator.windows()
        i = 0
        while len(wins) == 0 and i < 10:
            time.sleep(0.5)
            wins = automator.windows()
            i += 1
            print 'automator.windows() len = 0'
        current_window = wins[0]
        # check if Settings btn show to determine if logged in
        settings_btn = current_window.findFirstR(AXRole='AXButton', AXTitle='Settings')
        print 'timeLeft: ', timeout_seconds
        if settings_btn is not None and timeout_seconds > 0:
            return True
        elif timeout_seconds <= 0:
            print 'Wait login timeout'
            os.system('screencapture -R695,379,1225,801 ' + 'Log_In_Timeout_' + timeStamp + '.jpg')
            return False
        else:
            # print 'Not Found'
            time.sleep(1)
            timeout_seconds -= 1


def select_country_by_name(name):
    current_win = automator.windows()[0]
    select_country_btn = current_win.findFirstR(AXRole='AXPopUpButton')
    select_country_btn.Press()
    menu_item = currentWindow.findFirstR(AXRole='AXMenuItem', AXTitle=name)
    print 'country name: ' + name
    menu_item.Press()


def wait_login_screen(timeout_seconds):
    print '----- wait_login_screen()'
    while True:
        wins = automator.windows()
        i = 0
        while len(wins) == 0 and i < 10:
            time.sleep(0.5)
            wins = automator.windows()
            i += 1
            print 'automator.windows() len = 0'
        current_window = wins[0]
        # check if Phone Number field show to determine if logged out
        phone_number_field = current_window.findFirstR(AXRole='AXTextField', AXPlaceholderValue='Phone Number')
        print 'timeLeft: ', timeout_seconds
        if phone_number_field is not None and timeout_seconds > 0:
            return
        elif timeout_seconds <= 0:
            print 'Wait login timeout'
            break
        else:
            # print 'Not Found'
            time.sleep(1)
            timeout_seconds -= 1


def launch_app():
    global automator, currentWindow
    atomac.launchAppByBundleId('us.zoom.ringcentral')
    time.sleep(1)
    automator = atomac.getAppRefByBundleId('us.zoom.ringcentral')
    currentWindow = automator.windows()[0]
    signInBtn = currentWindow.findFirstR(AXRole='AXButton', AXTitle='Sign In')
    signInBtn.Press()
    wait_login_screen(15)


if __name__ == "__main__":
    args = sys.argv
    loopNumber = 2
    if len(args) == 2:
        loopNumber = int(args[1])
    elif len(args) > 2:
        print 'input error, e.g. python auto_login.py [loopNumber]'
        quit()

    print 'loop for %d times' % loopNumber
    atomac.terminateAppByBundleId('us.zoom.ringcentral')
    time.sleep(3)
    launch_app()

    index = 0
    while index < loopNumber:
        print '******* index: ' + str(index)
        currentWindow = automator.windows()[0]
        phoneNumberField = currentWindow.findFirstR(AXRole='AXTextField', AXPlaceholderValue='Phone Number')
        # extField = currentWindow.findFirstR(AXRole='AXTextField', AXPlaceholderValue='Ext')
        passwordField = currentWindow.findFirstR(AXRole='AXTextField', AXPlaceholderValue='Password')
        loginBtn = currentWindow.findFirstR(AXRole='AXButton', AXTitle='Login')
        # time.sleep(5)
        # change country
        i = index % len(country_name_dict)
        country_name = country_name_dict.keys()[i]
        phone_num = country_name_dict.get(country_name)
        select_country_by_name(country_name)
        time.sleep(1)
        currentWindow.clickMouseButtonLeft({980.00, 461.00})
        time.sleep(1)
        phoneNumberField.sendKeys(phone_num)
        currentWindow.clickMouseButtonLeft({980.00, 550.00})
        time.sleep(1)
        passwordField.sendKeys("Test")
        app('System Events').keystroke('!')
        passwordField.sendKeys("123")
        loginBtn.Press()

        status = wait_until_loggedin(30)
        if not status:
            atomac.terminateAppByBundleId('us.zoom.ringcentral')
            time.sleep(3)
            launch_app()
            continue

        timeStamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        print 'timeStamp: ', timeStamp
        os.system('screencapture -R1540,23,360,662 ' + timeStamp + '.jpg')
        currentWindow = automator.windows()[0]
        btn = currentWindow.findAll(AXRole='AXGroup')[0].findAll(AXRole='AXButton')[1]
        time.sleep(1)
        try:
            btn.Press()
        except:
            print('expected error')
        currentWindow = automator.windows()[0]
        # btn = currentWindow.findAll(AXRole='AXGroup')[0]
        # print btn.findAll()
        # currentWindow.clickMouseButtonLeft({1640.00, 65.00})
        time.sleep(1)
        # currentWindow.findAll(AXRole='AXGroup')[0].findAll(AXRole='AXMenuItem', AXTitle='Log Out')[0].Press()
        currentWindow.clickMouseButtonLeft({1730.00, 141.00})
        wait_login_screen(30)
        index += 1
        print 'Test Passed: %d Times' % index
