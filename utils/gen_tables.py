# Gen Tables
# 장기 위치별 이동가능 위치를 방향별로 미리 구해놓는다.
# 임시 프로그램

import pprint


# 비트 위치
LL = 1
UU = 2
RR = 4
DD = 8
LU = 16
RU = 32
RD = 64
DL = 128

# 인덱스
I_LL = 0
I_UU = 1
I_RR = 2
I_DD = 3
I_LU = 4
I_RU = 5
I_RD = 6
I_DL = 7



##########
#  4 1 5
#  0   2
#  7 3 6
#
# Left    -> Up       -> Right      -> Down      -> 
# Left_up -> Right_up -> Right_down -> Left_down
# 위 순서대로 방향을 정함
# (대각선 방향은 개수가 적다.)



link_map = [] # 연결 맵

# 장기 판의 그어진 선 그대로 연결된 방향 맵


for i in range(90):
    r = i // 9
    c = i % 9
    
    cell = LL + UU + RR + DD 

    # 판 경계지점에서 비트 Off
    if r == 0:
        cell &= ~UU
    if r == 9:
        cell &= ~DD
    if c == 0:
        cell &= ~LL
    if c == 8:
        cell &= ~RR
    
    # 궁성에서 비트 On
    if (r == 0 and c == 3) or (r == 7 and c == 3):
        cell |= RD
    if (r == 0 and c == 5) or (r == 7 and c == 5):
        cell |= DL
    if (r == 1 and c == 4) or (r == 8 and c == 4):
        cell |= (LU + RU + RD + DL)
    if (r == 2 and c == 3) or (r == 9 and c == 3):
        cell |= RU
    if (r == 2 and c == 5) or (r == 9 and c == 5):
        cell |= LU
    
    link_map.append(cell)


# 연결 맵 출력
def print_link_map():
    for i in range(90):
        r = i // 9
        c = i % 9
        #print( format(link_map[i], '08b') + '  ', end='')
        print( format(link_map[i], '#04x') + ', ' , end='')
        if c == 8: 
            print('')


#print_link_map()




## 궁성 맵 : 궁성 안에서만 연결된 맵 정의
gung_map = []


for i in range(90):
    r = i // 9
    c = i % 9
    
    cell = 0

    if (r == 0 and c == 3) or (r == 7 and c == 3):
        cell = RR + RD + DD
    if (r == 0 and c == 4) or (r == 7 and c == 4):
        cell = LL + RR + DD
    if (r == 0 and c == 5) or (r == 7 and c == 5):
        cell = LL + DD + DL

    if (r == 1 and c == 3) or (r == 8 and c == 3):
        cell = UU + RR + DD
    if (r == 1 and c == 4) or (r == 8 and c == 4):
        cell = LL + UU + RR + DD + LU + RU + RD + DL
    if (r == 1 and c == 5) or (r == 8 and c == 5):
        cell = LL + UU + DD
    
    if (r == 2 and c == 3) or (r == 9 and c == 3):
        cell = UU + RU + RR
    if (r == 2 and c == 4) or (r == 9 and c == 4):
        cell = LL + UU + RR
    if (r == 2 and c == 5) or (r == 9 and c == 5):
        cell = LL + LU + UU
    
    
    gung_map.append(cell)


# 궁성맵 출력
def print_gung_map():
    print('')
    for i in range(90):
        r = i // 9
        c = i % 9
        #print( format(gung_map[i], '08b') + '  ', end='')
        print( format(gung_map[i], '#04x') + ', ' , end='')
        if c == 8: 
            print('')


#print_gung_map()




## 점프맵: 뛰는기물 (마, 상)의 맵
jump_map = []


for i in range(90):
    r = i // 9
    c = i % 9
    
    # 모든 방향을 킨다.
    cell = LL + UU + RR + DD + LU + RU + RD + DL 

    # 경계지점에서 bit off
    if r == 0:
        cell &= ~UU
        cell &= ~LU
        cell &= ~RU
    if r == 9:
        cell &= ~DD
        cell &= ~DL
        cell &= ~RD
    if c == 0:
        cell &= ~LL
        cell &= ~LU
        cell &= ~DL
    if c == 8:
        cell &= ~RR
        cell &= ~RU
        cell &= ~RD

    jump_map.append(cell)


# 점프맵 출력
def print_jump_map():
    print('')
    for i in range(90):
        r = i // 9
        c = i % 9
        #print( format(jump_map[i], '08b') + '  ', end='')
        print( format(jump_map[i], '#04x') + ', ' , end='')
        if c == 8: 
            print('')


#print_jump_map()



########################################
#
#  위에서 만든 각 맵을 기반으로 이동 가능한 위치 추적 계산함
#




# 방향별 다음 위치 (해당 방향으로 갈수 없을경우 -1)
def nextPos(pos, dir, map):
    dirs = [LL, UU, RR, DD, LU, RU, RD, DL]
    dtrs = [-1, -9, 1, 9, -10, -8, 10, 8]
    if map[pos] & dirs[dir] > 0 :
        return pos + dtrs[dir]
    else:
        return -1
    

