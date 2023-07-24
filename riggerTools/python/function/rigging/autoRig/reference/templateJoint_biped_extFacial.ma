//Maya ASCII 2018 scene
//Name: templateJoint_biped_extFacial.ma
//Last modified: Mon, Jul 17, 2023 04:11:14 PM
//Codeset: 1252
requires maya "2018";
requires -nodeType "ikSpringSolver" "ikSpringSolver" "1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "88766DAF-4028-8F49-8684-8C85944B3A2A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 90.826502207279049 53.941160752264267 37.061264416314032 ;
	setAttr ".r" -type "double3" 8.0616472703981774 72.199999999998866 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "44017135-4256-76C8-9411-34B8F6F83669";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 103.19345177980061;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0.0001698487937105142 41.453871469226954 0 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "588C317B-4269-571B-C655-A2A88FFCD028";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "C5E11644-4D92-5B80-6E26-CDA3CD6AA8EF";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "4BF35588-4810-5C37-9BD7-0C96E77AC4B3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "C45A3327-46E7-8C82-AE97-16AF29423D1B";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "7F60405D-400A-6AAF-39A0-F99C5DF69F28";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1002.8512290249457 74.230631379642929 0.62523741394157439 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "E37FC84E-493D-ED40-7A9A-CCA77A73B9AF";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1002.8512290249457;
	setAttr ".ow" 27.102393816143604;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 74.230631379642929 0.62523741394135168 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "template_ctrl";
	rename -uid "8BA50ABA-442F-9CED-74C1-91BF027DD4AD";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "template_ctrlShape" -p "template_ctrl";
	rename -uid "03FE2973-4C76-00A0-A5B5-759206886E1D";
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
	rename -uid "8E9A517E-4046-734D-47CC-9692B18EA7D0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 0 0 1;
createNode joint -n "cog_tmpJnt" -p "root";
	rename -uid "0F446697-4E0C-6088-AD5E-E7B6855242D0";
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
	rename -uid "C8B761A1-4452-B74A-E511-2F9251E7DEA9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 4 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 115.97688088568215 1.638809891990324 1;
createNode joint -n "spine02_tmpJnt" -p "spine01_tmpJnt";
	rename -uid "548D2603-4C13-50B1-FC08-EFA5191806F2";
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
	rename -uid "CF01477B-42FA-8C50-C9BC-D4A8FAAB2E58";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 4 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 139.05166856595392 2.6655195481726714 1;
createNode joint -n "spine04_tmpJnt" -p "spine03_tmpJnt";
	rename -uid "CD6C1D6F-4635-433C-0AD4-4CB160A86D5E";
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
	rename -uid "1A1BF003-4AC6-8565-405A-359A2E3D420F";
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
	rename -uid "4E4E10D7-4031-0FD2-AE29-9F8B40312EFA";
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
createNode joint -n "eyeLFT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "F17A905A-4F0D-1F61-EE1B-49AA173FF83B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.8239219872507531 2.6158880095642019 2.6483026590950898 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeRGT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "2602C3EB-4607-6054-F373-16986C72D8BE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.8239219872507531 2.6158880095642019 2.6483026590950898 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eye_tmpJnt" -p "head01_tmpJnt";
	rename -uid "EEB6F233-466D-8ED4-3C5C-0FB3D86F67B9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 2.6528101527827932 20 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetRGT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "F965E353-46B8-B2D2-557A-0595B2BD39BE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.824 -0.00010040181385306823 3.5527136788005009e-15 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetLFT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "AC471A8E-4B5E-AC68-6053-94AC72F07871";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.824 1.4210854715202004e-14 0 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "headTop_tmpJnt" -p "head01_tmpJnt";
	rename -uid "DE8C138B-48F8-6927-965B-A5BEB1C131F9";
	setAttr ".t" -type "double3" 0 2.1223338562240315 2.2204460492503131e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "head02_tmpJnt" -p "headTop_tmpJnt";
	rename -uid "346A9AFF-4B67-6D60-B539-609D4FE3C89D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 8.1986726466046065 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766744 0 0 0 0 2.2572056524766739 0
		 0 185.97992277316624 -2.309516956192498 1;
	setAttr ".typ" 8;
	setAttr ".radi" 3;
