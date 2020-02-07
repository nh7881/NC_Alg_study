'''
생각했던 strategy
1. 학생수 n을 입력받으면 그 크기의 list를 생성한다.(stud_list라 명명한다)
2.입력받은 친구끼리 짝지어주는 법을 두개씩 구분하여 리스트에 저장한다.(coup_list라 명명한다)
(재귀)
3.coup_list를 왼쪽부터 차례대로 원소를 가리킨다.
4.coup_list의 원소 쌍 값(예시: 2,3)을 stud_list의 해당 인덱스 값과 동일하게 넣는다
stud_list index->0 1 2 3 4 5
stud_list ele  -> | |2|3| |
4-1.둘 다 들어갔고, 아직 stud_list가 꽉 차지 않았으면 재귀로 부르며 coup_list의 다음 원소를 가리킨다
4-2.원소 쌍 중에서 하나라도 이미 있다면 continue로 다음 원소를 가리킨다.
4-3. 4-1과 4-2 모두 이미 stud_list가 다 찼으면 해당 재귀함수를 빠져나온다.
5. 4-1을 한 후 stud_list가 다 찼으면 그건 모든 학생을 짝짓는 법(pt라고 변수를 만든다)을 하나 찾았다는 뜻이다.
즉, pt++을 해준다.
6. 모든 재귀가 끝나고 난 후 pt값은 주어진 테스트케이스에서 학생들을 짝짓는 방법의 개수이다.
'''

'''
def read()
1. 입력받은 것을 유의미하게 분류함
2. 테스트케이스를 여러번 받기에 for문으로 여려번 연산할 예정
3. for문 안에서 실제 연산할 함수를 부를 예정
'''
def read_():
    print("테스트케이스의 수를 입력하시오")
    testcase_num = int(input())

    for i in range(testcase_num):
        print(i,"번째 테스트케이스입니다")
        print("학생수와 친구쌍의 수를 띄어쓰기로 구분하여 쓰십시오")
        stud_friend_num = input()
        stud_friend_list = stud_friend_num.split()
        print(stud_friend_list)
        stud_num_ = stud_friend_list[0]
        friend_num_ = stud_friend_list[1]
        stud_num = int(friend_num_)
        friend_num = int(friend_num_)

        print("띄어쓰기로 구분하며 친구끼리 짝지어주는 방법의 나열하여 쓰십시오")
        combi_string = input()
        combi_list_ = combi_string.split()
        ###현재 원소는 str형이다

''' 
def


'''


if __name__ == "__main__":
    read_()
