//Maya ASCII 2018 scene
//Name: templateJoint_biped_hi.ma
//Last modified: Wed, Apr 21, 2021 10:23:48 AM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -n "template_ctrl";
	rename -uid "00F2DFE7-45C7-918E-05F0-21A3783912B9";
	addAttr -ci true -sn "comment" -ln "comment" -dt "string";
	setAttr -l on -k off ".v";
	setAttr -l on -k on ".comment" -type "string" "this template is for having 5 finger joint";
createNode nurbsCurve -n "template_ctrlShape" -p "template_ctrl";
	rename -uid "197C0CD9-4FB0-81AA-A9D8-F68EFB4B4E4E";
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
	rename -uid "0AA9BC50-4F4D-3A32-55B6-408BF235D6EC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 0 0 1;
	setAttr ".radi" 0.5;
createNode joint -n "cog_tmpJnt" -p "root";
	rename -uid "7BF73595-40C3-FDD0-3E60-D5BF588F1F1C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ovc" 15;
	setAttr ".t" -type "double3" 0 49.206240451110233 1.3234605691345716 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 110.89219816924373 0.5817317347463723 1;
	setAttr ".dl" yes;
	setAttr ".typ" 18;
	setAttr ".otp" -type "string" "COG";
createNode joint -n "spine01_tmpJnt" -p "cog_tmpJnt";
	rename -uid "EB56E7F0-47BA-D278-3926-EA82C2C571C3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".ove" yes;
	setAttr ".t" -type "double3" 0 1.760546899160282 -0.4100593188253735 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 115.97688088568215 1.638809891990324 1;
createNode joint -n "spine02_tmpJnt" -p "spine01_tmpJnt";
	rename -uid "7A7B9816-4159-32C1-CFD9-2DB3085ED3A6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 4.3472279495527246 0.28925147949545205 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 124.85510799594223 3.421218434598865 1;
	setAttr ".typ" 6;
createNode joint -n "spine03_tmpJnt" -p "spine02_tmpJnt";
	rename -uid "135FEFA7-48BE-B5AF-62CC-E79DDCC7F0E4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 6.2894404656637235 -0.68261042201022648 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 139.05166856595392 2.6655195481726714 1;
createNode joint -n "spine04_tmpJnt" -p "spine03_tmpJnt";
	rename -uid "2285AD16-49DA-4087-C7E9-15A2938255CF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 3.9643925792914487 -0.32916127108306459 ;
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766735 0 0 0 0 2.2572056524766735 0
		 0 148.00011790456719 0.43085775501548795 1;
	setAttr ".typ" 6;
createNode joint -n "clavLFT_tmpJnt" -p "spine04_tmpJnt";
	rename -uid "0D6F496F-46D4-8385-970E-D4822494EE0B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 1.6636444217215913 -0.98384906841826592 1.0292657376910188 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 3.7551875924212634 145.77936822614953 2.7541221960322289 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "upperArmLFT_tmpJnt" -p "clavLFT_tmpJnt";
	rename -uid "3908B705-417E-FDFC-F1F6-FC9222381786";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.9983401960907217 1.0954513473278809 -2.7157728773674537 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -3.1672506203428572 4.1562551900270126 -127.36140407964923 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "lowerArmLFT_tmpJnt" -p "upperArmLFT_tmpJnt";
	rename -uid "B2B26A67-414C-C969-AD19-BB8672A768B1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 3.5527136788005009e-14 14.894761361963656 -1.7763568394002505e-15 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 10.524179068855664 -13.317008616570469 -1.6408560625667801 ;
	setAttr ".bps" -type "matrix" -1.4006199132373915 -1.7549533389677487 0.23104110946210146 0
		 1.7548216048946899 -1.4152761192647916 -0.11212492500003585 0 0.23203954665175947 0.11004381789718293 2.242548854429911 0
		 36.58775806427002 128.66083526611328 -11.438733339309692 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "handLFT_tmpJnt" -p "lowerArmLFT_tmpJnt";
	rename -uid "592BB629-4B62-7A41-0F11-29BA89E469A8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.9737991503207013e-14 9.3318551482346024 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -6.3045753992097167 8.2564104755060779 0.082265279359387392 ;
	setAttr ".bps" -type "matrix" -1.1425486938383038 -1.9456871570843366 -0.062139573044116159 0
		 1.9466586471973824 -1.1416234555382549 -0.046833264131358118 0 0.0089415363718770291 -0.077296378276171654 2.2558640642568304 0
		 52.824464797973633 117.74364089965817 -10.812332153320309 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "handLFT_prop_jnt" -p "handLFT_tmpJnt";
	rename -uid "096B24C7-42DA-8079-C0ED-5B89013F1DD6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 0 6.6958443414345741 1.6825082993499052e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 18.739948874104801 0 ;
	setAttr ".bps" -type "matrix" 2.0211694160679943 0.97154585376466329 -0.25680771631066757 0
		 -0.90601840470197903 2.0112903362471197 0.4783504899473574 0 0.43472082934371808 -0.32524943493307901 2.1909376903926479 0
		 58.891023006333263 104.27635388271605 -14.015292574656838 1;
	setAttr ".dl" yes;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
	setAttr ".oclr" -type "float3" 0.40000001 0.40000001 0.40000001 ;
createNode joint -n "thumb01LFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "FDED0864-4478-0A15-3FB5-0EB81E471A5F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.2168213748461767 1.0195473502027976 2.0860180664669348 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 83.282226748843229 -17.222674086135243 -66.320146596647959 ;
	setAttr ".bps" -type "matrix" -1.9292247829251112 0.3523100682868977 1.1175628440064949 0
		 0.93808943375450948 -0.82566347927261774 1.8796928980145207 0 0.70218039619341954 2.0710226440944011 0.55927207727771955 0
		 55.613149462896928 114.39107448747276 -9.5984222125244933 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "thumb02LFT_tmpJnt" -p "thumb01LFT_tmpJnt";
	rename -uid "99EBC1B9-499F-1DC1-6B4F-7DA942E893F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.25649261402844559 2.2507511968495555 -0.12490843316540889 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -16.311254366107697 22.42338595060939 27.138130319200613 ;
	setAttr ".bps" -type "matrix" -1.8670305603142436 -0.57221142405374725 1.1321432465053674 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 57.361130408373768 112.85258148540528 -6.0959124827992408 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "thumb03LFT_tmpJnt" -p "thumb02LFT_tmpJnt";
	rename -uid "470649DE-4579-ECF3-209C-56B961232482";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.0302869668521453e-13 2.5261692415110453 3.5527136788005009e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0 3.1805546814635168e-15 0 ;
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "thumb04LFT_tmpJnt" -p "thumb03LFT_tmpJnt";
	rename -uid "867C2508-4FDC-A997-672F-7599662CCAA0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.4210854715202004e-14 1.8828534968703727 3.5527136788005009e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0 3.1805546814635168e-15 0 ;
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "pinkyBaseLFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "586AB2D5-4EA4-D264-34D6-8C95816E33FB";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.7162289594310991 -1.9970960816912378 -2.3183177897968523 ;
	setAttr ".r" -type "double3" 1.6948380758848785e-12 1.3268876561730515e-12 6.2338871756686879e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.2552561012555858 252.1367054901647 30.152775544048776 ;
	setAttr ".radi" 0.5;
