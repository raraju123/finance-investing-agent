import fs from "fs";
import { exec } from "child_process";

console.log("⚙️ Node.js Orchestrator Agent Starting...");

exec("python agent.py", (error, stdout, stderr) => {
  if (error) {
    console.error("Python agent error:", error);
    return;
  }

  console.log("📡 Python Agent Output:");
  console.log(stdout);

  fs.writeFileSync("agent_output.json", stdout);
  console.log("💾 Saved agent_output.json");
});
