/*
 *  Displays a context menu for setting case extensions according to
 *  the IcePaHC annotation scheme
 *  caseTags indicates which tags should be interpreted as case tags
 *  for this purpose
 */ 
var displayCaseMenu = true;
var caseTags=["N","NS","NPR","NPRS","PRO","D","NUM","ADJ","ADJR","ADJS","Q","QR","QS"];

/* extensions are treated as not part of the label for various purposes, 
 * they are all binary, and they show up in the toggle extension menu  
 */
var extensions=["-SPE","-PRN","-SBJ","-LFD","-RSP","-XXX","-ZZZ"];

/*
 * Phrase labels in this list (including the same ones with indices and
 * extensions) get a different background color so that the annotator can
 * see the "floor" of the current clause
 */
var ipnodes=["IP-SUB","IP-MAT","IP-IMP","IP-INF","IP-PPL","RRC"];

/*
 * Keycode is from onKeyDown event.
 * This can for example be tested here:
 * http://www.asquare.net/javascript/tests/KeyCode.html
 */
function customCommands(){
	addCommand(65,"leafafter"); // a
	addCommand(66,"leafbefore"); // b
	addCommand(69,"setlabel",["CP-ADV","CP-CMP"]); //e
	addCommand(88,"makenode","XP"); // x
	addCommand(67,"coindex"); // c
	addCommand(82,"setlabel",["CP-REL","CP-FRL","CP-CAR","CP-CLF"]); // r
	addCommand(83,"setlabel",["IP-SUB","IP-MAT","IP-IMP"]); // s
	addCommand(86,"setlabel",["IP-SMC","IP-INF","IP-INF-PRP"]); // v
	addCommand(84,"setlabel",["CP-THT","CP-THT-PRN","CP-DEG","CP-QUE"]); // t
	addCommand(71,"setlabel",["ADJP","ADJP-SPR","NP-MSR","QP"]); // g
	addCommand(70,"setlabel",["PP","ADVP","ADVP-TMP","ADVP-LOC","ADVP-DIR"]); // f
//	addCommand(49,"redo"); // 1
	addCommand(50,"setlabel",["NP","NP-PRN","NP-POS","NP-COM"]); // 2
//	addCommand(51,"makenode","NP","NP-PRD","NP-POS"); // 3
	addCommand(52,"toggleextension","-PRN"); // 4
        addCommand(53,"toggleextension","-SPE"); // 5
	addCommand(81,"setlabel",["CONJP","ALSO","FP"]); // q
	addCommand(87,"setlabel",["NP-SBJ","NP-OB1","NP-OB2","NP-PRD"]); // w
	addCommand(68,"prunenode"); // d
	addCommand(90,"undo"); // z
	addCommand(76,"rename"); // l
//	addCommand(188,"clearselection"); // <
	addCommand(32,"clearselection"); // spacebar
//	addCommand(78, "makenode","XP"); // n    
}


/*
 * Default phrase label suggestions in context menu 
 */
var defaultConMenuGroup = ["VBPI","VBPS","VBDI","VBDS","VBI","VAN","VBN","VB"];

/**
 * Phrase labels that are suggested in context menu when one of the other ones is set
 */
function customConMenuGroups(){
	addConMenuGroup( ["IP-SUB","IP-MAT","IP-INF","IP-IMP","CP-QUE","QTP","FRAG"] );
	addConMenuGroup( ["ADJP","ADJX","NP-MSR","QP","NP","ADVP","IP-PPL"] );
	addConMenuGroup( ["NP-SBJ","NP-OB1","NP-OB2","NP-PRD","NP-POS","NP-PRN","NP","NX","NP-MSR","NP-TMP","NP-ADV","NP-COM","NP-CMP","NP-DIR","NP-ADT","NP-VOC","QP"] );
	addConMenuGroup( ["PP","ADVP","ADVP-TMP","ADVP-LOC","ADVP-DIR","NP-MSR","NP-ADV"] );
	addConMenuGroup( ["VBPI","VBPS","VBDI","VBDS","VBI","VAN","VBN","VB","HV"] );
	addConMenuGroup( ["HVPI","HVPS","HVDI","HVDS","HVI","HV"] );	
	addConMenuGroup( ["RP","P","ADV","ADVR","ADVS","ADJ","ADJR","ADJS","C","CONJ","ALSO"] );
	addConMenuGroup( ["WADVP","WNP","WPP","WQP","WADJP"] );
	addConMenuGroup( ["CP-THT","CP-QUE","CP-REL","CP-DEG","CP-ADV","CP-CMP"] );
}

/*
 * Context menu items for "leaf before" shortcuts
 */
function customConLeafBefore(){
	addConLeafBefore( "NP-SBJ", "*con*");
	addConLeafBefore( "NP-SBJ", "*exp*");
	addConLeafBefore( "NP-SBJ", "*arb*");
	addConLeafBefore( "NP-SBJ", "*pro*");
	addConLeafBefore( "TO", "*");
	addConLeafBefore( "WADVP", "0");
	addConLeafBefore( "WNP", "0");
	addConLeafBefore( "WQP", "0");
	addConLeafBefore( "WADJP", "0");
	addConLeafBefore( "WPP", "0");
	addConLeafBefore( "C", "0");
	addConLeafBefore( "P", "0");
	addConLeafBefore( "CODE", "*XXX*");	
	addConLeafBefore( "CODE", "*TTT*");
	addConLeafBefore( "CODE", "*SSS*");	
}
