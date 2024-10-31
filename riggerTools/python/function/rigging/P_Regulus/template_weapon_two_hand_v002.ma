//Maya ASCII 2023 scene
//Name: template_weapon_two_hand_v002.ma
//Last modified: Thu, Oct 31, 2024 12:28:49 AM
//Codeset: 1252
requires maya "2023";
requires -nodeType "ikSpringSolver" "ikSpringSolver" "1.0";
requires "stereoCamera" "10.0";
requires "mtoa" "5.1.2";
requires -nodeType "quatToEuler" -nodeType "quatProd" "quatNodes" "1.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202205052215-234554116d";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 19045)";
fileInfo "UUID" "0938DB98-4F51-F9E4-3047-20851CF57960";
createNode transform -n "extract_dual_weapon";
	rename -uid "3C2F32B5-4F62-BB72-382E-5DBAFD6ACD4C";
createNode transform -n "handPropRGTCtrlZro_grp_tmp" -p "extract_dual_weapon";
	rename -uid "AC7831FB-4ED0-B81C-4017-CF89EB3AD864";
	setAttr ".t" -type "double3" -43.5603 74.6511 3.11287 ;
	setAttr ".r" -type "double3" 90 1.9200767349048417e-13 -179.99999999999997 ;
createNode transform -n "handPropRGT_ctrl_tmp" -p "handPropRGTCtrlZro_grp_tmp";
	rename -uid "718EDF87-4B0E-C737-27BB-5AA21932456B";
	setAttr ".ro" 3;
createNode nurbsCurve -n "handPropRGT_ctrl_tmpShape" -p "handPropRGT_ctrl_tmp";
	rename -uid "5109DAB9-4F13-FE9A-34E8-698775682427";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 33 0 no 3
		34 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33
		34
		-1.5888046367689095 -6.1071618768786688 -1.5888046367689102
		1.2084235697908976e-15 -6.1071618768786502 -2.2469083699764076
		1.2084235697908976e-15 6.0327790453805097 -2.2469083699764076
		-1.5888046367689095 6.0327790453805097 -1.5888046367689102
		-1.5888046367689095 -6.1071618768786688 -1.5888046367689102
		-2.2469083699764107 -6.1071618768786626 4.6332462092912053e-16
		-2.2469083699764107 6.0327790453805097 -1.9335153995653373e-16
		-1.5888046367689095 6.0327790453805097 -1.5888046367689102
		-2.2469083699764107 6.0327790453805097 -1.9335153995653373e-16
		-1.5888046367689095 6.0327790453805079 1.5888046367689121
		-1.5888046367689095 -6.1071618768786626 1.5888046367689121
		-2.2469083699764107 -6.1071618768786626 4.6332462092912053e-16
		-1.5888046367689095 -6.1071618768786626 1.5888046367689121
		1.2084235697908976e-15 -6.1071618768786626 2.2469083699764147
		1.2084235697908976e-15 6.0327790453805079 2.2469083699764139
		-1.5888046367689095 6.0327790453805079 1.5888046367689121
		-1.5888046367689095 -6.1071618768786626 1.5888046367689121
		-1.5888046367689095 6.0327790453805079 1.5888046367689121
		1.2084235697908976e-15 6.0327790453805079 2.2469083699764139
		1.5888046367689124 6.0327790453805079 1.5888046367689121
		1.5888046367689124 -6.1071618768786626 1.5888046367689121
		1.2084235697908976e-15 -6.1071618768786626 2.2469083699764147
		1.5888046367689124 -6.1071618768786626 1.5888046367689121
		2.2469083699764116 -6.1071618768786626 4.6332462092912053e-16
		2.2469083699764116 6.0327790453805097 -1.9335153995653373e-16
		1.5888046367689124 6.0327790453805079 1.5888046367689121
		2.2469083699764116 6.0327790453805097 -1.9335153995653373e-16
		1.5888046367689124 6.0327790453805097 -1.5888046367689102
		1.5888046367689124 -6.1071618768786688 -1.5888046367689102
		2.2469083699764116 -6.1071618768786626 4.6332462092912053e-16
		1.5888046367689124 -6.1071618768786688 -1.5888046367689102
		1.2084235697908976e-15 -6.1071618768786502 -2.2469083699764076
		1.2084235697908976e-15 6.0327790453805097 -2.2469083699764076
		1.5888046367689124 6.0327790453805097 -1.5888046367689102
		;
	setAttr -k on ".gimbal";
createNode transform -n "handPropRGT_gmbCtrl_tmp" -p "handPropRGT_ctrl_tmp";
	rename -uid "D300C154-46D6-80F2-6D6D-8FA100055A72";
	setAttr -l on -k off ".v";
	setAttr ".ro" 3;
createNode nurbsCurve -n "handPropRGT_gmbCtrl_tmpShape" -p "handPropRGT_gmbCtrl_tmp";
	rename -uid "5F640D5C-43EC-7C12-FA32-B98C49784F77";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 33 0 no 3
		34 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33
		34
		-0.82179550177702232 -3.1588768328682777 -0.82179550177702243
		6.2504667402977472e-16 -3.1588768328682679 -1.1621939844705558
		6.2504667402977472e-16 3.1204029545071608 -1.1621939844705558
		-0.82179550177702232 3.1204029545071608 -0.82179550177702243
		-0.82179550177702232 -3.1588768328682777 -0.82179550177702243
		-1.1621939844705573 -3.1588768328682741 2.3965066599782103e-16
		-1.1621939844705573 3.1204029545071608 -1.0000941721889678e-16
		-0.82179550177702232 3.1204029545071608 -0.82179550177702243
		-1.1621939844705573 3.1204029545071608 -1.0000941721889678e-16
		-0.82179550177702232 3.1204029545071599 0.82179550177702365
		-0.82179550177702232 -3.1588768328682741 0.82179550177702365
		-1.1621939844705573 -3.1588768328682741 2.3965066599782103e-16
		-0.82179550177702232 -3.1588768328682741 0.82179550177702365
		6.2504667402977472e-16 -3.1588768328682741 1.1621939844705595
		6.2504667402977472e-16 3.1204029545071599 1.1621939844705591
		-0.82179550177702232 3.1204029545071599 0.82179550177702365
		-0.82179550177702232 -3.1588768328682741 0.82179550177702365
		-0.82179550177702232 3.1204029545071599 0.82179550177702365
		6.2504667402977472e-16 3.1204029545071599 1.1621939844705591
		0.82179550177702376 3.1204029545071599 0.82179550177702365
		0.82179550177702376 -3.1588768328682741 0.82179550177702365
		6.2504667402977472e-16 -3.1588768328682741 1.1621939844705595
		0.82179550177702376 -3.1588768328682741 0.82179550177702365
		1.162193984470558 -3.1588768328682741 2.3965066599782103e-16
		1.162193984470558 3.1204029545071608 -1.0000941721889678e-16
		0.82179550177702376 3.1204029545071599 0.82179550177702365
		1.162193984470558 3.1204029545071608 -1.0000941721889678e-16
		0.82179550177702376 3.1204029545071608 -0.82179550177702243
		0.82179550177702376 -3.1588768328682777 -0.82179550177702243
		1.162193984470558 -3.1588768328682741 2.3965066599782103e-16
		0.82179550177702376 -3.1588768328682777 -0.82179550177702243
		6.2504667402977472e-16 -3.1588768328682679 -1.1621939844705558
		6.2504667402977472e-16 3.1204029545071608 -1.1621939844705558
		0.82179550177702376 3.1204029545071608 -0.82179550177702243
		;
