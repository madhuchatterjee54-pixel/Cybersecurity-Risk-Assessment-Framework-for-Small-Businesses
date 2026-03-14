# Cybersecurity Risk Assessment Framework for Small Businesses (SMEs)

## Executive Summary
This document outlines a comprehensive Cybersecurity Risk Assessment Framework tailored specifically for Small and Medium-sized Enterprises (SMEs). It provides a structured approach to identifying, evaluating, and mitigating cyber threats, culminating in practical case studies that validate the model.

## 1. Common Cybersecurity Risks in SMEs
SMEs often lack the robust security infrastructure of larger enterprises, making them prime targets for malicious actors. The most prevalent risks include:
*   **Phishing & Social Engineering:** Fraudulent emails or communications intended to trick employees into revealing credentials or sensitive information.
*   **Ransomware & Malware:** Malicious software that encrypts business-critical data, halting operations until a ransom is paid.
*   **Insider Threats:** Accidental data leaks by uninformed employees or intentional sabotage by disgruntled staff.
*   **Weak Authentication:** Reliance on single, easily guessable passwords without Multi-Factor Authentication (MFA).
*   **Unsecured Remote Access:** Vulnerabilities introduced by remote work, such as unsecured Wi-Fi networks and lack of VPNs.
*   **Supply Chain Attacks:** Compromises originating from third-party vendors or software providers with weak security postures.

## 2. Risk Assessment Model
To provide a scalable and industry-standard approach, this framework adapts the **NIST Cybersecurity Framework (CSF)** core functions for SMEs:
1.  **Identify:** Inventory all hardware, software, and sensitive data. Understand the business context and resources that support critical functions.
2.  **Protect:** Implement safeguards to ensure delivery of services. This includes access control, awareness training, data encryption, and network security.
3.  **Detect:** Define continuous monitoring mechanisms to identify occurrences of cybersecurity events in a timely manner (e.g., antivirus monitoring, log reviews).
4.  **Respond:** Develop an Incident Response plan. Define actions to take regarding a detected cybersecurity incident to contain its impact.
5.  **Recover:** Formulate a recovery plan to restore any capabilities or services impaired during an incident. Focus on resilient backups.

## 3. Risk Evaluation Metric
To rank threats based on severity and impact, we utilize a **5x5 Risk Matrix**. 
*   **Risk Score = Likelihood × Impact**

**Likelihood (Probability of Occurrence):**
1.  **Rare:** Highly unlikely to occur.
2.  **Unlikely:** Not expected to happen but possible.
3.  **Possible:** Might occur at some time.
4.  **Likely:** Will probably occur in most circumstances.
5.  **Almost Certain:** Expected to occur in most circumstances.

**Impact (Severity of Consequences):**
1.  **Negligible:** Minor inconvenience, no financial loss.
2.  **Minor:** Small operational disruption, minimal data exposure.
3.  **Moderate:** Noticeable operational disruption, some financial loss.
4.  **Significant:** Major disruption to critical services, severe financial or reputational damage.
5.  **Severe:** Business sustainability threatened, catastrophic data loss.

**Risk Tiers:**
*   **1 - 4 (Low Risk):** Acceptable risk; maintain current controls.
*   **5 - 9 (Medium Risk):** Monitor risk; implement mitigations when cost-effective.
*   **10 - 16 (High Risk):** Unacceptable risk; prompt mitigation planning and execution required.
*   **17 - 25 (Critical Risk):** Stop operations if necessary; immediate and aggressive mitigation required.

## 4. Risk Mitigation Strategies
Mitigation strategies should be scaled to the SME's budget and technical capability.
*   **Implement Multi-Factor Authentication (MFA):** Require MFA for all critical systems, especially email, VPNs, and financial platforms.
*   **Automated Off-site Backups:** Employ the 3-2-1 backup rule (3 copies, 2 different media, 1 off-site/cloud) ensuring backups are immutable (immune to ransomware).
*   **Next-Generation Firewalls (NGFW) & EDR:** Upgrade from traditional antivirus to Endpoint Detection and Response (EDR) solutions, paired with a modern edge firewall.
*   **Employee Security Awareness Training:** Conduct quarterly mandatory phishing simulations and security best-practice training.
*   **Patch Management Policy:** Automate OS and third-party application updates to eliminate known vulnerabilities.
*   **Network Segmentation:** Isolate critical data (like point-of-sale systems) from general employee networks and guest Wi-Fi.

## 5. Model Validation: Case Studies

### Case Study A: Local Retail Store
*   **Business Profile:** Brick-and-mortar boutique with an online Shopify presence and a local Point-of-Sale (PoS) system.
*   **Identified Threat:** Ransomware attack on the PoS network via an employee clicking a malicious link on a store computer.
*   **Risk Evaluation:** Likelihood (3 - Possible) × Impact (4 - Significant) = **12 (High Risk)**.
*   **Mitigation Strategy Applied:** Network segmentation (isolating the PoS terminal from the general web-browsing computer), installing EDR, and disabling web browsing on the PoS machine.
*   **Post-Mitigation Risk:** Likelihood (1 - Rare) × Impact (4 - Significant) = **4 (Low Risk)**.

### Case Study B: Small Accounting Firm
*   **Business Profile:** 10-person firm handling highly sensitive client tax and financial records.
*   **Identified Threat:** Credential harvesting via a spear-phishing campaign posing as the IRS, leading to mass data exfiltration.
*   **Risk Evaluation:** Likelihood (4 - Likely) × Impact (5 - Severe) = **20 (Critical Risk)**.
*   **Mitigation Strategy Applied:** Enforced strict MFA on all accounts, deployed advanced email spam/phishing filters, and trained staff on verification protocols for unexpected emails.
*   **Post-Mitigation Risk:** Likelihood (2 - Unlikely) × Impact (3 - Moderate - due to early containment) = **6 (Medium Risk)**.

### Case Study C: Remote-First Marketing Agency
*   **Business Profile:** 15 employees working fully remote, utilizing personal Wi-Fi and SaaS applications.
*   **Identified Threat:** Man-in-the-Middle (MitM) attack over unsecured public Wi-Fi leading to session hijacking.
*   **Risk Evaluation:** Likelihood (4 - Likely) × Impact (3 - Moderate) = **12 (High Risk)**.
*   **Mitigation Strategy Applied:** Mandatory usage of a corporate VPN or Zero Trust Network Access (ZTNA) solution when connecting from untrusted networks, and enforcing endpoint device encryption.
*   **Post-Mitigation Risk:** Likelihood (1 - Rare) × Impact (3 - Moderate) = **3 (Low Risk)**.

## 6. Documented Findings and Best Practices
### Key Findings
1.  **Human Element remains the weakest link:** Across all case studies, employee actions (clicking links, poor passwords) were the primary attack vectors.
2.  **Basic Hygiene provides massive ROI:** Complex security tools are often unnecessary if foundational hygiene (MFA, Backups, Patching) is maintained.
3.  **Risk calculation clarifies priorities:** Business owners respond better to the 5x5 matrix than to technical jargon, as it contextualizes cyber threats as business risks.

### Best Practices for SMEs
*   **Adopt a "Culture of Security":** Security should not just be an IT problem; it should be part of the SME's daily operational mindset.
*   **Leverage Managed Service Providers (MSPs):** If in-house IT expertise is lacking, partnering with a reputable MSP can bridge the security gap affordably.
*   **Prepare for the Worst:** Assume a breach *will* happen. Have a printed Incident Response checklist ready so employees know exactly who to call when a screen goes dark or money goes missing.
