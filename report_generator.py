import json

def generate_report():
    data = json.load(open("agent_output.json"))
    json.dump(data, open("report.json", "w"), indent=2)
    return data
