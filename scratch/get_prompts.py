import json, os

transcript_path = r"C:\Users\thand\.gemini\antigravity\brain\23316da3-e558-4e4a-9c0f-11f4730e426e\.system_generated\logs\transcript_full.jsonl"

queries = [
    "beneficial_ownership_1791905876590",
    "internal_investigation_1791905942006",
    "cross_border_ma_1791905904638",
    "corporate_investigations_1791883501360",
    "executive_screening_1791883533720",
    "financial_fraud_1791883611509",
    "ma_due_diligence_1791883574148",
    "corp_intel_hero_1791911016830",
    "scoping_proposal_1791912865538",
    "services_hero_1791961043460",
    "service_details_hero_1791961248361",
    "about_hero_1791960866326",
    "home_corporate_hero_1791960604778",
    "about_advisory_spotlight_1791957294424",
    "case_scoping_spotlight_1791957173104",
    "transaction_feasibility_1791957393659",
    "risk_briefing_cta_1791960276856",
    "newsletter_briefing_1791955826007",
    "investigative_history_archive_1791978075346"
]

found = {}

with open(transcript_path, "r", encoding="utf-8", errors="ignore") as fp:
    for line in fp:
        for q in queries:
            if q in line:
                try:
                    data = json.loads(line)
                    # look in tool_calls or content
                    tc = data.get("tool_calls", [])
                    for call in tc:
                        if call.get("name") == "generate_image":
                            found[q] = call.get("args", {}).get("Prompt")
                except:
                    pass

for k, v in found.items():
    print(f"\n--- {k} ---")
    print(v)
