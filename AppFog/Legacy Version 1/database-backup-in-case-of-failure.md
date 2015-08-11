{{{
  "title": "Application Specific: How do make sure I have backups of my AppFog hosted database in case of failure?",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>You can create a cron job on your local machine that will run the `af export-service` command to make a backup of your service hosted on AppFog. The command provides a link that can be pulled down with wget or curl to your local machine.</p>
