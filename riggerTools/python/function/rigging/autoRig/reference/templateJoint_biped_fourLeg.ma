//Maya ASCII 2018ff09 scene
//Name: templateJoint_biped_fourLeg.ma
//Last modified: Tue, Mar 02, 2021 02:23:59 PM
//Codeset: 1252
requires maya "2018ff09";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201903222215-65bada0e52";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "00A21B7A-4124-AF54-F6F5-1684B636B86E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 67.349941486852344 53.942367993095644 124.46720439594208 ;
	setAttr ".r" -type "double3" -7.538352729602428 27.399999999999931 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "D21F2A39-41A1-3FB4-D7EE-468A77C133F1";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 141.88315321766714;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0.00015817271864193572 40.34365821454638 0 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "A80AC60B-4170-B37F-9D54-18905EF1976E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "937E50F3-4219-6E53-6A46-F38434D06635";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "09540500-4AE7-E8EF-B8DA-E7BB59E4AD17";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "583C032F-48EA-E371-99A8-DFA868D1F638";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "FE989A6E-4BFF-B99D-9242-289D212A0D92";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D2FE2DB8-4C20-8492-B8BA-D8A78B524BA6";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "template_ctrl";
	rename -uid "C4B751F4-4953-3FC6-EC36-C29C8EDB71C4";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "template_ctrlShape" -p "template_ctrl";
	rename -uid "8680F758-49DC-BF2A-BDB4-B9BE793D43E4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".ovrgb" -type "float3" 0.88571429 0.88571429 0.88571429 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 25 0 no 3
		26 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		26
		-10.207552707887748 0 -10.207552707887729
		-10.207552707887748 0 -10.207552707887729
		-5.1037763539438643 0 -15.311329061831604
		-10.207552707887729 0 -15.311329061831604
		0 0 -25.518881769719343
		10.207552707887729 0 -15.311329061831604
		5.1037763539438643 0 -15.311329061831604
		10.207552707887729 0 -10.134965437108015
		15.311329061831604 0 -5.1037763539438643
		15.311329061831604 0 -10.207552707887729
		25.518881769719343 0 0
		15.311329061831604 0 10.207552707887729
		15.311329061831604 0 5.1037763539438643
		10.207552707887748 0 10.207552707887729
		5.1037763539438643 0 15.311329061831604
		10.207552707887729 0 15.311329061831604
		0 0 25.518881769719343
		-10.207552707887729 0 15.311329061831604
		-5.1037763539438643 0 15.311329061831604
		-10.207552707887748 0 10.207552707887729
		-15.311329061831604 0 5.1037763539438643
		-15.311329061831604 0 10.207552707887729
		-25.518881769719343 0 0
		-15.311329061831604 0 -10.207552707887729
		-15.311329061831604 0 -5.1037763539438643
		-10.207552707887748 0 -10.207552707887729
		;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "root" -p "template_ctrl";
	rename -uid "2F41FC42-4C1A-5A98-BA0B-29B9333ECEED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 0 0 1;
createNode joint -n "cog_tmpJnt" -p "root";
	rename -uid "B9E30449-4833-89DA-F06B-87BC7CF7716E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ovc" 15;
	setAttr ".t" -type "double3" 0 45 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 110.89219816924373 0.5817317347463723 1;
	setAttr ".dl" yes;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "COG";
createNode joint -n "spine01_tmpJnt" -p "cog_tmpJnt";
	rename -uid "F7880603-4B75-21DA-F049-68B07229120B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 4 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 115.97688088568215 1.638809891990324 1;
createNode joint -n "spine02_tmpJnt" -p "spine01_tmpJnt";
	rename -uid "0502756E-4215-8C96-1E67-1BA5542513C0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 4 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 124.85510799594223 3.421218434598865 1;
	setAttr ".typ" 6;
createNode joint -n "spine03_tmpJnt" -p "spine02_tmpJnt";
	rename -uid "F000BE14-4AEA-A899-2865-388D420006AD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 4 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 139.05166856595392 2.6655195481726714 1;
createNode joint -n "spine04_tmpJnt" -p "spine03_tmpJnt";
	rename -uid "BBC64937-47AA-AFDA-A555-A9A5BB56121E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 4 0 ;
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766735 0 0 0 0 2.2572056524766735 0
		 0 148.00011790456719 0.43085775501548795 1;
	setAttr ".typ" 6;
createNode joint -n "neck_tmpJnt" -p "spine04_tmpJnt";
	rename -uid "8B96B3A8-4CFF-CFD8-3106-02BD4B844BB0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 6.9131851446357189 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 153.29402538616662 -3.7208063810808136 1;
	setAttr ".typ" 7;
createNode joint -n "head01_tmpJnt" -p "neck_tmpJnt";
	rename -uid "485B7F01-44BA-3E29-EEA4-7FB803A8C9AB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 4.1596844130104529 0.62523741394135124 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766744 0 0 0 0 2.2572056524766739 0
		 0 162.68328855573293 -2.309516956192498 1;
	setAttr ".typ" 8;
createNode joint -n "head02_tmpJnt" -p "head01_tmpJnt";
	rename -uid "12BAFF2F-4A8E-2A16-98CC-71880AAC030D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 10.321006502828638 2.2204460492503131e-16 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766744 0 0 0 0 2.2572056524766739 0
		 0 185.97992277316624 -2.309516956192498 1;
	setAttr ".typ" 8;
	setAttr ".radi" 3;
createNode joint -n "eyeLFT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "FFBE281E-464F-0408-EB50-44B308BEEAC6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.8239219872507531 2.6158880095642019 2.6483026590950898 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "jaw01Lwr_tmpJnt" -p "head01_tmpJnt";
	rename -uid "19A44EE8-4B38-6BA6-9FC9-F4AD7C6A0ED6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.6747740263279888e-16 0.85186845196689376 0.85055887360982263 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -5.6817911712458105e-17 -0.46395345786243802 0.8858595763085072 0 1.0848650946202438e-16 0.8858595763085072 0.46395345786243802 0
		 -2.281527907856237e-09 138.24609308456581 1.2332340767044465 1;
createNode joint -n "jaw02Lwr_tmpJnt" -p "jaw01Lwr_tmpJnt";
	rename -uid "1654BAFF-47F6-09B5-6F04-F9BEA2BEFAB2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.45346939366313e-16 -1.8375419927605208 2.2988962736372129 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661394e-09 134.88585971678842 7.6491683844072185 1;
createNode joint -n "jaw03Lwr_tmpJnt" -p "jaw02Lwr_tmpJnt";
	rename -uid "FE69C916-421F-3CD8-EB00-E3B4CD1A2D1B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3956450219389744e-17 -1.4210854715202004e-14 1.9710502458233852 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661419e-09 134.88585971678845 9.7309712720145338 1;
