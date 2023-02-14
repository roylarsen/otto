from logging import exception
import requests, json, urllib3, pprint

class GHAPI:
    def __init__(self, ghtoken):
        self.ghurl = "https://api.github.com/repos/"
        self.ghtoken = ghtoken

    def get_prs(self, repos, labels):
        headers = {
            "authorization" : "bearer " + self.ghtoken,
            "Accept": "application/vnd.github.v3+json"
        }

        resp = {}
        prs = []
        for repo in repos.split(","):
            resp[repo] = []
            r = requests.get("{0}{1}/pulls?state=open".format(self.ghurl, repo), headers=headers)
            for pull in r.json():
                for labels in pull["labels"]:
                    if "infrared" in labels["name"]:
                        pprint.pprint(pull)
                        prs.append(pull['number'])
                resp[repo] = prs
            prs = []
        return resp
    
    def get_workflows(self, repos):
        headers = {
            "authorization": "bearer " + self.ghtoken,
            "Accept": "application/vnd.github+json"
        }

        resp = {}
        workflows = []
        for repo in repos.split(","):
            resp[repo] = []
            r = requests.get("{0}{1}/actions/workflows".format(self.ghurl, repo), headers=headers)
            for workflow in r.json()['workflows']:   
                workflows.append(workflow['name'])
            
            resp[repo] = workflows
            workflows = []
        return resp
