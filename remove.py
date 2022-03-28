import os
import random


file_list = os.listdir("noise")
random.shuffle(file_list)
for file_ in file_list[10000:]:
    os.remove("noise/" + file_)