createNode joint -n "pinky01LFT_tmpJnt" -p "pinkyBaseLFT_tmpJnt";
	rename -uid "C67C008C-4F67-A982-2C19-52B669DA13E3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.4033219031261979e-13 2.5377470362008836 -5.6843418860808015e-14 ;
	setAttr ".r" -type "double3" -1.4801506348860801e-12 -3.2948558653287821e-13 -1.3178429537976444e-12 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -15.644840265318507 -16.990815779745684 5.3446575020763323 ;
	setAttr ".bps" -type "matrix" 1.0794628981158811 -0.058762086411279196 1.9814853586046262 0
		 1.4215420704544786 -1.5495750168189177 -0.82037355317641203 0 1.3816495037063139 1.6402260947881213 -0.70404571190857501 0
		 62.205154990637126 111.73991274880089 -16.463022243221697 1;
	setAttr ".radi" 0.5;
createNode joint -n "pinky02LFT_tmpJnt" -p "pinky01LFT_tmpJnt";
	rename -uid "BC098C3B-46EB-71F9-6A77-B5846A689246";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 7.815970093361102e-14 2.9356845782505046 1.3500311979441904e-13 ;
	setAttr ".r" -type "double3" -1.1134053472215568e-12 1.1833433840989926e-12 -9.5687775741977957e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.5408151166151658 1.0155772181039755 4.9105814153408343 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 64.832687829787858 108.35094778363963 -17.922809609624039 1;
	setAttr ".radi" 0.5;
createNode joint -n "pinky03LFT_tmpJnt" -p "pinky02LFT_tmpJnt";
	rename -uid "EB4912CE-4002-7562-A4F1-C2849AFE822B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.2382096176443156e-13 3.0348067318408587 2.8421709430404007e-14 ;
	setAttr ".r" -type "double3" 1.012820305420263e-12 -2.5842006786885555e-14 -6.2371174265168557e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.4423381518481384 -2.1125168880449183 0.27155308219162322 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
	setAttr ".radi" 0.5;
createNode joint -n "pinky04LFT_tmpJnt" -p "pinky03LFT_tmpJnt";
	rename -uid "856FF544-48AA-42D9-BBAC-DBA50872EAFA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 1.2789769243681803e-13 2.691140443303321 2.6290081223123707e-13 ;
	setAttr ".r" -type "double3" -3.7272125173400585e-16 7.9513867036587919e-16 8.0756271209034607e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 3.1805546814635168e-15 0 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
	setAttr ".radi" 0.5;
createNode joint -n "ringBaseLFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "2734A989-4258-9298-9FA8-72A850BC31C8";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.3466488348176853 -2.3366455804974144 -1.1329413252090261 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 80.909301190979633 -79.484224592544209 -49.039461710006833 ;
	setAttr ".radi" 0.5;
createNode joint -n "ring01LFT_tmpJnt" -p "ringBaseLFT_tmpJnt";
	rename -uid "406EF626-42C4-E867-81B3-22A5B2CDB7C4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.2079226507921703e-13 3.6144954895512953 2.2026824808563106e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -20.111364662281503 -6.9832973424127518 3.0998270093486298 ;
	setAttr ".bps" -type "matrix" -0.12299867417619993 0.038889901762868689 2.2535164208996612 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.170254213498513 1.9299088122531929 0.030568116544767172 0
		 63.101856530072354 112.66335954985358 -14.311344503683257 1;
	setAttr ".radi" 0.5;
createNode joint -n "ring02LFT_tmpJnt" -p "ring01LFT_tmpJnt";
	rename -uid "077DB0B4-440E-3D4E-6113-A5A9A3F26403";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.3344880755994382e-13 4.0719291931879216 -1.0658141036401503e-13 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.2695633294678057 3.957114679145044 -0.29326564991010673 ;
	setAttr ".bps" -type "matrix" -0.20143743016798987 -0.29068663250527088 2.2293276118558052 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402449 1.1478616308859193 0.32284746254245783 0
		 66.993758410796886 108.45338229160024 -14.867414758093657 1;
	setAttr ".radi" 0.5;
createNode joint -n "ring03LFT_tmpJnt" -p "ring02LFT_tmpJnt";
	rename -uid "6B33B3E6-42AF-DCDB-C5DE-0AA6C88C7F3B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.3964831775156199e-14 3.8582630780063596 -1.0658141036401503e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.3409493593460553 -0.40247575563500226 -1.6830172425310328 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
	setAttr ".radi" 0.5;
createNode joint -n "ring04LFT_tmpJnt" -p "ring03LFT_tmpJnt";
	rename -uid "2C22057C-4997-C3E5-8105-7F9F612A5755";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 7.8381745538536052e-14 2.5395488469730827 2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 3.1805546814635168e-15 0 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
	setAttr ".radi" 0.5;
createNode joint -n "middleBaseLFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "C7017EFA-44C6-ED09-1705-BFA3E71031BC";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.2144035198093803 -2.3429230648881862 0.014742439823252526 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 47.253496025354686 -71.247737670343781 -25.342573920280227 ;
	setAttr ".radi" 0.5;
createNode joint -n "middle01LFT_tmpJnt" -p "middleBaseLFT_tmpJnt";
	rename -uid "61AC4851-4896-5EED-05DB-5A9B88CC5275";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0.048418710319408476 4.0995050648693772 0.022973442504600428 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -0.07855072237619086 2.4191478724138546 0.63587220690795465 ;
	setAttr ".bps" -type "matrix" -0.12299867417619968 0.038889901762869106 2.2535164208996616 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.1702542134985132 1.9299088122531931 0.030568116544766679 0
		 62.950811016387775 112.71111734259617 -11.543968776495438 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "middle02LFT_tmpJnt" -p "middle01LFT_tmpJnt";
	rename -uid "1E76535C-47A6-224A-EAA2-CBB33E8EF075";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.29538670449846549 3.2933531612545206 -0.52375822500411573 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999956 0.99999999999999967 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -18.881492046128145 16.802435263098481 -8.0844170874091805 ;
	setAttr ".bps" -type "matrix" -0.20143743016798973 -0.29068663250527049 2.2293276118558056 0
		 1.1752615749089648 -1.9216899634424138 -0.14437891992889554 0 1.9165491253402447 1.1478616308859197 0.3228474625424575 0
		 67.715255810002049 108.22407346356407 -12.127039229244525 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "middle03LFT_tmpJnt" -p "middle02LFT_tmpJnt";
	rename -uid "A8464C8C-41CE-75B5-74E9-BA800DA6E1E0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.29937280027887425 3.7753091816976214 0.44772382012503442 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0 -3.1805546814635168e-15 0 ;
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "middle04LFT_tmpJnt" -p "middle03LFT_tmpJnt";
	rename -uid "F47A61E1-478B-4C18-5614-9AA295B4E72C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 0.43314509008794744 2.5705493146996594 -0.06643589748293266 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0 -3.1805546814635168e-15 0 ;
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "indexBaseLFT_tmpJnt" -p "handLFT_tmpJnt";
	rename -uid "E6301090-4E36-588B-A6E7-54808D093A80";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -0.89758078220361881 -2.3739699360625277 0.93540500303403862 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 48.042143574917581 -56.932624130087 -31.299288009693978 ;
	setAttr ".radi" 0.5;
