# readthedocs setup notes

> I am not 100% on the best way to set up automation rules for us. For many of our repos, it might be better just to set a single rule that catches every new GitHub release and sets it as default.

* Settings
  * Programming Language: `Python`
* Advanced Settings
  * Default version: `Stable` (ideally)
  * Versioning scheme: `Multiple versions without translation`
  * Build pull requests for this project
* Integrations
  * GitHub Incoming Webhook
* Environment variables
  * `SPHINX_GITHUB_CHANGELOG_TOKEN`: provide a read-only fine-grained github token (https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#fine-grained-personal-access-tokens). I have an active one. It'll require renewal at least every 12 months.
* Automation rules
  * Stable release rule
    * Match: `Custom match`
    * Custom match: a pattern for latest stable release
    * Version type: `Tag`
    * Action: `Set version as default`
  * Dev version release rule
    * Match: `Custom match`
    * Custom match: a pattern for a dev release
    * Version type: `Tag`
    * Action: `Activate version`
