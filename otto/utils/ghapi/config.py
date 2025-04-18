class Config:
    """Standard class for lazy-loading otto modules"""
    CONFIGURATION = {"github": {
                        "pat": "UNSET - Follow instructions to create PAT here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token", 
                        "repos": "UNSET - Comma separated list with no spaces of repositories e.g. 'repo1,repo2'", 
                        "labels": "UNSET - Comma separated list with no spaces of repositories e.g. 'label1,label2'"
                    }}