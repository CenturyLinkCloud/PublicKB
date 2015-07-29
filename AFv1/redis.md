{{{
  "title": "Services: Redis",
  "date": "1-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#redis-vcap">The VCAP_SERVICES Environment Variable</a></li>
<li><a href="#redis-ruby">Ruby</a></li>
<li><a href="#redis-sinatra-tutorial">Redis with Sinatra Tutorial</a></li>
</ul>
<h3 id="redis-vcap">The VCAP_SERVICES Environment Variable</h3>
<p>When you provision and bind a service to your app, AppFog creates an environment variable called <code>VCAP_SERVICES</code>. For apps that can't be automatically configured, you can find the information your app needs to connect to the database in this variable.</p>
<p>This variable contains a <code>JSON</code> document with a list of all credentials and connection information for the bound services.</p>
<p>Here's an example that of the environment variable for an app that has a Redis service bound to it:</p>
<pre>{"redis-2.2":[
    {
        "name":"redis-example",
        "label":"redis-2.2",
        "plan":"free",
        "tags":["redis","redis-2.2","key-value","nosql"],
        "credentials":{
            "hostname":"10.7.66.164",
            "host":"10.7.66.164",
            "port":5004,
            "password":"191dc43f-69a3-4d31-ac5e-4b66155b2e8e",
            "name":"9e3f3a9c-82ba-4c2e-bc83-b498e5447251"
        }
    }
]}
</pre>
<p>You can use your app's language-specific facility to call the environment variable.</p>
<p>In Java:</p>
<pre>java.lang.System.getenv("VCAP_SERVICES")
</pre>
<p>In Ruby:</p>
<pre>ENV['VCAP_SERVICES']
</pre>
<p>In Javascript:</p>
<pre>process.env.VCAP_SERVICES
</pre>
<p>In Python:</p>
<pre>os.getenv("VCAP_SERVICES")
</pre>
<p>In PHP:</p>
<pre>getenv("VCAP_SERVICES")
</pre>
<h3 id="redis-ruby">Ruby</h3>
<p>Connecting your Ruby app to a bound Redis service is simple:</p>
<pre>require "redis"

configure do
    services = JSON.parse(ENV['VCAP_SERVICES'])
    redis_key = services.keys.select { |svc| svc =~ /redis/i }.first
    redis = services[redis_key].first['credentials']
    redis_conf = {:host =&gt; redis['hostname'], :port =&gt; redis['port'], :password =&gt; redis['password']}
    @@redis = Redis.new redis_conf
end
</pre>
<p>The last line creates a class variable <code>@@redis</code>, available to all subclasses in your application, that will be used at runtime to add keys/values to Redis.</p>
<p>In your application use <a href="http://redis.io/commands">Redis commands</a> to edit and add key/values to the data store.</p>
<h3 id="redis-sinatra-tutorial">Redis with Sinatra Tutorial</h3>
<p>In this tutorial, we'll build a simple, <code>CRUD</code>-style note-taking app with Sinatra and we'll use Redis as the data store for the project.</p>
<h4>Setting up the Redis connection</h4>
<p>First, we'll create a <code>Gemfile</code>:</p>
<pre>source 'http://rubygems.org'

gem 'redis'
gem 'haml'
gem 'sinatra'
</pre>
<p>At the top of the <code>app.rb</code> file, we'll specify the dependencies:</p>
<pre>require 'rubygems'
require 'sinatra'
require 'redis'
require 'haml'
require 'json'
</pre>
<p>Next, we'll connect to the Redis service:</p>
<pre>configure do
    services = JSON.parse(ENV['VCAP_SERVICES'])
    redis_key = services.keys.select { |svc| svc =~ /redis/i }.first
    redis = services[redis_key].first['credentials']
    redis_conf = {:host =&gt; redis['hostname'], :port =&gt; redis['port'], :password =&gt; redis['password']}
    @@redis = Redis.new redis_conf
end
</pre>
<p>Interacting with the database involves simply running methods on this object.</p>
<h4>Getting started with routes and templates</h4>
<p>Now that we have a database connection established we can start. This will be a single-page app, so we'll keep our routes simple. Let's start with the basic get <code>'/'</code> route:</p>
<pre>get '/' do
  @title = "Sinatra + Redis + AppFog = WIN"
  @notes = @@redis.LRANGE("notes", 0, -1)
  haml :index
end
</pre>
<p>Here, we've specified the page title and created a <code>@notes</code> object that will store the notes we create. In order to do that, we need to query Redis. The <code>LRANGE</code> command in Redis gives back all of the values of the list (the <code>L</code> in <code>LRANGE</code> refers to "list") if you go from element <code>0</code> (the first element) to element <code>-1</code> (the last element). The list in question, <code>notes</code>, doesn’t exist yet. Querying Redis for it simply returns nothing, and our <code>@notes</code> variable will be empty at first. The <code>haml :index</code> command will specify which view needs to be rendered (index) and which templating engine we’ll be using (Haml).</p>
<p>Now, we'll start building our actual <code>views/index.haml</code> page. First, some boilerplate. <a href="http://haml.info/">Here</a> are Haml's docs, for reference.</p>
<pre>!!!
%html
  %head
    %title= @title
    %link{ :rel =&gt; "stylesheet", :type =&gt; "text/css", :href =&gt; "style.css" }
  %body
    %h1 Welcome to Redis on AppFog!
</pre>
<p>So now we have a basic stub of a site. With that in place, we'll set up a container for our notes and a generator for producing <code>DOM</code> elements for specific notes:</p>
<pre>#notes-container
  %h3 Notes:
  %ul
    - @notes.each do |note|
      %li
        %span #{note.to_s}
        %br
</pre>
<p>Under the "Notes" header, we've set up an unordered list (<code>%ul</code>) and below that we embed actual Ruby code into the view (with the hyphen). Remember that the <code>@notes</code> list is what houses the notes that we’ve entered into our Redis database. Here, I've created a simple Ruby block, whereby I take each member of the <code>@notes</code> list and create a list item (<code>%li</code>). Within each list item, there will be a <code>%span</code> that houses each specific note, followed by a line break (<code>%br</code>).</p>
<h4>The <code>@notes</code> list is sad and empty. Let's fix that.</h4>
<p>Right now, if we go to our main index page, we’ll see a couple headers and no notes. Next, we'll enable users to actually input notes of their own and store them in Redis. In our view, above the <code>#notes-container</code>, let's set up a form for inputting data:</p>
<pre>#mainForm
  %form{ :id =&gt; "newNote", :action =&gt; "/newNote", :method =&gt; "post" }
    %fieldset
      %label{ :for =&gt; "newNote" } Leave me a brief note!
      %br
      %input{ :type =&gt; "text", :name =&gt; "newNote" }
      %br
      %input{ :type =&gt; "submit", :value =&gt; "Submit" }
</pre>
<p>This form will provide a text field for entering text and a "Submit" button. Upon submission, it will <code>POST</code> the <code>/newNote</code> action. Let's set up our server to handle this request, below our initial get <code>'/'</code> route:</p>
<pre>post '/newNote' do
  if params[:newNote].length &gt;= 1
    @newNote = params[:newNote]
    @@redis.LPUSH("notes", @newNote)
  end

  redirect ‘/’
end
</pre>
<p>First, note that the <code>params[:newNote]</code> variable stores the text that has been submitted in the form. In order to push that information into our Redis store, we need to make sure that text has been entered, hence the <code>if params[:newNote].length &gt;= 1</code> condition. If text has been entered, then we'll store that in the <code>@newNote</code> variable.</p>
<p>Now comes the exciting part: making our first list push to Redis. We simply run the <code>LPUSH</code> command on the redis variable we created at the top, and push our <code>@newNote</code> to the notes list. Once that has been done, the server will reload the page, except that this time it will do so with a <code>@notes</code> list that has actual content.</p>
<h4>Spicing it up with list lengths, deletion, and timestamps</h4>
<p>Let's go a little further by allowing users to delete all of the notes that they've made thus far. We'll insert a "Delete all" button into our view:</p>
<pre>%form{ :id =&gt; "deleteNotes", :action =&gt; "/", :method =&gt; "post" }
  %input{ :type =&gt; "submit", :value =&gt; "Delete all" }
</pre>
<p>Now, let’s set up our server to handle this method in the <code>app.rb</code> file:</p>
<pre>post '/deleteNotes' do
  @@redis.FLUSHALL

  redirect '/'
end
</pre>
<p>The <code>FLUSHALL</code> command empties out the entire Redis store. This is a command that we'll use sparingly, of course, but in this case it works for our purposes.</p>
<p>Next, we'll add a timestamp to each note so we can remember when it was posted and to keep tabs on how many notes have been created.</p>
<p>In order to do that, we'll create a <code>before</code> block in the Sinatra server. This code will be called every time an <code>HTTP</code> request is made, no matter what that request is. We'll set up two new variables, <code>@length</code> for the length of the notes list, and <code>@time</code> for the current time:</p>
<pre>before do
  @length = @@redis.LLEN("notes")
  @time = Time.now.to_s
end
</pre>
<p>To get the length of our notes list, we'll ping Redis and use the <code>LLEN</code> (list length) command on our list. For the timestamp, there's no reason to use Redis over simply calling on the <code>Time.now</code> variable from the Ruby standard library, so we'll just use that and convert it to a string.</p>
<p>Now, let's change our <code>index.haml</code> file to actually present this information in the view. We'll create a sidebar on the right side of the page that keeps a tally of how many notes are in my list:</p>
<pre>#right-sidebar
  %h4 Total number of notes: #{@length}</pre>
