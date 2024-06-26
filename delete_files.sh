#!/bin/bash

# 삭제할 파일 확장자 목록
EXTENSIONS=("json" "csv" "dat")

# 스크립트 실행 시 첫 번째 인수로 디렉토리 위치를 입력받음
if [ $# -ne 1 ]; then
    echo "사용법: $0 <삭제할 디렉토리 위치>"
    exit 1
fi

# 입력된 디렉토리 위치
target_dir=$1

# 현재 날짜로부터 한 달 전 날짜 계산
find_date=$(date -d "-1 month" +"%Y-%m-%d")

# 각 확장자별로 한 달 전에 생성된 파일 찾아 삭제
for ext in "${EXTENSIONS[@]}"; do
    find "${target_dir}" -type f -name "*.${ext}" -mtime +${find_date} -exec rm -f {} \;
done
