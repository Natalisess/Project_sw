# 학번 : 202268010
# 이름 : 조재열

from datetime import datetime   
# datetime을 import함 datetime은 날짜와 시간을 동시에 표현하기 위해서 사용되며, 위에서 다룬 date와 time 클래스에서 지원하는 대부분의 기능을 지원합니다

def Project_line(line, line_2) :  # 프로그램 줄 처리 함수
    return line + line_2

def Project_time() : # 과제 시간 계산 함수
    Project_file = open("조재열.txt", "w", encoding='utf-8') # 현재 폴더에 조재열.txt 파일로 쓰기모드로 열고 한글이 포함하여 UTF-8로 인코딩을 변경
    now  = datetime.now()   # datetime.now()로 현재 날짜를 가져온다

    line = "===============================" # 프로그램 줄 처리 
    line_2 =  "===================" # 
    line_3 = Project_line(line,line_2)

    print(line) # 프로그램 줄처리
    print("[현재] :", now.year,'년', now.month,'월', now.day,'일') # 현재시간을 년,월,일별로 출력한다 ex : 2022년 10월 12일
    print("[입력완료] 적으면 종료")
    print(line) # 프로그램 줄처리

    homework = input("[과제]를 입력하시오. : ")
    project = []    # 입력받은 과제를 프로젝트 변수에 저장

    while homework != "입력완료" : # 입력완료 문자가 입력되기 전까지 
        project.append(homework) # 프로젝트에 홈워크를 추가한다
        homework = input("[과제]를 입력하시오. : ") # 다시 과제를 입력

    print(line) # 프로그램 줄처리 
    print(line_3) # 프로그램 줄처리 

    for i in range(len(project)):   # 과제 개수로 반복을 한다
        Project_date = datetime.strptime("".join(input("[과제] 제출해야되는 날짜를 입력하시오 : ").split("-")),"%Y%m%d") 
        '''
        과제 날짜를 입력받는다 datetime.strptime을 활용하여 datetime객체로 바꾸어준다.
        strptime은 문자열로 되어있는 날짜또는 시간을 datetime객체로 바꾸어준다.
        join함수를 이용하여 리스트를 하나하나 더해서 합친다. 
        "-"경계로 문자열을 분리 %Y%m%d 각각 년,월,일별로 포메팅한다.
        '''
        print(line_3) # 프로그램 줄처리 
        print(f"[과제] 제출 날짜 : {Project_date.year}년 {Project_date.month}월 {Project_date.day}일") # 과제 제출날짜를 포메팅하여 제출날짜를 날짜를 출력한다 f string
        Project_minus_date = Project_date - now # 과제 남은 기한을 과제 제출 날짜 - 현재로 구한다.
        print(f"[{project[i]}]의 남은 날짜 : {Project_minus_date.days}일 남았습니다.") # i의 값에 받아진 과제를 순서대로 출력한다
        Project_file.writelines(f"{project[i]},{Project_date.year},{Project_date.month},{Project_date.day}\n") # 파일에 과제 이름 과제 년,월,일을 한꺼번에 모든 줄을 입력한다

    Project_file.close() # 파일을 닫늗다
