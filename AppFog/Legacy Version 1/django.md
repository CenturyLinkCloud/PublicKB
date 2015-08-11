{{{
  "title": "Languages And Frameworks: Django",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog supports Django versions 1.3 and 1.4. To ensure your applicaiton is deployed using version 1.4 you will want to specify it within your requirements.txt file. If not specified it will default to version 1.3.</p>
<p>When you run the <code>af update</code> command on a Django app, AppFog automatically runs the <code>syncdb</code> command against the bound database for you as part of the staging process.</p>
<p>More coming soon. Meanwhile, check out <a href="https://github.com/appfog/af-python-django">the GitHub repo for our Python Django Jumpstart</a>.</p>