createNode joint -n "index01LFT_tmpJnt" -p "indexBaseLFT_tmpJnt";
	rename -uid "C23A1008-4FA3-950D-9118-A4B34A4AC1C6";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.0658141036401503e-14 4.2101647864737295 -9.2370555648813024e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.3855413439249067 5.5733914743769093 3.0206541225265462 ;
	setAttr ".radi" 0.5;
createNode joint -n "index02LFT_tmpJnt" -p "index01LFT_tmpJnt";
	rename -uid "2E182650-454E-D032-7F07-EA896F854A93";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -8.5265128291212022e-14 3.5144809794240803 4.2632564145606011e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.839734946170269 0.44915283199530293 -1.0322458661159066 ;
	setAttr ".radi" 0.5;
createNode joint -n "index03LFT_tmpJnt" -p "index02LFT_tmpJnt";
	rename -uid "35217C05-4B42-53F6-96C7-95BDCF761265";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 2.4868995751603507e-14 3.3461307119009467 2.8421709430404007e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -11.123506380904304 2.914298951009398 -13.587338141135568 ;
	setAttr ".radi" 0.5;
createNode joint -n "index04LFT_tmpJnt" -p "index03LFT_tmpJnt";
	rename -uid "323C69E2-4880-5955-B0F6-2E80E9146C84";
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 3.907985046680551e-14 2.7277723669652767 5.6843418860808015e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -3.1805546814635168e-15 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "armLFT_pov_tmpJnt" -p "lowerArmLFT_tmpJnt";
	rename -uid "4CA57A4F-49C2-B7C4-5815-A18B772431A3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.5598404110899509 -1.9752827068693648 -15.626254474430137 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 11.690518081224996 9.5416640443905535e-15 127.65530493713308 ;
	setAttr ".bps" -type "matrix" 0.99815258060496437 8.9981312040783247e-10 0.060757105194783181 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 -0.060757105194783181 -5.4770116136011496e-11 0.99815258060496437 0
		 40.855079650878928 143.65834045410159 -6.71590328216549 1;
	setAttr ".radi" 3;
createNode joint -n "neck_tmpJnt" -p "spine04_tmpJnt";
	rename -uid "0629CCEF-4B0D-9A00-47C3-D18C89B8EFE1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 2.3453367998573071 -1.8392936999519613 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 153.29402538616662 -3.7208063810808136 1;
	setAttr ".typ" 7;
	setAttr ".radi" 0.5;
createNode joint -n "head01_tmpJnt" -p "neck_tmpJnt";
	rename -uid "9F5AE477-4873-CF17-4105-24985458829D";
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
	setAttr ".radi" 0.5;
createNode joint -n "head02_tmpJnt" -p "head01_tmpJnt";
	rename -uid "694B50AF-4161-C5FD-1045-E68418D7AF7A";
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
	setAttr ".radi" 5;
createNode joint -n "eyeLFT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "F53AC8B8-4655-070A-83B8-C487AC4F47F0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.8239219872507531 2.6158880095642019 2.6483026590950898 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "jaw01Lwr_tmpJnt" -p "head01_tmpJnt";
	rename -uid "846B50BA-4303-D4FD-7A07-76A25B630FEE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.6747740263279888e-16 0.85186845196689376 0.85055887360982263 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 2.8444367822037024e-14 0 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -5.6817911712458105e-17 -0.46395345786243802 0.8858595763085072 0 1.0848650946202438e-16 0.8858595763085072 0.46395345786243802 0
		 -2.281527907856237e-09 138.24609308456581 1.2332340767044465 1;
createNode joint -n "jaw02Lwr_tmpJnt" -p "jaw01Lwr_tmpJnt";
	rename -uid "9E2AF7A4-4FC2-B79C-6D31-CDAC2C1779A1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.45346939366313e-16 -1.8375419927605208 2.2988962736372129 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661394e-09 134.88585971678842 7.6491683844072185 1;
createNode joint -n "jaw03Lwr_tmpJnt" -p "jaw02Lwr_tmpJnt";
	rename -uid "1199E5E8-4531-77DB-05BE-BF8E08E48994";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3956450219389744e-17 -1.4210854715202004e-14 1.9710502458233852 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661419e-09 134.88585971678845 9.7309712720145338 1;
createNode joint -n "eyeRGT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "127ED8FF-4699-44B6-2195-8990ADC82DE2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.8239219872507531 2.6158880095642019 2.6483026590950898 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eye_tmpJnt" -p "head01_tmpJnt";
	rename -uid "A607E0A5-4EA4-D000-B3FC-45BD4BD24ED4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 2.6528101527827932 20 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetRGT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "C37FF74C-49AB-5C3A-3201-2C82520AFCC5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.824 -0.00010040181385306823 3.5527136788005009e-15 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetLFT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "F3C09B2A-482A-39F3-FFCE-CDB6A19D9C3D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.824 1.4210854715202004e-14 0 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.5196086821242486e-22 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "jaw01Upr_tmpJnt" -p "head01_tmpJnt";
	rename -uid "85FF1A3A-4E92-63E2-4638-E7B74BB5A398";
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
	rename -uid "8E1A993D-4F99-2A3A-4547-1089AB27CD4B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.3956450219400147e-17 2.8421709430404007e-14 2.1995495613608833 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 0 0 -2.4651903288156624e-32 -2.2204460492503136e-16 1.0000000000000002 0
		 1.2246467991473532e-16 1 2.2204460492503131e-16 0 -2.2815279078562374e-09 137.53090779923286 10.215768076274593 1;
createNode joint -n "clavRGT_tmpJnt" -p "spine04_tmpJnt";
	rename -uid "8A4B75F8-4992-F51E-45CC-91A0B3BD500D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -1.66364 -0.98384834477840855 1.0292689632886411 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -180 0 0 ;
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 3.7551875924212634 145.77936822614953 2.7541221960322289 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
	setAttr ".radi" 0.5;