createNode joint -n "eyeRGT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "D17884E5-4650-4E9A-6124-C3813B90D6BB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.8239219872507531 2.6158880095642019 2.6483026590950898 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eye_tmpJnt" -p "head01_tmpJnt";
	rename -uid "E5776A82-4673-11D9-8E7F-B3A7609E9331";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 2.6528101527827932 20 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetRGT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "203A20BF-4E03-46ED-EAF6-60BEA9B200D9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.824 -0.00010040181385306823 3.5527136788005009e-15 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetLFT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "BE557304-47E7-2D8C-8F66-CD94AA453354";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.824 1.4210854715202004e-14 0 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "jaw01Upr_tmpJnt" -p "head01_tmpJnt";
	rename -uid "903C2EF1-416A-6F98-950A-1DBBEFAE0171";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.3781271601296714e-16 -0.073181430527156976 3.0903813408731957 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 180 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 0 0 -2.4651903288156624e-32 -2.2204460492503136e-16 1.0000000000000002 0
		 1.2246467991473532e-16 1 2.2204460492503131e-16 0 -2.2815279078562374e-09 137.53090779923286 7.8685026751330751 1;
createNode joint -n "jaw02Upr_tmpJnt" -p "jaw01Upr_tmpJnt";
	rename -uid "C4852CF2-4C61-31C0-D54B-049F593C91AE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3956450219400147e-17 2.8421709430404007e-14 2.1995495613608833 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 0 0 -2.4651903288156624e-32 -2.2204460492503136e-16 1.0000000000000002 0
		 1.2246467991473532e-16 1 2.2204460492503131e-16 0 -2.2815279078562374e-09 137.53090779923286 10.215768076274593 1;
createNode joint -n "clavLFT_tmpJnt" -p "spine04_tmpJnt";
	rename -uid "3EAB7EBC-4714-8D06-A523-729FBCD1FC34";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.959241812099985 3.5839992763601458 1.2201467744023777 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 3.7551875924212634 145.77936822614953 2.7541221960322289 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
createNode joint -n "upperArmLFT_tmpJnt" -p "clavLFT_tmpJnt";
	rename -uid "9A2ADEF7-4D08-C5A3-CB89-D08CB04CD2AA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 1.7027428057123277 1.0954513473278809 -2.7157728773674537 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -4.9117097928146274 3.975693351829396e-16 -127.11027750389992 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "lowerArmLFT_tmpJnt" -p "upperArmLFT_tmpJnt";
	rename -uid "B4C8066D-4CC1-52FA-ABC8-5FA111AAF0A4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.0807050667123614e-15 12.059744188269297 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 11.411056756073945 0 0 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "handLFT_tmpJnt" -p "lowerArmLFT_tmpJnt";
	rename -uid "84F96B53-4720-8D46-21B1-2A99689F1BE7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 3.0552107862440049e-15 12.05974418826931 -8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -5.7055283780369752 0 0 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "thumb01LFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "F2F8001C-4303-9924-6444-818E0DE02F1B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.30964913755101975 1.8399138553434486 1.0086561935180212 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 76.374707497341731 -12.65608191924988 -36.990833542097697 ;
	setAttr ".bps" -type "matrix" -1.9292247829251112 0.3523100682868977 1.1175628440064949 0
		 0.93808943375450948 -0.82566347927261774 1.8796928980145207 0 0.70218039619341954 2.0710226440944011 0.55927207727771955 0
		 55.613149462896928 114.39107448747276 -9.5984222125244933 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb02LFT_tmpJnt" -p "thumb01LFT_tmpJnt";
	rename -uid "9A9C7F4D-4B7B-BFF3-98BE-DBA3F804637E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.5527136788005009e-14 1.8633414710587872 1.4210854715202004e-14 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -31.442781836867077 21.446388096676841 10.314464936620407 ;
	setAttr ".bps" -type "matrix" -1.8670305603142436 -0.57221142405374725 1.1321432465053674 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 57.361130408373768 112.85258148540528 -6.0959124827992408 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb03LFT_tmpJnt" -p "thumb02LFT_tmpJnt";
	rename -uid "116BDFA8-4FE5-7443-C485-A483D040DC5D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.9737991503207013e-14 2.526169241511071 9.9475983006414026e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb04LFT_tmpJnt" -p "thumb03LFT_tmpJnt";
	rename -uid "95204DAD-4F3E-687C-5468-09AE5DF31C1C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -7.1054273576010019e-15 1.8828534968703514 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "index01LFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "E10950A0-4867-6956-D869-CC8C0628A0ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.4571897905401343 3.7926566379706763 2.4131588674274935 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 50.964351500181365 -64.845283544124158 -16.787294061454876 ;
	setAttr ".bps" -type "matrix" -0.4024552055538394 -0.42915249271898948 2.1791822555922997 0
		 1.9262278576306877 -1.170007226260164 0.12532632827596146 0 1.1057365896011373 1.8819905913858135 0.5748350771527182 0
		 62.494586037671674 112.28512666087872 -8.5088436543149495 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index02LFT_tmpJnt" -p "index01LFT_tmpJnt";
	rename -uid "04B12F2B-4D86-36BB-66F2-1990C17B2F51";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.5527136788005009e-15 2.8833356695549064 7.1054273576010019e-15 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -31.776405321903091 41.290257150562105 -22.493331543073964 ;
	setAttr ".bps" -type "matrix" -0.65910907501621852 -0.55974485883547076 2.0850031841249486 0
		 1.1752615749089586 -1.9216899634424198 -0.14437891992889629 0 1.8108873005646784 1.0434417736436381 0.85258067491683254 0
		 67.988022556400921 108.80627315913544 -8.2305227253235742 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index03LFT_tmpJnt" -p "index02LFT_tmpJnt";
	rename -uid "0DE55C3B-468A-71A6-3B4F-399B8D838D78";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 1.7046288448146831 -4.2632564145606011e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -0.6591090750162184 -0.55974485883547065 2.0850031841249481 0
		 1.1752615749089583 -1.9216899634424194 -0.14437891992889626 0 1.8108873005646779 1.0434417736436379 0.85258067491683232 0
		 70.185507378557446 105.65220540014701 -8.3969435169588831 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index04LFT_tmpJnt" -p "index03LFT_tmpJnt";
	rename -uid "39AC5354-41E8-A6D3-D894-09A4A22E599D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 1.4210854715202004e-14 1.3476812425844242 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -0.6591090750162184 -0.55974485883547065 2.0850031841249481 0
		 1.1752615749089583 -1.9216899634424194 -0.14437891992889626 0 1.8108873005646779 1.0434417736436379 0.85258067491683232 0
		 70.185507378557446 105.65220540014701 -8.3969435169588831 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".oclr" -type "float3" 0.31666666 0.31666666 0.31666666 ;
