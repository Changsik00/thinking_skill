# Spec 016: DevOps Automation (CI)

## 🎯 목적 (Goal)
GitHub Actions를 도입하여 코드가 푸시될 때마다 자동으로 테스트를 실행하고, 프로젝트의 신뢰성을 확보합니다.

## 🛠 변경 사항 (Changes)
### 1. Infrastructure Layer (`.github/workflows/test.yml`)
- **CI 파이프라인 구축**: `uv` 패키지 매니저를 사용하여 의존성을 설치하고 `pytest`를 실행하는 워크플로우 생성.
- **Trigger**: `main` 브랜치 및 `feat/**` 기능 브랜치 푸시 시 동작.
- **Env Fix**: 테스트 실행에 필요한 환경변수(`GEMINI_API_KEY`) 더미 값 주입.

### 2. Regression Fixes (Test)
CI 도입 과정에서 발견된 기존 테스트 코드의 노후화(Signature 불일치)를 수정했습니다.
- `tests/unit/interfaces/test_openai_router.py`: Mock Generator에 `model_name` 인자 추가.
- `test/mocks/fake_adapters.py`: `FakeBrain`의 `think/think_stream` 메서드에 `model_name` 인자 추가.
- `tests/unit/usecases/test_run_debate.py`: Spec 013(자동 저장 제거) 변경 사항을 반영하여 테스트 로직 수정.

### 3. Documentation (`README.md`)
- **Build Status Badge**: 타이틀 하단에 GitHub Actions 상태 배지 추가.

## ✅ 검증 (Verification)
- [x] **Local Test**: `uv run pytest` 전체 통과 (23 passed).
- [x] **CI Test**: GitHub Actions 워크플로우 통과 (Green).

## 📝 리뷰 포인트
- CI 워크플로우 설정(`.yml`)이 적절한지 확인 부탁드립니다.
- 테스트 코드 수정 사항이 기존 의도를 해치지 않는지 검토 바랍니다.
