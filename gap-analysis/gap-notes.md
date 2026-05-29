# Gap Analysis — Fictional SME: "DataSync Ltd"

**Date:** February 2026
**Analyst:** Yauheni Skrypnikau (study exercise)
**Organisation:** DataSync Ltd (fictional)
**Applicable Frameworks:** GDPR, NIS2 (important entity), ISO/IEC 27001:2022

---

## Organisation Profile

**DataSync Ltd** is a fictional B2B SaaS company providing data integration services to clients across the EU. Key characteristics:

| Attribute | Value |
|-----------|-------|
| Employees | 85 |
| EU customers | 120 B2B clients, processing personal data on their behalf |
| Sector | Digital infrastructure / Managed IT services |
| NIS2 status | Important entity (managed service provider) |
| GDPR role | Both Data Controller (own staff data) and Data Processor (client data) |
| ISO 27001 | Not currently certified; informal security practices in place |
| IT infrastructure | Hybrid — AWS cloud + on-premises office network |

---

## Gap Analysis Methodology

1. **Document review** — Review existing security policies, procedures, and technical controls against framework requirements
2. **Technical assessment** — Review AWS configuration, network architecture, endpoint management
3. **Interviews** — CTO, HR manager, customer-facing team
4. **Gap scoring:**
   - **Compliant** — control fully implemented and effective
   - **Partial** — control exists but incomplete, inconsistent, or undocumented
   - **Gap** — control is absent or clearly insufficient
   - **N/A** — not applicable to this organisation

---

## GDPR Gap Analysis

### Article 32 — Security of Processing

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| Encryption of personal data at rest | AWS S3 server-side encryption enabled on all buckets | Compliant | Good — encryption enabled by default |
| Encryption in transit | HTTPS enforced on all APIs and web applications | Compliant | TLS 1.2+ in use |
| Access controls on personal data | AWS IAM in use but roles not reviewed in 18 months | Partial | Some over-permissioned roles identified |
| Pseudonymisation where appropriate | Not implemented | Gap | No pseudonymisation of client datasets |
| Ability to restore data after incident | Daily AWS backups in place | Partial | Backups exist but recovery procedures never tested |
| Regular testing of security measures | Annual pen test (external) | Partial | No continuous vulnerability scanning; internal testing ad hoc |

### Article 33 — Breach Notification Procedure

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| Breach detection capability | AWS GuardDuty enabled; no SIEM | Partial | Limited centralised logging and correlation |
| Internal breach notification procedure | No documented procedure | Gap | No documented escalation path when breach suspected |
| 72-hour supervisory authority notification procedure | No documented procedure | Gap | DPA contact details not known to incident responders |
| Data subject notification procedure | No documented procedure | Gap | No template or process for Art. 34 notifications |

### Article 28 — Data Processing Agreements (DPAs)

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| DPAs in place with all sub-processors | DPAs in place with AWS and Stripe; others not checked | Partial | 3 other sub-processors (Twilio, HubSpot, Zendesk) — DPAs not verified |
| Sub-processor list maintained | Not maintained | Gap | No formal register of sub-processors |

---

## NIS2 Gap Analysis (Article 21 Measures)

### Art. 21(2)(a) — Risk analysis and information system security policies

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| Documented information security policy | Basic policy document (2 pages, 2021) | Partial | Outdated; does not cover cloud security or supply chain |
| Regular risk assessment | No formal risk assessment ever conducted | Gap | Risk is managed informally by CTO |
| Risk register | No formal risk register | Gap | |

### Art. 21(2)(b) — Incident handling

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| Incident response plan | No documented IRP | Gap | |
| Incident detection capability | AWS GuardDuty; no SIEM | Partial | Limited visibility into on-premises environment |
| NIS2 24h/72h reporting procedure | No procedure | Gap | Not aware of reporting obligation to CSIRT |

### Art. 21(2)(c) — Business continuity

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| Business continuity plan | No formal BCP | Gap | Recovery procedures exist in CTO head; not documented |
| Disaster recovery plan | AWS backup in place; no DR plan | Partial | No RTO/RPO defined |
| Crisis management procedures | No crisis management plan | Gap | |

### Art. 21(2)(d) — Supply chain security

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| Supplier security assessment | Not performed | Gap | No security criteria in supplier selection |
| Supplier security requirements in contracts | Standard SLAs only; no security clauses | Gap | |
| Supply chain risk register | None | Gap | |

### Art. 21(2)(g) — Cybersecurity training

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| Annual security awareness training | No formal training programme | Gap | Ad hoc awareness from CTO |
| Role-specific security training | None | Gap | |
| Phishing simulation | Never conducted | Gap | |

### Art. 21(2)(j) — Multi-factor authentication

| Requirement | Current State | Gap Score | Notes |
|-------------|--------------|-----------|-------|
| MFA on all remote access | MFA on AWS console but not on all SaaS tools | Partial | G Suite MFA not enforced for all users; no MFA on VPN |
| MFA on privileged accounts | AWS root account: MFA enabled; other admin accounts: mixed | Partial | |

---

## Gap Summary

| Framework | Compliant | Partial | Gap | Total Checked |
|-----------|----------|---------|-----|---------------|
| GDPR | 2 | 5 | 4 | 11 |
| NIS2 | 0 | 4 | 10 | 14 |
| **Total** | **2** | **9** | **14** | **25** |

**Key observations:**
- The organisation has some basic technical controls (encryption, cloud backups, MFA on some services) but has almost no documented security governance, procedures, or policies
- The most critical gaps are around incident response (no IRP, no breach notification procedure) and governance (no risk assessment, no security policy fit for purpose)
- NIS2 compliance is at an early stage — awareness of NIS2 obligations is limited within the organisation

See [`remediation-roadmap.md`](remediation-roadmap.md) for prioritised next steps.
