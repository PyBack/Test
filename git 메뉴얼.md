# git 메뉴얼

## github 에서 clone 다운로드
1. sourcetree 실행
2. Clone/New 버튼 클릭
3. GitHub 사이트 Repository 에서 https 주소 카피
4. URL 주소에 붙여넣기
5. 다운 받을 빈 폴더 설정
6. 실행

## git에서 특정 브랜치만 clone하는 방법
git clone -b {branch_name} --single-branch {저장소 URL}  
ex) git clone -b test --single-branch https://github.com/pyback/test.git  

## git 리모트 저장소에 push 하기
```sh
$ git push origin master
$ git push -u origin {repositary_name}  // 특정 remote 레포지터리에 push
```

## 신규 local repository 를 github 에 업로드 하기
```sh
$ git remote add origin remote {URL} (https://github.com/$username/$repo_name))  
$ git push -u origin master
```

## git 신규 branch remote 저장소에 push 하기
1. Create a new branch:  
$ git checkout -b feature_branch_name  
2. Edit, add and commit your files.  
3. Push your branch to the remote repository: <br/>
$ git push -u origin feature_branch_name

## pull request 후 review 결과 반영하여 commit 하기
1. Edit for review result
2. $ git add .
3. $ git commit -m "something for review"
4. $ git push origin HEAD

## 로컬에서 reset 한경우 강제로 push remote 하기
애러 메세지가 아래 처럼 뜨는 경우  
(Git push failed, To prevent from losing history, non-fast forward updates were rejected.)  
$ git push origin master --force

## git 저장소 병합
git remote add other /path/to/XXX  
git fetch other  
git checkout -b TEMP other/master  
mkdir ZZZ  
git mv stuff ZZZ/stuff # repeat as necessary for each file/dir  
git commit -m "Moved stuff to ZZZ"  
git checkout master  
git merge TEMP --allow-unrelated-histories # should add ZZZ/ to master  
git commit  
git remote rm other  
git branch -d TEMP # to get rid of the extra branch before pushing  
git push # if you have a remote, that is  

## git 리모트 브랜치 삭제
git 에서 remote branch delete 하는 방법.  
삭제할 브랜치 이름은 feature/TEST-860 이다
 
### 방법 1
```sh
$ git push origin --delete feature/TEST-860
```

### 방법 2
```sh
$ git branch -d feature/TEST-860  <br/>
$ git push origin feature/TEST-860
```

## 특정 로컬 branch 삭제
```sh
$ git branch -D {branch_name}
```
## git add 옵션
```sh
$ git add -A  : stages all changes
$ git add .   : stages new files and modifications, without deletions
$ git add -u  : stages modifications and deletions, without new files
```

## commit 취소 명령어 예제
```sh
$ git reset HEAD^ : 최종 커밋 취소. 그러나 변경된 파일은 남아있다.  
$ git reset --hard HEAD^ : 최종 커밋 취소하고 파일 까지 복구한다.  
$ git reset HEAD~n : 마지막 n개의 커밋을 취소 한다. 그러나 변경된 파일은 남아 있다. ( n : 숫자 )  
$ git reset --hard HEAD~n : 마지막 n개의 커밋을 취소. 파일 또한 복구됨.  
$ git commit --amend : commit 메세지 변경하기
```

## Git remote branch 가져오기
1. 먼저 원격의 브랜치에 접근하기 위해 git remote를 갱신해줄 필요가 있다. ($ git remote update)
2. 원격 저장소 branch 확인 ($ git branch -r)
3. 로컬, 원격 저장소 branch 확인 ($ git branch -a)
4. 원격 저장소의 branch 가져오기 ($ git checkout -t origin/$BRANCH_NAME

## git log 옵션
[alias]  <br/>
lg1 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all  <br/>
lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all
lg = !"git lg1"  <br/>
```sh
$ git log --pretty=format:'%h %ad %s' --date=short  --graph : 해시코드 날짜 커밋내용 + 그래프
```
