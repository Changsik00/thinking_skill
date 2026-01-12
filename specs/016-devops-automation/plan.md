# Plan 016: DevOps Automation

## Goal Description
GitHub Actions를 도입하여 코드가 푸시될 때마다 자동으로 유닛 테스트(`pytest`)를 실행하는 CI 파이프라인을 구축합니다.

## User Review Required
> [!NOTE]
> **Dependency Manager**: 프로젝트가 `uv`를 사용하므로, CI 환경에서도 `uv`를 설치하고 의존성을 관리하도록 구성합니다.

## Proposed Changes

### Infrastructure
#### [NEW] [.github/workflows/test.yml](file:///Users/ck/Project/Thingking/.github/workflows/test.yml)
- **Trigger**: `push` (branches: main), `pull_request` (branches: main)
- **Steps**:
    1. Checkout code
    2. Install uv
    3. Set up Python
    4. Install dependencies (`uv sync`)
    5. Run tests (`uv run pytest`)

### Documentation
#### [MODIFY] [README.md](file:///Users/ck/Project/Thingking/README.md)
- Badges 섹션에 'Build Status' 추가 (Optional, 추후 PR 시점에 추가).

## Verification Plan

### Automated Verification
- **GitHub Actions**: 이 브랜치를 푸시했을 때 GitHub Actions 탭에서 워크플로우가 성공(Green Check)하는지 확인.

### Manual Verification
- 로컬에서 `uv run pytest`가 통과하는지 선행 확인.
