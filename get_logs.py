import json
import urllib.request
import sys

# Load runs
with open('runs.json') as f:
    data = json.load(f)

# Find first failing 'Build, Scan and Push Docker Image'
failed_run = None
for run in data.get('workflow_runs', []):
    if run['name'] == 'Build, Scan and Push Docker Image' and run['conclusion'] == 'failure':
        failed_run = run
        break

if not failed_run:
    print("No failing run found")
    sys.exit(0)

# Fetch jobs for this run
req = urllib.request.Request(failed_run['jobs_url'])
with urllib.request.urlopen(req) as response:
    jobs_data = json.loads(response.read().decode())

# Find failed steps
for job in jobs_data.get('jobs', []):
    if job['conclusion'] == 'failure':
        print(f"Job failed: {job['name']}")
        for step in job['steps']:
            if step['conclusion'] == 'failure':
                print(f"Step failed: {step['name']}")
                # We can't fetch step logs easily without auth, but we know the step name.