createNode transform -n "handPropLFTCtrlZro_grp_tmp" -p "extract_dual_weapon";
	rename -uid "249C97A9-47AC-C38F-F52C-809122D6996F";
	setAttr ".t" -type "double3" 43.56034532298235 74.651134999806544 3.1128735542297443 ;
	setAttr ".r" -type "double3" 90 4.4979835663949474e-15 -179.99999999999991 ;
createNode transform -n "handPropLFT_ctrl_tmp" -p "handPropLFTCtrlZro_grp_tmp";
	rename -uid "183D7012-419D-15D8-8636-C89276DDA267";
	setAttr ".ro" 3;
createNode nurbsCurve -n "handPropLFT_ctrl_tmpShape" -p "handPropLFT_ctrl_tmp";
	rename -uid "866D477A-4538-312C-0EEE-4CA4FC925F20";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 33 0 no 3
		34 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33
		34
		-1.5888046367689095 -6.1071618768786688 -1.5888046367689102
		1.2084235697908976e-15 -6.1071618768786502 -2.2469083699764076
		1.2084235697908976e-15 6.0327790453805097 -2.2469083699764076
		-1.5888046367689095 6.0327790453805097 -1.5888046367689102
		-1.5888046367689095 -6.1071618768786688 -1.5888046367689102
		-2.2469083699764107 -6.1071618768786626 4.6332462092912053e-16
		-2.2469083699764107 6.0327790453805097 -1.9335153995653373e-16
		-1.5888046367689095 6.0327790453805097 -1.5888046367689102
		-2.2469083699764107 6.0327790453805097 -1.9335153995653373e-16
		-1.5888046367689095 6.0327790453805079 1.5888046367689121
		-1.5888046367689095 -6.1071618768786626 1.5888046367689121
		-2.2469083699764107 -6.1071618768786626 4.6332462092912053e-16
		-1.5888046367689095 -6.1071618768786626 1.5888046367689121
		1.2084235697908976e-15 -6.1071618768786626 2.2469083699764147
		1.2084235697908976e-15 6.0327790453805079 2.2469083699764139
		-1.5888046367689095 6.0327790453805079 1.5888046367689121
		-1.5888046367689095 -6.1071618768786626 1.5888046367689121
		-1.5888046367689095 6.0327790453805079 1.5888046367689121
		1.2084235697908976e-15 6.0327790453805079 2.2469083699764139
		1.5888046367689124 6.0327790453805079 1.5888046367689121
		1.5888046367689124 -6.1071618768786626 1.5888046367689121
		1.2084235697908976e-15 -6.1071618768786626 2.2469083699764147
		1.5888046367689124 -6.1071618768786626 1.5888046367689121
		2.2469083699764116 -6.1071618768786626 4.6332462092912053e-16
		2.2469083699764116 6.0327790453805097 -1.9335153995653373e-16
		1.5888046367689124 6.0327790453805079 1.5888046367689121
		2.2469083699764116 6.0327790453805097 -1.9335153995653373e-16
		1.5888046367689124 6.0327790453805097 -1.5888046367689102
		1.5888046367689124 -6.1071618768786688 -1.5888046367689102
		2.2469083699764116 -6.1071618768786626 4.6332462092912053e-16
		1.5888046367689124 -6.1071618768786688 -1.5888046367689102
		1.2084235697908976e-15 -6.1071618768786502 -2.2469083699764076
		1.2084235697908976e-15 6.0327790453805097 -2.2469083699764076
		1.5888046367689124 6.0327790453805097 -1.5888046367689102
		;
	setAttr -k on ".gimbal";
createNode transform -n "handPropLFT_gmbCtrl_tmp" -p "handPropLFT_ctrl_tmp";
	rename -uid "0F27D911-4E24-F6E0-F4E4-F688E07F338F";
	setAttr -l on -k off ".v";
	setAttr ".ro" 3;
