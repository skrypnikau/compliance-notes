# NIST Cybersecurity Framework 2.0 — Quick Reference

## Overview

The NIST Cybersecurity Framework (CSF) 2.0 was published in February 2024. It is a voluntary framework applicable to any organisation, sector, or size. CSF 2.0 significantly expanded from version 1.1:

- Added a new **Govern (GV)** function (was absent in CSF 1.1)
- Explicit supply chain risk management (GV.SC category)
- Improved guidance for small and medium enterprises
- Technology-neutral and sector-agnostic design

---

## The Six CSF 2.0 Functions

| Function | Abbreviation | Description |
|---------|-------------|-------------|
| **Govern** | GV | Establish and monitor cybersecurity risk management strategy, expectations, and policy |
| **Identify** | ID | Understand and document assets, risks, and vulnerabilities |
| **Protect** | PR | Implement safeguards to manage cybersecurity risks |
| **Detect** | DE | Find and analyse cybersecurity events |
| **Respond** | RS | Take action on detected cybersecurity incidents |
| **Recover** | RC | Restore capabilities and services after an incident |

---

## Govern (GV) — New in CSF 2.0

| Category | ID | Summary |
|---------|-----|---------|
| Organisational Context | GV.OC | Mission, stakeholders, requirements, risk tolerance |
| Risk Management Strategy | GV.RM | Prioritisation, risk tolerance, risk appetite documented |
| Roles, Responsibilities, and Authorities | GV.RR | Cybersecurity roles defined; board accountability |
| Policy | GV.PO | Policies established, communicated, enforced |
| Oversight | GV.OV | Outcomes reviewed; strategy and posture updated |
| Cybersecurity Supply Chain Risk Management | GV.SC | Supplier risk managed; SCRM programme |

**Key subcategories for NIS2 alignment:**
- GV.RM-01: Risk management objectives established (NIS2 Art. 21(2)(a))
- GV.SC-01 to GV.SC-10: Supply chain risk management (NIS2 Art. 21(2)(d))
- GV.RR-02: Roles and responsibilities assigned (NIS2 Art. 21 governance)

---

## Identify (ID)

| Category | ID | Summary |
|---------|-----|---------|
| Asset Management | ID.AM | Inventory of hardware, software, data, and services |
| Risk Assessment | ID.RA | Identify, analyse, and prioritise cyber risks |
| Improvement | ID.IM | Improvements identified from assessments, incidents, exercises |

**Key subcategories:**
- ID.AM-01: Hardware assets inventoried
- ID.AM-02: Software assets inventoried
- ID.AM-05: Software platforms inventoried (relevant to SBOM for EU CRA)
- ID.RA-01: Vulnerabilities in assets identified
- ID.RA-09: Third-party risks identified
- ID.RA-10: Critical suppliers identified and assessed

---

## Protect (PR)

| Category | ID | Summary |
|---------|-----|---------|
| Identity Management, Authentication, Access Control | PR.AA | Manage identities, credentials, and access |
| Awareness and Training | PR.AT | Security awareness and role-based training |
| Data Security | PR.DS | Data protection — confidentiality, integrity, availability |
| Platform Security | PR.PS | Secure configuration of hardware, software, services |
| Technology Infrastructure Resilience | PR.IR | Resilience design for infrastructure |

**Key subcategories:**
- PR.AA-03: Users and services authenticated (MFA — NIS2 Art. 21(2)(j))
- PR.AT-01: Personnel are aware of cybersecurity responsibilities (NIS2 Art. 21(2)(g))
- PR.DS-01: Data at rest is protected (encryption — GDPR Art. 32, CRA Annex I)
- PR.DS-02: Data in transit is protected
- PR.PS-01: Configuration management (NIS2 Art. 21(2)(a))

---

## Detect (DE)

| Category | ID | Summary |
|---------|-----|---------|
| Continuous Monitoring | DE.CM | Monitor assets, users, networks, and services for anomalies |
| Adverse Event Analysis | DE.AE | Detect, correlate, and analyse adverse events |

**Key subcategories:**
- DE.CM-01: Networks monitored for anomalies
- DE.CM-03: User activity monitored
- DE.CM-06: External service provider activities monitored
- DE.AE-02: Potentially adverse events analysed
- DE.AE-06: Information on adverse events shared

---

## Respond (RS)

| Category | ID | Summary |
|---------|-----|---------|
| Incident Management | RS.MA | Manage and respond to detected incidents |
| Incident Analysis | RS.AN | Investigate incidents |
| Incident Response Reporting and Communication | RS.CO | Communicate about incidents internally and externally |
| Incident Mitigation | RS.MI | Contain and mitigate incidents |

**Key subcategories for NIS2 alignment:**
- RS.MA-01: Incident response plan executed (NIS2 Art. 21(2)(b))
- RS.CO-03: Information shared consistent with plans (NIS2 Art. 23 reporting)
- RS.CO-04: Coordinate with stakeholders (CSIRT, authorities)
- RS.MI-01: Incidents contained

---

## Recover (RC)

| Category | ID | Summary |
|---------|-----|---------|
| Incident Recovery Plan Execution | RC.RP | Execute recovery activities |
| Incident Recovery Communication | RC.CO | Communicate recovery progress |

**Key subcategories for NIS2 alignment:**
- RC.RP-01: Recovery plan executed (NIS2 Art. 21(2)(c))
- RC.RP-03: Recovery activities validated
- RC.CO-03: Recovery activities communicated to stakeholders
- RC.CO-04: Public updates provided if appropriate

---

## CSF 2.0 vs CSF 1.1 — Key Changes Summary

| Change | CSF 1.1 | CSF 2.0 |
|--------|---------|---------|
| Number of Functions | 5 | 6 (added Govern) |
| Supply chain risk | Limited | Dedicated category (GV.SC) |
| Governance focus | Implicit | Explicit (entire GV function) |
| SME guidance | Limited | Improved quick start guides |
| Implementation tiers | 4 tiers | Still 4 tiers (refined) |
| Profiles | High-level | More detailed with examples |

---

## Using CSF 2.0 for EU Compliance

CSF 2.0 aligns well with both NIS2 and ISO 27001:

| EU Regulation | CSF Functions Most Relevant |
|-------------|--------------------------|
| GDPR (Art. 32 security) | PR, DE, RS |
| GDPR (breach notification) | DE, RS.CO |
| NIS2 (risk management) | GV, ID |
| NIS2 (incident handling) | DE, RS |
| NIS2 (business continuity) | RC |
| NIS2 (supply chain) | GV.SC |
| NIS2 (training) | PR.AT |
| EU CRA (product security) | PR.PS, ID.AM (SBOM), ID.RA |

The main limitation of using NIST CSF for EU compliance is that it is a framework (structured guidance), not a regulation. It provides no specific timelines (e.g., 72-hour breach notification), no legal definitions (e.g., what constitutes a significant incident under NIS2), and no certification path. It must be supplemented with EU-specific procedures.
