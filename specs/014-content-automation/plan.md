# Plan 014: Content Automation

## 1. Preparation
- [ ] `backlog/queue.md` 업데이트 (Spec 014를 Now로 이동).
- [ ] n8n Webhook URL 환경변수 확인 (`.env`).

## 2. Infrastructure Layer (`LangGraphBrain` & `N8nAdapter`)
- [ ] **`n8n_adapter.py` 개선**:
    - `trigger(result, target: str)` 메서드 시그니처 변경 (Target 구분).
    - 다양한 Payload(Target에 따라 다름) 구성 로직 추가.
- [ ] **`LangGraphBrain` 도구 추가**:
    - `_create_automation_tool` 메서드 추가.
    - `trigger_automation(target, summary)` 도구 정의.
    - `bind_tools` 목록에 추가. (MemoryVault가 있을 때와 유사하게 N8nAdapter가 있을 때 바인딩).

## 3. Configuration (`mcp_server.py`)
- [ ] `LangGraphBrain` 초기화 시 `N8nAdapter` 주입(이미 되어있는지 확인, 안되어 있다면 생성자 수정).
- [ ] `mcp_server.py`에서 `N8nAdapter` 인스턴스를 Brain에 전달.

## 4. Verification
- [ ] **Test Script (`tests/infrastructure/automation/test_n8n_trigger.py`)**:
    - Mock Server(또는 `requests-mock`)를 사용하여 `N8nAdapter`가 올바른 URL과 Payload로 요청을 보내는지 검증.
- [ ] **Integration Test (Manual)**:
    - n8n 로컬 컨테이너에 "Webhook" 노드 하나 띄워두고 URL 획득.
    - `.env`에 해당 URL 설정.
    - 스크립트로 `trigger_automation` 실행하여 n8n UI에서 수신 확인.
