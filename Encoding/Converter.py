import Base64Encoder
import UrlEncoder
import BinaryEncoder
import argparse


# initiate the parser
parser = argparse.ArgumentParser()

# General Arguments
parser.add_argument("string", help="the string to be encoded/decoded")
parser.add_argument("--decode", "-d", help="Decode the string", action='store_true')

# Converter Arguments
parser.add_argument("--base64", "-b64", help="String <==> Base64", action='store_true')
parser.add_argument("--url", "-u", help="String <==> Url", action='store_true')
parser.add_argument("--binary", "-b", help="String <==> Binary", action='store_true')


# read arguments from the command line
args = parser.parse_args()

# check for --width
if args.base64:  
    if args.decode:
        print(Base64Encoder.decode(args.string))
    else:
        print (Base64Encoder.encode(args.string))


if args.url:  
   
    if args.decode:
        print(UrlEncoder.decode(args.string))
    else:
        print (UrlEncoder.encode(args.string))

if args.binary:  
    if args.decode:
        print(BinaryEncoder.decode(args.string))
    else:
        print (BinaryEncoder.encode(args.string))