# uv 패키지 관리자 사용 가이드

## uv란?

uv는 Rust로 작성된 매우 빠른 Python 패키지 설치 및 의존성 해결 도구입니다. pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv 등의 기능을 하나로 통합한 올인원 도구입니다.

## 설치

### macOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Homebrew (macOS)
```bash
brew install uv
```

### pip으로 설치
```bash
pip install uv
```

## 기본 명령어

### 패키지 설치
```bash
# 단일 패키지 설치
uv add requests

# 여러 패키지 설치
uv add requests numpy pandas

# 개발 의존성으로 설치
uv add --dev pytest black flake8

# 특정 버전 설치
uv add "django>=4.0,<5.0"
uv add "numpy==1.24.0"
```

### 패키지 제거
```bash
# 패키지 제거
uv remove requests

# 여러 패키지 제거
uv remove requests numpy pandas
```

### 프로젝트 초기화
```bash
# 새 프로젝트 생성
uv init my-project
cd my-project

# 기존 디렉토리에서 초기화
uv init
```

### 가상환경 관리
```bash
# 가상환경 생성
uv venv

# 특정 Python 버전으로 가상환경 생성
uv venv --python 3.11

# 가상환경 활성화 (Linux/macOS)
source .venv/bin/activate

# 가상환경 활성화 (Windows)
.venv\Scripts\activate

# uv를 통한 명령 실행 (가상환경 자동 활성화)
uv run python script.py
uv run pytest
```

### 의존성 관리
```bash
# 의존성 설치 (pyproject.toml 기반)
uv sync

# 개발 의존성 제외하고 설치
uv sync --no-dev

# requirements.txt에서 설치
uv pip install -r requirements.txt

# 현재 설치된 패키지 목록
uv pip list

# 패키지 정보 확인
uv pip show requests
```

### Python 버전 관리
```bash
# 사용 가능한 Python 버전 확인
uv python list

# Python 설치
uv python install 3.11
uv python install 3.12

# 특정 Python 버전 사용
uv python pin 3.11
```

### 스크립트 실행
```bash
# Python 스크립트 실행
uv run python app.py

# 모듈 실행
uv run -m pytest

# 인라인 의존성과 함께 스크립트 실행
uv run --script script.py
```

## 고급 사용법

### 워크스페이스 관리
```bash
# 워크스페이스 초기화
uv init --workspace

# 워크스페이스에 패키지 추가
uv add --workspace requests
```

### 빌드 및 배포
```bash
# 패키지 빌드
uv build

# PyPI에 배포
uv publish

# 테스트 PyPI에 배포
uv publish --index-url https://test.pypi.org/simple/
```

### 캐시 관리
```bash
# 캐시 상태 확인
uv cache info

# 캐시 정리
uv cache clean

# 특정 패키지 캐시 정리
uv cache clean requests
```

### 설정 관리
```bash
# 설정 확인
uv config list

# 설정 변경
uv config set index-url https://pypi.org/simple/

# 설정 초기화
uv config unset index-url
```

## 실용적인 사용 예시

### 새 Django 프로젝트 시작
```bash
# 프로젝트 생성 및 초기화
mkdir my-django-app
cd my-django-app
uv init

# Django 설치
uv add django

# Django 프로젝트 생성
uv run django-admin startproject mysite .

# 개발 서버 실행
uv run python manage.py runserver
```

### 데이터 분석 환경 구성
```bash
# 프로젝트 초기화
uv init data-analysis
cd data-analysis

# 데이터 분석 패키지들 설치
uv add pandas numpy matplotlib seaborn jupyter

# Jupyter 노트북 실행
uv run jupyter notebook
```

### 테스트 환경 구성
```bash
# 테스트 도구들을 개발 의존성으로 설치
uv add --dev pytest pytest-cov black isort mypy

# 테스트 실행
uv run pytest

# 코드 포매팅
uv run black .
uv run isort .

# 타입 체크
uv run mypy .
```

### requirements.txt에서 마이그레이션
```bash
# 기존 requirements.txt가 있는 경우
uv add --requirements requirements.txt

# 또는 직접 설치
uv pip install -r requirements.txt

# pyproject.toml로 변환
uv export --format requirements-txt > requirements.txt
```

## pyproject.toml 예시

```toml
[project]
name = "my-app"
version = "0.1.0"
description = "My awesome application"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
dependencies = [
    "requests>=2.25.0",
    "click>=8.0.0",
]
requires-python = ">=3.8"

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "isort>=5.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=7.0.0",
    "black>=22.0.0",
    "isort>=5.0.0",
]
```

## 유용한 팁

### 성능 최적화
- uv는 기본적으로 매우 빠르지만, `--no-cache` 옵션으로 캐시를 비활성화할 수 있습니다
- `--offline` 옵션으로 오프라인 모드를 사용할 수 있습니다

### CI/CD 환경에서 사용
```bash
# CI에서 의존성 설치
uv sync --frozen

# 정확한 버전으로 잠금
uv lock

# 잠금 파일 업데이트
uv lock --upgrade
```

### 환경변수 설정
```bash
# 인덱스 URL 설정
export UV_INDEX_URL=https://pypi.org/simple/

# 캐시 디렉토리 설정
export UV_CACHE_DIR=/path/to/cache
```

이 가이드를 통해 uv를 효과적으로 사용하여 Python 개발 환경을 관리할 수 있습니다. uv는 전통적인 pip + virtualenv 조합보다 훨씬 빠르고 사용하기 쉬운 현대적인 도구입니다.