createNode joint -n "headBottom_tmpJnt" -p "head01_tmpJnt";
	rename -uid "1C6E27CC-427F-0747-CBFD-A5A28FB6AF77";
	setAttr ".t" -type "double3" 0 -0.82520827730756707 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "jaw01Lwr_tmpJnt" -p "headBottom_tmpJnt";
	rename -uid "56A81161-42A7-F26C-6BEB-FF93CB3B7D24";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.6747740263279888e-16 1.6770767292744608 0.85055887360982263 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -5.6817911712458105e-17 -0.46395345786243802 0.8858595763085072 0 1.0848650946202438e-16 0.8858595763085072 0.46395345786243802 0
		 -2.281527907856237e-09 138.24609308456581 1.2332340767044465 1;
createNode joint -n "jaw02Lwr_tmpJnt" -p "jaw01Lwr_tmpJnt";
	rename -uid "D462A5BA-48EE-A383-163A-27A1B98B0D3E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.45346939366313e-16 -1.8375419927605208 2.2988962736372129 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661394e-09 134.88585971678842 7.6491683844072185 1;
createNode joint -n "jaw03Lwr_tmpJnt" -p "jaw02Lwr_tmpJnt";
	rename -uid "3E9DBA2E-4705-1848-4195-9AA8B187CC2A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3956450219389744e-17 -1.4210854715202004e-14 1.9710502458233852 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661419e-09 134.88585971678845 9.7309712720145338 1;
createNode joint -n "jaw01Upr_tmpJnt" -p "headBottom_tmpJnt";
	rename -uid "92D1F07C-4043-ABC6-A3D2-739EA6852B02";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.3781271601296714e-16 0.7520268467804101 3.0903813408731957 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 180 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 0 0 -2.4651903288156624e-32 -2.2204460492503136e-16 1.0000000000000002 0
		 1.2246467991473532e-16 1 2.2204460492503131e-16 0 -2.2815279078562374e-09 137.53090779923286 7.8685026751330751 1;
createNode joint -n "jaw02Upr_tmpJnt" -p "jaw01Upr_tmpJnt";
	rename -uid "F7DC55F4-49AB-9C5A-7997-8483FB218E16";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3956450219400147e-17 2.8421709430404007e-14 2.1995495613608833 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 0 0 -2.4651903288156624e-32 -2.2204460492503136e-16 1.0000000000000002 0
		 1.2246467991473532e-16 1 2.2204460492503131e-16 0 -2.2815279078562374e-09 137.53090779923286 10.215768076274593 1;
createNode joint -n "clavLFT_tmpJnt" -p "spine04_tmpJnt";
	rename -uid "116E547F-4E76-E8F5-793C-AF9D57149374";
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
	rename -uid "72F4096F-483D-B61B-0319-9B9926EEA543";
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
	rename -uid "B22CFD0C-4A94-E328-D568-EA8CF2E2DAD1";
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
	rename -uid "40E0DCD6-45D0-49C2-7452-5396603086D9";
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
	rename -uid "0A3D5E6D-4B68-185A-2991-A48E253EECA9";
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
	rename -uid "2AED9814-49C4-4998-48B5-18A74E354850";
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
	rename -uid "FE5C863B-4C68-7922-A306-A283DD67E3FC";
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
	rename -uid "20C1D29B-49F5-2FF6-94FC-3984E700364C";
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
	rename -uid "B51D33E9-4353-1C78-7B94-8C8940DAC9D3";
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
	rename -uid "ED3D0B2F-4423-D227-6CC9-81B4C1328E98";
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
	rename -uid "1F88CCD4-48C3-3E22-8556-1DAC799E6220";
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
	rename -uid "DBDE37F5-41BB-8AB9-84C3-F19818C22D9B";
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
	rename -uid "9C2E4412-4C10-E7A5-DB86-81A0016E424D";
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
	rename -uid "957FF00D-4673-B225-E979-E99C3650568B";
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
	rename -uid "F492B678-43FC-AB3A-9FC5-008B753B6A9A";
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
	rename -uid "B212D118-42B1-7AD4-5286-69BB8C349BC9";
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
	rename -uid "CF502500-43F4-D334-A37E-F3A1CFCDC7FB";
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
	rename -uid "355E3506-485A-B438-479D-07B098D2111E";
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
	rename -uid "744373B1-4AAE-410E-67D1-788F42805BE1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.8421709430404007e-14 1.9997015580105324 1.9895196601282805e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
