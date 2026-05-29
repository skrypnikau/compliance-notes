#!/usr/bin/env python3
"""
GRC-as-Code Compliance Mapper
Maps NIS2 compliance articles to ISO/IEC 27001:2022 clauses and NIST CSF v2.0 controls.
Author: Yauheni Skrypnikau
"""

import os
import json
import csv
import sys
import argparse

# ANSI color codes for premium terminal styling
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

MAPPINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mappings.json")

def load_mappings():
    try:
        with open(MAPPINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{RED}{BOLD}[ERROR]{RESET} Database file {MAPPINGS_FILE} not found. Please ensure mappings.json is in the same directory.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"{RED}{BOLD}[ERROR]{RESET} Failed to decode JSON database: {e}")
        sys.exit(1)

def print_header(title):
    border = "=" * 80
    print(f"\n{BLUE}{BOLD}{border}")
    print(f" {title.center(78)} ")
    print(f"{border}{RESET}\n")

def display_article(key, data):
    print(f"{CYAN}{BOLD}NIS2 Requirement:{RESET} {data['nis2_article']} - {BOLD}{data['nis2_title']}{RESET}")
    print(f"{YELLOW}Implementation Guidance:{RESET} {data['description']}")
    print("-" * 80)
    
    print(f"{GREEN}{BOLD}Mapped ISO/IEC 27001:2022 Controls:{RESET}")
    for ctrl in data.get("iso_27001", []):
        print(f"  • {BOLD}{ctrl['clause']:<10}{RESET} | {ctrl['title']}")
    if not data.get("iso_27001"):
        print("  None")
        
    print(f"\n{BLUE}{BOLD}Mapped NIST CSF v2.0 Controls:{RESET}")
    for ctrl in data.get("nist_csf", []):
        print(f"  • {BOLD}{ctrl['control']:<10}{RESET} | {ctrl['title']}")
    if not data.get("nist_csf"):
        print("  None")
    print("\n" + "=" * 80 + "\n")

def list_articles(mappings):
    print_header("NIS2 COMPLIANCE ARTICLES MATRIX")
    for key, data in mappings.items():
        print(f"• {GREEN}{BOLD}{data['nis2_article']:<18}{RESET} | {data['nis2_title']}")
    print(f"\nUse {BOLD}--article \"<Article Number>\"{RESET} to view detailed control mapping.")

def search_article(query, mappings):
    query_clean = query.lower().strip()
    matches = []
    
    # Try direct mapping key search first
    for key, data in mappings.items():
        if query_clean in data['nis2_article'].lower() or query_clean in data['nis2_title'].lower():
            matches.append((key, data))
            
    if not matches:
        print(f"{RED}{BOLD}[NO MATCH]{RESET} Could not find any NIS2 articles matching query: '{query}'")
        sys.exit(0)
        
    print_header(f"SEARCH RESULTS FOR: '{query.upper()}'")
    for key, data in matches:
        display_article(key, data)

def export_csv(filename, mappings):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["NIS2 Article", "NIS2 Title", "ISO 27001:2022 Clauses", "NIST CSF v2.0 Controls", "Implementation Guidance"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for key, data in mappings.items():
                iso_str = "; ".join([f"{c['clause']} ({c['title']})" for c in data.get("iso_27001", [])])
                nist_str = "; ".join([f"{c['control']} ({c['title']})" for c in data.get("nist_csf", [])])
                writer.writerow({
                    "NIS2 Article": data["nis2_article"],
                    "NIS2 Title": data["nis2_title"],
                    "ISO 27001:2022 Clauses": iso_str,
                    "NIST CSF v2.0 Controls": nist_str,
                    "Implementation Guidance": data["description"]
                })
        print(f"{GREEN}{BOLD}[SUCCESS]{RESET} GRC Compliance Matrix successfully exported to {BOLD}{filename}{RESET}")
    except Exception as e:
        print(f"{RED}{BOLD}[ERROR]{RESET} Failed to export CSV: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="GRC-as-Code: NIS2 to ISO 27001 & NIST CSF Compliance Mapper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python grc_mapper.py --list
  python grc_mapper.py --article "Article 21(2)(a)"
  python grc_mapper.py --article "MFA"
  python grc_mapper.py --export-csv compliance_matrix.csv
"""
    )
    parser.add_argument("--list", action="store_true", help="List all available NIS2 compliance articles in database")
    parser.add_argument("--article", type=str, metavar="QUERY", help="Lookup or search mappings for a specific NIS2 article or keyword")
    parser.add_argument("--export-csv", type=str, metavar="FILE", help="Export the complete compliance mapping matrix to a CSV file")
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
        
    args = parser.parse_args()
    mappings = load_mappings()
    
    if args.list:
        list_articles(mappings)
    elif args.article:
        search_article(args.article, mappings)
    elif args.export_csv:
        export_csv(args.export_csv, mappings)

if __name__ == "__main__":
    main()
