var conmenus=new Object();
var conleafs=new Array();

function addConMenu( label, suggestions ){
	conmenus[label]=new function(){
		this.suggestions = suggestions;
	}
}


function addConLeaf(suggestion,before,label,word){
	conleaf=new Object();
	conleaf.suggestion=suggestion;
	conleaf.before=before;
	conleaf.label=label;
	conleaf.word=word;
	
	conleafs.push(conleaf);
}

function addConMenuGroup( group ){
   for(i=0; i<group.length; i++){
      addConMenu(group[i],group);
   }	
}

// Load the custom context menu groups from user settings file
customConMenuGroups();

function addConLeafBefore( phrase, terminal ){
	addConLeaf("&lt; ("+phrase+" "+terminal+")",true,phrase,terminal);
}

// Load the custom context menu "leaf before" items
customConLeafBefore(); 

	
defaultsPhrases=defaultConMenuGroup;

function isCasePhrase( nodeLabel ){
	if( nodeLabel.startsWith("NP") ){
		return true;			
	}		
	if( nodeLabel.startsWith("ADJP") ){
		return true;			
	}		
	if( nodeLabel.startsWith("QP") ){
		return true;			
	}		
		
	return false;
}

function getSuggestions( label ){
	
	indstr="";
	indtype="";
	extensionstring="";
	
	if( parseIndex(label)>0 ){		
	    indstr=parseIndex(label);
	    indtype=parseIndexType(label);
	 }
	 extensionstring=""; //parseExtensions(label);
	 label = parseLabel(label); //.substr(0,label.length-extensionstring.length);	
	
	 //alert( extensionstring );
	
	// alert(extensionstring);
		
	var suggestions = new Array();		
	var menuitems = defaultsPhrases;		
	if( conmenus[label] != null ){
		menuitems = conmenus[label].suggestions;
	}		
	
	for( i=0; i<menuitems.length; i++ ){
		var menuitem = menuitems[i];
		suggestions.push( menuitem + extensionstring + indtype + indstr );
		
		if( conmenus[menuitem] != null ){
			var iitems = conmenus[menuitem].suggestions;
			for( j=0; j<iitems.length; j++){
				suggestions.push(iitems[j]  + extensionstring + indtype + indstr );
			}
			
		}				
	}
	
	
	
	/*
	for( i=0; i<suggestions.length; i++){
			var suggestion = suggestions[i];
			
			if( conmenus[suggestion[i]] != null ){
				moremenus = conmenus[suggestion[i]];
				for( j=0; j<moremenus.length; j++ ){
					suggestions
				}				
			}

	}
	*/
	
	return suggestions.unique();		
}


