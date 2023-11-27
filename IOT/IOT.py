from tkinter import *
from tkinter import ttk, scrolledtext
import tkinter as tk
from future.moves import tkinter
from PIL import Image
import urllib.request
import os
import socket
import json
import requests
import time
import string
import datetime
#import pyaudio
#import sounddevice
import wave
from datetime import datetime
# global ws_server1
import os
import time
from tkinter import simpledialog
import asyncio
import websockets
from tkinter import filedialog as fd
import sys
import subprocess
from websocket import create_connection
from easygui import *
import threading
from time import sleep
from configparser import ConfigParser
import sqlite3
import re
import runpy
#from easygui import *
import cv2 as cv
import cv2
from cv2 import *
import io
#from matplotlib import pyplot as plt
import configparser
import copy
import multiprocessing
import binascii
from threading import Timer
import shutil
log_now = datetime.now()
log_date_time = log_now.strftime("%d_%m_%Y_%H_%M_%S")
folder_name = "logs"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
log_file_name = os.path.join(folder_name, f"logfile_{log_date_time}.log")
if not os.path.exists("LIVE_SNAPS"):
    os.makedirs("LIVE_SNAPS")

def remove_chunks(source_folder):
    destination_folder = "junk"

    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Move each file from the source folder to the destination folder
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Check if the item is a file (not a directory) before moving
        if os.path.isfile(source_path):
            shutil.move(source_path, destination_path)

# index
ra = tkinter.Tk()
ra.title('IOT')
ra.geometry('400x300')
frame = Frame(ra, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.85, rely=0.15)

# Cientra techsolutions display
canvas = Canvas(ra, width=700, height=100, bg="white smoke")

canvas.create_text(350, 55, text="CIENTRA TECHSOLUTIONS Pvt.Ltd", fill="midnight blue", font=('Helvetica 15 bold'),
                   width=600)
canvas.pack()

# adding text below Cientra
a = Label(ra, text="An ISO 9001:2015 Company", font=("arial italic", 12))
a.pack()

def chunks_clean():
    for filename in os.listdir("chunks"):
        file_path = os.path.join("chunks", filename)
        os.remove(file_path)
    for filename in os.listdir("LIVE_CS"):
        file_path = os.path.join("LIVE_CS", filename)
        os.remove(file_path)
    for filename in os.listdir("chunks_Audio"):
        file_path = os.path.join("chunks_Audio", filename)
        os.remove(file_path)
    for filename in os.listdir("chunks_video"):
        file_path = os.path.join("chunks_vodeo", filename)
        os.remove(file_path)
    for filename in os.listdir("chunks_Audio_RS"):
        file_path = os.path.join("chunks_Audio_RS", filename)
        os.remove(file_path)
    for filename in os.listdir("junk"):
        file_path = os.path.join("junk", filename)
        os.remove(file_path)


def Log_prints():
    log_text = scrolledtext.ScrolledText(ra, wrap=tk.WORD)
    log_text.place(x=800, y=600, width=950, height=350)
    log_text.tag_configure("uplink", foreground="blue")
    log_text.tag_configure("downlink", foreground="green")
    
    logfile_path = log_file_name
    try:
        with open(logfile_path, "r") as file:
            log_content = file.read()
            log_text.insert(tk.END, log_content)
            log_lines = log_text.get("1.0", tk.END).splitlines()
            for idx, line in enumerate(log_lines):
                if line.endswith("sent"):
                    log_text.tag_add("uplink", f"{idx + 1}.0", f"{idx + 1}.end")
                elif line.endswith("response") or line.endswith("data"):
                    log_text.tag_add("downlink", f"{idx + 1}.0", f"{idx + 1}.end")
    except FileNotFoundError:
        log_text.insert(tk.END, "Logfile not found.")


global ws_server1
config = configparser.ConfigParser()
if len(sys.argv) < 2:
	sys.exit("PLEASE ENTER REQURIED PARAMETERS")
else:
	IOTX=sys.argv[1]
config_iot = ConfigParser()
config_iot.read('confiot.ini')
config_iot[IOTX]['ueid'] = '-1'
with open("confiot.ini", "w") as f:
    config_iot.write(f)
# chars = " " + string.punctuation + string.digits + string.ascii_letters
# with open('keyfile.key', 'r') as f:
#    key = f.read()
"""
import smbus
import time
bus = smbus.SMBus(1)
from mpu6050 import mpu6050
import time
from contextlib import redirect_stdout
Device_Address = 0x68
mpu = mpu6050(Device_Address)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin_a = 18
pin_b = 24
def discharge():
    GPIO.setup(pin_a, GPIO.IN)
    GPIO.setup(pin_b, GPIO.OUT)
    GPIO.output(pin_b, False)
    time.sleep(0.004)
def charge_time():
    GPIO.setup(pin_b, GPIO.IN)
    GPIO.setup(pin_a, GPIO.OUT)
    count = 0
    GPIO.output(pin_a, True)
    while not GPIO.input(pin_b):
        count = count + 1
    return count

def analog_read():
    discharge()
    return charge_time()



 
# Set the GPIO mode to BCM

GPIO.setmode(GPIO.BCM)
servo_pin = 18
# Set the frequency of the PWM signal (usually 50 Hz)
pwm_frequency = 50

# Initialize the GPIO pin for PWM

GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, pwm_frequency)
# Function to set the angle of the servo

def set_angle(angle):

    duty_cycle = (angle / 18) + 2

    pwm.ChangeDutyCycle(duty_cycle)

    time.sleep(1)  # Give the servo some time to move
try:
    # Start the PWM
    pwm.start(0)
    # Rotate the servo to different angles
    set_angle(0)  # 0 degrees

    set_angle(90)  # 90 degrees

    set_angle(180)  # 180 degrees

 

except KeyboardInterrupt:

    pass

 

# Clean up the GPIO

pwm.stop()

GPIO.cleanup()


"""

# closebutton
def close():
    ra.destroy()

btn1_nms = Button(ra, text="CLOSE", fg='white', bg='RED', command=close)
btn1_nms.pack()
btn1_nms.place(anchor='center', relx=0.974, rely=0.026)


key = b'Cientra@1'
data_encrypted = ""


def encryption(data):
    data_to_encrypt = data.encode()
    encrypted = data_encrypted
    nr = 0
    n = len(key)
    for ch in data_to_encrypt:
        message = ch
        password = (key[nr])
        encrypted = encrypted + (chr(message ^ password))
        nr += 1
        if nr == n:
            nr = 0
    encrypted = encrypted.encode()
    return encrypted

def sending1(data):
    if globals()["Protocol"]=="WEB_SOCKET":
        globals()["ws_server1"].send(data)
        print(data)
    elif globals()["Protocol"]=='Http':
        print("sending data to the",globals()["Protocol"])
        print(data)
        globals()["sock"].send(data.encode())
    elif globals()["Protocol"]=="TCP":
        print("sending data to the",globals()["Protocol"])
        print(data)
        globals()["sock"].send(data.encode())
    else:
        pass


def receiving1(Protocol):
    while True:
        if globals()["Protocol"]=="WEB_SOCKET":
            rec_call = globals()["ws_server1"].recv()
            process_received(rec_call)
            #print(rec_call)
            with open(log_file_name, "a") as file_object:
                file_object.write('>>Downlink data')
                file_object.write('\n')
                file_object.write("Data----->" + "From the Network is"+"----->"+ rec_call)
                file_object.write('\n')
            Log_prints()
        elif globals()["Protocol"]=="Http":
            print("data receiving from the",globals()["Protocol"])
            rec_call = globals()["sock"].recv(4096)
            process_received(rec_call.decode())
        elif globals()["Protocol"]=="TCP":
            print("data receiving from the",globals()["Protocol"])
            rec_call = globals()["sock"].recv(1024)
            process_received(rec_call.decode())
        else:
            pass

globals()["sensor_timer"] = True
def sensor(actual_sensor_name,timer,operation):
    global sensor_timer
    ti = int(timer)
    if globals()["sensor_timer"]:
        t1 = threading.Timer(ti, sensor, args=[actual_sensor_name,ti,operation])
        if ti != 0 and operation == "START":
            t1.start()
            print("Threading Started")
            if actual_sensor_name=="TEMPERATURE":
                value1=actual_sensor_name+" "+str(mpu.get_temp())+" "+str(ti)
            elif actual_sensor_name=="POTENTIOMETER":
                value1=actual_sensor_name+" "+str(analog_read())+" "+str(ti) 
            else:
                value1="unknown sensor name"
            data = json.dumps({"userid":  config_iot[IOTX]['userid'], "command": "5G_sensorvalue", "value": value1})
            size_data = sys.getsizeof(data)
            Preamble = config_iot['encryption/decryption']['Preamble']
            if Preamble == "3$@!":
                size = hex(size_data)[2:].zfill(4)
                msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                data = Preamble.encode() + msg_len.encode() + encryption(data)
                sending1(data)
            elif Preamble == "2$@!":
                size = hex(size_data)[2:].zfill(4)
                msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                data = Preamble + msg_len + data
                sending1(data.encode())
            else:
                sending1(Preamble + data)
            globals()["sensor_timer"] = True
            
        elif operation == "STOP" and (ti == 0 or ti != 0):
            if actual_sensor_name=="TEMPERATURE":
                value1=actual_sensor_name+" "+str(mpu.get_temp())+" "+str(ti)
            elif actual_sensor_name=="POTENTIOMETER":
                value1=actual_sensor_name+" "+str(analog_read())+" "+str(ti) 
            else:
                value1="unknown sensor name"
            data = json.dumps({"userid": config_iot[IOTX]['userid'], "sensor_name":actual_sensor_name, "value": value1})       
            size_data = sys.getsizeof(data)
            Preamble = config_iot['encryption/decryption']['Preamble']
            if Preamble == "3$@!":
                size = hex(size_data)[2:].zfill(4)
                msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                data = Preamble.encode() + msg_len.encode() + encryption(data)
                sending1(data)
            elif Preamble == "2$@!":
                size = hex(size_data)[2:].zfill(4)
                msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                data = Preamble + msg_len + data
                sending1(data.encode())
            else:
                sending1(Preamble + data)            
            t1.cancel()
            globals()["sensor_timer"] = False
            print("Threading is finished")
        else:
            print("invalid operation please update")
    else:
        globals()["sensor_timer"] = True

