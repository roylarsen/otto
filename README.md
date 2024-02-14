# otto

DevOps Automation tool. There's a lot of tasks that involve us repeating the same things over and over again, so I wanted to automate those

## Name Origins

The name `otto` comes from the Vermont Technical College radio station automation software. `otto`
handles (handled? - not sure if it's still used, it was a gross mess of Perl written by college students)
playing music and pre-recorded station IDs while there wasn't an active DJ. `otto` also handled scheduling requests taken
in over the Website.

## Installation instructions

`pip install git+ssh://git@github.com/roylarsen/otto.git#otto --user`

## Completed Features

* ~Retrieve open PRs for infrared team and format them for Slack~
* ~Installable by PIP~
* ~Driven by config (~/.otto.conf)~

## Planned Features

* Add Testing. PyTest or Tox
* Add support for templating for more easy Banyan/Terraform/Infrstructure testing
* Fix variables so there's more consistency
* Add better validation between a modules expoected configuration and what's provided by the config file
* Update checks
* Workflow kickoffs in banyan-deployments
* Modular CLI
