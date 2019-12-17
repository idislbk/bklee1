# 최초 생성시

1. git init

2. git add readme.md   …or  git add .

3. git commit -m "first commit"  // 로컬 저장소로 커밋한다.

4. git remote add origin  [깃저장소경로]   //  깃저장소경로를 origin으로 alias 한다 <br/>
    ex) git remote add origin https://github.com/~~~.git

5. (이미 경로에 무언가 있다면 )협업으로 인해 소스 내려받기도 필요하면 <br/>
    git pull origin master  origin의 내용이 master로 복사됨. 

6. ** 처음 push 시에만 로그인하라고 뜰 수 있음.  깃허브 계정으로 로그인 하면됨(최초 1회)  <br/>
git push -u origin master             // 저장소로 밀어넣는다.  master : 현재 브랜치  <br/>
…or push an existing repository from the command line   

    ** 혼자 쓸때는 위에만 하면 됨.
2회 시부터는 **git status** 명령어로 상태 봐가면서 할 것

# 다른놈 복사해서 진행 할때
1. git clone [깃저장소경로]  :  git pull 과 비슷하지만 클라이언트 상에 아무것도 없을 때 서버의 프로젝트 내려받음.  init 까지 실행함.

2. 최초 생성시의 2 ~ 6 반복


[참조 명령어](https://blog.naver.com/rnwkrud94/221242876100)
```
reset A             A위치로 커밋을 되돌린다(옵션 --soft (추천), --hard, --mixed)
merge A          현재 브랜치에 A 내용을 합친다.(merge인자는 최대 1개)
rebase A          현재 브랜치의 내용을 A브랜치에 이어 붙이고 현재 브랜치 HEAD를 그 위치로 이동
rebase A B       B의 내용을 A에 이어붙이고 B브랜치 HEAD를 그 위치로 이동
rebase -I A       현재 브랜치의 내용을 A에 이어 붙이는데 특정 커밋을 선택할 수 있음
rebase --onto master server client  ***master에 client 내용을 이어 붙임
cherrypick A1 A2 B       커밋 A1,A2을 B에 이어 붙임
branch A B                 A브랜치를 생성하고 그 위치를 B로 설정
branch -f A B    A브랜치를 B위치로 옮긴다.
branch -u A B  A브랜치가 B브랜치를 추적하도록 설정(B브랜치는 존재해야됨)
checkout A                 A브랜치로 HEAD를 이동
checkout -b A B           A브랜치를 B위치에 생성하고 HEAD를 이동
fetch    원격 내용을 로컬에 다운로드하고 원격브랜치의 위치만 옮김(로컬브랜치 위치는 그대로) 
fetch origin B:A           원격B브랜치의 내용을 로컬A브랜치에 fetch
fetch origin :A  출발지에 아무것도 안쓰면 null을 옮기는 것이므로 로컬A브랜치가 삭제됨
pull                           fetch+merge. 원격브랜치를 추적하고있는 브랜치에서만 가능
pull –-rebase               fetch+rebase. 원격브랜치를 추척하고있는 브랜치에서만 가능
pull origin A:B              원격A브랜치 내용을 로컬B브랜치에 fetch + 현재 브랜치에 merge
push     현재 브랜치의 내용을 같은 원격브랜치에 업로드(원격브랜치에 연결된 브랜치에서만 가능)
push origin A  로컬A브랜치 내용을 원격A브랜치에 push
push origin A:B            로컬A브랜치 내용을 원격B브랜치에 push
push origin :B              출발지가 비어있으면 null을 push한다는 것이므로 원격B브랜치가 삭제됨
HEAD~n           HEAD의 n개 위에 있는 커밋
HEAD~^2~3      HEAD의 ~(1개 위에 있는 커밋) ^2(부모커밋 중 2번째) ~3(3개 위에 있는 커밋)
***
rebase --onto master server client
브랜치가 master,server,client 있는데 로그가 다음과 같다면
a ← b ← c <=master
   ↖ d ← e <=server
         ↖ f  ← g <=client
사실 client의 f,g는 master의 a와 직접 연관이 없는 상태이다.
master와 상관없는 client의 내용을 이어붙이기 위해서 중간에 연결고리인 server를 명시해준다.
그리고 rebase --onto 옵션을 사용해서 명령을 내리면 다음과 같은 상태가 된다.
a ← b ← c (<=master) ← f  ← g <=client
   ↖ d ← e <=server
```