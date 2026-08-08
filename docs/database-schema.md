Database Schema

1. Design Goals

The database must:

1. Preserve authoritative legal sources exactly.
2. Preserve precise legal citations.
3. Represent relationships between laws, provisions, rights, issues, systems, and procedures.
4. Support automatic updates from official legal databases.
5. Store AI-generated classifications separately from official legal data.
6. Preserve human verification and revision history.
7. Support public, organization-restricted, and personal information.
8. Allow the knowledge base to grow continuously without redesigning the entire database.

⸻

2. Core Data Model

The platform is organized around the following core entities:

Law
  │
  └── Provision
        │
        ├── Right
        ├── Issue
        ├── System
        ├── Obligation
        ├── Subject
        ├── Target
        ├── Procedure
        ├── Remedy
        ├── Quantitative Requirement
        ├── International Standard
        ├── Case
        └── Advocacy Knowledge

⸻

3. Law

Represents a legal instrument.

Required fields

* law_id
* law_name
* law_type
* jurisdiction
* official_identifier
* enactment_date
* effective_date
* last_amended_date
* status
* official_source_url

Law Type

Examples:

* LAW
* ENFORCEMENT_DECREE
* ENFORCEMENT_RULE
* ADMINISTRATIVE_RULE
* PUBLIC_NOTICE
* INTERNATIONAL_TREATY
* OTHER

⸻

4. Provision

Represents a specific legal provision.

A provision is the basic unit for legal citation and analysis.

Required fields

* provision_id
* law_id
* article
* paragraph
* subparagraph
* item
* article_title
* text
* effective_date
* source_url

Example

Law:
교통약자의 이동편의 증진법
Article:
제16조
Paragraph:
제1항
Text:
[Original legal text]

The system must preserve the original text.

⸻

5. Legal Hierarchy

Legal instruments must maintain their hierarchical relationships.

Example:

Law
 └── Enforcement Decree
      └── Enforcement Rule

The database should store relationships between related provisions.

Example:

Law Article 16
       │
       └── implemented by
               ↓
Enforcement Decree Article XX
               │
               └── detailed by
                       ↓
Enforcement Rule Article XX

Relationship types may include:

* IMPLEMENTS
* DETAILS
* REFERS_TO
* EXCEPTS
* REPLACES
* AMENDS

⸻

6. Right

Represents a disability-related right or legal interest.

Examples:

* Mobility
* Accessibility
* Independent Living
* Education
* Employment
* Health
* Housing
* Participation
* Equality
* Non-discrimination
* Information Access

Fields:

* right_id
* name
* description

⸻

7. Issue

Represents a practical disability rights issue.

Examples:

* Special Transportation
* Supported Housing
* Personal Assistance
* Assistive Technology
* Accessible Transportation
* Boarding Assistance
* Reasonable Accommodation
* Deinstitutionalization

Fields:

* issue_id
* name
* description

⸻

8. System

Represents a specific legal, administrative, or service system.

Examples:

* Special Transportation Services
* Personal Assistance Services
* Supported Housing
* Assistive Technology Support
* Disability Employment Quota

Fields:

* system_id
* name
* description

⸻

9. Legal Actor

Represents an entity that has legal authority, responsibility, or a legal relationship.

Examples:

* Central Government
* Local Government
* Ministry
* Municipality
* Public Institution
* Transportation Operator
* Employer
* School
* Service Provider

Fields:

* actor_id
* name
* actor_type

⸻

10. Target Group

Represents people who are protected, supported, or affected.

Examples:

* Persons with Disabilities
* Persons with Mobility Difficulties
* Wheelchair Users
* Persons with Developmental Disabilities
* Children with Disabilities
* Older Persons

Fields:

* target_id
* name
* description

⸻

11. Obligation

Represents a legal obligation.

Fields:

* obligation_id
* provision_id
* actor_id
* action
* target_id
* conditions
* source_text
* verification_status

Examples of actions:

* Provide
* Establish
* Operate
* Install
* Maintain
* Support
* Accommodate
* Report
* Investigate

⸻

12. Procedure

Represents a legally established procedure.

Fields:

* procedure_id
* name
* initiator
* responsible_authority
* required_documents
* time_limit
* steps
* provision_id

Examples:

* Application
* Registration
* Eligibility Assessment
* Complaint
* Investigation
* Administrative Appeal
* Mediation
* Litigation

⸻

13. Remedy

Represents a legal remedy or enforcement mechanism.

