from random import randint as rd

ans='';cnt=1
print('정보처리기사 보안 관련 용어 랜덤 질문입니다.')
while 1:
    chk=0
    ty=rd(1,1)*1000
    num=ty+rd(0,84)
    file=str(num)+'.txt'
    data=open(file,'r',encoding='UTF-8')

    
    for _ in data:
        if chk==0:
            print('\n%d번 문제입니다.\n'%cnt+'-'*20+'\n')
            ans=_.split()
        else:
            print(_,end=' ')
        chk+=1
    cnt+=1
    
    yours=input('\n1.영문 소문자로만 풀네임 입력해주세요.\n2. 또는 대문자 약어를 적으시오.\n3. 한글도 가능.\n띄어쓰기 대신 언더바\'_\'를 쓰시오..기호없음.\n')

    if yours in ans:
        print('맞았습니다.')
        print('정답은    ',' 또는 '.join(ans),'   입니다.')
    else:
        print('틀렸습니다.')
        print('정답은    ',' 또는 '.join(ans),'    입니다.')
        
    re=input('\n끝내시려면  0과 Enter를 눌러주세요.\n')
    if re=='0':
        break
    data.close()