createNode nurbsCurve -n "handPropLFT_gmbCtrl_tmpShape" -p "handPropLFT_gmbCtrl_tmp";
	rename -uid "8C3C7300-4FB2-77B7-29D4-7DAEAE3F6E45";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 33 0 no 3
		34 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33
		34
		-0.82179550177702232 -3.1588768328682777 -0.82179550177702243
		6.2504667402977472e-16 -3.1588768328682679 -1.1621939844705558
		6.2504667402977472e-16 3.1204029545071608 -1.1621939844705558
		-0.82179550177702232 3.1204029545071608 -0.82179550177702243
		-0.82179550177702232 -3.1588768328682777 -0.82179550177702243
		-1.1621939844705573 -3.1588768328682741 2.3965066599782103e-16
		-1.1621939844705573 3.1204029545071608 -1.0000941721889678e-16
		-0.82179550177702232 3.1204029545071608 -0.82179550177702243
		-1.1621939844705573 3.1204029545071608 -1.0000941721889678e-16
		-0.82179550177702232 3.1204029545071599 0.82179550177702365
		-0.82179550177702232 -3.1588768328682741 0.82179550177702365
		-1.1621939844705573 -3.1588768328682741 2.3965066599782103e-16
		-0.82179550177702232 -3.1588768328682741 0.82179550177702365
		6.2504667402977472e-16 -3.1588768328682741 1.1621939844705595
		6.2504667402977472e-16 3.1204029545071599 1.1621939844705591
		-0.82179550177702232 3.1204029545071599 0.82179550177702365
		-0.82179550177702232 -3.1588768328682741 0.82179550177702365
		-0.82179550177702232 3.1204029545071599 0.82179550177702365
		6.2504667402977472e-16 3.1204029545071599 1.1621939844705591
		0.82179550177702376 3.1204029545071599 0.82179550177702365
		0.82179550177702376 -3.1588768328682741 0.82179550177702365
		6.2504667402977472e-16 -3.1588768328682741 1.1621939844705595
		0.82179550177702376 -3.1588768328682741 0.82179550177702365
		1.162193984470558 -3.1588768328682741 2.3965066599782103e-16
		1.162193984470558 3.1204029545071608 -1.0000941721889678e-16
		0.82179550177702376 3.1204029545071599 0.82179550177702365
		1.162193984470558 3.1204029545071608 -1.0000941721889678e-16
		0.82179550177702376 3.1204029545071608 -0.82179550177702243
		0.82179550177702376 -3.1588768328682777 -0.82179550177702243
		1.162193984470558 -3.1588768328682741 2.3965066599782103e-16
		0.82179550177702376 -3.1588768328682777 -0.82179550177702243
		6.2504667402977472e-16 -3.1588768328682679 -1.1621939844705558
		6.2504667402977472e-16 3.1204029545071608 -1.1621939844705558
		0.82179550177702376 3.1204029545071608 -0.82179550177702243
		;
createNode transform -n "weaponCtrl_grp" -p "extract_dual_weapon";
	rename -uid "89E34EB8-4AE6-BBD0-C0EF-CA9E0CE721D8";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "R_weapon_ctrl" -p "weaponCtrl_grp";
	rename -uid "6064204C-4965-7798-58E6-2F9495A02B5F";
	setAttr ".ove" yes;
createNode nurbsCurve -n "R_weapon_ctrlShape" -p "R_weapon_ctrl";
	rename -uid "E1049153-4FD7-A88A-DB35-01AD08A9FD7F";
	addAttr -ci true -sn "SpaceSwitch" -ln "SpaceSwitch" -min 0 -max 2 -en "World:Hand R:Hand L" 
		-at "enum";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".ls" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 48 0 no 3
		49 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
		49
		-16.171231192952987 -1.9689928136107794e-16 3.215609292379928
		-20.622998696141281 0 4.1245997392282545
		-20.622998696141281 0 8.249199478456509
		-28.872198174597774 0 0
		-20.622998696141281 0 -8.249199478456509
		-20.622998696141281 0 -4.1245997392282545
		-16.171185566747525 1.9691196157396922e-16 -3.2158163759716962
		-15.226019332339503 3.8619069399090032e-16 -6.3069726595420219
		-13.708582329517954 5.6095474820669632e-16 -9.1610862592750042
		-11.66518907892968 7.1429937528577857e-16 -11.665394067629977
		-9.1607058263917587 8.3940829516095837e-16 -13.708577783331295
		-6.3065868242159588 9.3232498677348713e-16 -15.226022513962517
		-3.2156431508157413 9.9024281193411554e-16 -16.171892379477281
		-4.1245997392282545 0 -20.622998696141281
		-8.249199478456509 0 -20.622998696141281
		0 0 -28.872198174597774
		8.249199478456509 0 -20.622998696141281
		4.1245997392282545 0 -20.622998696141281
		3.2156431508157368 9.9024281193411554e-16 -16.171892379477281
		6.3065868242159624 9.3232498677348713e-16 -15.226022513962514
		9.160705826391764 8.3940829516095837e-16 -13.708577783331304
		11.665189078929687 7.1429937528577986e-16 -11.665394067630004
		13.708582329517959 5.6095474820669651e-16 -9.1610862592750149
		15.22601933233949 3.8619069399090313e-16 -6.3069726595420592
		16.171185566747514 1.9691196157397085e-16 -3.2158163759717238
		20.622998696141281 0 -4.1245997392282545
		20.622998696141281 0 -8.249199478456509
		28.872198174597774 0 0
		20.622998696141281 0 8.249199478456509
		20.622998696141281 0 4.1245997392282545
		16.171231192953027 -1.9689928136107621e-16 3.2156092923798876
		15.226133376794246 -3.8617922674658541e-16 6.306785385230401
		13.708665426342954 -5.6094226347776685e-16 9.1608823681786049
		11.665264034636511 -7.1428673080394887e-16 11.665187567570742
		9.160964092984095 -8.3940939650891132e-16 13.708595769708293
		6.3068821410327436 -9.3232925178870665e-16 15.226092166946907
		3.2157145911224316 -9.9020147921772424e-16 16.171217364992771
		4.1245997392282545 0 20.622998696141281
		8.249199478456509 0 20.622998696141281
		0 0 28.872198174597774
		-8.249199478456509 0 20.622998696141281
		-4.1245997392282545 0 20.622998696141281
		-3.2157145911224032 -9.9020147921772503e-16 16.171217364992778
		-6.3068821410327018 -9.3232925178870665e-16 15.226092166946922
		-9.1609640929840701 -8.3940939650891152e-16 13.708595769708314
		-11.665264034636499 -7.1428673080394956e-16 11.665187567570756
		-13.708665426342931 -5.6094226347776941e-16 9.1608823681786369
		-15.226133376794245 -3.8617922674658832e-16 6.3067853852304347
		-16.171231192952987 -1.9689928136107794e-16 3.215609292379928
		;
	setAttr -k on ".SpaceSwitch" 1;
createNode transform -n "L_weapon_ctrl" -p "weaponCtrl_grp";
	rename -uid "BF00E19A-495F-3463-4EB6-A3A1703EFEED";
	setAttr ".ove" yes;
