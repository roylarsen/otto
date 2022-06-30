import click, os
from otto.utils.ghapi.ghapi import GHAPI
from otto.core.config.file import ConfigFile

@click.group("otto")
def cli():
    pass

@cli.group("config")
def config():
    """
    Sub-commands related to configuring the bd tool
    """
    pass

@config.command()
def create():
    """Creates a new config if none exists"""
    config = ConfigFile()

    if not config.check():
        print("Creating new config at {0}".format(config.conffile))
        config.create()
    else:
        print("Config already exists at {0}".format(config.conffile))

@cli.group("deploy")
def deploy():
    """NOT IMPLEMENTED
    Sub-commands involved in deployments
    \n\r\t With Great Power Comes Great Responsibity 
    \n\t\t- Uncle Ben 
    \n\r\t\t\t- Roy Larsen
    """
    pass

@cli.group("gh")
def gh():
    """Sub-commands involved in retrieving information from GitHub"""
    if os.environ.get("GITHUB_TOKEN") is None:
        print("Please make sure to set the GITHUB_TOKEN environment variable with your GitHubPAT")
    pass

@gh.command()
@click.option("-r", "--repos", default="mh-iac,banyan-deployments", help="Comma separated list of repositories to get PRs from. By default, mh-iac and banyan-deployments")
@click.option("-f", "--format", is_flag=True, default=False, help="Formats the output for posting on Slack")
def get_prs(repos, format):
    """Gets PRs based on rules"""
    if os.environ.get("GITHUB_TOKEN") is not None:
        token = os.environ.get("GITHUB_TOKEN")
    gh = GHAPI(ghtoken=token)

    if format:
        for repo, prs in gh.get_prs(repos).items():
            print("*{0}*".format(repo))
            for pr in prs:
                for url, details in pr.items():
                    print(" * {0} \n\t* Title: {1} \n\t* Author: {2}".format(url, details[0], details[1]))
    else:
        print(gh.get_prs(repos))

if __name__ == "__main__":
    cli()