AI Tagging Specification

1. Purpose

This document defines how the Disability Law Platform analyzes and structures legal information using AI.

The purpose of AI analysis is to make legal information easier to search, connect, and understand.

AI must not replace legal interpretation. It must extract, classify, and connect information while preserving the original legal source.

⸻

2. Core Principles

2.1 Source First

The original legal text is the primary source.

AI-generated information must always be traceable to the original source.

AI must not alter the meaning of the original provision.

⸻

2.2 Legal Metadata and AI Analysis Are Separate

Information directly obtained from an official source must be stored separately from information generated or classified by AI.

Official Legal Metadata

Examples:

* Law name
* Type of legislation
* Article number
* Paragraph number
* Subparagraph number
* Item number
* Article title
* Enforcement date
* Amendment date
* Amendment history
* Annex or attached forms
* Original text
* Official source

These values should be obtained from authoritative sources whenever possible.

AI must not invent or modify legal identifiers.

AI-Generated Information

Examples:

* Related right
* Related issue
* Related system
* Obligation
* Target group
* Responsible entity
* Procedure
* Remedy
* Numerical requirement
* Related international standards

AI-generated information must be linked to the source provision.

⸻

3. Legal Hierarchy

The system must preserve the relationship between different levels of legislation.

Example:

Law
 └── Enforcement Decree
      └── Enforcement Rule

The system should allow users to move between related provisions.

Example:

Transportation Accessibility Act
Article 16
        ↓
Enforcement Decree
Article XX
        ↓
Enforcement Rule
Article XX

The system must distinguish between:

* Law
* Enforcement Decree
* Enforcement Rule
* Administrative rules
* Public notices
* Local ordinances (future or optional scope)

⸻

4. Legal Citation Tags

Every provision must preserve its precise citation.

Required fields:

* law_name
* law_type
* article
* paragraph
* subparagraph
* item
* article_title
* effective_date
* amendment_date
* source_url

Example:

교통약자의 이동편의 증진법
제16조
제1항

The platform should allow users to copy a complete legal citation.

⸻

5. Core Semantic Tags

5.1 Right

The fundamental right or interest related to the provision.

Examples:

* Accessibility
* Mobility
* Independent living
* Education
* Employment
* Health
* Housing
* Participation
* Equality and non-discrimination
* Information access

⸻

5.2 Issue

The practical issue addressed by the provision.

Examples:

* Special transportation
* Supported housing
* Personal assistance
* Assistive technology
* Accessible transportation
* Boarding assistance
* Reasonable accommodation
* Discrimination
* Deinstitutionalization

⸻

5.3 System

The specific legal or administrative system established by the provision.

Examples:

* Special transportation system
* Personal assistance service
* Supported housing
* Assistive technology support
* Disability employment quota

⸻

5.4 Subject

The person or organization responsible for an obligation or empowered to act.

Examples:

* Central government
* Local government
* Minister
* Mayor
* Public institution
* Transportation operator
* Employer
* School
* Service provider

⸻

5.5 Target

The person or group protected, supported, or affected.

Examples:

* Persons with disabilities
* Persons with mobility difficulties
* Wheelchair users
* Persons with developmental disabilities
* Children with disabilities
* Older persons
* Caregivers

⸻

5.6 Obligation

An action that a legal subject is required to perform.

Examples:

* Establish
* Provide
* Operate
* Install
* Maintain
* Support
* Accommodate
* Investigate
* Report
* Prepare a plan

⸻

5.7 Prohibition

Actions that are prohibited.

Examples:

* Discrimination
* Refusal of service
* Denial of reasonable accommodation
* Unlawful restriction of access

⸻

5.8 Authority

A power or discretion granted to an institution or official.

Examples:

* Approve
* Designate
* Order
* Inspect
* Investigate
* Issue a permit
* Impose an administrative sanction

⸻

6. Procedure Tags

The system should identify procedures established by law.

Examples:

* Application
* Registration
* Eligibility determination
* Assessment
* Notification
* Appeal
* Administrative review
* Complaint
* Investigation
* Mediation
* Litigation

The system should identify:

1. Who initiates the procedure
2. Who receives the application or complaint
3. Required documents
4. Time limits
5. Decision-making authority
6. Appeal or review mechanisms

⸻

7. Remedy Tags

The system must identify possible remedies and enforcement mechanisms.

Examples:

* Administrative appeal
* Administrative litigation
* Civil litigation
* Discrimination complaint
* Human rights complaint
* Corrective order
* Administrative sanction
* Criminal penalty
* Compensation
* Restoration of rights

Where possible, the system should identify the relevant legal provision and authority.

