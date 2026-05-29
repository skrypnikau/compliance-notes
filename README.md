# EU Cyber Compliance Notes

![Focus](https://img.shields.io/badge/Focus-EU%20Cyber%20Compliance-purple)
![Frameworks](https://img.shields.io/badge/Frameworks-GDPR%20%7C%20NIS2%20%7C%20EU%20CRA-blue)
![Mapped To](https://img.shields.io/badge/Mapped%20To-ISO%2027001%20%7C%20NIST%20CSF-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

A personal study repository mapping EU cyber-compliance regulations (GDPR, NIS2, EU CRA) to established security control frameworks (ISO/IEC 27001:2022 and NIST Cybersecurity Framework 2.0). Includes a sample gap analysis for a fictional SME and a prioritised remediation roadmap.

This work was produced as part of self-study for roles in cybersecurity, GRC, and compliance, with a focus on understanding how regulatory obligations translate to practical security controls.

---

## Why This Matters

European organisations now face a layered compliance landscape:

- **GDPR** (since 2018) — security of personal data processing; breach notification
- **NIS2 Directive** (transposition deadline October 2024) — security obligations for essential and important entities
- **EU Cyber Resilience Act (CRA)** (entered into force October 2024) — security requirements for products with digital elements

Understanding how these regulations relate to each other — and to ISO 27001 and NIST CSF — is essential for:

1. **Avoiding duplicate work** — many controls satisfy multiple frameworks simultaneously
2. **Gap analysis** — knowing where your controls stand against each framework
3. **Reporting** — demonstrating compliance to auditors, regulators, and customers

---

## Frameworks Covered

| Framework | Version | Type | Scope |
|-----------|---------|------|-------|
| GDPR | EU 2016/679 | Regulation (binding) | Processing of personal data |
| NIS2 Directive | EU 2022/2555 | Directive (transposed into national law) | Essential and important entities |
| EU Cyber Resilience Act (CRA) | EU 2024/2847 | Regulation (binding) | Products with digital elements |
| ISO/IEC 27001 | 2022 edition | International standard (voluntary) | ISMS scope defined by organisation |
| NIST Cybersecurity Framework | 2.0 (2024) | Framework (voluntary) | Any organisation |

---

## Repository Structure

```
compliance-notes/
├── frameworks/
│   ├── gdpr-controls.md          GDPR articles mapped to ISO 27001 controls
│   ├── nis2-controls.md          NIS2 requirements mapped to NIST CSF
│   └── eu-cra-controls.md        EU CRA requirements mapped to controls
├── gap-analysis/
│   ├── gap-notes.md              Sample gap analysis for a fictional SME
│   └── remediation-roadmap.md    Prioritised remediation steps
├── reference/
│   ├── iso27001-summary.md       Quick reference ISO 27001 control families
│   └── nist-csf-summary.md       Quick reference NIST CSF functions and categories
├── mappings.json                 Structured GRC database mapping NIS2 to ISO & NIST CSF
└── grc_mapper.py                 Python GRC-as-Code CLI compliance mapper
```

---

## 🤖 GRC-as-Code Automation: Compliance Mapper

To transition these theoretical compliance mappings into active **GRC-as-Code**, this repository includes a structured JSON compliance database and a premium Python CLI automation tool (`grc_mapper.py`) that allows security teams to query, search, and export compliance maps instantly.

### Key Features
1. **Interactive Querying:** Instantly lookup the exact ISO 27001:2022 clauses and NIST CSF v2.0 controls required for any NIS2 Article (e.g. MFA, Supply Chain, Incident Handling, etc.).
2. **Search Capability:** Perform fuzzy search across compliance requirement titles, article references, and controls.
3. **Structured GRC Matrix:** Contains mappings for NIS2 Article 21 (risk-management measures).
4. **CSV Exporting:** Export the complete cross-framework compliance matrix to a professional CSV file for integration with corporate GRC dashboards (e.g. ServiceNow GRC, OneTrust, or internal audits).

### How to Use

#### 1. List All Mapped NIS2 Articles
```bash
python grc_mapper.py --list
```

#### 2. Query/Search Detailed Control Mappings
Search by article ID or keyword (e.g., "Article 21(2)(j)" or "MFA"):
```bash
python grc_mapper.py --article "MFA"
```

#### 3. Export to CSV Report
Generate a complete compliance mapping report:
```bash
python grc_mapper.py --export-csv compliance_matrix.csv
```

---

## Methodology

The mapping approach used in this repository:

1. **Read the source regulation** — identify each specific obligation or requirement (e.g., GDPR Article 32 requires "appropriate technical measures")
2. **Decompose to control-level requirements** — break the obligation into specific controls that would satisfy it
3. **Map to ISO 27001 Annex A** — identify which Annex A controls (2022 edition) satisfy each requirement
4. **Map to NIST CSF** — identify which CSF Functions, Categories, and Subcategories are relevant
5. **Note gaps** — where the regulation requires something not fully covered by ISO 27001 or NIST CSF, this is noted

**Scope note:** The mappings are intentionally simplified for study purposes. A production compliance programme would require a formal risk assessment, legal review, and context-specific analysis. These notes are not legal advice.

---

## Key Insights

**GDPR and ISO 27001 have significant overlap** — an organisation with a mature ISO 27001 ISMS will have satisfied many GDPR Article 32 obligations. The main GDPR-specific gaps are around data subject rights, breach notification timelines, and DPA requirements.

**NIS2 raises the bar significantly from NIS1** — it extends scope to a much larger number of sectors and entities, introduces stricter incident reporting (24h initial notification), and adds supply chain security requirements.

**The EU CRA introduces product security obligations** that are largely absent from traditional ISO 27001 implementations. Annex I of the CRA reads like a secure development lifecycle (SDLC) and vulnerability management standard.

**NIST CSF 2.0 added the Govern function** (new in 2024) — this aligns well with NIS2 governance requirements around board-level accountability.

---

## Author

**Yauheni Skrypnikau** — Cybersecurity Analyst
Studying EU cyber-regulation and GRC alongside technical blue-team skills.
*   **LinkedIn:** [linkedin.com/in/skrypnikau](https://www.linkedin.com/in/skrypnikau)
*   **GitHub:** [github.com/skrypnikau](https://github.com/skrypnikau)
