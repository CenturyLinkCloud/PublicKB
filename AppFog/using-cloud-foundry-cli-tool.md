{{{ "title": "Using the Cloud Foundry CLI Tool", "date": "01-26-2016", "author": "Ben Heisel", "attachments": [], "related-products" : [], "contentIsHTML": false }}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

AppFog Users

### Overview

This article is intended to provide the available commands using the Cloud Foundry CLI `cf` tool, version 6.x. For more information refer to the [Cloud Foundry Docs](https://docs.cloudfoundry.org/devguide/installcf) or how to [Install the CLI Tool](login-using-cf-cli.md).

### Common Commmand examples

* Deploy an application using `cf push <APP_NAME>`. By default, the `cf push` command looks for a manifest.yml file in the current working directory. Use the -f option to provide a non-standard manifest location or filename. For more information refer to this document on [Using a Manifest File](http://docs.cloudfoundry.org/devguide/deploy-apps/manifest.html). Here are possible options when pushing an application:
```
cf push APP_NAME [-b BUILDPACK_NAME] [-c COMMAND] [-d DOMAIN] [-f MANIFEST_PATH] [--docker-image DOCKER_IMAGE]
   [-i NUM_INSTANCES] [-k DISK] [-m MEMORY] [-n HOST] [-p PATH] [-s STACK] [-t TIMEOUT] [-u HEALTH_CHECK_TYPE]
   [--no-hostname] [--no-manifest] [--no-route] [--no-start]
```
This example deploys an application named `example-app` with 2 instances, each with a memory allocation of 256M,  and using a specific buildpack:
```
cf push example-app -i 2 -m 256M -b https://github.com/CenturyLinkCloud/php-buildpack.git#af_custom_php
```
* List all provisioned applications:
```
cf apps
```
* View detailed information on a specific application, including state, CPU usage, memory:
```
cf app <APP_NAME>
```
* Get a dump of application logs in the Loggregator buffer:
```
cf logs <APP_NAME> --recent
```
* To obtain an active stream of the application logs:
```
cf logs <APP_NAME>
```
* View the files in an application directory:
```
cf files <APP_NAME>
```
* Users have the ability to navigate to a specific directory or view the contents of a file:
```
cf files <APP_NAME> path/to/file-to-view
```
* Show recent events for an application:
```
cf events <APP_NAME>
```
* Scale the number of appliation instances:
```
cf scale <APP_NAME> -i <NUMBER_OF_INSTANCES>
```
* Scale the memory reservation for an application, for example 128M, 1G. **Note**, scaling memory reservation will restart the application:
```
cf scale <APP_NAME> -m <DESIRED_MEMORY>
```
* View the current User, targeted Space and Org using `cf target`. Change the targeted Space or Org using the `-s` or `-o` options. For example, to change the targeted Space:
```
cf target -s <SPACE>
```

### cf CLI Tool Commands

The commands provided here can be displayed using `cf help` from the CLI. For detailed information on a specific command use `cf help <COMMAND>`.

```
NAME:
   cf - A command line tool to interact with Cloud Foundry

USAGE:
   [environment variables] cf [global options] command [arguments...] [command options]

VERSION:
   6.13.0-e68ce0f-2015-10-15T22:53:58+00:00

GETTING STARTED:
   help                                   Show help
   login                                  Log user in
   logout                                 Log user out
   passwd                                 Change user password
   target                                 Set or view the targeted org or space

   api                                    Set or view target api url
   auth                                   Authenticate user non-interactively

APPS:
   apps                                   List all apps in the target space
   app                                    Display health and status for app

   push                                   Push a new app or sync changes to an existing app
   scale                                  Change or view the instance count, disk space limit, and memory limit for an app
   delete                                 Delete an app
   rename                                 Rename an app

   start                                  Start an app
   stop                                   Stop an app
   restart                                Restart an app
   restage                                Restage an app
   restart-app-instance                   Terminate the running application Instance at the given index and instantiate a new instance of the application with the same index

   events                                 Show recent app events
   files                                  Print out a list of files in a directory or the contents of a specific file
   logs                                   Tail or show recent logs for an app

   env                                    Show all env variables for an app
   set-env                                Set an env variable for an app
   unset-env                              Remove an env variable

   stacks                                 List all stacks (a stack is a pre-built file system, including an operating system, that can run apps)
   stack                                  Show information for a stack (a stack is a pre-built file system, including an operating system, that can run apps)

   copy-source                            Make a copy of app source code from one application to another.  Unless overridden, the copy-source command will restart the application.

   create-app-manifest                    Create an app manifest for an app that has been pushed successfully.

   get-health-check                       get the health_check_type value of an app
   set-health-check                       set health_check_type flag to either 'port' or 'none'
   enable-ssh                             enable ssh for the application
   disable-ssh                            disable ssh for the application
   ssh-enabled                            Reports whether SSH is enabled on an application container instance
   ssh                                    SSH to an application container instance

SERVICES:
   marketplace                            List available offerings in the marketplace
   services                               List all service instances in the target space
   service                                Show service instance info

   create-service                         Create a service instance
   update-service                         Update a service instance
   delete-service                         Delete a service instance
   rename-service                         Rename a service instance

   create-service-key                     Create key for a service instance
   service-keys                           List keys for a service instance
   service-key                            Show service key info
   delete-service-key                     Delete a service key

   bind-service                           Bind a service instance to an app
   unbind-service                         Unbind a service instance from an app

   create-user-provided-service           Make a user-provided service instance available to cf apps
   update-user-provided-service           Update user-provided service instance name value pairs

ORGS:
   orgs                                   List all orgs
   org                                    Show org info

   create-org                             Create an org
   delete-org                             Delete an org
   rename-org                             Rename an org

SPACES:
   spaces                                 List all spaces in an org
   space                                  Show space info

   create-space                           Create a space
   delete-space                           Delete a space
   rename-space                           Rename a space

   allow-space-ssh                        Allow SSH access for the space
   disallow-space-ssh                     Disallow SSH access for the space
   space-ssh-allowed                      Reports whether SSH is allowed in a space

DOMAINS:
   domains                                List domains in the target org
   create-domain                          Create a domain in an org for later use
   delete-domain                          Delete a domain
   create-shared-domain                   Create a domain that can be used by all orgs (admin-only)
   delete-shared-domain                   Delete a shared domain

ROUTES:
   routes                                 List all routes in the current space or the current organization
   create-route                           Create a url route in a space for later use
   check-route                            Perform a simple check to determine whether a route currently exists or not.
   map-route                              Add a url route to an app
   unmap-route                            Remove a url route from an app
   delete-route                           Delete a route
   delete-orphaned-routes                 Delete all orphaned routes (e.g.: those that are not mapped to an app)

BUILDPACKS:
   buildpacks                             List all buildpacks
   create-buildpack                       Create a buildpack
   update-buildpack                       Update a buildpack
   rename-buildpack                       Rename a buildpack
   delete-buildpack                       Delete a buildpack

USER ADMIN:
   create-user                            Create a new user
   delete-user                            Delete a user

   org-users                              Show org users by role
   set-org-role                           Assign an org role to a user
   unset-org-role                         Remove an org role from a user

   space-users                            Show space users by role
   set-space-role                         Assign a space role to a user
   unset-space-role                       Remove a space role from a user

ORG ADMIN:
   quotas                                 List available usage quotas
   quota                                  Show quota info
   set-quota                              Assign a quota to an org

   create-quota                           Define a new resource quota
   delete-quota                           Delete a quota
   update-quota                           Update an existing resource quota

   share-private-domain                   Share a private domain with an org
   unshare-private-domain                 Unshare a private domain with an org

SPACE ADMIN:
   space-quotas                           List available space resource quotas
   space-quota                            Show space quota info
   create-space-quota                     Define a new space resource quota
   update-space-quota                     update an existing space quota
   delete-space-quota                     Delete a space quota definition and unassign the space quota from all spaces
   set-space-quota                        Assign a space quota definition to a space
   unset-space-quota                      Unassign a quota from a space

SERVICE ADMIN:
   service-auth-tokens                    List service auth tokens
   create-service-auth-token              Create a service auth token
   update-service-auth-token              Update a service auth token
   delete-service-auth-token              Delete a service auth token

   service-brokers                        List service brokers
   create-service-broker                  Create a service broker
   update-service-broker                  Update a service broker
   delete-service-broker                  Delete a service broker
   rename-service-broker                  Rename a service broker

   migrate-service-instances              Migrate service instances from one service plan to another
   purge-service-offering                 Recursively remove a service and child objects from Cloud Foundry database without making requests to a service broker

   service-access                         List service access settings
   enable-service-access                  Enable access to a service or service plan for one or all orgs
   disable-service-access                 Disable access to a service or service plan for one or all orgs

SECURITY GROUP:
   security-group                         Show a single security group
   security-groups                        List all security groups
   create-security-group                  Create a security group
   update-security-group                  Update a security group
   delete-security-group                  Deletes a security group
   bind-security-group                    Bind a security group to a space
   unbind-security-group                  Unbind a security group from a space

   bind-staging-security-group            Bind a security group to the list of security groups to be used for staging applications
   staging-security-groups                List security groups in the staging set for applications
   unbind-staging-security-group          Unbind a security group from the set of security groups for staging applications

   bind-running-security-group            Bind a security group to the list of security groups to be used for running applications
   running-security-groups                List security groups in the set of security groups for running applications
   unbind-running-security-group          Unbind a security group from the set of security groups for running applications

ENVIRONMENT VARIABLE GROUPS:
   running-environment-variable-group     Retrieve the contents of the running environment variable group
   staging-environment-variable-group     Retrieve the contents of the staging environment variable group
   set-staging-environment-variable-group Pass parameters as JSON to create a staging environment variable group
   set-running-environment-variable-group Pass parameters as JSON to create a running environment variable group

FEATURE FLAGS:
   feature-flags                          Retrieve list of feature flags with status of each flag-able feature
   feature-flag                           Retrieve an individual feature flag with status
   enable-feature-flag                    Enable the use of a feature so that users have access to and can use the feature.
   disable-feature-flag                   Disable the use of a feature so that users have access to and can use the feature.

ADVANCED:
   curl                                   Executes a raw request, content-type set to application/json by default
   config                                 write default values to the config
   oauth-token                            Retrieve and display the OAuth token for the current session
   ssh-code                               Get a one time password for ssh clients

ADD/REMOVE PLUGIN REPOSITORY:
   add-plugin-repo                        Add a new plugin repository
   remove-plugin-repo                     Remove a plugin repository
   list-plugin-repos                      list all the added plugin repository
   repo-plugins                           List all available plugins in all added repositories

ADD/REMOVE PLUGIN:
   plugins                                list all available plugin commands
   install-plugin                         Install the plugin defined in command argument
   uninstall-plugin                       Uninstall the plugin defined in command argument

INSTALLED PLUGIN COMMANDS:

ENVIRONMENT VARIABLES:
   CF_COLOR=false                     Do not colorize output
   CF_HOME=path/to/dir/               Override path to default config directory
   CF_PLUGIN_HOME=path/to/dir/        Override path to default plugin config directory
   CF_STAGING_TIMEOUT=15              Max wait time for buildpack staging, in minutes
   CF_STARTUP_TIMEOUT=5               Max wait time for app instance startup, in minutes
   CF_TRACE=true                      Print API request diagnostics to stdout
   CF_TRACE=path/to/trace.log         Append API request diagnostics to a log file
   HTTP_PROXY=proxy.example.com:8080  Enable HTTP proxying for API requests

GLOBAL OPTIONS:
   --version, -v                      Print the version
   --build, -b                        Print the version of Go the CLI was built against
   --help, -h                         Show help
```