createNode nurbsCurve -n "L_weapon_ctrlShape" -p "L_weapon_ctrl";
	rename -uid "6F85A3DB-4CC6-E57E-E050-B8905B5D3F50";
	addAttr -ci true -sn "SpaceSwitch" -ln "SpaceSwitch" -min 0 -max 2 -en "World:Hand L:Hand R" 
		-at "enum";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".ls" 4;
	setAttr ".cc" -type "nurbsCurve" 
		1 48 0 no 3
		49 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48
		49
		-16.171231192952987 -1.9689928136107794e-16 3.215609292379928
		-20.622998696141281 0 4.1245997392282545
		-20.622998696141281 0 8.249199478456509
		-28.872198174597774 0 0
		-20.622998696141281 0 -8.249199478456509
		-20.622998696141281 0 -4.1245997392282545
		-16.171185566747525 1.9691196157396922e-16 -3.2158163759716962
		-15.226019332339503 3.8619069399090032e-16 -6.3069726595420219
		-13.708582329517954 5.6095474820669632e-16 -9.1610862592750042
		-11.66518907892968 7.1429937528577857e-16 -11.665394067629977
		-9.1607058263917587 8.3940829516095837e-16 -13.708577783331295
		-6.3065868242159588 9.3232498677348713e-16 -15.226022513962517
		-3.2156431508157413 9.9024281193411554e-16 -16.171892379477281
		-4.1245997392282545 0 -20.622998696141281
		-8.249199478456509 0 -20.622998696141281
		0 0 -28.872198174597774
		8.249199478456509 0 -20.622998696141281
		4.1245997392282545 0 -20.622998696141281
		3.2156431508157368 9.9024281193411554e-16 -16.171892379477281
		6.3065868242159624 9.3232498677348713e-16 -15.226022513962514
		9.160705826391764 8.3940829516095837e-16 -13.708577783331304
		11.665189078929687 7.1429937528577986e-16 -11.665394067630004
		13.708582329517959 5.6095474820669651e-16 -9.1610862592750149
		15.22601933233949 3.8619069399090313e-16 -6.3069726595420592
		16.171185566747514 1.9691196157397085e-16 -3.2158163759717238
		20.622998696141281 0 -4.1245997392282545
		20.622998696141281 0 -8.249199478456509
		28.872198174597774 0 0
		20.622998696141281 0 8.249199478456509
		20.622998696141281 0 4.1245997392282545
		16.171231192953027 -1.9689928136107621e-16 3.2156092923798876
		15.226133376794246 -3.8617922674658541e-16 6.306785385230401
		13.708665426342954 -5.6094226347776685e-16 9.1608823681786049
		11.665264034636511 -7.1428673080394887e-16 11.665187567570742
		9.160964092984095 -8.3940939650891132e-16 13.708595769708293
		6.3068821410327436 -9.3232925178870665e-16 15.226092166946907
		3.2157145911224316 -9.9020147921772424e-16 16.171217364992771
		4.1245997392282545 0 20.622998696141281
		8.249199478456509 0 20.622998696141281
		0 0 28.872198174597774
		-8.249199478456509 0 20.622998696141281
		-4.1245997392282545 0 20.622998696141281
		-3.2157145911224032 -9.9020147921772503e-16 16.171217364992778
		-6.3068821410327018 -9.3232925178870665e-16 15.226092166946922
		-9.1609640929840701 -8.3940939650891152e-16 13.708595769708314
		-11.665264034636499 -7.1428673080394956e-16 11.665187567570756
		-13.708665426342931 -5.6094226347776941e-16 9.1608823681786369
		-15.226133376794245 -3.8617922674658832e-16 6.3067853852304347
		-16.171231192952987 -1.9689928136107794e-16 3.215609292379928
		;
	setAttr -k on ".SpaceSwitch" 1;
createNode transform -n "L_origin_loc" -p "weaponCtrl_grp";
	rename -uid "0BE1052A-4A1F-5397-A51D-32A7B494A0E7";
	setAttr ".v" no;
createNode locator -n "L_origin_locShape" -p "L_origin_loc";
	rename -uid "942F42D0-41C8-8656-ABDC-3AB9CE7BD051";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 20 20 20 ;
createNode transform -n "R_origin_loc" -p "weaponCtrl_grp";
	rename -uid "AE9AE26B-4F98-55F9-F666-7B8BD7902F0A";
	setAttr ".v" no;
createNode locator -n "R_origin_locShape" -p "R_origin_loc";
	rename -uid "366EA086-4AFD-F561-72B6-C8BC75276054";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 20 20 20 ;
createNode joint -n "root_tmp" -p "extract_dual_weapon";
	rename -uid "7812C655-4898-2852-E292-888DDCC0A1D6";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "L_Weapon_bJnt" -p "root_tmp";
	rename -uid "CF7B12F1-4579-21A5-3507-06A4B86ECF31";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode joint -n "R_Weapon_bJnt" -p "root_tmp";
	rename -uid "00EE45C2-459D-5A13-9008-F68BEFBB2CBE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode transform -s -n "persp";
	rename -uid "A022C707-4128-5896-0705-51837E0784F8";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 133.05780466336304 96.279514581840672 -189.08914434424992 ;
	setAttr ".r" -type "double3" -16.538352729589612 -929.79999999993447 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "1AC78935-44A0-0DBB-754B-F993296B56F4";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 243.95748696378666;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -1.1920928955078125e-07 0 -1.7881393432617188e-07 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "B0BA49D7-4D28-D471-9F91-189BFA94898E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "1631CA11-4558-3280-9AD8-4A85F770AE93";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "68C42BF5-4958-F786-A9FD-60987AFE2B67";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -22.67884624113529 -8.8747150354588626 1003.8394179904773 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "44604B3C-4F13-F5CB-B48D-3EB83A49729C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.7265479904772;
	setAttr ".ow" 130.40429767568389;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" -43.5603 74.6511 3.1128700000000005 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "80C4C0D9-4814-274D-529C-0298E2F9A558";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "8836FB92-48D6-D537-BE0D-738D71C66C7F";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode blendMatrix -n "R_weapon_blendMatrix";
	rename -uid "FB9D0228-4DD1-CE33-A777-F7B71B049BFC";
	setAttr -s 2 ".tgt";
