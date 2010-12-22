startnode=null;
endnode=null;
var mousenode=null;
var undostack=new Array();
var redostack=new Array();
var commands=new Object();

$(document).ready(function() {
	resetIds();
	assignEvents(); 
	$("#debugpane").empty();
	$("#debugpane").append( toLabeledBrackets($("#editpane")) );
});


function addCommand( keycode, type, label ){
	commands[keycode]=new function(){
		this.type = type;
		this.label=label;
	}
}

function stackTree(){
	undostack.push( $("#editpane").html() );
}

function redo(){
	var nextstate = redostack.pop();
	if( !(nextstate == undefined) ){
		currentstate=$("#editpane").html();
		undostack.push(currentstate);
		$("#editpane").empty();
		$("#editpane").append(nextstate);
		clearSelection();		
		$(".snode").mousedown(handleNodeClick);
	}
}

function undo(){	

	var prevstate = undostack.pop();
//	alert("undo: "+prevstate);

	if( !(prevstate == undefined) ){
		// alert(prevstate);
		currentstate=$("#editpane").html();
		redostack.push(currentstate);

		$("#editpane").empty();
		$("#editpane").append(prevstate);
		clearSelection();
		$(".snode").mousedown(handleNodeClick);
	}
}

function assignEvents(){
	addCommand(69,"makenode","IP-INF"); //e
	addCommand(88,"makenode","XP"); // x
	addCommand(67,"makenode","CP-CMP"); // c
	addCommand(82,"makenode","CP-REL"); // r
	addCommand(83,"makenode","NP-SBJ"); // s
	addCommand(49,"makenode","NP-OB1"); // 1
	addCommand(50,"makenode","NP-OB2"); // 2
	addCommand(51,"makenode","NP-PRD"); // 3
	addCommand(81,"undo"); // q
	addCommand(87,"redo"); // w
	addCommand(68,"prunenode"); // d
	addCommand(90,"clearselection"); // z

	document.body.onkeydown = function(e){	

		if( commands[e.keyCode] !=null ){
			type = commands[e.keyCode]["type"];
			label = commands[e.keyCode]["label"];
			if( type=="makenode") {
				if( e.shiftKey ){
					setLabel( label );
				}
				else {
					makeNode(label);
				}
			}	
			else if (type=="undo"){
				undo();
			}
			else if (type=="redo"){
				redo();
			}
			else if (type=="prunenode"){
				pruneNode();
			}
			else if (type=="clearselection"){
				clearSelection();
			}
		}

	}	
	$(".snode").mousedown(handleNodeClick);
/*
	$(".snode>.snode").mouseover(
	    function(e) {
		    e.stopPropagation();
		    updateMouseNode(this);
		}
	);
*/
}

/*
function updateMouseNode(node){	
	if( mousenode ){
		$(mousenode).css('color','black');
	}
	mousenode=node;
	$(mousenode).css('color','red');
	$(mousenode).children().css('color','black');
}
*/

function handleNodeClick(e){
	  		e = e || window.event;
	  		var elementId = (e.target || e.srcElement).id;
			// alert(e.button);
			if( e.button == 2 ){
				if( startnode ){
					moveNode( elementId ); 
				}
			}
			else {
				// leftclick
				selectNode(elementId);
			}
			e.stopPropagation();
}

function selectNode(nodeId){
	var node = document.getElementById(nodeId);
	if( node == startnode ){
	     startnode=null;
	     if(endnode){
		startnode=endnode;
		endnode=null;
	     }
	}
	else if (startnode == null ){
	     startnode=node;
	}
	else {
		if( node==endnode){
		     endnode=null;
		}
		else {
		     endnode=node;
		}
	}

	updateSelection();
}

/*
function selectEndnode(node){
	doSelectNode( document.getElementById(node) );
}
*/

function clearSelection(){
	startnode=null; endnode=null;
	resetIds();
	updateSelection();
}

function updateSelection(){

	document.getElementById("labsel1").innerHTML="null";
	document.getElementById("labsel2").innerHTML="null";
	if( startnode ){
		document.getElementById("labsel1").innerHTML=startnode.id;
		//startnode.setAttribute('class','snodesel');
	}
	if( endnode ){
		document.getElementById("labsel2").innerHTML=endnode.id;
		//endnode.setAttribute('class','snodesel');
	}

	// update selection display
	$('.snode').removeClass('snodesel');
	if( startnode )
		$("#"+startnode.id).addClass('snodesel');
	if( endnode )
		$("#"+endnode.id).addClass('snodesel');
	
}

