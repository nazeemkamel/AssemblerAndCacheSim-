import argparse
import math
from pkg_resources._vendor.jaraco.context import null
from pip._vendor.packaging.markers import Undefined

cache = {}

def hex_to_binary(hex_string):
    """
    Convert a hexadecimal string to a binary string.
    """
    # Convert the hex string to an integer
    decimal_num = int(hex_string, 16)
    
    # Convert the decimal number to a binary string
    binary_string = format(decimal_num, 'b').zfill(32)
    
    return binary_string


def format_output(address, tag_bits, index_bits, hit_code):
    return address + '|' + tag_bits + '|' + index_bits + '|' + hit_code + '\n'


def cacheProcessor(hexAddress, nway):
    global n
    global m
    global cache
    binAddress = hex_to_binary(hexAddress)
    tag_len = int(32 - (n + m + 2))
    tag_bits = binAddress[0:tag_len] 
    index_bits = binAddress[tag_len:int(tag_len + n)]
    if binAddress[30:32] != '00':
        return hexAddress, tag_bits, index_bits, 'U'
    set = cache.get(index_bits)
    if set == None:
        cache[index_bits] = [tag_bits]
        return hexAddress, tag_bits, index_bits, 'M' 
    elif tag_bits in set:
        return hexAddress, tag_bits, index_bits, 'H'
    else:
        if len(set) == nway:
            set.pop(0)
        set.append(tag_bits)
        return hexAddress, tag_bits, index_bits, 'M'


def main():
    
    parser = argparse.ArgumentParser(description='Project 5')
    parser.add_argument('--type', required = True, choices= ['d', 's'], help='type of cache, either direct or set associative')
    parser.add_argument('--nway', required = False, type = int, help= 'number of ways, required for set associative')
    parser.add_argument('--cache_size', required = True, type = int, help= 'total cache size in bytes, must be power of two')
    parser.add_argument('--block_size', required = True, type = int, help= 'total block size in bytes, must be power of two')
    parser.add_argument('--memfile', required = True, help= 'input text file memory address in hexadecimal')

    
    args = parser.parse_args()
    
    if args.type == 's' and args.nway is None:
        print("ERROR: missing nway parameter")
        exit(-1)
    
    global n
    global m
    x = math.log2(args.cache_size)
    m = math.log2(args.block_size)
    n = x - m
    m = m - 2
    
    if not n.is_integer():
        print("ERROR: invalid cache size")
        exit(-1)

    if not m.is_integer():
        print("ERROR: invalid block size")
        exit(-1)
    
    if args.type == 'd':
        args.nway = 1
    
    hits = 0
    instructions = 0
    with open(args.memfile, 'r') as input: 
        with open('cache.txt', 'w') as output: 
             
            for line in input:
                address, tag_bits, index_bits, hit_code = cacheProcessor(line.strip(), args.nway)
                out = format_output(address, tag_bits, index_bits, hit_code)
                output.write(out)
                instructions += 1
                if hit_code == 'H':
                    hits += 1
            output.write(format("\n hit rate: %.1f\n" % ((hits/instructions) * 100)))
            
if __name__ == "__main__":
    main()
        
