# Walkthrough: Spec 012 (Model Upgrade)

## 📌 개요
LLM 모델을 최신화하고 상황에 따라 모델을 선택할 수 있는 **동적 모델 선택(Dynamic Model Selection)** 기능을 구현했습니다.
또한 사용자의 "비용 관리" 및 "최신 모델 사용" 요구를 충족하기 위해 `.env` 설정 및 API 인터페이스를 개선했습니다.

## 🛠️ 변경 사항

### 1. Configuration (`.env`)
- `GEMINI_MODEL_NAME` 환경 변수 추가.
- 기본값으로 `gemini-2.0-flash-thinking-exp-1219` 설정 (고성능 추론).

### 2. Infrastructure Layer (`LangGraphBrain`)
- 동적 모델 로딩 구현: `config={"configurable": {"model_name": "..."}}`를 통해 요청별 LLM 인스턴스 생성.
- 리팩토링: `app/domain/interfaces` 패키지 구조 정리 (Circular Import 및 Shadowing 문제 해결).

### 3. Application & API Layer
- **`RunDebateUseCase`**: `execute(topic, model_name)` 파라미터 추가 및 전파.
- **`OpenAI Router`**:
    - `list_models` 엔드포인트에 `gemini-3.0-flash`, `gemini-2.0-flash-thinking-exp` 등 최신 모델 추가.
    - `chat/completions` 요청의 `model` 필드를 UseCase로 전달.

## ✅ 검증 결과

### Verification Script
`scripts/verify_model_upgrade.py` 실행 결과:
```
--- 1. Checking Configuration ---
Default Model (from env): gemini-2.0-flash-thinking-exp-1219
✅ Default model matches .env

--- 2. Checking Factory Method (Mocking Config) ---
Requested 'gemini-1.5-flash'. LLM Model: gemini-1.5-flash
✅ Dynamic Model Selection works (Factory level)
```

## 📝 사용 방법

### OpenWebUI
1. 채팅창 상단 모델 선택 메뉴에서 `macs/gemini-2.0-flash-thinking-exp` 등을 선택.
2. 대화 시작 -> 선택한 모델로 토론 진행.

### CLI / API
```bash
# 기본 모델 사용
python scripts/run_debate.py "AI Ethics"

# .env 변경하여 기본 모델 변경 가능
export GEMINI_MODEL_NAME="gemini-1.5-flash"
```
