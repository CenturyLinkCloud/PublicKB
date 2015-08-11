{{{
  "title": "Application Specific: I am having trouble updating my application",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>When using <code>af update</code> AppFog compares the existing app with the content you're uploading and makes the changes. When the app is large or has a large number of files users may experience 500 errors as the comparison takes too long. </p>
<h3>Using --trace</h3>
<p>This flag will provide verbose output and may help provide more information as to the cause of the error.</p>
<h3>Using --no-resources</h3>
<p>You can use the <code>--no-resources</code> flag with your update command. This flag skips the resource cache step when updating the application. In turn, it forces an upload of only updated files from your local directory to AppFog.</p>
<h3>Updating in Stages</h3>
<p>The current platform has an upload limitation around 100MB. The workaround is to update an app in stages.</p>
<p>Let's say you split your app up into four chunks (the amount, of course, will depend on the size of your app). In this example, we'll refer to them as A, B, C and D. Using four separate updates, we will "build" the app code onto AppFog.</p>
<p>First you will break up your code into four separate sub-directories in your app's directory on your local computer, (for example, &lt;appname_code&gt;/code_pieces/code_A/)<br />Then in your CLI, do four separate updates, changing the directory for each of the updates, like this:</p>
<pre><code>$ pwd
~/appname_code
$ cp ../code_pieces/code_A/* .
$ af update myapp --no-start
</code></pre>
<p>&lt;code_A is uploaded to AppFog&gt;</p>
<pre><code>$ cp ../code_pieces/code_B/* .
$ af update myapp --no-start
</code></pre>
<p>&lt;code_A code is matched and ignored&gt;<br />&lt;code_B is uploaded to AppFog&gt;</p>
<pre><code>$ cp ../code_pieces/code_C/* .
$ af update myapp --no-start
</code></pre>
<p>&lt;code_A code is matched and ignored&gt;<br />&lt;code_B code is matched and ignored&gt;<br />&lt;code_C is uploaded to AppFog&gt;</p>
<pre><code>$cp ../code_pieces/code_D/* .
$af update myapp
</code></pre>
<p>&lt;code_A, code_B, and code_C code is matched and ignored&gt;<br />&lt;code_D is uploaded to AppFog, app attempts to start&gt;</p>
