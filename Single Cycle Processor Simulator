import argparse
from bitstring import BitArray
from pip._vendor.pyparsing.util import line
from pip._vendor.tomli._parser import Output
from _ast import If

Success = 0
SegFault = 1
RegDst = '0'
ALUSrc = '0'
MemtoReg = '0'
RegWrite = '0'
MemRead = '0'
MemWrite= '0'
Branch = '0'
ALUOp1 = '0'
ALUOp2 = '0'
ZeroBit = '0'
PCounter = 65536
Reg = [0, 0, 0, 0, 0, 0, 0, 0]
Mem = []
Instructions = []

def b2unsigned(imm):
    b=BitArray(bin=imm) #imm is the binary value you wish to change to decimal
    return b.uint

def b2signed(imm):
    b=BitArray(bin=imm) #imm is the binary value you wish to change to decimal
    return b.int


def formatregisters():
    return '%d|%d|%d|%d|%d|%d|%d|%d|%d\n' % (PCounter, Reg[0], Reg[1], Reg[2], Reg[3], Reg[4], Reg[5], Reg[6], Reg[7]) 

def formatcontrols():
    return '%c%c%c%c%c%c%c%c%c%c\n' % (RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp1, ALUOp2, ZeroBit)

def getbits(bits, start, end):
    e=31-end
    s=31-start + 1
    return bits[e:s]

def simulate(input):
    global RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp1, ALUOp2, ZeroBit, PCounter, Reg 
    opcode = getbits(input, 26, 31)
    if opcode == '000000': #R type 
        RegDst = '1'
        ALUSrc = '0'
        MemtoReg = '0'
        RegWrite = '1'
        MemRead = '0'
        MemWrite = '0'
        Branch = '0'
        ALUOp1 = '1'
        ALUOp2 = '0'
        ZeroBit = '0'
        
        function =  getbits(input, 0, 5)
        rd = b2unsigned( getbits(input, 11, 15))
        rt = b2unsigned( getbits(input, 16, 20))
        rs = b2unsigned( getbits(input, 21, 25))
        if function == '100000':
            Reg[rd] = Reg[rs] + Reg[rt]
        elif function == '100010':
            Reg[rd] = Reg[rs] - Reg[rt]
        if Reg[rd] == 0:
            ZeroBit = '1'
        PCounter += 4
        
        
    elif opcode == '001000': #i type addi
        
        RegDst = '0'
        ALUSrc = '1'
        MemtoReg = '0'
        RegWrite = '1'
        MemRead = '0'
        MemWrite = '0'
        Branch = '0'
        ALUOp1 = '0'
        ALUOp2 = '0'
        ZeroBit = '0'
        
        rt = b2unsigned( getbits(input, 16, 20))
        rs = b2unsigned( getbits(input, 21, 25))
        immediate = b2signed( getbits(input, 0, 15))
        Reg[rt] = Reg[rs] + immediate
        if Reg[rt] == 0:
            ZeroBit = '1'
        PCounter += 4
        
    elif opcode == '000100': #i type beq
        
        RegDst = 'X'
        ALUSrc = '0'
        MemtoReg = 'X'
        RegWrite = '0'
        MemRead = '0'
        MemWrite = '0'
        Branch = '1'
        ALUOp1 = '0'
        ALUOp2 = '1'
        ZeroBit = '0'
    
        rt = b2unsigned( getbits(input, 16, 20))
        rs = b2unsigned( getbits(input, 21, 25))
        immediate = b2signed( getbits(input, 0, 15))
        if Reg[rt] == Reg[rs]:
            PCounter += 4 + (immediate * 4)
            ZeroBit = '1'
        else: 
            PCounter += 4
            
    
    elif opcode == '000101': #i type bne
        
        RegDst = 'X'
        ALUSrc = '0'
        MemtoReg = 'X'
        RegWrite = '0'
        MemRead = '0'
        MemWrite = '0'
        Branch = '1'
        ALUOp1 = '1'
        ALUOp2 = '1'
        ZeroBit = '0'
    
        rt = b2unsigned( getbits(input, 16, 20))
        rs = b2unsigned( getbits(input, 21, 25))
        immediate = b2signed( getbits(input, 0, 15))
        if Reg[rt] != Reg[rs]:
            PCounter += 4 + (immediate * 4)
        else: 
            ZeroBit = '1'
            PCounter += 4
    
    elif opcode == '100011': # i type lw
        
        RegDst = '0'
        ALUSrc = '1'
        MemtoReg = '1'
        RegWrite = '1'
        MemRead = '1'
        MemWrite = '0'
        Branch = '0'
        ALUOp1 = '0'
        ALUOp2 = '0'
        ZeroBit = '0'
        
        rt = b2unsigned( getbits(input, 16, 20))
        rs = b2unsigned( getbits(input, 21, 25))
        immediate = b2signed( getbits(input, 0, 15))
        wordaddr = int((Reg[rs] + immediate) / 4) 
        if wordaddr < 0 or wordaddr > len(Mem):
            print("error: segmentation fault")
            return SegFault
        if wordaddr == 0:
            ZeroBit = '1'
        Reg[rt] = Mem[wordaddr]
        PCounter += 4
        
    
    elif opcode == '101011': # i type sw
        
        RegDst = 'X'
        ALUSrc = '1'
        MemtoReg = 'X'
        RegWrite = '0'
        MemRead = '0'
        MemWrite = '1'
        Branch = '0'
        ALUOp1 = '0'
        ALUOp2 = '0'
        ZeroBit = '0'
        
        rt = b2unsigned( getbits(input, 16, 20))
        rs = b2unsigned( getbits(input, 21, 25))
        immediate = b2signed( getbits(input, 0, 15))
        wordaddr = int((Reg[rs] + immediate) / 4)
        if wordaddr < 0 or wordaddr > len(Mem):
            print("error: segmentation fault")
            return SegFault
        if wordaddr == 0:
            ZeroBit = '1'
        Mem[wordaddr] = Reg[rt]
        PCounter += 4
    return Success


