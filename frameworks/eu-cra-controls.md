# EU Cyber Resilience Act (CRA) — Requirements Mapped to Controls

**Source:** EU Regulation 2024/2847 (Cyber Resilience Act)
**Entered into Force:** October 2024
**Application Dates:** Reporting obligations: September 2026; Full application: December 2027
**Scope:** Products with digital elements (hardware and software) placed on the EU market

---

## Overview

The EU CRA is the first EU-wide regulation specifically targeting the security of products with digital elements (PWDEs) — any hardware or software product with direct or indirect data connections. It places obligations primarily on **manufacturers** but also on importers and distributors.

The CRA introduces:
- **Essential security requirements** (Annex I) that PWDEs must meet
- **Vulnerability handling requirements** (Annex I, Part II)
- **Conformity assessment** obligations (Annex II/III depending on product class)
- **Incident and vulnerability reporting** obligations to ENISA

---

## CRA Annex I, Part I — Essential Cybersecurity Requirements for Products

### Requirement 1: No known exploitable vulnerabilities at placement on market

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.8 — Management of technical vulnerabilities | Vulnerability scanning and patching of products before release |
| ISO 27001:2022 | 8.25 — Secure development lifecycle | Security testing integrated into development |
| NIST CSF | ID.RA-01 — Asset vulnerabilities identified | Vulnerability identification in product components |
| NIST CSF | ID.RA-06 — Risk response informed by vulnerabilities | Vulnerability remediation before shipping |

---

### Requirement 2: Security by default configuration

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.27 — Secure system architecture and engineering principles | Hardened default configuration |
| ISO 27001:2022 | 8.9 — Configuration management | Documented and tested default configurations |
| NIST CSF | PR.PS-01 — Configuration management | Baseline configurations established |

---

### Requirement 3: Protection against unauthorised access (authentication, access control)

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 5.15 — Access control | Access control mechanisms in product |
| ISO 27001:2022 | 5.17 — Authentication information | Password policies for product accounts |
| NIST CSF | PR.AA-03 — Users, services, and hardware are authenticated | MFA or strong authentication in product |
| NIST CSF | PR.AA-05 — Access permissions are managed | Least-privilege access in product design |

---

### Requirement 4: Protection of confidentiality — encryption of personal data and other sensitive data

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.24 — Use of cryptography | Encryption of data in transit and at rest |
| NIST CSF | PR.DS-01 — Data at rest is protected | Storage encryption |
| NIST CSF | PR.DS-02 — Data in transit is protected | TLS or equivalent for data transmission |

---

### Requirement 5: Protection of integrity — data, product, and configuration

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.20 — Networks security | Network integrity controls |
| ISO 27001:2022 | 8.16 — Monitoring activities | Integrity monitoring |
| NIST CSF | DE.CM-09 — Computing hardware and software are monitored to find adverse events | Hash verification, code signing, integrity checking |

---

### Requirement 6: Minimise attack surface (disable unused features, functions, ports)

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.8 — Management of technical vulnerabilities | Identify and disable unnecessary features |
| ISO 27001:2022 | 8.21 — Security of network services | Disable unused network ports and protocols |
| NIST CSF | PR.PS-03 — Hardware is maintained | Hardware attack surface reduction |

---

### Requirement 7: Logging capabilities

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.15 — Logging | Audit logging in product |
| ISO 27001:2022 | 8.17 — Clock synchronisation | Timestamps in logs must be accurate |
| NIST CSF | DE.AE-03 — Event data are collected and correlated | Product logs support detection |

---

### Requirement 8: Possibility of security updates and patches

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.8 — Management of technical vulnerabilities | Patching mechanism required |
| ISO 27001:2022 | 8.25 — Secure development lifecycle | Update mechanism designed securely |
| NIST CSF | PR.PS-02 — Software is maintained | Software update processes |

---

## CRA Annex I, Part II — Vulnerability Handling Requirements

### Requirement: Identify and document vulnerabilities and components

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 8.8 — Management of technical vulnerabilities | Vulnerability tracking |
| NIST CSF | ID.AM-05 — Software platforms and applications are inventoried | Software Bill of Materials (SBOM) |
| NIST CSF | ID.RA-01 — Asset vulnerabilities identified | Continuous vulnerability identification |

**CRA-specific note:** The CRA explicitly requires a **Software Bill of Materials (SBOM)** in a machine-readable format. This is a new requirement not traditionally covered by ISO 27001.

---

### Requirement: Disclose vulnerabilities and provide coordinated vulnerability disclosure (CVD) policy

**Mapped Controls:**

| Framework | Control | Notes |
|-----------|---------|-------|
| ISO 27001:2022 | 5.28 — Collection of evidence | Vulnerability documentation |
| NIST CSF | RS.CO-03 — Information is shared consistent with response plans | External communication of vulnerabilities |

---

### Requirement: Report actively exploited vulnerabilities to ENISA within 24 hours

**CRA Reporting Timelines:**

| Event | Deadline | Report to |
|-------|---------|-----------|
| Actively exploited vulnerability discovered | 24 hours early warning | ENISA + national CSIRT |
| Actively exploited vulnerability | 72 hours full notification | ENISA + national CSIRT |
| Severe incident impacting security | 24 hours early warning | ENISA + national CSIRT |

**Note:** This mirrors NIS2 reporting timelines and is designed to align the two frameworks.

---

## CRA Product Classifications

| Class | Examples | Conformity Assessment |
|-------|---------|----------------------|
| Default (most products) | Smart home devices, consumer routers, games | Self-assessment |
| Class I | Identity management software, browsers, password managers, VPNs, network monitoring tools | Self-assessment or third party |
| Class II | OS, hypervisors, industrial control systems, safety systems | Third-party certification required |
| Critical components | Hardware security modules, smartcard ICs, root CAs | European Cybersecurity Scheme certification required |

---

## CRA vs GDPR — Interaction

Both CRA and GDPR apply to products that process personal data. Key interaction points:

| Obligation | CRA Requirement | GDPR Requirement | Overlap |
|-----------|----------------|-----------------|---------|
| Encryption | Annex I, Req. 4 | Art. 32(1)(a) | High |
| Access control | Annex I, Req. 3 | Art. 32 | High |
| Logging | Annex I, Req. 7 | Art. 32 (accountability) | Partial |
| Vulnerability management | Annex I, Part II | Art. 32 (appropriate measures) | Partial |
| Breach notification | 24h to ENISA | 72h to DPA (Art. 33) | Different timelines and recipients |
