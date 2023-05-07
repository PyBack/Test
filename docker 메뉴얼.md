# Docker 메뉴얼

## 1.Docker를 사용하여 MySQL 설치하고 접속하기

### 1-1.Docker 설치 및 버전 확인
```sh
$ docker -v           : 도커 버전 확인
Docker version 19.03.13, build 4484c46d9d
```

### 1-2.Docker 설치 및 버전 확인
mysql latest 버전 이미지 다운로드 
```sh
$ docker pull mysql  
```


MySQL 버전을 지정하려면 태그에 버전을 지정한다. 다운로드할 수 있는 MySQL 버전은 docker hub에서 확인할 수 있다.   
예를 들어, MySQL 8.0.22 버전을 다운로드하려면 다음과 같이 태그에 버전을 지정한다.
``` sh
$ docker pull mysql:8.0.22   : mysql 8.0.2 버전 이미지 다운로드 
8.0.22: Pulling from library/mysql
Digest: sha256:8c17271df53ee3b843d6e16d46cff13f22c9c04d6982eb15a9a47bd5c9ac7e2d
Status: Downloaded newer image for mysql:8.0.22
docker.io/library/mysql:8.0.22
```

``` sh
$ docker images              : docker 이미지 리스트 확인
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mysql               8.0.22              db2b37ec6181        2 weeks ago         545MB
mysql               latest              db2b37ec6181        2 weeks ago         545MB
```

### 1-3. MySQL Docker 컨테이너 생성 및 실행
``` sh
$ docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=<password> -d -p 3306:3306 mysql:latest
```

### 1.4 Docker 컨테이너 리스트 출력
``` sh
$ docker ps -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                      PORTS     NAMES
8c1bf870bf54   flask-vue-argon-backend    "python3 app.py"         41 minutes ago   Exited (0) 39 minutes ago             backend-docker
becb1adc69ba   flask-vue-argon-frontend   "docker-entrypoint.s…"   42 minutes ago   Exited (1) 40 minutes ago             frontend-docker
b18a33ebab02   mysql:5.7                  "docker-entrypoint.s…"   5 days ago       Exited (0) 39 minutes ago             my-back-mysql
2a7d5f50de1e   mysql:8.0.22               "docker-entrypoint.s…"   5 days ago       Exited (0) 5 days ago                 mysql-container-test
d0c246b617e1   docker101tutorial          "/docker-entrypoint.…"   4 weeks ago      Exited (0) 4 weeks ago                docker-tutorial
6f8e3b492e2f   alpine/git                 "git clone https://g…"   4 weeks ago      Exited (0) 4 weeks ago                repo
```

### 1.5 MySQL Docker 컨테이너 접속
``` sh
$ docker exec -it mysql-container bash
root@dc557b92f573:/# mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.22 MySQL Community Server - GPL

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)

mysql> USE mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```

## 2. Docker Container 에 볼륨 설정하기

볼륨 리스트 확인 하기
```sh
$  docker volume list
DRIVER    VOLUME NAME
local     b97c5432ff0a86802d2cbca69484448f1ecd5c530ddcad7e4b7eea3c6ec2e8c5
```

## 3. Docker 를 사용하여 Flask REST API 서버 이미지 생성 및 컨테이너 실행

### 3-1. Docker 이미지 생성
``` sh
$ docker (image) build -t {이미지이름} ./
```
1. -t (--tag) 옵션은 이미지명과 태그명을 붙이는 것 실제 사용에서 거의 필수
2. 도커파일 경로에서 "."은 현재 작업 디렉터리
3. -f 옵션은 기본인 Dockerfile 대신에 다른 파일 명을 사용할 경우 사용
``` sh
$ docker (image) build {이미지이름} -f Dockerfile-test  -t exmaple/echo:latest ./
```
4. --pull 옵션은 매번 베이스 이미지를 강제로 새로 받아옴
``` sh
$ docker (image) build {이미지이름} --pull=true -t exmaple/echo:latest ./
```

### 3-2. Docker 이미지 컨테이너 실행
기본 명령어
``` sh
$ docker (container) run {이미지이름}:{버전}
```

1 -d 옵션
	서버프로그램을 run 시키면 해당 쉘이 서버 로그창으로 바뀜
	그러지 않게 하기 위해 백그라운드(daemon)으로 컨테이너를 실행시킨다는 옵션
2 -p 옵션
	포트 포워딩 지정
	<호스트 포트>:<컨터에너포트>
	호스트포트는 중복되면 안됨
3 -i 옵션
	컨테이너 쪽 쉘에 들어가서 명령 실행할 수 있는 입력이 되게끔 함
4 -t 옵션
	터미널 기능 활성화
	주로 -it 옵션이 함께 자주 사용
5 -v 옵션
	볼륨 마운트 이용시 사용
6 --name 옵션
	컨테이너의 이름을 지정해줌
	--name <이름> 옵션과 붙여서 사용
7 --rm 옵션
	컨테이너를  stop 시키는 동시에 삭제까지 한번에 실행

예시)
``` sh
$ docker container run -it --name backend-test-docker -d -p 5050:5000 backend-test:latest
```


참고 사이트:   
[docker mysql 컨터에너 생성](https://poiemaweb.com/docker-mysql)  
[mysql container에 볼륨 설정하기](https://velog.io/@june20516/mysql-dockerize2-mysql-container%EC%97%90-%EB%B3%BC%EB%A5%A8-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)  
[docker 이미지 빌드와 컨테이너 실행](https://conanglog.tistory.com/69)  
