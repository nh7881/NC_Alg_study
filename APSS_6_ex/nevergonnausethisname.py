###6예제 보글게임
'''
def make_boggle_sqr(): 2차원리스트 보글테이블 만드는 함수
    출력:이차원 스트링리스트

def make_dict(): 찾을 스트링을 리스트에 넣어 출력하는 함수
    출력:일차원 스트링리스트

def next_dir(col, row, dir_idx): 이차원리스트의 한 원소에 대해서,
                                 주변 8방향중 어디로 갈지 정하고
                                 인덱스 범위에서 벗어나면 -1,-1을 출력하여 알리는 함수
    출력: int형 변수 두개 col,row

def find_first_word(), find_next_word(): 재귀용 함수->만악의 근원...
    의도: for문 (8방향을 체크하게 한다)
         만약 col,row가 인덱스 범위를 벗어날 경우 continue로 다음방향을 향하게 예외처리한다.
         8방향에 대한 col,row값을 next_col, next_row라 명명한다.
         if(sqr[next_col][next_row] == word[0:1]) ->만약 가리킨 방향의 원소가 찾던 글자(word[0:1])면
                                                    next_col,next_row값을 매개변수로 넣어 재귀를 돌린다.
         그렇게 재귀로 원소를 옮겨다니며 맞는 원소는 list에 저장하고 필요할 경우 그 전 원소로 돌아가며 pop한다
         결과적으로 list에 저장된 글자와 make_dict()에서 만든 스트링을 비교해서 맞으면 있다고 출력
         끝까지 모두 찾았는데도 없으면 없다고 출력.


'''

def make_boggle_sqr():
    sqr=[['u','r','l','p','m'],
         ['x','p','r','e','t'],
         ['g','i','a','e','t'],
         ['x','t','n','z','y'],
         ['x','d','q','r','s']]
    return sqr


def make_dict():
    dict_list=['pretty','girl','repeat']
    return dict_list


def find_first_word(sqr, word):
    print(word,sqr)
    for dir_idx in range(8):
        next_col,next_row = next_dir(0,0,dir_idx)
        if(next_col <0 or next_row <0):continue
        print(next_col, " ", next_row) ###다음 방향 추출 완료

        if(sqr[next_col][next_row] == word[0:1]):
            if(len(word) == 1):
                print("찾았다")
                return
            find_next_word(sqr,word[1:])

def find_next_word(sqr,word):
    for dir_idx in range(8):
        next_col, next_row = next_dir(0, 0, dir_idx)
        if (next_col < 0 or next_row < 0): continue
        print(next_col, " ", next_row)  ###다음 방향 추출 완료

        if (sqr[next_col][next_row] == word[0:1]):
            if (len(word) == 1):
                print("찾았다")
                return
            find_next_word(sqr, word[1:])


###-1,-1출력시 해당 방향으로 가지 말기
def next_dir(col, row, dir_idx):
    if (dir_idx == 0): return col, row-1
    if (dir_idx == 1): return col+1,row-1
    if (dir_idx == 2): return col+1,row
    if (dir_idx == 3): return col+1,row+1
    if (dir_idx == 4): return col,row+1
    if (dir_idx == 5): return col-1,row+1
    if (dir_idx == 6): return col-1,row
    if (dir_idx == 7): return col-1,row-1
    return -1,-1


if __name__ == "__main__":
    find_word(make_boggle_sqr(),make_dict())
