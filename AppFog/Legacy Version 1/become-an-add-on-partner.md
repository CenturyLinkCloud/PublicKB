{{{
  "title": "Add-ons: Become an Add-on Partner",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog provides your app with extra functionality by partnering with various third-party services. You can add everything from logs to databases to powerful metrics to your app with a single click .</p>
<h3>How Add-ons Work</h3>
<p>Our add-on partners can create provisioning services that are compatible with AppFog.</p>
<ul>
<li><a href="#provision">Provisioning Workflow</a></li>
<li><a href="#callback">API Callback Spec</a></li>
<li><a href="#api">API Spec</a></li>
<li><a href="#authentication">Authentication</a></li>
<li><a href="#manifest">Manifest Format</a></li>
<li><a href="#regions">Regions</a></li>
<li><a href="#sso">Single Sign-on</a></li>
</ul>
<h3 id="provision">Provisioning Workflow</h3>
<ol>
<li>The user installs the add-on from the AppFog app console. This sends a request to the add-on partner to provision the service.</li>
<li>AppFog makes a <code>POST</code> request to <a href="https://partner.com/appfog/resources">https://partner.com/appfog/resources</a>. It passes in the <code>customer_id</code> (email address), plan, and the <code>callback_url</code>.</li>
<li>The partner returns the local ID of the newly created resource. If it's able to provision the resource synchronously, the config parameter can be set. It may not be possible to provision the resource synchronously, so the config can be empty.</li>
<li>If the config is empty, the user sees a message stating that the resource is waiting to be provisioned.</li>
<li>Once the resource is provisioned, the partner makes a call to the callback URL, as specified in the initial provisioning call, and passes the new config parameters to be set.</li>
<li>Once the config parameters are set, they are set as environment variables in the user's app and instructions are displayed to the user on how to perform the integration.</li>
</ol>

<h3 id="callback">API Callback Spec</h3>
<p>This is a method implemented by the AppFog services. It is used to update the configuration values for a given resource as provided by the add-on partner. The configuration parameters can be specified by the partner when the provisioning call is made by AppFog; however, if the call takes a while to process the partner can use this method to update those parameters later.</p>
<p>PUT to path as defined in <code>callback_url</code> on provisioning call.</p>
<p>Request Body:</p>
<pre>{
    "config":{"VAR_XYZ":"http://partner.com/5678ADFD"}
}</pre>
<p>Response:</p>
<pre>200 OK</pre>
<h3 id="api">API Spec</h3>
<h4>Example Provisioning Request</h4>
<p>Request: <code>POST /phpfog/resources</code></p>
<p>Request Body:</p>
<pre>{
    "customer_id":"user@email.com",
    "plan":"free",
    "callback_url":"https://path_to_resource",
    "options":{}
}</pre>
<p>Response Body:</p>
<pre>{
    "id":789,
    "config":{"ADDONNAME_VAR1":"some configuration value"},
    "message":""
}</pre>
<h4>Request Fields</h4>
<ul>
<li><code>customer_id</code> - The identification of the user in the AppFog system (i.e. email address).</li>
<li><code>plan</code> - The plan being provisioned. This will be "free" for the moment; however, in the future this can be higher-tier plans once they're supported.</li>
<li><code>callback_url</code> - This is the address of the resource in AppFog's system. The provider can use this to update the configuration for this resource (e.g. during provisioning).</li>
<li><code>options</code> - This contains additional options for the specific service. It's a placeholder for now and AppFog will not send these requests yet.</li>
</ul>
<h4>Response Fields</h4>
<ul>
<li><code>id</code> - This is the ID of the resource in the provider's system.</li>
<li><code>config</code> - The required key/value pairs of parameters required to provision the service. The manifest specifies what keys are allowed. Configuration paramters are required, but the particular configuration parameters up to the provider. They can also be updated later using the <code>callback_url</code> to update the config.</li>
<li><code>message</code> - This is a message to the system. It's ignored for now.</li>
</ul>
<h4>Example Deprovisioning Request</h4>
<p>Request: <code>DELETE /phpfog/resources/:id</code></p>
<p>Request Body: none</p>
<p>Response:</p>
<pre>200 OK</pre>
<h4>Request Fields</h4>
<p>This is a DELETE request to the particular <code>URL</code> and doesn't contain a body.</p>
<h4>Response Fields</h4>
<p>Only an HTTP response status is required.</p>
<h3 id="authentication">Authentication</h3>
<p>All calls to both the provisioning API on the partners service as well as the AppFog callback service must be authenticated using <code>HTTP Basic Auth</code>.</p>
<p>All requests must be completed over <code>HTTPS</code>.</p>
<p>The manifest file specifies the username and password to be used for all of these calls. The "<code>id</code>" in the manifest is the username, the "<code>api_password</code>" is the password.</p>
<h3 id="manifest">Manifest Format</h3>
<p>The manifest file is a <code>JSON</code> document that defines the information necessary for AppFog to make provisioning calls to the provider.</p>
<p>Add-on partners should provide the manifest file out-of-band by emailing it to the AppFog team to incorporate into the system.</p>
<h4>Example Manifest</h4>
<p><code>example-manifest.json</code></p>
<pre>{
    "id": "company",
    "name": "Product",
    "plans": [
        {
            "id": "free"
        }
    ],
    "api": {
        "config_vars": [
            "PRODUCT_URI"
        ],
        "password": "SDasdf98asdf68ZoRak5Tl",
        "sso_salt": "DfauasdfDF0s0afsadf0",
        "production": {
            "base_url": "https://api.company.com/partners/af/resources",
            "sso_url": "https://www.company.com/login/partners/af"
        },
        "test": {
            "base_url": "https://localhost:8081/partners/af/resources",
            "sso_url": "https://localhost:8081/login/partners/af"
        }
    }
}</pre>
<h4>Fields</h4>
<ul>
<li><code>id</code> - The add-on id. All lowercase, no spaces or punctuation. This is used in conjunction with the password to authenticate provisioning calls.</li>
<li><code>name</code> - The friendly name to appear in the add-on tab of the app console in AppFog.</li>
<li><code>api/config_vars</code> - A list of variables to be returned on provisioning calls. The variable names must be prefixed with the add-on id and an underscore. Example: "<code>PROVIDER_</code>"</li>
<li><code>api/production</code> - The root <code>URL</code> of the provisioning service of provider.</li>
<li><code>api/test</code> - Same <code>URL</code> as production, but for testing in a QA environment.</li>
<li><code>api/path</code> - (Optional) Overrides the default path "<code>appfog/resources</code>".</li>
<li><code>api/username</code> - (Optional) The username used by AppFog to authenticate itself with the partner service via <code>HTTP Basic Auth</code>. The "<code>id</code>" is used if the username is not specified.</li>
<li><code>api/password</code> - The password used by AppFog to authenticate itself with the partner service via <code>HTTP Basic Auth</code>.</li>
<li><code>api/sso_salt</code> - Shared secret used in single sign-on between AppFog and the provider.</li>
<li><code>plans/id</code> - The name of the "free" plan that will be offered to AppFog users and used for testing and integration purposes.</li>
</ul>
<h3 id="regions">Regions</h3>
<p>AppFog supports running apps in regions other than AWS US-East.</p>
<p>To let you know where the app provisioning an add-on is located, we've extended the provisioning API to provide a <code>region</code> parameter in the provision request.</p>
<p>It's up to you, the add-on provider, to take advantage of region information in the provision request. You can do one of three things with the parameter:</p>
<ol>
<li>Ignore the parameter and provision your add-on normally.</li>
<li>Read the parameter, accept the request and provision your add-on normally.</li>
<li>Read the parameter and reject the request, returning a <code>422</code> error with a message explaining the reason for the rejection.</li>
</ol>
<p>If your add-on isn't latency-sensitive (e.g. email, etc.), it's probably safe to ignore it. If your add-on is latency sensitive and you're currently running your service in, for example, AWS EU-West, you should provision services only for apps specifying that region.</p>
<p>If you're not running infrastructure in the same infrastructure as the app and you don't think your add-on is usable across data centers (or maybe you don't want to incur ingress/outgress bandwidth charges), you can respond with <code>HTTP 422</code> and a message in the response body, something like this:</p>
<pre>{ "message": "eu-west not supported, sorry" }</pre>
<p>Here's a list of the current possible parameter values:</p>
<ul>
<li><code>'amazon-web-services::us-east-1'</code></li>
<li><code>'amazon-web-services::ap-southeast-1'</code></li>
<li><code>'amazon-web-services::eu-west-1'</code></li>
</ul>
<h3 id="sso">Single Sign-on</h3>
<p>Once a resource is fully provisioned, a "Manage" button will appear in the AppFog app console for the given add-on. This button will redirect the user to the management page of the particular resource on the partner's website.</p>
<p>After the user clicks the button, they will be redirected to the following generated <code>URL</code>:</p>
<pre>https://partner.com/appfog/resources/:id?token=:token&amp;timestamp=:timestamp</pre>
<p>The <code>:id</code> is the <code>id</code> of the resource which was defined in the response to the provisioning call for creating this resource.</p>
<p>The token is defined as a combination of the <code>id</code>, <code>salt</code>, and <code>timestamp</code>.</p>
<p>The salt is the "<code>sso_salt</code>" variable as defined in the manifest.</p>
<p>The timestamp is the current UNIX timestamp.</p>
<pre>token = sha1(id + ':' + salt + ':' + timestamp)</pre>
<p>After the partner validates the salt (shared secret) and the timestamp (we recommend 30 seconds), they can be allowed to manage the resource as defined by the <code>id</code>.</p>
