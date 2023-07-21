#!/usr/bin/env python3

import psutil
import shutil
import getpass
import emails
import socket

username = getpass.getuser()

def health_check():
    '''perform healthcheck for cpu, ram, harddisk and network'''
    cpu_usage = int(psutil.cpu_percent(interval=1))
    if cpu_usage >= 80:
        cpu_message()
    ram = psutil.virtual_memory()
    min_ram = 500*1028*1028
    if ram.available <= min_ram:
        ram_message()
    harddisk= psutil.disk_usage('/')
    if harddisk.percent >= 80:
        harddisk_message()
    if socket.gethostbyname("localhost") != "127.0.0.1":
        network_message()

def cpu_message():
    sender = "automation@example.com"
    receiver = username+"@example.com"
    subject = "Error - CPU usage is over 80%"
    body = " Please check your system and resolve the issue as soon as possible."
    message = emails.generate_health(sender, receiver, subject, body)
    emails.send(message)

def harddisk_message():
    sender = "automation@example.com"
    receiver = username+"@example.com"
    subject = "Error - Available disk space is less than 20%"
    body = " Please check your system and resolve the issue as soon as possible."
    message = emails.generate_health(sender, receiver, subject, body)
    emails.send(message)

def ram_message():
    sender = "automation@example.com"
    receiver = username+"@example.com"
    subject = "Error - Available memory is less than 500MB"
    body = " Please check your system and resolve the issue as soon as possible."
    message = emails.generate_health(sender, receiver, subject, body)
    emails.send(message)

def network_message():
    sender = "automation@example.com"
    receiver = username+"@example.com"
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    body = " Please check your system and resolve the issue as soon as possible."
    message = emails.generate_health(sender, receiver, subject, body)
    emails.send(message)

health_check()

                     