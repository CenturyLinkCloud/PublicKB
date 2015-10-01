# Commit Analyzer

This project contains a number of parsers that run against each markdown file (`*.md` filename) in a project repository, creating a test suite of sorts.

The parsers validate that the following are true:

* File's JSON front-matter parses correctly and contains the required fields (title, date, autor)
* File's markdown successfully parses
* All relative files (images and other markdown files) are valid links

## Usage

1. Add this project as a submodule into your repository. It is recommended to install this in the `lib` directory:

```shell
$ git submodule add git@github.com:CenturyLinkCloud/KB-Commit-Analyzer.git lib
```

2. Then you'll be able to run the suite:

```shell
node lib/index.js
```

_Note that the first time you wish to run the commit analyzer, you'll have to run `npm install` from the `lib` directory. This assumes you have [Node.js](http://nodejs.org) installed._

The output will tell you if any file fails parsing. This script is also run as part of continuous integration with [travis-ci](http://travis-ci.org).

#### Ignoring Files

If a file contains a link that the commit analyzer catches as being invalid (such as in a code sample), and you'd like the analyzer to ignore that file, you can add the filename to `commit_analyzer_ignore.txt`. (It isn't necessary to include the entire file path; just the filename will suffice.)

### Writing Additional Parsers

A parser must contain a `parse()` method that accepts a `file` and a global `failed` boolean as arguments. For reference, see the [`file_parser.coffee`](https://github.com/CenturyLinkCloud/KB-Commit-Analyzer/blob/master/parsers/file_parser.coffee#L32) file. It should parse a file as required (likely by converting it to markdown and splitting on a newline, passing each line into some sort of check) and return a boolean, which signifies whether or not there were any failures in parsing). It should be `exported` in the `module.exports` in the file and `require`d in `app.coffee`. Finally, the name of the parser should be added to the `parsers` array in `app.coffee`.
