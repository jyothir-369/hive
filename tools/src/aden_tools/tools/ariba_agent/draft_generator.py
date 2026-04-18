
from .integrations import fetch_fabric_lab_data, fetch_research_citations


def generate_rfi_draft(opportunity: dict) -> str:
    fabric_data = fetch_fabric_lab_data()
    citations = fetch_research_citations(opportunity.get("description", ""))

    return f"""
Subject: Response to RFI - {opportunity.get('title')}

Dear Procurement Team,

We are pleased to respond to your opportunity.

Relevant Experience:
{fabric_data}

Proposed Approach:
- AI-driven architecture
- Cloud-native infrastructure
- Scalable enterprise systems

Research Support:
{citations}

We look forward to further engagement.

Best regards,
Procurement Automation Agent
""".strip()
