{{{
  "title": "Getting Started With AppFog v1: Environment Variables",
  "date": "1-25-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog provides for easy implementation and use of environment variables either using the web console or the CLI. If you haven't already installed it, here is the <a href="appfog-cli-tool-manual.md">AppFog CLI Tool Manual</a>.</p>
<h3>Web Console</h3>
<p>Simply navigate to the application's <strong>Mission Control</strong> page and select the <strong>Env Variables</strong> button on the left. Once entered select the <strong>Update</strong> button to provision the variable.</p>
<p> </p>
<h3>CLI</h3>
<p>Here are the commands to use in the <a href="appfog-cli-tool-manual.md">CLI</a>.</p>
<table>
<tbody>
<tr>
<td>env &lt;appname&gt;</td>
<td>List application environment variables</td>
</tr>
<tr>
<td>env-add &lt;appname&gt; &lt;variable[=]value&gt;</td>
<td>Add an environment variable to an app</td>
</tr>
<tr>
<td>env-del &lt;appname&gt; &lt;variable&gt;</td>
<td>Delete an environment variable to an app</td>
</tr>
</tbody>
</table>
<p> </p>
<h3>Note</h3>
<p>An existing variable value can be changed in the web console; however, in CLI they have to be deleted and readded to change the value. For example:</p>
<pre>af env-add TEST=first</pre>
<p>Followed by</p>
<pre>af env-add TEST=second</pre>
<p>Does not change the value of $TEST to second but results in:</p>
<pre>+----------+--------+
| Variable | Value  |
+----------+--------+
| TEST     | first  |
| TEST     | second |
+----------+--------+
</pre>
