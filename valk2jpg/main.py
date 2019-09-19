import argparse
import cv2
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-o', '--output')
    parser.add_argument('-r', '--recursive', action='store_true')
    args = parser.parse_args()

def main():
    args = get_args()
