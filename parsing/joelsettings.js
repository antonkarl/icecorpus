//Joel Wallenberg's modifications of:

// Copyright (c) 2011, 2012 Anton Karl Ingason, Aaron Ecay

// This file is part of the Annotald program for annotating
// phrase-structure treebanks in the Penn Treebank style.

// This file is distributed under the terms of the GNU General
// Public License as published by the Free Software Foundation, either
// version 3 of the License, or (at your option) any later version.

// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
// General Public License for more details.

// You should have received a copy of the GNU Lesser General Public
// License along with this program.  If not, see
// <http://www.gnu.org/licenses/>.


/*
 * Whether to include detailed information on key and mouse actions in the
 * event log
 */
// TODO: add to user manual
var logDetail = true;

/*
 * Displays a context menu for setting case extensions according to
 * the IcePaHC annotation scheme.
 *
 * caseTags indicates which tags bear case indicators; casePhrases indicates
 * which phrasal categories case pertains to (though they themselves are not
 * marked)
 */
var displayCaseMenu = true; // This feature is inoperative, pending modularization
var caseTags = ["N","NS","NPR","NPRS",
                "PRO","D","NUM",
                "ADJ","ADJR","ADJS",
                "Q","QR","QS","WPRO","WD","VAN"];
var casePhrases = ["NP","QP","ADJP"];
var caseMarkers = ["N", "A", "D", "G"];
/*
 * Which labels are barriers to recursive case assignment.
 */
var caseBarriers = ["IP","CP","NP"];

/*
 * These two functions should return true if the string argument is a valid
 * label for a branching (-Phrase-) and non-branching (-Leaf-) label, and
 * false otherwise.  The utility function basesAndDashes is provided.  It
 * takes two arguments, a list of base tags and a list of dash tags.  It
 * returns a function suitable for assigning to one of these variables. The
 * recommended way to accomplish this, however, is to use the waxeye parser
 * generator.  Samples and documentation for this method have yet to be
 * written.
 */
var testValidPhraseLabel = undefined;
var testValidLeafLabel   = undefined;

/*
 * Extensions are treated as not part of the label for various purposes, they
 * are all binary, and they show up in the toggle extension menu.  There are 3
 * classes of extensions: those that apply to leaf nodes, those that apply to
 * clausal nodes (IP and CP), and those that apply to non-leaf, non-clause
 * nodes.
 */
var extensions        = ["SBJ","RSP","LFD","PRN","SPE","XXX"];
var clause_extensions = ["RSP","LFD","SBJ","PRN","SPE","XXX"];
var leaf_extensions   = [];

/*
 * Phrase labels in this list (including the same ones with indices and
 * extensions) get a different background color so that the annotator can
 * see the "floor" of the current clause
 */
var ipnodes = ["IP-SUB","IP-MAT","IP-IMP","IP-INF","IP-PPL","RRC","IP-SMC"];

// Types of comments.
// Comments are nodes of the form (CODE {XXX:words_words_words})
// If "XXX" is in the following list, then when editing the contents of the
// comment with one of the editing functions (TODO: list), a dialog box will
// appear allowing the comment to be edited as text.
var commentTypes = ["COM", "TODO", "MAN"];

/*
 * Keycode is from onKeyDown event.
 * This can for example be tested here:
 * http://www.asquare.net/javascript/tests/KeyCode.html
 */
function customCommands() {
    addCommand({ keycode: 65 }, leafAfter ); // a
    addCommand({ keycode: 66 }, leafBefore); // b
    addCommand({ keycode: 69 }, setLabel, ["CP-ADV","CP-CMP"]); //e
    addCommand({ keycode: 88 }, makeNode, "XP"); // x
    addCommand({ keycode: 88, shift: true }, setLabel, ["XP"]);
    addCommand({ keycode: 67 }, coIndex); // c
    addCommand({ keycode: 82 }, setLabel, ["CP-REL","CP-FRL","CP-CAR",
                                           "CP-CLF"]); // r
    addCommand({ keycode: 83 }, setLabel, ["IP-SUB","IP-MAT","IP-IMP"]); // s
    addCommand({ keycode: 86 }, setLabel, ["IP-SMC","IP-PPL","IP-INF",
                                           "IP-INF-PRP"]); // v
    addCommand({ keycode: 84 }, setLabel, ["CP-THT","CP-THT-PRN","CP-DEG",
                                           "CP-QUE"]); // t
    addCommand({ keycode: 71 }, setLabel, ["ADJP","ADJP-SPR","NP-MSR",
                                           "QP"]); // g
    addCommand({ keycode: 70 }, setLabel, ["PP","ADVP","ADVP-TMP","ADVP-LOC",
                                           "ADVP-DIR"]); // f
    addCommand({ keycode: 50 }, setLabel, ["NP","NP-PRN","NP-POS",
                                           "NP-COM"]); // 2
    addCommand({ keycode: 50, shift: true }, splitWord); // 2
    addCommand({ keycode: 52 }, toggleExtension, "PRN"); // 4
    addCommand({ keycode: 53 }, toggleExtension, "SPE"); // 5
    addCommand({ keycode: 81 }, setLabel, ["CONJP","ALSO","FP"]); // q
    addCommand({ keycode: 87 }, setLabel, ["NP-SBJ","NP-OB1","NP-OB2",
                                           "NP-PRD"]); // w
    addCommand({ keycode: 68 }, pruneNode); // d
    addCommand({ keycode: 90 }, undo); // z
    addCommand({ keycode: 76 }, editNode); // l
    addCommand({ keycode: 32 }, clearSelection); // spacebar
    addCommand({ keycode: 192 }, toggleLemmata); // `
    addCommand({ keycode: 76, ctrl: true }, displayRename); // ctrl + l

    addCommand({ keycode: 191 }, search); // forward slash


    // TODO: remove this
    // An example of a context-sensitive label switching command.  If
    // neither NP or PP is the POS, the NP value (first in the dictionary)
    // is chosen by default.
    // addCommand({ keycode: 123 } , setLabel, { NP: ["NP-SBJ", "NP-OB1", "NP-OB2"],
    //                                           PP: ["PP-SBJ", "PP-OB1", "PP-OB2"]});
}
    addCommand({ keycode: 83, ctrl: true }, save);

