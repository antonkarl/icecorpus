var conmenus=new Object();	
defaultsPhrases=["IP-SUB","IP-MAT","IP-MAT-PRN","IP-INF","IP-IMP","CP-QUE"];

npGroup=["NP-SBJ","NP-OB1","NP-OB2","NP-PRD","NP-POS","NP-PRN","NP","NP-MSR","NP-TMP","NP-ADV","NP-DIR","NP-ADT","NP-LFD","NP-SBJ-RSP","NP-OB1-RSP","QP"];
for(i=0; i<npGroup.length; i++){
   addConMenu(npGroup[i],npGroup);
}

advpGroup=["PP","ADVP","ADVP-TMP","ADVP-LOC","ADVP-DIR","NP-MSR","NP-ADV","ADVP-LFD","PP-LFD","ADVP-RSP","ADVP-TMP-RSP"];
for(i=0; i<advpGroup.length; i++){
   addConMenu(advpGroup[i],advpGroup);
}

verbGroup=["VBPI","VBPS","VBDI","VBDS","VAN","VBN","VB"];
for(i=0; i<verbGroup.length; i++){
   addConMenu(verbGroup[i],verbGroup);
}

rpGroup=["RP","P","ADV","ADVR","ADVS","C","CONJ","ALSO"];
for(i=0; i<rpGroup.length; i++){
   addConMenu(rpGroup[i],rpGroup);
}

wpGroup=["WADVP","WNP","WPP","WQP","WADJP"];
for(i=0; i<wpGroup.length; i++){
   addConMenu(wpGroup[i],wpGroup);
}

// fixedLeaf(before,tag,label)

function loadContextMenu( nodeId ){


/*
			<li class="edit"><a href="#edit">IP-SUB</a></li>
			<li class="cut"><a href="#cut">IP-INF</a></li>
			<li class="copy"><a href="#copy">IP-SMC</a></li>
			<li class="paste separator"><a href="#paste">-SPE</a></li>
			<li class="delete"><a href="#delete">-PRN</a></li>
			<li class="quit separator"><a href="#quit">-XXX</a></li>
*/
	// XXX todo, wnode framkallar error on rightclick
	node = $("#"+nodeId).clone();
	nodelabel=trim(node.contents().filter(function() {
  			return this.nodeType == 3;
		}).first().text());

	//html=$("");

	// alert(nodelabel);

//	html+="<div class='conMenuItem'><a href='#fixedleaf:NP-SBJ:*con*:"+nodeId+"'>&lt; NP-SBJ *con*</a></div>";

	$("#conLeft").empty();	
	suggestions=defaultsPhrases;
	if( conmenus[nodelabel] != null ){
		suggestions=conmenus[nodelabel].suggestions;
	}

	for( i=0; i<suggestions.length; i++){
	    if( suggestions[i] != nodelabel ){
	    	newnode = $("<div class='conMenuItem'><a href='#'>"+suggestions[i]+"</a></div>");
		$(newnode).mousedown( function(){ 
			  		e = window.event;
			  		var elementId = (e.target || e.srcElement).id;
					suggestion = ""+ $(this).text();
					// alert(nodeId + " " + suggestion);
					setNodeLabel( $("#"+nodeId), suggestion );
					hideContextMenu(); 
				} );
 	        $("#conLeft").append( newnode );
	    }
	}
	
	$("#conRight").empty();	
	// do addleafbefore
	newnode = $("<div class='conMenuItem'><a href='#'>XXXX</a></div>");
			$(newnode).mousedown( function(){ 
				  		e = window.event;
				  		var elementId = (e.target || e.srcElement).id;
						suggestion = ""+ $(this).text();
						// alert(nodeId + " " + suggestion);
						setNodeLabel( $("#"+nodeId), suggestion );
						hideContextMenu(); 
					} );
		$("#conRight").append( newnode );

}

function addConMenu( label, suggestions ){
	conmenus[label]=new function(){
		this.suggestions = suggestions;
	}
}
