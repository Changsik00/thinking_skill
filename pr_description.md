# PR: Spec 014 - 콘텐츠 자동화 (Content Automation via n8n)

## 📌 개요
토론 결과를 외부 서비스(Slack, Blog 등)로 확장하기 위한 **자동화 인프라**를 구축했습니다.
Brain(에이전트)이 스스로 `trigger_automation` 도구를 사용하여 n8n Webhook을 호출할 수 있게 되었습니다.

## 🛠️ 변경 사항

### 1. Infrastructure Layer (`N8nAdapter`)
- **[MODIFY]** `trigger` 메서드: `target` 파라미터 추가. 슬랙, 이메일 등 목적지에 따라 페이로드를 구성하여 n8n으로 전송.

### 2. Application Layer (`LangGraphBrain`)
- **[NEW]** `trigger_automation` 도구: 에이전트가 사용할 수 있는 새 도구 정의.
- **[MODIFY]** `LangGraphBrain`: `nerve` (N8nAdapter) 의존성을 주입받아 도구 바인딩.

### 3. Example Workflow
- **[NEW]** `specs/014-content-automation/n8n-workflow-example.json`: n8n에 바로 Import하여 테스트할 수 있는 예제 워크플로우 제공. (Webhook -> Route -> Slack/Email Mock)

## 🧪 검증 (Verification)
- **Unit Test**: `uv run pytest tests/infrastructure/automation/test_n8n_trigger.py` (Pass)
    - `test_trigger_success`: 정상 페이로드 전송 확인.
    - `test_trigger_failure`: 404/500 에러 처리 확인.
    - `test_no_env_var`: 환경변수 누락 시 경고 처리 확인.
- **Manual Test**: 로컬 n8n 컨테이너와 연동하여 데이터 수신 확인 완료.

## 📝 리뷰 포인트
- `N8nAdapter`의 `target` 처리 로직 확장성.
- `LangGraphBrain`의 도구 조건부 바인딩 방식.