createNode joint -n "ring04LFT_tmpJnt" -p "ring03LFT_tmpJnt";
	rename -uid "BE727753-4EFE-EAE4-B06A-AEA07DF6C019";
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
	rename -uid "AB882D87-4063-042B-3313-A092D16D428E";
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
	rename -uid "EE057C50-4428-C61E-C58F-74B69A5FBFE9";
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
	rename -uid "23A106EC-4536-D1D0-1A7C-C1A259A86E84";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 5.6843418860808015e-14 1.6835536901174493 8.5265128291212022e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
createNode joint -n "pinky04LFT_tmpJnt" -p "pinky03LFT_tmpJnt";
	rename -uid "FB8AD212-49C2-62BE-D9E2-D48F6D11F59A";
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
	rename -uid "63780CB5-48C2-843E-3AAE-2B83CF727FC1";
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -2.0892307711238303 2.7850284249333175 0.40527634857571249 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 83.559238175224422 -78.1878578923899 -44.424606013084691 ;
	setAttr ".sd" 1;
	setAttr ".otp" -type "string" "base spread";
createNode joint -n "propLFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "4C2FCF2E-48E8-025F-9B66-13BE44406587";
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
	rename -uid "249477B9-44EE-5A3B-C10E-6FB1E8E9DED7";
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
	rename -uid "0F9F0C3D-4E12-47C5-EB90-AEA620DFAB6B";
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
	rename -uid "BBF46EA5-49E6-396C-1C87-69B48154634B";
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
	rename -uid "9591358C-4DCD-E0DD-2E30-51A2BFC75C80";
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
	rename -uid "28EDBD27-4D00-689F-2070-8E8DF81EFAC4";
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
	rename -uid "1CD5980B-4A85-945C-DAF6-D4A5973D45DD";
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
	rename -uid "078B3598-4729-E12D-6954-8DB8A1FCBE92";
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
	rename -uid "432FFA62-43D6-805F-8DF8-BAB38E87AF12";
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
	rename -uid "C5CE2DEA-40CD-E5AA-8DD6-32A44954ACB2";
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
	rename -uid "6F98C2B9-4CCE-81CB-A0E5-C3A0E5AE9B26";
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
	rename -uid "3ED08B37-46DF-B475-DC75-8C9370EC9189";
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
	rename -uid "A1380BD7-457E-4095-2FAB-5796137542CF";
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
	rename -uid "88550506-4831-8759-327A-6095BF049DB4";
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
	rename -uid "D65881AE-4A19-D947-6FF5-8AA16A5C0295";
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
	rename -uid "84BDB7CF-497C-E2FD-EE63-FDBBCCF0A964";
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
	rename -uid "6F5951BE-4C61-5610-239E-B8934C6A6DD6";
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
	rename -uid "A3FBA77C-4B4C-3DA2-7514-48B068A2D28D";
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
	rename -uid "5A9C6705-493F-9B4D-CEBF-67B919CEF091";
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
	rename -uid "63FC7837-4B5D-C1FD-5799-698C9263F0C7";
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
	rename -uid "C6D80F89-424E-A76E-ACD6-DC95516A2121";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -5.0664606252581734e-06 -1.9997045997810603 2.6320823302228291e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
