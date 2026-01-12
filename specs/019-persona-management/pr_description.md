# Spec 019: Persona Management System

## 📝 Description
**Spec 019**는 에이전트의 페르소나(시스템 프롬프트) 관리 방식을 **하드코딩(Hardcoding)**에서 **설정 파일(Config-based)** 방식으로 전환하는 리팩토링 작업입니다.

이제 개발자가 아니더라도 `configs/personas.yaml` 파일만 수정하면 에이전트의 성격이나 행동 지침을 변경할 수 있습니다.

## 🛠 Changes

### 1. Configuration (`configs/personas.yaml`)
- `creative` (창의적 발산가)와 `critical` (냉철한 비평가)의 프롬프트를 YAML 설정으로 이관했습니다.

### 2. Domain Layer
- **Entity**: `Persona` (name, display_name, system_prompt)
- **Interface**: `PersonaRepository` (get_persona)

### 3. Infrastructure Layer
- **Implementation**: `FilePersonaRepository` (YAML 로더)
- **Refactoring**: `LangGraphBrain`이 더 이상 상수를 사용하지 않고, 주입받은 Repository를 통해 프롬프트를 로드합니다.

### 4. Dependency Injection
- `mcp_server.py`, `main.py`, `runner.py` (CLI) 모든 엔트리 포인트에서 `FilePersonaRepository`를 생성하고 주입하도록 수정했습니다.

## ✅ Verification
- **Unit Test**: `tests/unit/infrastructure/test_file_persona_repo.py`를 통해 YAML 로딩 및 조회 기능 검증 완료.
- **Backlog**: Backlog 업데이트 (Spec 17 Done, Spec 19 Added).
