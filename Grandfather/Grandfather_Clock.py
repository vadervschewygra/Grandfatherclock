#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import time
import subprocess
#print(time.ctime())

def hour():
    """This will check the current time and if matches will play sound for that hour"""
    hour1 = "~/Desktop/Grandfather/hour1.wav"
    hour2 = "~/Desktop/Grandfather/hour2.wav"
    hour3 = "~/Desktop/Grandfather/hour3.wav"
    hour4 = "~/Desktop/Grandfather/hour4.wav"
    hour5 = "~/Desktop/Grandfather/hour5.wav"
    hour6 = "~/Desktop/Grandfather/hour6.wav"
    hour7 = "~/Desktop/Grandfather/hour7.wav"
    hour8 = "~/Desktop/Grandfather/hour8.wav"
    hour9 = "~/Desktop/Grandfather/hour9.wav"
    hour10 = "~/Desktop/Grandfather/hour10.wav"
    hour11 = "~/Desktop/Grandfather/hour11.wav"
    hour12 = "~/Desktop/Grandfather/hour12.wav"

    if '01:00:' in time.ctime():
        subprocess.call(['sox', hour1, '-d'])
    elif '13:00:' in time.ctime():
        subprocess.call(['sox', hour1, '-d'])

    if '02:00:' in time.ctime():
        subprocess.call(['sox', hour2, '-d'])
    elif '14:00:' in time.ctime():
        subprocess.call(['sox', hour2, '-d'])

    if '03:00:' in time.ctime():
        subprocess.call(['sox', hour3, '-d'])
    elif '15:00:' in time.ctime():
        subprocess.call(['sox', hour3, '-d'])

    if '04:00:' in time.ctime():
        subprocess.call(['sox', hour4, '-d'])
    elif '16:00:' in time.ctime():
        subprocess.call(['sox', hour4, '-d'])

    if '05:00:' in time.ctime():
        subprocess.call(['sox', hour5, '-d'])
    elif '17:00:' in time.ctime():
        subprocess.call(['sox', hour5, '-d'])

    if '06:00:' in time.ctime():
        subprocess.call(['sox', hour6, '-d'])
    elif '18:00:' in time.ctime():
        subprocess.call(['sox', hour6, '-d'])

    if '07:00:' in time.ctime():
        subprocess.call(['sox', hour7, '-d'])
    elif '19:00:' in time.ctime():
        subprocess.call(['sox', hour7, '-d'])

    if '08:00:' in time.ctime():
        subprocess.call(['sox', hour8, '-d'])
    elif '20:00:' in time.ctime():
        subprocess.call(['sox', hour8, '-d'])

    if '09:00:' in time.ctime():
        subprocess.call(['sox', hour9, '-d'])
    elif '21:00:' in time.ctime():
        subprocess.call(['sox', hour9, '-d'])

    if '10:00:' in time.ctime():
        subprocess.call(['sox', hour10, '-d'])
    elif '22:00:' in time.ctime():
        subprocess.call(['sox', hour10, '-d'])

    if '11:00:' in time.ctime():
        subprocess.call(['sox', hour11, '-d'])
    elif '23:00:' in time.ctime():
        subprocess.call(['sox', hour11, '-d'])

    if '12:00:' in time.ctime():
        subprocess.call(['sox', hour12, '-d'])
    elif '0:00:' in time.ctime():
        subprocess.call(['sox', hour12, '-d'])

def quarters():
    """This will play .wav file for quarter and half hours"""
    half = "~/Desktop/Grandfather/onehalf.wav"
    quarter = "~/Desktop/Grandfather/onequarter.wav"
    threequarter = "~/Desktop/Grandfather/threequarter.wav"
    if ':30:' in time.ctime():
        subprocess.call(['sox', half, '-d'])
    elif ':15:' in time.ctime():
        subprocess.call(['sox', quarter, '-d'])
    elif ':45:' in time.ctime():
        subprocess.call(['sox', threequarter, '-d'])

hour()
quarters()