createNode blendMatrix -n "L_weapon_blendMatrix";
	rename -uid "AD6DC1F3-4EFA-6B4B-3124-2FA2319B5165";
	setAttr -s 2 ".tgt";
createNode condition -n "L_Weapon_cnd";
	rename -uid "77B7A3FB-41DC-4188-9F1A-7895EB770E25";
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 1 1 ;
createNode quatToEuler -n "L_Weapon_bJnt6_quatToEuler";
	rename -uid "3603F023-4F6D-B422-0E10-C1BAFAE9B09B";
createNode quatProd -n "L_Weapon_bJnt5_quatProd";
	rename -uid "DD7F6F3A-4EDB-D911-D8BF-56A87BAD516F";
	setAttr ".i2w" 1;
createNode decomposeMatrix -n "L_Weapon_bJnt1_deComp";
	rename -uid "CB619B70-4F63-9B6D-73A3-099746CA689E";
createNode multMatrix -n "L_Weapon_bJnt2_multMatrix";
	rename -uid "73DD36B9-494B-B490-A8F3-F8846464F9F8";
createNode quatToEuler -n "R_Weapon_bJnt6_quatToEuler";
	rename -uid "FEEE35EE-4430-A1F9-4357-919059961746";
createNode quatProd -n "R_Weapon_bJnt5_quatProd";
	rename -uid "E2AE1E36-4057-E034-3DCC-BDBEF57291D3";
	setAttr ".i2w" 1;
createNode decomposeMatrix -n "R_Weapon_bJnt1_deComp";
	rename -uid "33D8F21B-48A2-D517-5751-598A579A6AE2";
createNode multMatrix -n "R_Weapon_bJnt2_multMatrix";
	rename -uid "90896AFD-4956-3925-34CF-279CA50A7653";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "9B33960A-4D06-350D-BFE3-FDBB07B3B031";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "276E4D3C-4159-D96D-CBBC-8B9E393172C8";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "967EE51A-46B7-1A37-0ECE-F29EB438887C";
createNode displayLayerManager -n "layerManager";
	rename -uid "04317136-4453-F23C-9D26-7087C71E170D";
createNode displayLayer -n "defaultLayer";
	rename -uid "7A8EC1E3-4AA0-E83B-A4DD-94B1FB1EC59D";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "52B04C40-40BC-8F30-5141-AC9457E7FFE0";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "0B6CC093-448E-A8A4-0183-9382326F30CA";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "180A39AE-4964-EE4C-4360-ED8F45A938D8";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 150 -ast 1 -aet 250 ";
	setAttr ".st" 6;
createNode condition -n "R_weapon_blendMatrix_case01_cnd";
	rename -uid "E3412D39-4C58-FF1F-E7D8-DBAEFF4B7E37";
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 1 1 ;
createNode condition -n "R_weapon_blendMatrix_case02_cnd";
	rename -uid "48563EE2-47C5-E1CA-DC7E-ADB97FCD3479";
	setAttr ".st" 1;
	setAttr ".ct" -type "float3" 0 1 0 ;
	setAttr ".cf" -type "float3" 1 0 1 ;
createNode condition -n "R_weapon_blendMatrix_case03_cnd";
	rename -uid "68B50423-48C9-9986-D8FF-F49F683CAF6C";
	setAttr ".st" 2;
	setAttr ".ct" -type "float3" 0 0 1 ;
	setAttr ".cf" -type "float3" 1 1 0 ;
createNode plusMinusAverage -n "R_weapon_blendMatrix_pma";
	rename -uid "80B49B8B-4E81-2C83-892D-05AEB7802400";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "15F5A663-4A64-2C86-F0FE-21810F20822E";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n"
		+ "            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n"
		+ "            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n"
		+ "            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n"
		+ "            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 1\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n"
		+ "            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n"
		+ "            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n"
		+ "            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n"
		+ "            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1683\n            -height 1101\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner2\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner2\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n"
		+ "            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n"
		+ "            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            -ufeFilter \"USD\" \"InactivePrims\" -ufeFilterValue 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n"
		+ "            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n"
		+ "            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -ufeFilter \"USD\" \"InactivePrims\" -ufeFilterValue 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n"
		+ "                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n"
		+ "                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1.25\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n"
		+ "                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n"
		+ "                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n"
		+ "                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n"
		+ "                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -connectedGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n"
		+ "                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -showUnitConversions 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n"
		+ "                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -connectedGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -showUnitConversions 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"|persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n"
		+ "                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererOverrideName \"stereoOverrideVP2\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n"
		+ "                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n"
		+ "                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 0\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n"
		+ "            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n"
		+ "            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 0\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1683\\n    -height 1101\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 0\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1683\\n    -height 1101\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 1000 -size 1000 -divisions 10 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode condition -n "L_weapon_blendMatrix_case01_cnd";
	rename -uid "D83DE7B0-4635-C214-0FE8-0AA6DBD8351D";
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 1 1 ;
createNode condition -n "L_weapon_blendMatrix_case02_cnd";
	rename -uid "EFC2D21F-421A-A57B-991E-12814D5A8E43";
	setAttr ".st" 1;
	setAttr ".ct" -type "float3" 0 1 0 ;
	setAttr ".cf" -type "float3" 1 0 1 ;
createNode condition -n "L_weapon_blendMatrix_case03_cnd";
	rename -uid "1EF45FFA-4D7A-3FD3-385C-42B2AC49FB40";
	setAttr ".st" 2;
	setAttr ".ct" -type "float3" 0 0 1 ;
	setAttr ".cf" -type "float3" 1 1 0 ;