# Receiving from Aggregator
def process_received(rec_call):
    new_Win = Tk()
    new_Win.withdraw()
    try:
        if rec_call.split('/')[0] == "PasswordValidation":
            pass

        else:
            message = json.loads(rec_call)
            print("message->", message,type(message))
            if message.get("command") == "RETRIEVE_IOT":
                sensor_name=message.get("NAME")
                print(sensor_name)
                print(type(sensor_name))
                if sensor_name.startswith("SENSOR"):
                    i = int(sensor_name[len("SENSOR"):len("SENSOR")+1])
                    print(i)
                    timer=message.get("TIMER")
                    print(type(timer))
                    operation = message.get("OPERATIONS")
                    ID = message.get("ID")
                    print("ID FROM SERVER:",ID)
                    actual_sensor_id = config_iot[IOTX][f"sensor{i}_id"]
                    print("ID FROM CONFIG FILE",actual_sensor_id)
                    actual_sensor_name = config_iot[IOTX][f"sensor{i}_name"]
                    print(actual_sensor_name)
                    config_iot[IOTX][f"sensor{i}_timer"] = timer
                    config_iot[IOTX][f"sensor{i}_operation"] = operation
                    with open('confiot.ini', 'w') as f:
                        config_iot.write(f)
                    timer = config_iot[IOTX][f"sensor{i}_timer"]
                    ti = int(timer)
                    if operation == "FETCH":
                        if actual_sensor_name=="POTENTIOMETER" and ID == actual_sensor_id:
                            value1=sensor_name+" "+str(analog_read())+" "+str(ti)
                        elif actual_sensor_name =="TEMPERATURE" and ID == actual_sensor_id:
                            value1=sensor_name+" "+str(mpu.get_temp())+" "+str(ti)
                        else:
                            print("some invalid parameters")
                        data = json.dumps({"userid":  config_iot[IOTX]['userid'], "command": "5G_sensorvalue", "value": value1})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            sending1(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            sending1(data.encode())
                        else:
                            sending1(Preamble + data)
                        
                    elif operation == "START" and ti == 0:
                        print("Hiii")
                        if actual_sensor_name=="POTENTIOMETER" and ID == actual_sensor_id:
                            value1=sensor_name+" "+str(analog_read())+" "+str(ti)
                        elif actual_sensor_name =="TEMPERATURE" and ID == actual_sensor_id:
                            value1=sensor_name+" "+str(mpu.get_temp())+" "+str(ti)
                        data = json.dumps({"userid":  config_iot[IOTX]['userid'], "command": "5G_sensorvalue", "value": value1})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            sending1(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            sending1(data.encode())
                        else:
                            sending1(Preamble + data)
                    
                    
                    
                    elif (operation == "START" and ti != 0) or (operation=="STOP" and ti == 0 or ti !=0) and ID == actual_sensor_id:
                        print("************************************************")
                        timer = config_iot[IOTX][f"sensor{i}_timer"]
                        sensor(actual_sensor_name,timer,operation)
                    else:
                        print("there is no such operations")
                        
                    
                    
                elif sensor_name.startswith("ACTUATOR"):
                    i = int(sensor_name[len("ACTUATOR"):len("ACTUATOR")+1])
                    print("i is ------------------------------->",i)
                    operation = message.get("OPERATIONS")
                    print("OPERATION NAME IS -------------------------------->",operation)
                    config_iot[IOTX][f"actuator{i}_operation"] = operation
                    with open('confiot.ini', 'w') as f:
                        config_iot.write(f)
                    ID = message.get("ID")
                    print("ID FROM SERVER",ID)
                    actual_actuator_id = config_iot[IOTX][f'actuator{i}_id']
                    print("ID FROM CONFIG FILE",actual_actuator_id)
                    actual_actuator_name = config_iot[IOTX][f'actuator{i}_name']
                    print(actual_actuator_name)
                    print(type(actual_actuator_name))
                    print(sensor_name)
                    
                    if (operation == "ON" or operation == "OFF" or operation == "BEEP") and actual_actuator_name == "BUZZER" and ID == actual_actuator_id:
                        GPIO.setmode(GPIO.BCM)
                        buzzer_pin = 17
                        GPIO.setup(buzzer_pin, GPIO.OUT)
                        def turn_buzzer_on():
                            GPIO.output(buzzer_pin, GPIO.HIGH)
                        def turn_buzzer_off():
                            GPIO.output(buzzer_pin, GPIO.LOW)
                        try:
                            if operation == "ON":
                                turn_buzzer_on()
                            elif operation == "OFF":
                                turn_buzzer_off()
                            elif operation == "BEEP":
                                turn_buzzer_on()
                                sleep(2)
                                turn_buzzer_off()
                            elif operation == None:
                                print("no operation")
                            else:
                                print("Invalid choice. Please enter a valid option.")
                        except Exception as e:
                            print(e)
                    
                    
                    elif operation == "CAPTURE" and actual_actuator_name == "CAMERA" and ID == actual_actuator_id:
                        try:
                            cam_port = 0
                            cam = cv.VideoCapture(cam_port)
                            result, image = cam.read()
                            now = datetime.now()
                            date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
                            print(date_time)
                            if result:
                                path = os.path.join("LIVE_SNAPS", f"captured_image_{date_time}.jpg")
                                cv.imwrite(path, image)
                                image = cv.imread(path)
                                cv.imshow("IOT_CAPTURE!!", image)
                                cv.waitKey(5000)
                                cv.destroyAllWindows()
                                def chunk_large_file(input_file, chunk_size):
                                    os.makedirs("LIVE_CS", exist_ok=True)
                                    for filename in os.listdir("LIVE_CS"):
                                        file_path = os.path.join("LIVE_CS", filename)
                                        os.remove(file_path)
                                    with open(input_file, 'rb') as f:
                                        chunk_number = 0
                                        while True:
                                            chunk_data = f.read(chunk_size)
                                            if not chunk_data:
                                                break
                                            chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                            with open(os.path.join("LIVE_CS", chunk_filename), 'wb') as chunk_file:
                                                chunk_file.write(chunk_data)
                                            chunk_number += 0.01
                                            print(chunk_number)
                                        files = os.listdir("LIVE_CS")
                                        file_size = len(os.listdir("LIVE_CS"))
                                        for file in files:
                                            file_path = os.path.join("LIVE_CS", file)
                                            print(sys.getsizeof(file))
                                            if os.path.isfile(file_path):
                                                with open(file_path, 'rb') as f:
                                                    file_contents = f.read()
                                                    file_content = list(file_contents)
                                                    f.close
                                                    data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Capture_Live_Photo_CS','file_formate':input_file[-4:],'chunk_name':file,'data':file_content,'file_name':file_name, 'chunks_count':file_size})
                                                    size_data = sys.getsizeof(data)
                                                    Preamble = config_iot['encryption/decryption']['Preamble']
                                                    if Preamble == "3$@!":
                                                        size = hex(size_data)[2:].zfill(4)
                                                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                        data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                        sending1(data)
                                                    elif Preamble == "2$@!":
                                                        size = hex(size_data)[2:].zfill(4)
                                                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                        data = Preamble + msg_len + data
                                                        sending1(data.encode())
                                                    else:
                                                        sending1(Preamble + data)
                                input_file = path
                                if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                                    print(fn)
                                    file_name,formatt=fn[0].split('.')
                                else:
                                    print("invalid file")
                                chunk_size = 1024*60
                                chunk_large_file(input_file, chunk_size)
                            else:
                                print("no camera on current device")
                        except Exception as e:
                            print(e)
                            
                    elif (operation == "NEUTRAL" or "ROTATE-90" or "ROTATE-180") and actual_actuator_name == "SERVOMOTER" and ID == actual_actuator_id:  #NEUTRAL,ROTATE-90,ROTATE-180
                        print("THE ACTUATOR SERVOMOTER TRIGGERED FROM SERVER")
                        try:
                            if operation == "NEUTRAL":
                                print('hello')
                                GPIO.setmode(GPIO.BCM)
                                servo_pin = 18
                                pwm_frequency = 50
                                GPIO.setup(servo_pin, GPIO.OUT)
                                pwm = GPIO.PWM(servo_pin, pwm_frequency)
                                def set_angle(angle):
                                    duty_cycle = (angle / 18) + 2
                                    pwm.ChangeDutyCycle(duty_cycle)
                                    time.sleep(1)  # Give the servo some time to move
                                try:
                                    # Start the PWM
                                    pwm.start(0)
                                    # Rotate the servo to different angles
                                    set_angle(0)  #
                                except KeyboardInterrupt:
                                    pass
                                pwm.stop()
                                GPIO.cleanup()                         
                            elif operation == "ROTATE-90":
                                GPIO.setmode(GPIO.BCM)
                                servo_pin = 18
                                pwm_frequency = 50
                                GPIO.setup(servo_pin, GPIO.OUT)
                                pwm = GPIO.PWM(servo_pin, pwm_frequency)
                                def set_angle(angle):
                                    duty_cycle = (angle / 18) + 2
                                    pwm.ChangeDutyCycle(duty_cycle)
                                    time.sleep(1)  # Give the servo some time to move
                                try:
                                    # Start the PWM
                                    pwm.start(0)
                                    # Rotate the servo to different angles
                                    set_angle(90)  #
                                except KeyboardInterrupt:
                                    pass
                                pwm.stop()
                                GPIO.cleanup()
                            elif operation == "ROTATE-180":
                                GPIO.setmode(GPIO.BCM)
                                servo_pin = 18
                                pwm_frequency = 50
                                GPIO.setup(servo_pin, GPIO.OUT)
                                pwm = GPIO.PWM(servo_pin, pwm_frequency)
                                def set_angle(angle):
                                    duty_cycle = (angle / 18) + 2
                                    pwm.ChangeDutyCycle(duty_cycle)
                                    time.sleep(1)  # Give the servo some time to move
                                try:
                                    # Start the PWM
                                    pwm.start(0)
                                    # Rotate the servo to different angles
                                    set_angle(180)  #
                                except KeyboardInterrupt:
                                    pass
                                pwm.stop()
                                GPIO.cleanup()
                                
                            else:
                                print("SERVOMOTER CAN PERFORM ONLY NEUTRAL or ROTATE-90 or ROTATE-180 FUNCTIONS")
                        except Exception as e:
                            print(e)
                                
                            
                    elif operation == "ON" or operation == "OFF" or operation == "BLINK" and actual_actuator_name == "LED" and ID == actual_actuator_id:  #ON,OFF,BLINK
                        print("THE ACTUATOR LED TRIGGERED FROM SERVER")
                        GPIO.setmode(GPIO.BCM)
                        # Define the GPIO pins for the LED and buzzer
                        led_pin = 21  # BCM GPIO 17 for the LED
                        # Set up the GPIO pins as outputs
                        GPIO.setup(led_pin, GPIO.OUT)
                        def turn_led_on():
                            GPIO.output(led_pin, GPIO.HIGH)
                        def turn_led_off():
                            GPIO.output(led_pin, GPIO.LOW)
                        try:
                            
                            if operation == "ON":
                                turn_led_on()
                            elif operation == "OFF":
                                turn_led_off()
                            elif operation == "BLINK":
                                turn_led_on()
                                sleep(3)
                                turn_led_off()
                            elif operation == None:
                                print("no operation")
                                
                            else:
                                print("LED CAN PERFORM ONLY ON or OFF or BLINK FUNCTIONS")
                                print("Invalid choice. Please enter a valid option.")
                        except Exception as e:
                            print(e)


                    else:
                        print("not yet updated with valid operator")
                    
                else:
                    print("THERE IS NO SUCH PARAMETER")
         
              


            elif message.get("NAME") == "5G_Capture_Live_Photo_CS":
                try:
                    cam_port = 0
                    cam = cv.VideoCapture(cam_port)
                    result, image = cam.read()
                    now = datetime.now()
                    date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
                    if result:
                        path = os.path.join("LIVE_SNAPS", f"captured_image_{date_time}.jpg")
                        cv.imwrite(path, image)
                        image = cv.imread(path)
                        cv.imshow("IOT_CAPTURE!!", image)
                        cv.waitKey(5000)
                        cv.destroyAllWindows()
                        def chunk_large_file(input_file, chunk_size):
                            os.makedirs("LIVE_CS", exist_ok=True)
                            for filename in os.listdir("LIVE_CS"):
                                file_path = os.path.join("LIVE_CS", filename)
                                os.remove(file_path)
                            with open(input_file, 'rb') as f:
                                chunk_number = 0
                                while True:
                                    chunk_data = f.read(chunk_size)
                                    if not chunk_data:
                                        break
                                    chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                    with open(os.path.join("LIVE_CS", chunk_filename), 'wb') as chunk_file:
                                        chunk_file.write(chunk_data)
                                    chunk_number += 0.01
                                    print(chunk_number)
                                files = os.listdir("LIVE_CS")
                                file_size = len(os.listdir("LIVE_CS"))
                                for file in files:
                                    file_path = os.path.join("LIVE_CS", file)
                                    print(sys.getsizeof(file))
                                    if os.path.isfile(file_path):
                                        with open(file_path, 'rb') as f:
                                            file_contents = f.read()
                                            file_content = list(file_contents)
                                            f.close
                                            data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Capture_Live_Photo_CS','file_formate':input_file[-4:],'chunk_name':file,
                                            'data':file_content,'file_name':file_name, 'chunks_count':file_size})
                                            print(file_name)
                                            size_data = sys.getsizeof(data)
                                            Preamble = config_iot['encryption/decryption']['Preamble']
                                            if Preamble == "3$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                sending1(data)
                                            elif Preamble == "2$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble + msg_len + data
                                                sending1(data.encode())
                                            else:
                                                sending1(Preamble + data)
                        input_file = path
                        if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                        	print(fn)
                        	file_name,formatt=fn[0].split('.')
                        else:
                            print("invalid file")
                        chunk_size = 1024*60
                        chunk_large_file(input_file, chunk_size)
                        
                        	
                    else:
                        print("no camera on current device")
                except Exception as e:
                    print(e)
                


            elif message.get("command") == "5G_Capture_Live_Photo_CS":
                try:
                    cam_port = 0
                    cam = cv.VideoCapture(cam_port)
                    result, image = cam.read()
                    date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
                    now = datetime.now()
                    if result:
                        path = os.path.join("LIVE_SNAPS", f"captured_image_{date_time}.jpg")
                        cv.imwrite(path, image)
                        image = cv.imread(path)
                        cv.imshow("IOT_CAPTURE!!", image)
                        cv.waitKey(5000)
                        cv.destroyAllWindows()
                        def chunk_large_file(input_file, chunk_size):
                            os.makedirs("LIVE_CS", exist_ok=True)
                            for filename in os.listdir("LIVE_CS"):
                                file_path = os.path.join("LIVE_CS", filename)
                                os.remove(file_path)
                            with open(input_file, 'rb') as f:
                                chunk_number = 0
                                while True:
                                    chunk_data = f.read(chunk_size)
                                    if not chunk_data:
                                        break
                                    chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                    with open(os.path.join("LIVE_CS", chunk_filename), 'wb') as chunk_file:
                                        chunk_file.write(chunk_data)
                                    chunk_number += 0.01
                                    print(chunk_number)
                                files = os.listdir("LIVE_CS")
                                file_size = len(os.listdir("LIVE_CS"))
                                for file in files:
                                    file_path = os.path.join("LIVE_CS", file)
                                    print(sys.getsizeof(file))
                                    if os.path.isfile(file_path):
                                        with open(file_path, 'rb') as f:
                                            file_contents = f.read()
                                            file_content = list(file_contents)
                                            f.close
                                            data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Capture_Live_Photo_CS','file_formate':input_file[-4:],'chunk_name':file,
                                            'data':file_content,'file_name':file_name,'chunks_count':file_size})
                                            size_data = sys.getsizeof(data)
                                            Preamble = config_iot['encryption/decryption']['Preamble']
                                            if Preamble == "3$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                sending1(data)
                                            elif Preamble == "2$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble + msg_len + data
                                                sending1(data.encode())
                                            else:
                                                sending1(Preamble + data)
                        input_file = os.path.join("LIVE_SNAPS", f"captured_image_{date_time}.jpg")
                        if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                        	print(fn)
                        	file_name,formatt=fn[0].split('.')
                        else:
                            print("invalid file")
                        chunk_size = 1024*60
                        chunk_large_file(input_file, chunk_size)
                        	
                    else:
                        print("no camera on current device")
                        
                except Exception as e:
                    print(e)
                    
            elif message.get("command") == "5G_SMS":
                try:
                    phone_number = message.get("PHONE_NUMBER")
                    if phone_number is not None:
                        ser_data = "SMS alert from IOT"
                        if ser_data is not None:
                            data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SMS', 'message': ser_data, 'Phone_number':phone_number})
                            size_data = sys.getsizeof(data)
                            Preamble = config_iot['encryption/decryption']['Preamble']
                            if Preamble == "3$@!":
                                size = hex(size_data)[2:].zfill(4)
                                msg_len = config_iot['msg_code']['sms_5g'] + hex(size_data)[2:].zfill(4)
                                data = Preamble.encode() + msg_len.encode() + encryption(data)
                                print(data)
                                client_socket.sendall(data)
                            elif Preamble == "2$@!":
                                size = hex(size_data)[2:].zfill(4)
                                msg_len = config_iot['msg_code']['sms_5g'] + hex(size_data)[2:].zfill(4)
                                data = Preamble + msg_len + data
                                print(data)
                                client_socket.sendall(data.encode())
                            else:
                                print(data)
                                client_socket.sendall(Preamble + data)
                        else:
                            print('User canceled SMS input.')
                    else:
                        print('User canceled phone number input.')

                except Exception as e:
                    print(e)
                with open(log_file_name, "a") as file_object:
                    file_object.write('>>Payload sent')
                    file_object.write('\n')
                    file_object.write("Data to the network is---------->"+ data)
                    file_object.write('\n')
                Log_prints()


            elif message.get("command") == "5G_PAYLOAD":
                try:
                    user_data = message.get("DATA")
                    data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Payloadsend', 'message': user_data})
                    size_data = sys.getsizeof(data)
                    Preamble = config_iot['encryption/decryption']['Preamble']
                    if Preamble == "3$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble.encode() + msg_len.encode() + encryption(data)
                        sending1(data)
                    elif Preamble == "2$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble + msg_len + data
                        sending1(data.encode())
                    else:
                        sending1(Preamble + data)

                except Exception as e:
                    print(e)
                with open(log_file_name, "a") as file_object:
                    file_object.write('>>Payload sent')
                    file_object.write('\n')
                    file_object.write("Data to the network is---------->"+ data)
                    file_object.write('\n')
                Log_prints()

            elif message.get("command") == "5G_SendfileUP":
                try:
                    filename = message.get("file_name")
                    print(filename)
                    f = open(filename, "r")
                    file_data = f.read()
                    f.close()
                    data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SendfileUP', 'data': file_data})
                    size_data = sys.getsizeof(data)
                    Preamble = config_iot['encryption/decryption']['Preamble']
                    if Preamble == "3$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble.encode() + msg_len.encode() + encryption(data)
                        sending1(data)
                    elif Preamble == "2$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble + msg_len + data
                        sending1(data.encode())
                    else:
                        sending1(Preamble + data)

                except Exception as e:
                    print(e)
                with open(log_file_name, "a") as file_object:
                    file_object.write('>>Payload sent')
                    file_object.write('\n')
                    file_object.write("Data to the network is---------->"+ data)
                    file_object.write('\n')
                Log_prints()


            elif message.get("command") == "file_list":
                try:
                    current_directory = os.path.dirname(os.path.abspath(__file__))
                    try:
                        files = os.listdir(current_directory)
                        list_file = []
                        for file in files:
                            if os.path.isfile(file) and '.' in file:
                                list_file.append(file)
                        print(list_file)
                    except FileNotFoundError:
                        print(f"The specified path '{current_directory}' does not exist.")
                    except PermissionError:
                        print(f"Permission error accessing the path '{current_directory}'.")
                    data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'USERID':IOTX, 'command': 'file_list','file_list': list_file})
                    size_data = sys.getsizeof(data)
                    Preamble = config_iot['encryption/decryption']['Preamble']
                    if Preamble == "3$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble.encode() + msg_len.encode() + encryption(data)
                        sending1(data)
                    elif Preamble == "2$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble + msg_len + data
                        sending1(data.encode())
                    else:
                        sending1(Preamble + data)

                except Exception as e:
                    print(e)
                with open(log_file_name, "a") as file_object:
                    file_object.write('>>CP_file data sent')
                    file_object.write('\n')
                    file_object.write("Data to the network is---------->"+ data)
                    file_object.write('\n')
                Log_prints()


            elif message.get("command") == "5G_sendfile_CP":
                try:
                    filename = fd.askopenfilename()
                    print(filename)
                    f = open(filename, "r")
                    file_data = f.read()
                    f.close()
                    data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SendfileCP', 'data': file_data})
                    size_data = sys.getsizeof(data)
                    Preamble = config_iot['encryption/decryption']['Preamble']
                    if Preamble == "3$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble.encode() + msg_len.encode() + encryption(data)
                        sending1(data)
                    elif Preamble == "2$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble + msg_len + data
                        sending1(data.encode())
                    else:
                        sending1(Preamble + data)

                except Exception as e:
                    print(e)
                with open(log_file_name, "a") as file_object:
                    file_object.write('>>CP_file data sent')
                    file_object.write('\n')
                    file_object.write("Data to the network is---------->"+ data)
                    file_object.write('\n')
                Log_prints()

            elif message.get("command") == "5G_sendfile_UP":
                try:
                    filename = fd.askopenfilename()
                    print(filename)
                    f = open(filename, "r")
                    file_data = f.read()
                    f.close()
                    data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SendfileUP', 'data': file_data})
                    size_data = sys.getsizeof(data)
                    Preamble = config_iot['encryption/decryption']['Preamble']
                    if Preamble == "3$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble.encode() + msg_len.encode() + encryption(data)
                        sending1(data)
                    elif Preamble == "2$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble + msg_len + data
                        sending1(data.encode())
                    else:
                        sending1(Preamble + data)

                except Exception as e:
                    print(e)
                with open(log_file_name, "a") as file_object:
                    file_object.write('>>CP_file data sent')
                    file_object.write('\n')
                    file_object.write("Data to the network is---------->"+ data)
                    file_object.write('\n')
                Log_prints()

            elif message.get("command") == "5G_SendPhoto_S":
                try:
                    def chunk_large_file(input_file, chunk_size):
                        os.makedirs("chunks", exist_ok=True)
                        for filename in os.listdir("chunks"):
                            file_path = os.path.join("chunks", filename)
                            os.remove(file_path)
                        with open(input_file, 'rb') as f:
                            chunk_number = 0
                            while True:
                                chunk_data = f.read(chunk_size)
                                if not chunk_data:
                                    break
                                chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                with open(os.path.join("chunks", chunk_filename), 'wb') as chunk_file:
                                    chunk_file.write(chunk_data)
                                chunk_number += 0.01
                                print(chunk_number)
                            files = os.listdir("chunks")
                            file_size = len(os.listdir("chunks"))
                            for file in files:
                                file_path = os.path.join("chunks", file)
                                if os.path.isfile(file_path):
                                    with open(file_path, 'rb') as f:
                                        file_contents = f.read()
                                        file_content = list(file_contents)
                                        f.close
                                        data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SendPhoto_S','file_formate':input_file[-4:],'chunk_name':file,'data':file_content,'file_name':file_name, 'chunks_count':file_size})
                                        size_data = sys.getsizeof(data)
                                        Preamble = config_iot['encryption/decryption']['Preamble']
                                        if Preamble == "3$@!":
                                            size = hex(size_data)[2:].zfill(4)
                                            msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                                            sending1(data)
                                        elif Preamble == "2$@!":
                                            size = hex(size_data)[2:].zfill(4)
                                            msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                            data = Preamble + msg_len + data
                                            sending1(data.encode())
                                        else:
                                            sending1(Preamble + data)
                    input_file = fd.askopenfilename(filetypes=[("image files", "*.jpg *.png")]) #("image files", "*.jpg *.jpeg *.png *.bmp *.gif")
                    if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                        print(fn)
                        file_name,formatt=fn[0].split('.')
                        	
                    else:
                        print("invalid name")
                    chunk_size = 1024*60
                    chunk_large_file(input_file, chunk_size)
                except Exception as e:
                    print(e)

            
            elif message.get("command") == "5G_Capture_Live_Photo_C":
                try:
                    cam_port = 0
                    cam = cv.VideoCapture(cam_port)
                    result, image = cam.read()
                    if result:
                        cv.imshow("CAPTURE!!", image)
                        now = datetime.now()
                        date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
                        path = f"LIVE_SNAPS/5g_capture{date_time}.jpg"
                        cv.imwrite(path, image)
                        print("5G_Capture_Live_Photo_C is done verify the image in live snaps")
                        # filename = '%s.png' % date_time
                        # cv.imwrite(filename, image)
                        cv.waitKey(2000)
                        cv.destroyAllWindows()
                    else:
                        print("no camera on current device")
                except Exception as e:
                    print(e)
           
                    
            elif message.get("command") == "5G_Degister":
                print('Logout Request sent')    
                try:
                    data = json.dumps({'MsgCode': config_iot['msg_code']['deregister_5g']})
                    size_data = sys.getsizeof(data)
                    Preamble = config_iot['encryption/decryption']['Preamble']
                    if Preamble == "3$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['deregister_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble.encode() + msg_len.encode() + encryption(data)
                        print("*********************************",data)
                        client_socket.sendall(data)
                    elif Preamble == "2$@!":
                        size = hex(size_data)[2:].zfill(4)
                        msg_len = config_iot['msg_code']['deregister_5g'] + hex(size_data)[2:].zfill(4)
                        data = Preamble + msg_len + data
                        print(data)
                        client_socket.sendall(data.encode())
                    else:
                        print("the data is *************",data)
                        client_socket.sendall(data.encode())
                    config_iot[IOTX]['ueid'] = '-1'
                    with open("confiot.ini", "w") as f:
                        config_iot.write(f)
                except Exception as e:
                    print(e)
                with open("logs.txt", "a") as file_object:
                    file_object.write('>>Logout sent')
                    file_object.write('\n')
                    file_object.write( "LOGOUT sent to the Network/--------->"+data)
                    file_object.write('\n')
                Log_prints()          
            
            else:
                #print("Command is not found")
                pass
            remove_chunks("chunks")
            remove_chunks("LIVE_CS")



    except:
        pass
    finally:
        pass
    new_Win.destroy()


            
        