createNode joint -n "ring04RGT_tmpJnt" -p "ring03RGT_tmpJnt";
	rename -uid "AC75D4C3-4AE2-CA9E-C87E-E3966FC1C3AF";
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
	rename -uid "BE95BEBF-4D01-0012-4213-45BBBC3930D9";
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
	rename -uid "0177C864-4F20-3806-4D2E-629D083FD9A5";
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
	rename -uid "B81BB8AC-4071-C33E-479C-6189E51C5618";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.7276733899128658e-05 -1.6835580527225318 -9.2027594440935445e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
createNode joint -n "pinky04RGT_tmpJnt" -p "pinky03RGT_tmpJnt";
	rename -uid "3D99BA3A-4CB8-DF1F-C3D0-81B6600739AA";
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
	rename -uid "E5BD0A19-4BEA-7151-FA80-B4A85F3945A1";
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 2.0891979254714244 -2.7850014977017086 -0.4052736368999883 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 83.559238175224991 -78.187857892389786 -44.424606013085238 ;
	setAttr ".sd" 1;
	setAttr ".otp" -type "string" "base spread";
createNode joint -n "propRGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "B9871EFC-460A-398F-81D9-0EA17C08BFA2";
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
	rename -uid "00205AFB-4F6B-734B-7850-5F921EA3B811";
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
	rename -uid "B0FAB77F-44F1-770A-D576-1BAD75449D8D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 103.48487111611378 0 1;
	setAttr ".typ" 2;
createNode joint -n "upperLegLFT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "9AB1EA20-457A-07E7-EE51-4FB54D077CB7";
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
	rename -uid "9F7C11E1-4660-2117-391C-54B750E16669";
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
	rename -uid "5E100841-47F3-D865-2E71-EF850930ABC4";
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
	rename -uid "D9F5DDA9-4AED-3B52-6479-989823304376";
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
	rename -uid "70624EBC-487D-2EC6-EEB4-A187A4DB9CE3";
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
	rename -uid "C902BEA6-428A-58A6-13F3-A5B91E1E873A";
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
	rename -uid "BCA37A34-4401-83DB-AB8F-EC9CAEAD5691";
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
	rename -uid "F0C276CD-4B00-2F3A-B57D-F49070FC607B";
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
	rename -uid "AB79ADB9-400E-BEA4-D8A9-FD90562807B3";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -2.6645352591003757e-15 -1.2052411550258419 18.670042035146455 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -3.6935934746626913 4.4139062980501586e-32 180 ;
	setAttr ".radi" 3;
createNode joint -n "upperLegRGT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "F6077C39-438A-CF45-7EB3-AF9B0F6FE763";
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
	rename -uid "EC73FB1D-4E6B-FA4B-7C68-8094258FEE42";
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
	rename -uid "C5E0293B-4F54-2204-1DCE-F087239F5C29";
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
	rename -uid "EB4D524D-46EC-A09A-1B50-B6AE91469E25";
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
	rename -uid "E55312B5-4B1D-09A2-0257-0A9CC15402F6";
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
	rename -uid "3835AFD9-410E-B986-6D42-28A20400E18F";
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
	rename -uid "9E326E34-4C1A-BE42-2528-75B0BABCE82B";
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
	rename -uid "E47B9D7F-4249-1982-0F6C-9BB13F027559";
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
	rename -uid "A1B4C447-418D-5748-A9E8-C6A3A76D36C8";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.4408920985006262e-15 1.2052409198025522 -18.670038391370099 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 176.30640652533728 -4.4139062980501575e-32 -180 ;
	setAttr ".radi" 3;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "19333B5D-478D-1E1C-3703-AEB5F1817122";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "59EDA078-42C2-78E6-A0B2-92B05A0C8B7F";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "42129265-4F80-8BE1-3A77-CD8CAAC90D13";
createNode displayLayerManager -n "layerManager";
	rename -uid "875F6FCD-4BA9-ADAF-319B-3E8908B2584F";