createNode joint -n "upperArmRGT_tmpJnt" -p "clavRGT_tmpJnt";
	rename -uid "187ED1B8-4A51-ACB8-5C05-559B85E65767";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.99834 -1.0955000000000013 2.7157799999999996 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -3.1672506203427604 4.1562551900270073 -127.36140407964923 ;
	setAttr ".bps" -type "matrix" -1.3744118257180622 -1.7904393550384567 0.017216469686458489 0
		 1.7391097749788855 -1.3400494091369772 -0.52415849627491007 0 0.4259890626200164 -0.30589516925535037 2.1954359069503733 0
		 10.52305803108526 148.25202719935152 -3.3759356936044287 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "lowerArmRGT_tmpJnt" -p "upperArmRGT_tmpJnt";
	rename -uid "B4FBE61F-47A0-5765-CCAF-248D4E5F800D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -5.3051604979259537e-05 -14.894803190304206 -9.4425268013509367e-06 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 10.524179068855489 -13.317008616570465 -1.6408560625667596 ;
	setAttr ".bps" -type "matrix" -1.4006199132373915 -1.7549533389677487 0.23104110946210146 0
		 1.7548216048946899 -1.4152761192647916 -0.11212492500003585 0 0.23203954665175947 0.11004381789718293 2.242548854429911 0
		 36.58775806427002 128.66083526611328 -11.438733339309692 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "handRGT_tmpJnt" -p "lowerArmRGT_tmpJnt";
	rename -uid "CECC5D50-4FA9-CF61-37AB-1F895F4AE72B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.8402285423112517e-05 -9.3317918044468762 -1.2313800135999031e-05 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -6.3045753992094813 8.2564104755060512 0.082265279359407611 ;
	setAttr ".bps" -type "matrix" -1.1425486938383038 -1.9456871570843366 -0.062139573044116159 0
		 1.9466586471973824 -1.1416234555382549 -0.046833264131358118 0 0.0089415363718770291 -0.077296378276171654 2.2558640642568304 0
		 52.824464797973633 117.74364089965817 -10.812332153320309 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
	setAttr ".radi" 0.5;
createNode joint -n "handRGT_prop_jnt" -p "handRGT_tmpJnt";
	rename -uid "1A74D24B-4B1F-7591-DAE8-7B87EFC6B706";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -1.0711271002605827e-05 -6.6959016512175253 -2.7426859400304926e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.207418262772186e-06 18.739948874104815 -4.2140011638314698e-14 ;
	setAttr ".bps" -type "matrix" 2.0211694160679943 0.97154585376466329 -0.25680771631066757 0
		 -0.90601840470197903 2.0112903362471197 0.4783504899473574 0 0.43472082934371808 -0.32524943493307901 2.1909376903926479 0
		 58.891023006333263 104.27635388271605 -14.015292574656838 1;
	setAttr ".dl" yes;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
	setAttr ".oclr" -type "float3" 0.40000001 0.40000001 0.40000001 ;
createNode joint -n "thumb01RGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "9D4BF24B-44C5-EEB7-04DB-3EB8FD366FF2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.2168720941948763 -1.019594904875909 -2.0860177508740985 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 83.282226748843073 -17.222674086135367 -66.320146596647959 ;
	setAttr ".bps" -type "matrix" -1.9292247829251112 0.3523100682868977 1.1175628440064949 0
		 0.93808943375450948 -0.82566347927261774 1.8796928980145207 0 0.70218039619341954 2.0710226440944011 0.55927207727771955 0
		 55.613149462896928 114.39107448747276 -9.5984222125244933 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "thumb02RGT_tmpJnt" -p "thumb01RGT_tmpJnt";
	rename -uid "E3B8FB11-45AA-1AE3-0A1F-5FB7A2A1077E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.25649165273879859 -2.2507488005944989 0.12484667596201859 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -16.311254366107637 22.423385950609386 27.138130319200631 ;
	setAttr ".bps" -type "matrix" -1.8670305603142436 -0.57221142405374725 1.1321432465053674 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 57.361130408373768 112.85258148540528 -6.0959124827992408 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "thumb03RGT_tmpJnt" -p "thumb02RGT_tmpJnt";
	rename -uid "2E8E45C7-4FAC-F3B5-347C-A8BC3A1A0AB1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 3.6836131226181124e-05 -2.5262023118173191 -3.4529642931602211e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "thumb04RGT_tmpJnt" -p "thumb03RGT_tmpJnt";
	rename -uid "9EF5F421-4875-0032-6C8A-72823100D0C8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -3.8004303569039166e-05 -1.8828515822726133 4.2298619227665313e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -1.8670305603142432 -0.57221142405374714 1.1321432465053671 0
		 1.0711651635057355 -1.7903123862259391 0.86160554187537652 0 0.67954355041973624 1.2499331996074883 1.7523883465643608 0
		 60.067074897000246 108.32994940262525 -3.9193510645981413 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
	setAttr ".radi" 0.5;
createNode joint -n "pinkyBaseRGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "BD962799-4D14-BF15-519B-1EB4C16102BB";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 1.7161868788748436 1.9970383562780221 2.3183152146402 ;
	setAttr ".r" -type "double3" 1.6948380758848785e-12 1.3268876561730515e-12 6.2338871756686879e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.2552561012558656 252.13670549016476 30.152775544048342 ;
	setAttr ".radi" 0.5;
createNode joint -n "pinky01RGT_tmpJnt" -p "pinkyBaseRGT_tmpJnt";
	rename -uid "0C3DA250-469C-4FA1-DC09-4FB581E7B6D7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.1567237392948755e-06 -2.5377530283082912 1.4217862826626515e-05 ;
	setAttr ".r" -type "double3" -1.4801506348860801e-12 -3.2948558653287821e-13 -1.3178429537976444e-12 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -15.644840265318399 -16.990815779745649 5.3446575020762914 ;
	setAttr ".bps" -type "matrix" 1.0794628981158811 -0.058762086411279196 1.9814853586046262 0
		 1.4215420704544786 -1.5495750168189177 -0.82037355317641203 0 1.3816495037063139 1.6402260947881213 -0.70404571190857501 0
		 62.205154990637126 111.73991274880089 -16.463022243221697 1;
	setAttr ".radi" 0.5;
createNode joint -n "pinky02RGT_tmpJnt" -p "pinky01RGT_tmpJnt";
	rename -uid "34D238C7-4E58-18AA-13DF-1EB520AC8A4E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.5745117735832537e-05 -2.9356869153929166 -3.0707320448186692e-05 ;
	setAttr ".r" -type "double3" -1.1134053472215568e-12 1.1833433840989926e-12 -9.5687775741977957e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.5408151166152493 1.0155772181039682 4.9105814153408192 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 64.832687829787858 108.35094778363963 -17.922809609624039 1;
	setAttr ".radi" 0.5;
createNode joint -n "pinky03RGT_tmpJnt" -p "pinky02RGT_tmpJnt";
	rename -uid "9AB28975-46C3-7E07-B69C-C080A6422644";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -8.479515532400228e-06 -3.0347764549405891 -8.1444404642638801e-06 ;
	setAttr ".r" -type "double3" 1.012820305420263e-12 -2.5842006786885555e-14 -6.2371174265168557e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.442338151847752 -2.1125168880447189 0.27155308219159507 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
	setAttr ".radi" 0.5;
