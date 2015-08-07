{{{
  "title": "Customize: Custom Error Pages",
  "date": "1-28-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h2 id="debugging">Custom Error Pages</h2>
<p>The Custom Error Page feature enables an application or service to return a user-defined error page that matches the look and feel of your application, web site or service when a system-level error occurs.</p>
<p>There are two types of errors that can be returned to service requests:</p>
<p>1. Application-related errors: E.g. "404 page not found"</p>
<p>2. System-related errors: E.g. "503 service unavailable" or "502 service temporary overloaded"</p>
<p>For application-related errors, your application or service is responsible for handling and returning the error response, such as a "404 page not found" message. </p>
<p>If your app encounters a system-level error, the AppFog platform returns a default error page . You can create a custom error page for your applications to provide a more consistent user experience.</p>
<h2 id="debugging">Creating a Custom Error Page</h2>
<p>To replace AppFog's default error page with a customized version, <a href="https://console.appfog.com/login">login to the Web Console</a> and open the Mission Control page for your application. Choose the "Custom Error Page" option from the left nav menu to edit your page. You have two options:</p>
<ul>
<li>Edit the default error page HTML directly</li>
<li>Use the Custom Error Page Generator below to update the HTML</li>
</ul>
<p>Either way, once you've finished making your changes, click the "Apply Updates" button and then preview the changes by clicking the preview link above the text box.</p>
<p>Note: The error page HTML uses the AppFog CSS. You can reference a different CSS and/or images by using absolute paths in your HTML (e.g., <code>&lt;img src="https://s3.amazonaws.com/error-page-assets/icon-warning.png"&gt;</code>) and uploading the CSS and/or assets to the location you specify. To confirm the error page renders correctly, use the preview option above the HTML text box.</p>
<p>You can host the pages anywhere that can serve web pages; we recommend uploading to Amazon S3. If you use S3, don’t forget to set the HTML and all assets to be publicly readable.</p>
<h3 id="testing">Testing</h3>
<p>To test your custom error page, stop your application, and then open the URL for your app. The custom error page will be displayed in your browser.</p>