createNode displayLayer -n "defaultLayer";
	rename -uid "E8E7FF6C-409E-61C9-E259-3EB807F780FA";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "A3F2CB67-40D8-24B2-F334-46AAC97D568C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "867DE171-4C6D-D7B7-A2F5-20ADFF68390A";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "5BD6B475-4467-64C7-6BEC-029EA986CDC7";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 1;
	setAttr -av ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".hwi";
	setAttr -av ".ta";
	setAttr -av ".tq";
	setAttr -av ".etmr";
	setAttr -av ".tmr";
	setAttr -av ".aoon";
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr -k on ".hff";
	setAttr -av ".hfd";
	setAttr -av -k on ".hfs";
	setAttr -av ".hfe";
	setAttr -av ".hfc";
	setAttr -av -k on ".hfcr";
	setAttr -av -k on ".hfcg";
	setAttr -av -k on ".hfcb";
	setAttr -av ".hfa";
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
	setAttr -k on ".blen";
	setAttr -k on ".blat";
	setAttr -av ".msaa";
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -cb on ".macc";
	setAttr -cb on ".macd";
	setAttr -cb on ".macq";
	setAttr -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -av -k on ".edl";
	setAttr -cb on ".ren";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -av -cb on ".imfkey";
	setAttr -av -k on ".gama";
	setAttr -av -cb on ".an";
	setAttr -cb on ".ar";
	setAttr ".fs" 1;
	setAttr ".ef" 10;
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -av -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -av -cb on ".pff";
	setAttr -av -cb on ".peie";
	setAttr -av -cb on ".ifp";
	setAttr -k on ".rv";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -cb on ".sosl";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -av -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".mbso";
	setAttr -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -k on ".pram";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -cb on ".ope";
	setAttr -cb on ".oppf";
	setAttr -av -k on ".rcp";
	setAttr -av -k on ".icp";
	setAttr -av -k on ".ocp";
	setAttr -cb on ".hbl";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -av -k off -cb on ".fbfm";
	setAttr -av -k off -cb on ".ehql";
	setAttr -av -k off -cb on ".eams";
	setAttr -av -k off -cb on ".eeaa";
	setAttr -av -k off -cb on ".engm";
	setAttr -av -k off -cb on ".mes";
	setAttr -av -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -av -k off -cb on ".mbs";
	setAttr -av -k off -cb on ".trm";
	setAttr -av -k off -cb on ".tshc";
	setAttr -av -k off -cb on ".enpt";
	setAttr -av -k off -cb on ".clmt";
	setAttr -av -k off -cb on ".tcov";
	setAttr -av -k off -cb on ".lith";
	setAttr -av -k off -cb on ".sobc";
	setAttr -av -k off -cb on ".cuth";
	setAttr -av -k off -cb on ".hgcd";
	setAttr -av -k off -cb on ".hgci";
	setAttr -av -k off -cb on ".mgcs";
	setAttr -av -k off -cb on ".twa";
	setAttr -av -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "root.s" "cog_tmpJnt.is";
connectAttr "cog_tmpJnt.s" "spine01_tmpJnt.is";
connectAttr "spine01_tmpJnt.s" "spine02_tmpJnt.is";
connectAttr "spine02_tmpJnt.s" "spine03_tmpJnt.is";
connectAttr "spine03_tmpJnt.s" "spine04_tmpJnt.is";
connectAttr "spine04_tmpJnt.s" "neck_tmpJnt.is";
connectAttr "neck_tmpJnt.s" "head01_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eyeLFT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eyeRGT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eye_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTargetRGT_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTargetLFT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "headTop_tmpJnt.is";
connectAttr "headTop_tmpJnt.s" "head02_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "headBottom_tmpJnt.is";
connectAttr "headBottom_tmpJnt.s" "jaw01Lwr_tmpJnt.is";
connectAttr "jaw01Lwr_tmpJnt.s" "jaw02Lwr_tmpJnt.is";
connectAttr "jaw02Lwr_tmpJnt.s" "jaw03Lwr_tmpJnt.is";
connectAttr "headBottom_tmpJnt.s" "jaw01Upr_tmpJnt.is";
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
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of templateJoint_biped_extFacial.ma
