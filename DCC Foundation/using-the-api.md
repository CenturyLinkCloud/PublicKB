{{{
  "title": "Using the API",
  "date": "12-29-2017",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we walk through the basics of creating a New Session with the vCloud Director (vCD) APIs that are part of DCC Foundation. Once a new session is established, you can follow the detailed [VMware API documentation](https://code.vmware.com/apis/220/vcloud).

### Create a New Session
To create a New API Session with the vCD endpoint:
* Header: Authorization = Basic (username: <username>@<org>)
* Header: Accept = application/vnd.vmware.vcloud.session+xml;version=27.0
* Method: POST
* URL: https://<yourdccfoundationurl>/api/sessions

Be sure to note the return header with key name x-vcloud-authorization. This will include a unique session hex number for this header, e.g. 117a0c919f9f4fa5975306d2a7831d95.
