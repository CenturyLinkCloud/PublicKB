{{{
  "title": "Application Specific: Why does my app return a 510 In Progress error?",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>In an effort to provide the best service possible, AppFog implements a feature that we refer to as "spindown". Inactive free applications may be suspended as determined by our administrator. This lets us conserve memory so we can continue to offer great service to the apps that need it. Your app will be started back up in the background when it receives a new request, and will return a 510 error until it's fully started.</p>
<p>Alternatively, apps on a <a href="https://www.appfog.com/pricing/">paid account</a> will not be spun down.</p>