createNode plusMinusAverage -n "L_weapon_blendMatrix_pma";
	rename -uid "6BCCAFC5-48E1-D5EB-2041-FD9B7B232A63";
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "8EBDD25F-4151-2ABE-F926-6C94DF81C2F6";
	setAttr -s 2 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2824.999887744591 -1184.9201710027378 ;
	setAttr ".tgi[0].vh" -type "double2" 921.42853481429097 664.6820964370462 ;
	setAttr -s 16 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 825.71429443359375;
	setAttr ".tgi[0].ni[0].y" 134.28572082519531;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" -410;
	setAttr ".tgi[0].ni[1].y" 32.857143402099609;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -2154.970458984375;
	setAttr ".tgi[0].ni[2].y" -19.848506927490234;
	setAttr ".tgi[0].ni[2].nvs" 18306;
	setAttr ".tgi[0].ni[3].x" -102.85713958740234;
	setAttr ".tgi[0].ni[3].y" 32.857143402099609;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 1145.7142333984375;
	setAttr ".tgi[0].ni[4].y" 84.285713195800781;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -1463.374755859375;
	setAttr ".tgi[0].ni[5].y" 266.28277587890625;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" -536.30718994140625;
	setAttr ".tgi[0].ni[6].y" -924.86260986328125;
	setAttr ".tgi[0].ni[6].nvs" 18306;
	setAttr ".tgi[0].ni[7].x" 211.42857360839844;
	setAttr ".tgi[0].ni[7].y" -60;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -754.15625;
	setAttr ".tgi[0].ni[8].y" -161.4420166015625;
	setAttr ".tgi[0].ni[8].nvs" 18306;
	setAttr ".tgi[0].ni[9].x" -880.5098876953125;
	setAttr ".tgi[0].ni[9].y" 581.0262451171875;
	setAttr ".tgi[0].ni[9].nvs" 18306;
	setAttr ".tgi[0].ni[10].x" 518.5714111328125;
	setAttr ".tgi[0].ni[10].y" 134.28572082519531;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" -1583.8663330078125;
	setAttr ".tgi[0].ni[11].y" 148.94677734375;
	setAttr ".tgi[0].ni[11].nvs" 18306;
	setAttr ".tgi[0].ni[12].x" -241.31404113769531;
	setAttr ".tgi[0].ni[12].y" -239.517578125;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -1173.8868408203125;
	setAttr ".tgi[0].ni[13].y" -280.67471313476562;
	setAttr ".tgi[0].ni[13].nvs" 18306;
	setAttr ".tgi[0].ni[14].x" -1561.1695556640625;
	setAttr ".tgi[0].ni[14].y" -664.45660400390625;
	setAttr ".tgi[0].ni[14].nvs" 18306;
	setAttr ".tgi[0].ni[15].x" -1597.2567138671875;
	setAttr ".tgi[0].ni[15].y" -244.87599182128906;
	setAttr ".tgi[0].ni[15].nvs" 18306;
	setAttr ".tgi[1].tn" -type "string" "Untitled_2";
	setAttr ".tgi[1].vl" -type "double2" -2875.7355148652528 -527.62675764893504 ;
	setAttr ".tgi[1].vh" -type "double2" -609.06893826782448 591.42081693172827 ;
	setAttr -s 15 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" -1839.5238037109375;
	setAttr ".tgi[1].ni[0].y" 322.38095092773438;
	setAttr ".tgi[1].ni[0].nvs" 18306;
	setAttr ".tgi[1].ni[1].x" -2111.428466796875;
	setAttr ".tgi[1].ni[1].y" 131.42857360839844;
	setAttr ".tgi[1].ni[1].nvs" 18304;
	setAttr ".tgi[1].ni[2].x" -2470;
	setAttr ".tgi[1].ni[2].y" -451.42855834960938;
	setAttr ".tgi[1].ni[2].nvs" 18306;
	setAttr ".tgi[1].ni[3].x" -248.57142639160156;
	setAttr ".tgi[1].ni[3].y" 145.71427917480469;
	setAttr ".tgi[1].ni[3].nvs" 18304;
	setAttr ".tgi[1].ni[4].x" -862.85711669921875;
	setAttr ".tgi[1].ni[4].y" 95.714286804199219;
	setAttr ".tgi[1].ni[4].nvs" 18304;
	setAttr ".tgi[1].ni[5].x" 70;
	setAttr ".tgi[1].ni[5].y" 95.714286804199219;
	setAttr ".tgi[1].ni[5].nvs" 18304;
	setAttr ".tgi[1].ni[6].x" -2111.428466796875;
	setAttr ".tgi[1].ni[6].y" 30;
	setAttr ".tgi[1].ni[6].nvs" 18304;
	setAttr ".tgi[1].ni[7].x" -1482.857177734375;
	setAttr ".tgi[1].ni[7].y" 95.714286804199219;
	setAttr ".tgi[1].ni[7].nvs" 18304;
	setAttr ".tgi[1].ni[8].x" -2470;
	setAttr ".tgi[1].ni[8].y" 82.857139587402344;
	setAttr ".tgi[1].ni[8].nvs" 18306;
	setAttr ".tgi[1].ni[9].x" -2470;
	setAttr ".tgi[1].ni[9].y" -184.28572082519531;
	setAttr ".tgi[1].ni[9].nvs" 18306;
	setAttr ".tgi[1].ni[10].x" -1797.142822265625;
	setAttr ".tgi[1].ni[10].y" -72.619049072265625;
	setAttr ".tgi[1].ni[10].nvs" 18306;
	setAttr ".tgi[1].ni[11].x" -1175.7142333984375;
	setAttr ".tgi[1].ni[11].y" 95.714286804199219;
	setAttr ".tgi[1].ni[11].nvs" 18304;
	setAttr ".tgi[1].ni[12].x" -555.71429443359375;
	setAttr ".tgi[1].ni[12].y" 145.71427917480469;
	setAttr ".tgi[1].ni[12].nvs" 18304;
	setAttr ".tgi[1].ni[13].x" -2801.699462890625;
	setAttr ".tgi[1].ni[13].y" 718.365966796875;
	setAttr ".tgi[1].ni[13].nvs" 18306;
	setAttr ".tgi[1].ni[14].x" -2990.95849609375;
	setAttr ".tgi[1].ni[14].y" 267.08609008789062;
	setAttr ".tgi[1].ni[14].nvs" 18306;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av -k on ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".rm";
	setAttr -k on ".lm";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".hom";
	setAttr -k on ".hodm";
	setAttr -k on ".xry";
	setAttr -k on ".jxr";
	setAttr -k on ".sslt";
	setAttr -k on ".cbr";
	setAttr -k on ".bbr";
	setAttr -k on ".mhl";
	setAttr -k on ".cons";
	setAttr -k on ".vac";
	setAttr -av -k on ".hwi";
	setAttr -k on ".csvd";
	setAttr -av -k on ".ta";
	setAttr -av -k on ".tq";
	setAttr -k on ".ts";
	setAttr -av -k on ".etmr";
	setAttr -av -k on ".tmr";
	setAttr -av -k on ".aoon";
	setAttr -av -k on ".aoam";
	setAttr -av -k on ".aora";
	setAttr -k on ".aofr";
	setAttr -av -k on ".aosm";
	setAttr -av -k on ".hff";
	setAttr -av -k on ".hfd";
	setAttr -av -k on ".hfs";
	setAttr -av -k on ".hfe";
	setAttr -av ".hfc";
	setAttr -av -k on ".hfcr";
	setAttr -av -k on ".hfcg";
	setAttr -av -k on ".hfcb";
	setAttr -av -k on ".hfa";
	setAttr -av -k on ".mbe";
	setAttr -k on ".mbt";
	setAttr -av -k on ".mbsof";
	setAttr -k on ".mbsc";
	setAttr -k on ".mbc";
	setAttr -k on ".mbfa";
	setAttr -k on ".mbftb";
	setAttr -k on ".mbftg";
	setAttr -k on ".mbftr";
	setAttr -k on ".mbfta";
	setAttr -k on ".mbfe";
	setAttr -k on ".mbme";
	setAttr -k on ".mbcsx";
	setAttr -k on ".mbcsy";
	setAttr -k on ".mbasx";
	setAttr -k on ".mbasy";
	setAttr -av -k on ".blen";
	setAttr -k on ".blth";
	setAttr -k on ".blfr";
	setAttr -k on ".blfa";
	setAttr -av -k on ".blat";
	setAttr -av -k on ".msaa";
	setAttr -av -k on ".aasc";
	setAttr -k on ".aasq";
	setAttr -k on ".laa";
	setAttr -k on ".fprt" yes;
	setAttr -k on ".rtfm";
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
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 9 ".u";
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
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -k on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -k on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -k on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -k on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
lockNode -l 0 -lu 1;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -cb on ".macc";
	setAttr -av -cb on ".macd";
	setAttr -av -cb on ".macq";
	setAttr -av -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -av -k on ".clip";
	setAttr -av -k on ".edm";
	setAttr -av -k on ".edl";
	setAttr -av -cb on ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -av -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -av -cb on ".imfkey";
	setAttr -av -k on ".gama";
	setAttr -av -k on ".exrc";
	setAttr -av -k on ".expt";
	setAttr -av -cb on ".an";
	setAttr -cb on ".ar";
	setAttr -av -k on ".fs";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -av -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -av -cb on ".ep";
	setAttr -av -k on ".fec";
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
	setAttr -av -k on ".comp";
	setAttr -av -k on ".cth";
	setAttr -av -k on ".soll";
	setAttr -av -cb on ".sosl";
	setAttr -av -k on ".rd";
	setAttr -av -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -av -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -av -k on ".mm";
	setAttr -av -k on ".npu";
	setAttr -av -k on ".itf";
	setAttr -av -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -av -k on ".uf";
	setAttr -av -k on ".oi";
	setAttr -av -k on ".rut";
	setAttr -av -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -av -k on ".mbso";
	setAttr -av -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -av -k on ".pfb";
	setAttr -av -k on ".pram";
	setAttr -av -k on ".poam";
	setAttr -av -k on ".prlm";
	setAttr -av -k on ".polm";
	setAttr -av -cb on ".prm";
	setAttr -av -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -av -k on ".ubc";
	setAttr -av -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -av -k on ".udbx";
	setAttr -av -k on ".smc";
	setAttr -av -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -av -k on ".tlwd";
	setAttr -av -k on ".tlht";
	setAttr -av -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -av -cb on ".ope";
	setAttr -av -cb on ".oppf";
	setAttr -av -k on ".rcp";
	setAttr -av -k on ".icp";
	setAttr -av -k on ".ocp";
	setAttr -cb on ".hbl";
	setAttr ".dss" -type "string" "lambert1";
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
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
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
	setAttr -av -cb on ".hwcc";
	setAttr -av -cb on ".hwdp";
	setAttr -av -cb on ".hwql";
	setAttr -av -k on ".hwfr";
	setAttr -av -k on ".soll";
	setAttr -av -k on ".sosl";
	setAttr -av -k on ".bswa";
	setAttr -av -k on ".shml";
	setAttr -av -k on ".hwel";