createNode joint -n "middle01LFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "3E1F8A72-40C7-BC6D-6646-C09C3127C5D2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.9955862768776171 3.9905791809785702 1.1659711197270071 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 65.698125001957521 -78.187857892389871 -44.424606013084727 ;
	setAttr ".bps" -type "matrix" -0.12299867417619968 0.038889901762869106 2.2535164208996616 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.1702542134985132 1.9299088122531931 0.030568116544766679 0
		 62.950811016387775 112.71111734259617 -11.543968776495438 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle02LFT_tmpJnt" -p "middle01LFT_tmpJnt";
	rename -uid "92022009-432C-79D4-5E66-A2AA979CC77F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.5527136788005009e-15 2.9109673831029514 -4.9737991503207013e-14 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999956 0.99999999999999967 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -19.125750489691676 17.638870467440505 -5.3475830827462731 ;
	setAttr ".bps" -type "matrix" -0.20143743016798973 -0.29068663250527049 2.2293276118558056 0
		 1.1752615749089648 -1.9216899634424138 -0.14437891992889554 0 1.9165491253402447 1.1478616308859197 0.3228474625424575 0
		 67.715255810002049 108.22407346356407 -12.127039229244525 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle03LFT_tmpJnt" -p "middle02LFT_tmpJnt";
	rename -uid "0DD5F62B-48A5-4585-7548-F58FEE6FFD8E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.0658141036401503e-14 1.994912738126249 1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle04LFT_tmpJnt" -p "middle03LFT_tmpJnt";
	rename -uid "418291CB-4287-5EF0-5C52-59AE81430C00";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 3.5527136788005009e-15 1.3476812425844262 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "ring01LFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "5B4C8F51-469A-92DB-3E04-B895C41F1987";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.2985934206254939 4.2961115176482902 0.015804437385636083 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 97.310322374873522 -80.117396372124517 -80.530516800490105 ;
	setAttr ".bps" -type "matrix" -0.12299867417619993 0.038889901762868689 2.2535164208996612 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.170254213498513 1.9299088122531929 0.030568116544767172 0
		 63.101856530072354 112.66335954985358 -14.311344503683257 1;
createNode joint -n "ring02LFT_tmpJnt" -p "ring01LFT_tmpJnt";
	rename -uid "7BA962D7-4D58-44C5-01E5-9CBA8DDE20C1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.7081449022480228e-14 2.5519209161688341 -6.3948846218409017e-14 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -16.73191194155708 10.905736776015546 -2.1234322733326616 ;
	setAttr ".bps" -type "matrix" -0.20143743016798987 -0.29068663250527088 2.2293276118558052 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402449 1.1478616308859193 0.32284746254245783 0
		 66.993758410796886 108.45338229160024 -14.867414758093657 1;
createNode joint -n "ring03LFT_tmpJnt" -p "ring02LFT_tmpJnt";
	rename -uid "108F3438-4533-8407-B7BB-F39D5D441192";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.8421709430404007e-14 1.9997015580105324 1.9895196601282805e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
createNode joint -n "ring04LFT_tmpJnt" -p "ring03LFT_tmpJnt";
	rename -uid "B18979D4-4E78-34FA-A83E-23B810760096";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 0 1.3476812425844249 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
createNode joint -n "pinky01LFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "C76D3B17-429C-2BAD-C351-AC8813169B02";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.968447563320062 4.7032080529404006 -0.96355612475654495 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -118.8110886264038 -85.404710387368709 132.92708565426986 ;
	setAttr ".bps" -type "matrix" 1.0794628981158811 -0.058762086411279196 1.9814853586046262 0
		 1.4215420704544786 -1.5495750168189177 -0.82037355317641203 0 1.3816495037063139 1.6402260947881213 -0.70404571190857501 0
		 62.205154990637126 111.73991274880089 -16.463022243221697 1;
createNode joint -n "pinky02LFT_tmpJnt" -p "pinky01LFT_tmpJnt";
	rename -uid "C04A8AE6-42D3-B40C-2F6F-5BB1B97E6A5D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.5757174171303632e-14 2.0068617669804292 -6.3948846218409017e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -22.568955125495762 -9.5742942440493941 -0.59331501227231842 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 64.832687829787858 108.35094778363963 -17.922809609624039 1;
createNode joint -n "pinky03LFT_tmpJnt" -p "pinky02LFT_tmpJnt";
	rename -uid "7086DE0C-4688-50E4-8834-D8B0DC0B2977";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 5.6843418860808015e-14 1.6835536901174493 8.5265128291212022e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
createNode joint -n "pinky04LFT_tmpJnt" -p "pinky03LFT_tmpJnt";
	rename -uid "4A7CDB62-47B5-9E42-113B-C2BF944D7095";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.7763568394002505e-15 1.3476812425844358 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
createNode joint -n "baseSpreadLFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "BDE94FDC-468A-4814-6FA1-A398429C9131";
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -2.0892307711238303 2.7850284249333175 0.40527634857571249 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 83.559238175224422 -78.1878578923899 -44.424606013084691 ;
	setAttr ".sd" 1;
	setAttr ".otp" -type "string" "base spread";
createNode joint -n "propLFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "810CB183-4B8E-6778-1949-ADBF06951CBF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".t" -type "double3" -0.32093265280951044 5.71588639901245 1.1143716900424654 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 90.47897076372395 0.63304367065672462 127.11292354749385 ;
	setAttr ".bps" -type "matrix" 2.0211694160679943 0.97154585376466329 -0.25680771631066757 0
		 -0.90601840470197903 2.0112903362471197 0.4783504899473574 0 0.43472082934371808 -0.32524943493307901 2.1909376903926479 0
		 58.891023006333263 104.27635388271605 -14.015292574656838 1;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
	setAttr ".oclr" -type "float3" 0.40000001 0.40000001 0.40000001 ;
createNode joint -n "elbowPovLFT_tmpJnt" -p "lowerArmLFT_tmpJnt";
	rename -uid "09C6F9F7-4682-FF79-9FD0-F5AB4077713E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.3782231391701316e-06 -1.9776680104366449 -17.359523124840276 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.9321094444828675 5.1790126264472605 127.2881815940509 ;
	setAttr ".bps" -type "matrix" 0.99815258060496437 8.9981312040783247e-10 0.060757105194783181 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 -0.060757105194783181 -5.4770116136011496e-11 0.99815258060496437 0
		 40.855079650878928 143.65834045410159 -6.71590328216549 1;
	setAttr ".radi" 3;
createNode joint -n "clavRGT_tmpJnt" -p "spine04_tmpJnt";
	rename -uid "D305D550-48C5-570B-8993-9291059DDF2A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.95924 3.5840000000000032 1.2201500000000003 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 3.7551875924212634 145.77936822614953 2.7541221960322289 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
