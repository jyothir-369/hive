from __future__ import annotations

from typing import Dict

from .integrations import fetch_fabric_lab_data, fetch_research_citations


def generate_rfi_draft(opportunity: Dict[str, object]) -> str:
    """
    Generate first-draft RFI response.
    """
    title = opportunity.get("title") or "Untitled Opportunity"

    try:
        fabric_data = fetch_fabric_lab_data()
    except Exception:
        fabric_data = []

    try:
        citations = fetch_research_citations(str(opportunity.get("description", "")))
    except Exception:
        citations = []

    return f"""
Subject: Response to RFI - {title}

Dear Procurement Team,

We are pleased to respond to your opportunity.

Relevant Experience:
{chr(10).join(fabric_data)}

Proposed Approach:
- AI-driven architecture
- Cloud-native infrastructure
- Scalable enterprise systems

Research Support:
{chr(10).join(citations)}

Best regards,
Procurement Automation Agent
""".strip()
