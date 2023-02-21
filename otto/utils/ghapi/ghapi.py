from logging import exception
import requests, json

class GHAPI:
    def __init__(self, ghtoken):
        self.ghtoken = ghtoken

    def get_prs(self, repos, labels):
        headers = {
            "Authorization" : f"bearer {self.ghtoken}",
        }
        prs = {}
        repos = repos.split(",")
        for repo in repos:
            payload = {
                "query": f"""
                    query {{
                        repository(owner: "{repo.split('/')[0]}", name: "{repo.split('/')[1]}"){{
                            pullRequests(first:15,labels:"{labels}",states:OPEN){{
                                edges{{
                                    node{{
                                        author{{
                                            login
                                        }}
                                        title
                                        url
                                    }}
                                }}
                            }}
                        }}
                    }}
                """
            } 

            r = requests.post("https://api.github.com/graphql", headers=headers, data=json.dumps(payload))
            prs[repo.split('/')[1]] = r.json()['data']['repository']['pullRequests']['edges']
        return prs
    
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