createNode joint -n "upperArmRGT_tmpJnt" -p "clavRGT_tmpJnt";
	rename -uid "8607A6B7-4784-B8BC-4667-93BF1492FD93";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.70274 -1.0955000000000013 2.71578 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -4.9117097928144364 0 -127.11027750389992 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "lowerArmRGT_tmpJnt" -p "upperArmRGT_tmpJnt";
	rename -uid "A6933754-409D-27EF-6C4C-5285C226DED2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -5.8155203845444703e-05 -12.059767310798446 -3.9106756855034064e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 11.411056756073783 0 0 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "handRGT_tmpJnt" -p "lowerArmRGT_tmpJnt";
	rename -uid "AFFBFDC4-43BC-EF72-9506-E4A4F3849734";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 3.0572036529008528e-05 -12.059791777388396 6.2086218247103808e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -5.7055283780371528 0 0 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "thumb01RGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "7086899D-47FE-847F-C4A2-27A6F12652C2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.30966235198479097 -1.8398676860729406 -1.0086537184370425 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 76.374707497341902 -12.656081919249798 -36.990833542097704 ;
	setAttr ".bps" -type "matrix" -1.9292247829251112 0.3523100682868977 1.1175628440064949 0
		 0.93808943375450948 -0.82566347927261774 1.8796928980145207 0 0.70218039619341954 2.0710226440944011 0.55927207727771955 0
		 55.613149462896928 114.39107448747276 -9.5984222125244933 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb02RGT_tmpJnt" -p "thumb01RGT_tmpJnt";
	rename -uid "CA551C51-4B10-821E-6DD6-F7A15ABC346F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 2.2038787221845269e-05 -1.8633518559855624 4.1933955671424883e-05 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -31.442781836867105 21.446388096676817 10.314464936620388 ;
	setAttr ".bps" -type "matrix" -1.8670305603142436 -0.57221142405374725 1.1321432465053674 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 57.361130408373768 112.85258148540528 -6.0959124827992408 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb03RGT_tmpJnt" -p "thumb02RGT_tmpJnt";
	rename -uid "DBC0E9F6-40ED-5DF7-F5D0-7CB04F11A4CD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.2648229864994391e-05 -2.5261446967345362 -1.5528460306057923e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb04RGT_tmpJnt" -p "thumb03RGT_tmpJnt";
	rename -uid "99CB9EC6-4AF3-065B-B4C7-BA831615B97D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 7.9966485131421905e-06 -1.8828015541370151 -4.2134010282524059e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "index01RGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "81CB0621-44E0-7B53-692E-DD8912F34505";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.4572112568810098 -3.7925806987721202 -2.4131580352845461 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 50.964351500181714 -64.845283544124129 -16.787294061455203 ;
	setAttr ".bps" -type "matrix" -0.4024552055538394 -0.42915249271898948 2.1791822555922997 0
		 1.9262278576306877 -1.170007226260164 0.12532632827596146 0 1.1057365896011373 1.8819905913858135 0.5748350771527182 0
		 62.494586037671674 112.28512666087872 -8.5088436543149495 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index02RGT_tmpJnt" -p "index01RGT_tmpJnt";
	rename -uid "7B7FAB44-4659-D7F5-8012-39B1D7AAB9D3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -6.3323230499179317e-06 -2.8833914375060772 8.9869982517143399e-05 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -31.776405321903027 41.290257150562113 -22.493331543073943 ;
	setAttr ".bps" -type "matrix" -0.65910907501621852 -0.55974485883547076 2.0850031841249486 0
		 1.1752615749089586 -1.9216899634424198 -0.14437891992889629 0 1.8108873005646784 1.0434417736436381 0.85258067491683254 0
		 67.988022556400921 108.80627315913544 -8.2305227253235742 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index03RGT_tmpJnt" -p "index02RGT_tmpJnt";
	rename -uid "A7C77351-4882-BC67-3ECC-B1BC8BEFD633";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.3474706470617548e-05 -1.7045661792805595 -1.6470438886528882e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 1.7075472925031871e-06 0 0 ;
	setAttr ".bps" -type "matrix" -0.6591090750162184 -0.55974485883547065 2.0850031841249481 0
		 1.1752615749089583 -1.9216899634424194 -0.14437891992889626 0 1.8108873005646779 1.0434417736436379 0.85258067491683232 0
		 70.185507378557446 105.65220540014701 -8.3969435169588831 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index04RGT_tmpJnt" -p "index03RGT_tmpJnt";
	rename -uid "4BB7B3C1-477E-A769-3A35-7389303D0101";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -3.0696578718902856e-06 -1.3476637386390458 -6.9299902243358247e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -1.7075472925031882e-06 0 0 ;
	setAttr ".bps" -type "matrix" -0.6591090750162184 -0.55974485883547065 2.0850031841249481 0
		 1.1752615749089583 -1.9216899634424194 -0.14437891992889626 0 1.8108873005646779 1.0434417736436379 0.85258067491683232 0
		 70.185507378557446 105.65220540014701 -8.3969435169588831 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
	setAttr ".oclr" -type "float3" 0.31666666 0.31666666 0.31666666 ;
createNode joint -n "middle01RGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "A640155F-40FB-0A67-5A2C-CFA7283E6E2E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.9956190276401458 -3.990563810865325 -1.1659685172979288 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 65.698125001958132 -78.187857892389744 -44.424606013085317 ;
	setAttr ".bps" -type "matrix" -0.12299867417619968 0.038889901762869106 2.2535164208996616 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.1702542134985132 1.9299088122531931 0.030568116544766679 0
		 62.950811016387775 112.71111734259617 -11.543968776495438 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle02RGT_tmpJnt" -p "middle01RGT_tmpJnt";
	rename -uid "974A3564-4AE0-B47B-D509-60A00D3CA40A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.0691960428133029e-06 -2.9109724247771744 2.8217323560397745e-05 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999956 0.99999999999999967 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -19.125750489691633 17.638870467440494 -5.3475830827462456 ;
	setAttr ".bps" -type "matrix" -0.20143743016798973 -0.29068663250527049 2.2293276118558056 0
		 1.1752615749089648 -1.9216899634424138 -0.14437891992889554 0 1.9165491253402447 1.1478616308859197 0.3228474625424575 0
		 67.715255810002049 108.22407346356407 -12.127039229244525 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle03RGT_tmpJnt" -p "middle02RGT_tmpJnt";
	rename -uid "7AF53A9D-40F6-8DCB-B1CC-03949876475A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.283187279061849e-05 -1.9948845408344393 3.5263083752568036e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle04RGT_tmpJnt" -p "middle03RGT_tmpJnt";
	rename -uid "93529D37-4423-8574-C33B-4981F06AFDFC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.5387229392871404e-05 -1.3476562433473984 1.8601715488841819e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "ring01RGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "849712C1-4ED9-D6D9-A048-4ABF3418927B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.2985900633935614 -4.2960501242227433 -0.015802729100676149 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 97.310322374873635 -80.117396372124361 -80.530516800490133 ;
	setAttr ".bps" -type "matrix" -0.12299867417619993 0.038889901762868689 2.2535164208996612 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.170254213498513 1.9299088122531929 0.030568116544767172 0
		 63.101856530072354 112.66335954985358 -14.311344503683257 1;