def loadInstructions(input):
    with open(input, 'r') as input:
        for line in input:
            Instructions.append(line) 
            

def initializeMemory(memoryfile):
    with open(memoryfile, 'r') as input:
        for line in input:
            if line.strip() == '':
                break
            Mem.append(int(line)) 

def dumpMemory(memoryfile):
    with open(memoryfile, 'w') as output:
        for m in Mem:
            output.write(str(m) + '\n') 


            
def main():
    parser = argparse.ArgumentParser(description='Project 4 Simulator')
    parser.add_argument('input')
    parser.add_argument('memory')
    
    args = parser.parse_args()
    print('simulating binary', args.input, 'memory', args.memory)
    
    
    loadInstructions(args.input)
    initializeMemory(args.memory)
    
    with open('out_control.txt', 'w') as outcontrol: 
        with open('out_registers.txt', 'w') as outregisters: 
            outregisters.write(formatregisters())
            
            while True:
                i = int((PCounter - 65536) / 4)
                if i == len(Instructions): #got to the end
                    break
                elif i < 0 or i > len(Instructions):
                    outcontrol.write('!!! Segmentation Fault !!!\r\n')
                    outregisters.write('!!! Segmentation Fault !!!\r\n')
                    break
                else:
                    error = simulate(Instructions[i])
                    if error == SegFault:
                        outcontrol.write('!!! Segmentation Fault !!!\r\n')
                        outregisters.write('!!! Segmentation Fault !!!\r\n')
                        break   
                    
                    outcontrol.write(formatcontrols())
                    outregisters.write(formatregisters())

            dumpMemory("out_memory.txt")
                  
if __name__ == "__main__":
    main()
    
    
    
