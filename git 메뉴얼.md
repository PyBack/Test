# git 메뉴얼

## github 에서 clone 다운로드
1. sourcetree 실행
2. Clone/New 버튼 클릭
3. GitHub 사이트 Repository 에서 https 주소 카피
4. URL 주소에 붙여넣기
5. 다운 받을 빈 폴더 설정
6. 실행

## git 리모트 저장소에 push 하기
$ git push origin master

## 신규 local repository 를 github 에 업로드 하기
$ git remote add origin remote $URL (https://github.com/$username/$repo_name))
$ git push -u origin master

## git 신규 branch remote 저장소에 push 하기
1. Create a new branch:
$ git checkout -b feature_branch_name
2. Edit, add and commit your files.
3. Push your branch to the remote repository:
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
$ git push origin --delete feature/TEST-860

### 방법 2
$ git branch -d feature/TEST-860
$ git push origin feature/TEST-860

