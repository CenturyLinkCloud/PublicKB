#
# Modules
#

request = require('urllib-sync').request
path    = require('path')
fs      = require('fs')
marked  = require('marked')
_       = require('underscore')

#
# CONSTANTS
#

ERROR_CODE_RANGE_START = 400

App =
  failures: []

RegExplorer =
  link: /(https?:\/\/?)([\da-z\.-]+\.[a-z\.]{2,6}[\/\w\-].*?)"/

LinkParser =
  linkMatches: []
  parse: (file, failed) ->
    console.log "Parsing links...\n\n\n"

    output = fs.readFileSync file.fullPath, 'utf-8'
    markdown = marked(output).split("\n")

    _.each markdown, (line) =>
      line = line.replace(/&amp;/g, '&')
      linkMatch = RegExplorer.link.exec(line)
      @linkMatches.push linkMatch[0].slice(0,-1) if linkMatch

    @validateLinks(file.fullPath)

  validateLinks: (file) ->
    _.each @linkMatches, (link) => @validateLink(link, file)
    failed = if App.failures.length then true else false
    failed

  validateLink: (link, file) ->
    try
      res = request(link)
      status = res.status
      @logError(link, null, status, file) if status >= ERROR_CODE_RANGE_START
    catch error
      @logError(link, error.stack.slice(0, 100), null, file)

  logError: (link, status, errorMsg, file) ->
    extraMsg = if status then "response #{status}." else "error '#{errorMsg}'."
    console.log 'Build failed!'
    console.log "Reaching '#{link}' failed for the following reason: #{extraMsg}"
    console.log "Link referenced in '#{file}'\n"
    App.failures.push link

module.exports = LinkParser
