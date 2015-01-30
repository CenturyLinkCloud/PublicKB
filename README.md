Public Knowledge Base
========

Welcome to [CenturyLink Cloud](http://www.centurylinkcloud.com) knowledge base repository. This is the source of information on all of our products and services available today. Please follow the guidelines below to contribute or make changes.

##How this Works

* **Headers:** The system uses Jekyll _(like)_ headers to be able to list current information and also track things such as author, date created, modified, keywords, title, etc.

```code
---
title: Blogging Like a Hacker
author: Joe Smith
keywords: cat, foo, bar, nice, crack, fun
categories: Hyperscale, VMStandard
permlink: /blogging-like-a-hacker
---
```

* **Markdown:** It is also built using all markdown for the documents. For more information about markdown please use [Google](https://www.google.com/webhp?sourceid=chrome-instant&rlz=1C5CHFA_enUS503US504&ion=1&espv=2&ie=UTF-8#q=markdown%20syntax)

* **Folder Structure:** folders are by products and should remain that way. If you want your document to be supported in multiple categories please use the headers to list all of the categories it is in. All image and assets should be located in the local product folder or in a folder next to the document. It should not be on the root of the directory structure. 



##How to Make Changes

To make any changes please submit a [pull request](https://help.github.com/articles/creating-a-pull-request). Once a pull request is accepted it will be live within the next 1-2 hours to our public web site. This also allows for rolling back a commit and making changes with history tracking.

##Setting Up a Test Environment


##FAQ
- Specific Markdown
- Specific Class and Modules

- Images - when adding an image to an article, place the image file in the `images/` directory in the root of this repo. In the article itself, set the image source path like so: 

  ```
  /knowledge-base/images/[image file]
  ```


- Attachments - when adding an attachment to an article, place the file in the 'attachments/' directory at the root of this repo. In the article itself, add the file information to the front-matter data at the top of the article like so:

  ```
  "attachments": [
    {
      "file_name": "Attached File",
      "url": "/knowledge-base/attachments/Balancing Agility Cost and Control.pdf",
      "type": "application/pdf"
    }
  ]
  ```

  `"file_name"` will be the human readable output of the file which will appear on the page

  `"url"` needs to be set exactly like the above example, like so: 
    
    `/knowledge-base/attachments/[file name]`

  `"type"` is simply the MIME type of the file and is used to check which sort of icon to present on the front end.


- How Attachments are Handled
- Front Matter - Config Data
- Category Landing page config
- Anchors and TOC