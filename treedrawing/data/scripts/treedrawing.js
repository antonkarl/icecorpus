startnode=null;
endnode=null;
var mousenode=null;
var undostack=new Array();
var redostack=new Array();
var commands=new Object();


var name = "#floatMenu";  
var menuYloc = null;  

String.prototype.startsWith = function(str){
    return (this.substr(0,str.length) === str);
}

$(document).ready(function() {
	resetIds();
	assignEvents(); 
	$("#debugpane").empty();
	// $("#debugpane").append( wnodeString($("#editpane")) );

    // make menu float
    menuYloc = parseInt($(name).css("top").substring(0,$(name).css("top").indexOf("px")))  
    $(window).scroll(function () {  
        var offset = menuYloc+$(document).scrollTop()+"px";  
        $(name).animate({top:offset},{duration:500,queue:false});  
    });  

    // inital highlight of IPs
    var snodes = $(".snode"); 
    for( i=0; i<snodes.length; i++ ){

		text = $("#"+snodes[i].id).contents().filter(function() {
  			return this.nodeType == 3;
		}).first().text();
		if( trim(text).startsWith("IP-SUB") || trim(text).startsWith("IP-MAT") || trim(text).startsWith("IP-IMP") ){
			$("#"+snodes[i].id).addClass('ipnode');
		}
    }

    // floatmenu ready

   // setup context menu
				// Show menu when #myDiv is clicked
				/* $(".wnode").contextMenu({
					menu: 'myMenu'
				},
					function(action, el, pos) {
					alert(
						'Action: ' + action + '\n\n' +
						'Element ID: ' + $(el).attr('id') + '\n\n' + 
						'X: ' + pos.x + '  Y: ' + pos.y + ' (relative to element)\n\n' + 
						'X: ' + pos.docX + '  Y: ' + pos.docY+ ' (relative to document)'
						);
				}); */



});

function connectContextMenu(){
	// XXX 
}

function disableContextMenu(){
	// XXX
}

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

function save(){
	// alert("saving");

	var tosave = toLabeledBrackets($("#editpane"));
	$.post("/doSave", {trees: tosave});
	
}

function assignEvents(){
	addCommand(65,"leafafter"); //e
	addCommand(66,"leafbefore"); //e

	addCommand(88,"makenode","XP"); // x
	addCommand(67,"setlabel",["CP-ADV","CP-CMP"]); // c
	addCommand(82,"setlabel",["CP-REL","CP-FRL","CP-CAR"]); // r
	addCommand(83,"setlabel",["IP-SUB","IP-MAT","IP-IMP"]); // s
	addCommand(86,"setlabel",["IP-SMC","IP-INF","IP-INF-PRP"]); // v
	addCommand(84,"setlabel",["CP-THT","CP-THT-PRN","CP-QUE"]); // t
	addCommand(71,"setlabel",["PP","ADVP","ADVP-TMP","ADVP-LOC","ADVP-DIR"]); // g
//	addCommand(49,"makenode","NP-OB1"); // 1
//	addCommand(50,"makenode","NP-OB2"); // 2
//	addCommand(51,"makenode","NP-PRD"); // 3
	addCommand(52,"redo"); // 4
	addCommand(81,"undo"); // q
	addCommand(87,"setlabel",["NP-SBJ","NP-OB1","NP-OB2","NP"]); // w
	addCommand(68,"prunenode"); // d
	addCommand(90,"clearselection"); // z
	addCommand(76,"rename"); // x
//	addCommand(78, "makenode","XP"); // n
        //78 n

	document.body.onkeydown = handleKeyDown;	
	$(".snode").mousedown(handleNodeClick);
	$("#butsave").mousedown(save);
	$("#butundo").mousedown(undo);
	$("#butredo").mousedown(redo);

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

function handleKeyDown(e){	

		// alert(e.keyCode);

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
			else if (type=="rename"){
				//e.stopPropagation();
				displayRename();
				e.preventDefault();
				// e.stopPropagation();
			}
			else if (type=="setlabel"){
				setLabel(label);
			}
			else if (type=="leafbefore"){
				leafBefore();
			}
			else if (type=="leafafter"){
				leafAfter();
			}
		}

	}

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
/*
	if(node == "s01"){
		return false;
	}
*/
	return true;
}

