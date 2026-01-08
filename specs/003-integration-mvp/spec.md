# Spec 003: Integration MVP

## 1. Intent (의도)
**"생각을 기록하고 행동으로 연결한다."**
[Phase 2]에서 검증된 LangGraph의 토론 결과를 휘발성 메모리(RAM)에서 꺼내, 영구 저장소(File/DB)에 저장하고 외부 자동화 툴(n8n)로 전달하는 것이 목표입니다.

## 2. Scope (범위)

### 2.1. In-Scope
- **File Archiving**: 토론이 끝나면 `data/archives/{Timestamp}_{Topic}.md` 파일로 저장.
- **ChromaDB Integration**: 토론의 핵심 요약(Summary)과 전체 맥락을 벡터 임베딩으로 저장.
- **n8n Webhook**: 토론이 완료되면 n8n 웹훅을 호출하여 알림(Mock)을 보냄.

### 2.2. Out-of-Scope
- OpenWebUI 연동 (Phase 4).
- 복잡한 RAG 검색 로직 (저장만 먼저 구현).
- 실제 n8n 자동화 워크플로우 (이메일 발송 등은 n8n 측 설정이므로 여기서는 트리거만).

## 3. Implementation Details (구현 상세)

### 3.1. Archiving (Markdown)
- `agents/runner.py` 종료 시점에 **최종 결과(Critical Agent의 마지막 응답)**만 파일로 저장.
- 포맷:
  ```markdown
  # Topic: {Topic}
  Date: {YYYY-MM-DD HH:mm:ss}
  
  ## Final Conclusion
  {Critical Agent's Response}
  ```

### 3.2. ChromaDB
- `chromadb` 클라이언트 사용.
- Collection Name: `macs_discussions`.
- Data: `documents=[full_text]`, `metadatas=[{'topic': topic, 'timestamp': ts}]`.

### 3.3. n8n Webhook
- `requests.post(N8N_WEBHOOK_URL, json={...})`.
- `.env`에 `N8N_WEBHOOK_URL` 추가.

## 4. Verification Plan (검증 계획)

### 4.1. Automated
- 없음 (단위 테스트 프레임워크 도입 전).

### 4.2. Manual
1. **Archive Check**: `uv run python -m agents.runner "Test"` 후 `data/archives/`에 파일 생성 확인.
2. **ChromaDB Check**: Python 쉘에서 ChromaDB 조회하여 데이터 유입 확인.
3. **n8n Check**: n8n 대시보드에서 실행 로그 확인.

## 5. Constraints
- Docker 컨테이너(`chroma`, `n8n`)가 실행 중이어야 함.
- 로컬 파일 시스템 권한 필요.
