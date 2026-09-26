import json
import time
from typing import Dict, Any, List, Optional

class PersonalContextMemoryGraphSynthesizerClient:
    """
    Production-grade personal episodic memory and context graph synthesizer.
    Aggregates emails, notes, Slack pings, and documents into an entity relationship graph
    with recency decay weighting to provide instant pre-interaction briefings for personal agents.
    """
    def __init__(self, decay_half_life_days: float = 14.0):
        self.decay_half_life = decay_half_life_days

    def synthesize_context_graph(
        self,
        target_entity: str = "Dr. Julian Vance",
        interaction_context: str = "Upcoming Partnership Strategy Call",
        memory_snippets: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        if not memory_snippets:
            memory_snippets = [
                {"source": "Email", "days_ago": 3, "summary": "Mentioned their team is finalizing Series B round with Sequoia", "sentiment": "positive", "importance": 0.95},
                {"source": "Meeting Note", "days_ago": 18, "summary": "Expressed strong interest in adopting our automated MCP agent pipelines", "sentiment": "positive", "importance": 0.88},
                {"source": "Slack DM", "days_ago": 35, "summary": "Preferred communication via Signal or asynchronous voice memos over Zoom", "sentiment": "neutral", "importance": 0.70},
                {"source": "Calendar Event", "days_ago": 1, "summary": "Confirmed 30-minute sync for Thursday 2:00 PM EST", "sentiment": "neutral", "importance": 0.80}
            ]

        weighted_insights = []
        cumulative_salience = 0.0

        for m in memory_snippets:
            days = m["days_ago"]
            decay = round(0.5 ** (days / self.decay_half_life), 3)
            salience = round(m["importance"] * decay, 3)
            cumulative_salience += salience
            weighted_insights.append({
                "source": m["source"],
                "recency_days": days,
                "salience_score": salience,
                "insight": m["summary"]
            })

        # Sort by salience
        weighted_insights.sort(key=lambda x: x["salience_score"], reverse=True)

        return {
            "synthesis_id": "ctx_mem_5510",
            "target_entity": target_entity,
            "interaction_context": interaction_context,
            "synthesized_memories_count": len(memory_snippets),
            "aggregate_salience_score": round(cumulative_salience, 2),
            "executive_pre_briefing": [w["insight"] for w in weighted_insights[:3]],
            "strategic_talking_points": [
                f"Acknowledge momentum on their recent milestone ({weighted_insights[0]['insight']})",
                "Present bespoke MCP integration roadmap as requested in prior session",
                "Respect asynchronous preference for subsequent follow-up deliverables"
            ],
            "recommended_personal_agent_demeanor": "CONFIDENT_PARTNER_EMPATHETIC"
        }