connectAttr "handPropRGT_ctrl_tmpShape.gimbal" "handPropRGT_gmbCtrl_tmpShape.v";
connectAttr "handPropLFT_ctrl_tmpShape.gimbal" "handPropLFT_gmbCtrl_tmpShape.v";
connectAttr "R_weapon_blendMatrix.omat" "R_weapon_ctrl.opm";
connectAttr "L_weapon_blendMatrix.omat" "L_weapon_ctrl.opm";
connectAttr "L_Weapon_bJnt6_quatToEuler.ort" "L_Weapon_bJnt.r";
connectAttr "L_Weapon_bJnt1_deComp.ot" "L_Weapon_bJnt.t";
connectAttr "L_Weapon_bJnt1_deComp.os" "L_Weapon_bJnt.s";
connectAttr "root_tmp.s" "L_Weapon_bJnt.is";
connectAttr "root_tmp.s" "R_Weapon_bJnt.is";
connectAttr "R_Weapon_bJnt6_quatToEuler.ort" "R_Weapon_bJnt.r";
connectAttr "R_Weapon_bJnt1_deComp.ot" "R_Weapon_bJnt.t";
connectAttr "R_Weapon_bJnt1_deComp.os" "R_Weapon_bJnt.s";
connectAttr "R_origin_loc.wm" "R_weapon_blendMatrix.imat";
connectAttr "handPropRGT_gmbCtrl_tmp.wm" "R_weapon_blendMatrix.tgt[0].tmat";
connectAttr "R_weapon_blendMatrix_pma.o3y" "R_weapon_blendMatrix.tgt[0].wgt";
connectAttr "handPropLFT_gmbCtrl_tmp.wm" "R_weapon_blendMatrix.tgt[1].tmat";
connectAttr "R_weapon_blendMatrix_pma.o3z" "R_weapon_blendMatrix.tgt[1].wgt";
connectAttr "L_origin_loc.wm" "L_weapon_blendMatrix.imat";
connectAttr "handPropLFT_gmbCtrl_tmp.wm" "L_weapon_blendMatrix.tgt[0].tmat";
connectAttr "L_weapon_blendMatrix_pma.o3y" "L_weapon_blendMatrix.tgt[0].wgt";
connectAttr "handPropRGT_gmbCtrl_tmp.wm" "L_weapon_blendMatrix.tgt[1].tmat";
connectAttr "L_weapon_blendMatrix_pma.o3z" "L_weapon_blendMatrix.tgt[1].wgt";
connectAttr "L_Weapon_bJnt5_quatProd.oq" "L_Weapon_bJnt6_quatToEuler.iq";
connectAttr "L_Weapon_bJnt.ro" "L_Weapon_bJnt6_quatToEuler.iro";
connectAttr "L_Weapon_bJnt1_deComp.oq" "L_Weapon_bJnt5_quatProd.iq1";
connectAttr "L_Weapon_bJnt2_multMatrix.o" "L_Weapon_bJnt1_deComp.imat";
connectAttr "L_weapon_ctrl.wm" "L_Weapon_bJnt2_multMatrix.i[2]";
connectAttr "R_Weapon_bJnt5_quatProd.oq" "R_Weapon_bJnt6_quatToEuler.iq";
connectAttr "R_Weapon_bJnt.ro" "R_Weapon_bJnt6_quatToEuler.iro";
connectAttr "R_Weapon_bJnt1_deComp.oq" "R_Weapon_bJnt5_quatProd.iq1";
connectAttr "R_Weapon_bJnt2_multMatrix.o" "R_Weapon_bJnt1_deComp.imat";
connectAttr "R_weapon_ctrl.wm" "R_Weapon_bJnt2_multMatrix.i[2]";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "R_weapon_ctrlShape.SpaceSwitch" "R_weapon_blendMatrix_case01_cnd.ft"
		;
