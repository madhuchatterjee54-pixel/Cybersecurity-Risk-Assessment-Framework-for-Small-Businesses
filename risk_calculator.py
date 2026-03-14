"""
Cybersecurity Risk Calculator for SMEs
Interactive Menu-Driven Tool
"""
import time

def clear_screen():
    print("\n" * 50)

def print_header():
    print("=" * 60)
    print("   SME CYBERSECURITY RISK ASSESSMENT CALCULATOR")
    print("=" * 60)

def display_scales():
    print("\n--- Evaluation Scales ---")
    print("Likelihood (Probability):")
    print("  1 - Rare (Highly unlikely)")
    print("  2 - Unlikely (Not expected, but possible)")
    print("  3 - Possible (Might occur)")
    print("  4 - Likely (Probably will occur)")
    print("  5 - Almost Certain (Expected in most circumstances)")
    print("\nImpact (Severity):")
    print("  1 - Negligible (Minor inconvenience)")
    print("  2 - Minor (Small disruption, minimal data exposure)")
    print("  3 - Moderate (Noticeable disruption, some financial loss)")
    print("  4 - Significant (Major disruption, severe damage)")
    print("  5 - Severe (Business threatened, catastrophic loss)")
    print("-" * 60 + "\n")

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"-> Error: Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("-> Error: Please enter a valid whole number.")

def calculate_risk(likelihood, impact):
    score = likelihood * impact
    
    if score <= 4:
        category = "LOW RISK (Green)"
        action = "Acceptable risk. Maintain current security controls."
    elif score <= 9:
        category = "MEDIUM RISK (Yellow)"
        action = "Monitor closely. Implement cost-effective mitigations."
    elif score <= 16:
        category = "HIGH RISK (Orange)"
        action = "Unacceptable risk. Prompt mitigation planning and execution required."
    else:
        category = "CRITICAL RISK (Red)"
        action = "CRITICAL PRIORITY. Stop operations if necessary; immediate aggressive mitigation."
        
    return score, category, action

def add_new_threat():
    clear_screen()
    print_header()
    print("\n--- Assess a New Threat ---")
    
    threat_name = input("\nEnter the name or description of the threat (e.g., 'Phishing via Email'): ")
    
    display_scales()
    
    print(f"\nEvaluating: '{threat_name}'")
    likelihood = get_valid_input("Enter the LIKELIHOOD score (1-5): ", 1, 5)
    impact = get_valid_input("Enter the IMPACT score (1-5): ", 1, 5)
    
    score, category, action = calculate_risk(likelihood, impact)
    
    print("\n" + "=" * 60)
    print("   ASSESSMENT RESULTS  ")
    print("=" * 60)
    print(f"Threat Target : {threat_name}")
    print(f"Metrics       : Likelihood ({likelihood}) x Impact ({impact})")
    print(f"Risk Score    : {score} / 25")
    print(f"Risk Category : {category}")
    print(f"Recommended   : {action}")
    print("=" * 60)
    
    input("\nPress Enter to return to the Main Menu...")

def show_case_studies():
    clear_screen()
    print_header()
    print("\n--- View Case Studies ---")
    print("1. Local Retail Store (PoS Ransomware)")
    print("2. Accounting Firm (Spear-Phishing Data Breach)")
    print("3. Remote Agency (Public Wi-Fi Man-in-the-Middle)")
    print("0. Go Back")
    
    choice = input("\nSelect a case study to view (0-3): ")
    
    print("\n" + "-" * 50)
    if choice == "1":
        print("Retail Store Threat: Ransomware infection via malicious link.")
        print("Initial Risk : High Risk (Score: 12)")
        print("Mitigation   : Network segmentation & Endpoint Detection (EDR).")
        print("Residual Risk: Low Risk (Score: 4)")
    elif choice == "2":
        print("Accounting Firm Threat: IRS Spear-Phishing credential theft.")
        print("Initial Risk : Critical Risk (Score: 20)")
        print("Mitigation   : Enforced MFA and advanced email filtering.")
        print("Residual Risk: Medium Risk (Score: 6)")
    elif choice == "3":
        print("Remote Agency Threat: Session hijacking over public Wi-Fi.")
        print("Initial Risk : High Risk (Score: 12)")
        print("Mitigation   : Mandatory Corporate VPN/ZTNA usage.")
        print("Residual Risk: Low Risk (Score: 3)")
    elif choice == "0":
        return
    else:
        print("Invalid selection.")
        
    input("\nPress Enter to return to the Main Menu...")

def main_menu():
    while True:
        clear_screen()
        print_header()
        print("\nMain Menu:")
        print("  [1] Assess a New Cybersecurity Threat")
        print("  [2] View Evaluation Scoring Matrix (Help)")
        print("  [3] View Example Case Studies from Report")
        print("  [0] Exit Application")
        
        choice = input("\nEnter your choice (0-3): ")
        
        if choice == '1':
            add_new_threat()
        elif choice == '2':
            clear_screen()
            print_header()
            display_scales()
            input("\nPress Enter to return to the Main Menu...")
        elif choice == '3':
            show_case_studies()
        elif choice == '0':
            print("\nExiting the Risk Calculator. Stay secure!")
            time.sleep(1)
            break
        else:
            print("\n-> Invalid choice. Please enter a number between 0 and 3.")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()
