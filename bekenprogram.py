#!/usr/bin/env python3
import sys
import os
import argparse
import bkutils

chip_map = {
    "bk7231": bkutils.CHIP_TYPE_BK7231,
    "bk7231u": bkutils.CHIP_TYPE_BK7231U,
    "bk7221u": bkutils.CHIP_TYPE_BK7221U,
    "bk7251": bkutils.CHIP_TYPE_BK7251,
}

def parse_args():
    description = '''Beken HID Downloader.'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-c', '--chip',
                        default='bk7231u',
                        choices=chip_map.keys(),
                        help="chip type")
    parser.add_argument('filename',
                        help='specify file_crc.bin')
    args = parser.parse_args()

    return args

def show_all_chips():
    print("Available:")
    for c in chip_map.keys():
        print("\t{}".format(c))
    sys.exit(-1)

args = parse_args()
filename = args.filename
chip_type = args.chip
if chip_type not in chip_map:
    print("Cannot find chip: {}".format(chip_type))
    show_all_chips()
if not os.path.exists(filename):
    print("file: {} not exist".format(filename))
    sys.exit(-1)

downloader = bkutils.HidDownloader(chip_map[chip_type])
downloader.Download(filename)