function currentText(){
	return wnodeString($("#editpane"));
}

function moveNode(targetParent){
	textbefore = currentText();

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
			if( currentText() != textbefore ){undo();redostack.pop();}
		}
		else if( startnode.id == lastchildId ){
			stackTree();
 			$("#"+startnode.id).insertAfter( $("#"+targetParent).children().filter( $("#"+startnode.id).parents() ) );		
			if( currentText() != textbefore ){undo();redostack.pop();}
		}
		else {
			// alert("cannot move from this position");
		}
	} // otherwise move under my sister
	else {		
//		if( parseInt( startnode.id.substr(2) ) >  parseInt( targetParent.substr(2) ) ){
		if( parseInt( startnode.id.substr(2) ) > parseInt( targetParent.substr(2) ) ){
			//if( $("#"+startnode.id).siblings().is("#"+startnode.id+"~.snode") ){
				stackTree();
				$("#"+startnode.id).appendTo("#"+targetParent);	
				if( currentText() != textbefore ){undo();redostack.pop();}
			//}
		}
		else if( parseInt( startnode.id.substr(2) ) <  parseInt( targetParent.substr(2) ) ) {
			stackTree();
			$("#"+startnode.id).insertBefore( $("#"+targetParent).children().first() );	
			if( currentText() != textbefore ){undo();redostack.pop();}
		}
	}
	clearSelection();
}

function trim( s ){
	return s.replace(/^\s*/, "").replace(/\s*$/, "");
}

function leafBefore(){
	makeLeaf(true);
}

function leafAfter(){
	makeLeaf(false);
}


function makeLeaf(before){
	if( startnode && !endnode ){
		document.body.onkeydown = null;	
		editor=$("<div id='leafeditor' class='snode'><input id='leafphrasebox' class='labeledit' type='text' value='WADVP' /> <input id='leaftextbox' class='labeledit' type='text' value='0' /></div>")

  	        stackTree();

		if( before ){
			editor.insertBefore(startnode);
		}
		else {
			editor.insertAfter(startnode);
		}

		$("#leafphrasebox,#leaftextbox").keydown(function(event) {
			if(event.keyCode == '13'){			   
			   newphrase = $("#leafphrasebox").val().toUpperCase()+" ";
			   newtext = $("#leaftextbox").val();

  			   $("#leafeditor").replaceWith( "<div class='snode'>"+ newphrase+" <span class='wnode'>"+newtext+"</span></div>" );

			   startnode=null; endnode=null;
			   resetIds();
			   updateSelection();
			   document.body.onkeydown = handleKeyDown;	
			}

		});

		
		setTimeout(function(){ $("#leafphrasebox").focus(); }, 10);

		// $("#leafphrasebox").val("xxx");
		//startnode=null; endnode=null;
		//resetIds();
		//updateSelection();
		//document.body.onkeydown = handleKeyDown;

	}

//		alert( oldtext );
//		clearSelection();		
//		$("#renamebox").blur();
//  		e = e || window.event;
//		e.stopPropagate();
}

function displayRename(){
	if( startnode && !endnode ){
		document.body.onkeydown = null;	
		oldtext = $("#"+startnode.id).contents().filter(function() {
  			return this.nodeType == 3;
		}).first().text();
		stackTree();
		$("#"+startnode.id).contents().filter(function() {
  			return this.nodeType == 3;
		}).first().replaceWith("<input id='renamebox' class='labeledit' type='text' />");	
		$("#renamebox").keydown(function(event) {
			if(event.keyCode == '13'){			   
			   newtext = $("#renamebox").val().toUpperCase()+" ";
  			   $("#renamebox").replaceWith( newtext );
			   if( newtext == oldtext ){ undo(); redostack.pop(); }
				startnode=null;
				//endnode=null;
				//resetIds();
				updateSelection();
			   	document.body.onkeydown = handleKeyDown;	
			}
		});
//		alert( oldtext );
//		clearSelection();		
//		$("#renamebox").blur();
//  		e = e || window.event;
//		e.stopPropagate();


		// setTimeout(function(){ $("#renamebox").focus(); }, 10);
//		$("#renamebox").focus();
		$("#renamebox").val( trim(oldtext) );		
		$("#renamebox").select(); 

	}
}

