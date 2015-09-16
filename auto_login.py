
import atomac
import time
import sys
import datetime
import os


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
            return
        elif timeout_seconds <= 0:
            print 'Wait login timeout'
        else:
            # print 'Not Found'
            time.sleep(1)
            timeout_seconds -= 1


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

if __name__ == "__main__":
    args = sys.argv
    loopNumber = 2
    if len(args) == 2:
        loopNumber = int(args[1])
    elif len(args) > 2:
        print 'input error, e.g. python auto_login.py [loopNumber]'
        quit()

    print 'loop for %d times' % loopNumber
    atomac.launchAppByBundleId('us.zoom.ringcentral')
    time.sleep(1)
    automator = atomac.getAppRefByBundleId('us.zoom.ringcentral')
    currentWindow = automator.windows()[0]
    signInBtn = currentWindow.findFirstR(AXRole='AXButton', AXTitle='Sign In')
    signInBtn.Press()
    wait_login_screen(15)

    index = 0
    while index < loopNumber:
        print '******* index: ' + str(index)
        currentWindow = automator.windows()[0]
        phoneNumberField = currentWindow.findFirstR(AXRole='AXTextField', AXPlaceholderValue='Phone Number')
        # extField = currentWindow.findFirstR(AXRole='AXTextField', AXPlaceholderValue='Ext')
        passwordField = currentWindow.findFirstR(AXRole='AXTextField', AXPlaceholderValue='Password')
        continueBtn = currentWindow.findFirstR(AXRole='AXStaticText', AXValue='Continue')
        phoneNumberField.Press()
        phoneNumberField.sendKeys('16505394171')
        passwordField.Press()
        passwordField.sendKeys('19860426')
        continueBtn.Press()
        wait_until_loggedin(15)
        timeStamp = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        print 'timeStamp: ', timeStamp
        os.system('screencapture -R1540,23,360,662 ' + timeStamp + '.jpg')
        currentWindow = automator.windows()[0]
        currentWindow.clickMouseButtonLeft({1713.00, 68.00})
        time.sleep(1)
        currentWindow.clickMouseButtonLeft({1740.00, 140.00})
        wait_login_screen(15)
        index += 1
        print 'Test Passed: %d Times' % index