connectAttr "R_weapon_ctrlShape.SpaceSwitch" "R_weapon_blendMatrix_case02_cnd.ft"
		;
connectAttr "R_weapon_ctrlShape.SpaceSwitch" "R_weapon_blendMatrix_case03_cnd.ft"
		;
connectAttr "R_weapon_blendMatrix_case01_cnd.ocr" "R_weapon_blendMatrix_pma.i3[0].i3x"
		;
connectAttr "R_weapon_blendMatrix_case02_cnd.ocg" "R_weapon_blendMatrix_pma.i3[0].i3y"
		;
connectAttr "R_weapon_blendMatrix_case03_cnd.ocb" "R_weapon_blendMatrix_pma.i3[0].i3z"
		;
connectAttr "L_weapon_ctrlShape.SpaceSwitch" "L_weapon_blendMatrix_case01_cnd.ft"
		;
connectAttr "L_weapon_ctrlShape.SpaceSwitch" "L_weapon_blendMatrix_case02_cnd.ft"
		;
connectAttr "L_weapon_ctrlShape.SpaceSwitch" "L_weapon_blendMatrix_case03_cnd.ft"
		;
connectAttr "L_weapon_blendMatrix_case01_cnd.ocr" "L_weapon_blendMatrix_pma.i3[0].i3x"
		;
connectAttr "L_weapon_blendMatrix_case02_cnd.ocg" "L_weapon_blendMatrix_pma.i3[0].i3y"
		;
connectAttr "L_weapon_blendMatrix_case03_cnd.ocb" "L_weapon_blendMatrix_pma.i3[0].i3z"
		;
connectAttr "R_Weapon_bJnt6_quatToEuler.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "R_weapon_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "R_weapon_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "R_Weapon_bJnt2_multMatrix.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "R_Weapon_bJnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn";
connectAttr "handPropRGT_gmbCtrl_tmp.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "handPropLFT_gmbCtrl_tmp.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "R_Weapon_bJnt1_deComp.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "R_weapon_blendMatrix.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "R_origin_loc.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn";
connectAttr "R_Weapon_bJnt5_quatProd.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "R_weapon_blendMatrix_case01_cnd.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "handPropLFT_gmbCtrl_tmpShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "R_weapon_blendMatrix_pma.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn"
		;
connectAttr "R_weapon_blendMatrix_case03_cnd.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "R_weapon_blendMatrix_case02_cnd.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn"
		;
connectAttr "L_weapon_blendMatrix.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[0].dn"
		;
connectAttr "handPropLFT_gmbCtrl_tmp.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[1].dn"
		;
connectAttr "L_weapon_blendMatrix_case03_cnd.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[2].dn"
		;
connectAttr "L_Weapon_bJnt6_quatToEuler.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[3].dn"
		;
connectAttr "L_Weapon_bJnt1_deComp.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[4].dn"
		;
connectAttr "L_Weapon_bJnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[5].dn";
connectAttr "L_origin_loc.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[6].dn";
connectAttr "L_weapon_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[7].dn";
connectAttr "L_weapon_blendMatrix_case02_cnd.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[8].dn"
		;
connectAttr "L_weapon_blendMatrix_case01_cnd.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[9].dn"
		;
connectAttr "L_weapon_blendMatrix_pma.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[10].dn"
		;
connectAttr "L_Weapon_bJnt2_multMatrix.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[11].dn"
		;
connectAttr "L_Weapon_bJnt5_quatProd.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[12].dn"
		;
connectAttr "handPropRGT_gmbCtrl_tmp.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[13].dn"
		;
connectAttr "L_weapon_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[14].dn"
		;
connectAttr "L_Weapon_cnd.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "R_weapon_blendMatrix_case01_cnd.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "R_weapon_blendMatrix_case02_cnd.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "R_weapon_blendMatrix_case03_cnd.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "R_weapon_blendMatrix_pma.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "L_weapon_blendMatrix_case01_cnd.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "L_weapon_blendMatrix_case02_cnd.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "L_weapon_blendMatrix_case03_cnd.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "L_weapon_blendMatrix_pma.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of template_weapon_two_hand_v002.ma
