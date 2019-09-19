#!/usr/bin/env python

from __future__ import print_function
import os
import logging
import cv2
import sys
import argparse
import numpy as np
logging.basicConfig(level=logging.INFO)

try:
    wdir = os.path.abspath(sys.argv[1])
except IndexError:
    logging.error("Usage: {} <dir>".format(__file__))
    sys.exit()

logging.info('Workdir: {}'.format(wdir))
for root, dirs, files in os.walk(wdir):
    logging.debug('Current dir: {}'.format(root))
    for f in files:
        full_f = os.path.join(root, f)
        logging.debug(full_f)
        try:
            name, ext = f.rsplit('.')
            if ext != 'bin':
                continue
            target, stype, dist, res, idx = name.split('_')
            width, height = map(int, res.split('x'))
        except ValueError as e:
            logging.error("Failed to split: {}".format(e))
            continue
        if stype == 'YUY2':
            cv2_cspace, depth = cv2.COLOR_YUV2RGB_YUYV, 2
        elif stype == 'IR':
            cv2_cspace, depth = cv2.COLOR_GRAY2RGB, 1
        else:
            logging.debug("Skipping unknown stype {}".format(stype))
            continue
        with open(full_f, 'rb') as fo:
            data = fo.read()
        logging.debug("File size read: {}".format(len(data)))
        rdata = data[:width*height*depth]
        logging.debug("Truncated file size: {}".format(len(rdata)))
        fdata = np.frombuffer(rdata, np.uint8).reshape((height, width, depth))
        logging.debug("img shape: {}".format(fdata.shape))
        img = cv2.cvtColor(fdata, cv2_cspace)
        new_f = os.path.join(os.path.dirname(full_f), name + '.jpg')
        logging.info("Saving {}".format(new_f))
        cv2.imwrite(new_f, img)
