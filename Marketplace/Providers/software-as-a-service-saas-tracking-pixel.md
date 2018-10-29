{{{
"title": "Software as a Service (SaaS) Integration - Tracking Pixel",
"date": "03-01-2017",
"author": "Rich DuBose",
"attachments": [],
"contentIsHTML": false
}}}

### Overview

CenturyLink has created multiple opportunities for software vendors to integrate with the Cloud Marketplace. Each of these methods is designed for the provider to be as independent as possible as they work through the integration process.  To be included in the Cloud Marketplace, a SaaS provider must implement one of these methods. During the Marketplace Provider Onboarding Program, we will discuss which integration type is the best fit. 

### Integration Types

#### Tracking Pixel

**Overview** 

The tracking pixel option allows CenturyLink to monitor demand & accounts created by the CenturyLink Cloud Marketplace drives to your organizations website & product.

Below is a JavaScript tracking pixel that may be used to integrate with the CenturyLink Cloud Marketplace. You will need the Provider Key that you were provided during onboarding with the tracking pixel. If you were not provided a Provider Key or require a new one to be issued, contact us at [Marketplace@centurylink.com](mailto:Marketplace@centurylink.com).

**JavaScript Tracking Pixel**
```
'use strict';
const request = require('request'),
  ONRAMP_BASE_URL = process.env.ONRAMP_BASE_URL,
  ONRAMP_URL = ONRAMP_BASE_URL + '/api/SaasTrackings';

function createSaasTracking(partnerKey, serviceName, customerId, purchasedAt) {
  let options = {
    body: {
      partnerKey: partnerKey,
      serviceName: serviceName,
      customerId: customerId,
      purchasedAt: purchasedAt
    },
    qs: {},
    method: 'POST',
    timeout: 60000,
    simple: false,
    json: true
  };

  request(ONRAMP_URL, options, function (error, response, body) {
    if (error) {
      console.error('error:', error);
      process.exit(1);
    }
    console.log('statusCode:', response && response.statusCode);
    console.log('body:', body);
  });
}

if (process.argv.length < 4) {
  console.error('error - missing parameter.');
  console.error('usage:', process.argv[1], 'partner-key service-name customer-id paurchased-at');
  process.exit(1);
}

createSaasTracking(process.argv[2], process.argv[3], process.argv[4], process.argv[5]);
```
