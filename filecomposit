#!/usr/bin/python

import argparse, shutil, pathlib, os

parser = argparse.ArgumentParser(description='Easily compose files together.')
parser.add_argument('--in', dest='idir',
                    default="./",
                    help='Input directory')
parser.add_argument('--out', dest='odir',
                    default="./output",
                    help="Output directory")
parser.add_argument('--exclude', dest='excludes',
                    default=".git", nargs="+",
                    help="Excluded directories and files")
parser.add_argument('--delim', dest='delim',
                    default="—",
                    help="Delimiter")

args = parser.parse_args()

args.idir = os.path.realpath(args.idir)
args.odir = os.path.realpath(args.odir)
args.excludes = [os.path.realpath(os.path.join(args.idir, i)) for i in args.excludes]

if os.path.isdir(args.odir) and len(os.listdir(args.odir)):
    print("Error: output directory is not empty.")
    exit()

if not os.path.isdir(args.idir):
    print("Error: in directory does not exist.")
    exit()

os.makedirs(args.odir, exist_ok=True)

def get_corsp(path):
    return os.path.join(args.odir, os.path.relpath(path, args.idir))

def write_make(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def convert_file(in_path, out_path):
    if os.path.isfile(out_path):
        return
    print(f"{in_path} 🠒 {out_path}")
    
    try:
        with open(in_path, 'r') as f:
            content = f.read().split(args.delim)
    except UnicodeDecodeError:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        shutil.copyfile(in_path, out_path)
        return
    
    out_content = ""
    for i, v in enumerate(content):
        if i % 2 == 0:
            out_content += v
            continue
        
        if v.startswith('/'):
            i_path = os.path.join(args.idir, v[1:])
        else:
            i_path = os.path.join(os.path.dirname(in_path), v)
        
        i_path = os.path.abspath(i_path)
        c_path = get_corsp(i_path)
        
        if not os.path.isfile(c_path):
            convert_file(i_path, c_path)
        
        with open(c_path, 'r') as f:
            out_content += f.read()
    
    write_make(out_path, out_content)
    
    return out_content

def traverse_files(path):
    for p_ in os.listdir(path):
        p = os.path.join(path, p_)
        
        if any(map(pathlib.Path(p).is_relative_to, args.excludes)):
            continue
        
        if os.path.isdir(p):
            traverse_files(p)
        else:
            convert_file(p, get_corsp(p))

traverse_files(args.idir)