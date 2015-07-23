{{{
  "title": "Languages And Frameworks: Sinatra",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog currently only offers one app server for Sinatra apps: Thin. If you're using Bundler, and nothing in your app's bundle requires Thin, VCAP cannot safely start your app using it.</p>
<p>To use AppFog services with Sinatra, you have to access the <code>VCAP_SERVICES</code> environment variable.</p>
<p>AppFog autodetects your Sinatra app by searching for <code>require 'sinatra'</code> in the <code>*.rb</code> files. It then chooses that file as the main Sinatra app file.</p>
<p>If you use Bundler to load Sinatra, AppFog may not recognize your app. In this case, you can simply manually tell AppFog that it's a Sinatra app when you push your code:</p>
<pre>$ af push
Would you like to deploy from the current directory? [Yn]:
Application Name: sinatra-example
Detected a Standalone Application, is this correct? [Yn]: n
1: Rails
2: Spring
3: Grails
4: Lift
5: JavaWeb
6: Standalone
7: Sinatra
8: Node
9: PHP
10: Erlang/OTP Rebar
11: WSGI
12: Django
13: Rack
Select Application Type: 7
Selected Sinatra Application
...
</pre>
<p><!--- You can put a comment in your app’s main file like this:</p>

<pre># require 'sinatra'   # required for framework detection in AppFog...
require 'rubygems'
require 'bundler'
Bundler.require
...
</pre>

<p>---></p>
<h3>Sample Sinatra App Using DataMapper and Bundler</h3>
<h4>Gemfile</h4>
<pre>source 'http://rubygems.org'

gem 'sinatra'
gem 'data_mapper'

group :development do
    gem 'dm-sqlite-adapter'
end

group :production do
    gem 'dm-mysql-adapter'
end
</pre>
<h4><code>sinatra_dm.rb</code></h4>
<p>The name of this sinatra app will be <code>sinatra_dm.rb</code>.</p>
<p><!--- Note the commented out require of sinatra, which is necessary for proper detection of the app’s main file. ---></p>
<p><!---    # require 'sinatra'   # required for framework detection in AppFog. ---></p>
<pre># Sample Sinatra app with DataMapper
# Based on http://sinatra-book.gittr.com/ DataMapper example
require 'rubygems'
require 'bundler'
Bundler.require

if ENV['VCAP_SERVICES'].nil?
    DataMapper::setup(:default, "sqlite3://#{Dir.pwd}/blog.db")
else
    require 'json'
    svcs = JSON.parse ENV['VCAP_SERVICES']
    mysql = svcs.detect { |k,v| k =~ /^mysql/ }.last.first
    creds = mysql['credentials']
    user, pass, host, name = %w(user password host name).map { |key| creds[key] }
    DataMapper.setup(:default, "mysql://#{user}:#{pass}@#{host}/#{name}")
end

class Post
    include DataMapper::Resource
    property :id, Serial
    property :title, String
    property :body, Text
    property :created_at, DateTime
end

DataMapper.finalize
Post.auto_upgrade!

get '/' do
    @posts = Post.all(:order =&gt; [:id.desc], :limit =&gt; 20)
    erb :index
end

get '/post/new' do
    erb :new
end

get '/post/:id' do
    @post = Post.get(params[:id])
    erb :post
end

post '/post/create' do
    post = Post.new(:title =&gt; params[:title], :body =&gt; params[:body])
    if post.save
        status 201
        redirect "/post/#{post.id}"
    else
        status 412
        redirect '/'
    end
end
</pre>
<h3>Views</h3>
<h4>Index</h4>
<pre>&lt;!-- views/index.erb --&gt;

&lt;h1&gt;All Blog Posts&lt;/h1&gt;
&lt;ul&gt;
    &lt;% @posts.each do |post| %&gt;
        &lt;li&gt;&lt;a href="/post/&lt;%= post.id %&gt;"&gt;&lt;%= post.title %&gt;&lt;/a&gt;&lt;/li&gt;
    &lt;% end %&gt;
&lt;/ul&gt;
&lt;br /&gt;
&lt;a href="/post/new"&gt;Create new post&lt;/a&gt;
</pre>
<h4>New</h4>
<pre>&lt;!-- views/new.erb --&gt;

&lt;h1&gt;Create a new blog post&lt;/h1&gt;
&lt;form action="/post/create" method="POST"&gt;
    &lt;p&gt;Title: &lt;input type="text" name="title"&gt;&lt;/input&gt;&lt;/p&gt;
    &lt;p&gt;Text: &lt;textarea name="body" rows="10" cols="40"&gt;&lt;/textarea&gt;&lt;/p&gt;
    &lt;input type="submit" name="Publish" /&gt;
&lt;/form&gt;
</pre>
<h4>Post</h4>
<pre>&lt;!-- views/post.erb --&gt;

&lt;h1&gt;&lt;%= @post.title %&gt;&lt;/h1&gt;
&lt;p&gt;&lt;%= @post.body %&gt;&lt;/p&gt;
&lt;a href="/"&gt;All Posts&lt;/a&gt;
</pre>
<h4>Test Locally</h4>
<pre>$ ruby sinatra_dm.rb
</pre>
<p>Then visit <a href="http://localhost:4567/">http://localhost:4567/</a> in your browser.</p>
<h4>Bundle and Push</h4>
<pre>$ bundle install; bundle package
$ af push
</pre>