Fields:

* remedy_id
* name
* authority
* procedure
* conditions
* possible_result
* provision_id

Examples:

* Administrative Appeal
* Civil Litigation
* Administrative Litigation
* Human Rights Complaint
* Corrective Order
* Compensation
* Administrative Sanction

⸻

14. Quantitative Requirement

Represents a numerical or measurable legal requirement.

This is a high-priority data type.

Fields:

* quantity_id
* provision_id
* quantity_type
* value
* unit
* minimum
* maximum
* ratio
* condition
* effective_date
* source_text

Examples:

Minimum:
10 vehicles
Ratio:
1 vehicle / 100 persons
Deadline:
30 days
Penalty:
10,000,000 KRW

The original legal wording must always be preserved.

⸻

15. International Standard

Represents international disability rights standards.

Examples:

* UN CRPD
* CRPD Article
* General Comment
* Concluding Observations
* Optional Protocol

Fields:

* standard_id
* name
* article
* paragraph
* source
* source_url
* description

The system must distinguish between:

* Official relationship
* AI-suggested relationship
* User-created relationship

⸻

16. Case

Represents judicial or quasi-judicial decisions.

Examples:

* Supreme Court decisions
* Constitutional Court decisions
* Administrative Court decisions
* National Human Rights Commission decisions

Fields:

* case_id
* case_name
* case_number
* institution
* decision_date
* source_url
* summary

Cases may be linked to provisions, rights, issues, and systems.

⸻

17. Advocacy Knowledge

Represents organization-specific or user-generated knowledge.

Examples:

* Legal analysis
* Negotiation materials
* Campaign strategies
* Policy proposals
* Field experience
* Legislative arguments

Fields:

* knowledge_id
* title
* content
* author
* organization
* created_at
* updated_at
* visibility
* verification_status

⸻

18. Personal Note

Represents information belonging to an individual user.

Examples:

* Research notes
* Draft arguments
* Personal annotations
* Unpublished ideas

Fields:

* note_id
* user_id
* title
* content
* created_at
* updated_at
* visibility

Personal notes are private by default.

⸻

19. Users and Permissions

The system must support different access levels.

User

Fields:

* user_id
* name
* organization
* role
* status

Access Levels

PUBLIC
ORGANIZATION
PRIVATE

Example

Public legal provision
        ↓
PUBLIC
Internal advocacy analysis
        ↓
ORGANIZATION
Personal research note
        ↓
PRIVATE

Access control must be enforced at the data level, not only at the user interface level.

⸻

20. AI Analysis

AI-generated information must be stored separately from authoritative information.

Fields may include:

* analysis_id
* source_type
* source_id
* tag_type
* tag_value
* confidence
* model
* created_at
* verification_status

Example:

Source:
Provision 12345
Tag:
Issue = Special Transportation
Confidence:
0.94
Status:
AI_UNREVIEWED

⸻

21. Verification

Every AI-generated classification must have a verification status.

Possible values:

* AI_UNREVIEWED
* AI_REVIEWED
* HUMAN_VERIFIED
* DISPUTED

Human corrections must be preserved in the revision history.

⸻

22. Revision History

The system must preserve changes to important data.

Fields:

* revision_id
* entity_type
* entity_id
* changed_by
* changed_at
* change_type
* previous_value
* new_value

Legal amendments and user edits must be distinguishable.

⸻

23. Relationships

The database should support many-to-many relationships.

Examples:

Provision ↔ Right
Provision ↔ Issue
Provision ↔ System
Provision ↔ Actor
Provision ↔ Target
Provision ↔ Procedure
Provision ↔ Remedy
Provision ↔ Quantitative Requirement
Provision ↔ International Standard
Provision ↔ Case
Provision ↔ Advocacy Knowledge

A single provision may therefore be connected to many rights, systems, cases, and advocacy materials.

⸻

24. Source and Provenance

Every important piece of information must have provenance.

The system should record:

* Original source
* Source URL
* Source date
* Retrieval date
* Effective date
* Data origin
* AI-generated or human-generated status
* Verification status

The system must allow users to trace an answer back to its original source.

⸻

25. Design Principle

The database should not simply store documents.

It should represent relationships between:

Law
↓
Provision
↓
Rights / Issues / Systems
↓
Obligations / Procedures / Remedies
↓
International Standards / Cases
↓
Advocacy Knowledge

The legal provision remains the authoritative foundation, while the connected knowledge makes the information useful for research and advocacy.
