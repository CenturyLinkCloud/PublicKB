{{{
  "title": "Using the API",
  "date": "5-17-2018",
  "author": "Anthony Hakim",
  "keywords": ["cpc", "cloud", "vmware", "admin", "vcloud", "vcf", "api"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we walk through the basics of creating a New Session (Logging In) with the vCloud Director (vCD) API that is part of CenturyLink Private Cloud on VMware Cloud Foundation™. Once a new session is established, you should follow the detailed [VMware API documentation](https://code.vmware.com/apis/220/vcloud).

### Create a New Session (Logging In)
To begin using the API, you request the system to create a Session object. In this request, you supply your credentials in an Authorization header of the form prescribed by the identity provider that your organization uses. The response includes an authorization token, which you must include in subsequent requests.

Every version of the vCloud API supported by vCloud Director has a login URL that a client can obtain by making an unauthenticated GET request to the api/versions URL. See Example: [Retrieve the Login URL and List of Supported API Versions](https://pubs.vmware.com/vcd-80/index.jsp?topic=%2Fcom.vmware.vcloud.api.sp.doc_90%2FGUID-1CE15CDF-7858-4BE3-8474-505EE3B7BBA1.html). Because all other vCloud API requests must be authenticated, any vCloud API workflow must begin with a login request that creates a session and returns an authorization token in the value of the x-vcloud-authorization header. The token must be included in subsequent vCloud API requests.

To create a session object, you supply your credentials in an Authorization header of the form prescribed by the identity provider that your organization uses, then POST a request to the vCloud API login URL. This request does not have a body. All the information required to create a session is included in the Authorization header.

**Prerequisites**

* Login credentials of a CenturyLink Private Cloud on VMware Cloud Foundation user with appropriate rights.

**Procedure**

* Create a New Session with the vCD endpoint, using the following:
  * Header: Authorization = Basic (username: username@org)
  * Header: Accept = application/vnd.vmware.vcloud.session+xml;version=27.0
  * Method: POST
  * URL: https://yourdccfoundationurl/api/sessions

Response:

The response HEADER includes a re-usable x-vcloud-authorization authorization token and a Session element whose Link elements reference the vCloud API objects to which you have access rights.

* Be sure to note the return header with key name x-vcloud-authorization. This will include a unique session hex number for this header, e.g. 117a0c919f9f4fa5975306d2a7831d95.
* This header, including the token, must be included in each subsequent vCloud API request.
* If the Authorization header is missing from the request, the server returns HTTP response code 403.
* If the credentials supplied in the Authorization header are invalid, the server returns HTTP response code 401.
Important
The authorization token expires after a configurable interval of client inactivity. The default interval is 30 minutes. After the token expires, you must log in again to obtain a new token. The system administrator can change this default.
