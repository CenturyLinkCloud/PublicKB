{{{
  "title": "Overview Test Article",
  "date": "01-13-2015",
  "author": "Kevin Bleich",
  "attachments": [],
  "related-products" : [],
  "preview" : "",
  "overview": "CenturyLink Cloud accounts start with a pre-defined resource (CPU/memory/storage) limit per data center. As customers grow their cloud usage, it's common to request an increase in resource limits.   Note that only paying customers will have their resource limits increased unless executive approval is given.",
  "contentIsHTML": false
}}}

### Detailed Steps
    
1.  Error Message

    You get an error in the upper right hand corner of Control indicating lack of resources (CPU, Memory, Storage) when you are building a new machine. 

2.  Contact Support
  
    Please contact support on Chat or by emailing noc@email.com

    __To open a Chat with an engineer:__

    1.  Log into control

    2.  Go to menu and select __Info__

    3.  At the bottom of the page, click __Support Chat__

3.  Please let them know that you have reached your resource limitations.

4.  The engineer will validate your identity and then increase your limit.

5.  After the resources on your account have increased.

    __In Control:__

    1.  Go to __Servers__

    2.  Select the proper Data-Center that you need the additional resources

    3.  Select __Settings__

    4.  Scroll down to __Resource Limits__

    5.  Increase the limit of the specific Resource

``` markdown
| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```
``` xml
<div class="highlight"><pre><span class="nx">grunt</span><span class="p">.</span><span class="nx">initConfig</span><span class="p">({</span>
  <span class="nx">assemble</span><span class="o">:</span> <span class="p">{</span>
    <span class="nx">options</span><span class="o">:</span> <span class="p">{</span>
      <span class="nx">assets</span><span class="o">:</span> <span class="s1">'docs/assets'</span><span class="p">,</span>
      <span class="nx">data</span><span class="o">:</span> <span class="s1">'src/data/*.{json,yml}'</span><span class="p">,</span>
      <span class="nx">helpers</span><span class="o">:</span> <span class="s1">'src/custom-helpers.js'</span><span class="p">,</span>
      <span class="nx">partials</span><span class="o">:</span> <span class="p">[</span><span class="s1">'src/partials/**/*.{hbs,md}'</span><span class="p">]</span>
    <span class="p">},</span>
    <span class="nx">pages</span><span class="o">:</span> <span class="p">{</span>
      <span class="nx">options</span><span class="o">:</span> <span class="p">{</span>
        <span class="nx">layout</span><span class="o">:</span> <span class="s1">'default.hbs'</span>
      <span class="p">},</span>
      <span class="nx">files</span><span class="o">:</span> <span class="p">{</span>
        <span class="s1">'./'</span><span class="o">:</span> <span class="p">[</span><span class="s1">'src/templates/pages/index.hbs'</span><span class="p">]</span>
      <span class="p">}</span>
    <span class="p">}</span>
  <span class="p">}</span>
<span class="p">};</span>
</pre></div>
```

  