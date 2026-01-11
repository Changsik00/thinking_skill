# Spec 012: 모델 업그레이드 및 설정 유연화 (Model Upgrade)

## 1. 개요 (Overview)
현재 Thingking 시스템의 두뇌(`LangGraphBrain`)는 `gemini-2.0-flash-001` 모델을 기본값으로 사용하며, 코드를 수정하지 않고는 모델을 변경하기 어렵습니다.
사용자의 요청("Gemini 3 Migration")에 따라 최신 **Thinking Model**을 적용하여 추론 능력을 강화하고, 향후 모델 변경이 용이하도록 설정을 유연화합니다.

## 2. 문제 정의 (Problem Statement)
- **하드코딩**: `langgraph_adapter.py`에 모델명(`gemini-2.0-flash-001`)이 하드코딩되어 있습니다.
- **성능 한계**: 기본 Flash 모델은 복잡한 추론(Thinking)이 필요한 토론 시나리오에서 깊이 있는 논쟁을 전개하는 데 한계가 있습니다.

## 3. 제안 솔루션 (Proposed Solution)

### 3.1 환경 변수 기반 유연한 설정
- `GEMINI_MODEL_NAME`을 통해 모델을 변경할 수 있도록 수정합니다.
- `.env.example`에 **비용 효율 (Cost-Effective)** vs **고성능 (High-Performance)** 옵션을 주석으로 명시하여 사용자가 선택하기 쉽게 합니다.

### 3.2 모델 옵션 제안
- **High Performance**: `gemini-2.0-flash-thinking-exp-1219` (추론 강화)
- **Cost Effective**: `gemini-1.5-flash` (빠르고 저렴/무료)

### 3.3 동적 모델 선택 (Dynamic Selection)
- OpenWebUI 등 클라이언트에서 요청 시 모델을 지정하면, 해당 모델로 토론을 수행할 수 있도록 인터페이스를 개선합니다.
    - `ThinkingBrain.think(topic, model_name=None)`
    - `ThinkingBrain.think_stream(topic, model_name=None)`
- 모델명이 없으면 `.env`의 기본값을 사용합니다.

## 4. 범위 (Scope)

### 포함 (In Scope)
- `LangGraphBrain` 초기화 로직 수정.
- `.env` 및 `.env.example` 파일 업데이트.
- 모델 변경 후 간단한 토론 테스트.

### 제외 (Out of Scope)
- Thinking Process 시각화 (Thinking 토큰 스트리밍 처리 등은 별도 Spec으로 분리 권장).
- 다른 제공자(OpenAI, Anthropic) 추가.

## 5. 성공 기준 (Success Criteria)
- `.env` 파일에서 `GEMINI_MODEL_NAME`을 변경하면 시스템이 해당 모델을 로드해야 함.
- 토론 실행 시 `gemini-2.0-flash-thinking-exp`(또는 최신) 모델이 정상 동작해야 함.