/*
 * Default phrase label suggestions in context menu
 */
var defaultConMenuGroup = ["VBPI","VBPS","VBDI","VBDS","VBI","VAN","VAG","VBN","VB","N","ADJ"];

/*
 * Phrase labels that are suggested in context menu when one of the other ones
 * is set
 */
function customConMenuGroups() {
    addConMenuGroup( ["IP-SUB","IP-MAT","IP-INF","IP-IMP","IP-SMC","IP-PPL","RRC","CP-QUE","QTP","FRAG"] );
    addConMenuGroup( ["ADJP","ADJX","NP-MSR","QP","NP","ADVP"] );
    addConMenuGroup( ["NP-SBJ","NP-OB1","NP-OB2","NP-PRD","NP-POS","NP-PRN",
                      "NP","NX","WNP","NP-MSR","NP-TMP","NP-ADV","NP-COM","NP-CMP",
                      "NP-DIR","NP-ADT","NP-VOC","QP"] );
    addConMenuGroup( ["PP","WPP","ADVP","ADVP-TMP","ADVP-LOC","ADVP-DIR","NP-MSR","NP-ADV"] );
    //joel modified:
    addConMenuGroup( ["ADJ","ADJR","ADJS","N","NS","VAN","ADV","Q"] );
    addConMenuGroup( ["HVPI","HVPS","HVDI","HVDS","HVI","HV","HVN","HAN"] );
    addConMenuGroup( ["BEPI","BEPS","BEDI","BEDS","BEI","BE","BEN"] );
    addConMenuGroup( ["RDPI","RDPS","RDDI","RDDS","RDI","RD","RDN"] );
    addConMenuGroup( ["VBPI","VBPS","VBDI","VBDS","VBI","VAN","VAG","VBN","VB","HV","BE","RD","MD","MDDI","MDPI"] );
    //joel modified above

    addConMenuGroup( ["RP","P","ADV","ADVR","ADVS","C","CONJ","ALSO","BEPI"] );
    addConMenuGroup( ["WADVP","WNP","WPP","WQP","WADJP"] );
    addConMenuGroup( ["CP-THT","CP-QUE","CP-REL","CP-DEG","CP-ADV","CP-CMP"] );
    
//joel modified:
    addConMenuGroup( ["N","NS","NPR","NPRS","PRO","EX","MAN","OTHER","OTHERS","WPRO"] );
    addConMenuGroup( ["Q","QR","QS","PRO","WPRO","WD"] );
    addConMenuGroup( [".",","] );
}

/*
 * Context menu items for "leaf before" shortcuts
 */
function customConLeafBefore() {
    addConLeafBefore("NP-SBJ" , "*con*"     );
    addConLeafBefore("NP-SBJ" , "*pro*"     );
    addConLeafBefore("NP-SBJ" , "*arb*"     );
    addConLeafBefore("NP-SBJ" , "*exp*"     );
    addConLeafBefore("WNP"      , "0"         );
    addConLeafBefore("WADVP"      , "0"         );
    addConLeafBefore("C"      , "0"         );
    addConLeafBefore("CODE"   , "{COM:XXX}" );
}

// An example of a CSS rule for coloring a syntactic tag.  The styleTag
// function takes care of setting up a (somewhat complex) CSS rule that
// applies the given style to any node that has the given label.  Dash tags
// are accounted for, i.e. NP also matches NP-FOO (but not NPR).  The
// lower-level addStyle() function adds its argument as CSS code to the
// document.
// styleTag("NP", "color: red");

// An example of a CSS rule for coloring a dash tag.  Similarly to the
// styleTag function, styleDashTag takes as an argument the name of a dash tag
// and CSS rule(s) to apply to it.

styleDashTag("FLAG", "color: red");