"""
This file converts any given file of assembly into machine code 
then outputs the machine code in a different file by splitting the command from the variables, 
then searching thru dictionaries for their machine code variants
"""

import argparse
import re
from _socket import error

outputFile = "out_code.txt"

RType = ("add", "sub", "sll", "srl", "slt")
IType = ("addi", "beq", "bne", "lw", "sw")

Args_rd_rs_rt = ("add", "sub", "slt")
Args_rd_rt_ra = ("sll", "srl")
Args_rt_rs_imm = ("addi")
Args_rs_rt_imm = ("beq", "bne")
Args_rt_imm_rs = ("lw", "sw")

functionCode = {
    "add": "100000",
    "sub": "100010",
    "sll": "000000",
    "srl": "000010",
    "slt": "101010",
    }
opCode = {
    "addi": "001000",
    "beq":  "000100",
    "bne":  "000101",
    "lw":   "100011",
    "sw":   "101011",
    }
registers = {
    "$1": "00000",
    "$1": "00001",
    "$2": "00010",
    "$2": "00011",
    "$2": "00100",
    "$2": "00101",
    "$2": "00110",
    "$2": "00111",
    "$1": "01000",
    "$1": "01001",
    "$2": "01010",
    "$2": "01011",
    "$2": "01100",
    "$2": "01101",
    "$2": "01110",
    "$2": "01111",
    "$1": "10000",
    "$1": "10001",
    "$2": "10010",
    "$2": "10011",
    "$2": "10100",
    "$2": "10101",
    "$2": "10110",
    "$2": "10111",
    "$1": "11000",
    "$1": "11001",
    "$2": "11010",
    "$2": "11011",
    "$2": "11100",
    "$2": "11101",
    "$2": "11110",
    "$2": "11111",
    }


errorMsg = "!!! Invalid Input !!!"

#         return format(regN, "05b")
def getRegister(str): #given string returns the registernumber
    if str[0]!= '$':
        return -1
    regN = -1
    if len(str) > 1 and str[1].isdigit():
        regN = int(str[1:])
        if regN < 0 or regN > 31:
            return -1
        return regN
    if str == "$zero":
        return 0
    if str == "$at":
        return 1
    if str == "$gp":
        return 28
    if str == "$sp":
        return 29
    if str == "$fp":
        return 30
    if str == "$ra":
        return 31
    if len(str) > 2:
        if str[1] == 'v':
            regN = int(str[2:])
            if regN >= 0 and regN <= 1:
                return regN + 2
            return -1
        if str[1] == 'a':
            regN = int(str[2:])
            if regN >= 0 and regN <= 3:
                return regN + 4
            return -1
        if str[1] == 't':
            regN = int(str[2:])
            if regN >= 0 and regN <= 7:
                return regN + 8
            if regN >= 8 and regN <= 9:
                return regN + 16
            return -1
        if str[1] == 's':
            regN = int(str[2:])
            if regN >= 0 and regN <= 7:
                return regN + 16
            return -1
        if str[1] == 'k':
            regN = int(str[2:])
            if regN >= 0 and regN <= 1:
                return regN + 26
            return -1

    return -1

def formatRType(rs, rt, rd, ra, cmd):  #determines 
    rsID = getRegister(rs)
    rtID = getRegister(rt)
    rdID = getRegister(rd)
    raID = getRegister(ra)
    if rsID == -1 or rtID == -1 or rdID == -1 or raID == -1 or cmd not in functionCode:
        return errorMsg
    return "000000" + format(rsID, "05b") + format(rtID, "05b") + format(rdID, "05b") + format(raID, "05b") + functionCode[cmd]

def parseImmediate(str):
    if str[0] == '-':
        return ~int(str[1:]) + 1
    return int(str)
    
    
def formatIType(cmd, rs, rt, imm):
    rsID = getRegister(rs)
    rtID = getRegister(rt)

    if rsID == -1 or rtID == -1 or cmd not in opCode or imm < -32768 or imm > 32767:
        return errorMsg
    
    return opCode[cmd] + format(rsID, "05b") + format(rtID, "05b") + format(0xFFFF & imm, "016b")

def compile(str):
    cmd=''
    args=()
    str = str.strip()
    if str[0] == '#':
        return ""
    
    parts = str.split() 
    if len(parts) != 2:
        return errorMsg
    cmd = parts[0]
    args = parts[1].strip().split(",")
    if cmd in RType:
        if cmd in Args_rd_rs_rt:
            if len(args) != 3:
                return errorMsg
            return formatRType(args[1], args[2], args[0], "$zero", cmd)
        if cmd in Args_rd_rt_ra:
            if len(args) != 3:
                return errorMsg
            return formatRType("$zero", args[1], args[0], args[2], cmd)
        return errorMsg
    
    
    if cmd in IType:
        if cmd in Args_rt_rs_imm:
            if len(args) != 3:
                return errorMsg
            return formatIType(cmd, args[1], args[0], parseImmediate(args[2]))
        if cmd in Args_rs_rt_imm:
            if len(args) != 3:
                return errorMsg
            return formatIType(cmd, args[0], args[1], parseImmediate(args[2]) >> 2)
        if cmd in Args_rt_imm_rs:
            if len(args) != 2:
                return errorMsg
            m = re.match(r'^(-?\d+)\((.*)\)$', args[1])
            if not m:
                return errorMsg
            rs = m.groups()[1]
            imm = m.groups()[0]
            return formatIType(cmd, rs, args[0], parseImmediate(imm))
        
        return errorMsg               

    return errorMsg               
    
    

def main():
    parser = argparse.ArgumentParser(description='MIPS Translator')
    parser.add_argument('--input', required = True, help='the file to be translated')

    args = parser.parse_args()
    print('translating', args.input)
    print('into file ', outputFile) 
       
    with open(args.input, 'r') as input: 
        with open(outputFile, 'w') as output:  
            for line in input:
                out = compile(line.strip())               
                output.write(out)
                output.write('\n')
                if out == errorMsg:
                    print(errorMsg)
                    break

if __name__ == "__main__":
    main()
    
    
