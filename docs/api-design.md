API Design

1. Purpose

This document defines how the Disability Law Platform obtains authoritative legal information and keeps the legal database synchronized with official sources.

The initial priority is integration with the Korean National Law Information Center API.

⸻

2. Core Architecture

The legal information pipeline is:

Official Legal Source
        ↓
API Collector
        ↓
Raw Legal Data
        ↓
Normalization
        ↓
Legal Database
        ↓
Change Detection
        ↓
AI Analysis
        ↓
Human Verification
        ↓
Search / Knowledge Graph

The official source is the authoritative origin of legal text.

⸻

3. Official Source

Primary Source

Korean National Law Information Center API

The system should use the official API whenever available.

The system must preserve:

* Original legal text
* Official identifiers
* Article numbers
* Effective dates
* Amendment dates
* Official source information

⸻

4. API Collector

The API Collector retrieves legal information from the official source.

Responsibilities:

* Search legal instruments
* Retrieve law metadata
* Retrieve full legal text
* Retrieve individual provisions when supported
* Retrieve amendment information
* Retrieve effective dates
* Store retrieval timestamps

The collector must not modify the original legal text.

⸻

5. Raw Data Layer

Raw API responses should be preserved separately from normalized database records.

Example:

API Response
     ↓
Raw Data Storage
     ↓
Normalization
     ↓
Application Database

This allows the system to reprocess the original data if the database schema changes.

⸻

6. Normalization

Official data must be converted into the platform’s internal data model.

Example:

Official API
     ↓
Law
     ↓
Provision
     ↓
Paragraph
     ↓
Subparagraph
     ↓
Item

The normalization process must preserve the original legal hierarchy.

⸻

7. Automatic Updates

The system should periodically check official sources for changes.

Possible update cycle:

Scheduled Update
       ↓
Check Last Modified Date
       ↓
Has Changed?
   ↙          ↘
 No            Yes
 ↓              ↓
End        Retrieve New Version
                 ↓
            Store New Version
                 ↓
            Detect Changes
                 ↓
            Re-analyze

The update frequency should be configurable.

⸻

8. Version Management

Each legal version must be stored separately.

Example:

Law A
Version 1
Effective: 2025-01-01
Version 2
Effective: 2026-03-01
Version 3
Effective: 2027-01-01

Users should be able to identify which version was effective at a particular point in time.

⸻

9. Change Detection

The system should identify changes between versions.

Possible change types:

* Added provision
* Deleted provision
* Modified provision
* Renumbered provision
* Changed effective date
* Changed annex
* Changed numerical requirement

Example:

Before:
"10 vehicles"
After:
"15 vehicles"
Change:
Numerical requirement modified

The system should preserve both versions.

⸻

10. AI Re-analysis

When a provision changes, the system should determine whether existing AI analysis remains valid.

Example:

Provision amended
       ↓
Compare old/new text
       ↓
Identify affected tags
       ↓
Re-run AI analysis
       ↓
Mark previous analysis as outdated
       ↓
Generate new analysis

Unchanged provisions should not needlessly undergo full re-analysis.

⸻

11. Source Reliability

The system should prioritize sources according to authority.

Example hierarchy:

Official Legal Database
        ↓
Official Government Source
        ↓
Official International Organization
        ↓
Court / Human Rights Institution
        ↓
Academic / Research Source
        ↓
Other Sources

The source hierarchy must be visible in the data model.

⸻

12. Error Handling

The API integration must handle:

* API unavailable
* Request timeout
* Rate limits
* Invalid responses
* Missing data
* Temporary network errors
* Changes to API format

The system must not overwrite existing authoritative data with incomplete or invalid API responses.

⸻

13. Data Integrity

The system must verify:

* Law identifier
* Law name
* Article number
* Effective date
* Amendment date
* Source URL
* Original text

before updating the database.

If validation fails, the update should be flagged for review.

⸻

14. Update Log

Every synchronization should be logged.

Fields may include:

* sync_id
* source
* started_at
* completed_at
* status
* records_checked
* records_changed
* records_added
* records_deleted
* error_count

Example:

2026-08-08
Source:
National Law Information Center
Checked:
1,245 provisions
Changed:
7 provisions
Added:
2 provisions
Errors:
0

⸻

15. API Credentials and Security

API credentials must never be stored in source code.

Credentials should be stored using environment variables or a secure secret-management system.

Example:

LAW_API_KEY=********

Secrets must never be committed to GitHub.

⸻

16. Manual Override

Authorized administrators must be able to:

* Retry failed synchronization
* Review detected changes
* Correct normalization errors
* Trigger re-analysis
* Mark data for human verification

Manual corrections must be recorded in the revision history.

⸻

17. Future External Sources

The architecture should allow additional sources to be integrated later.

Potential sources include:

* UN CRPD
* UN Treaty Collection
* Constitutional Court
* Supreme Court
* National Human Rights Commission
* Government ministries
* Overseas legislation databases

Each source should have an independent connector.

⸻

18. Design Principle

The platform follows:

Official source → structured data → AI analysis → human verification

rather than:

AI → legal information

The AI is an analysis layer, not the source of legal authority.