createNode joint -n "pinky04RGT_tmpJnt" -p "pinky03RGT_tmpJnt";
	rename -uid "B81AF9E8-4EA1-A1D8-8427-8E9042B0EFAD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 1.5450079089873725e-05 -2.691161358955148 1.509848618752585e-05 ;
	setAttr ".r" -type "double3" -3.7272125173400585e-16 7.9513867036587919e-16 8.0756271209034607e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1.3216378545460152 0.087066046027842431 1.8277500492771792 0
		 0.69762084247148648 -2.1083345790675505 -0.40401462898028229 0 1.691619312715785 0.80145003831167139 -1.2613799168013742 0
		 65.904963884273641 104.75563693005263 -18.526902671640553 1;
	setAttr ".radi" 0.5;
createNode joint -n "ringBaseRGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "65EC244A-4A81-A0A1-EECF-05B9E05BB2BD";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 1.346645242861868 2.3366415263082772 1.1329430154730942 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 80.909301190979036 -79.484224592544294 -49.039461710006208 ;
	setAttr ".radi" 0.5;
createNode joint -n "ring01RGT_tmpJnt" -p "ringBaseRGT_tmpJnt";
	rename -uid "7B0EAA4B-463F-08A0-B005-FD84CAB52594";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 4.6203851935544549e-06 -3.6145624256600257 3.1391909608657897e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -20.111364662281492 -6.9832973424127145 3.0998270093485942 ;
	setAttr ".bps" -type "matrix" -0.12299867417619993 0.038889901762868689 2.2535164208996612 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.170254213498513 1.9299088122531929 0.030568116544767172 0
		 63.101856530072354 112.66335954985358 -14.311344503683257 1;
	setAttr ".radi" 0.5;
createNode joint -n "ring02RGT_tmpJnt" -p "ring01RGT_tmpJnt";
	rename -uid "A682B500-4AAD-1538-0D51-D4B17F4D0E47";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 5.4674971621260227e-06 -4.0718897881687202 5.4565926319583014e-05 ;
	setAttr ".s" -type "double3" 0.99999999999999978 1 0.99999999999999978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -9.2695633294677791 3.9571146791449321 -0.2932656499100677 ;
	setAttr ".bps" -type "matrix" -0.20143743016798987 -0.29068663250527088 2.2293276118558052 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402449 1.1478616308859193 0.32284746254245783 0
		 66.993758410796886 108.45338229160024 -14.867414758093657 1;
	setAttr ".radi" 0.5;
createNode joint -n "ring03RGT_tmpJnt" -p "ring02RGT_tmpJnt";
	rename -uid "7A385F9F-4FE2-84B8-540A-94AFCA466F6A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.8997536583853503e-06 -3.8582656652793554 -3.6862119863201315e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.3409493593459105 -0.4024757556348656 -1.6830172425308108 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
	setAttr ".radi" 0.5;
createNode joint -n "ring04RGT_tmpJnt" -p "ring03RGT_tmpJnt";
	rename -uid "1F259746-4352-3C26-A9BC-66B456CF13F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -2.3698123357007717e-06 -2.5395471678461368 4.9871681824242842e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -0.20143743016798993 -0.29068663250527094 2.2293276118558056 0
		 1.1752615749089654 -1.9216899634424149 -0.14437891992889576 0 1.9165491253402454 1.1478616308859195 0.32284746254245789 0
		 68.991267376956372 104.41680464445054 -15.167125438614308 1;
	setAttr ".radi" 0.5;
createNode joint -n "middleBaseRGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "7456465B-4B0E-C210-0727-CE812C4537A0";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 1.2143962184245254 2.3429044319015411 -0.01474517386619623 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 47.253496025354295 -71.247737670343838 -25.342573920279804 ;
	setAttr ".radi" 0.5;
createNode joint -n "middle01RGT_tmpJnt" -p "middleBaseRGT_tmpJnt";
	rename -uid "C9380DFB-4CEB-7272-FFC4-C3968FFA523F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -0.048402616755808481 -4.0995398448992368 -0.022998778222415694 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -0.078550722364478451 2.4191478724137725 0.63587220690792068 ;
	setAttr ".bps" -type "matrix" -0.12299867417619968 0.038889901762869106 2.2535164208996616 0
		 1.9262278576306904 -1.1700072262601595 0.1253263282759618 0 1.1702542134985132 1.9299088122531931 0.030568116544766679 0
		 62.950811016387775 112.71111734259617 -11.543968776495438 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "middle02RGT_tmpJnt" -p "middle01RGT_tmpJnt";
	rename -uid "C4FA6CF0-4566-3A55-737E-F49CE0EA48B8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.29540585119479346 -3.2932974542457085 0.52378128671674062 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999956 0.99999999999999967 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -18.881492046140281 16.802435263096918 -8.0844170874126675 ;
	setAttr ".bps" -type "matrix" -0.20143743016798973 -0.29068663250527049 2.2293276118558056 0
		 1.1752615749089648 -1.9216899634424138 -0.14437891992889554 0 1.9165491253402447 1.1478616308859197 0.3228474625424575 0
		 67.715255810002049 108.22407346356407 -12.127039229244525 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "middle03RGT_tmpJnt" -p "middle02RGT_tmpJnt";
	rename -uid "B55D7796-441F-C320-E0AD-20830F360F5F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.29939736353500024 -3.7753676479998255 -0.4476745163458844 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "middle04RGT_tmpJnt" -p "middle03RGT_tmpJnt";
	rename -uid "B65D7108-4678-38CD-CF49-F8BDB0E86477";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -0.43311766576869815 -2.5705662126528313 0.066410417607002614 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 8.5377364625159408e-07 -2.3696978997167325e-23 -1.7655625192200639e-31 ;
	setAttr ".bps" -type "matrix" -0.20143743016798979 -0.29068663250527055 2.2293276118558061 0
		 1.1752615749089652 -1.9216899634424147 -0.14437891992889559 0 1.9165491253402456 1.1478616308859202 0.32284746254245766 0
		 69.852294520573054 104.27895730604915 -12.508467343696475 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
	setAttr ".radi" 0.5;
createNode joint -n "indexBaseRGT_tmpJnt" -p "handRGT_tmpJnt";
	rename -uid "463519D0-473F-38FC-E8E6-159BBF4D0106";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 0.89760037013562055 2.3739163144568458 -0.93540590105688615 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 48.042143574917347 -56.932624130087049 -31.299288009693768 ;
	setAttr ".radi" 0.5;
createNode joint -n "index01RGT_tmpJnt" -p "indexBaseRGT_tmpJnt";
	rename -uid "92E376D2-4F6B-7276-FD3F-FBB44CB1D38C";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -5.9706054607033821e-06 -4.210158127701237 1.6722026693116732e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -2.385541343925333 5.5733914743769404 3.020654122526536 ;
	setAttr ".radi" 0.5;
