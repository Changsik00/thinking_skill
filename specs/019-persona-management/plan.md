# Plan 019: Persona Management Implementation

## 1. Config 정의
*   `configs/personas.yaml` 파일 생성.
*   기존 `app/infrastructure/llm/prompts.py` 내용을 YAML 포맷으로 이관.

## 2. Domain Layer
*   **Entity**: `app/domain/entities/persona.py`
    *   `Persona` (dataclass): name, system_prompt 등.
*   **Interface**: `app/domain/repositories/persona_repository.py`
    *   `get_persona(name: str) -> Persona`

## 3. Infrastructure Layer
*   **Adapter**: `app/infrastructure/storage/file_persona_repository.py`
    *   `PyYAML` 등 사용하여 YAML 로딩.
    *   `get_persona` 구현.

## 4. App Layer Refactoring
*   **Brain Modification**: `app/infrastructure/llm/langgraph_adapter.py`
    *   `__init__`에서 `PersonaRepository` 주입 받도록 변경 (또는 초기화 시 로드).
    *   `_create_workflow` 내부에서 `CREATIVE_SYSTEM_PROMPT` 대신 `self.persona_repo.get_persona("creative").system_prompt` 사용.
*   **Dependency Injection**: `app/interfaces/mcp_server.py` 등에서 Repository 인스턴스 생성 및 주입.

## 5. Verification
*   **Unit Test**:
    *   `MockPersonaRepository`를 이용해 Brain 동작 테스트.
    *   YAML 로더 테스트.
*   **Manual**:
    *   `personas.yaml` 내용을 수정(예: 말투 변경) 후 앱 재시작하여 토론 실행 시 반영되는지 확인.
