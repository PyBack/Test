# HearthStone 스플린트

json 파일로 되어 있는 카드 정보를 개발자가 읽어서 카드 내용을 구현
카드 로더 
json loader <- cards.json 자료 구조에 맞게 읽어서 객체 생성
카드 데이터 중에 정체 불명의 카드는 예외 처리
optional  타입  c++17 
사용 예 std::optional<size_t>(attack)
mac os clang 에는  optional 는 없음

power 능력 부분 메뉴얼로 구현해야 함
basic cards generator

직업별로 카드 능력 구현, 뽑을 수 없는 능력은 별도로 구현 해야 함
돌롱잎 맷돼지 ID CS_134 (json 파일에서 ID 검색 가능)
녹색 괴물은 별도 능력치가 있어서 별도 구현 필요
순수 가상 함수 Impl 구현 필수 (카드 드로우 시 자동 발동)

p->PowerTask.emplace_back(new PowerTask::HelpfullTask(EntityType::TARGET))
p->PowerTask.emplace_back(new PowerTask::AddEnchantTask(ID, EntityType::TARGET))


## 카드 구현 완료 후 테스트 방법
구글 테스트 사용
머지 할때 CI 구현
경고 수준도 오류로 설정되어 있어서 코딩시 주의 필요
테스트는 각 카드마다 설정
먼저 게임 에이전트 설정 필요 (게정 및 뎈 설정 필요)
덱의 두번째 인자 직업이 인가 임 (테스트 할때는 이것을 넣어 줘야 함)
테스트 전용 AutoResponser 

이후 설정은 테스트 시나리오 작성
draw -> 카드 한장 보유 확인 -> 뽑는 플레이어 주체를 먼저 넣고 영향받을 수 있는 플레이어 설정
-> play card task (카드 를 내놓는 행위)
-> 이글거리는 전쟁도끼 장착 -> 장착 확인 (확인 메타데이터)
-> Expect_EQ( , nullptr)

## 카드 테스트시 턴 초기화로 공격가능하도록 변경 설정
TaskMeta temporal;
taskAgent.RunMulti(temporal, player1, player2, BasicTasks::SwapPlayerTask(), BasicTasks::SwapPlayerTask());

## 카드 구현
Bloodfen Raptor 카드 구현
(https://hearthstone.gamepedia.com/Bloodfen_Raptor)


## Python API 구현
라이브러리를 활용하여 pyd 생성


## Pull Request 방법
- 테스트가 완료되면 로컬 레파짓토리에 commit
- 로컬에서 commit 한 내용을 Folk 시킨 자기 계정의 레파짓토리에 push
($ git push origin master)
- github 레파짓토리에서 "new pull request" 버튼 클릭
- merge 내용 확인


## git folk 버전 최신 업데이트
- git remote -v
- git remote remove upstream (upstream 주소 업데이트 할려면 기존에 있던 remote branch 삭제)
- git remote add upstream https://github.com/utilForever/Hearthstonepp.git
- git fetch upstream
- git checkout master
- git merge upstream/master
- git log --graph --decorate --oneline
- git push origin master (github 에 push)


## git GUI Tool 
- git 크라켄 사용

## xcode 업그레이드 이슈 해결
- cc 링크 애러 이슈
- xcode-select --install
- https://apple.stackexchange.com/questions/254380/macos-sierra-invalid-active-developer-path

## 저장소에 추적하지 않아야 하는 파일이 추가된 경우, 
하지만 작업공간에서 파일이 삭제되면 안되는 경우에 아래의 명령을 사용하면 
저장소에서는 파일이 삭제되지만 내 작업공간에는 파일이 남아 있게 된다.
 "--cached" 옵션없이 사용하면 내 작업공간의 파일도 같이 삭제한다.
$ git rm --cached filename

## Git commit, add, pull, merge 취소하기

reset 명령은 현재 브랜치의 HEAD가 다른 commit 을 가리키게 만듭니다. 
예를 들어서, 방금 commit 한 내용에 잘못된 부분이 있어 커밋을 취소하고, 수정 한 뒤 다시 커밋하고자 할 때 아래와 같이 할 수 있습니다.

$ git commit ;; a mistake
$ git reset --soft HEAD^ 
$ edit file
$ git add file
$ git commit -c ORIG_HEAD


### 1. soft, mixed, hard

reset 옵션 중 soft 는, 현재의 인덱스, 워킹 트리를 그대로 유지한채로 HEAD 를 변경할 것을 의미합니다. 
default 옵션인 mixed 는 인덱스는 취소한채 워킹트리만 그대로, hard 는 인덱스와 워킹트리 변화를 모두 제거하고 HEAD 를 변경합니다.
따라서 위의 reset 구문은 변화를 그대로 유지한 채 HEAD가 이전 커밋을 가리키게 하겠다. 라는 의미입니다. 그래야만 잘못된 부분을 수정할 수 있습니다.


### 2. ORIG_HEAD

reset 을 이용해 HEAD 를 변경하고 나면, 이전의 HEAD 는 .git/ORIG_HEAD 라는 이름으로 저장이 됩니다. 
따라서 새롭게 커밋하고 복잡한 히스토리를 만드는 것 없이 ORIG_HEAD 를 이용해, 잘못된 커밋객체에 다시 수정 사항을 반영할 수 있습니다. 
그리고 -c 옵션은 ORIG_HEAD 의 커멘트를 그대로 이용한다는 뜻입니다.


Cancle merge, commit

모든 pull 과 merge 는 ORIG_HEAD 를 남기므로 reset 의 hard 옵션을 잘못된 merge 나 pull 을 되돌리는데 사용할 수 있습니다. 
hard 옵션은 워킹트리, 인덱스 보존 없이 reset 이 가리키는 커밋의 내용을 그대로 따라가기 때문입니다.

$ git reset --hard ORIG_HEAD
$ git reset --merge ORIG_HEAD ;; If you wanna keep your changes


또한 hard 옵션을 이용하면, commit 도 취소할 수 있습니다. @ 은 1.8.4 부터 도입된 HEAD 의 동의어 입니다. 
@^, @~1 @~, 모두 이전 HEAD 를 가리키는 뜻입니다.

$ git reset --hard @^


Cancle add (index)

reset 을 이용해 add 를 취소할 수 있습니다. reset 의 default 옵션인 mixed 가 워킹트리를 보존하지만, 
Index 는 보존하지 않기 때문입니다. 현재 HEAD 를 가리키면서 mixed 를 적용하면, index 를 취소할 수 있습니다.

$ git reset HEAD
