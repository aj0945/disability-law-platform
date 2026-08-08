Search Design

1. Purpose

The search system is designed to help users find legal grounds based on real-world disability rights issues, rather than requiring users to know the name or number of a law in advance.

The system should support both:

1. Precise legal research
2. Issue-based advocacy research

⸻

2. Search Modes

2.1 Legal Search

Users may search by:

* Law name
* Article number
* Article title
* Legal term
* Keyword

Example:

교통약자의 이동편의 증진법 제16조

The system should return the exact provision first.

⸻

2.2 Issue Search

Users may search using a practical issue.

Examples:

특별교통수단 법정대수
지원주택
활동지원 단가
탑승교 배치 의무
장애인 영화관람석

The system should identify relevant legal systems and provisions.

⸻

2.3 Rights Search

Users may search by a disability right.

Examples:

이동권
자립생활
주거권
교육권
노동권
건강권
접근권
차별금지

The system should return provisions associated with the relevant right.

⸻

2.4 Procedure Search

Users may search for what they can do in a specific situation.

Examples:

차별당했을 때 어떻게 해야 하나
장애인 차별 구제 절차
행정기관이 처분을 안 해줄 때
서비스 신청이 거부됐을 때

The system should prioritize:

* Procedures
* Responsible authorities
* Deadlines
* Required documents
* Appeals
* Complaints
* Litigation
* Other remedies

⸻

3. Search by Legal Hierarchy

Search results should preserve the relationship:

법률
 ↓
시행령
 ↓
시행규칙

Example:

교통약자의 이동편의 증진법
제16조
   ↓
시행령 제XX조
   ↓
시행규칙 제XX조

Users should be able to navigate between related provisions.

⸻

4. Search Result Structure

Each result should display:

법령명
조문번호
조문 제목
핵심 내용
의무 주체
대상
권리
제도
절차
구제
수치
원문 보기

The exact original provision must always be accessible.

⸻

5. Relevance Ranking

Search results should consider multiple signals.

Priority should generally be given to:

1. Exact legal citation
2. Exact article title
3. Exact legal terminology
4. Keyword match
5. Issue match
6. System match
7. Right match
8. Semantic similarity
9. Related provisions
10. Advocacy knowledge

Official legal sources should be prioritized over secondary sources.

⸻

6. Keyword Expansion

The system should recognize related terminology.

Example:

특별교통수단
↓
장애인콜택시
↓
교통약자 이동지원
↓
특별교통수단 운행

Another example:

지원주택
↓
장애인 지원주택
↓
주거지원
↓
지역사회 자립생활

Keyword expansion must not change the meaning of the user’s query.

Expanded terms should be identifiable in the search system.

⸻

7. Concept Search

The system should support searches based on concepts rather than exact wording.

Example:

User:

휠체어 이용자가 시외버스를 타고 싶다

Possible concepts:

장애인
휠체어
시외버스
접근성
교통
이동권
탑승
편의시설
차별

The system may use these concepts to identify relevant provisions.

⸻

8. Numerical Search

Users should be able to search for numerical requirements.

Examples:

특별교통수단 몇 대
장애인 관람석 몇 석
운행률 몇 퍼센트
신청 후 며칠
과태료 얼마

Results should prioritize provisions containing quantitative requirements.

⸻

9. Obligation Search

Users should be able to search for who is legally required to do something.

Examples:

국가가 해야 하는 것
지자체 의무
운송사업자 의무
학교의 장애인 편의 제공 의무
고용주의 의무

Results should identify:

* Obligation holder
* Required action
* Target
* Conditions
* Legal basis

⸻

10. Remedy Search

The system should support searches focused on enforcement and remedies.

Example:

장애인 차별을 당했다

Potential result structure:

1. 차별금지 규정
2. 구제 절차
3. 진정
4. 시정명령
5. 행정심판
6. 행정소송
7. 민사소송
8. 관련 기관

Each result must identify its legal basis.

⸻

11. Search Filters

Users should be able to filter results by:

Legal Type

* Law
* Enforcement Decree
* Enforcement Rule
* Administrative Rule
* International Standard
* Case

Information Type

* Right
* Obligation
* Procedure
* Remedy
* Numerical Requirement
* Definition
* Prohibition
* Authority

Subject

* Central Government
* Local Government
* Public Institution
* Employer
* School
* Transportation Operator
* Service Provider

Target

* Persons with Disabilities
* Wheelchair Users
* Persons with Developmental Disabilities
* Other groups

⸻

12. Search Result Explanation

AI-generated explanations must clearly distinguish:

Source

Original legal text.

Extraction

Information directly extracted from the text.

Analysis

AI-generated classification or relationship.

User Knowledge

Information contributed by authorized users.

Example:

[법령 원문]
제16조 ...
[AI 추출]
의무 주체: 지방자치단체
[AI 분석]
관련 제도: 특별교통수단
[활동가 자료]
2026년 입법 쟁점: ...

⸻

13. Source Traceability

Every search result must allow the user to answer:

“이 내용은 어디에 근거하고 있는가?”

The system should provide:

* Law name
* Article number
* Paragraph
* Source URL
* Effective date
* Original text

⸻

14. Version-Aware Search

Search results must take legal validity dates into account.

The system should distinguish:

* Current provision
* Future provision
* Historical provision
* Repealed provision

Users should be able to search according to a specific date when necessary.

Example:

2024년 당시 특별교통수단 법정대수

⸻

15. Internal Knowledge Search

Authorized users may search internal organizational knowledge.

Examples:

국토부 특별교통수단 협의
2026년 예산
국감 자료
소송 준비

Internal information must never appear in results for unauthorized users.

⸻

16. Search Suggestions

The system may provide suggested searches.

Example:

User:

지원주택

Suggestions:

지원주택 관련 법
지원주택 국가 의무
장애인 지원주택 대상
지원주택 관련 시행령
지원주택 구제절차
지원주택 해외 입법례

⸻

17. No-Result Behavior

If no reliable legal provision is found, the system must not fabricate an answer.

Instead:

직접적으로 일치하는 법적 근거를 찾지 못했습니다.
다음 검색어를 시도해보세요:
- 관련 제도명
- 관련 권리
- 의무 주체
- 유사한 법적 용어

⸻

18. Search Philosophy

The platform should support the following research flow:

현실의 문제
     ↓
키워드
     ↓
쟁점
     ↓
제도
     ↓
법령
     ↓
조문
     ↓
의무 / 권리 / 수치 / 절차
     ↓
구제 또는 입법 근거

The user should not need to know the legal terminology in advance.

⸻

19. Core Principle

The search system is not merely a legal document search engine.

It is a tool for moving between:

현장의 문제 ↔ 법적 근거 ↔ 권리 ↔ 제도 ↔ 구제 ↔ 입법

while always preserving the original legal source.
