"""
Created on Thu April 2 13:21:14 2020

@author: KM Zubair
"""

import random
import csv


# Fieldnames of the columns
fields = ['Wide(Inches)', 'Weight(Pounds)', 'Ram Size(GB)','Ram Type', 'HDD', 'Processor','Battery(mAh)','Camera(MP)','Display','Label']

# Display, Ram size and Ram type of all Devices
display = ['LED','AMOLED','OLED','LTPS-SCREEN','IPS-LCD','IPS']
ram_size = ['2','4','8','16']
ram_type = ['DR2','DDR3','DDR4']

# HDD size for laptop, ThinkPad,IdeaPad,MateBook
hdd_LTIM = ['128GB','256GB','512GB','1TB']

# Camera MP for laptop, ThinkPad,IdeaPad,MateBook
camera_LTIM = ['1.2','1.3','1.9','2.1','3.1','4']

# 1 = Laptop, 2 = ThinkPad, 3 = IdeaPad, 4 = MateBook, 5 = Tablets, 6 = HandSets
def Laptop():
    Wide = round(random.uniform(13, 16),1)
    Weight = round(random.uniform(2, 8), 2)
    Ram = random.choice(ram_size)
    Ram_Type = random.choice(ram_type)
    HDD = random.choice(hdd_LTIM)
    Processor = round(random.uniform(1.6, 3.5), 2)
    Battery = random.randint(2000, 6000)
    Camera = random.choice(camera_LTIM)
    Display = random.choice(display)
    return Wide, Weight, Ram, Ram_Type, HDD, Processor,Battery,Camera, Display, 1


def ThinkPad():
    Wide = round(random.uniform(14, 15.6),1)
    Weight = round(random.uniform(4, 6), 2)
    Ram = random.choice(ram_size)
    Ram_Type = random.choice(ram_type)
    HDD = random.choice(hdd_LTIM)
    Processor = round(random.uniform(2.30, 3.0), 2)
    Battery = random.randint(2500, 4000)
    Camera = random.choice(camera_LTIM)
    Display = random.choice(display)
    return Wide, Weight, Ram, Ram_Type, HDD, Processor,Battery,Camera, Display, 2


def IdeaPad():
    Wide = round(random.uniform(15.6, 16),1)
    Weight = round(random.uniform(2.3, 3), 2)
    Ram = random.choice(ram_size)
    Ram_Type = random.choice(ram_type)
    HDD = random.choice(hdd_LTIM)
    Processor = round(random.uniform(2.3, 3.5), 2)
    Battery = random.randint(2000, 6000)
    Camera = random.choice(camera_LTIM)
    Display = random.choice(display)
    return Wide, Weight, Ram, Ram_Type, HDD, Processor,Battery,Camera, Display, 3

def MateBook():
    Wide = round(random.uniform(13.6, 15.6),1)
    Weight = round(random.uniform(2.9, 3.8), 2)
    Ram = random.choice(ram_size)
    Ram_Type = random.choice(ram_type)
    HDD = random.choice(hdd_LTIM)
    Processor = round(random.uniform(3.7, 4.5), 2)
    Battery = random.randint(3600, 5000)
    Camera = random.choice(camera_LTIM)
    Display = random.choice(display)
    return Wide, Weight, Ram, Ram_Type, HDD, Processor,Battery,Camera, Display, 4

def Tablets():
    hdd_tablets = ['16GB','32GB','64GB']
    camera_tablets = ['1.3','2','3','4','6','8','10','12','13']
    processor_tablets = ['1.3','1.5','1.8','2.36']
    Wide = round(random.uniform(9.7, 12),1)
    Weight = round(random.uniform(0.7, 1.8), 2)
    Ram = random.choice(ram_size)
    Ram_Type = random.choice(ram_type)
    HDD = random.choice(hdd_tablets)
    Processor = random.choice(processor_tablets)
    Battery = random.randint(2500, 5000)
    Camera = random.choice(camera_tablets)
    Display = random.choice(display)
    return Wide, Weight, Ram, Ram_Type, HDD, Processor,Battery, Camera,Display, 5

def HandSets():
    hdd_handsets = ['16GB','32GB','64GB','128GB']
    processor_handsets = ['1.3','1.5','1.8','2.36','2.5','2.96']
    camera_handsets = ['1.3','2','3','4','6','8','10','12','13','16','32','48','108']
    Wide = round(random.uniform(3, 5.6),1)
    Weight = round(random.uniform(0.130, 0.190), 3)
    Ram = random.choice(ram_size)
    Ram_Type = random.choice(ram_type)
    HDD = random.choice(hdd_handsets)
    Processor = random.choice(processor_handsets)
    Battery = random.randint(600, 4000)
    Camera = random.choice(camera_handsets)
    Display = random.choice(display)
    return Wide, Weight, Ram, Ram_Type, HDD, Processor,Battery,Camera,Display, 6


# array to store them
data = []

# generate 1500 records of each
iternum = 1500
while iternum > 0:
    laptop = Laptop()
    data.append(laptop)
    thinkpad = ThinkPad()
    data.append(thinkpad)
    ideapad = IdeaPad()
    data.append(ideapad)
    matebook = MateBook()
    data.append(matebook)
    tablets = Tablets()
    data.append(tablets)
    handsets = HandSets()
    data.append(handsets)
    iternum -= 1




# give filename
# PLEASE CHANGE THE FILE LOCATION ACCODING TO YOUR PREFERENCE WHILE RUNNING THIS CODE
filename = "G:\Sem 2\IS CSC 2301 Section 02\QUIZ 2\quiz2\KMZubair\FILE.csv"

with open(filename, 'w', newline='') as csvfile:
    # create writer object
    csvwriter = csv.writer(csvfile)

    # write the fields
    csvwriter.writerow(fields)

    # write data to file
    for eachdata in data:
        csvwriter.writerow(eachdata)
