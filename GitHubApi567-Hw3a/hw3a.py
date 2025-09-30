import requests
import json


def list_repos(userID):
    url = f'https://api.github.com/users/{userID}/repos'
    response = requests.get(url)

    if response.status_code == 404:
        raise ValueError(f'Data for user "{userID}" was not found')
    
    user_repos = response.json()
    user_results = []

    for repo in user_repos:
        name = repo.get('name')
        if not name:
            continue
        
        commits_url = f'https://api.github.com/repos/{userID}/{name}/commits'
        commits_response = requests.get(commits_url)

        if commits_response.status_code == 404:
            commit_count = 0
        else:
            repo_commits = commits_response.json()
            commit_count = len(repo_commits)

        user_results.append({'repo': name, "commits": commit_count})
    return user_results

if __name__ == '__main__':
    userID = input("Please enter your GitHub user ID: ")
    repos = list_repos(userID)
    for r in repos:
        print(f"Repo: {r['repo']} Number of commits: {r['commits']}")
