{{{
  "title": "CDN Mesh Delivery Capabilities",
  "date": "02-13-2020",
  "author": "Jim Greene",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

CenturyLink® CDN Mesh Delivery is an advanced implementation of the WebRTC standard that enables delivery of live and video on-demand (VOD) content across a meshed topology from a CDN and between end user devices.

Tier 1 broadcasters can access the following technology for live streams, catch-up TV, user generated content, as well as ad or subscription-based VOD content.

**Platform compatibility**

* Web browsers (Chrome, Firefox, Safari, Opera, Chromium-based browsers)
* iOS
* Android
* Android TV
* tvOS
* FireTV
* all other Android-based STBs
* Chromium-based STBs
* Chromecast
* Samsung TVs (Tizen 3.0+)
* LG TVs (WebOS 3+)

**Player compatibility**

* hls.js
* dash.js
* video.js
* Skaka Player
* Flowplayer
* Clappr
* JW Player
* THEOPlayer
* Bitmovin Player
* RadiantMP
* Castlabs
* Brightcove Player
* Azure Media Player
* thePlatform MPX Player
* AMP
* Kaltura Player
* ExoPlayer
* NexPlayer
* AVPlayer

**Custom players**

* Can integrate with custom HTML5 players upon request
* Can integrate with custom Android & iOS-based players upon request

**Media format support**

* HTTP Streaming formats supports: DASH, HLS, Smooth Streaming
* Supports both live and VOD streaming, without adding any latency for live
* CMAF support
* Support for multi-bitrate streams

**Media features**

* DRMs, tokens, geo-blocking & authentication mechanisms supported
* SSAI providers support: Amazon Media Tailor, Yospace, AdInsertion Platform
* Supports all common media features like subtitles, multi-audio, DVR, fallback URLs, etc.

**Security features**

* Mesh network cryptographic integrity checks
* Domain whitelisting
* App secret key whitelisting
* Fully encrypted communications with the backend (HTTPS & WSS)
* DNA backend authentication and matching features
* Fully encrypted DTLS mesh network communications

**DNA dashboard - Web GUI to monitor and control**

* Monitor DNA vs CDN traffic in volume and throughput
* See number of concurrent users over time
* See details per stream and per platform
* QoS data: buffering ratio over time

**Data API**

* Basic Data API:
   - DNA & CDN traffic over time
   - Concurrent viewers over time
   - Buffering ratio over time
   - Top 100 streams in traffic, bandwidth and audience

**Advanced data analysis**

* Advanced Insights API (to be released in December) allowing multidimensional queries including:
   - Platform
   - Live & VOD
   - Stream
   - SiteId
   - Country
   - ISP
* Custom Efficiency Reports per customer upon request (paid service), accessing and compiling data from our Hadoop data pipeline

**Dashboard real-time monitoring**

* Real-time monitoring panel showing top streams with DNA vs. CDN efficiency and audience

**Alerting and reporting**

* Automatic reporting interface that can send daily, weekly and monthly reports on efficiency and traffic
* On-demand alerting service from our customer support if we detect anything unusual in different metrics: efficiency, audience, QoS, new release, etc.

**Dashboard configuration**

* Create properties to use different configuration options for different types of content (live vs. VoD, premium vs. free, etc.)
* SSAI detection
* Range request detection
* Wifi and cellular network upload and download configuration
* Activation Ratio feature for easy ramp-up and full control over the mesh network
* Activation threshold for VOD: activate the DNA plugin only on the most popular streams with more than 3 active users in the last 20 minutes

**Client-side configuration and API**

* Configuration: ContentId, asynchronous loading, siteId for DNA Enterprise
* Client API:
   - Per-user traffic data
   - Upload and download control API per network type

**Client-side optimization features**

* UDP-based delivery, better resource utilization than for HTTP/TCP
* 100% transparent for end-users: nothing to install
* In-segment multisourcing: pre-fetching each segment from several peers at the same time
* Adaptive Device Resource Usage: our module constantly monitors core health metrics on the device (CPU, memory, QoS, battery, etc.) to adapt the efficiency algorithms to the capabilities of the device in real time
* Advanced congestion control algorithms
* Protection against uplink saturation
* Pre-buffering from other peers
* Dynamic buffer level configuration (patented)

**Matching features**

* Smart matching via machine learning by network topology, ISP, region, city, etc.
* Can restrict matching between specific ISPs or inside specific ISPs

**SLA**

* 99.99% uptime
* Instant and seamless fallback to CDN in case of any issues
* Multi-region backend for better resilience and high availability
* Can overcome short CDN downtimes by offloading delivery to the peer network

More information: [Technical Brochure](https://www.ctl.io/lp/resources/cdn-mesh-delivery-technical-brochure.pdf)