createNode joint -n "index02RGT_tmpJnt" -p "index01RGT_tmpJnt";
	rename -uid "663B362D-49F1-4D78-5BD8-E5BD9C0D34E9";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" 1.6353886696407471e-05 -3.5145073547914354 -2.1199845932073913e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.83973494617157518 0.44915283199525602 -1.0322458661157903 ;
	setAttr ".radi" 0.5;
createNode joint -n "index03RGT_tmpJnt" -p "index02RGT_tmpJnt";
	rename -uid "1D99C911-4F72-17CA-542E-51AA680E10F4";
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -2.8695985829330084e-05 -3.3461281654135053 4.7989560187033931e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -11.123506380902731 2.9142989510098407 -13.587338141135573 ;
	setAttr ".radi" 0.5;
createNode joint -n "index04RGT_tmpJnt" -p "index03RGT_tmpJnt";
	rename -uid "D23999D8-4C46-1428-9853-4D8DFC1019B1";
	setAttr ".ove" yes;
	setAttr ".ovc" 3;
	setAttr ".t" -type "double3" -3.86481314862408e-06 -2.7277353869500027 -1.912666688497211e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.4787793334710979e-06 -5.7462120146647205e-22 -8.2088750633335376e-23 ;
	setAttr ".radi" 0.5;
createNode joint -n "armRGT_pov_tmpJnt" -p "lowerArmRGT_tmpJnt";
	rename -uid "6FD84623-4844-EABD-04B3-1C80FC76AC90";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.5598440402809999 1.9752845130210801 15.626277666999174 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 11.690518081224671 -5.6454845595977434e-14 127.65530493713308 ;
	setAttr ".bps" -type "matrix" 0.99815258060496437 8.9981312040783247e-10 0.060757105194783181 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 -0.060757105194783181 -5.4770116136011496e-11 0.99815258060496437 0
		 40.855079650878928 143.65834045410159 -6.71590328216549 1;
	setAttr ".radi" 3;
createNode joint -n "hip_tmpJnt" -p "cog_tmpJnt";
	rename -uid "50DEE13A-4089-AEC9-560C-8981CB103DF7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -1.6589548580831082 0.005252352934912885 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 2.2572056524766739 0 0 0 0 2.2572056524766739 0 0 0 0 2.2572056524766739 0
		 0 103.48487111611378 0 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.5;
createNode joint -n "upperLegLFT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "1033F175-499F-12D9-3D29-068D4C6F212F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 4.1020196177146797 -4.9209490559431615 -1.4730898928435754 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0 0 180 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.5;
createNode joint -n "lowerLegLFT_tmpJnt" -p "upperLegLFT_tmpJnt";
	rename -uid "49DEFA56-4219-E5E4-48E9-8781DB3284C3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.13950303839991918 12.786643256625833 0.75525254473979486 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.5924072265625 67.79876708984375 1.4713684320449825 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.5;
createNode joint -n "ankleLFT_tmpJnt" -p "lowerLegLFT_tmpJnt";
	rename -uid "B82C8DE0-4965-1E7B-38AD-F686CC0790D3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -0.20050474863411427 26.549133532081154 -3.1662032127003821 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 10.026567459106442 25.278465270996087 -5.7832069396972638 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.5;
createNode joint -n "heelRollLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "ADA44532-4C9C-EA83-65C6-DCA5C48610A6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.033340069789104199 3.0947476126643974 -2.6025350751851821 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 180 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 2.7642796773228715e-16 2.2572056524766739 2.7642796773228715e-16 0
		 3.3852662587815329e-32 2.7642796773228715e-16 -2.2572056524766739 0 9.951313972473141 0.44198825955391641 -11.657663345336907 1;
	setAttr ".radi" 0.5;
createNode joint -n "footInLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "ABEAC613-420C-BC1A-72CB-2FA4110C1024";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.1453625871492257 3.2916306108357674 3.5567496503932015 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -90.000000000004192 89.999999999999943 0 ;
	setAttr ".bps" -type "matrix" -2.0048013493549223e-15 2.4551735554138001e-31 -2.2572056524766739 0
		 2.2572056524766739 1.651196833540488e-13 -2.0048013493549223e-15 0 1.649943832697141e-13 -2.2572056524766739 0 0
		 14.869093924780286 -0.0024171567950581618 2.2451089524518615 1;
	setAttr ".radi" 0.5;
createNode joint -n "footOutLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "DFF479D1-4795-635C-08B5-A99FA8E11901";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.1907646984344384 3.2916306108359201 3.5567496907259 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -180 -89.999999999999957 0 ;
	setAttr ".bps" -type "matrix" -1.7542011806855572e-15 2.1482768609870751e-31 2.2572056524766739 0
		 0 2.2572056524766739 -2.2257766178534174e-31 0 -2.2572056524766739 0 -1.5036010120161916e-15 0
		 5.0815629059024978 -0.0024171567953992223 2.245109043491059 1;
	setAttr ".radi" 0.5;
createNode joint -n "ballLFT_tmpJnt" -p "ankleLFT_tmpJnt";
	rename -uid "1DA9A835-40E1-1248-7394-198D0E2C4C74";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0.033340069789105087 3.2775314875556401 4.1384630622823444 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 90.863171496667746 0 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 4.1642808448503742e-18 0.034003933605589051 2.2569495098632566 0
		 2.7639659930912251e-16 2.2569495098632566 -0.034003933605589051 0 9.9513139724731374 0.029407463967817904 3.9547955989837629 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 0.5;
createNode joint -n "toesTipLFT_tmpJnt" -p "ballLFT_tmpJnt";
	rename -uid "6EDBDBAB-4628-F14B-0987-559E14A6391C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.6645352591003757e-15 7.1965674742258825 -0.0026471785861566718 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -1.9994200605091257 0.31657387116730312 8.9934785386618881 ;
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 0.5;
createNode joint -n "legLFT_pov_tmpJnt" -p "lowerLegLFT_tmpJnt";
	rename -uid "A7B7F127-4E2A-9992-C73E-8D9DB02E7DA9";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.7763568394002505e-15 -0.57523165258364983 19.28788439633524 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0 0 -180 ;
	setAttr ".radi" 3;
createNode joint -n "upperLegRGT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "908A006C-4747-1B41-D0B6-ED8D7982160F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -4.1020203810367741 -4.92096747162703 -1.473089971249812 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.2591018676757777 102.72009288869495 -0.29758316278457636 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.5;
createNode joint -n "lowerLegRGT_tmpJnt" -p "upperLegRGT_tmpJnt";
	rename -uid "35D59490-44AD-5BBE-7D20-5198CEE4A6AD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.1395037660611429 -12.786619406291535 -0.75525431989366398 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 9.5924072265625 67.79876708984375 1.4713684320449825 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.5;
