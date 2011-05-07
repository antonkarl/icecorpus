var conmenus=new Object();
var conleafs=new Array();

function addConMenu( label, suggestions ){
	conmenus[label]=new function(){
		this.suggestions = suggestions;
	}
}


function addConLeaf(suggestion,before,label,word){
//	alert(label);
	
	conleaf=new Object();
	conleaf.suggestion=suggestion;
	conleaf.before=before;
	conleaf.label=label;
	conleaf.word=word;
	
	conleafs.push(conleaf);
}
//addConLeaf(suggestion,before,label,word);
addConLeaf("&lt; (NP-SBJ *con*)",true,"NP-SBJ","*con*");
addConLeaf("&lt; (NP-SBJ *exp*)",true,"NP-SBJ","*exp*");
addConLeaf("&lt; (NP-SBJ *arb*)",true,"NP-SBJ","*arb*");
addConLeaf("&lt; (NP-SBJ *pro*)",true,"NP-SBJ","*pro*");
addConLeaf("&lt; (TO *)",true,"TO","*");
addConLeaf("&lt; (WADVP 0)",true,"WADVP","0");
addConLeaf("&lt; (WNP 0)",true,"WNP","0");
addConLeaf("&lt; (WQP 0)",true,"WQP","0");
addConLeaf("&lt; (WADJP 0)",true,"WADJP","0");
addConLeaf("&lt; (WPP 0)",true,"WPP","0");
addConLeaf("&lt; (C 0)",true,"C","0");
addConLeaf("&lt; (P 0)",true,"P","0");
// alert( conleafs[0].label );

	
defaultsPhrases=["VBPI","VBPS","VBDI","VBDS","VBI","VAN","VBN","VB"];

rootGroup=["IP-SUB","IP-MAT","IP-INF","IP-IMP","CP-QUE","QTP","FRAG"];
for(i=0; i<rootGroup.length; i++){
   addConMenu(rootGroup[i],rootGroup);
}

adjpGroup=["ADJP","ADJX","NP-MSR","QP","NP","ADVP"];
for(i=0; i<adjpGroup.length; i++){
   addConMenu(adjpGroup[i],adjpGroup);
}

npGroup=["NP-SBJ","NP-OB1","NP-OB2","NP-PRD","NP-POS","NP-PRN","NP","NX","NP-MSR","NP-TMP","NP-ADV","NP-COM","NP-CMP","NP-DIR","NP-ADT","NP-VOC","QP"];
for(i=0; i<npGroup.length; i++){
   addConMenu(npGroup[i],npGroup);
}


advpGroup=["PP","ADVP","ADVP-TMP","ADVP-LOC","ADVP-DIR","NP-MSR","NP-ADV"];
for(i=0; i<advpGroup.length; i++){
   addConMenu(advpGroup[i],advpGroup);
}

verbGroup=["VBPI","VBPS","VBDI","VBDS","VBI","VAN","VBN","VB"];
for(i=0; i<verbGroup.length; i++){
   addConMenu(verbGroup[i],verbGroup);
}

rpGroup=["RP","P","ADV","ADVR","ADVS","ADJ","ADJR","ADJS","C","CONJ","ALSO"];
for(i=0; i<rpGroup.length; i++){
   addConMenu(rpGroup[i],rpGroup);
}

wpGroup=["WADVP","WNP","WPP","WQP","WADJP"];
for(i=0; i<wpGroup.length; i++){
   addConMenu(wpGroup[i],wpGroup);
}

cpGroup=["CP-THT","CP-THT-PRN","CP-ADV","CP-CMP"];
for(i=0; i<cpGroup.length; i++){
   addConMenu(cpGroup[i],cpGroup);
}


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

function loadContextMenu( nodeId ){

	nodeIndex = getIndex( $("#"+nodeId) );
	indexSep="";
	indexString="";
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
	
	if( nodeIndex > -1 ){
		lastindex=Math.max(nodelabel.lastIndexOf("-"),nodelabel.lastIndexOf("="));
		indexSep = nodelabel.charAt(lastindex);
		nodelabel = nodelabel.substr(0, getLabel( $(node)).length-2 );									
		indexString = indexSep+""+nodeIndex;
	}

	//html=$("");

	// alert(nodelabel);

//	html+="<div class='conMenuItem'><a href='#fixedleaf:NP-SBJ:*con*:"+nodeId+"'>&lt; NP-SBJ *con*</a></div>";

	$("#conLeft").empty();	
	$("#conLeft").append($("<div class='conMenuHeading'>Label</div>"));	
	
	if (/-[NADG]$/.test( nodelabel )) {
		caseTags=["N","NS","NPR","NPRS","PRO","D","NUM","ADJ","ADJR","ADJS","Q","QR","QS"];		
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
					// alert(nodeId + " " + suggestion);
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
	
		suggestions = defaultsPhrases;
		if (conmenus[nodelabel] != null) {
			suggestions = conmenus[nodelabel].suggestions;
		}
		
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
	
//alert("x"+nodelabel+"x");	

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
//	
//	setNodeLabel(nodeId,"sss",true);
}




function doConLeaf(idx,conleaf,nodeId){
		return function(){
			//e = window.event;
			//var elementId = (e.target || e.srcElement).id;
			// suggestion = "" + $(this).text();
			 //alert(elementId);
			//(before,label,word,targetId,fixed)
			makeLeaf(conleaf.before, conleaf.label, conleaf.word, nodeId, true);
			hideContextMenu();
		}
}
