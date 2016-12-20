#
# Modules
#

fs     = require('fs')
marked = require('marked')
colors = require('colors')
_      = require('underscore')

App =
  failures: []

MarkdownParser =
  parse: (file, failed) ->
    process.stdout.write "."
    fs.readFile file.fullPath, 'utf-8', (err, data) ->
      try
        marked(data)
      catch error
        console.log e
        console.log "\nFile '#{file.fullPath}' failed markdown parsing.\n"
        App.failures.push file.fullPath

    failed = true if App.failures.length
    failed

module.exports = MarkdownParser
