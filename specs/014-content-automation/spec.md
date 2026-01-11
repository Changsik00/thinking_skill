# Spec 014: Content Automation (Infrastructure)

## 🎯 Background (배경)
현재 시스템은 토론 결과를 로컬 파일로 저장하는 것까지 가능합니다.
사용자는 토론 결과를 바탕으로 슬랙 공유, 블로그 포스팅 등 2차 활용(Content Creation)을 원합니다.
이를 위해 워크플로우 자동화 도구인 **n8n**과의 연동을 강화해야 합니다.

## 🥅 Goal (목표)
- Brain(에이전트)이 의도에 따라 **n8n Webhook**을 트리거할 수 있어야 합니다.
- **Dry Run / Local Verification**: 실제 외부 서비스(Slack 등)로 메시지를 쏘는 대신, n8n까지 데이터가 도달하는지(Connection)를 로컬에서 검증하는 것을 목표로 합니다.

## 📋 Requirements (요구사항)
1. **Tooling**: Brain이 사용할 수 있는 `trigger_automation` 도구 추가.
    - 파라미터: `target` (e.g., "slack", "blog"), `content` (요약 내용).
2. **Infrastructure**: `N8nAdapter`가 페이로드를 구성하여 n8n Webhook URL로 POST 요청 전송.
3. **Verification**: n8n 컨테이너에서 Webhook 수신 로그 확인 또는 Mock Server 응답 확인.

## 📏 Success Criteria (성공 기준)
- OpenWebUI에서 "이거 슬랙으로 보내줘"라고 요청했을 때,
- Brain이 `trigger_automation` 도구를 호출하고,
- `N8nAdapter`가 성공적으로 HTTP POST 요청을 보내며,
- 결과적으로 "자동화 트리거 성공" 응답이 돌아와야 합니다.