createNode joint -n "ring02RGT_tmpJnt" -p "ring01RGT_tmpJnt";
	rename -uid "761D3E73-4ECF-3854-8D7E-85819689F57C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.3556475426668158e-06 -2.5519193135500835 -3.1133067075472809e-05 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -16.731911941556959 10.905736776015514 -2.1234322733326252 ;
	setAttr ".bps" -type "matrix" -0.20143743016798987 -0.29068663250527088 2.2293276118558052 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402449 1.1478616308859193 0.32284746254245783 0
		 66.993758410796886 108.45338229160024 -14.867414758093657 1;
createNode joint -n "ring03RGT_tmpJnt" -p "ring02RGT_tmpJnt";
	rename -uid "3CF85661-4AB0-AE90-06FD-B3AA79D94004";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.0664606252581734e-06 -1.9997045997810603 2.6320823302228291e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
createNode joint -n "ring04RGT_tmpJnt" -p "ring03RGT_tmpJnt";
	rename -uid "DC8403EA-4B4C-1F04-2C56-089B76D5D957";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -6.4647112534288453e-06 -1.347667987894025 1.9735953777910709e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
createNode joint -n "pinky01RGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "A7C537C7-46FC-98DC-38EB-A484CECE266A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.9684521188027162 -4.703209547342655 0.9635621766448752 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -118.81108862640492 -85.404710387368866 132.92708565427108 ;
	setAttr ".bps" -type "matrix" 1.0794628981158811 -0.058762086411279196 1.9814853586046262 0
		 1.4215420704544786 -1.5495750168189177 -0.82037355317641203 0 1.3816495037063139 1.6402260947881213 -0.70404571190857501 0
		 62.205154990637126 111.73991274880089 -16.463022243221697 1;
createNode joint -n "pinky02RGT_tmpJnt" -p "pinky01RGT_tmpJnt";
	rename -uid "1B5068E1-4927-0672-12AE-4581C0E73F8C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.5995844069345324e-06 -2.0067814654751199 3.7338800787267701e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -22.568955125495741 -9.5742942440493479 -0.59331501227233607 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 64.832687829787858 108.35094778363963 -17.922809609624039 1;
createNode joint -n "pinky03RGT_tmpJnt" -p "pinky02RGT_tmpJnt";
	rename -uid "04F047DE-459E-4F38-CFA2-A794F607D5BB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.7276733899128658e-05 -1.6835580527225318 -9.2027594440935445e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
createNode joint -n "pinky04RGT_tmpJnt" -p "pinky03RGT_tmpJnt";
	rename -uid "18144C34-4036-BD21-BE49-CA9971D0F0BA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 2.0854218172772221e-05 -1.3477379437194621 7.4323165428324955e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
createNode joint -n "baseSpreadRGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "7D4065D6-4466-DBD9-2191-44B8DD0581BD";
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 2.0891979254714244 -2.7850014977017086 -0.4052736368999883 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 83.559238175224991 -78.187857892389786 -44.424606013085238 ;
	setAttr ".sd" 1;
	setAttr ".otp" -type "string" "base spread";
createNode joint -n "propRGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "B78A9A88-408A-4188-E3BE-FB8471BE3623";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".t" -type "double3" 0.32089599283879977 -5.7158312703254133 -1.1143696839436728 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -89.521029236276163 0.63304367065659761 127.11292354749385 ;
	setAttr ".bps" -type "matrix" 2.0211694160679943 0.97154585376466329 -0.25680771631066757 0
		 -0.90601840470197903 2.0112903362471197 0.4783504899473574 0 0.43472082934371808 -0.32524943493307901 2.1909376903926479 0
		 58.891023006333263 104.27635388271605 -14.015292574656838 1;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
	setAttr ".oclr" -type "float3" 0.40000001 0.40000001 0.40000001 ;
createNode joint -n "elbowPovRGT_tmpJnt" -p "lowerArmRGT_tmpJnt";
	rename -uid "1AF475D8-4B46-FCB0-D28F-A587D9917A27";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.0523344919022293e-05 1.9941209448423862 17.357646746414964 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -176.06789055551712 5.1790126264472853 127.28818159405093 ;
	setAttr ".bps" -type "matrix" 0.99815258060496437 8.9981312040783247e-10 0.060757105194783181 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 -0.060757105194783181 -5.4770116136011496e-11 0.99815258060496437 0
		 40.855079650878928 143.65834045410159 -6.71590328216549 1;
	setAttr ".radi" 3;
createNode joint -n "hip_tmpJnt" -p "cog_tmpJnt";
	rename -uid "03D6D4F9-4893-9E3A-04D4-288E9D11DBDC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 103.48487111611378 0 1;
	setAttr ".typ" 2;
createNode joint -n "upperLegLFT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "FB376669-4A4F-72C9-CFE2-2EBB6EC1765A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 3.6935934746627073 4.4139062980501575e-32 -180 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "lowerLegLFT_tmpJnt" -p "upperLegLFT_tmpJnt";
	rename -uid "A9CF41D1-4642-2E43-CD63-28AB8ABBED3B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 4.8985871965894122e-15 20.041629918284329 -3.7747582837255322e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -7.3871869493254003 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "ankleLFT_tmpJnt" -p "lowerLegLFT_tmpJnt";
	rename -uid "C676FCE7-4A19-ADC3-9228-91924E747A40";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.6645352591003757e-15 20.041629918284325 -1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.6935934746626939 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "ballLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "6A6FA096-48CE-3D15-2CD1-C7B8E8AD3A91";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -3.5527136788005009e-15 4.9999999999999991 5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "toesTipLFT_tmpJnt" -p "ballLFT_tmpJnt";
	rename -uid "4E18BC6B-41E9-29E6-8F9F-E9BAF59C39BF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 3 -1.4248663566049916e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "footOutLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "A930766D-45C6-E517-338C-57BD7A16CCF8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.9999999999999969 5 5.5511151231257827e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -180 -89.999999999999957 0 ;
	setAttr ".bps" -type "matrix" -1.7542011806855572e-15 2.1482768609870751e-31 2.2572056524766739 0
		 0 2.2572056524766739 -2.2257766178534174e-31 0 -2.2572056524766739 0 -1.5036010120161916e-15 0
		 5.0815629059024978 -0.0024171567953992223 2.245109043491059 1;
createNode joint -n "heelRollLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "81D1784F-49AC-8D09-1737-1CB411A6AA32";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.5527136788005009e-15 5 -5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 180 89.999999999999986 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 2.7642796773228715e-16 2.2572056524766739 2.7642796773228715e-16 0
		 3.3852662587815329e-32 2.7642796773228715e-16 -2.2572056524766739 0 9.951313972473141 0.44198825955391641 -11.657663345336907 1;
