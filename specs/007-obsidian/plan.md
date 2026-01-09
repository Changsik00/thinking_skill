# Implementation Plan: Obsidian Integration

## 1. Domain/Infrastructure Layer (`LocalAdapter`)
- **Config Update**: `__init__`에서 `os.getenv("OBSIDIAN_VAULT_PATH", "data/archives")`를 읽도록 수정.
- **Content Formatting**:
    - 단순 텍스트 결합 방식(`f""`)을 개선.
    - `result.content` 앞에 **YAML Frontmatter** 추가.
    - Tags: `#macs-agent` 등 기본 태그 추가.

## 2. Configuration (`.env`)
- `.env.example`에 `OBSIDIAN_VAULT_PATH` 추가.

## 3. Dependency Injection (`main.py`)
- `LocalAdapter` 인스턴스 생성 시 별도 모듈 변경 불필요 (Environment Variable 내부 처리 권장).
- 또는 `main.py`의 `lifespan`에서 주입할 수도 있음. (Env 변수 사용이 더 깔끔함)

## 4. Testing
- `LocalAdapter` 단위 테스트 업데이트 (Frontmatter 검증).
