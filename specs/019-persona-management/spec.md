# Spec 019: Persona Management System

## 1. 개요 (Overview)
현재 하드코딩된 Python 문자열(`app/infrastructure/llm/prompts.py`)로 관리되는 에이전트 페르소나(시스템 프롬프트)를 외부 설정 파일(`YAML`)로 분리하고, 이를 동적으로 로드하여 관리하는 시스템을 구축합니다.

## 2. 문제 정의 (Problem Statement)
*   **유연성 부족**: 페르소나(성격, 말투, 역할)를 수정하려면 코드를 직접 수정하고 배포해야 합니다.
*   **확장성 제한**: 새로운 페르소나(예: "친절한 멘토", "소크라테스")를 추가하기 어렵습니다.
*   **운영 비효율**: 비개발자가 프롬프트를 튜닝하거나 관리할 수 없습니다.

## 3. 목표 (Goals)
*   **Configuration**: `configs/personas.yaml` 파일에서 페르소나를 정의하고 수정할 수 있어야 합니다.
*   **Dynamic Loading**: 애플리케이션 시작 시(또는 실행 시) 설정을 읽어와 `LangGraphBrain`에 적용해야 합니다.
*   **Maintainability**: 기존 `prompts.py`의 하드코딩을 제거하고, Clean Architecture에 맞춰 Repository 패턴으로 페르소나를 제공합니다.

## 4. 논-골 (Non-Goals)
*   **Hot Reloading**: 파일 수정 시 실시간 반영 (이번 Spec에서는 재시작을 전제로 함, 추후 개선).
*   **UI Editor**: 웹 대시보드에서 직접 수정하는 UI (추후 Spec으로 미룸). 일단은 파일 기반 관리.

## 5. 설계 (Design)

### 5.1. Config Structure (`personas.yaml`)
```yaml
personas:
  creative:
    name: "creative_diverger"
    display_name: "창의적 발산가"
    system_prompt: |
      당신은 '창의적 발산가'입니다...
  critical:
    name: "critical_converger"
    display_name: "냉철한 비평가"
    system_prompt: |
      당신은 '냉철한 비평가'입니다...
```

### 5.2. Architecture Change
*   **Existing**: `LangGraphBrain` imports `CREATIVE_SYSTEM_PROMPT` (Global Constant).
*   **New**: `LangGraphBrain` injects `PersonaRepository` interface.
    *   `Domain`: `Persona` (Entity), `PersonaRepository` (Interface).
    *   `Infrastructure`: `FilePersonaRepository` (Adapter implementation using YAML).
