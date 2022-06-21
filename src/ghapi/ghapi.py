from logging import exception
import requests, json, urllib3

class GHAPI:
    def __init__(self, ghtoken):
        self.ghurl = "https://api.github.com/repos/hca-mobilehb/"
        self.ghtoken = ghtoken

    def get_prs(self, repos, label):
        headers = {
            "authorization" : "bearer " + self.ghtoken,
            "Accept": "application/vnd.github.v3+json"
        }

        resp = {}
        prs = []
        for repo in repos.split(","):
            resp[repo] = []
            r = requests.get("{0}{1}/pulls".format(self.ghurl, repo), headers=headers)
            for pull in r.json():
                for labels in pull["labels"]:
                    if label in labels["name"]:
                        prs.append({pull['html_url'] : [pull['title'], pull['user']['login']]})
                resp[repo] = prs
            prs = []
        return resp