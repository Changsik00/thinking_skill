# Spec 020: Linting & Formatting Automation

## 1. 개요 (Overview)
Python 코드의 스타일 일관성을 유지하고, `IndentationError`와 같은 구문 오류를 사전에 방지하기 위해 **Ruff** 기반의 Linting 및 Formatting 자동화를 도입합니다.

## 2. 문제 정의 (Problem Statement)
*   **코드 스타일 불일치**: 여러 파일에서 들여쓰기 방식이나 import 순서가 제각각일 수 있습니다.
*   **잠재적 버그**: 최근 `Spec 019` 과정에서 발생한 `IndentationError`처럼, 육안으로 확인하기 어려운 오류가 CI 단계에서 발견되어 개발 속도를 저해합니다.
*   **수동 프로세스**: 개발자가 직접 포맷팅을 신경 써야 하므로 생산성이 저하됩니다.

## 3. 목표 (Goals)
*   **Ruff 도입**: 단일 도구로 Linting, Formatting, Import Sorting을 모두 처리합니다.
*   **Configuration**: `pyproject.toml`에 Ruff 설정을 중앙 집중화합니다.
*   **Automation**: `Makefile` 또는 `uv run` 명령어로 손쉽게 실행할 수 있도록 합니다.
*   **CI Integration**: GitHub Actions(`test.yml`)에 Lint 단계를 추가하여, 스타일 가이드를 위반한 코드는 병합되지 않도록 합니다.

## 4. 논-골 (Non-Goals)
*   **Legacy Code Reform**: 기존 코드 전체를 한 번에 완벽하게 고치는 것은 목표가 아닙니다 (점진적 적용). 다만, 자동 수정 가능한(Auto-fixable) 항목은 적용합니다.
*   **Pre-commit Hooks**: 이번 Spec에서는 로컬 명령어와 CI 설정까지만 다룹니다 (Pre-commit은 선택 사항).
