# NIS2 Directive — Requirements Mapped to NIST CSF 2.0

**Source:** EU Directive 2022/2555 (NIS2), particularly Article 21 (cybersecurity risk management measures)
**Mapped to:** NIST Cybersecurity Framework 2.0 (Functions, Categories, Subcategories)
**Note:** NIS2 must be transposed into national law by each EU member state. This mapping is based on the directive text itself.

---

## Scope of NIS2

NIS2 applies to **essential entities** and **important entities** across a range of sectors including energy, transport, banking, financial market infrastructure, health, drinking water, wastewater, digital infrastructure, managed services, public administration, and space.

Key differences from NIS1:
- Significantly expanded scope (more sectors and more organisations)
- Stricter security requirements (Article 21)
- Stricter incident reporting timelines (24h early warning, 72h incident notification, 1 month final report)
- Supply chain security obligations explicitly added
- Board-level accountability for cybersecurity

---

## Article 21 — Cybersecurity Risk Management Measures

Article 21 lists the minimum security measures that covered entities must implement:

### Art. 21(2)(a) — Policies on risk analysis and information system security

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| GOVERN (GV) | GV.OC: Organisational Context | GV.OC-01 | Mission and risk tolerance defined |
| GOVERN (GV) | GV.RM: Risk Management Strategy | GV.RM-01, GV.RM-02 | Risk management policy and strategy |
| IDENTIFY (ID) | ID.RA: Risk Assessment | ID.RA-01 to ID.RA-10 | Full risk assessment process |

---

### Art. 21(2)(b) — Incident handling

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| DETECT (DE) | DE.AE: Adverse Event Analysis | DE.AE-01 to DE.AE-08 | Detection and analysis of security events |
| RESPOND (RS) | RS.MA: Incident Management | RS.MA-01 to RS.MA-05 | Incident management procedures |
| RESPOND (RS) | RS.CO: Incident Response Reporting | RS.CO-01 to RS.CO-03 | Internal and external communication |

**NIS2-specific gap:** NIS2 requires:
- Early warning to CSIRT within **24 hours** of becoming aware of a significant incident
- Incident notification within **72 hours** with initial assessment
- Intermediate report if applicable
- Final report within **1 month**

NIST CSF does not specify timelines — these must be defined in organisation-specific incident response procedures.

---

### Art. 21(2)(c) — Business continuity (backups, disaster recovery, crisis management)

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| RESPOND (RS) | RS.MI: Incident Mitigation | RS.MI-01, RS.MI-02 | Mitigation of incident impact |
| RECOVER (RC) | RC.RP: Incident Recovery Plan Execution | RC.RP-01 to RC.RP-06 | Recovery procedures |
| RECOVER (RC) | RC.CO: Incident Recovery Communication | RC.CO-03, RC.CO-04 | Communication during recovery |
| GOVERN (GV) | GV.OC: Organizational Context | GV.OC-03, GV.OC-04 | Critical service dependencies and partner services identified |

---

### Art. 21(2)(d) — Supply chain security

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| GOVERN (GV) | GV.SC: Cybersecurity Supply Chain Risk Management | GV.SC-01 to GV.SC-10 | Full supply chain risk management (new in CSF 2.0) |
| IDENTIFY (ID) | ID.RA: Risk Assessment | ID.RA-09, ID.RA-10 | Third-party risk included in risk assessment |

**Note:** NIST CSF 2.0 added the GOVERN function with the GV.SC category specifically to address supply chain risk — this was a significant gap in CSF 1.1 and aligns well with NIS2 Art. 21(2)(d).

---

### Art. 21(2)(e) — Security in network and information systems acquisition, development, and maintenance

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| PROTECT (PR) | PR.PS: Platform Security | PR.PS-01 to PR.PS-06 | Secure configuration and development |
| PROTECT (PR) | PR.AA: Identity Management, Authentication, Access Control | PR.AA-01 to PR.AA-06 | Access control in systems |
| IDENTIFY (ID) | ID.IM: Improvement | ID.IM-01 to ID.IM-04 | Lessons learned from security testing |

---

### Art. 21(2)(f) — Policies and procedures to assess the effectiveness of cybersecurity risk management measures

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| GOVERN (GV) | GV.OV: Oversight | GV.OV-01 to GV.OV-03 | Review of cybersecurity outcomes |
| IDENTIFY (ID) | ID.IM: Improvement | ID.IM-02, ID.IM-03 | Continuous improvement |

---

### Art. 21(2)(g) — Basic cyber hygiene practices and cybersecurity training

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| PROTECT (PR) | PR.AT: Awareness and Training | PR.AT-01, PR.AT-02 | Cybersecurity awareness training |
| GOVERN (GV) | GV.RR: Roles, Responsibilities, and Authorities | GV.RR-02, GV.RR-04 | Role-based security responsibilities |

---

### Art. 21(2)(h) — Policies and procedures regarding the use of cryptography and encryption

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| PROTECT (PR) | PR.DS: Data Security | PR.DS-01, PR.DS-02, PR.DS-10 | Protection of data in transit and at rest |

---

### Art. 21(2)(i) — Human resources security, access control policies, and asset management

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| PROTECT (PR) | PR.AA: Identity Management, Authentication, Access Control | PR.AA-01 to PR.AA-06 | Access control |
| IDENTIFY (ID) | ID.AM: Asset Management | ID.AM-01 to ID.AM-08 | Asset inventory and management |

---

### Art. 21(2)(j) — Use of multi-factor authentication or continuous authentication

**NIST CSF Mapping:**

| NIST CSF Function | Category | Subcategory | Notes |
|------------------|---------|-------------|-------|
| PROTECT (PR) | PR.AA: Identity Management, Authentication, Access Control | PR.AA-03, PR.AA-05 | MFA and strong authentication |

---

## NIS2 Incident Reporting Requirements Summary

| Report Type | Deadline | Contents |
|------------|---------|---------|
| Early warning | 24 hours after awareness | Indicate whether caused by unlawful/malicious act; transboundary impact |
| Incident notification | 72 hours after awareness | Updated early warning + initial assessment (severity, indicators, impact) |
| Intermediate report | Upon request from CSIRT/competent authority | Current status, actions taken |
| Final report | 1 month after incident notification | Full description, severity/impact, likely cause, measures applied/ongoing |

---

## NIS2 vs NIS1 — Key Changes

| Area | NIS1 | NIS2 |
|------|------|------|
| Scope | Limited sectors, operator of essential services (OES) | Expanded sectors, essential + important entities |
| Supply chain | Not explicitly required | Explicitly required (Art. 21(2)(d)) |
| Incident reporting | No specific timeline | 24h / 72h / 1 month |
| Penalties | Varied by member state | Minimum harmonised: up to 10M EUR or 2% global turnover (essential entities) |
| Board accountability | Not specified | Management bodies personally accountable |
| Enforcement | Inconsistent across EU | More harmonised, proactive supervision for essential entities |
