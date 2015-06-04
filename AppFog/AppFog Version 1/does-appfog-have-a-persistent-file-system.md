{{{
  "title": "Platform Specific: Does AppFog have a persistent file system?",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Not yet. We're working on this feature, but in the meantime, the file system is volatile. This means that any changes you make to the file system through a web interface, including any admin changes and content uploads, will be lost on the app's next start, stop, restart, deploy, or resource change. Because of this, you should make any changes to the file system on a local development environment and keep media assets and content uploads on an external storage system.</p>
