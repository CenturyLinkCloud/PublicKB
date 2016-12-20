#
# Modules
#

fs         = require('fs')
path       = require('path')
marked     = require('marked')
colors     = require('colors')
_          = require('underscore')


App =
  failures: []

RegExplorer =
  # anything the l has a space and then caracters after the .md of the link.
  # [foo](/folder/bar.md "title attribute")
  attributes: /(\[[^\[]+\]\(.*\.md\s.+?\))/i

LinkAttributeParser =
  imagePaths: []
  markdownPaths:  []

  currentPath: ''

  Attributes: []

  parse: (file, failed) ->
    App.failures = []
    @printWorkingIndicator()
    @currentPath = file.fullParentDir

    output = fs.readFileSync file.fullPath, 'utf-8'
    markdown = output.split("\n")

    _.each markdown, (line) =>

      attributeMatches = RegExplorer.attributes.exec(line)
      if attributeMatches
        console.log "\nInvalid markdown link '#{attributeMatches[0]}', titles are not supported. (Referenced from '#{file.fullPath}')".red
        failed = true

    failed

  printWorkingIndicator: ->
    process.stdout.write "."


module.exports = LinkAttributeParser
