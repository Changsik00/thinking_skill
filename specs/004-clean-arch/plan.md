# Implementation Plan: Core Refactoring

## 1. Goal
비즈니스 로직(토론 흐름 관리)을 인프라(LangGraph, 파일시스템, n8n)로부터 격리한다.

## 2. Proposed Changes

### Domain Layer (New)
#### [NEW] [app/domain/entities.py](file:///Users/ck/Project/Thingking/app/domain/entities.py)
- `DiscussionResult`: 토론 결과 (content, metadata).

#### [NEW] [app/domain/interfaces.py](file:///Users/ck/Project/Thingking/app/domain/interfaces.py)
- `ThinkingBrain`: LLM/Graph 인터페이스 (`think(topic) -> str`).
- `MemoryVault`: 저장소 인터페이스 (`save(topic, content)`).
- `NerveSystem`: 자동화 인터페이스 (`trigger(topic, content)`).

### Use Case Layer (New)
#### [NEW] [app/usecases/run_debate.py](file:///Users/ck/Project/Thingking/app/usecases/run_debate.py)
- `RunDebateUseCase`: `execute(topic)` 메서드 구현.
- 생성자에서 `ThinkingBrain`, `MemoryVault`, `NerveSystem` 주입 받음.

### Infrastructure Layer (Migration)
#### [MOVE/REFACTOR] agents/graph.py -> app/infrastructure/llm/langgraph_adapter.py
- `LangGraphBrain` 클래스로 래핑하여 `ThinkingBrain` 구현.

#### [MOVE/REFACTOR] utils/storage.py -> app/infrastructure/storage/local_adapter.py
- `LocalStorage` 및 `ChromaStorage` 클래스로 래핑하여 `MemoryVault` 구현.

#### [MOVE/REFACTOR] utils/automation.py -> app/infrastructure/automation/n8n_adapter.py
- `N8nNerve` 클래스로 래핑하여 `NerveSystem` 구현.

### Interface Layer
#### [MODIFY] agents/runner.py -> app/interfaces/cli/runner.py
- UseCase를 조립(Composition)하고 실행하는 역할로 변경.

## 3. Verification Plan
- **Integration**: `uv run python -m app.interfaces.cli.runner "Refactor Test"` 실행 시 기존과 동일한 결과가 나와야 함.
