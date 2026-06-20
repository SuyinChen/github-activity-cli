# GitHub Activity CLI

Project URL:
https://roadmap.sh/projects/github-user-activity

A simple Python command-line application that fetches and displays recent GitHub user activity using the GitHub API.

## Usage

```bash
python3 github_activity.py <username>
```

Example:

```bash
python3 github_activity.py SuyinChen
```

## Sample Output

```text
- Starred nilbuild/developer-roadmap
- Created branch 'monica-ai-ads' in jlb8dh-tech/photo-to-sim
- Opened pull request in jlb8dh-tech/photo-to-sim
- Pushed to main branch in jlb8dh-tech/photo-to-sim
```

## Features

- Fetch recent GitHub activity
- Parse GitHub API responses
- Human-readable event formatting
- Error handling for invalid usernames
- Error handling for missing arguments

## Technologies

- Python
- GitHub REST API
- JSON
- CLI