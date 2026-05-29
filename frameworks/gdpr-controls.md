# GDPR — Key Articles Mapped to ISO/IEC 27001:2022 Controls

**Source:** EU Regulation 2016/679 (GDPR)
**Mapped to:** ISO/IEC 27001:2022 Annex A controls
**Focus:** Articles with direct information security implications

---

## Overview

GDPR does not prescribe specific technical controls. Instead, Article 32 requires organisations to implement "appropriate technical and organisational measures" taking into account risk, state of the art, cost, and nature of processing. ISO 27001 provides a structured control framework that, when properly implemented, satisfies a significant portion of GDPR security obligations.

---

## Article 5 — Principles Relating to Processing (Integrity and Confidentiality)

**GDPR Requirement:** Personal data must be processed with "appropriate security... including protection against unauthorised or unlawful processing and against accidental loss, destruction or damage."

| ISO 27001:2022 Control | Control ID | How It Satisfies GDPR Art. 5 |
|----------------------|-----------|-------------------------------|
| Information security policies | 5.1 | Establishes governance foundation for data protection |
| Information classification | 5.12 | Ensures personal data is identified and protected appropriately |
| Access control | 5.15, 8.3 | Restricts access to personal data to authorised personnel only |
| Cryptography policy | 8.24 | Protects confidentiality and integrity of personal data in transit and at rest |
| Physical security | 7.1, 7.2, 7.3 | Protects physical media containing personal data |
| Secure disposal | 8.10 | Ensures personal data is securely erased when no longer needed |

---

## Article 25 — Data Protection by Design and by Default

**GDPR Requirement:** Implement data protection principles "from the outset" and process only data necessary for the specific purpose.

| ISO 27001:2022 Control | Control ID | Mapping |
|----------------------|-----------|---------|
| Secure development lifecycle | 8.25, 8.26, 8.27, 8.28 | Embeds security (and privacy by extension) into software development |
| Information classification | 5.12 | Ensures data minimisation — only necessary data collected and retained |
| Supplier relationships | 5.19, 5.20 | Extends privacy-by-design to third-party processors |

**ISO 27001 gap:** ISO 27001 does not explicitly address data minimisation as a principle. This must be addressed through privacy-specific controls (e.g., ISO 29101, NIST Privacy Framework, or internal procedures).

---

## Article 32 — Security of Processing

**GDPR Requirement:** Implement appropriate technical and organisational measures including, as appropriate:
- Pseudonymisation and encryption
- Ability to ensure ongoing confidentiality, integrity, availability, and resilience
- Ability to restore access to personal data after a technical incident
- Regular testing, assessing, and evaluating of technical/organisational measures

| ISO 27001:2022 Control | Control ID | GDPR Art. 32 Element |
|----------------------|-----------|----------------------|
| Cryptography policy | 8.24 | Encryption and pseudonymisation |
| Business continuity | 5.29, 5.30, 8.13, 8.14 | Resilience and recovery after incidents |
| Backup | 8.13 | Ability to restore access to personal data |
| Information security incident management | 5.24, 5.25, 5.26, 5.27, 5.28 | Detecting and responding to incidents affecting personal data |
| Vulnerability management | 8.8 | Regular testing and assessment of controls |
| Access control reviews | 5.18 | Ongoing evaluation of access to personal data |
| Internal audits | 9.2 (clause, not Annex A) | Regular evaluation of the ISMS effectiveness |

---

## Article 33 — Notification of Breach to Supervisory Authority

**GDPR Requirement:** Notify the supervisory authority (DPA) within 72 hours of becoming aware of a personal data breach (where the breach is likely to result in a risk to the rights and freedoms of individuals).

| ISO 27001:2022 Control | Control ID | Mapping |
|----------------------|-----------|---------|
| Information security incident management | 5.24, 5.25 | Detection and classification of incidents including data breaches |
| Incident reporting | 6.8 | Internal reporting procedures that feed into breach notification workflow |
| Incident documentation | 5.27 | Preserving evidence and records needed for breach notification |

**GDPR-specific gap:** ISO 27001 does not specify a 72-hour notification timeline or require a Data Protection Officer (DPO). GDPR-specific procedures must supplement the ISMS for breach notification.

---

## Article 34 — Communication of Breach to Data Subjects

**GDPR Requirement:** Where a breach is likely to result in a high risk to individuals, notify affected data subjects without undue delay.

| ISO 27001:2022 Control | Control ID | Mapping |
|----------------------|-----------|---------|
| Communication during incidents | 5.26 | External communication procedures (can be adapted for data subject notification) |
| Stakeholder management | 5.6 | Contact with relevant parties (data subjects are a key stakeholder category) |

---

## Article 35 — Data Protection Impact Assessment (DPIA)

**GDPR Requirement:** Conduct a DPIA before processing likely to result in high risk to individuals (e.g., large-scale processing, systematic monitoring, processing of special categories of data).

| ISO 27001:2022 Control | Control ID | Mapping |
|----------------------|-----------|---------|
| Information security risk assessment | Clause 6.1.2 | Risk assessment methodology applicable to DPIAs |
| Risk treatment | Clause 6.1.3 | Risk treatment process maps to DPIA remediation actions |

**Note:** A GDPR DPIA is specifically focused on risks to data subjects, not just risks to the organisation. ISO 27001 risk assessment covers organisational risk but needs to be extended to cover data subject risks for DPIA purposes.

---

## Summary: ISO 27001 Coverage of GDPR

| GDPR Requirement Area | ISO 27001 Coverage | Gap |
|----------------------|-------------------|-----|
| Confidentiality and integrity of processing | Strong | Data minimisation not covered |
| Privacy by design | Partial | No explicit data minimisation or purpose limitation controls |
| Security measures (encryption, access control, resilience) | Strong | Well covered |
| Breach detection | Strong | Covered by incident management controls |
| 72-hour breach notification | None | Requires GDPR-specific procedure |
| DPO appointment | None | Regulatory requirement; outside ISO 27001 scope |
| DPIA | Partial | Risk assessment methodology applicable but needs adaptation |
| Data subject rights (access, erasure, portability) | None | Entirely GDPR-specific; requires dedicated procedures |
