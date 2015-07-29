{{{
  "title": "Application Specific: Is it possible with increase the max_execution_time for PHP scripts?",
  "date": "1-27-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>While you cannot use a custom php.ini there are some other things you can try.</p>
<p>Using set_time_limit function will allow you to extend the execution time limit.</p>
<p><a href="http://www.php.net/manual/en/function.set-time-limit.php">http://www.php.net/manual/en/function.set-time-limit.php</a></p>
<p>You can use ini_set as well to change the max_execution_time at the beginning of the script.</p>
<p><a href="http://php.net/manual/en/function.ini-set.php">http://php.net/manual/en/function.ini-set.php</a></p>
<p>The runtime configuration applied for php apps on AppFog is available here.</p>
<ul>
<li><a href="http://php_info.aws.af.cm">PHP 5.3</a></li>
<li><a href="http://php_info54.aws.af.cm/">PHP 5.4</a></li>
<li><a href="http://php_info55.aws.af.cm/">PHP 5.5</a></li>
<li><a href="http://php_info56.aws.af.cm/">PHP 5.6</a></li>
</ul>