createNode joint -n "footInLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "B329210C-46FF-6162-084A-87B3F178D375";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.0000000000000036 5 5.5511151231257827e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -90.000000000004192 89.999999999999943 0 ;
	setAttr ".bps" -type "matrix" -2.0048013493549223e-15 2.4551735554138001e-31 -2.2572056524766739 0
		 2.2572056524766739 1.651196833540488e-13 -2.0048013493549223e-15 0 1.649943832697141e-13 -2.2572056524766739 0 0
		 14.869093924780286 -0.0024171567950581618 2.2451089524518615 1;
createNode joint -n "kneePovLFT_tmpJnt" -p "lowerLegLFT_tmpJnt";
	rename -uid "22F47276-4292-2495-D00C-6F8A76BB59BA";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -2.6645352591003757e-15 -1.2052411550258419 18.670042035146455 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -3.6935934746626913 4.4139062980501586e-32 180 ;
	setAttr ".radi" 3;
createNode joint -n "upperLegRGT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "0B130541-4827-8907-562E-7C9AA277A69E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -5 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 3.6935934746625794 180 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "lowerLegRGT_tmpJnt" -p "upperLegRGT_tmpJnt";
	rename -uid "C1FB04EC-4BEF-CCFA-C3C3-BC86534E8B97";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 8.8817841970012523e-16 -20.041630153507644 -3.6437763935026624e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -7.3871869493253444 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "ankleRGT_tmpJnt" -p "lowerLegRGT_tmpJnt";
	rename -uid "EC39F244-4D02-E24A-2AF5-FB9044754D13";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.7763568394002505e-15 -20.04163015350764 3.6437763271668366e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.6935934746627939 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "ballRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "F8AFC2F2-4A31-F6D9-D7C6-668814E92DD4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -5 -4.9999999999999973 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "toesTipRGT_tmpJnt" -p "ballRGT_tmpJnt";
	rename -uid "04752938-469B-EF0E-E5D7-CCB82816F912";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -2.9999999999999991 1.2583376061289592e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "footOutRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "66D1CB91-4156-CB84-DAD4-E5A7044858B9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.9999999999999991 -4.9999999999999991 2.6155955450304147e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 179.99999879258175 -90 0 ;
	setAttr ".bps" -type "matrix" -1.7542011806855572e-15 2.1482768609870751e-31 2.2572056524766739 0
		 0 2.2572056524766739 -2.2257766178534174e-31 0 -2.2572056524766739 0 -1.5036010120161916e-15 0
		 5.0815629059024978 -0.0024171567953992223 2.245109043491059 1;
createNode joint -n "heelRollRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "F8061476-429F-D615-A371-AB90DA069FA5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 1.7763568394002505e-15 -4.9999999999999973 5.0000000000000009 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 179.99999879258175 90 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 2.7642796773228715e-16 2.2572056524766739 2.7642796773228715e-16 0
		 3.3852662587815329e-32 2.7642796773228715e-16 -2.2572056524766739 0 9.951313972473141 0.44198825955391641 -11.657663345336907 1;
createNode joint -n "footInRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "6393814A-45C8-0D62-E5C6-C98E586CD49D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 3.0000000000000009 -4.9999999999999991 1.880807465542003e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -90.000000000004192 89.999999999999943 0 ;
	setAttr ".bps" -type "matrix" -2.0048013493549223e-15 2.4551735554138001e-31 -2.2572056524766739 0
		 2.2572056524766739 1.651196833540488e-13 -2.0048013493549223e-15 0 1.649943832697141e-13 -2.2572056524766739 0 0
		 14.869093924780286 -0.0024171567950581618 2.2451089524518615 1;
createNode joint -n "kneePovRGT_tmpJnt" -p "lowerLegRGT_tmpJnt";
	rename -uid "13C46437-490F-279B-2AAA-FEA3F217C61E";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.4408920985006262e-15 1.2052409198025522 -18.670038391370099 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 176.30640652533728 -4.4139062980501575e-32 -180 ;
	setAttr ".radi" 3;
createNode joint -n "AAupperLegLFT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "79E97D2F-49FA-0BF9-3BFE-D4B493C1924F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 13.042098137979828 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 3.693593474662705 0 -180 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "AAlowerLegLFT_tmpJnt" -p "AAupperLegLFT_tmpJnt";
	rename -uid "EC9313D8-458A-C104-83BC-F58D6D6A5027";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 4.8985871965894122e-15 20.041629918284329 -3.7747582837255322e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -7.3871869493254003 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "AAankleLFT_tmpJnt" -p "AAlowerLegLFT_tmpJnt";
	rename -uid "3397A1E6-495A-1267-D2D5-2CBB22BAB13E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -2.6645352591003757e-15 20.041629918284325 -1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.6935934746626939 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "AAballLFT_tmpJnt" -p "AAankleLFT_tmpJnt";
	rename -uid "AC4718E7-4AA5-BFFA-D174-9F8587F3FA91";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -3.5527136788005009e-15 4.9999999999999991 5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 90.000000000000014 0 0 ;
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "AAtoesTipLFT_tmpJnt" -p "AAballLFT_tmpJnt";
	rename -uid "D6A22C6D-4EE4-3FFF-306C-16BA4F26145E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 3 -1.4248663566049916e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "AAfootOutLFT_tmpJnt" -p "AAankleLFT_tmpJnt";
	rename -uid "C3C4B232-4C51-FD40-BC38-C2A02C3EA7D0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.9999999999999969 5 5.5511151231257827e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -180 -89.999999999999957 0 ;
	setAttr ".bps" -type "matrix" -1.7542011806855572e-15 2.1482768609870751e-31 2.2572056524766739 0
		 0 2.2572056524766739 -2.2257766178534174e-31 0 -2.2572056524766739 0 -1.5036010120161916e-15 0
		 5.0815629059024978 -0.0024171567953992223 2.245109043491059 1;
createNode joint -n "AAheelRollLFT_tmpJnt" -p "AAankleLFT_tmpJnt";
	rename -uid "5BF78BAD-4C89-8857-C6B3-7A96C838D59F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.5527136788005009e-15 5 -5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 180 89.999999999999986 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 2.7642796773228715e-16 2.2572056524766739 2.7642796773228715e-16 0
		 3.3852662587815329e-32 2.7642796773228715e-16 -2.2572056524766739 0 9.951313972473141 0.44198825955391641 -11.657663345336907 1;
