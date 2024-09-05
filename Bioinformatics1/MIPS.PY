mips = {
    'type': {
        'ADD': 'R',
        'ADDI': 'I',
        'ADDIU' : 'I',
        'ADDU': 'R',
        'AND': 'R',
        'ANDI' : 'I',
        'BEQ': 'I',
        'BNE': 'I',
        'J' : 'J',
        'JAL': 'J',
        'JR': 'R',
        'LBU' : 'I',
        'LHU': 'I',
        'LL': 'I',
        'LUI' : 'I',
        'LW': 'I',
        'NOR': 'R',
        'OR' : 'R',
        'ORI': 'I',
        'SLT': 'R',
        'SLTI' : 'I',
        'SLTIU' : 'I',
        'SLTU': 'R',
        'SLL': 'R',
        'SRL' : 'R',
        'SB': 'I',
        'SC': 'I',
        'SH' : 'I',
        'SW': 'I',
        'SUB': 'R',
        'SUBU' : 'R',
    },
    'opcode': {
        'ADD': '0',
        'ADDI': '8',
        'ADDIU' : '9',
        'ADDU': '0',
        'AND': '0',
        'ANDI' : 'c',
        'BEQ': '4',
        'BNE': '5',
        'J' : '2',
        'JAL': '3',
        'JR': '0',
        'LBU' : '24',
        'LHU': '25',
        'LL': '30',
        'LUI' : 'f',
        'LW': '23',
        'NOR': '0',
        'OR' : '0',
        'ORI': 'd',
        'SLT': '0',
        'SLTI' : 'a',
        'SLTIU' : 'b',
        'SLTU': '0',
        'SLL': '0',
        'SRL' : '0',
        'SB': '28',
        'SC': '38',
        'SH' : '29',
        'SW': '2b',
        'SUB': '0',
        'SUBU' : '0',
    },
    'funct': {
        'ADD': '20',
        'ADDU': '21',
        'AND': '24',
        'JR': '8',
        'NOR': '27',
        'OR' : '25',
        'SLT': '2A',
        'SLTU': '2B',
        'SLL': '0',
        'SRL' : '2',
        'SUB': '22',
        'SUBU' : '23',
    },
    'res': {
        '$zero': 0,
        '$at': 1,
        '$v0': 2,
        '$a0': 4,
        '$t0': 8,
        '$s0': 16,
        '$t8': 24, 
        '$k0': 26,
        '$gp': 28,
        '$sp': 29,
        '$fp': 30,
        '$ra': 31
    }
}
#ham lay loai 
def get_type(st):
    return mips['type'].get(st.upper(), 'Khong co')

#ham lay funct
def get_funct(st):
    return mips['funct'].get(st.upper(), 'Khong co')

#ham lay opcode
def get_op(st):
    return mips['opcode'].get(st.upper(), 'Khong co')

#ham lay vt so dau tien cua string, neu khong co xuat ra do dai string
def xuly_res(st):
    tmp = ''
    for i in st:
        if (i >= '0' and i <= '9'):
            return st.find(i)
    return len(st)

#ham doi thanh ghi ra so tuong ung
def get_NumRes(st):
    vt = xuly_res(st)

    #Neu phia trc so la $ thi thanh ghi do co dang $0-$31
    if(st[ : vt] == '$'):
        return int(st[vt : ])

    num = 0
    #thanh ghi nay co so o cuoi
    if (vt != len(st)):
        num = int(st[vt : ])
    
    #check xem co phai thanh ghi $t8-$t9 ko
    #lay thanh ghi dau tien cua khoang thanh ghi
    if(st[ : vt] == '$t' and num >= 8):
        st = '$t8'
    else :
        st = st[ : vt] if vt == len(st) else st[ : vt] + '0'
    
    #lay id dau tien cua khoang thanh ghi
    id = mips['res'].get(st, 'Khong co')

    #So thanh ghi = so thanh ghi do + thanh ghi dau tien cua khoang
    if (id != 'Khong co'):
        if(st == '$t8'):
            id = int(mips['res'][st]) + num - 8
        else:
             id = int(mips['res'][st]) + num
    return id