createNode joint -n "ankleRGT_tmpJnt" -p "lowerLegRGT_tmpJnt";
	rename -uid "5E4B1C13-439A-6C3B-8F55-089145012A0F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0.20052281789986903 -26.549140451927343 3.1662029242357113 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 -2.7642796773228715e-16 -2.2572056524766739 0 0
		 0 0 2.2572056524766739 0 10.026567459106442 25.278465270996087 -5.7832069396972638 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
	setAttr ".radi" 0.5;
createNode joint -n "heelRollRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "4F718A5A-4D0B-EC61-63D8-B48E3A55334D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -0.033358440407621259 -3.0947461231723539 2.6025387682764722 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -180 1.4033418597069752e-14 -1.4033418597069752e-14 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 2.7642796773228715e-16 2.2572056524766739 2.7642796773228715e-16 0
		 3.3852662587815329e-32 2.7642796773228715e-16 -2.2572056524766739 0 9.951313972473141 0.44198825955391641 -11.657663345336907 1;
	setAttr ".radi" 0.5;
createNode joint -n "footInRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "3E6A050F-41F8-5AE7-C1E3-8EB1FC92D7D2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 2.1453256535223728 -3.2916291271599483 -3.5567478954364202 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -90.000000000004192 89.999999999999929 0 ;
	setAttr ".bps" -type "matrix" -2.0048013493549223e-15 2.4551735554138001e-31 -2.2572056524766739 0
		 2.2572056524766739 1.651196833540488e-13 -2.0048013493549223e-15 0 1.649943832697141e-13 -2.2572056524766739 0 0
		 14.869093924780286 -0.0024171567950581618 2.2451089524518615 1;
	setAttr ".radi" 0.5;
createNode joint -n "footOutRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "1A9C9C51-4B35-7EFE-F611-BAB2E8E3773F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.1907842268498019 -3.2916291271599483 -3.5567478954364198 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -180 -89.999999999999972 0 ;
	setAttr ".bps" -type "matrix" -1.7542011806855572e-15 2.1482768609870751e-31 2.2572056524766739 0
		 0 2.2572056524766739 -2.2257766178534174e-31 0 -2.2572056524766739 0 -1.5036010120161916e-15 0
		 5.0815629059024978 -0.0024171567953992223 2.245109043491059 1;
	setAttr ".radi" 0.5;
createNode joint -n "ballRGT_tmpJnt" -p "ankleRGT_tmpJnt";
	rename -uid "477CADCF-4379-34F7-42E7-29B4EFC0583A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -0.033358440407622147 -3.2775299955693411 -4.1384625609215773 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" 90.863171496667746 1.0650026288506287e-16 -1.4138326379220642e-14 ;
	setAttr ".bps" -type "matrix" -2.2572056524766739 2.7642796773228715e-16 0 0 4.1642808448503742e-18 0.034003933605589051 2.2569495098632566 0
		 2.7639659930912251e-16 2.2569495098632566 -0.034003933605589051 0 9.9513139724731374 0.029407463967817904 3.9547955989837629 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 0.5;
createNode joint -n "toesTipRGT_tmpJnt" -p "ballRGT_tmpJnt";
	rename -uid "D4E9849F-4F66-2525-959B-11AF6D91C1AB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 8.8817841970012523e-16 -7.1965499230458594 0.0026469597944873552 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -1.9994200605091101 0.3165738711672948 8.9934785386618579 ;
	setAttr ".bps" -type "matrix" -2.2294218507236918 -0.0071546779436613564 0.3529934555652815 0
		 0.35306595571988514 -0.045177947870845614 2.2289640511929374 0 -2.7572613058041876e-15 2.2567421476948466 0.045740970587629187 0
		 9.951313972473141 0.26814451813698909 19.800535202026367 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
	setAttr ".radi" 0.5;
createNode joint -n "legRGT_pov_tmpJnt" -p "lowerLegRGT_tmpJnt";
	rename -uid "891A2110-4921-4690-368C-6CA7A03E21F8";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.1470979192936852e-06 0.57520128489143829 -19.287922729286663 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 0 180 0 ;
	setAttr ".radi" 3;
createNode transform -s -n "persp";
	rename -uid "6EADA48C-4486-5A24-A4EA-40AE5779550B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 47.168892806322461 85.313657493552725 83.210507665451743 ;
	setAttr ".r" -type "double3" -24.338352729978233 -345.00000000005366 4.1159406277626634e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "989130E3-4311-5C1F-40BF-6696D7556F9A";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 96.747430057954489;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 27.786862444432764 52.520332673906474 1.3605343076679473 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "ADC2D1FF-4866-AB7E-8AA9-A8B7462C24AC";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 29.472629722681987 1002.2036233577213 -1.6538365543381304 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "4D635DCF-40C5-7F80-762E-808D78CAB2C7";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 950.7051572441427;
	setAttr ".ow" 21.656087459066221;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 29.472629722681987 51.498466113578623 -1.6538365543383413 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "AEE51B2D-493F-F52C-BC5E-55A2E63FC9F0";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 30.841596107972457 50.592710445301876 1011.0444768608269 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "FDB8E629-46CB-A6AC-9263-B29DBE43383C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1013.8098794171258;
	setAttr ".ow" 13.005891681812605;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 33.842296232319462 49.898262702238711 -2.7654025562989277 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "D135581F-4D32-C0D9-39FE-66BE803D8BE1";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.7203622940284 48.093974865279925 3.196475929786784 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "1895C1FF-4D76-71EE-B37A-AF8B2BF20722";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 969.18610209700137;
	setAttr ".ow" 15.741056171649358;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 31.534260197027017 48.093974865279925 3.1964759297865677 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode displayLayerManager -n "layerManager";
	rename -uid "9A055C1C-4F22-E5D4-ACFC-339CFFA68148";
	setAttr ".cdl" 3;
	setAttr -s 3 ".dli[1:2]"  3 2;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D1E9F591-4BA5-3116-9CBF-C79E486EF062";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "8C19CBF3-4B41-09FC-9B5A-8E87C216CEA7";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "1F8803AB-4FF6-08A1-072D-EB80121BD975";
createNode displayLayer -n "defaultLayer";
	rename -uid "C898949A-4127-0B4F-67D0-D8A93EF503D2";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "F8AC642C-4574-829F-F371-CAA96B701507";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "B908E3D0-446B-1159-C91B-18B719A41711";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "0C832185-4B38-D747-EF0B-4F92E03B516B";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 120 -ast 0 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "1DD6CBFE-43D8-C928-1D7A-2589AD823477";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -622.61902287839052 -351.19046223542102 ;
	setAttr ".tgi[0].vh" -type "double2" 690.47616303913287 413.09522168030884 ;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av -k on ".unw";
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
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
	setAttr -k on ".ro" yes;
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
	setAttr -k on ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
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
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -k off -cb on ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off -cb on ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -cb on ".hwcc";
	setAttr -cb on ".hwdp";
	setAttr -cb on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "root.s" "cog_tmpJnt.is";
