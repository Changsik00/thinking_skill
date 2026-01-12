# Spec 020: Linting & Formatting Automation

## 📝 Description
**Spec 020**은 프로젝트에 `ruff`를 도입하여 코드 스타일 일관성을 보장하고 잠재적인 버그(예: `IndentationError`, `ImportError`)를 사전에 방지합니다.

이 PR은 다음 내용을 포함합니다:
*   **Ruff 도입**: `flake8`, `black`, `isort`를 대체하는 고성능 린터/포매터.
*   **코드 리팩토링**:
    *   모든 Python 파일에 Formatting 적용 (Line length 120).
    *   `main.py`, `mcp_server.py`의 모듈 레벨 Import 문제 (`E402`) 수정 및 구조 정리.
    *   `init.py`의 Unused Import 문제 (`F401`) 수정.
*   **CI 통합**: GitHub Actions에 Lint Check 단계 추가.

## 🛠 Changes

### 1. Configuration (`pyproject.toml`)
```toml
[tool.ruff]
line-length = 120
target-version = "py311"
# ...
```

### 2. CI (`.github/workflows/test.yml`)
- `Lint with Ruff` 단계 추가.
- `Check Formatting` 단계 추가.

### 3. Refactoring
- **`app/main.py`**: Import 문을 최상단으로 이동하고 앱 초기화 로직을 정리했습니다.
- **`app/interfaces/mcp_server.py`**: Import 문 정리.
- **`app/infrastructure/llm/prompts.py`**: Deprecated 파일이므로 Lint 예외 처리 (`per-file-ignores`).

## ✅ Verification
- **Local**:
    - `uv run ruff check .` -> **Pass** (Clean).
    - `uv run ruff format --check .` -> **Pass** (Clean).
    - `uv run pytest` -> **Pass** (26 tests).
- **CI**: 커밋 후 GitHub Actions 통과 예정.
