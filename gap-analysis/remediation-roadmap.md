# Remediation Roadmap — DataSync Ltd (Fictional)

**Based on:** Gap analysis in gap-notes.md
**Purpose:** Prioritised plan to address identified compliance gaps against GDPR and NIS2

---

## Prioritisation Criteria

Gaps are prioritised using the following factors:

1. **Regulatory risk** — How significant is the gap relative to regulatory obligations?
2. **Business risk** — Could exploitation cause serious business disruption or customer harm?
3. **Implementation effort** — How long and how expensive is remediation?
4. **Quick wins** — Low-effort, high-impact actions to do immediately

---

## Priority 1 — Critical (Address Within 30 Days)

### P1-01: Document and test an Incident Response Plan (IRP)

**Gap addressed:** NIS2 Art. 21(2)(b); GDPR Art. 33
**Why critical:** Without an IRP, the organisation cannot meet the NIS2 24/72-hour reporting obligations or GDPR 72-hour breach notification. In the event of an incident, response will be chaotic and legal deadlines will be missed.

**Actions:**
1. Appoint an incident response owner (CTO or Deputy)
2. Define incident classification criteria (Low / Medium / High / Critical)
3. Document the escalation chain for each severity level
4. Identify and record contact details for: national CSIRT, Data Protection Authority (DPA), legal counsel
5. Create a one-page quick-reference card for the on-call person
6. Run a tabletop exercise simulating a data breach within 30 days of completing the IRP
7. Document the NIS2 reporting procedure: who reports, to whom, what information, by when

**Effort:** Medium (1-2 weeks of focused work by CTO + legal counsel input)
**Cost:** Low (internal effort + legal review)

---

### P1-02: Enforce MFA on all administrative and remote access

**Gap addressed:** NIS2 Art. 21(2)(j)
**Why critical:** Accounts without MFA are among the most common attack vectors. This is a quick technical win.

**Actions:**
1. Enforce MFA for all users in Google Workspace via Admin Console
2. Enable MFA on the VPN
3. Review AWS IAM: disable any admin accounts that do not have MFA
4. Policy: no new admin account is created without MFA enforced at creation

**Effort:** Low (1-3 days of technical work)
**Cost:** Low

---

### P1-03: Verify Data Processing Agreements with all sub-processors

**Gap addressed:** GDPR Art. 28
**Why critical:** Processing personal data through sub-processors without valid DPAs is a direct GDPR violation.

**Actions:**
1. Create a register of all third-party services that receive or process personal data
2. For each sub-processor, verify a valid DPA or Standard Contractual Clauses is in place
3. Contact Twilio, HubSpot, and Zendesk to obtain signed DPAs
4. Maintain the sub-processor register as a living document

**Effort:** Low to medium (1 week)
**Cost:** Low (DPAs are typically freely available from major vendors)

---

## Priority 2 — High (Address Within 90 Days)

### P2-01: Conduct a formal risk assessment and create a risk register

**Gap addressed:** NIS2 Art. 21(2)(a); ISO 27001 Clause 6.1
**Why high:** Without a risk register, security investments are ad hoc and gaps may be systematically missed.

**Actions:**
1. Define the scope of the risk assessment
2. Create an asset inventory (cloud resources, on-premises, data categories)
3. Use a simple risk matrix (likelihood x impact)
4. Identify top 10 risks with risk owner, risk score, and current controls
5. Review and update risk register quarterly

**Effort:** Medium (2-3 weeks for first assessment)

---

### P2-02: Implement centralised logging and basic SIEM capability

**Gap addressed:** NIS2 Art. 21(2)(b); GDPR Art. 32
**Why high:** Current detection relies on AWS GuardDuty only. On-premises events are not logged centrally.

**Actions:**
1. Evaluate SIEM options: Microsoft Sentinel, Elastic SIEM, or a managed SIEM service
2. Define log sources: AWS CloudTrail, GuardDuty, VPN logs, Windows Event logs, GSuite audit logs
3. Set up centralised log collection with minimum 90-day retention
4. Create basic detection rules: failed login threshold, new admin user created, large data download
5. Define an alert triage process

**Effort:** High (4-8 weeks)
**Cost:** Moderate (SIEM licensing or managed service)

---

### P2-03: Create and communicate an information security policy suite

**Gap addressed:** NIS2 Art. 21(2)(a); ISO 27001 control 5.1

**Policies to create:**
1. Information Security Policy (top-level, management-approved)
2. Acceptable Use Policy
3. Access Control and User Account Management Policy
4. Incident Response Policy (links to IRP from P1-01)
5. Data Classification and Handling Policy
6. Remote Working and BYOD Policy

**Effort:** Medium (1-2 weeks per policy; can be templated)

---

### P2-04: Implement a security awareness training programme

**Gap addressed:** NIS2 Art. 21(2)(g)

**Actions:**
1. Select a training platform (KnowBe4, Proofpoint, or SANS Securing the Human)
2. Assign mandatory annual training for all staff
3. Run a baseline phishing simulation
4. Deliver targeted training for IT admin and finance staff

**Effort:** Low to medium
**Cost:** Low to moderate (training platform subscription)

---

## Priority 3 — Medium (Address Within 180 Days)

### P3-01: Create and test a Business Continuity Plan and Disaster Recovery Plan

**Gap addressed:** NIS2 Art. 21(2)(c)

**Actions:**
1. Define RTO and RPO for critical services
2. Document recovery procedures for the top 3 failure scenarios
3. Test backup restoration and document results
4. Conduct a tabletop exercise simulating a major outage

---

### P3-02: Implement supplier security assessment process

**Gap addressed:** NIS2 Art. 21(2)(d)

**Actions:**
1. Create a tiered supplier classification (critical / standard / low-risk)
2. For critical suppliers: require security questionnaire or review of certifications (ISO 27001, SOC 2)
3. Add minimum security requirements to new supplier contracts
4. Review critical suppliers annually

---

### P3-03: Review and remediate AWS IAM permissions

**Gap addressed:** GDPR Art. 32; NIS2 Art. 21(2)(i)

**Actions:**
1. Run AWS IAM Access Analyzer to identify over-permissioned roles
2. Apply principle of least privilege
3. Remove or disable inactive IAM users or access keys
4. Enable AWS CloudTrail on all regions and accounts

---

## Roadmap Summary Table

| ID | Action | Priority | Effort | Target Date |
|----|--------|---------|--------|-------------|
| P1-01 | Document and test IRP | Critical | Medium | +30 days |
| P1-02 | Enforce MFA everywhere | Critical | Low | +14 days |
| P1-03 | Verify DPAs with sub-processors | Critical | Low | +30 days |
| P2-01 | Conduct risk assessment | High | Medium | +90 days |
| P2-02 | Implement SIEM | High | High | +90 days |
| P2-03 | Create policy suite | High | Medium | +90 days |
| P2-04 | Security awareness training | High | Low | +60 days |
| P3-01 | BCP and DRP | Medium | Medium | +180 days |
| P3-02 | Supplier security assessment | Medium | Medium | +180 days |
| P3-03 | IAM remediation | Medium | Low | +60 days |
