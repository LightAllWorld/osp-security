#!/bin/python3
# -*- coding: utf-8 -*-
# Author -> Jude Park

import os
import sys
import subprocess as sp
import numpy as np

extract_type = sys.argv[1]

if (extract_type == 'normal'):
    file_extension = sys.argv[2] # Normal Files 일 경우 dll 과 exe 로 파일 확장자가 나뉨
    normal_file_path = os.listdir('/home/dainelpark/NormalFiles/{}/'.format(file_extension))

    for i in normal_file_path:
        result = sp.check_output(['python2.7', '/home/dainelpark/Security/peframe/peframe.py', '/home/dainelpark/NormalFiles/{}/{}'.format(sys.argv[2], i)])

        print(result)

elif (extract_type == 'malware'):
    malware_file_path = os.listdir('/home/dainelpark/malware_pe/')

    for i in malware_file_path:
        result = sp.check_output(['python2.7', '/home/dainelpark/Security/peframe/peframe.py', '/home/dainelpark/malware_pe/{}'.format(i)])

        print(result)
