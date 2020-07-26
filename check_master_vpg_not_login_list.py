#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import pandas as pd

file_path = "/home/ubuntu/"
master = "m3"

def check_master_vpg_not_login_list():
    csv_file = file_path + master + "_vpg_not_login_list.csv"
    master_vpg_not_login_list = pd.read_csv(csv_file)
    error_msg = "4:4:"

    if (len(master_vpg_not_login_list) == 0):
        print ("0:0:OK")
    else:
        for index in range(len(master_vpg_not_login_list)):
            error_msg = error_msg+master_vpg_not_login_list['p2p_domain'][index]+".tutk.com_"+master_vpg_not_login_list['vid'][index]+":"+master_vpg_not_login_list['pid'][index]+":"+master_vpg_not_login_list['gid'][index]+"/"
        
        print (error_msg)


if __name__ == "__main__":
    check_master_vpg_not_login_list()
