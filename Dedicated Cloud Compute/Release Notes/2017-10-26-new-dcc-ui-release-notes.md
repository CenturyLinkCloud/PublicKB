{{{
"title": "New DCC UI Release Notes: October 26, 2017",
"date": "10-26-2017",
"author": "Anthony Hakim",
"attachments": [],
"contentIsHTML": false
}}}

### Bug Fixes and General Updates

* Bug fixes for Create VM:

  Added validation error if the catalog is from a different cluster.

* ESX Validation error handling in UI:

  When a validation fails during add product, the API was returning a generic error code to the UI. This has been updated to return a more specific error message.

* OS Validation bug fix:

  Added better wording for validation error message for CPU requirement check.
