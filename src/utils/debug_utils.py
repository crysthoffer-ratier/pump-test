DEBUG_MODE = True

def debug_message(msg: str) -> None:
    if DEBUG_MODE:
        print(f"[DEBUG]: {msg}")