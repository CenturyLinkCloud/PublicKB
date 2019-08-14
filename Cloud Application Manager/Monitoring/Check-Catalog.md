{{{
  "title": " CAM Monitoring Site - Check Catalog
",
  "date": "08-14-2019",
  "author": "Randy Wansing",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": true,
  "sticky": true
}}}

<html>
	<head>
	    <title>List of Checks</title>
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">    
	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
	    <script>
	        var xhr = new XMLHttpRequest();
	        
	        xhr.open('GET', "https://api.watcher.ctl.io/check_types", true);
	        xhr.send();
	        xhr.addEventListener("readystatechange", processRequest, false);

	        	
	        function processRequest() {

	          console.log("response came back");
	          console.log(xhr);
	            if (xhr.readyState == 4 && xhr.status == 200) {
	        		var response = JSON.parse(xhr.responseText);
	                var categories = response.items.map(function (item) {return item.category});
	                var distictCategory = GetUniqueCategory(categories);

	                // CREATE TABS
	                createTabs(distictCategory);
	                // CREATE TAB CONTENT
	                createCollapse(response, distictCategory);

	                document.getElementById("response").innerHTML = '<h3 class="heading text-success">Overview</h3><br /><p>The Check Catalog is library that contains the available Checks (metric or status) that can be added to Policies within the Cloud Application Manager.  Managed Services Anywhere offers ' + response.count + ' Total Checks. <br /><h3 class="heading text-success">Check Catalog </h3><br />'
	            }
	        }

	        function GetUniqueCategory(categories) {
	            var UniqueNames = [];
	            categories.forEach(function(value) {
	            if (UniqueNames.indexOf(value) === -1) {
	                    UniqueNames.push(value);
	                }
	            });

	            return UniqueNames.sort();
	        }

	        function createTabs(categories) {
	            var cloudNames = ['AWS', 'Azure', 'VMWare'];
	            var systemNames = ['Apache', 'Docker', 'Elastic Search', 'Java', 'Kubernetes', 'MS IIS Server', 'MS SQL Server', 'MongoDB', 'MySQL', 'Postgres', 'Rabbit MQ', 'Tomcat'];
	            var fileNames = ['File System', 'HTTP', 'Linux System', 'Logging', 'Networking', 'NTP', 'Process', 'SNMP', 'Windows System'];
	            var customNames = ['Custom', 'Metric Service'];

	                                        
	            // CREATE TAB.
	            var ul = document.createElement("ul");
	            
	            ul.className = 'nav md-pills pills-primary flex-column';
	            ul.setAttribute("role", "tablist");

	            for (i = 0; i < cloudNames.length; i++) {
	                var ariaControlsValue = 'v-pills-' + cloudNames[i].toLowerCase().replace(" ", "_");
	                var li = document.createElement('li');           
	                li.className = 'nav-item';
	                var iElement = document.createElement('i');
	                iElement.className = 'fas fa-cloud';
	                var a = document.createElement('a');
	                a.className = 'nav-link';
	                a.href = '#' + cloudNames[i].toLowerCase().replace(" ", "_");
	                a.setAttribute("data-toggle", "pill");
	                a.setAttribute("role", "tab");
	                a.setAttribute("aria-controls", ariaControlsValue);
	                a.setAttribute("aria-selected", "false");
	                a.type = 'button';
	                a.innerHTML = '<i class="fas fa-cloud"></i>  ' + cloudNames[i];
	                li.appendChild(a);
	                ul.appendChild(li);
	            }

	            for (i = 0; i < systemNames.length; i++) {
	                var ariaControlsValue = 'v-pills-' + systemNames[i].toLowerCase().replace(" ", "_");
	                var li = document.createElement('li');            
	                li.className = 'nav-item';
	                var a = document.createElement('a');
	                a.className = 'nav-link';
	                if (systemNames[i] === 'Elastic Search' || systemNames[i] === 'Rabbit MQ'){
	                    a.href = '#' + systemNames[i].toLowerCase().replace(" ", "");
	                } else if(systemNames[i] === 'MS IIS Server') {
	                   
	                    a.href = '#ms_iis';
	                } else if(systemNames[i] === 'MS SQL Server') {
	                   
	                    a.href = '#ms_sql';
	                } else {
	                    a.href = '#' + systemNames[i].toLowerCase().replace(" ", "_");
	                }                
	                a.setAttribute("data-toggle", "pill");
	                a.setAttribute("role", "tab");
	                a.setAttribute("aria-controls", ariaControlsValue);
	                a.setAttribute("aria-selected", "false");
	                a.type = 'button';
	                a.innerHTML = '<i class="fas fa-desktop"></i>  ' + systemNames[i];
	                li.appendChild(a);
	                ul.appendChild(li);
	            }

	            for (i = 0; i < fileNames.length; i++) {
	                var ariaControlsValue = 'v-pills-' + fileNames[i].toLowerCase().replace(" ", "_");
	                var li = document.createElement('li');            
	                li.className = 'nav-item';
	                var a = document.createElement('a');
	                a.className = 'nav-link';
	                if (fileNames[i] === 'File System'){
	                    a.href = '#' + fileNames[i].toLowerCase().replace(" ", "");
	                } else {
	                    a.href = '#' + fileNames[i].toLowerCase().replace(" ", "_");
	                }
	                a.setAttribute("data-toggle", "pill");
	                a.setAttribute("role", "tab");
	                a.setAttribute("aria-controls", ariaControlsValue);
	                a.setAttribute("aria-selected", "false");
	                a.type = 'button';
	                a.innerHTML = '<i class="fas fa-server"></i>  ' + fileNames[i];
	                li.appendChild(a);
	                ul.appendChild(li);
	            }

	            for (i = 0; i < customNames.length; i++) {
	                var ariaControlsValue = 'v-pills-' + customNames[i].toLowerCase().replace(" ", "_");
	                var li = document.createElement('li');            
	                li.className = 'nav-item';
	                var a = document.createElement('a');
	                a.className = 'nav-link active';
	                if (customNames[i] === 'Metric Service') {
	                    a.href = '#metric'
	                } else {
	                    a.href = '#' + customNames[i].toLowerCase().replace(" ", "_");
	                }
	                
	                a.setAttribute("data-toggle", "pill");
	                a.setAttribute("role", "tab");
	                a.setAttribute("aria-controls", ariaControlsValue);
	                a.setAttribute("aria-selected", "false");
	                a.type = 'button';
	                a.innerHTML = '<i class="fas fa-toolbox"></i>  ' + customNames[i];
	                li.innerHTML = a.outerHTML;
	                ul.appendChild(li);
	            }
	            var divContainer = document.getElementById("v-pill-tab");
	            divContainer.setAttribute('data-spy', 'scroll');
	            divContainer.setAttribute('style', 'position: relative; height: 400px; overflow-y: scroll;');
	            divContainer.innerHTML = "";
	            divContainer.appendChild(ul);
	        }
	        function createCollapse(response, categories) { 
	            var divTabContent = document.getElementById('v-pill-tabcontent');                      
	            for (i = 0; i < categories.length; i++) { 
	                var divTabPane = document.createElement('div');               
	                divTabPane.className = 'tab-pane fade';
	                divTabPane.setAttribute("id", categories[i]);
	                divTabPane.setAttribute("role", "tabpanel");
	                divTabPane.setAttribute("aria-labelledby", "v-pills-" + categories[i] + "-tab");
	                divTabPane.setAttribute('data-spy', 'scroll');
	                divTabPane.setAttribute('style', 'position: relative; height: 400px; overflow-y: scroll;');
	                var divCard = document.createElement('div');
	                divCard.className = 'accordion';
	                divCard.setAttribute('id', 'accordion_' + categories[i]);
	                for (j = 0; j < response.items.length; j++) {                    
	                    if (response.items[j].category === categories[i]) {
	                        var name = response.items[j].name;
	                        if (name.toLowerCase() === 'chrony' && response.items[j].type === 'metric') {
	                            continue;
	                        }                        
	                        console.log(name);
	                        var description = response.items[j].description;                        
	                        var divCard2 = document.createElement('div');
	                        divCard2.className = 'card';
	                        var divCardHeader = document.createElement('div');
	                        divCardHeader.className = 'card-header';
	                        divCardHeader.setAttribute('id', categories[i] + '' + i);
	                        var cardHeaderValue = document.createElement('h2');
	                        cardHeaderValue.className = 'mb-0';
	                        var cardHeaderButton = document.createElement('button');
	                        cardHeaderButton.className = 'btn btn-link';
	                        cardHeaderButton.setAttribute('type', 'button');
	                        cardHeaderButton.setAttribute('data-toggle', 'collapse');                        
	                        cardHeaderButton.setAttribute('data-target', '#' + name.toLowerCase().replace(/\s+/g, '-'));
	                        cardHeaderButton.setAttribute('aria-expanded', 'true');
	                        cardHeaderButton.setAttribute('aria-controls', name.toLowerCase().replace(/\s+/g, '-'));
	                        cardHeaderButton.innerHTML = name;
	                        if (name.toLowerCase() === 'process' || name.toLowerCase() === 'snmp') {
	                            name += '1'
	                            cardHeaderButton.setAttribute('data-target', '#' + name.toLowerCase());
	                            cardHeaderButton.setAttribute('aria-controls', name.toLowerCase());
	                        } else {
	                            cardHeaderButton.setAttribute('data-target', '#' + name.toLowerCase().replace(/\s+/g, '-'));
	                            cardHeaderButton.setAttribute('aria-controls', name.toLowerCase().replace(/\s+/g, '-'));
	                        }
	                        cardHeaderValue.appendChild(cardHeaderButton);
	                        divCardHeader.appendChild(cardHeaderValue);
	                        divCard2.appendChild(divCardHeader);
	                        divCard.appendChild(divCard2);                        
	                        var divCardCollapse = document.createElement('div');
	                        divCardCollapse.className = 'collapse';
	                        divCardCollapse.setAttribute('id', name.toLowerCase().replace(/\s+/g, '-'))
	                        divCardCollapse.setAttribute('aria-labelledby', categories[i] + '' + i);
	                        divCardCollapse.setAttribute('data-parent', '#accordion_' + categories[i]);
	                        var divCardBody = document.createElement('div');
	                        divCardBody.className = 'card-body';                        
	                        divCardBody.innerHTML = description;
	                        divCardCollapse.appendChild(divCardBody);                        
	                        divTabPane.appendChild(divCard).appendChild(divCardCollapse);
	                        divTabContent.appendChild(divTabPane)
	                    }                    
	                }
	                
	            }
	            
	            
	            

	        }
	        
	    </script>
	</head>
	<body>
	  <div class="container" id="response" >
	    count of checks    
	  </div>
	  <div class="container left">
	      <div class="row">
	          <div data-spy="scroll" class="col-3" id="v-pill-tab" data-offset="0">
	          
	          </div>
	          <div class="tab-content col-9" id="v-pill-tabcontent">

	          </div>
	      </div>
	  </div>  
	</body>
</html>
