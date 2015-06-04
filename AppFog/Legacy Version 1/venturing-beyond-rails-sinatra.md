{{{
  "title": "Venturing beyond Rails: Sinatra",
  "date": "5-22-2013",
  "author": "Originally Posted On AppFog",
  "attachments": [],
  "contentIsHTML": false
}}}

**Starting Rails**

So far, it’s been a pretty uneven go. Multiple times a day I’ve experienced (a) “a-ha!” moments in which something has become clear to me in a flash and after which I could no longer imagine not knowing what I came to know, and (b) moments in which I’ve felt like the whole enterprise of learning programming is simply beyond my ken.

A few days ago, for example, I think I finally came to understand routing, which is notoriously tricky and, I can only presume, an initial stumbling block for many learning Rails. This demanded of me several hours of agony, a multitude of “ConnectionNotEstablished” messages in my browser, and a few not-so-small doses of my self-respect. But overcoming this hurdle made it feel like the heavens were once again opening up and like anything is possible.

My next step will be learning how to use Rails in conjunction with [databases](http://edgeguides.rubyonrails.org/active_record_migrations.html) to such an extent that I can begin actually doing more meaningful things with Rails. Linking and routing between pages that are essentially just HTML isn’t quite as exciting as it was on the first day. This already seems like orders of magnitude more difficult than routing, which is analogous to setting up a telephone operator. Connecting to a database already strikes me as a far more delicate matter, and probably far more tortuous in implementation. Wish me luck.

But in spite of really enjoying Rails so far—the aforementioned pesky roadblocks notwithstanding—I’m already confronting a temptation that I can only imagine is common to all developers: the temptation to explore or even (*gasp*) switch to other platforms without mastering the one you’re already working with. This is a temptation that has demanded a bit of self-reflection on my part.

**Enter Sinatra**

Last week, one of AppFog’s many ninjas-in-residence advised me to switch to [Sinatra](http://www.sinatrarb.com/) (another Ruby-based development platform) in response to a Twitter gripe of mine about my “Rails-related failure” (my words, not his!). Being the incorrigible completist and dabbler that I am, I immediately began checking out Sinatra.

The first thing that struck me about it is its simplicity. An über-simple Sinatra app could consist of one Ruby file, including views. All you have to do is type in an ominous __END__ once your routes and models are in place and begin doing layouts, be they in [haml](http://haml.info/) or [erb](http://guides.rubyonrails.org/layouts_and_rendering.html) or what-have-you. Here’s an example a simple but functional Sinatra app, consisting of the single Ruby file <code>app.rb</code>:

<pre><code>
require 'rubygems'
require 'sinatra'
require 'haml'

get '/' do
  @title = "Main Page"
  haml :index
end

__END__

@@index
!!!
%html
  %head
    %title= @title
  %body
    %h1
      Welcome to the Main Page!
</code></pre>

Go to the terminal, open up the directory in which <code>app.rb</code> is housed, and type ruby app.rb. This will get the app up and running on your local host (port 4567 is the default), and you’ll see the basic rendered index HTML file shown directly above. Now, this app isn’t exactly going to set the world on fire. But it serves to make one thing immediately clear: making a Rails app with this little functionality would necessarily involve a whole host of files and folders. 18 lines of code in one Ruby file? Forget it.

Rails is designed to allow you to hit the ground running, and it accomplishes that with aplomb (once some initial hurdles are cleared). But Sinatra has you hitting the ground practically blazing.

At the moment, I’m not sure how scalable Sinatra ultimately is, and time will tell where I ultimately stand on that. There are already a variety of deeply [divergent opinions](http://stackoverflow.com/questions/3594681/rails-3-vs-sinatra) circulating out there, and I’m curious to see how the framework develops over time. But if you’re a Rubyist and wary of this or that element of Rails (such as the opinionated [MVC](http://www.tutorialspoint.com/ruby-on-rails/rails-framework.htm) architecture specific to it) or if you have a simple project that doesn’t require loads of complex functionality, then give Sinatra a shot. Check it out on [pluralsight](http://www.pluralsight.com/courses/meet-sinatra) or via a free tutorial like [this one](http://code.tutsplus.com/tutorials/an-introduction-to-haml-and-sinatra--net-14858).

My more general advice to up-and-coming developers is to do one of two things when faced with the temptation to stray from the framework you’re learning. The preferred option is make a list of things to explore at a future date when things “slow down” or you have some “free time” (whenever that is or whatever that even means). The second–and highly deprecated–option is to spend just enough time exploring something to satiate your curiosity, and then ditch it immediately.

If people you trust and respect are telling you to try something out, don’t shut out their influence. But so far, all signs nonetheless point to one conclusion: consistently giving in to the temptation to dabble will mean that you could end up spinning your wheels in perpetuity and never reaching true mastery of much of anything. This is the fate of the dilettante, and it is a well-trodden one…
