CenturyLink Cloud Knowledge Base
========

Welcome to the [CenturyLink Cloud](http://www.centurylinkcloud.com) knowledge base repository. This is the source of information on all of our products and services available today. Please follow the guidelines below to contribute or make changes.

If you are new to Git and Github, we highly recommend spending 5 minutes reading this great article on [Understanding the Github Flow](https://guides.github.com/introduction/flow/). This repo follows the Github Flow.


##Overview

The repository is organized by category, and each folder represents a category. Within each category folder are markdown (.md) files that represent an individual knowledge base article.

The top of each .md file contains metadata about the knowledge base article itself. It is used to list things such as author, date created, modified, keywords, title, etc. It looks like this:

```code
{{{
  "title": "ARTICLE TITLE",
  "date": "01-15-2015",
  "author": "Author Name",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}
```

##How to Make Additions or Changes

1. [Fork](https://guides.github.com/activities/forking/) the https://github.com/CenturyLinkCloud/PublicKB repository. This will produce a personal copy of this repo.

2. Then Clone the repo to your desktop.

2. **Anything in the `master` branch is always deployable.** Create a [new branch](https://github.com/blog/1377-create-and-delete-branches) from `master`. Your branch name should be descriptive (e.g., `january-release-notes`, `anti-affinity-policy-faq`) so that others have an idea of what the branch is for.

3. Once your branch has been created, make your changes (add, edit, delete) your knowledge base article in your favorite Markdown editor (we like [Atom](https://atom.io/)).

  ### Links (KB article to KB article)

  Links to articles in the **same** kb category should follow this format:

    ```
    [Link Text](kb-article-name.md)
    ```
    
    so like this:
    
    ```
    [Packages Best Practices](packages-best-practices.md)
    [Using SAML for Single-Sign-On](using-saml-for-single-sign-on-to-the-centurylink-platform-control-portal.md )
    ```

  Links to articles in a **different** kb category should follow this format:

    ```
    [Link Text](../category/kb-article-name.md)
    ```
    
    so like this (folder names are case-sensitive):
    
    ```
    [Packages Best Practices](../Blueprints/packages-best-practices.md)
    [Using SAML for Single-Sign-On](../Control Portal/using-saml-for-single-sign-on-to-the-centurylink-platform-control-portal.md )
    ```

  ### Images

  When adding an image to an article, place the image file in the `images/` directory in the root of this repo. In the article itself, set the image source path like so:

    ```
    ../images/[image file]
    ```

  ### Attachments

  When adding an attachment to an article, place the file in the 'attachments/' directory at the root of this repo. In the article itself, add the file information to the front-matter data at the top of the article like so:

    ```
    "attachments": [
      {
        "file_name": "Attached File",
        "url": "../attachments/Balancing Agility Cost and Control.pdf",
        "type": "application/pdf"
      }
    ]
    ```

  `"file_name"` will be the human readable output of the file which will appear on the page

  `"url"` needs to be set exactly like the above example, like so:

    ```
    ../attachments/[file name]
    ```

  `"type"` is simply the MIME type of the file and is used to check which sort of icon to present on the front end.

4. Commit your change(s) locally to your branch.

5. Push or sync your commit(s) to the remote repository on Github.

6. Create a [pull request](https://help.github.com/articles/creating-a-pull-request) to merge your changes into the `master` branch.

  * [Create a pull request using Github for Windows](https://github.com/blog/1969-create-pull-requests-in-github-for-windows)
  * [Create a pull request using Github for Mac](https://github.com/blog/1946-create-pull-requests-with-github-for-mac)

7. CenturyLink Cloud Platform Team reviews your pull request. If accepted, it will be added to the [Knowledge Base on CenturyLinkCloud.com](http://www.centurylinkcloud.com/knowledge-base).
