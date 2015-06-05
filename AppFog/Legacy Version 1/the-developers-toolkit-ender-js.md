{{{
  "title": "The developer’s toolkit: Ender.js",
  "date": "1-19-2015",
  "author": "Originally Posted On AppFog",
  "attachments": [],
  "contentIsHTML": false
}}}

You guys know me. You know that I talk a lot of things up in this space. I can’t help it. I’m a generally excitable person. But one thing I have never said is that I’m completely blown away by something. Well, now is that time. I am completely blown away by Ender.

###What problem does Ender solve?

I’ll start with a common problem and explain the advantage of Ender that way. A project I’m working on now has the following at the bottom of the index.html file:

<pre><code>

<script src="http://ajax.cdnjs.com/ajax/libs/json2/20110223/json2.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
<script src="http://ajax.cdnjs.com/ajax/libs/underscore.js/1.1.4/underscore-min.js"></script>
<script src="http://ajax.cdnjs.com/ajax/libs/backbone.js/0.3.3/backbone-min.js"></script>
<script src="http://ajax.microsoft.com/ajax/jquery.templates/beta1/jquery.tmpl.js"></script>
<script src=”http://cdnjs.cloudflare.com/ajax/libs/raphael/2.0.1/raphael-min.js”></script>

</code></pre>

This should look familiar to, well, all of you. Many of you have probably seen much worse. Whenever I’ve been confronted by things like this, I’ve always had an inkling that there had to be a Better Way That Just Works, and as far as I can tell, Ender has come along and provided that hotly sought-after Better Way.

###So what is this Ender thing anyway?

Ender is essentially a JavaScript build tool rooted in the command line. It enables you to compile a variety of JavaScript libraries into a single JS library labeled “ender.js.” That way, instead of having to insert a pile of script src tags into your HTML, you can get the job done with just one:

<pre><code> <script src=”ender.js”></script></code></pre>

BOOM. Done. And if you need a minified version, this is done automatically and put in the file <code>ender.min.js</code> in the same directory.

###Cool! How do I use it?

Well, fortunately it’s about as simple a CLI tool as you’ll find out there. You install it via NPM–which has to be one of the best package managers on the planet–with a simple <code>sudo npm install -g ender</code> and then the whole experience is pretty seamless.

If I wanted to combine the above JS libraries–Backbone, JSON2, Underscore, jQuery, jQuery.tmpl, and Raphael–I could start with any one of them (I’ll start with Backbone) and run the following command in my target directory:

<pre><code>$ ender build backbone</code></pre>

From there, I would progressively add the others. One downside thus far is that Ender doesn’t seem to like it when you add multiple libraries in a single command. Instead, you need to add them one by one, like so:

<pre><code>$ ender add json2
$ ender add underscore
</code></pre>

But wait! Ender doesn’t need to go and fetch Underscore because it knows that Underscore is a dependency of Backbone. And so when I added Backbone to my ender.js file, it added Underscore for me. And jQuery comes built into your initial ender.js file by default, so you don’t have to worry about that one either. That leaves just Raphael and jQuery.tmpl to install, which can be done just like all the others.

So what if you have your own native JavaScript that you’d like to weave into the library? With Ender, you can also add file paths.

<pre><code>$ ender add ./my_js_library.js</code></pre>

And if you decide later on that there’s a library you don’t need, that’s easy as well. If I no longer need to make my page look super sleek and thus no longer need Raphael.js, I can run a simple remove command:

<pre><code>$ ender remove raphael</code></pre>

At the moment, not all commonly used JavaScript libraries are available on Ender. But I imagine that that will change once people realize how useful it is. Fortunately, publishing new ones is easy. If you want your own JavaScript libraries (or someone else’s for that matter) to be published to Ender and hence accessible via ender build, ender add, and other commands, it’s as simple as publishing to Node Package Manager. You just need to modify the package.json file in your package root folder to include

<pre><code>“ender”: “./src/exports/ender.js”</code></pre>

Then, follow the normal NPM publishing route and ender add <new_js_library> will work for everyone else.

This strikes me as being a huge win for developers, and I firmly hope that build tools like this will eventually be deemed best practice in the JavaScript universe.

Other useful aspects of Ender include the ender info command, which gives you an actual dependency tree of the ender.js file that you have constructed up to that point, much like the tree command found in some *nix environments. There’s a lot more where that came from, and I suggest checking out the docs to have a more comprehensive look at what Ender has on offer.

###This sounds too good to be true…

Now, Ender surely isn’t flawless. I’m sure that there are plenty of namespace issues that emerge when different libraries use the same function and/or variable names. This is something that should be very much on your radar when using Ender, and you should never assume that throwing together any set of libraries haphazardly will always work out unproblematically.

You also need to be aware that using Ender means changing the way you code in JavaScript, much like jQuery did several years ago. For a solid video tutorial for beginners, I suggest [this video](https://vimeo.com/23836209).

But this is not a problem unique to Ender. It’s a problem you always had before. The difference is that now you have a mature JavaScript build tool that will help you eliminate the <code><src script=”mylib.js”></src></code> spaghetti at the bottom of your page and generally tidy up the entirety of your JavaScript coding experience.

Give it a shot, JS fanatics! You have nothing to lose but your separate, non-joined JS libraries!
