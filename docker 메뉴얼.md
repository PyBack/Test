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
```

``` sh
$ docker images              : docker 이미지 리스트 확인
```

참고 사이트: https://poiemaweb.com/docker-mysql