def Login_server():
    print('Login sent')
    try:
        data=json.dumps({'MsgCode':"Login_Request", 'Userid': config_iot[IOTX]['userid'], 'Password': config_iot[IOTX]['password'], 'serialnumber':config_iot[IOTX]['serialnumber']})     
        size_data = sys.getsizeof(data)
        Preamble = config_iot['encryption/decryption']['Preamble']
        if Preamble == "3$@!":
            size = hex(size_data)[2:].zfill(4)
            msg_len = config_iot['msg_code']['login_request'] + hex(size_data)[2:].zfill(4)
            data = Preamble.encode() + msg_len.encode() + encryption(data)
            sending1(data)
        elif Preamble == "2$@!":
            size = hex(size_data)[2:].zfill(4)
            msg_len = config_iot['msg_code']['login_request'] + hex(size_data)[2:].zfill(4)
            data = Preamble + msg_len + data
            sending1(data.encode())
        else:
            sending1(Preamble + data)
    except Exception as e:
        print(e)
    with open(log_file_name, "a+") as file_object:
        file_object.write('>>Login Request sent')
        file_object.write('\n')
        file_object.write("LOGIN/" + "sent to the network"+ data)
        file_object.write('\n')



def command6( *args):

    #print('internode')
    if menu6.get() == "Secuirity surveillance":
        def command2121( *args):
        	print('surveillance')
        	
        	if menu2121.get()== "id_card_verify":
        		print("data")
        		thres = 0.45
        		cap = cv2.VideoCapture(0)
        		frame_width = int(cap.get(3))
        		frame_height = int(cap.get(4))
        		size = (frame_width, frame_height)
        		result = cv2.VideoWriter('filename.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, size)
        		cap.set(3,1280)
        		cap.set(4,720)
        		cap.set(10,70)
        		classNames = ['ID_CARD']
        		classFile = 'classes.names'
        		with open(classFile,'rt') as f:
        			classNames = f.read().rstrip('\n').split('\n')
        		configPath = 'yolov3_custom.cfg'
        		weightsPath = 'yolov3_training_last.weights'
        		net = cv2.dnn_DetectionModel(weightsPath,configPath)
        		net.setInputSize(320,320)
        		net.setInputScale(1.0/ 127.5)
        		net.setInputMean((127.5, 127.5, 127.5))
        		net.setInputSwapRB(True)
        		
        		while True:
        			success,img = cap.read()
        			classIds, confs, bbox = net.detect(img,confThreshold=thres)
        			print(classIds,confs,bbox)
        			if len(classIds) != 0:
        				for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
        					cv2.rectangle(img,box,color=(0,255,0),thickness=2)
        					#cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
        					#cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
        					try:
        						if confs >= 0.85:
        							reader = easyocr.Reader(['en'], gpu=False)
        							#result = reader.readtext(img)
        							result = reader.readtext(img, detail = 0, paragraph=True)
        							print(result)
        						
        							result = list[result]
        							print(len(result))
        							print(result[1:3])
        							break
        						else:
        							print("system is waiting for Best frame")
        							continue	
        					except Exception as e:
                                                    print("hiiiiiiiiiiiiiiiiiii")
                                                    print(e)
        					data = json.dumps({'ueid':config_iot[IOTX]['ueid'], 'command': 'Payloadsend','data': result[1:3]})
        					sending1(data)
        			cv2.imshow("Output",img)
        			k=cv2.waitKey(1)
        			if k == 27:
        				break
        		cap.release()

        	elif menu2121.get() =="Add_id_details":
        		try:
        			text = "ID_DETAILS_SAME_AS_ID_CARD"
        			# window title
        			title = "ID_CARD_DETAILS"
        			# list of multiple inputs
        			input_list = ["company_name", "Employee_name","Employee_number", "Blood_group",]
        			# creating a integer box
        			output = multenterbox(text, title, input_list)
        			# title for the message box
        			title = "Message Box"
        			# creating a message
        			message = str(output)
        			print(message)
        			my_list_2 = re.findall(r"'([^']*)'", message)
        			print(my_list_2)
        			data = json.dumps({'initial':'initval','command': 'Add_id_details', 'company_name':my_list_2[0], 'Employee_name':my_list_2[1], 'Employee_number':my_list_2[2], 'Blood_group':my_list_2[3]})
        			sending1(data)
        		except Exception as e:
        			print(e)        		        	
        				
        	elif menu2121.get() =="Face_detection":
        		print("face detection")
        	elif menu2121.get() == "People_count":
        		print("people count")
        	else:
        		pass
        def command2122( *args):
        	print('surveillance')
        	
        	if menu2122.get() == "licence_number":
        		print("data")
        		
        	elif menu2122.get() =="vehicle_count":
        		print("face detection")
        	elif menu2122.get() == "People_count":
        		print("people count")
        	else:
        		pass        		
        
        menu2121 = StringVar()
        menu2121.set("Secuirity")
        drop = OptionMenu(ra, menu2121,"id_card_verify","Add_id_details","Face_detection","People_count",command = command2121)
        drop.pack()
        drop.config(width=18)
        drop.place(anchor='center', relx=0.3, rely=0.35)
        menu2122 = StringVar()
        menu2122.set("Transport")
        drop = OptionMenu(ra, menu2122,"licence_number","vehicle_count","parking_slot",command = command2122)
        drop.pack()
        drop.config(width=18)
        drop.place(anchor='center', relx=0.17, rely=0.35)
#surveillance
menu6= StringVar()
menu6.set("surveillance")
drop= OptionMenu(ra,menu6,"Secuirity surveillance","Transport surveillance",command = command6)
drop.pack()
drop.config(width=18)
drop.place(anchor='center',relx=0.25,rely=0.3)
cc=Label(ra, text="surveillance", fg='white', bg='red', font=("arial italic", 12) )
cc.pack()
cc.place(anchor='center', relx=0.25, rely=0.27)
def Node(*args):
    if menu1.get() == 'simulated-iot':
        if True:

            def command103(*args):

                if menu2222.get() == "5G_Deregister":
                    print('Logout Request sent')
                    

                    try:
                        data = json.dumps({'MsgCode': config_iot['msg_code']['deregister_5g']})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['deregister_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            print("*********************************",data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['deregister_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            print("the data is *************",data)
                            client_socket.sendall(data.encode())
                        config_iot[IOTX]['ueid'] = '-1'
                        with open("confiot.ini", "w") as f:
                            config_iot.write(f)
                    except Exception as e:
                        print(e)
                    with open("logs.txt", "a") as file_object:
                        file_object.write('>>Logout sent')
                        file_object.write('\n')
                        file_object.write( "LOGOUT sent to the Network/--------->"+data)
                        file_object.write('\n')
                    Log_prints()
                    
                elif menu2222.get() == "5G_Capture_Live_Photo_CS":
                    try:
                        cam_port = 0
                        cam = cv.VideoCapture(cam_port)
                        result, image = cam.read()
                        now = datetime.now()
                        date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
                        if result:
                            path = os.path.join("LIVE_SNAPS", f"captured_image_{date_time}.jpg")
                            cv.imwrite(path, image)
                            image = cv.imread(path)
                            cv.imshow("IOT_CAPTURE!!", image)
                            cv.waitKey(5000)
                            cv.destroyAllWindows()
                            def chunk_large_file(input_file, chunk_size):
                                os.makedirs("LIVE_CS", exist_ok=True)
                                for filename in os.listdir("LIVE_CS"):
                                    file_path = os.path.join("LIVE_CS", filename)
                                    os.remove(file_path)
                                with open(input_file, 'rb') as f:
                                    chunk_number = 0
                                    while True:
                                        chunk_data = f.read(chunk_size)
                                        if not chunk_data:
                                            break
                                        chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                        with open(os.path.join("LIVE_CS", chunk_filename), 'wb') as chunk_file:
                                            chunk_file.write(chunk_data)
                                        chunk_number += 0.01
                                        print(chunk_number)
                                    files = os.listdir("LIVE_CS")
                                    file_size = len(os.listdir("LIVE_CS"))
                                    for file in files:
                                        file_path = os.path.join("LIVE_CS", file)
                                        print(sys.getsizeof(file))
                                        if os.path.isfile(file_path):
                                            with open(file_path, 'rb') as f:
                                                file_contents = f.read()
                                                file_content = list(file_contents)
                                                f.close
                                                data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Capture_Live_Photo_CS','file_formate':input_file[-4:],'chunk_name':file,'data':file_content,'file_name':file_name,'chunks_count':file_size})
                                                size_data = sys.getsizeof(data)
                                                Preamble = config_iot['encryption/decryption']['Preamble']
                                                if Preamble == "3$@!":
                                                    size = hex(size_data)[2:].zfill(4)
                                                    msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                    data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                    sending1(data)
                                                elif Preamble == "2$@!":
                                                    size = hex(size_data)[2:].zfill(4)
                                                    msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                    data = Preamble + msg_len + data
                                                    sending1(data.encode())
                                                else:
                                                    sending1(Preamble + data)
                            input_file = os.path.join("LIVE_SNAPS", f"captured_image_{date_time}.jpg")
                            if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                                print(fn)
                                file_name,formatt=fn[0].split('.')
                            else:
                                print("invalid file")
                            chunk_size = 1024*60
                            chunk_large_file(input_file, chunk_size)
                        else:
                            print("no camera on current device")
                    except Exception as e:
                        print(e)

                elif menu2222.get() == "5G_Capture_Live_Photo_C":
                    try:
                        cam_port = 0
                        cam = cv.VideoCapture(cam_port)
                        result, image = cam.read()
                        if result:
                            cv.imshow("CAPTURE!!", image)
                            now = datetime.now()
                            date_time = now.strftime("%d_%m_%Y_%H_%M_%S")
                            path = f"LIVE_SNAPS/5g_capture{date_time}.jpg"
                            cv.imwrite(path, image)
                            print("5G_Capture_Live_Photo_C is done verify the image in live snaps")
                            cv.waitKey(2000)
                            cv.destroyAllWindows()
                        else:
                            print("no camera on current device")

                    except Exception as e:
                        print(e)

                elif menu2222.get() == "5G_SendPhoto_S":
                    try:
                        def chunk_large_file(input_file, chunk_size):
                            os.makedirs("chunks", exist_ok=True)
                            for filename in os.listdir("chunks"):
                                file_path = os.path.join("chunks", filename)
                                os.remove(file_path)
                            with open(input_file, 'rb') as f:
                                chunk_number = 0
                                while True:
                                    chunk_data = f.read(chunk_size)
                                    if not chunk_data:
                                        break
                                    chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                    with open(os.path.join("chunks", chunk_filename), 'wb') as chunk_file:
                                        chunk_file.write(chunk_data)
                                    chunk_number += 0.01
                                    print(chunk_number)
                                files = os.listdir("chunks")
                                file_size = len(os.listdir("chunks"))
                                for file in files:
                                    file_path = os.path.join("chunks", file)
                                    if os.path.isfile(file_path):
                                        with open(file_path, 'rb') as f:
                                            file_contents = f.read()
                                            file_content = list(file_contents)
                                            f.close
                                            data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SendPhoto_S','file_formate':input_file[-4:],'chunk_name':file,
                                            'data':file_content,'file_name':file_name,'chunks_count':file_size})
                                            size_data = sys.getsizeof(data)
                                            Preamble = config_iot['encryption/decryption']['Preamble']
                                            if Preamble == "3$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                sending1(data)
                                            elif Preamble == "2$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble + msg_len + data
                                                sending1(data.encode())
                                            else:
                                                sending1(Preamble + data)
                        input_file = fd.askopenfilename(filetypes=[("image files", "*.jpg *.png")]) #("image files", "*.jpg *.jpeg *.png *.bmp *.gif")
                        if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                        	print(fn)
                        	file_name,formatt=fn[0].split('.')
                        	
                        else:
                        	print("invalid name")
                        chunk_size = 1024*60
                        chunk_large_file(input_file, chunk_size)
                    except Exception as e:
                        print(e)
                        
                elif menu2222.get() == "5G_Video_send":
                    try:
                        def chunk_large_file(input_file, chunk_size):
                            os.makedirs("chunks_video", exist_ok=True)
                            for filename in os.listdir("chunks_video"):
                                file_path = os.path.join("chunks_video", filename)
                                os.remove(file_path)
                            with open(input_file, 'rb') as f:
                                chunk_number = 0
                                while True:
                                    chunk_data = f.read(chunk_size)
                                    if not chunk_data:
                                        break
                                    chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                    with open(os.path.join("chunks_video", chunk_filename), 'wb') as chunk_file:
                                        chunk_file.write(chunk_data)
                                    chunk_number += 0.01
                                    print(chunk_number)
                                files = os.listdir("chunks_video")
                                for file in files:
                                    file_path = os.path.join("chunks_video", file)
                                    if os.path.isfile(file_path):
                                        with open(file_path, 'rb') as f:
                                            file_contents = f.read()
                                            file_content = list(file_contents)
                                            f.close
                                            data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Video_send','file_formate':input_file[-4:],'chunk_name':file,
                                            'data':file_content,'file_name':file_name})
                                            size_data = sys.getsizeof(data)
                                            Preamble = config_iot['encryption/decryption']['Preamble']
                                            if Preamble == "3$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                sending1(data)
                                            elif Preamble == "2$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble + msg_len + data
                                                sending1(data.encode())
                                            else:
                                                sending1(Preamble + data)
                        input_file =fd.askopenfilename(filetypes=[('image files', '.mp4'), ('image files', '.avi')])
                        if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                        	print(fn)
                        	file_name,formatt=fn[0].split('.')
                        	
                        else:
                        	print("invalid name")
                        chunk_size = 1024*60
                        chunk_large_file(input_file, chunk_size)
                    except Exception as e:
                        print(e)

                elif menu2222.get() == "5G_Audio_Record_send":
                    try:
                        OUTPUT_FILE = "recorded_audio.wav"
                        def record_audio(duration):
                            FORMAT, CHANNELS, RATE, CHUNK = pyaudio.paInt16, 1, 44100, 1024    # Audio recording parameters
                            audio = pyaudio.PyAudio()
                            stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
                            print("Recording started...")
                            frames = []
                            try:
                                for i in range(int(RATE / CHUNK * duration)):
                                    data = stream.read(CHUNK)
                                    frames.append(data)
                                print("Recording finished.")
                                stream.stop_stream()
                                stream.close()
                                audio.terminate()
                                with wave.open(OUTPUT_FILE, "wb") as wav_file:
                                    wav_file.setnchannels(CHANNELS)
                                    wav_file.setsampwidth(audio.get_sample_size(FORMAT))
                                    wav_file.setframerate(RATE)
                                    wav_file.writeframes(b''.join(frames))
                                print("Audio file saved as:", OUTPUT_FILE)
                            except Exception as e:
                                print(e)
                                
                        duration = simpledialog.askinteger(title='Duration of recording', prompt='please enter Number of seconds')
                        record_audio(duration)
                        input_file = OUTPUT_FILE
                        def chunk_large_file(input_file, chunk_size):
                            os.makedirs("chunks_Audio_RS", exist_ok=True)
                            for filename in os.listdir("chunks_Audio_RS"):
                                file_path = os.path.join("chunks_Audio_RS", filename)
                                os.remove(file_path)
                            with open(input_file, 'rb') as f:
                                chunk_number = 0
                                while True:
                                    chunk_data = f.read(chunk_size)
                                    if not chunk_data:
                                        break
                                    chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                    with open(os.path.join("chunks_Audio_RS", chunk_filename), 'wb') as chunk_file:
                                        chunk_file.write(chunk_data)
                                    chunk_number += 0.01
                                files = os.listdir("chunks_Audio_RS")
                                for file in files:
                                    file_path = os.path.join("chunks_Audio_RS", file)
                                    if os.path.isfile(file_path):
                                        with open(file_path, 'rb') as f:
                                            file_contents = f.read()
                                            file_content = list(file_contents)
                                            f.close
                                            data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Audio_Record_send','file_formate':input_file[-4:],'chunk_name':file,'data':file_content,'file_name':file_name})
                                            size_data = sys.getsizeof(data)
                                            Preamble = config_iot['encryption/decryption']['Preamble']
                                            if Preamble == "3$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                sending1(data)
                                            elif Preamble == "2$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble + msg_len + data
                                                sending1(data.encode())
                                            else:
                                                sending1(Preamble + data)
                        if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                        	print(fn)
                        	file_name,formatt=fn[0].split('.')
                        	
                        else:
                        	print("invalid name")
                        chunk_size = 1024*60
                        chunk_large_file(input_file, chunk_size)
                    except Exception as e:
                        print(e)


                elif menu2222.get() == "5G_Audio_send":
                    try:
                        def chunk_large_file(input_file, chunk_size):
                            os.makedirs("chunks_Audio", exist_ok=True)
                            for filename in os.listdir("chunks_Audio"):
                                file_path = os.path.join("chunks_Audio", filename)
                                os.remove(file_path)
                            with open(input_file, 'rb') as f:
                                chunk_number = 0
                                while True:
                                    chunk_data = f.read(chunk_size)
                                    print(type(chunk_data))
                                    if not chunk_data:
                                        break
                                    chunk_filename = f"chunk_{chunk_number:.2f}.txt"
                                    with open(os.path.join("chunks_Audio", chunk_filename), 'wb') as chunk_file:
                                        chunk_file.write(chunk_data)
                                        print(chunk_filename)
                                    chunk_number += 0.01
                                    print(chunk_number)
                                files = os.listdir("chunks_Audio")
                                for file in files:
                                    file_path = os.path.join("chunks_Audio", file)
                                    if os.path.isfile(file_path):
                                        with open(file_path, 'rb') as f:
                                            file_contents = f.read()
                                            file_content = list(file_contents)
                                            f.close
                                            data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Audio_send','file_formate':input_file[-4:],'chunk_name':file,
                                            'data':file_content,'file_name':file_name})
                                            size_data = sys.getsizeof(data)
                                            Preamble = config_iot['encryption/decryption']['Preamble']
                                            if Preamble == "3$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble.encode() + msg_len.encode() + encryption(data)
                                                sending1(data)
                                            elif Preamble == "2$@!":
                                                size = hex(size_data)[2:].zfill(4)
                                                msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                                                data = Preamble + msg_len + data
                                                sending1(data.encode())
                                            else:
                                                sending1(Preamble + data)
                        input_file =fd.askopenfilename(filetypes=[('Audio files', '.wav'),('Audio files', '.mp3')])
                        if fn:=re.findall(r"[\w\s-]+\.\w+",input_file):
                        	print(fn)
                        	file_name,formatt=fn[0].split('.')
                        	
                        else:
                        	print("invalid name")
                        chunk_size = 1024*60
                        chunk_large_file(input_file, chunk_size)
                    except Exception as e:
                        print(e)

                elif menu2222.get() == "5G_SMSsend":
                    try:
                        user_sen = "SMS alert from IOT"
                        phone_no_entry = simpledialog.askstring(title='PHONENUMBER', prompt='please enter Number')
                        data = json.dumps(
                            {'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SMSsend', 'message': user_sen,
                             'dest_layer': phone_no_entry})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']

                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['sms_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['sms_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            client_socket.sendall(Preamble+data)
                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>SMS sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()

                elif menu2222.get() == "5G_slice_Request":
                    try:
                        data = json.dumps({'MsgCode': config_iot['msg_code']['slice'],'sst': config_iot[IOTX]['sst'], 'sd': config_iot[IOTX]['sd']})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['slice'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['slice'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            client_socket.sendall(Preamble+data)
                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>SMS sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()

                elif menu2222.get() == "5G_speed":
                    try:
                        text = "AMBR IN NUMBERS AND UNIT IN [bps, kbps, mbps, gbps, tbps]"
                        title = "5G SPEED"
                        input_list = ["AMBR", "UNIT"]
                        output = multenterbox(text, title, input_list)
                        title = "Message Box"
                        message = str(output)
                        my_list_2 = re.findall(r"'([^']*)'", message)
                        speed = my_list_2[0] + my_list_2[1]
                        data = json.dumps({'MsgCode': config_iot['msg_code']['speed'],'QoS': speed})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['speed'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['speed'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            client_socket.sendall(Preamble+data)
                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>SMS sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()

                elif menu2222.get() == "5G_App_service":
                    try:
                        QCI = simpledialog.askstring(title='QCI', prompt="ENTER QCI NUM B/W [1 TO 9] \nCHECK CONFIG FILE FOR REFERENCE")
                        data = json.dumps({'MsgCode': config_iot['msg_code']['app_service'],'QCI': QCI})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['app_service'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['app_service'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            client_socket.sendall(Preamble+data)
                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>SMS sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()

                elif menu2222.get() == "5G_PSM":
                    try:
                        #QCI = simpledialog.askstring(title='QCI', prompt="ENTER QCI NUM B/W [1 TO 9] \nCHECK CONFIG FILE FOR REFERENCE")
                        psm_timer = config_iot[IOTX]['psm_timer']
                        psm_enabled = True
                        data = json.dumps({'MsgCode': config_iot['msg_code']['psm'],"TIMER":"T3324","psm_timer_value":psm_timer})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['psm'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['psm'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            client_socket.sendall(Preamble+data)
                        while psm_enabled:
                            sleep_start_time = time.time()
                            print(f'Going to sleep for {psm_timer} minutes...')
                            while (time.time() - sleep_start_time) < int(psm_timer):
                                time.sleep(int(psm_timer)-1)
                            print(f'Staying active i just completed psm mode')
                            data = json.dumps({'Status':"Active"})
                            sending1(data)
                            psm_enabled = False
                            break
                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>PSM sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()



                elif menu2222.get() == "5G_eDRX":
                    try:
                        #QCI = simpledialog.askstring(title='QCI', prompt="ENTER QCI NUM B/W [1 TO 9] \nCHECK CONFIG FILE FOR REFERENCE")
                        data = json.dumps({'MsgCode': config_iot['msg_code']['edrx']})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['edrx'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['edrx'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            client_socket.sendall(Preamble+data)
                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>SMS sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()


                elif menu2222.get() == "5G_Rereg":
                    try:
                        #QCI = simpledialog.askstring(title='QCI', prompt="ENTER QCI NUM B/W [1 TO 9] \nCHECK CONFIG FILE FOR REFERENCE")
                        data = json.dumps({'MsgCode': config_iot['msg_code']['re_reg']})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['re_reg'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            client_socket.sendall(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['re_reg'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            client_socket.sendall(data.encode())
                        else:
                            client_socket.sendall(Preamble+data)
                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>SMS sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()


                elif menu2222.get() == "5G_Payloadsend":
                    try:
                        user_sen = simpledialog.askstring(title="SMS",
                                                          prompt="Please enter PAYLOAD DATA:")
                        # phone_no_entry = simpledialog.askstring(title='NUMBER', prompt='please enter dest Number')
                        data = json.dumps(
                            {'ueid': config_iot[IOTX]['ueid'], 'command': '5G_Payloadsend', 'message': user_sen})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']

                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            sending1(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            sending1(data.encode())
                        else:
                            sending1(Preamble + data)

                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>Payload sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()


                elif menu2222.get() == "5G_SendfileUP":

                    try:
                        user_sen = simpledialog.askstring(title="IP:PORT",
                                                          prompt="Please enter destination:")
                        filename = fd.askopenfilename()
                        print(filename)
                        f = open(filename, "r")
                        file_data = f.read()
                        f.close()
                        data = json.dumps(
                            {'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SendfileUP', 'data': file_data,
                             'dest_layer': user_sen})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']
                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            sending1(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            sending1(data.encode())
                        else:
                            sending1(Preamble + data)

                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>UP_file data sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()

                elif menu2222.get() == "5G_SendfileCP":

                    try:
                        filename = fd.askopenfilename()
                        print(filename)
                        f = open(filename, "r")
                        file_data = f.read()
                        f.close()
                        data = json.dumps(
                            {'ueid': config_iot[IOTX]['ueid'], 'command': '5G_SendfileCP', 'data': file_data})
                        size_data = sys.getsizeof(data)
                        Preamble = config_iot['encryption/decryption']['Preamble']

                        if Preamble == "3$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble.encode() + msg_len.encode() + encryption(data)
                            sending1(data)
                        elif Preamble == "2$@!":
                            size = hex(size_data)[2:].zfill(4)
                            msg_len = config_iot['msg_code']['files_5g'] + hex(size_data)[2:].zfill(4)
                            data = Preamble + msg_len + data
                            sending1(data.encode())
                        else:
                            sending1(Preamble + data)

                    except Exception as e:
                        print(e)
                    with open(log_file_name, "a") as file_object:
                        file_object.write('>>CP_file data sent')
                        file_object.write('\n')
                        file_object.write("Data to the network is---------->"+ data)
                        file_object.write('\n')
                    Log_prints()


                elif menu2222.get() == "Subscribe":
                    canvas1 = Canvas(ra, width=800, height=200, bg="black")

                    canvas1.create_text(350, 55, text="", fill="midnight blue", font=('Helvetica 15 bold'), width=600)
                    canvas1.pack()
                    canvas1.place(anchor='center', relx=0.65, rely=0.8)

                    s = canvas1.create_text(350, 55,
                                            text=">>Initiated Subscription-" + config_iot['protocol']['web_server'] ,
                                            fill="yellow", font=('Helvetica 15 bold'),
                                            width=600)
                    canvas1.moveto(s, 0.4, 0.63)

                    try:
                        newwindow = Toplevel(ra)
                        def var_states():
                            b = str(var1.get()) + str(var2.get()) + str(var3.get()) + str(var4.get()) + str(
                                var5.get()) + str(var6.get()) + str(var7.get()) + str(var8.get()) + str(
                                var9.get()) + str(var10.get()) + str(var11.get()) + str(var12.get()) + str(
                                var13.get()) + str(var14.get()) + str(var15.get()) + str(var16.get()) + str(
                                var17.get()) + str(var18.get()) + str(var19.get()) + str(var20.get()) + str(
                                var21.get()) + str(var22.get()) + str(var23.get()) + str(var24.get()) + str(
                                var25.get()) + str(var26.get()) + str(var27.get()) + str(var28.get()) + str(
                                var29.get()) + str(var30.get()) + str(var31.get())
                            serial = simpledialog.askstring(title="SERIAL_NO",
                                                            prompt="Please enter SERIAL NUMBER:")
                            data = json.dumps({'serial_number': serial, 'command': 'Subscribe', 'bits': b})
                            size_data = sys.getsizeof(data)
                            data = config_iot['msg_code']['register_5g'] + hex(size_data)[2:].zfill(4) + data
                            Preamble = config_iot['encryption/decryption']['Preamble']

                            if Preamble == "3$@!" :
                                sending1(Preamble.encode() + encryption(data))
                            elif Preamble == "2$@!" :
                                sending1(Preamble + data)
                            else:
                                sending1(Preamble + data)

                        Label(newwindow, text="Feautures opted:").grid(row=0, sticky=W)
                        var1 = IntVar()
                        Checkbutton(newwindow, text="REGISTER_5G", variable=var1).grid(row=1, sticky=W)
                        var2 = IntVar()
                        Checkbutton(newwindow, text="SMS_SEND", variable=var2).grid(row=2, sticky=W)
                        var3 = IntVar()
                        Checkbutton(newwindow, text="PAYLOAD_SEND", variable=var3).grid(row=3, sticky=W)
                        var4 = IntVar()
                        Checkbutton(newwindow, text="5G_FILE_UP", variable=var4).grid(row=4, sticky=W)
                        var5 = IntVar()
                        Checkbutton(newwindow, text="5G_FILE_CP", variable=var5).grid(row=5, sticky=W)
                        var6 = IntVar()
                        Checkbutton(newwindow, text="PHOTO_SEND", variable=var6).grid(row=6, sticky=W)
                        var7 = IntVar()
                        Checkbutton(newwindow, text="AUDIO_SEND_CP", variable=var7).grid(row=7, sticky=W)
                        var8 = IntVar()
                        Checkbutton(newwindow, text="AUDIO_SEND_UP", variable=var8).grid(row=8, sticky=W)
                        var9 = IntVar()
                        Checkbutton(newwindow, text="VIDEO_UP", variable=var9).grid(row=9, sticky=W)
                        var10 = IntVar()
                        Checkbutton(newwindow, text="5G_SMS_SEND", variable=var10).grid(row=10, sticky=W)
                        var11 = IntVar()
                        Checkbutton(newwindow, text="5G_PAYLOAD_SEND", variable=var11).grid(row=11, sticky=W)
                        var12 = IntVar()
                        Checkbutton(newwindow, text="5G_PHOTO_SEND_CP", variable=var12).grid(row=12, sticky=W)
                        var13 = IntVar()
                        Checkbutton(newwindow, text="5G_PHOTO_SEND_UP", variable=var13).grid(row=13, sticky=W)
                        var14 = IntVar()
                        Checkbutton(newwindow, text="IOT_SPECIFIC", variable=var14).grid(row=14, sticky=W)
                        var15 = IntVar()
                        Checkbutton(newwindow, text="DL_SMS_SEND", variable=var15).grid(row=15, sticky=W)
                        var16 = IntVar()
                        Checkbutton(newwindow, text="DL_PAYLOAD_SEND", variable=var16).grid(row=16, sticky=W)
                        var17 = IntVar()
                        Checkbutton(newwindow, text="DL_5G_FILE_UP", variable=var17).grid(row=17, sticky=W)
                        var18 = IntVar()
                        Checkbutton(newwindow, text="DL_5G_FILE_CP", variable=var18).grid(row=18, sticky=W)
                        var19 = IntVar()
                        Checkbutton(newwindow, text="DL_PHOTO_SEND", variable=var19).grid(row=19, sticky=W)
                        var20 = IntVar()
                        Checkbutton(newwindow, text="DL_AUDIO_SEND_CP", variable=var20).grid(row=20, sticky=W)
                        var21 = IntVar()
                        Checkbutton(newwindow, text="DL_AUDIO_SEND_UP", variable=var21).grid(row=21, sticky=W)
                        var22 = IntVar()
                        Checkbutton(newwindow, text="Deregister", variable=var22).grid(row=22, sticky=W)
                        var23 = IntVar()
                        Checkbutton(newwindow, text="UPdate_sensor", variable=var23).grid(row=23, sticky=W)
                        var24 = IntVar()
                        Checkbutton(newwindow, text="UPdate_actuator", variable=var24).grid(row=24, sticky=W)
                        var25 = IntVar()
                        Checkbutton(newwindow, text="sensor_timer", variable=var25).grid(row=25, sticky=W)
                        var26 = IntVar()
                        Checkbutton(newwindow, text="sensor_act", variable=var26).grid(row=26, sticky=W)
                        var27 = IntVar()
                        Checkbutton(newwindow, text="sensor_value", variable=var27).grid(row=27, sticky=W)
                        var28 = IntVar()
                        Checkbutton(newwindow, text="value_actuator", variable=var28).grid(row=2, column=1, sticky=W)
                        var29 = IntVar()
                        Checkbutton(newwindow, text="Refresh_sensor", variable=var29).grid(row=3, column=1, sticky=W)
                        var30 = IntVar()
                        Checkbutton(newwindow, text="Refresh_act", variable=var30).grid(row=4, column=1, sticky=W)
                        var31 = IntVar()
                        Checkbutton(newwindow, text="Data_rate", variable=var31).grid(row=5, column=1, sticky=W)
                        Button(newwindow, text='OK', command=var_states).grid(row=7, column=2, sticky=W, pady=4)


                    except Exception as e:
                        print(e)



                elif menu2222.get() == "MemberReq":
                    canvas1 = Canvas(ra, width=800, height=200, bg="black")

                    canvas1.create_text(350, 55, text="", fill="midnight blue", font=('Helvetica 15 bold'), width=600)
                    canvas1.pack()
                    canvas1.place(anchor='center', relx=0.65, rely=0.8)

                    s = canvas1.create_text(350, 55,
                                            text=">>Initiated MEMBER REQ-" + config_iot['protocol']['web_server'] ,
                                            fill="yellow", font=('Helvetica 15 bold'),
                                            width=600)
                    canvas1.moveto(s, 0.4, 0.63)

                    try:

                        text = "Please Enter the following details"

                        # window title
                        title = "Cientra Gateway 5G"

                        # list of multiple inputs
                        input_list = ["Name", "LastName", "Email", "Mobile Number", "Company", "Serial number",
                                      "Server Protocol", "Server URL"]

                        # list of default text

                        # creating a integer box
                        output = multenterbox(text, title, input_list)

                        # title for the message box
                        title = "Message Box"

                        # creating a message
                        message = str(output)
                        print(message)

                        my_list_2 = re.findall(r"'([^']*)'", message)

                        print(my_list_2)  #
                        print(my_list_2[0])
                        print('init membership')

                        data = json.dumps({'initial': 'initval', 'command': 'Membership', 'Name': my_list_2[0],
                                           'Last name': my_list_2[1], 'Email': my_list_2[2],
                                           'Mobile Number': my_list_2[3], 'Company': my_list_2[4],
                                           'Serial Num': my_list_2[5], 'Server Protocol': my_list_2[6],
                                           'Server URL': my_list_2[7]})

                        size_data = sys.getsizeof(data)
                        data = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4) + data
                        Preamble = config_iot['encryption/decryption']['Preamble']

                        if Preamble == "3$@!" :
                            sending1(Preamble.encode() + encryption(data))
                        elif Preamble == "2$@!" :
                            sending1(Preamble + data)
                        else:
                            sending1(Preamble + data)
                    except Exception as e:
                        print(e)

                elif menu2222.get() == "Ping":
                    canvas1 = Canvas(ra, width=800, height=200, bg="black")

                    canvas1.create_text(350, 55, text="", fill="midnight blue", font=('Helvetica 15 bold'), width=600)
                    canvas1.pack()
                    canvas1.place(anchor='center', relx=0.65, rely=0.8)

                    s = canvas1.create_text(350, 55,
                                            text=">>Initiated PING-" + config_iot['protocol']['web_server'],
                                            fill="yellow", font=('Helvetica 15 bold'),
                                            width=600)
                    canvas1.moveto(s, 0.4, 0.63)

                    try:
                        data = json.dumps({'ueid': config_iot[IOTX]['ueid'], 'command': 'Ping', 'message': 'ping'})
                        size_data = sys.getsizeof(data)
                        data = config_iot['msg_code']['payload_5g'] + hex(size_data)[2:].zfill(4) + data
                        Preamble = config_iot['encryption/decryption']['Preamble']

                        if Preamble == "3$@!" :
                            sending1(Preamble.encode() + encryption(data))
                        elif Preamble == "2$@!" :
                            sending1(Preamble + data)
                        else:
                            sending1(Preamble + data)


                    except Exception as e:
                        print(e)

            menu2222 = StringVar()
            menu2222.set("-features-")
            drop = OptionMenu(ra, menu2222, "5G_SMSsend", "5G_Payloadsend", "5G_SendfileCP", "5G_SendfileUP", "5G_slice_Request", "5G_speed","5G_App_service", "5G_eDRX","5G_Rereg","5G_PSM","5G_Capture_Live_Photo_C",
                              "5G_Capture_Live_Photo_CS",
                              "5G_SendPhoto_S", "5G_Video_send","5G_Audio_send" ,"5G_Audio_Record_send",
                              "Subscribe", "MemberReq", "5G_Deregister", command=command103)
            drop.pack()
            drop.config(width=10)
            drop.place(anchor='center', relx=0.05, rely=0.35)



def socket_type(*args):
    if menu.get() == "WEB_SOCKET":
        globals()["Protocol"]="WEB_SOCKET"
        def Parameters(*args):
            if conf_input.get() == "APN_IP":
                def on_server_selected(event):
                    selected_server = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'apn_ip').split(', ')
                    server_options.remove(selected_server)
                    server_options.insert(0, selected_server)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'apn_ip', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['apn_ip'] = selected_server
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)                    
                    print(f"Selected iot_server: {selected_server}")
                    apn_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'apn_ip').split(', ')
                server_label = Label(ra, text="APN_IP:", fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.65, rely=0.15)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.65, rely=0.18)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)

            elif conf_input.get() == "Aggregator_IP":
                def on_server_selected(event):
                    selected_Aggregator = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'aggregator_ip').split(', ')
                    server_options.remove(selected_Aggregator)
                    server_options.insert(0, selected_Aggregator)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'aggregator_ip', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['aggregator_ip'] = selected_Aggregator
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected Aggregator is: {selected_Aggregator}")
                    Aggregator_IP_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'aggregator_ip').split(', ')
                server_label = Label(ra, text="Aggregator_IP:", fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.75, rely=0.15)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.75, rely=0.18)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)

            elif conf_input.get() == "Core_PLMN":
                def on_server_selected(event):
                    selected_Core = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'core_plmn').split(', ')
                    server_options.remove(selected_Core)
                    server_options.insert(0, selected_Core)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'core_plmn', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['core_plmn'] = selected_Core
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected core is: {selected_Core}")
                    Core_PLMN_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'core_plmn').split(', ')
                server_label = Label(ra, text="Select_Core:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.85, rely=0.15)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.85, rely=0.18)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)

            elif conf_input.get() == "SST":
                def on_server_selected(event):
                    selected_SST = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'sst').split(', ')
                    server_options.remove(selected_SST)
                    server_options.insert(0, selected_SST)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'sst', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['sst'] = selected_SST
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected sst is: {selected_SST}")
                    SST_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'sst').split(', ')
                server_label = Label(ra, text="Select SST:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.95, rely=0.15)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.95, rely=0.18)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)

            elif conf_input.get() == "SD":
                def on_server_selected(event):
                    selected_SD = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'sd').split(', ')
                    server_options.remove(selected_SD)
                    server_options.insert(0, selected_SD)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'sd', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['sd'] = selected_SD
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected SD is: {selected_SD}")
                    SD_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'sd').split(', ')
                server_label = Label(ra, text="Select SD:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.65, rely=0.25)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.65, rely=0.28)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)

            elif conf_input.get() == "company":
                def on_server_selected(event):
                    selected_company = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'company').split(', ')
                    server_options.remove(selected_company)
                    server_options.insert(0, selected_company)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'company', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['company'] = selected_company
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected company is: {selected_company}")
                    company_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'company').split(', ')
                server_label = Label(ra, text="Select company:",fg='white', bg='red', font=("arial italic", 12))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.75, rely=0.25)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.75, rely=0.28)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)
                

            elif conf_input.get() == "serial_number":
                def on_server_selected(event):
                    selected_serial_number = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'serial_number').split(', ')
                    server_options.remove(selected_serial_number)
                    server_options.insert(0, selected_serial_number)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'serial_number', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['serialnumber'] = selected_serial_number
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected serial_number is: {selected_serial_number}")
                    serial_number_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'serial_number').split(', ')
                server_label = Label(ra, text="Select_serial_number:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.85, rely=0.25)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.85, rely=0.28)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)


            elif conf_input.get() == "IMEI":
                def on_server_selected(event):
                    selected_IMEI = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'imei').split(', ')
                    server_options.remove(selected_IMEI)
                    server_options.insert(0, selected_IMEI)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'imei', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['imei'] = selected_IMEI
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected IMEI is: {selected_IMEI}")
                    IMEI_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'imei').split(', ')
                server_label = Label(ra, text="Select_IMEI:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.95, rely=0.25)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.95, rely=0.28)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)

            elif conf_input.get() == "IMSI":
                def on_server_selected(event):
                    selected_IMSI = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'imsi').split(', ')
                    server_options.remove(selected_IMSI)
                    server_options.insert(0, selected_IMSI)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'imsi', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['imsi'] = selected_IMSI
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected IMSI is: {selected_IMSI}")
                    IMSI_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'imsi').split(', ')
                server_label = Label(ra, text="Select IMSI:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.65, rely=0.35)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.65, rely=0.38)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)


            elif conf_input.get() == "GUTI":
                def on_server_selected(event):
                    selected_GUTI = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'guti').split(', ')
                    server_options.remove(selected_GUTI)
                    server_options.insert(0, selected_GUTI)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'guti', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['guti'] = selected_GUTI
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected GUTI is: {selected_GUTI}")
                    GUTI_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'guti').split(', ')
                server_label = Label(ra, text="Select GUTI:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.75, rely=0.35)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.75, rely=0.38)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)


            elif conf_input.get() == "Device_type":
                def on_server_selected(event):
                    selected_Device_type = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'Device_type').split(', ')
                    server_options.remove(selected_Device_type)
                    server_options.insert(0, selected_Device_type)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'Device_type', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['Device_type'] = selected_Device_type
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected Device_type is: {selected_Device_type}")
                    Device_type_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'Device_type').split(', ')
                server_label = Label(ra, text="Select_Device_type:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.85, rely=0.35)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.85, rely=0.38)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)

            elif conf_input.get() == "QCI":
                def on_server_selected(event):
                    selected_QCI = server_var.get()
                    server_options = config_iot.get('Registration_parameters', 'qci').split(', ')
                    server_options.remove(selected_QCI)
                    server_options.insert(0, selected_QCI)
                    updated_servers = ', '.join(server_options)
                    config_iot.set('Registration_parameters', 'qci', updated_servers)
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    config_iot[IOTX]['qci'] = selected_QCI
                    with open('confiot.ini', 'w') as config_file:
                        config_iot.write(config_file)
                    print(f"Selected QCI is: {selected_QCI}")
                    QCI_update()
                server_var = StringVar()
                server_options = config_iot.get('Registration_parameters', 'qci').split(', ')
                server_label = Label(ra, text="Select QCI:",fg='white', bg='red', font=("arial italic", 10))
                server_label.pack(pady=5)
                server_label.place(anchor='center', relx=0.95, rely=0.35)
                server_combobox = ttk.Combobox(ra, textvariable=server_var, values=server_options)
                server_combobox.pack()
                server_combobox.place(anchor='center', relx=0.95, rely=0.38)
                server_var.set(server_options[0])
                server_combobox.bind("<<ComboboxSelected>>", on_server_selected)
            else:
                pass

        conf_input = StringVar()
        conf_input.set("Parameters")
        drop = OptionMenu(ra, conf_input, "APN_IP", "Aggregator_IP", "Core_PLMN","SST", "SD", "company", "serial_number","IMEI","IMSI","GUTI","Device_type","QCI",command=Parameters)
        drop.pack()
        drop.config(width=10)
        drop.place(anchor='center', relx=0.55, rely=0.18)
        cc = Label(ra, text="Change_Parameters", fg='white', bg='red', font=("arial italic", 12))
        cc.pack()
        cc.place(anchor='center', relx=0.55, rely=0.15)
        #update_button = Button(ra, text=config_iot['protocol']['web_server'], command=socket_type)
        #update_button.pack()
        #update_button.place(anchor='center', relx=0.6, rely=0.25)
        print("ws://" + config_iot['protocol']['web_server'])
        connection_flag = False
        while connection_flag == False:
            try:
                globals()["ws_server1"] = create_connection("ws://" + config_iot['protocol']['web_server'],socket = client_socket)
                connection_flag = True
                threading.Thread(target=receiving1, args=(Protocol,)).start()
            except:
                time.sleep(3)
                continue
        sleep(1)
        Login_server()
        #Register_5G()

    elif menu.get() == "MQTT":
        pass        
    elif menu.get() == "TCP":
        pass
    elif menu.get() == "HTTP":
        pass
    else:
        pass

# protocal selection
# IOT
menu1 = StringVar()
menu1.set("UE/IOT")
drop = OptionMenu(ra, menu1, "simulated-iot", "Real-iot",command =Node)
drop.pack()
drop.config(width=10)
drop.place(anchor='center', relx=0.05, rely=0.3)

d = Label(ra, text="UE/IOT", fg='white', bg='red', font=("arial italic", 12))
d.pack()
d.place(anchor='center', relx=0.05, rely=0.27)

conf_input = StringVar()
conf_input.set("Parameters")
def apn_update():
    params = Button(ra, text=config_iot[IOTX]['apn_ip'], fg='white', bg='midnight blue', width=17)
    params.pack()
    params.place(anchor='center', relx=0.05, rely=0.72)
    params=Label(ra, text="APN_IP", fg='midnight blue', font=("arial italic", 12), width=17)
    params.pack()
    params.place(anchor='center', relx=0.05, rely=0.68)
    
def Aggregator_IP_update():
    params = Button(ra, text=config_iot[IOTX]['aggregator_ip'], fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.15, rely=0.72)
    params=Label(ra, text="Aggregator_IP", fg='midnight blue', font=("arial italic", 12),width=17)
    params.pack()
    params.place(anchor='center', relx=0.15, rely=0.68)


def Core_PLMN_update():
    params = Button(ra, text=config_iot[IOTX]['core_plmn'], fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.25, rely=0.72)
    params=Label(ra, text="Core_PLMN", fg='midnight blue', font=("arial italic", 12),width=17 )
    params.pack()
    params.place(anchor='center', relx=0.25, rely=0.68)

def SST_update():
    params = Button(ra, text=config_iot[IOTX]['sst'], fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.35, rely=0.72)
    params=Label(ra, text="SST", fg='midnight blue', font=("arial italic", 12),width=17 )
    params.pack()
    params.place(anchor='center', relx=0.35, rely=0.68)

def SD_update():
    params = Button(ra, text=config_iot[IOTX]['sd'], fg='white', bg='midnight blue', width=17)
    params.pack()
    params.place(anchor='center', relx=0.05, rely=0.80)
    params=Label(ra, text="SD", fg='midnight blue', font=("arial italic", 12), width=17)
    params.pack()
    params.place(anchor='center', relx=0.05, rely=0.77)


def company_update():
    params = Button(ra, text=config_iot[IOTX]['company'], fg='white', bg='midnight blue', width=17)
    params.pack()
    params.place(anchor='center', relx=0.15, rely=0.80)
    params=Label(ra, text="company", fg='midnight blue', font=("arial italic", 12),width=17 )
    params.pack()
    params.place(anchor='center', relx=0.15, rely=0.77)


def serial_number_update():
    params = Button(ra, text=config_iot[IOTX]['serialnumber'], fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.25, rely=0.80)
    params=Label(ra, text="serial_number", fg='midnight blue', font=("arial italic", 12),width=17 )
    params.pack()
    params.place(anchor='center', relx=0.25, rely=0.77)

def IMEI_update():
    params = Button(ra, text=config_iot[IOTX]['imei'], fg='white', bg='midnight blue', width=17)
    params.pack()
    params.place(anchor='center', relx=0.35, rely=0.80)
    params=Label(ra, text="IMEI", fg='midnight blue', font=("arial italic", 12), width=17)
    params.pack()
    params.place(anchor='center', relx=0.35, rely=0.77)


def IMSI_update():
    params = Button(ra, text=config_iot[IOTX]['imsi'], fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.05, rely=0.88)
    params=Label(ra, text="IMSI", fg='midnight blue', font=("arial italic", 12),width=17)
    params.pack()
    params.place(anchor='center', relx=0.05, rely=0.85)

def GUTI_update():
    params = Button(ra, text=config_iot[IOTX]['guti'], fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.15, rely=0.88)
    params=Label(ra, text="GUTI", fg='midnight blue', font=("arial italic", 12),width=17)
    params.pack()
    params.place(anchor='center', relx=0.15, rely=0.85)


def Device_type_update():
    params = Button(ra, text=config_iot[IOTX]['device_type'], fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.25, rely=0.88)
    params=Label(ra, text="Device_type", fg='midnight blue', font=("arial italic", 12),width=17)
    params.pack()
    params.place(anchor='center', relx=0.25, rely=0.85)


def QCI_update():
    params = Button(ra, text="UNDER_DEVELOPMENT", fg='white', bg='midnight blue',width=17)
    params.pack()
    params.place(anchor='center', relx=0.35, rely=0.88)
    params=Label(ra, text="QCI", fg='midnight blue', font=("arial italic", 12),width=17)
    params.pack()
    params.place(anchor='center', relx=0.35, rely=0.85)
   
params = Button(ra, text="PARAMAETERS", fg='white', bg='red')
params.pack()
params.place(anchor='center', relx=0.2, rely=0.6)
apn_update()
Aggregator_IP_update()
Core_PLMN_update()
SST_update()
SD_update()
company_update()
serial_number_update()
IMEI_update()
IMSI_update()
GUTI_update()
Device_type_update()
QCI_update()
def Register_5G():
    try:
        data = json.dumps({'MsgCode': config_iot['msg_code']['register_5g'], 'companyname': config_iot[IOTX]['company'], 'Userid': config_iot[IOTX]['userid'], 'Password': config_iot[IOTX]['password'], 'serialnumber': config_iot[IOTX]['serialnumber'],'devicetype': config_iot[IOTX]['device_type'], 'mcc': config_iot[IOTX]['mcc'], 'mnc': config_iot[IOTX]['mnc'], 'server_ip': config_iot[IOTX]['iot_server']}) #'server_ip': config_iot[IOTX]['iot_server']
        params = Button(ra, text="LOG_PRINTS", fg='white', bg='red',width=17)
        params.pack()
        params.place(anchor='center', relx=0.65, rely=0.58)
        Log_prints()
        size_data = sys.getsizeof(data)
        #message = config_iot['msg_code']['register_5g'] + hex(size_data)[2:].zfill(4) + message
        Preamble = config_iot['encryption/decryption']['Preamble']    
        if Preamble == "3$@!":
            size = hex(size_data)[2:].zfill(4)
            msg_len = config_iot['msg_code']['register_5g'] + hex(size_data)[2:].zfill(4)
            message = Preamble.encode() + msg_len.encode() + encryption(data)
            client_socket.sendall(message)
            print("Registration request: ",message)
        elif Preamble == "2$@!":
            size = hex(size_data)[2:].zfill(4)
            msg_len = config_iot['msg_code']['register_5g'] + hex(size_data)[2:].zfill(4)
            message = Preamble + msg_len + data
            client_socket.sendall(message.encode())
            print("Registration request: ",message.encode())
        else:
            message = Preamble + message
            client_socket.sendall(message.encode())
            print("Registration request: ",message.encode())
        with open(log_file_name, "w") as file_object:
            file_object.write('>>Registration Request sent')
            file_object.write('\n')
            file_object.write("Registration/" + "sent to the network"+data)
            file_object.write('\n')
    except Exception as e:
        print(e)
    response = client_socket.recv(1024).decode()
    message = json.loads(response)
    print(f"Registration response: {message}")
    if message.get("command") == "REGISTRATION ACCEPT":
        ueid = message.get("ueid")
        imsi = message.get("IMSI")
        config_iot[IOTX]['ueid'] = str(ueid)
        config_iot[IOTX]['imsi'] = imsi
        with open("confiot.ini", "w") as f:
            config_iot.write(f)
        IMSI_update()
        with open(log_file_name, "a") as file_object:
            file_object.write('>>Registration response')
            file_object.write('\n')
            file_object.write("Response----->" + "From the Network is"+"----->"+ response)
            file_object.write('\n')
        Log_prints()
        sleep(2)

Conn_aadi = config_iot['msg_code']['Conn_aadi']
print(Conn_aadi)
if Conn_aadi == "True":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((config_iot['protocol']['tcp_ip'], int(config_iot['protocol']['tcp_port'])))
    Register_5G()
    menu = StringVar()
    default_websocket = config_iot['msg_code']['default_WS']
    if default_websocket == "True":
        menu.set("WEB_SOCKET")
        socket_type()
    else:
        menu.set("PROTOCOL/PORT")
        drop = OptionMenu(ra, menu, "WEB_SOCKET", "MQTT", "TCP", "HTTP", command=socket_type)
        drop.pack()
        drop.config(width=18)
        drop.place(anchor='center', relx=0.15, rely=0.18)
        cc = Label(ra, text="protocol_port_selection", fg='midnight blue',bg = "white", font=("arial italic", 12))
        cc.pack()
        cc.place(anchor='center', relx=0.15, rely=0.15)
else:
    connection_flag = False
    while connection_flag == False:
        try:
            globals()["ws_server1"] = create_connection("ws://" + config_iot['protocol']['web_server'])
            connection_flag = True
            Protocol = "WEB_SOCKET"
            threading.Thread(target=receiving1, args=(Protocol,)).start()
            #threading.Thread(target=receiving1).start()
        except:
            print("connection not found! wait...")
            time.sleep(3)
            continue
    sleep(1)
    Login_server()
#client_socket.close()

if __name__ == "__main__":
    ra.mainloop()
    chunks_clean()
