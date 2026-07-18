import json, os

FILE = "agent_memory.json"

def load_memory():
    return json.load(open(FILE)) if os.path.exists(FILE) else {"history": []}

def save_memory(entry):
    mem = load_memory()
    mem["history"].append(entry)
    json.dump(mem, open(FILE, "w"), indent=2)
