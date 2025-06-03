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

## github (원격저장소) 주소 변경하기
```bash
$ git remote reset-url origin {https://login-key@github.com/GitHunID/repository-name.git}
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

## 변경사항 마지막 커밋으로 되될리기
```sh
$ git checkout . : 변경된 파일 복구, 추가된 파일 삭제, 최종 커밋 상태로 되돌려져 있음  
```

## commit 변경 사항 추가 방법
1. 변경사항 A 커밋!
2. 미처 포함시키지 못한 변경사항 AA 발견!
3. git add AA
4. git commit -C HEAD --amend


## Git remote branch 가져오기
1. 먼저 원격의 브랜치에 접근하기 위해 git remote를 갱신해줄 필요가 있다. ($ git remote update)
2. 원격 저장소 branch 확인 ($ git branch -r)
3. 로컬, 원격 저장소 branch 확인 ($ git branch -a)
4. 원격 저장소의 branch 가져오기 ($ git checkout -t origin/$BRANCH_NAME

## git tracked 파일/폴더 untracked 로 변환하기
기존의 git의 관리를 받고 있던(commit된 것들) 파일이나 폴더를 .gitignore 파일에 작성하고  
add > commit > push 하여도  ignore(무시) 되지 않음  
기존에 가지고 있는 cached를 삭제해야함  
  
### 1.  Git 에서 파일 or 폴더 삭제하기 
git rm --cache 명령어는 Staging Area(add 를 하고나서의 영역)에서 파일을 제거하고 working directory(Local)에서는 파일을 유지하는 명령어
```sh
$ git rm --cached {삭제할파일}
$ git rm -r --cached {삭제할폴더}
ex) $ git rm -r --cached .vscode
```

### 2. .gitignore 파일에 해당 폴더 추가하기 
### 3. 변경 내역 Commit 하기
```sh
ex) $ git commit -m "untrack .vscode & apply .gitignore"
```
### 5. 원격 저장소 에 반영 
```sh
$ git push origin {branch_name}
```

## Git Submodule 사용 방법

### 1. Submodule이 포함된 레파지토리 clone
서브모듈을 포함하는 프로젝트를 일반적으로 클론하면, 서브모듈 디렉토리는 빈 디렉토리가 된다.   
**메인 프로젝트 입장에서 서브모듈은 사실 단지 현재 가리키는 커밋과 변경 여부만 적혀있는 하나의 파일에 불과** 하기 때문이다.  
기본적으로 서브모듈은 다른 레파지토리이기 때문에 해당 빈 디텍토리에 가서 clone 을 하면 된다.  
```sh
$ cd {submodule-folder}
$ git clone -b {branch_name} https://github.com/{sub-respository}.git
```
  
좀더 엄일한 초기화 방법은 아래와 같다  
```sh
$ git submodule init
$ git submodule update
```
git submodule init 은 서브모듈 디렉터리를 git 로컬 저장소로 초기화 해주고(git init 처럼)
git submodule update 는 각 브랜치와 HEAD 정보 및 커밋 내역을 가져온다. 
  
더 편한 방법은 --recurse-submodules 옵션을 사용하여 클론해야 서브모듈을 자동으로 함께 가져온다.
```sh
$ git clone --recurse-submodules https://github.com/{super-repository}.git
```

### 2. Submodule 변경 사항 업데이트
```sh
$ cd {submodule-folder}
$ git pull origin develop
```
  
참조 
https://hudi.blog/git-submodule/  
https://sgc109.github.io/2020/07/16/git-submodule/  


## git log 옵션
[alias]  <br/>
git config --global alias "log --color --decorate --oneline --graph"
lg1 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ad)%C(reset) %C(white)%s%C(reset) %C(dim white)- [%an]%C(reset)%C(bold yellow)%d%C(reset)' --date=short --all
lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%ad%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n'' %C(white)%s%C(reset) %C(dim white)- %an%C(reset)' --all --date=format: '%Y-%m-%d %H:%M:%S %z' 
lg = !'git lg1' <br/>
```sh
$ git log --pretty=format:'%h %ad %s' --date=short  --graph : 해시코드 날짜 커밋내용 + 그래프
```
## github invalid username n password, general token 설정
git push를 했을 때 다음과 같은 오류가 발생했을 때 해결 방법

```sh
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/
```

https://sosoeasy.tistory.com/536

## git config local user 셋팅
```sh
$ git init  # 이미 생성되어 있으면 안해도됨
$ git config --local user.name "your name"
$ git config --local user.email "your email"
```

아래와 같은 방법도 가능 한듯 🤔

can confirm that by printing on the terminal:
```
    Global user:git config --global user.name
    Local user: git config user.name
```

혹은

...or just edit the .git\config file and add these three lines somewhere:
```
[user]
    name = YourName
    email = your@email.com
```