function isPossibleTarget(node){

	// cannot move under a tag node
	if( $("#"+node).children().first().is("span") ){
		return false;
	}

	return true;
}


function moveNode(targetParent){
	if( ! isPossibleTarget(targetParent) ){
		// can't move under a tag node		
	}
	else if( $("#"+startnode.id).parent().children().length == 1 ){
		// alert("cant move an only child");
	}
	else if( $("#"+targetParent).parents().is( "#"+startnode.id ) ){ 
		// alert("can't move under one's own child");
        } // move up if moving to a node that is already my parent	
	else if( $("#"+startnode.id).parents().is( "#"+targetParent ) ){
		// alert( startnode.id );
		var firstchildId = $("#"+startnode.id).parent().children().first().closest("div").attr("id");
		var lastchildId = $("#"+startnode.id).parent().children().last().closest("div").attr("id");
		
		if( startnode.id == firstchildId ){
			stackTree();
			$("#"+startnode.id).insertBefore( $("#"+targetParent).children().filter( $("#"+startnode.id).parents() ) );		
		}
		else if( startnode.id == lastchildId ){
			stackTree();
 			$("#"+startnode.id).insertAfter( $("#"+targetParent).children().filter( $("#"+startnode.id).parents() ) );		
		}
		else {
			// alert("cannot move from this position");
		}
	} // otherwise move under my sister
	else {
		if( parseInt( startnode.id.substr(2) ) > parseInt( targetParent.substr(2) ) ){
			stackTree();
			$("#"+startnode.id).appendTo("#"+targetParent);	
		}
		else {
			stackTree();
			$("#"+startnode.id).insertBefore( $("#"+targetParent).children().first() );	
		}
	}
	clearSelection();
}

function setLabel(label){
	if( !isPossibleTarget(startnode.id) ){
		return;	
	}

	stackTree();
	$("#"+startnode.id).contents().filter(function() {
  			return this.nodeType == 3;
		}).first().replaceWith(label);
	clearSelection();
//  && $(this).is(":contains('Some Label ')"
}

function makeNode(label){
	// check if something is selected
	if( !startnode ){
		return;
	} 
	// FIX, note one node situation
	//if( (startnode.id == "sn0") || (endnode.id == "sn0") ){
		// can't make node above root
	//	return;
	//}
	// make end = start if only one node is selected
	if( !endnode ){
		// if only one node, wrap around that one
		stackTree();
		$("#"+startnode.id).wrapAll('<div class="snode">'+label+'</div>');
	}
	else {
		if( parseInt(startnode.id.substr(2)) > parseInt(endnode.id.substr(2)) ){
			// reverse them if wrong order
			temp = startnode;	
			startnode = endnode;
			endnode = temp;
		} 

		// otherwise, collect startnode and its sister up until endnode
		stackTree();
		$("#"+startnode.id).add($("#"+startnode.id).nextUntil("#"+endnode.id)).add("#"+endnode.id).wrapAll('<div class="snode">'+label+'</div>');	
	}

	startnode=null; endnode=null;
	resetIds();
	updateSelection();
}

function pruneNode(){
	if( startnode && !endnode ){
		if( ! isPossibleTarget(startnode.id) ){
			return;
		}

		if( startnode.id == "sn0" ){
			return;
		}

//		$("#"+startnode.id+">*:text").remove();
		stackTree();
		$("#"+startnode.id).replaceWith( $("#"+startnode.id+">*") );		
		startnode=null;
		endnode=null;
		resetIds();
 	        updateSelection();

/*
		startnode.removeChild(startnode.firstChild);
		while (startnode.firstChild)
		{  
		    startnode.parentNode.insertBefore(startnode.firstChild, startnode);
		}
		startnode.parentNode.removeChild(startnode);

		startnode=null;
		endnode=null;
 	        updateSelection();
		resetIds();
*/
	}
}

function resetIds(){
	var snodes = $(".snode"); // document.getElementsByClassName("snode");
	for( i=0; i<snodes.length; i++ ){
		snodes[i].id="sn"+i;
		//snodes[i].onmousedown=null;
                //snodes[i].onmousedown=handleNodeClick;
	}

	// assignEvents();
}

function toLabeledBrackets( node ){		
	// return recurseNode(node,"");
	out=node.clone();		
	out.find(".snode").before("(");
	out.find(".snode").after(")");
	out.find(".wnode").before(" ");
	
	return out.text();
}

