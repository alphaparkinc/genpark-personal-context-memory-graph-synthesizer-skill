import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import PersonalContextMemoryGraphSynthesizerClient

def main():
    client = PersonalContextMemoryGraphSynthesizerClient()
    res = client.synthesize_context_graph()
    print("=== Personal Context Memory Graph Synthesizer Output ===")
    print(f"Target Entity: {res['target_entity']} | Context: {res['interaction_context']}")
    print(f"Memories Indexed: {res['synthesized_memories_count']} | Aggregate Salience: {res['aggregate_salience_score']}")
    print("\nTop Synthesized Insights (Decay-Weighted):")
    for b in res['executive_pre_briefing']:
        print(f"  * {b}")
    print("\nStrategic Agent Talking Points:")
    for tp in res['strategic_talking_points']:
        print(f"  - {tp}")

if __name__ == '__main__':
    main()
