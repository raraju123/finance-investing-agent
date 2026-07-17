#!/bin/bash

echo "🚀 Multi-Agent Runtime Starting..."

if [ -f "agent.py" ]; then
    echo "▶ Starting Python agent..."
    python agent.py &
fi

if [ -f "agent.js" ]; then
    echo "▶ Starting Node.js agent..."
    node agent.js &
fi

if ls *.md 1> /dev/null 2>&1; then
    echo "▶ Hermes skill loaded (Markdown templates detected)"
fi

wait