function setLabel(label){
	if( !isPossibleTarget(startnode.id) ){
		return;	
	}

	stackTree();
	textnode = $("#"+startnode.id).contents().filter(function() {
  			return this.nodeType == 3;
		}).first();
	oldlabel=trim(textnode.text());
//	newlabel=label[0];
	for( i=0; i<label.length; i++ ){
		if( label[i] == oldlabel ){
		   if( i<label.length-1 ){
		      textnode.replaceWith(label[i+1]+" ");
		      return;
		   }
		   else {
		      textnode.replaceWith(label[0]+" ");
		      return;
		   }		   
		}
	}
        textnode.replaceWith(label[0]+" ");

// 	textnode.replaceWith(label[0]+" ");
//	clearSelection();
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
		$("#"+startnode.id).wrapAll('<div xxx="newnode" class="snode">'+label+' </div>');
	}
	else {
		if( parseInt(startnode.id.substr(2)) > parseInt(endnode.id.substr(2)) ){
			// reverse them if wrong order
			temp = startnode;	
			startnode = endnode;
			endnode = temp;
		} 

		// check if they are really sisters
		//if( $("#".startnode.id+"~.snode").is("#"+endnode.id) ){
			// otherwise, collect startnode and its sister up until endnode
			oldtext = currentText();
			stackTree();
			$("#"+startnode.id).add($("#"+startnode.id).nextUntil("#"+endnode.id)).add("#"+endnode.id).wrapAll('<div xxx="newnode" class="snode">'+label+'</div>');	
			// undo if this messed up the text order
			if( currentText() != oldtext ){	undo(); redostack.pop(); }
		//}
	}

	startnode=null; endnode=null;
	
	// toselect = $(".snode[xxx=newnode]").first();	
//	alert(toselect.attr("xxx"));

	resetIds();
	toselect = $(".snode[xxx=newnode]").first();	
	// alert(toselect.attr("id"));

	selectNode( toselect.attr("id") );
	toselect.attr("xxx",null)
	updateSelection();
}

function pruneNode(){
	if( startnode && !endnode ){

		deltext = $("#"+startnode.id).children().first().text();

		// if this is a leaf
		if( deltext == "0" || deltext.charAt(0) == "*" || deltext.charAt(0) == "{" ){
			// it is ok to delete leaf if is empty/trace
			stackTree();
			$("#"+startnode.id).remove();
			startnode=null;
			endnode=null;
			resetIds();
			updateSelection();
			return;
		} // but other leafs are not deleted
		else if( ! isPossibleTarget(startnode.id) ){
			return;
		}
		else if( startnode.id == "sn0" ){
			return;
		}

//		$("#"+startnode.id+">*:text").remove();
		stackTree();
		
		toselect = $("#"+startnode.id+">*").first();
		$("#"+startnode.id).replaceWith( $("#"+startnode.id+">*") );		
		startnode=null;
		endnode=null;
		resetIds();
		selectNode( toselect.attr("id") );
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
		
		
//		$("#"+snodes[i].id).addClass('snodesel');
/*
		text = $("#"+snodes[i].id).contents().filter(function() {
  			return this.nodeType == 3;
		}).first().text();
		if( trim(text).startsWith("IP-SUB") ){
			$("#"+snodes[i].id).addClass('snodesel');
		}
*/

//		snodes[i].="sn"+i;
		//snodes[i].onmousedown=null;
                //snodes[i].onmousedown=handleNodeClick;
	}

	// assignEvents();
}

function wnodeString( node ){
	thenode = node.clone();
	wnodes = thenode.find(".wnode");
	text="";
	for( i=0; i<wnodes.length; i++){
		text = text + wnodes[i].innerHTML + " ";
	}
	return text;
}

function toLabeledBrackets( node ){		
	// return recurseNode(node,"");
	out=node.clone();		
	out.find("#sn0>.snode").after("\n\n");
	out.find("#sn0>.snode").before("( ");
	out.find("#sn0>.snode").after(")");

	out.find(".snode").before("(");
	out.find(".snode").after(")");
	out.find(".wnode").before(" ");
	
	return out.text();
}

