{{{
  "title": "The developer’s toolkit: raphael.js",
  "date": "5-22-2013",
  "author": "Originally Posted On AppFog",
  "attachments": [],
  "contentIsHTML": false
}}}

JavaScript occasionally gets a bad rap as a programming language, but its usefulness if not indispensability for web developers of all stripes is difficult to deny. Yet another case in point: [raphael.js](http://raphaeljs.com/). This is a tool that lets you not only paint with JavaScript, but also to make interactive objects like [this](http://raphaeljs.com/curver.html).

Now, [raphael.js](http://raphaeljs.com/) seems like something that many of us could live without. But it also strikes me as perfect if you’re working on a project that needs just a tiny bit of extra aesthetic pizzazz beyond what’s available in CSS, jQuery,et al. Even better, it’s an absolute breeze if you feel even remotely comfortable in JavaScript. To give one very basic example: you can use just one instance of JavaScript’s “for” function (typically used for iteration) to produce 30 circles with circumferences varying according to an equation (for example, making concentric circles separated by 5 pixels). The following code will get you 30 such circles emanating out from the center of a 500×500 pixel canvas:

<pre><code>
for ( i = 0; i < 30; i++) {
var x = 0;
var circle = ( 250, 250, 0+5x );
};
</code></pre>

That’s it. Four lines. But this tool isn’t just about pizzazz. Things like [this](http://raphaeljs.com/pie.html) strike me as downright useful. And there are plenty of tutorials like [this one](http://www.cre8ivecommando.com/a-simple-way-to-draw-vector-graphics-on-the-web-raphael-js-16872/) to help ease you into using it and expand your capabilities.

Though I haven’t yet delved too deeply into JavaScript’s many uses (as I’ve been focusing on Ruby), I’ve been impressed by its versatility. In the coming weeks, I’ll be talking about other .js libraries as I discover them. Recommendations welcome!