# 직선 이동 , 맵 별로, 횟수만큼
def straight(pos, dir, map, cnt):
    ret = []
    curr = pos
    while cnt > 0:
        n = nextPos(curr, dir, map)
        if n < 0:
            break
        ret.append(n)
        curr = n
        cnt -= 1
    return ret


def print_test():
    for d in range(8):
        r = straight(13, d, link_map, 20)
        print(d, r)


#print_test()


## 연결맵 기반으로 각 위치마다 이동가능한 모든 후보 추적
# 3차원 배열로 늘어난다.
# [
#    [ 위치 0
#       [] 왼쪽
#       [] 위쪽
#       [1,2,3,4,5,6,7,8] 오른쪽 
#       [9,18,27,36,45,54,63,72] 아래
#       [], [], [], [] 대각선
#    ],
#    [ 위치 1
#      .....
# ]
# 이런식으로 만들어진다.
# 반드시 시작 위치부터 이동방향으로 진행되어야함. 
# 나중에 후보집합을 읽어나가면서 비지 않은 CELL을 만났을때 멈추어야 함.
link_cands = []


# 연결맵 후보집합 생성
def gen_link_cands():
    for i in range(90):
        cell = []
        for d in range(8):
            cell.append( straight(i, d, link_map, 20) )
        link_cands.append(cell)


gen_link_cands()

#pprint.pprint(link_cands)


# 궁맵 후보집합 생성
gung_cands = []
def gen_gung_cands():
    for i in range(90):
        cell = []
        for d in range(8):
            cell.append( straight(i, d, gung_map, 1) )
        gung_cands.append(cell)

gen_gung_cands()

#pprint.pprint(gung_cands)

# 점프맵 마 후보집합 생성
ma_cands = []
def gen_ma_jump_cands():
    for i in range(90):
        steps = [
            [I_LL, I_DL],
            [I_LL, I_LU],
            [I_UU, I_LU],
            [I_UU, I_RU],
            [I_RR, I_RU],
            [I_RR, I_RD],
            [I_DD, I_RD],
            [I_DD, I_DL],
        ]
        cell = []
        for step in steps:
            s = []
            curr = i
            n = nextPos(curr, step[0], jump_map)
            if n > 0:
                s.append(n)
            else:
                cell.append([])
                continue

            curr = n
            n = nextPos(curr, step[1], jump_map)
            if n > 0:
                s.append(n)
                cell.append(s)
            else:
                cell.append([])
                continue
        
        ma_cands.append(cell)



gen_ma_jump_cands()

#pprint.pprint(ma_cands[1])



sang_cands = []

def gen_sang_jump_cands():
    for i in range(90):
        steps = [
            [I_LL, I_DL, I_DL],
            [I_LL, I_LU, I_LU],
            [I_UU, I_LU, I_LU],
            [I_UU, I_RU, I_RU],
            [I_RR, I_RU, I_RU],
            [I_RR, I_RD, I_RD],
            [I_DD, I_RD, I_RD],
            [I_DD, I_DL, I_DL],
        ]
        cell = []
        for step in steps:
            s = []
            curr = i
            n = nextPos(curr, step[0], jump_map)
            if n > 0:
                s.append(n)
            else:
                cell.append([])
                continue

            curr = n
            n = nextPos(curr, step[1], jump_map)
            if n > 0:
                s.append(n)
            else:
                cell.append([])
                continue

            curr = n
            n = nextPos(curr, step[2], jump_map)
            if n > 0:
                s.append(n)
                cell.append(s)
            else:
                cell.append([])
                continue
        
        sang_cands.append(cell)


gen_sang_jump_cands()

#pprint.pprint(sang_cands[1])



## 파일-랭크 시스템을 위해 매핑 

files = ['a','b','c','d','e','f','g','h','i']
ranks = ['10','9','8','7','6','5','4','3','2','1']

mapping = {

}


def mapping_file_rank():
    ccnt = 0
    for r in ranks:
        for f in files:
            mapping[ccnt] =  f + r
            ccnt += 1

mapping_file_rank()

#pprint.pprint(link_cands)


import sys
 
path = 'test.txt'
sys.stdout = open(path, 'w')

def print_js_style(cands):
    print('{')
    for i, pcand in enumerate(cands):
        key = mapping[i]
        print("'" + key + "': [", end='')
        for k,dir in enumerate(pcand):
            if k != 0:
                print(',', end='')
            print('[', end='')
            for j,step in enumerate(dir):
                if j != 0:
                    print(',', end='')
                print(f"'{mapping[step]}'", end='')
            print(']', end='')
        print('],')
    print('}')

#print_js_style(link_cands)
#print_js_style(gung_cands)
#print_js_style(ma_cands)
print_js_style(sang_cands)