⸻

8. Numerical and Quantitative Tags

Numbers are particularly important for policy and advocacy research.

The system should extract:

* Required number
* Minimum number
* Maximum number
* Percentage
* Ratio
* Distance
* Area
* Age
* Time period
* Deadline
* Frequency
* Capacity
* Monetary amount
* Calculation formula

Example:

Minimum required vehicles: XX
Ratio: 1 vehicle per XX persons
Deadline: within XX days
Penalty: up to XX won

The original wording and unit must be preserved.

⸻

9. Condition Tags

The system should identify conditions that limit or determine the application of a provision.

Examples:

* Eligibility requirements
* Disability type
* Degree of disability
* Age
* Income
* Geographic area
* Institutional status
* Service registration
* Prior application
* Emergency circumstances

⸻

10. Related Provisions

The system should identify relationships between provisions.

Relationship types may include:

* Implements
* Refers to
* Defines
* Exceptions to
* Provides a procedure for
* Provides a penalty for
* Expands
* Limits
* Repeals
* Supersedes

Example:

Law Article 16
        ↓ implements
Enforcement Decree Article XX

⸻

11. International Standards

The system should allow legal provisions to be connected to international disability rights standards.

Examples:

* UN Convention on the Rights of Persons with Disabilities
* CRPD Article
* General Comment
* Concluding Observations
* Optional Protocol
* Other relevant UN standards

Example:

Domestic provision
        ↓
CRPD Article 9
        ↓
General Comment No. 2

The system must distinguish between:

* Direct source relationship
* Possible relevance identified by AI
* User-created relationship

⸻

12. Case Law and Decisions

Where available, legal provisions should be connected to:

* Court decisions
* Constitutional Court decisions
* National Human Rights Commission decisions
* Administrative decisions
* Other authoritative decisions

The system should preserve:

* Case name
* Case number
* Court or institution
* Decision date
* Relevant provision
* Source
* Summary
* Relationship to the provision

⸻

13. Advocacy Relevance

The system may classify provisions according to their practical relevance to advocacy.

Possible tags:

* Legal obligation
* Minimum standard
* Government responsibility
* Service entitlement
* Enforcement mechanism
* Discrimination prohibition
* Remedy
* Numerical standard
* Policy planning requirement

This classification must be clearly identified as an AI or user-generated classification, not as an official legal interpretation.

⸻

14. Confidence and Verification

AI-generated tags must include a confidence or verification status.

Possible statuses:

* AI_UNREVIEWED
* AI_REVIEWED
* HUMAN_VERIFIED
* DISPUTED

Human-verified information should be distinguishable from AI-generated information.

Users should be able to correct AI-generated tags.

Corrections should be recorded in the revision history.

⸻

15. User-Generated Tags

Authorized users may add their own tags.

Examples:

* Current campaign
* 2026 국토부 협의
* 입법 필요
* 소송 활용
* 국감 자료
* 예산 근거
* 자주 쓰는 조문

User-generated tags must be distinguishable from official legal metadata and AI-generated tags.

⸻

16. Example

A legal provision may ultimately be represented as:

[Official Information]
Law:
Transportation Accessibility Act
Provision:
Article XX
Effective Date:
YYYY-MM-DD
Source:
Official legal database
[AI Analysis]
Right:
Mobility
Issue:
Special Transportation
System:
Special Transportation Services
Subject:
Local Government
Target:
Persons with Mobility Difficulties
Obligation:
Provide and operate special transportation services
Numerical Requirement:
XX vehicles
Procedure:
Application → Eligibility Assessment → Service Provision
Remedy:
Administrative complaint / litigation
[Related Sources]
CRPD:
Article 9
Case Law:
Case XXXX
[Advocacy Tags]
Government Responsibility
Numerical Standard
Legislative Advocacy
[Verification]
Status:
HUMAN_VERIFIED

⸻

17. Prohibited AI Behavior

AI must not:

* Invent legal provisions
* Invent article numbers
* Change numerical requirements
* Present an interpretation as the text of the law
* Treat an AI-generated relationship as an official legal relationship
* Remove qualifications or exceptions from legal provisions
* Present outdated provisions as current law
* Hide uncertainty
* Provide legal conclusions without identifying supporting sources

⸻

18. Design Principle

The platform should answer two questions simultaneously:

“어디에 그렇게 쓰여 있는가?”

and

“그 조문이 무엇을 의미하고 어떤 제도와 연결되는가?”

The first question is answered through authoritative legal metadata and original text.

The second question is supported through AI-generated and human-verified semantic tags.

Both layers are essential to the platform.
