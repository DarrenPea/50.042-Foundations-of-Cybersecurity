#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.042 FCS

import argparse

def getInfo(headerfile):
    with open(headerfile, mode='rb') as h:
        information = h.read()
    return information

def extract(infile, outfile, headerfile):
    headerInformation = getInfo(headerfile)
    with open(infile, mode='rb') as i:
        i.seek(len(headerInformation) + 1)  # skip header information
    
        byte_ls = {}
        while True:
            byte = i.read(8)
            if not byte:
                break
            elif byte in byte_ls:
                byte_ls[byte] += 1
            else:
                byte_ls[byte] = 1

    maximum = max(byte_ls.values())
    for k,v in byte_ls.items():
        if v == maximum:
            common = k
        
    # replace most common byte as 0, rest is 1
    with open(outfile, mode='wb') as o, open(infile, mode='rb') as i:
        o.write(headerInformation)
        o.write(b'\n')
        i.read(len(headerInformation) + 1)
        
        while True:
            byte = i.read(8)
            if byte == b'':
                break
            elif byte == common:
                o.write(b'00000000')
            else:
                o.write(b'11111111')

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    success=extract(infile,outfile,headerfile)

            
