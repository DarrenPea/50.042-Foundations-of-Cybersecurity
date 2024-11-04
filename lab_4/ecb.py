#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS

from present import *
import argparse

nokeybits=80
blocksize=64

def split_plaintext_bytes(data):
    if len(data) % 8 != 0:
        data += b'\x00' * (8 - len(data) % 8) # padding with null bytes
    
    chunks = [int.from_bytes(data[i:i+8], byteorder="big") for i in range(0, len(data), 8)]
    return chunks

def ecb(infile,outfile,key,mode):
    with open(infile, 'rb') as f:
        file_data = f.read()

    data_chunks = split_plaintext_bytes(file_data)

    processed_chunks = []
    
    if mode.lower() == 'e':
        for chunk in data_chunks:
            processed_chunks.append(present(chunk, key))

    elif mode.lower() == 'd':
        for chunk in data_chunks:
            processed_chunks.append(present_inv(chunk, key))
    
    with open(outfile, 'wb') as f:
        for chunk in processed_chunks:
            f.write(chunk.to_bytes(8, byteorder='big'))
        
if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file, text in .txt should be e.g. 0xFFFFFFFFFFFFFFFFFFFF')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode = args.mode

    ## use keyfile_test for keyfile
    with open(keyfile, mode='r') as f:
        key_data = f.read()
        if key_data.startswith("0x"):
            key = int(key_data, 16)
        else:
            key = int(key_data)

    ecb(infile, outfile, key, mode)