function loadContextMenu( nodeId ){

	nodeIndex = getIndex( $("#"+nodeId) );
	indexSep="";
	indexString="";
	
	node = $("#"+nodeId).clone();
	nodelabel=trim(node.contents().filter(function() {
  			return this.nodeType == 3;
		}).first().text());
	
	if( nodeIndex > -1 ){
		lastindex=Math.max(nodelabel.lastIndexOf("-"),nodelabel.lastIndexOf("="));
		indexSep = nodelabel.charAt(lastindex);
		nodelabel = nodelabel.substr(0, getLabel( $(node)).length-2 );									
		indexString = indexSep+""+nodeIndex;
	}

	$("#conLeft").empty();	
	$("#conLeft").append($("<div class='conMenuHeading'>Label</div>"));	
	

			
	
	if (/-[NADG]$/.test( nodelabel )) {				
		//alert(nodelabel);		
		
		for (i = 0; i < caseTags.length; i++) {

			theCase=nodelabel.substr(nodelabel.length-1);
			suggestion = caseTags[i]+"-"+theCase;
			
			if (suggestion != nodelabel) {
				newnode = $("<div class='conMenuItem'><a href='#'>" + suggestion + "</a></div>");
				$(newnode).mousedown(function(){
					e = window.event;
					var elementId = (e.target || e.srcElement).id;
					suggestion = "" + $(this).text();
					setNodeLabel($("#" + nodeId), suggestion);
					hideContextMenu();
				});
				$("#conLeft").append(newnode);
			}
		}
		
		extraNominalSuggestions=["ADV","ES"];		
	    for (i = 0; i < extraNominalSuggestions.length; i++) {
			suggestion = extraNominalSuggestions[i];
			// suggest ADV 
			newnode = $("<div class='conMenuItem'><a href='#'>" + suggestion + "</a></div>");
			$(newnode).mousedown(function(){
				e = window.event;
				var elementId = (e.target || e.srcElement).id;
				suggestion = "" + $(this).text();
				// alert(nodeId + " " + suggestion);
				setNodeLabel($("#" + nodeId), suggestion);
				hideContextMenu();
			});
			$("#conLeft").append(newnode);
		}
		//setNodeLabel($("#" + childId), oldLabel.substr(0, oldLabel.length - 2) + "-" + theCase, true);
	}
	else {
	
	
	suggestions = getSuggestions(nodelabel);
		for (i = 0; i < suggestions.length; i++) {
			if (suggestions[i] != nodelabel) {
				newnode = $("<div class='conMenuItem'><a href='#'>" + suggestions[i]+indexString+"</a></div>");
				$(newnode).mousedown(function(){
					e = window.event;
					var elementId = (e.target || e.srcElement).id;
					suggestion = "" + $(this).text();
					// alert(nodeId + " " + suggestion);
					setNodeLabel($("#" + nodeId), suggestion);
					hideContextMenu();
				});
				$("#conLeft").append(newnode);
			}
		}
		
}
	
// do the right side context menu	
	$("#conRight").empty();	
	
// Set in user settings file
if( displayCaseMenu ){
			if (  /-[NADG]$/.test(nodelabel) ){
				// alert("x"+nodelabel+"x");
				
				    $("#conRight").append($("<div class='conMenuHeading'>Case</div>"));
					
					newnode = $("<div class='conMenuItem'><a href='#'>-N</a></div>");
					$(newnode).mousedown(setCaseOnTag(nodeId,nodelabel,"N"));
					$("#conRight").append(newnode);	
				    
					newnode = $("<div class='conMenuItem'><a href='#'>-A</a></div>");
					$(newnode).mousedown(setCaseOnTag(nodeId,nodelabel,"A"));
					$("#conRight").append(newnode);	
					    	
					newnode = $("<div class='conMenuItem'><a href='#'>-D</a></div>");
					$(newnode).mousedown(setCaseOnTag(nodeId,nodelabel,"D"));
					$("#conRight").append(newnode);	
					
					newnode = $("<div class='conMenuItem'><a href='#'>-G</a></div>");
					$(newnode).mousedown(setCaseOnTag(nodeId,nodelabel,"G"));
					$("#conRight").append(newnode);			
			}		
			else if( isCasePhrase(nodelabel) ){
				    $("#conRight").append($("<div class='conMenuHeading'>Case</div>"));
					
					newnode = $("<div class='conMenuItem'><a href='#'>-N</a></div>");
					$(newnode).mousedown(doSetCase(nodeId,"N"));
					$("#conRight").append(newnode);	
				    
					newnode = $("<div class='conMenuItem'><a href='#'>-A</a></div>");
					$(newnode).mousedown(doSetCase(nodeId,"A"));
					$("#conRight").append(newnode);	
					    	
					newnode = $("<div class='conMenuItem'><a href='#'>-D</a></div>");
					$(newnode).mousedown(doSetCase(nodeId,"D"));
					$("#conRight").append(newnode);	
					
					newnode = $("<div class='conMenuItem'><a href='#'>-G</a></div>");
					$(newnode).mousedown(doSetCase(nodeId,"G"));
					$("#conRight").append(newnode);			
			}	
}

	// do addleafbefore
	$("#conRight").append($("<div class='conMenuHeading'>Leaf before</div>"));
	for (i = 0; i < conleafs.length; i++) {
		stackTree();	    			
		newnode = $("<div class='conMenuItem'><a href='#'>"+conleafs[i].suggestion+"</a></div>");
		$(newnode).mousedown(doConLeaf(i,conleafs[i],nodeId));
		$("#conRight").append(newnode);
	}
	
	
	$("#conRightest").empty();	
	$("#conRightest").append($("<div class='conMenuHeading'>Toggle ext.</div>"));
			
	for( i=0; i<extensions.length; i++){	
		// do the right side context menu					
		newnode = $("<div class='conMenuItem'><a href='#'>"+extensions[i]+"</a></div>");
		$(newnode).mousedown( doToggleExtension( nodeId, extensions[i] )  );		
		$("#conRightest").append(newnode);	
	}
}

function doToggleExtension( nodeId, extension ){
	return function(){
		stackTree();		
		clearSelection();
		selectNode(nodeId);		
		//alert(nodeId + " " + extension);
		toggleExtension(extension);
		hideContextMenu();
		clearSelection();
	}	
}

/*
 * set case just on this one tag 
 */
function setCaseOnTag( nodeId, oldLabel, theCase ){
	return function(){
		stackTree();		
		setNodeLabel($("#"+nodeId), oldLabel.substr(0,oldLabel.length-2)+"-"+theCase,true);			
	}	
}

/*
 * set case on all case elements that are daughters of this phrase node
 */
function doSetCase( nodeId, theCase ){
	return function(){
		stackTree();
		//alert(nodeId + " " + theCase);
		daughters = $("#"+nodeId).children().each( function(){			
			childId = $(this).attr("id");
						
			oldLabel=trim($(this).contents().filter(function() {
  				return this.nodeType == 3;
			}).first().text());
			if( /-[NADG]$/.test(oldLabel) ) {				
				setNodeLabel($("#"+childId), oldLabel.substr(0,oldLabel.length-2)+"-"+theCase,true);					
			}
																			
				
		} );
		
				
	}

}




function doConLeaf(idx,conleaf,nodeId){
		return function(){
			makeLeaf(conleaf.before, conleaf.label, conleaf.word, nodeId, true);
			hideContextMenu();
		}
}
