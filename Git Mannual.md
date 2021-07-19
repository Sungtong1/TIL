# Git Manual by VS code





### 1. 저장소 선택후 VS code로 열어준다.



### 2. 터미널을 연다 

`control + (backtick)  ` 으로 터미널 실행



### 3. 깃으로 관리하기(Init)

``` $ git init ```

### 4. 이름과 이메일 등록

```$ git config --global user.name "(내 이름)"```

```$ git config --global user.email "(내 메일 주소)"```

### 5. 현재 상태 보기 (Status)

``` $ git staus ```

### 6. 스테이지로 이동 (Add)

```$git add .``` : 모든 파일을 스테이지로 이동

```$git add (파일명). 확장자``` : 특정 파일을 스테이지로 이동

* 파일명에 `space` 가 포함되어 있을 경우 `/스페이스바`를 통해 표현한다

### 7. Commit

```$ git commit -m "commit 메세지"``` 

### 8. Log 확인하기 (Log)

```$git log```

### 9 되돌아가기(Reset & Revert)

- 돌아가는 지점 이후의 행적을 삭제 

```$ git reset 일련번호 중 앞 6자리 --hard```

- 원하는 지점의 실행을 취소

``` git revert 취소 할 시점 일련번호 중 앞 6자리 ```

 ### 10. 새로운 Branch 생성 

`$git branch "branch 명"` : 새로운 branch 생성

`$git branch` : branch를 확인 (master 와 새로운 branch가 있을 것)

`$git checkout "branch 명"` : 해당 branch로 이동



### 11. 다른 Branch에서 가져오기

1.  먼저 Master Branch로 돌아온다 

   `$git checkout master`

2. 변화를 가져올 Branch를 가져온다

   `$git merge "변화를 가져올 Branch"`

3. 시각화된 작업 내역 보기

   `$git log --graph --all --decorate`

### 12. Branch 삭제 

`$git branch -D "브랜치 명"`



### 13. Remote 

`$git remote add origin "github url"`

`$git remote -v` : 등록된 저장소 목록 확인

### 14. Push & Pull

`$git push origin master`

`$git pull origin master`

