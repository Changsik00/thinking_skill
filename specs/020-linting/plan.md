# Plan 020: 린팅 및 포맷팅 자동화 계획 (Linting & Formatting Plan)

## 1. 설정 (Setup)
*   **Install Ruff**: `uv add --dev ruff` 명령어로 설치.
*   **Configure**: `pyproject.toml` 파일에 `[tool.ruff]` 섹션 추가.
    *   Line length: 88 또는 100 (표준 준수).
    *   Target version: Python 3.11+.
    *   Rules: `E` (pycodestyle), `F` (Pyflakes), `I` (isort) 활성화.

## 2. 실행 스크립트 (Execution Scripts)
*   **검사 (Check)**: `uv run ruff check .`
*   **포맷팅 (Format)**: `uv run ruff format .`
*   **자동 수정 (Auto Fix)**: `uv run ruff check --fix .`

## 3. CI 통합 (CI Integration)
*   `.github/workflows/test.yml` 수정:
    *   Step 추가: `Run Linter` (`uv run ruff check .`).
    *   Step 추가: `Run Formatter Check` (`uv run ruff format --check .`).

## 4. 검증 계획 (Verification Plan)
*   **Local**: 의도적으로 들여쓰기나 긴 줄을 만들어 `ruff`가 잡아내는지 확인.
*   **CI**: 스타일을 준수한 커밋을 푸시하여 Action 통과 확인.