connectAttr "cog_tmpJnt.s" "spine01_tmpJnt.is";
connectAttr "spine01_tmpJnt.s" "spine02_tmpJnt.is";
connectAttr "spine02_tmpJnt.s" "spine03_tmpJnt.is";
connectAttr "spine03_tmpJnt.s" "spine04_tmpJnt.is";
connectAttr "spine04_tmpJnt.s" "clavLFT_tmpJnt.is";
connectAttr "clavLFT_tmpJnt.s" "upperArmLFT_tmpJnt.is";
connectAttr "upperArmLFT_tmpJnt.s" "lowerArmLFT_tmpJnt.is";
connectAttr "lowerArmLFT_tmpJnt.s" "handLFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "handLFT_prop_jnt.is";
connectAttr "handLFT_tmpJnt.s" "thumb01LFT_tmpJnt.is";
connectAttr "thumb01LFT_tmpJnt.s" "thumb02LFT_tmpJnt.is";
connectAttr "thumb02LFT_tmpJnt.s" "thumb03LFT_tmpJnt.is";
connectAttr "thumb03LFT_tmpJnt.s" "thumb04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "pinkyBaseLFT_tmpJnt.is";
connectAttr "pinkyBaseLFT_tmpJnt.s" "pinky01LFT_tmpJnt.is";
connectAttr "pinky01LFT_tmpJnt.s" "pinky02LFT_tmpJnt.is";
connectAttr "pinky02LFT_tmpJnt.s" "pinky03LFT_tmpJnt.is";
connectAttr "pinky03LFT_tmpJnt.s" "pinky04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "ringBaseLFT_tmpJnt.is";
connectAttr "ringBaseLFT_tmpJnt.s" "ring01LFT_tmpJnt.is";
connectAttr "ring01LFT_tmpJnt.s" "ring02LFT_tmpJnt.is";
connectAttr "ring02LFT_tmpJnt.s" "ring03LFT_tmpJnt.is";
connectAttr "ring03LFT_tmpJnt.s" "ring04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "middleBaseLFT_tmpJnt.is";
connectAttr "middleBaseLFT_tmpJnt.s" "middle01LFT_tmpJnt.is";
connectAttr "middle01LFT_tmpJnt.s" "middle02LFT_tmpJnt.is";
connectAttr "middle02LFT_tmpJnt.s" "middle03LFT_tmpJnt.is";
connectAttr "middle03LFT_tmpJnt.s" "middle04LFT_tmpJnt.is";
connectAttr "handLFT_tmpJnt.s" "indexBaseLFT_tmpJnt.is";
connectAttr "indexBaseLFT_tmpJnt.s" "index01LFT_tmpJnt.is";
connectAttr "index01LFT_tmpJnt.s" "index02LFT_tmpJnt.is";
connectAttr "index02LFT_tmpJnt.s" "index03LFT_tmpJnt.is";
connectAttr "index03LFT_tmpJnt.s" "index04LFT_tmpJnt.is";
connectAttr "lowerArmLFT_tmpJnt.s" "armLFT_pov_tmpJnt.is";
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
connectAttr "spine04_tmpJnt.s" "clavRGT_tmpJnt.is";
connectAttr "clavRGT_tmpJnt.s" "upperArmRGT_tmpJnt.is";
connectAttr "upperArmRGT_tmpJnt.s" "lowerArmRGT_tmpJnt.is";
connectAttr "lowerArmRGT_tmpJnt.s" "handRGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "handRGT_prop_jnt.is";
connectAttr "handRGT_tmpJnt.s" "thumb01RGT_tmpJnt.is";
connectAttr "thumb01RGT_tmpJnt.s" "thumb02RGT_tmpJnt.is";
connectAttr "thumb02RGT_tmpJnt.s" "thumb03RGT_tmpJnt.is";
connectAttr "thumb03RGT_tmpJnt.s" "thumb04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "pinkyBaseRGT_tmpJnt.is";
connectAttr "pinkyBaseRGT_tmpJnt.s" "pinky01RGT_tmpJnt.is";
connectAttr "pinky01RGT_tmpJnt.s" "pinky02RGT_tmpJnt.is";
connectAttr "pinky02RGT_tmpJnt.s" "pinky03RGT_tmpJnt.is";
connectAttr "pinky03RGT_tmpJnt.s" "pinky04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "ringBaseRGT_tmpJnt.is";
connectAttr "ringBaseRGT_tmpJnt.s" "ring01RGT_tmpJnt.is";
connectAttr "ring01RGT_tmpJnt.s" "ring02RGT_tmpJnt.is";
connectAttr "ring02RGT_tmpJnt.s" "ring03RGT_tmpJnt.is";
connectAttr "ring03RGT_tmpJnt.s" "ring04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "middleBaseRGT_tmpJnt.is";
connectAttr "middleBaseRGT_tmpJnt.s" "middle01RGT_tmpJnt.is";
connectAttr "middle01RGT_tmpJnt.s" "middle02RGT_tmpJnt.is";
connectAttr "middle02RGT_tmpJnt.s" "middle03RGT_tmpJnt.is";
connectAttr "middle03RGT_tmpJnt.s" "middle04RGT_tmpJnt.is";
connectAttr "handRGT_tmpJnt.s" "indexBaseRGT_tmpJnt.is";
connectAttr "indexBaseRGT_tmpJnt.s" "index01RGT_tmpJnt.is";
connectAttr "index01RGT_tmpJnt.s" "index02RGT_tmpJnt.is";
connectAttr "index02RGT_tmpJnt.s" "index03RGT_tmpJnt.is";
connectAttr "index03RGT_tmpJnt.s" "index04RGT_tmpJnt.is";
connectAttr "lowerArmRGT_tmpJnt.s" "armRGT_pov_tmpJnt.is";
connectAttr "cog_tmpJnt.s" "hip_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "upperLegLFT_tmpJnt.is";
connectAttr "upperLegLFT_tmpJnt.s" "lowerLegLFT_tmpJnt.is";
connectAttr "lowerLegLFT_tmpJnt.s" "ankleLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "heelRollLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footInLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "footOutLFT_tmpJnt.is";
connectAttr "ankleLFT_tmpJnt.s" "ballLFT_tmpJnt.is";
connectAttr "ballLFT_tmpJnt.s" "toesTipLFT_tmpJnt.is";
connectAttr "lowerLegLFT_tmpJnt.s" "legLFT_pov_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "upperLegRGT_tmpJnt.is";
connectAttr "upperLegRGT_tmpJnt.s" "lowerLegRGT_tmpJnt.is";
connectAttr "lowerLegRGT_tmpJnt.s" "ankleRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "heelRollRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footInRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "footOutRGT_tmpJnt.is";
connectAttr "ankleRGT_tmpJnt.s" "ballRGT_tmpJnt.is";
connectAttr "ballRGT_tmpJnt.s" "toesTipRGT_tmpJnt.is";
connectAttr "lowerLegRGT_tmpJnt.s" "legRGT_pov_tmpJnt.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of templateJoint_biped_hi.ma
