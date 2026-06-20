import urllib.request
import urllib.error
import json
import sys

if len(sys.argv) != 2:
    print("Usage: python3 github_activity.py <username>")
    sys.exit()

username = sys.argv[1]

url = f"https://api.github.com/users/{username}/events"

try:
    response = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("Error: User not found")
    sys.exit()

data = response.read().decode("utf-8")
events = json.loads(data)

if len(events) == 0:
    print("No recent activity found or user does not exist.")
    sys.exit()

for event in events:
    event_type = event["type"]
    repo = event["repo"]["name"]

    if event_type == "WatchEvent":
        print(f"- Starred {repo}")

    elif event_type == "PushEvent":
        branch = event["payload"]["ref"].replace("refs/heads/", "")
        print(f"- Pushed to {branch} branch in {repo}")

    elif event_type == "PullRequestEvent":
        print(f"- Opened pull request in {repo}")

    elif event_type == "CreateEvent":
        ref = event["payload"]["ref"]
        ref_type = event["payload"]["ref_type"]
        print(f"- Created {ref_type} '{ref}' in {repo}")

    elif event_type == "MemberEvent":
        action = event["payload"]["action"]
        print(f"- {action.capitalize()} as a member in {repo}")

    else:
        print(f"- {event_type} in {repo}")