#
# Modules
#

readdirp     = require('readdirp')
path         = require('path')
es           = require('event-stream')
coffeescript = require('coffee-script')
fs           = require('graceful-fs')
_            = require('underscore')

#
# Parsers
#

frontMatterParser   = require('./parsers/front_matter_parser')
markdownParser      = require('./parsers/markdown_parser')
fileParser          = require('./parsers/file_parser')
linkParser          = require('./parsers/link_parser')
linkAttributeParser = require('./parsers/link_attribute_parser')

F =
  failed: null

Ignored =
  files: []

App =
  analyze: ->
    @loadIgnored()
    readdirp @readOpts(), (file) =>
      return if @fileIsIgnored file.name
      _.each @parsers, (parser) =>
        failed = F.failed
        F.failed = parser.parse(file, failed)
    , (err, res) =>
      if F.failed then process.exit(1) else process.exit(0)

  parsers: [frontMatterParser, markdownParser, fileParser, linkAttributeParser]
  #parsers: [fileParser]

  # Uncomment for production files
  directoryFilters: ['!node_modules', '!lib']
  fileFilters: '*.md'

  # Uncomment for test files
  #directoryFilters: ['Accounts & Users']
  #fileFilters: '!sinatra.md'

  readOpts: ->
    root: path.join(__dirname, '..')
    fileFilter: @fileFilters
    directoryFilter: @directoryFilters

  fileIsIgnored: (file) ->
    _.indexOf(Ignored.files, file) >= 0

  loadIgnored: ->
    try
      files = fs.readFileSync '../commit_analyzer_ignore.txt', 'utf-8'
      files = files.split('\n')
      console.log "\n\nIgnoring #{files.join(', ')}"
      _.each files, (file) -> Ignored.files.push file
    catch err
      console.log "\n\nunable to find commit_analyzer_ignore.txt file; not ignoring any files...\n\n"

App.analyze()
