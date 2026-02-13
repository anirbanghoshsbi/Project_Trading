from state_manager import get_trade_state, is_profit_phase

DECISION_TIME = "15:15"

def handle_message(msg):
    msg = msg.lower()

    # Stop-loss interference
    if "reduce" in msg or "adjust" in msg:
        return "Stop-loss modification detected. This is interference. Return to original plan."

    # Early entry detection
    if "entered" in msg or "took trade" in msg:
        if not decision_time_reached():
            return "Violation. Decision time is 3:15 PM only."

    # Strategy switching
    if "orb" in msg or "options instead" in msg:
        return "Strategy deviation detected. Sandbox only. Live system remains Elder Impulse."

    # Profit phase containment
    if is_profit_phase():
        return "Performance phase detected. Maintain system. No optimization."

    return "Acknowledged. Maintain discipline."

    # ==========================
    # 2️⃣ LLM BEHAVIORAL ANALYSIS
    # ==========================

    context = get_context()

    try:
        llm_response = call_llm(original_msg, context)

        parsed = json.loads(llm_response)
        risk = parsed.get("risk", "Unknown")
        message = parsed.get("message", "Maintain discipline.")

        # Log behavior with risk level
        log_behavior(original_msg, risk, message)

        return message

    except Exception:
        # Fallback safety if LLM fails
        fallback = "Discipline required. Maintain system rules."
        log_behavior(original_msg, "LLM_ERROR", fallback)
        return fallback

def decision_time_reached():
    from datetime import datetime
    now = datetime.now().strftime("%H:%M")
    return now >= DECISION_TIME