createNode joint -n "AAfootInLFT_tmpJnt" -p "AAankleLFT_tmpJnt";
	rename -uid "923E8181-4907-FF16-4032-DAB796162332";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -3.0000000000000036 5 5.5511151231257827e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -90.000000000004192 89.999999999999943 0 ;
	setAttr ".bps" -type "matrix" -2.0048013493549223e-15 2.4551735554138001e-31 -2.2572056524766739 0
		 2.2572056524766739 1.651196833540488e-13 -2.0048013493549223e-15 0 1.649943832697141e-13 -2.2572056524766739 0 0
		 14.869093924780286 -0.0024171567950581618 2.2451089524518615 1;
createNode joint -n "AAkneePovLFT_tmpJnt" -p "AAlowerLegLFT_tmpJnt";
	rename -uid "54C9039A-4A31-79CA-D423-BDA88D7A4ED9";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -2.6645352591003757e-15 -1.2052411550258419 18.670042035146455 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -3.6935934746626913 4.4139062980501586e-32 180 ;
	setAttr ".radi" 3;
createNode joint -n "AAupperLegRGT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "B6434681-4ED8-12C2-E8AC-238668B1A205";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -13.791930098027436 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 3.6935934746625794 180 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "AAlowerLegRGT_tmpJnt" -p "AAupperLegRGT_tmpJnt";
	rename -uid "C2556D0D-4ED7-AB7B-67F0-86ABAD2FD846";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 8.8817841970012523e-16 -20.041630153507644 -3.6437763935026624e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -7.3871869493253399 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "AAankleRGT_tmpJnt" -p "AAlowerLegRGT_tmpJnt";
	rename -uid "D3CA5DB5-4E12-5D61-BC79-6F943726F7B0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.7763568394002505e-15 -20.04163015350764 3.6437763271668366e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 3.6935934746627939 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "AAballRGT_tmpJnt" -p "AAankleRGT_tmpJnt";
	rename -uid "44936E0F-404A-D079-85C4-6EB3CF3B1714";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -5 -4.9999999999999973 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "AAtoesTipRGT_tmpJnt" -p "AAballRGT_tmpJnt";
	rename -uid "0F2914A5-41C0-4533-E107-8E85877DE1B2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 -2.9999999999999991 1.2583376061289592e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "AAfootOutRGT_tmpJnt" -p "AAankleRGT_tmpJnt";
	rename -uid "FC9C3025-4FC0-1179-4A94-0E9023043F3B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.9999999999999991 -4.9999999999999991 2.6155955450304147e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 179.99999879258175 -90 0 ;
	setAttr ".bps" -type "matrix" -1.7542011806855572e-15 2.1482768609870751e-31 2.2572056524766739 0
		 0 2.2572056524766739 -2.2257766178534174e-31 0 -2.2572056524766739 0 -1.5036010120161916e-15 0
		 5.0815629059024978 -0.0024171567953992223 2.245109043491059 1;
createNode joint -n "AAheelRollRGT_tmpJnt" -p "AAankleRGT_tmpJnt";
	rename -uid "A3062D5D-4A9B-22FB-ABFF-32A7C5602754";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 1.7763568394002505e-15 -4.9999999999999973 5.0000000000000009 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 179.99999879258175 90 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 2.7642796773228715e-16 2.2572056524766739 2.7642796773228715e-16 0
		 3.3852662587815329e-32 2.7642796773228715e-16 -2.2572056524766739 0 9.951313972473141 0.44198825955391641 -11.657663345336907 1;
createNode joint -n "AAfootInRGT_tmpJnt" -p "AAankleRGT_tmpJnt";
	rename -uid "4E5D51AC-45C4-934A-F493-9F81B6029522";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 3.0000000000000009 -4.9999999999999991 1.880807465542003e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -90.000000000004192 89.999999999999943 0 ;
	setAttr ".bps" -type "matrix" -2.0048013493549223e-15 2.4551735554138001e-31 -2.2572056524766739 0
		 2.2572056524766739 1.651196833540488e-13 -2.0048013493549223e-15 0 1.649943832697141e-13 -2.2572056524766739 0 0
		 14.869093924780286 -0.0024171567950581618 2.2451089524518615 1;
createNode joint -n "AAkneePovRGT_tmpJnt" -p "AAlowerLegRGT_tmpJnt";
	rename -uid "5BD94B1F-49ED-AF43-83B1-FB98F39A2896";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.4408920985006262e-15 1.2052409198025522 -18.670038391370099 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 176.30640652533728 0 -180 ;
	setAttr ".radi" 3;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "35396A64-4EBC-2CEA-30F5-37A3F388479E";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "99D6F2C0-430C-075D-5177-89B32FAFEB14";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "9382B18D-49BD-B74A-5A09-D89F4340EE0B";
createNode displayLayerManager -n "layerManager";
	rename -uid "3E5CC2DE-46A1-2920-8431-19BA74BA98AB";
createNode displayLayer -n "defaultLayer";
	rename -uid "2DF8B9B4-469B-B938-EEFB-09BA4E1CDC20";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "5B67DBB6-4A51-1050-FA67-2B849CB13C60";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "5F8E7648-43E2-B51D-2C6E-DFB54F4068BC";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "2B225356-417F-8DB7-C167-1CBCF3C699A5";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 948\n            -height 720\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n"
		+ "            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n"
		+ "            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n"
		+ "            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n"
		+ "                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n"
		+ "                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -autoFitTime 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n"
		+ "                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n"
		+ "                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n"
		+ "                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n"
		+ "\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n"
		+ "                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n"
		+ "                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n"
		+ "                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n"
		+ "                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n"
		+ "                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 948\\n    -height 720\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 948\\n    -height 720\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "08DEB864-4FB3-A92D-738B-26A2EFA69B06";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 0;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".fs" 1;
	setAttr ".ef" 10;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "root.s" "cog_tmpJnt.is";
