from MIPS import *
#===============================================
def HextoBin(st):
    num = int(st, 16)
    return format(num, 'b')

#===============================================
def DectoBin(st):
    num = int(st)
    string = ''
    if num < 0:
        num = (1 << 16) + num
    return format(num, 'b')

#===============================================
def BintoHex(st):
    i = 0
    res = ''
    while(i < len(st)):
        decc = int(st[i : i + 4], 2)
        res += format(decc, 'x')
        i += 4
    return res
#===============================================
def is_number(st):
    return st.isdigit() or (st.startswith('-') and st[1:].isdigit())

#===============================================
def Xuly_R(tmp):
    opcode = get_op(tmp[0])
    funct = get_funct(tmp[0])

    rd = 0
    rs = 0
    rt = 0
    shamt = 0
    res = HextoBin(opcode).zfill(6)

    if len(tmp) == 4:
        rd = int(get_NumRes(tmp[1]))
        if(tmp[3][0] != '$'):
            rt = int(get_NumRes(tmp[2]))
            shamt = int(tmp[3])
            rs = 0
        else :
            rs = int(get_NumRes(tmp[2]))
            rt = int(get_NumRes(tmp[3]))
    elif len(tmp) == 2:
        rs = int(get_NumRes(tmp[1]))
    res += DectoBin(rs).zfill(5) + DectoBin(rt).zfill(5) + DectoBin(rd).zfill(5) + DectoBin(shamt).zfill(5) + HextoBin(funct).zfill(6)

    return BintoHex(res)
#===============================================
def fill(string, check):
    while(len(string) <  16):
        string = check + string
    return string

#===============================================
def Xuly_I(tmp, vt):
    opcode = get_op(tmp[0])
    res = HextoBin(opcode).zfill(6)
    length = len(tmp)
    rs = 0
    rt = 0
    immediate = 0

    rt = int(get_NumRes(tmp[1]))

    if(is_number(tmp[length - 1])):
        immediate = int(tmp[length - 1])
        rs = int(get_NumRes(tmp[2]))
    elif(len(tmp) == 3):
        vt1 = tmp[2].find('(')
        vt2 = tmp[2].find(')')
        rs = int(get_NumRes(tmp[2][vt1 + 1 : vt2]))
        if(vt1 == 0):
            immediate = 0
        else:
            immediate = int(tmp[2][: vt1])
    elif(tmp[0] == 'beq' or tmp[0] == 'bne'):
        rs = int(get_NumRes(tmp[1]))
        rt = int(get_NumRes(tmp[2]))
        immediate = (address[tmp[3] + ':'] - vt) - 4
        immediate = int(immediate / 4) # bo 2 bit 0 o cuoi
    
    res += DectoBin(rs).zfill(5) + DectoBin(rt).zfill(5) + fill(DectoBin(immediate), '1' if immediate < 0 else '0')
    return BintoHex(res)

#===============================================
def Xuly_J(tmp):
    opcode = get_op(tmp[0])
    res = HextoBin(opcode).zfill(6)

    jumpAddr = '0400000'
    string = format(address[tmp[1] + ':'], 'x')
    lenn = len(string)
    jumpAddr = jumpAddr[: len(jumpAddr) - lenn] + string
    
    for s in jumpAddr:
        res += format(int(s), 'b').zfill(4)
    return (BintoHex(res[:len(res) - 2]))

#===============================================
def Xuly(st):
    tmp = [s.replace(',', '') for s in list(st.split())]
    type = get_type(tmp[0])

    if type == 'R':
        return Xuly_R(tmp)   
    elif type == 'I':
        return Xuly_I(tmp, address[st])
    elif type == 'J':
        return Xuly_J(tmp)
    else:
        return '0'

#===============================================
fi = open('input.asm', 'r')
fo = open('bin', 'w')

data = [s.replace('\n', '') for s in list(fi)]
fi.close()

BD = '0x00400000'
address ={}
addr = 0
for ls in data:
    if ls != '':
        if ls.endswith(':') == False:
            address.update({ls : addr})
            addr += 4
        else:
            address.update({ls : addr})

for ls in data:
    if(ls != ''):
        result = Xuly(ls)
        if(result != '0'):
            fo.write(result + '\n')
fo.close()