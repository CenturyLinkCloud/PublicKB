{{{
"title": "Cloud Platform - Release Notes: November 8, 2016",
"date": "11-08-2016",
"author": "Daniel Stephan",
"attachments": [],
"contentIsHTML": false
}}}


### Enhancements (3)

* __AppFog Cloud Foundry Upgrade:__

__Why__: We upgraded the Cloud Foundry platform underlying AppFog from v233, to the latest release, v245. This upgrade includes security patches, bug fixes, buildpack updates, and additional functionality. For more details on the specific CVEs resolved, buildpack changes, etc., please visit the [CF Release Notes](https://github.com/cloudfoundry/cf-release/releases) page.

__Required Actions__: All AppFog users should upgrade their CLI to the most recent version to ensure API compatibility. Download the CLI [here](https://github.com/cloudfoundry/cli).

__Known Issues__: cf-release v245 contains an issue staging Python buildpack-based apps and any apps using any buildpack that doesn't return a process type in the staging result. In the meantime, the workaround is to add a file called `Procfile` to the application root directory, containing the command: `web: python <appname.py>` (<appname.py> is the Python app name, e.g. `hello-world.py` ). More info on Procfiles [here](https://docs.cloudfoundry.org/buildpacks/prod-server.html#procfile).

- __Scheduled Maintenance__: The maintenance windows were scheduled as follows:
- The AppFog US West (UC1) upgrade began on Mon Oct 31 at 8:00 AM PDT (GMT-7). 
- The AppFog US East (VA1) upgrade began on Wed Nov 2 at 8:00 AM PDT (GMT-7).


### Announcements (1)

* __MSSQL Relational DB Beta Program Launches!__

We are now accepting beta customer requests for our MSSQL Relational DB Beta.  The beta service is currently limited to IL1 and includes a single instance of MSSQL with private routing, daily backups held for 7 days and configurable backup time.  Keep watching release notes for announcements on when new beta features and locations are added.  If you are interested in joining the beta program, please visit [https://www.ctl.io/relational-database/](https://www.ctl.io/relational-database/).
