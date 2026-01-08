The Constitution defines the invariant laws of this project. All Agents MUST comply with these rules at all times. This document takes precedence over all other instructions.

---

## 1. Authority & Decision Model

### 1.1 Roles

- User: Final decision maker and sole merge authority.
    
- Agent: Delegated executor within explicitly approved boundaries.
    

### 1.2 Decision Ownership

- The Agent MAY propose options.
    
- The User MUST approve: Work Mode (SDD/FF), Spec scope, Plan (execution contract), and Pull Request merge.
    
- The Agent MUST NOT self-approve any of the above.
    

## 2. Work Modes

### 2.1 Mode A — SDD (Spec-Driven Development)

- REQUIRED for: New features, architectural changes, non-trivial refactoring, and any change producing a PR.
    

### 2.2 Mode B — FF (Fast Flow)

- ONLY with explicit user approval.
    
- LIMITED to: Small, reversible changes, experiments, documentation, and one-off scripts.
    
- MUST NOT: Introduce architectural decisions, bypass Clean Architecture rules, or skip tests.
    

## 3. Alignment Requirement (Mandatory)

Before any Spec, Plan, or execution:

1. Agent MUST present: Intent understanding, Work Mode options, and Recommendation with reasoning.
    
2. User MUST explicitly select a mode.
    

- No mode is valid without explicit user confirmation.
    

## 4. Spec, Plan, and PR Contract

### 4.1 Spec Rules

- A Spec represents a single Pull Request.
    
- One Spec MUST NOT produce multiple PRs.
    
- If scope exceeds a single PR, the Spec MUST be split and overflow moved to Backlog.
    

### 4.2 Plan Rules

- A Plan is an execution contract defining: Scope boundaries, affected files, Task list, commit granularity, and test expectations.
    
- No execution is allowed without an approved Plan.
    

## 5. Execution Delegation

### 5.1 Delegation Rule

Once a Plan is explicitly accepted (Plan Accept), the Agent is authorized to:

- Execute all Tasks in tasks.md, commit per Task, add/run tests, and create a PR without further confirmation.
    

### 5.2 Delegation Limits

- Valid ONLY if execution stays within Plan scope, preserves Clean Architecture, and requires no new decisions.
    
- Any deviation MUST immediately stop execution and require re-alignment.
    

## 6. Accept Semantics

### 6.1 Plan Accept (Execution Authorization)

- Grants execution authority (Tasks, commits, tests, PR creation).
    
- Does NOT imply approval of final results.
    

### 6.2 PR Merge Accept (Final Approval)

- Grants permission to merge. ONLY given by the User. Independent of Plan Accept.
    

## 7. Task & Commit Integrity

- Each Task in tasks.md represents one logical unit of work.
    
- Agent MUST commit per Task. Batch commits are PROHIBITED.
    
- Commit history MUST reflect Task intent and order.
    

## 8. Testing & Quality Gate (Commit-Level TDD)

### 8.1 Test Requirement

- For testable behavior: Tests MUST be added/updated and executed before Task completion.
    
- A Task without tests is considered INCOMPLETE.
    

### 8.2 Test Exception Rule

- Omission allowed ONLY if not reasonably testable (e.g., docs, config).
    
- Agent MUST explicitly document the reason for omission. Unjustified omission is a violation.
    

## 9. Clean Architecture (Invariant)

- Dependency Rule: Source code dependencies MUST point inwards only.
    
- Layer violations (Entities, Use Cases, Adapters, Frameworks) are PROHIBITED.
    
- Any violation requires immediate correction or execution halt.
    

## 10. Git & Pull Request Law

- All work MUST be done on non-main branches created from main.
    
- Merge authority belongs exclusively to the User. Agent MUST NOT merge.
    
- One PR = One Spec. PR size MUST remain reviewable.
    

## 11. Backlog Law

- Backlog items are NON-EXECUTABLE.
    
- MUST NOT produce code changes, tasks, or commits until promoted to a Spec.
    
- Promotion requires explicit user approval.
    

## 12. Enforcement

- Violation invalidates current execution and overrides all other instructions.
    
- Requires immediate stop and user re-alignment. No exceptions without explicit user consent.