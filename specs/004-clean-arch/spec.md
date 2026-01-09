# Spec 004: Core Refactoring (Clean Architecture)

## 1. Intent (의도)
**"튼튼한 뼈대를 세운다."**
현재의 스크립트 기반 코드를 **Layered Architecture** (Clean Architecture 지향)로 리팩토링하여, 비즈니스 로직과 외부 의존성(LangGraph, Chroma, n8n)을 분리합니다. 이는 향후 FastAPI 연결 및 유지보수를 용이하게 하기 위함입니다.

## 2. Scope (범위)

### 2.1. In-Scope
- **Domain Layer**: 엔티티 및 인터페이스 정의 (Pure Python).
- **Use Case Layer**: 비즈니스 로직 캡슐화 (`RunDebateUseCase`).
- **Infrastructure Layer**: 구현체 이동 및 어댑터 패턴 적용 (`LangGraphAdapter`, `ChromaRepository`, `N8nAdapter`).
- **Interfaces Layer**: 컨트롤러 역할 (`CLIController`).

### 2.2. Out-of-Scope
- **FastAPI Server**: Spec 005에서 진행.
- **New Features**: 기능 추가 없음 (기존 로직 유지).

## 3. Architecture Design

### 3.1. Directory Structure
```
app/
├── domain/             # Entities, Interfaces (No external deps)
│   ├── entities.py     # Topic, DebateResult
│   └── interfaces.py   # LlmPort, StoragePort, AutomationPort
├── usecases/           # Application Business Rules
│   └── run_debate.py   # RunDebateUseCase
├── infrastructure/     # Frameworks & Drivers
│   ├── llm/            # LangGraph Implementation
│   ├── storage/        # File/Chroma Implementation
│   └── automation/     # n8n Implementation
└── interfaces/         # Interface Adapters
    └── cli/            # Current runner.py logic
```

### 3.2. Components
- **Topic (Entity)**: 주제와 관련 메타데이터.
- **RunDebateUseCase**:
    - Input: `topic_text`
    - Logic:
        1. LLM으로 토론 진행 (via LlmPort).
        2. 결과 저장 (via StoragePort).
        3. 결과 전송 (via AutomationPort).
    - Output: `DebateResult`

## 4. Verification Plan (검증 계획)
- **Refactoring Verification**: 기존 `uv run python -m agents.runner` 명령어가 리팩토링 후에도 **동일하게 동작**해야 함.
- **Dependency Check**: `domain` 폴더 내에서 외부 라이브러리(`langchain` 등) import가 없어야 함.