connectAttr "cog_tmpJnt.s" "spine01_tmpJnt.is";
connectAttr "spine01_tmpJnt.s" "spine02_tmpJnt.is";
connectAttr "spine02_tmpJnt.s" "spine03_tmpJnt.is";
connectAttr "spine03_tmpJnt.s" "spine04_tmpJnt.is";
connectAttr "spine04_tmpJnt.s" "neck_tmpJnt.is";
connectAttr "neck_tmpJnt.s" "head01_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "head02_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eyeLFT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "jaw01Lwr_tmpJnt.is";
connectAttr "jaw01Lwr_tmpJnt.s" "jaw02Lwr_tmpJnt.is";
connectAttr "jaw02Lwr_tmpJnt.s" "jaw03Lwr_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eyeRGT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eye_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTargetRGT_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTargetLFT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "jaw01Upr_tmpJnt.is";
connectAttr "jaw01Upr_tmpJnt.s" "jaw02Upr_tmpJnt.is";
connectAttr "spine04_tmpJnt.s" "clavLFT_tmpJnt.is";
connectAttr "clavLFT_tmpJnt.s" "upperArmLFT_tmpJnt.is";
connectAttr "upperArmLFT_tmpJnt.s" "lowerArmLFT_tmpJnt.is";
connectAttr "lowerArmLFT_tmpJnt.s" "handLFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "thumb01LFT_tmpJnt.is";
connectAttr "thumb01LFT_tmpJnt.s" "thumb02LFT_tmpJnt.is";
connectAttr "thumb02LFT_tmpJnt.s" "thumb03LFT_tmpJnt.is";
connectAttr "thumb03LFT_tmpJnt.s" "thumb04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "index01LFT_tmpJnt.is";
connectAttr "index01LFT_tmpJnt.s" "index02LFT_tmpJnt.is";
connectAttr "index02LFT_tmpJnt.s" "index03LFT_tmpJnt.is";
connectAttr "index03LFT_tmpJnt.s" "index04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "middle01LFT_tmpJnt.is";
connectAttr "middle01LFT_tmpJnt.s" "middle02LFT_tmpJnt.is";
connectAttr "middle02LFT_tmpJnt.s" "middle03LFT_tmpJnt.is";
connectAttr "middle03LFT_tmpJnt.s" "middle04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "ring01LFT_tmpJnt.is";
connectAttr "ring01LFT_tmpJnt.s" "ring02LFT_tmpJnt.is";
connectAttr "ring02LFT_tmpJnt.s" "ring03LFT_tmpJnt.is";
connectAttr "ring03LFT_tmpJnt.s" "ring04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "pinky01LFT_tmpJnt.is";
connectAttr "pinky01LFT_tmpJnt.s" "pinky02LFT_tmpJnt.is";
connectAttr "pinky02LFT_tmpJnt.s" "pinky03LFT_tmpJnt.is";
connectAttr "pinky03LFT_tmpJnt.s" "pinky04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "baseSpreadLFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "propLFT_tmpJnt.is";
connectAttr "lowerArmLFT_tmpJnt.s" "elbowPovLFT_tmpJnt.is";
connectAttr "spine04_tmpJnt.s" "clavRGT_tmpJnt.is";
connectAttr "clavRGT_tmpJnt.s" "upperArmRGT_tmpJnt.is";
connectAttr "upperArmRGT_tmpJnt.s" "lowerArmRGT_tmpJnt.is";
connectAttr "lowerArmRGT_tmpJnt.s" "handRGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "thumb01RGT_tmpJnt.is";
connectAttr "thumb01RGT_tmpJnt.s" "thumb02RGT_tmpJnt.is";
connectAttr "thumb02RGT_tmpJnt.s" "thumb03RGT_tmpJnt.is";
connectAttr "thumb03RGT_tmpJnt.s" "thumb04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "index01RGT_tmpJnt.is";
connectAttr "index01RGT_tmpJnt.s" "index02RGT_tmpJnt.is";
connectAttr "index02RGT_tmpJnt.s" "index03RGT_tmpJnt.is";
connectAttr "index03RGT_tmpJnt.s" "index04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "middle01RGT_tmpJnt.is";
connectAttr "middle01RGT_tmpJnt.s" "middle02RGT_tmpJnt.is";
connectAttr "middle02RGT_tmpJnt.s" "middle03RGT_tmpJnt.is";
connectAttr "middle03RGT_tmpJnt.s" "middle04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "ring01RGT_tmpJnt.is";
connectAttr "ring01RGT_tmpJnt.s" "ring02RGT_tmpJnt.is";
connectAttr "ring02RGT_tmpJnt.s" "ring03RGT_tmpJnt.is";
connectAttr "ring03RGT_tmpJnt.s" "ring04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "pinky01RGT_tmpJnt.is";
connectAttr "pinky01RGT_tmpJnt.s" "pinky02RGT_tmpJnt.is";
connectAttr "pinky02RGT_tmpJnt.s" "pinky03RGT_tmpJnt.is";
connectAttr "pinky03RGT_tmpJnt.s" "pinky04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "baseSpreadRGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "propRGT_tmpJnt.is";
connectAttr "lowerArmRGT_tmpJnt.s" "elbowPovRGT_tmpJnt.is";
connectAttr "cog_tmpJnt.s" "hip_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "upperLegLFT_tmpJnt.is";
connectAttr "upperLegLFT_tmpJnt.s" "lowerLegLFT_tmpJnt.is";
connectAttr "lowerLegLFT_tmpJnt.s" "ankleLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "ballLFT_tmpJnt.is";
connectAttr "ballLFT_tmpJnt.s" "toesTipLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footOutLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "heelRollLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footInLFT_tmpJnt.is";
connectAttr "lowerLegLFT_tmpJnt.s" "kneePovLFT_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "upperLegRGT_tmpJnt.is";
connectAttr "upperLegRGT_tmpJnt.s" "lowerLegRGT_tmpJnt.is";
connectAttr "lowerLegRGT_tmpJnt.s" "ankleRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "ballRGT_tmpJnt.is";
connectAttr "ballRGT_tmpJnt.s" "toesTipRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footOutRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "heelRollRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footInRGT_tmpJnt.is";
connectAttr "lowerLegRGT_tmpJnt.s" "kneePovRGT_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "AAupperLegLFT_tmpJnt.is";
connectAttr "AAupperLegLFT_tmpJnt.s" "AAlowerLegLFT_tmpJnt.is";
connectAttr "AAlowerLegLFT_tmpJnt.s" "AAankleLFT_tmpJnt.is";
connectAttr "AAankleLFT_tmpJnt.s" "AAballLFT_tmpJnt.is";
connectAttr "AAballLFT_tmpJnt.s" "AAtoesTipLFT_tmpJnt.is";
connectAttr "AAankleLFT_tmpJnt.s" "AAfootOutLFT_tmpJnt.is";
connectAttr "AAankleLFT_tmpJnt.s" "AAheelRollLFT_tmpJnt.is";
connectAttr "AAankleLFT_tmpJnt.s" "AAfootInLFT_tmpJnt.is";
connectAttr "AAlowerLegLFT_tmpJnt.s" "AAkneePovLFT_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "AAupperLegRGT_tmpJnt.is";
connectAttr "AAupperLegRGT_tmpJnt.s" "AAlowerLegRGT_tmpJnt.is";
connectAttr "AAlowerLegRGT_tmpJnt.s" "AAankleRGT_tmpJnt.is";
connectAttr "AAankleRGT_tmpJnt.s" "AAballRGT_tmpJnt.is";
connectAttr "AAballRGT_tmpJnt.s" "AAtoesTipRGT_tmpJnt.is";
connectAttr "AAankleRGT_tmpJnt.s" "AAfootOutRGT_tmpJnt.is";
connectAttr "AAankleRGT_tmpJnt.s" "AAheelRollRGT_tmpJnt.is";
connectAttr "AAankleRGT_tmpJnt.s" "AAfootInRGT_tmpJnt.is";
connectAttr "AAlowerLegRGT_tmpJnt.s" "AAkneePovRGT_tmpJnt.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of templateJoint_biped_fourLeg.ma
