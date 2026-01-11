# Plan: Spec 012 - 모델 업그레이드

## 1. 개요
LLM 모델을 `gemini-2.0-flash-001`에서 최신 `gemini-2.0-flash-thinking-exp-1219` (또는 해당 시점 최신 버전)으로 변경하고, `.env`를 통해 설정 가능하도록 개선합니다.

## User Review Required
> [!IMPORTANT]
> **Gemini 2.0 Flash Thinking** 모델은 Experimental 버전이므로 안정이 보장되지 않을 수 있습니다.
> 문제 발생 시 `.env`를 수정하여 언제든지 Stable 버전(`gemini-1.5-flash` 등)으로 롤백할 수 있습니다.

## 2. 변경 사항 (Proposed Changes)

### Global Configuration
#### [MODIFY] `.env.example`
- `GEMINI_MODEL_NAME` 변수 추가.
- 주석으로 다음 프로필 예시 제공:
  ```bash
  # [High Performance] Thinking Model (Experimental) - Best for reasoning
  GEMINI_MODEL_NAME=gemini-2.0-flash-thinking-exp-1219
  
  # [Cost Effective] Flash 1.5 - Best for speed & free tier
  # GEMINI_MODEL_NAME=gemini-1.5-flash
  ```

### Interface Layer (Core)
#### [MODIFY] `app/domain/interfaces.py`
- `ThinkingBrain.think(topic: str, model_name: Optional[str] = None)`
- `ThinkingBrain.think_stream(topic: str, model_name: Optional[str] = None)`

### Infrastructure Layer
#### [MODIFY] `app/infrastructure/llm/langgraph_adapter.py`
- `__init__`: Read default model from env `GEMINI_MODEL_NAME`.
- `think` / `think_stream`: Accept `model_name` param.
- **Dynamic Logic**:
    - LangGraph Node(`_creative_node`, `_critical_node`)에서 `state` 또는 `config`를 통해 모델명을 전달받아야 함.
    - `configurable` 필드를 활용하여 Graph 실행 시점에 모델명을 주입.
    - Node 내부에서 `model_name`이 변경된 경우 새로운 LLM 인스턴스 생성 (또는 캐싱).

### Application Layer
#### [MODIFY] `app/usecases/run_debate.py`
- `execute(topic, model_name=None)`: Brain에 model_name 전달.
- `execute_stream(topic, model_name=None)`: Brain에 model_name 전달.

### Interface Layer (API)
#### [MODIFY] `app/interfaces/api/openai_router.py`
- `OpenAIChatRequest`의 `model` 필드 값을 `use_case.execute_stream`에 전달.
- `list_models` 엔드포인트 업데이트:
    - `gemini-3.0-flash` (예시)
    - `gemini-2.0-flash-thinking-exp`
    - `gemini-2.0-flash-001`
    - 등 최신 모델 목록 반환.

## 3. 검증 계획 (Verification Plan)

### Manual Verification
1. `.env`에 `GEMINI_MODEL_NAME=gemini-2.0-flash-thinking-exp-1219` 설정.
2. `python scripts/run_debate_cli.py --topic "AI Ethics"` 실행.
3. 정상적으로 토론이 진행되는지 확인.
4. (가능하다면) 로그에서 `Thinking Process`가 발생하는지 확인 (모델 특성상 응답에 `<thinking>` 태그 등이 포함될 수 있음).
