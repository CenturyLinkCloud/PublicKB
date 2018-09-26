![Build Status of master branch](https://travis-ci.org/CenturyLinkCloud/PublicKB.svg?branch=master)

# CenturyLink Cloud Knowledge Base

Welcome to the [CenturyLink Cloud](http://www.ctl.io) Knowledge Base (KB) repository. This is the source of information on all of our products and services available today. Please follow the guidelines below to contribute or make changes.

If you are new to Git and Github, we highly recommend spending 5 minutes reading this great article on [Understanding the Github Flow](https://guides.github.com/introduction/flow/). This repo follows the Github Flow.

# NEW FEATURE - Markdown Checker

Before submitting your PR, validate the markdown in https://onramp.ctl.io/#!/markdownChecker

The Github file preview does not render markdown exactly the same as we do in ctl.io/knowledge-base/.  The OnRamp Markdown Checker will show you how your KB article will be rendered in ctl.io.  This is especially useful if you have a table in your article.

Please note, the preview in the OnRamp markdown checker **only** displays the html conversion view.  It does not give the same styles view (colors, font, etc.) at this time.

# Overview

The repository is organized by category, and each folder represents a category. Within each category folder are markdown (.md) files that represent an individual Knowledge Base article.

## How To Make Contributions

1. [Fork](https://guides.github.com/activities/forking/) the https://github.com/CenturyLinkCloud/PublicKB repository. This will produce a personal copy of this repo.

1. Then Clone the repo to your desktop.

   **Note:** If you are using the Github web-based client instead of the desktop version, you will not need to clone this repo to your desktop.

1. If you have an existing fork, make sure it's up to date with the latest version of the `master` branch to avoid conflicts. See the section on [how to merge the latest version of master into your fork](#merging-an-upstream-repository-into-your-fork).

1. **Anything in the `master` branch is always deployable.** Create a [new branch](https://github.com/blog/1377-create-and-delete-branches) from `master`. Your branch name should be descriptive (e.g., `january-release-notes`, `anti-affinity-policy-faq`) so that others have an idea of what the branch is for.

1. Once your branch has been created, make your changes (add, edit, delete) to your KB article in your favorite Markdown editor (we like [Atom](https://atom.io/)).

1. Validate the markdown to HTML conversion in https://onramp.ctl.io/#!/markdownChecker

1. Commit your change(s) locally to your fork/branch.

1. Push or sync your commit(s) to the remote repository on Github.

   **Note:** If you are using the Github web-based client you will not have to sync your commits to the remote repository. Your changes will be added to the repository once you commit them to your fork/branch.

1. Create a [pull request](https://help.github.com/articles/creating-a-pull-request) to merge your changes into the `master` branch.
  * [Create a pull request using Github for Windows](https://github.com/blog/1969-create-pull-requests-in-github-for-windows)
  * [Create a pull request using Github for Mac](https://github.com/blog/1946-create-pull-requests-with-github-for-mac)

    **Note:** If you are uploading a KB and its associated images/attachments, it should all be part of one pull request. Do not upload the article and the images/attachments in separate pull requests.

1. This repository contains a [commit analyzer](https://github.com/CenturyLinkCloud/KB-Commit-Analyzer) that runs against each file in the repository validating that the following are true:

  * File's JSON [front-matter](#front-matter) parses correctly and contains the required fields (title, date, autor)
  * File's markdown successfully parses
  * All [links](#links-kb-article-to-kb-article) and [images](#images) are valid (doesn't return 404)

  Issuing a pull-request will automatically trigger the commit analyzer to validate any changes to the repository as part of continuous integration with [travis-ci](http://travis-ci.org). If you try to commit changes in which there are syntax errors or broken links, the build log from travis-ci will display which files contain errors, and you will receive an email notification that the build failed.

  A pull-request containing errors will look like this:
  ![commit analyzer failure](images/analyzer-failure.png)

  Any error(s) will be displayed in the Travis-CI build log. The build log is accessible at [https://travis-ci.org/CenturyLinkCloud/PublicKB](https://travis-ci.org/CenturyLinkCloud/PublicKB) or by clicking on the "Details" link on the pull request page on Github. Here's an example of a broken link:
  ![build log error](images/analyzer-error-msg.png)

  Pushing/syncing additional commits to your fork/branch will trigger the analyzer to re-check your changes.

  A pull-request without errors will look like this:
  ![commit analyzer failure](images/analyzer-success.png)

  **Note:** Content authors are responsible for making their pull requests pass the commit analyzer. Once they pass, pull requests will be merged.

1. CenturyLink Cloud Team reviews your pull request. If accepted, it will be added to the [Knowledge Base on ctl.io](https://www.ctl.io/knowledge-base).
2. In general Pull Requests are review once in the morning and once in the afternoon (Seattle Time). This is not a garantee but is generally the practice. So if there are no changes required your pull request is generally accepted within a day. However, if there are changes required then the time line depends on when the changes are addressed. So remember to keep an eye on your pull request for comments.


#### Run the Commit Analyzer locally

To run this check locally, `cd` into the root of this project and run:

```shell
node lib/index.js
```

_Note that the first time you wish to run the commit analyzer, you'll have to run `npm install` from the `lib` directory. This assumes you have [Node.js](http://nodejs.org) installed._

### Merging an upstream repository into your fork

If your fork and branch are behind by a number of commits (meaning there have been a lot of changes made to the master branch since you originally forked it), you may need to update your fork to reflect the latest changes. This involves sending a pull request that asks for all changes in the current master branch to be merged into your fork and branch. This is the opposite of a pull request that you would normally send (which merges your changes into the CenturyLinkCloud/PublicKB master branch).

**Via Github.com Website**

1. Open your fork (and branch) on GitHub.
2. Click the **Pull Request** button (next to the **Branch:** drop down list).
3. Click **New Pull Request**. By default, GitHub will compare the master branch of the CenturyLinkCloud/PublicKB with your fork and branch.  
    **Note:** If you have not made any changes to your fork yet, there shouldn’t be anything to compare.
4. Reverse the order of the repositories and branches in the **Base Fork:** and **Head Fork:** drop down lists. Your repository and branch should come before the CenturyLinkCloud/PublicKB master repository and branch. This allows GitHub to compare your fork with the master. You should then see all the latest changes that have been made to the master branch.
5. Click the **Pull Request** button to create a pull request for this comparison.  
    **Note:** You should assign a predictable name to your pull request (e.g., Update from original).
6. Click on **Send Pull Request**.
7. Scroll down and click **Merge Pull Request** and then **Confirm Merge**. If your fork didn’t have any changes, you will be able to merge it automatically.  
    **Note:** You will not be able to merge your own pull request unless you have write access to the CenturyLink Cloud repository.

**Via Terminal (Mac) or Command Prompt (Windows)**

1. Open Terminal (for Mac users) or the command prompt (for Windows and Linux users).
1. Change the current working directory to your local project.
1. Check out the branch you wish to merge to. Usually, you will merge into master.

  `git checkout master`
1. Pull the desired branch from the upstream repository. This method will retain the commit history without modification.

  `git pull https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git BRANCH_NAME`
1. If there are conflicts, resolve them. For more information, see "Resolving a merge conflict from the command line".
1. Commit the merge.
1. Review the changes and ensure they are satisfactory.
1. Push the merge to your GitHub repository.

  `git push origin master`

## KB Article Format

### Category Directory Structure

You can use 1 level of nested categories by creating sub directories under the main category directory.  However, if a Category has any sub directories, all articles must be within those sub directories.

### Front Matter


The top of each .md file contains metadata about the Knowledge Base article itself. It is used to list things such as author, date created, modified, keywords, title, etc. It should look like this:

```code
{{{
  "title": "ARTICLE TITLE",
  "date": "01-15-2015",
  "author": "Author Name",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}
```

**Note:** The article title that appears on the web page is pulled from the "title" section in the metadata. You should not include the title in the text of the .md file.

#### `author`

Please just use your name and do not link off to other version sites (twitter, linkedin, etc.)

#### `contentIsHTML`

Generally this should be set to `false`. Only when a document is written entirely in HTML syntax should this be set to true.

#### `sticky` (optional)

If you would like to pin a KB article so that it always appears at the top of its category, set `"sticky":true`. By default, it's set to `false`.

### Headers

Use heading level 3 (###) as the highest heading level in the KB articles (for consistency).

### Sub-Categories

  Within the top level categories, additional tags can be assigned to articles based on the name of the articles parent folder name. Keep in mind the need for an additional level of folders when linking to images or other articles when authoring an article in a sub-category folder.

### Links

Links to other KB articles should follow this format:

    ```
    [Link Text](../category/kb-article-name.md)
    [Link Text](../category/sub-category/kb-article-name.md)
    ```

    Example (folder names are case-sensitive):

    ```
    [Packages Best Practices](../Blueprints/packages-best-practices.md)
    [Using SAML for Single-Sign-On](../Control Portal/using-saml-for-single-sign-on-to-the-centurylink-platform-control-portal.md)
    ```

Links to ctl.io sites (internal links) should follow this format:

    ```
    [Managed Microsoft SQL](//www.ctl.io/managed-services/ms-sql)
    ```
    **Note:** The links have the "http:" or "https:" removed so that the site will render regardless of the protocol (the ctl.io website only displays https; this ensures there are no conflicts.)

Links to external sites (not ctl.io) should be full, regular links and follow this format:

    ```
    [Github](https://github.com/)
    ```

Links to podcasts should look like this:

  ```
  <iframe id='ei8087582' src='//centurylinklabs.podomatic.com/embed/frame/posting/2016-06-06T12_59_45-07_00?json_url=http%3A%2F%2Fcenturylinklabs.podomatic.com%2Fentry%2Fembed_params%2F2016-06-06T12_59_45-07_00%3Fcolor%3D43bee7%26autoPlay%3Dfalse%26facebook%3Dtrue%26height%3D85%26width%3D620%26minicast%3Dfalse%26objembed%3D0&notb=1' height='85' width='620'frameborder='0' marginheight='0' marginwidth='0' scrolling='no' allowfullscreen></iframe>
  ```
  **Note:** Like the external site links, the "http:" and "https:" are removed from the links to eliminate conflicts.

  Podcasts should be posted on the podomatic website as well.

### Images

  When adding an image to an article, place the image file in the `images/` directory in the root of this repo. The images should not be referenced from outside links. In the article itself, set the image source path like so:

  **Top Level Category Article**
    ```
    ../images/[image file]
    ```

  **Sub-Category Article**
    ```
    ../../images/[image file]
    ```

  Be sure the file name does not include any spaces.

  The image reference within the article should look like this:

    ```
    ![Image Description](../images/[file-name])
    ```
 The image description should be short and relevant to the image.

### Images within Ordered Lists

 When referencing an image within an ordered list, the image should follow the format below. This keeps the image reference from breaking the numbering within the list.

    ```
    1. [Text][at least two blank spaces after the text]
    [blank line]
    [An indent, using tab or 4 blank spaces]![Image Description](../images/[file-name])
    [blank line]
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

  Be sure the file name does not include any spaces.

  `"url"` needs to be set exactly like the above example, like so:

    ```
    ../attachments/[file name]
    ```

  `"type"` is simply the MIME type of the file and is used to check which sort of icon to present on the front end.

### Tables

  Tables in articles should follow this format:

  ```
  **Bold Text**|**Bold Text**|**Bold Text**
  -------------|-------------|-------------
  TEXT COLUMN A|TEXT COLUMN B|TEXT COLUMN C
  TEXT COLUMN A|TEXT COLUMN B|TEXT COLUMN C
  ```

### Table of Contents

  For longer articles a table of contents can improve the browsing experience of the user. **Lowercase** must be used for the `#section-a` to properly jump to the appropriate section of the article.

  ```
  ### Table of Contents

  * [Section A](#section-a)
  * [Section B](#section-b)
  * [Section C](#section-c)
  * [Section C](#section-d)

  ### Section A
  Text for this area.

  ### Section B
  Text for this area.
  ```
