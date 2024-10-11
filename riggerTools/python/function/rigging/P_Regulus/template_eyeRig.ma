//Maya ASCII 2023 scene
//Name: eyeLFTZro_grp_ABC.ma
//Last modified: Wed, Oct 09, 2024 05:32:56 PM
//Codeset: 1252
requires maya "2023";
requires "stereoCamera" "10.0";
requires "mtoa" "5.1.2";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202205052215-234554116d";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 19045)";
fileInfo "UUID" "7FA2CF6D-44D7-FD79-A10A-C6A99C65EB1A";
createNode transform -n "eyeLFTZro_grp";
	rename -uid "6FDDE8D0-4644-7D60-6921-98BB19E01747";
	setAttr ".t" -type "double3" 5.2791419464969476 126.30026917177508 4.9975799792961446 ;
createNode transform -n "eyeLFTAim_grp" -p "eyeLFTZro_grp";
	rename -uid "9DFDDF54-4640-FF26-57FA-47864DC7D02E";
createNode transform -n "eyeLFT_ctrl" -p "eyeLFTAim_grp";
	rename -uid "A3B4D1F4-4D30-DEF1-C559-64973DA71FCA";
	setAttr ".ro" 2;
createNode nurbsCurve -n "eyeLFT_ctrlShape" -p "eyeLFT_ctrl";
	rename -uid "0A3953B3-4AA4-FC1C-90DD-43986DF9B3CC";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		0 7.1678029456090711 0
		0 4.7785352970727271 -4.7785352970727271
		0 0 -7.1678029456090711
		0 -4.7785352970727271 -4.7785352970727271
		0 -7.1678029456090711 0
		0 -4.7785352970727271 4.7785352970727271
		0 0 7.1678029456090711
		0 4.7785352970727271 4.7785352970727271
		0 7.1678029456090711 0
		4.7785352970727271 4.7785352970727271 0
		7.1678029456090711 0 0
		4.7785352970727271 -4.7785352970727271 0
		0 -7.1678029456090711 0
		-4.7785352970727271 -4.7785352970727271 0
		-7.1678029456090711 0 0
		-4.7785352970727271 4.7785352970727271 0
		0 7.1678029456090711 0
		;
	setAttr -k on ".gimbal";
createNode transform -n "eyeLFT_gmbCtrl" -p "eyeLFT_ctrl";
	rename -uid "CCD6B425-4B72-2397-D248-C7B648AD5CD2";
	setAttr -l on -k off ".v";
	setAttr ".ro" 2;
createNode nurbsCurve -n "eyeLFT_gmbCtrlShape" -p "eyeLFT_gmbCtrl";
	rename -uid "BCB14E22-49DC-F4CD-A947-63B3ACAF0234";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		0 1.0718334849114264 0
		0 0.71455565660761866 -0.71455565660761866
		0 0 -1.0718334849114264
		0 -0.71455565660761866 -0.71455565660761866
		0 -1.0718334849114264 0
		0 -0.71455565660761866 0.71455565660761866
		0 0 1.0718334849114264
		0 0.71455565660761866 0.71455565660761866
		0 1.0718334849114264 0
		0.71455565660761866 0.71455565660761866 0
		1.0718334849114264 0 0
		0.71455565660761866 -0.71455565660761866 0
		0 -1.0718334849114264 0
		-0.71455565660761866 -0.71455565660761866 0
		-1.0718334849114264 0 0
		-0.71455565660761866 0.71455565660761866 0
		0 1.0718334849114264 0
		;
createNode aimConstraint -n "eyeTargetLFT_aimCons" -p "eyeLFTAim_grp";
	rename -uid "6CC1352D-4049-DE7B-1D82-A486393A6949";
	addAttr -dcb 0 -ci true -sn "w0" -ln "eyeTargetLFT_ctrlW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".a" -type "double3" 0 0 1 ;
	setAttr ".wum" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 127.59796905517578 0.45919689536094666 1;
	setAttr ".wut" 2;
	setAttr ".rsrr" -type "double3" 0.019495315128306538 0.015096750688343657 2.5683908930660302e-06 ;
	setAttr -k on ".w0";
createNode transform -n "eyeRGTZro_grp";
	rename -uid "47F81E37-4058-BAB9-A3F3-79BB1783C9DD";
	setAttr ".t" -type "double3" -5.27914 126.3 4.99758 ;
	setAttr ".r" -type "double3" -179.99999914622637 0 0 ;
createNode transform -n "eyeRGTAim_grp" -p "eyeRGTZro_grp";
	rename -uid "34C6F97B-420D-5171-B29D-11A35BC0177B";
createNode transform -n "eyeRGT_ctrl" -p "eyeRGTAim_grp";
	rename -uid "F0C1066D-4C16-5DE8-D50A-14925D285497";
	setAttr ".ro" 2;
createNode nurbsCurve -n "eyeRGT_ctrlShape" -p "eyeRGT_ctrl";
	rename -uid "69414E6A-4D91-235A-7F1C-4AB63048CB57";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		3.8123171265815676e-15 7.1678029456090151 3.8123171265815676e-15
		3.8123171265815676e-15 4.7785352970726551 -4.7785352970727271
		3.8123171265815676e-15 -6.0997074025305082e-14 -7.1678029456090711
		3.8123171265815676e-15 -4.7785352970727919 -4.7785352970727271
		3.8123171265815676e-15 -7.1678029456091403 3.8123171265815676e-15
		3.8123171265815676e-15 -4.7785352970727919 4.7785352970727271
		3.8123171265815676e-15 -6.0997074025305082e-14 7.1678029456090711
		3.8123171265815676e-15 4.7785352970726551 4.7785352970727271
		3.8123171265815676e-15 7.1678029456090151 3.8123171265815676e-15
		4.7785352970727271 4.7785352970726551 3.8123171265815676e-15
		7.1678029456090711 -6.0997074025305082e-14 3.8123171265815676e-15
		4.7785352970727271 -4.7785352970727919 3.8123171265815676e-15
		3.8123171265815676e-15 -7.1678029456091403 3.8123171265815676e-15
		-4.7785352970727271 -4.7785352970727919 3.8123171265815676e-15
		-7.1678029456090711 -6.0997074025305082e-14 3.8123171265815676e-15
		-4.7785352970727271 4.7785352970726551 3.8123171265815676e-15
		3.8123171265815676e-15 7.1678029456090151 3.8123171265815676e-15
		;
	setAttr -k on ".gimbal";
createNode transform -n "eyeRGT_gmbCtrl" -p "eyeRGT_ctrl";
	rename -uid "C41C3E99-4B48-BA70-AB39-19B899E675F4";
	setAttr -l on -k off ".v";
	setAttr ".ro" 2;
createNode nurbsCurve -n "eyeRGT_gmbCtrlShape" -p "eyeRGT_gmbCtrl";
	rename -uid "BEBDF218-45DD-5A91-BD79-CB8A840C39B0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		0 1.0718334849114264 0
		0 0.71455565660761866 -0.71455565660761866
		0 0 -1.0718334849114264
		0 -0.71455565660761866 -0.71455565660761866
		0 -1.0718334849114264 0
		0 -0.71455565660761866 0.71455565660761866
		0 0 1.0718334849114264
		0 0.71455565660761866 0.71455565660761866
		0 1.0718334849114264 0
		0.71455565660761866 0.71455565660761866 0
		1.0718334849114264 0 0
		0.71455565660761866 -0.71455565660761866 0
		0 -1.0718334849114264 0
		-0.71455565660761866 -0.71455565660761866 0
		-1.0718334849114264 0 0
		-0.71455565660761866 0.71455565660761866 0
		0 1.0718334849114264 0
		;
createNode aimConstraint -n "eyeTargetRGT_aimCons" -p "eyeRGTAim_grp";
	rename -uid "94DC2C34-4433-CEDD-D04C-AF82B72C42CA";
	addAttr -dcb 0 -ci true -sn "w0" -ln "eyeTargetRGT_ctrlW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".a" -type "double3" 0 0 1 ;
	setAttr ".wum" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 127.59796905517578 0.45919689536094666 1;
	setAttr ".wut" 2;
	setAttr ".rsrr" -type "double3" -179.98056684959289 0.015102998285547453 -2.2504057210421568e-10 ;
	setAttr -k on ".w0";
createNode transform -n "eyeCenterLocal_grp";
	rename -uid "AB17433D-411C-B895-7E8D-1190A1903A1B";
	setAttr ".t" -type "double3" 0 126.28622501222546 46.272677727610926 ;
createNode transform -n "eyeCenterZro_grp";
	rename -uid "540B813C-4B0E-1D2C-4745-3584CCAD790B";
createNode transform -n "eyeCenterOffset_grp" -p "eyeCenterZro_grp";
	rename -uid "87F98A3C-4686-48AC-969C-48A11117AC94";
createNode transform -n "eyeCenter_ctrl" -p "eyeCenterOffset_grp";
	rename -uid "D095362E-49CB-C308-494C-2C924C666827";
	setAttr ".ro" 3;
createNode nurbsCurve -n "eyeCenter_ctrlShape" -p "eyeCenter_ctrl";
	rename -uid "386512CC-4FE2-E524-7D70-72B72DC9AB7A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 26 0 no 3
		27 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
		27
		-8.5468928263939379 0 0
		-8.4004454890460885 1.1123641077864814 0
		-7.9710887158688752 2.1489253809450504 0
		-7.2880771322217894 3.039039316755765 0
		-6.3979631964110748 3.7220509004028499 0
		-5.3614019232525081 4.1514076735800591 0
		-4.2490378154660267 4.2978550109279121 0
		4.2490378154660267 4.2978550109279121 0
		5.3614019232525081 4.1514076735800591 0
		6.3979631964110748 3.7220509004028499 0
		7.2880771322217894 3.039039316755765 0
		7.9710887158688752 2.1489253809450504 0
		8.4004454890460885 1.1123641077864814 0
		8.5468928263939379 0 0
		8.4004454890460885 -1.1123641077864814 0
		7.9710887158688752 -2.1489253809450504 0
		7.2880771322217894 -3.039039316755765 0
		6.3979631964110748 -3.7220509004028499 0
		5.3614019232525081 -4.1514076735800591 0
		4.2490378154660267 -4.2978550109279121 0
		-4.2490378154660267 -4.2978550109279121 0
		-5.3614019232525081 -4.1514076735800591 0
		-6.3979631964110748 -3.7220509004028499 0
		-7.2880771322217894 -3.039039316755765 0
		-7.9710887158688752 -2.1489253809450504 0
		-8.4004454890460885 -1.1123641077864814 0
		-8.5468928263939379 0 0
		;
createNode transform -n "eyeTargetLFTZro_grp" -p "eyeCenter_ctrl";
	rename -uid "A9994D86-4AAA-9F39-F17E-CF9766F27F7E";
	setAttr ".t" -type "double3" 5.2900174405810576 0 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1.0000000000000002 ;
createNode transform -n "eyeTargetLFT_ctrl" -p "eyeTargetLFTZro_grp";
	rename -uid "24E25BFD-4DC1-9F1B-FC35-FF894C92EC5D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".ro" 2;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "eyeTargetLFT_ctrlShape" -p "eyeTargetLFT_ctrl";
	rename -uid "0B2067C6-4E43-46EA-4B68-47990278B844";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 2.0870550832330315 0
		0 -2.0870550832330315 0
		0 0 0
		0 0 -2.0870550832330315
		0 0 2.0870550832330315
		0 0 0
		2.0870550832330315 0 0
		-2.0870550832330315 0 0
		-1.6696440665864256 0 0
		-1.6490890784826788 0.26118909991238104 0
		-1.587926677035485 0.51594840052433755 0
		-1.4876645508369712 0.75800337943363827 0
		-1.3507704338175492 0.98139173767850252 0
		-1.1806170069917277 1.1806170069917277 0
		-0.98139173767850252 1.3507704338175492 0
		-0.75800337943363827 1.4876645508369712 0
		-0.51594840052433755 1.587926677035485 0
		-0.26119076955644749 1.6490874088386129 0
		0 1.6696440665864256 0
		0.26118909991238104 1.6490874088386129 0
		0.51594840052433755 1.587926677035485 0
		0.75800337943363827 1.4876645508369712 0
		0.98139173767850252 1.3507704338175492 0
		1.1806170069917277 1.1806170069917277 0
		1.3507704338175492 0.98139173767850252 0
		1.4876645508369712 0.75800337943363827 0
		1.587926677035485 0.51594840052433755 0
		1.6490874088386129 0.26118909991238104 0
		1.6696440665864256 0 0
		1.6490874088386129 -0.26118909991238104 0
		1.587926677035485 -0.51594840052433755 0
		1.4876645508369712 -0.75800337943363827 0
		1.3507704338175492 -0.98139173767850252 0
		1.1806170069917277 -1.1806170069917277 0
		0.98139173767850252 -1.3507704338175492 0
		0.75800337943363827 -1.4876645508369712 0
		0.51594840052433755 -1.587926677035485 0
		0.26118909991238104 -1.6490874088386129 0
		0 -1.6696440665864256 0
		-0.26119076955644749 -1.6490874088386129 0
		-0.51594840052433755 -1.587926677035485 0
		-0.75800337943363827 -1.4876645508369712 0
		-0.98139173767850252 -1.3507704338175492 0
		-1.1806170069917277 -1.1806170069917277 0
		-1.3507704338175492 -0.98139173767850252 0
		-1.4876645508369712 -0.75800337943363827 0
		-1.587926677035485 -0.51594840052433755 0
		-1.6490890784826788 -0.26118909991238104 0
		-1.6696440665864256 0 0
		-1.6490890784826788 0 0.26118909991238104
		-1.587926677035485 0 0.51594840052433755
		-1.4876645508369712 0 0.75800337943363827
		-1.3507704338175492 0 0.98139173767850252
		-1.1806170069917277 0 1.1806170069917277
		-0.98139173767850252 0 1.3507704338175492
		-0.75800337943363827 0 1.4876645508369712
		-0.51594840052433755 0 1.587926677035485
		-0.26119076955644749 0 1.6490874088386129
		0 0 1.6696440665864256
		0.26118909991238104 0 1.6490874088386129
		0.51594840052433755 0 1.587926677035485
		0.75800337943363827 0 1.4876645508369712
		0.98139173767850252 0 1.3507704338175492
		1.1806170069917277 0 1.1806170069917277
		1.3507704338175492 0 0.98139173767850252
		1.4876645508369712 0 0.75800337943363827
		1.587926677035485 0 0.51594840052433755
		1.6490874088386129 0 0.26118909991238104
		1.6696440665864256 0 0
		1.6490874088386129 0 -0.26118909991238104
		1.587926677035485 0 -0.51594840052433755
		1.4876645508369712 0 -0.75800337943363827
		1.3507704338175492 0 -0.98139173767850252
		1.1806170069917277 0 -1.1806170069917277
		0.98139173767850252 0 -1.3507704338175492
		0.75800337943363827 0 -1.4876645508369712
		0.51594840052433755 0 -1.587926677035485
		0.26118909991238104 0 -1.6490874088386129
		0 0 -1.6696440665864256
		-0.26119076955644749 0 -1.6490874088386129
		-0.51594840052433755 0 -1.587926677035485
		-0.75800337943363827 0 -1.4876645508369712
		-0.98139173767850252 0 -1.3507704338175492
		-1.1806170069917277 0 -1.1806170069917277
		-1.3507704338175492 0 -0.98139173767850252
		-1.4876645508369712 0 -0.75800337943363827
		-1.587926677035485 0 -0.51594840052433755
		-1.6490890784826788 0 -0.26118909991238104
		-1.6696440665864256 0 0
		-1.6490890784826788 0 0.26118909991238104
		-1.587926677035485 0 0.51594840052433755
		-1.4876645508369712 0 0.75800337943363827
		-1.3507704338175492 0 0.98139173767850252
		-1.1806170069917277 0 1.1806170069917277
		-0.98139173767850252 0 1.3507704338175492
		-0.75800337943363827 0 1.4876645508369712
		-0.51594840052433755 0 1.587926677035485
		-0.26119076955644749 0 1.6490874088386129
		0 0 1.6696440665864256
		-7.7840642992732418e-09 0.26118909991238104 1.6490874088386129
		-1.537645345970235e-08 0.51594840052433755 1.587926677035485
		-2.2590284220914342e-08 0.75800337943363827 1.4876645508369712
		-2.9247822972021064e-08 0.98139173767850252 1.3507704338175492
		-3.5185077272802368e-08 1.1806170069917277 1.1806170069917277
		-4.025612023183868e-08 1.3507704338175492 0.98139173767850252
		-4.4335895508542551e-08 1.4876645508369712 0.75800337943363827
		-4.7323890530105629e-08 1.587926677035485 0.51594840052433755
		-4.9146640957598091e-08 1.6490874088386129 0.26118909991238104
		-4.9759233365628601e-08 1.6696440665864256 0
		-4.9146640957598091e-08 1.6490874088386129 -0.26118909991238104
		-4.7323890530105629e-08 1.587926677035485 -0.51594840052433755
		-4.4335895508542551e-08 1.4876645508369712 -0.75800337943363827
		-4.025612023183868e-08 1.3507704338175492 -0.98139173767850252
		-3.5185077272802368e-08 1.1806170069917277 -1.1806170069917277
		-2.9247822972021064e-08 0.98139173767850252 -1.3507704338175492
		-2.2590284220914342e-08 0.75800337943363827 -1.4876645508369712
		-1.537645345970235e-08 0.51594840052433755 -1.587926677035485
		-7.7840642992732418e-09 0.26118909991238104 -1.6490874088386129
		0 0 -1.6696440665864256
		0 -0.26119076955644749 -1.6490874088386129
		0 -0.51594840052433755 -1.587926677035485
		0 -0.75800337943363827 -1.4876645508369712
		0 -0.98139340732256952 -1.3507704338175492
		0 -1.1806170069917277 -1.1806170069917277
		0 -1.3507704338175492 -0.98139173767850252
		0 -1.4876645508369712 -0.75800337943363827
		0 -1.587926677035485 -0.51594840052433755
		0 -1.6490890784826788 -0.26118909991238104
		0 -1.6696440665864256 0
		0 -1.6490890784826788 0.26118909991238104
		0 -1.587926677035485 0.51594840052433755
		0 -1.4876645508369712 0.75800337943363827
		0 -1.3507704338175492 0.98139173767850252
		0 -1.1806170069917277 1.1806170069917277
		0 -0.98139340732256952 1.3507704338175492
		0 -0.75800337943363827 1.4876645508369712
		0 -0.51594840052433755 1.587926677035485
		0 -0.26119076955644749 1.6490874088386129
		0 0 1.6696440665864256
		;
createNode transform -n "eyeTargetRGTZro_grp" -p "eyeCenter_ctrl";
	rename -uid "15E96627-4707-C432-A702-FFA5C30C61E8";
	setAttr ".t" -type "double3" -5.2900199999999993 -0.00022501222547077759 2.2272389081479105e-05 ;
	setAttr ".r" -type "double3" 180 0 0 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1.0000000000000002 ;
createNode transform -n "eyeTargetRGT_ctrl" -p "eyeTargetRGTZro_grp";
	rename -uid "D9103DE0-4308-C2C9-EA25-5BB07D50CE77";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".ro" 2;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "eyeTargetRGT_ctrlShape" -p "eyeTargetRGT_ctrl";
	rename -uid "919321A8-4D2F-63E1-2DE5-5CB66941EB45";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 2.0870550832330315 0
		0 -2.0870550832330315 0
		0 0 0
		0 0 -2.0870550832330315
		0 0 2.0870550832330315
		0 0 0
		2.0870550832330315 0 0
		-2.0870550832330315 0 0
		-1.6696440665864256 0 0
		-1.6490890784826788 0.26118909991238104 0
		-1.587926677035485 0.51594840052433755 0
		-1.4876645508369712 0.75800337943363827 0
		-1.3507704338175492 0.98139173767850252 0
		-1.1806170069917277 1.1806170069917277 0
		-0.98139173767850252 1.3507704338175492 0
		-0.75800337943363827 1.4876645508369712 0
		-0.51594840052433755 1.587926677035485 0
		-0.26119076955644749 1.6490874088386129 0
		0 1.6696440665864256 0
		0.26118909991238104 1.6490874088386129 0
		0.51594840052433755 1.587926677035485 0
		0.75800337943363827 1.4876645508369712 0
		0.98139173767850252 1.3507704338175492 0
		1.1806170069917277 1.1806170069917277 0
		1.3507704338175492 0.98139173767850252 0
		1.4876645508369712 0.75800337943363827 0
		1.587926677035485 0.51594840052433755 0
		1.6490874088386129 0.26118909991238104 0
		1.6696440665864256 0 0
		1.6490874088386129 -0.26118909991238104 0
		1.587926677035485 -0.51594840052433755 0
		1.4876645508369712 -0.75800337943363827 0
		1.3507704338175492 -0.98139173767850252 0
		1.1806170069917277 -1.1806170069917277 0
		0.98139173767850252 -1.3507704338175492 0
		0.75800337943363827 -1.4876645508369712 0
		0.51594840052433755 -1.587926677035485 0
		0.26118909991238104 -1.6490874088386129 0
		0 -1.6696440665864256 0
		-0.26119076955644749 -1.6490874088386129 0
		-0.51594840052433755 -1.587926677035485 0
		-0.75800337943363827 -1.4876645508369712 0
		-0.98139173767850252 -1.3507704338175492 0
		-1.1806170069917277 -1.1806170069917277 0
		-1.3507704338175492 -0.98139173767850252 0
		-1.4876645508369712 -0.75800337943363827 0
		-1.587926677035485 -0.51594840052433755 0
		-1.6490890784826788 -0.26118909991238104 0
		-1.6696440665864256 0 0
		-1.6490890784826788 0 0.26118909991238104
		-1.587926677035485 0 0.51594840052433755
		-1.4876645508369712 0 0.75800337943363827
		-1.3507704338175492 0 0.98139173767850252
		-1.1806170069917277 0 1.1806170069917277
		-0.98139173767850252 0 1.3507704338175492
		-0.75800337943363827 0 1.4876645508369712
		-0.51594840052433755 0 1.587926677035485
		-0.26119076955644749 0 1.6490874088386129
		0 0 1.6696440665864256
		0.26118909991238104 0 1.6490874088386129
		0.51594840052433755 0 1.587926677035485
		0.75800337943363827 0 1.4876645508369712
		0.98139173767850252 0 1.3507704338175492
		1.1806170069917277 0 1.1806170069917277
		1.3507704338175492 0 0.98139173767850252
		1.4876645508369712 0 0.75800337943363827
		1.587926677035485 0 0.51594840052433755
		1.6490874088386129 0 0.26118909991238104
		1.6696440665864256 0 0
		1.6490874088386129 0 -0.26118909991238104
		1.587926677035485 0 -0.51594840052433755
		1.4876645508369712 0 -0.75800337943363827
		1.3507704338175492 0 -0.98139173767850252
		1.1806170069917277 0 -1.1806170069917277
		0.98139173767850252 0 -1.3507704338175492
		0.75800337943363827 0 -1.4876645508369712
		0.51594840052433755 0 -1.587926677035485
		0.26118909991238104 0 -1.6490874088386129
		0 0 -1.6696440665864256
		-0.26119076955644749 0 -1.6490874088386129
		-0.51594840052433755 0 -1.587926677035485
		-0.75800337943363827 0 -1.4876645508369712
		-0.98139173767850252 0 -1.3507704338175492
		-1.1806170069917277 0 -1.1806170069917277
		-1.3507704338175492 0 -0.98139173767850252
		-1.4876645508369712 0 -0.75800337943363827
		-1.587926677035485 0 -0.51594840052433755
		-1.6490890784826788 0 -0.26118909991238104
		-1.6696440665864256 0 0
		-1.6490890784826788 0 0.26118909991238104
		-1.587926677035485 0 0.51594840052433755
		-1.4876645508369712 0 0.75800337943363827
		-1.3507704338175492 0 0.98139173767850252
		-1.1806170069917277 0 1.1806170069917277
		-0.98139173767850252 0 1.3507704338175492
		-0.75800337943363827 0 1.4876645508369712
		-0.51594840052433755 0 1.587926677035485
		-0.26119076955644749 0 1.6490874088386129
		0 0 1.6696440665864256
		-7.7840642992732418e-09 0.26118909991238104 1.6490874088386129
		-1.537645345970235e-08 0.51594840052433755 1.587926677035485
		-2.2590284220914342e-08 0.75800337943363827 1.4876645508369712
		-2.9247822972021064e-08 0.98139173767850252 1.3507704338175492
		-3.5185077272802368e-08 1.1806170069917277 1.1806170069917277
		-4.025612023183868e-08 1.3507704338175492 0.98139173767850252
		-4.4335895508542551e-08 1.4876645508369712 0.75800337943363827
		-4.7323890530105629e-08 1.587926677035485 0.51594840052433755
		-4.9146640957598091e-08 1.6490874088386129 0.26118909991238104
		-4.9759233365628601e-08 1.6696440665864256 0
		-4.9146640957598091e-08 1.6490874088386129 -0.26118909991238104
		-4.7323890530105629e-08 1.587926677035485 -0.51594840052433755
		-4.4335895508542551e-08 1.4876645508369712 -0.75800337943363827
		-4.025612023183868e-08 1.3507704338175492 -0.98139173767850252
		-3.5185077272802368e-08 1.1806170069917277 -1.1806170069917277
		-2.9247822972021064e-08 0.98139173767850252 -1.3507704338175492
		-2.2590284220914342e-08 0.75800337943363827 -1.4876645508369712
		-1.537645345970235e-08 0.51594840052433755 -1.587926677035485
		-7.7840642992732418e-09 0.26118909991238104 -1.6490874088386129
		0 0 -1.6696440665864256
		0 -0.26119076955644749 -1.6490874088386129
		0 -0.51594840052433755 -1.587926677035485
		0 -0.75800337943363827 -1.4876645508369712
		0 -0.98139340732256952 -1.3507704338175492
		0 -1.1806170069917277 -1.1806170069917277
		0 -1.3507704338175492 -0.98139173767850252
		0 -1.4876645508369712 -0.75800337943363827
		0 -1.587926677035485 -0.51594840052433755
		0 -1.6490890784826788 -0.26118909991238104
		0 -1.6696440665864256 0
		0 -1.6490890784826788 0.26118909991238104
		0 -1.587926677035485 0.51594840052433755
		0 -1.4876645508369712 0.75800337943363827
		0 -1.3507704338175492 0.98139173767850252
		0 -1.1806170069917277 1.1806170069917277
		0 -0.98139340732256952 1.3507704338175492
		0 -0.75800337943363827 1.4876645508369712
		0 -0.51594840052433755 1.587926677035485
		0 -0.26119076955644749 1.6490874088386129
		0 0 1.6696440665864256
		;
createNode parentConstraint -n "eyeCenterZroGrp_orientCons" -p "eyeCenterZro_grp";
	rename -uid "CE0F446A-4E92-BD84-6AD8-EBBB60EBE168";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "worldW1" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "localW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".rst" -type "double3" 0 -1.3117440429503233 45.813480832249979 ;
	setAttr -k on ".w1" 0;
	setAttr -k on ".w0";
createNode transform -n "eyeCenterWorld_grp";
	rename -uid "510FAAA0-4515-2621-F29A-779F2934BB1E";
	setAttr ".t" -type "double3" 0 126.28622501222546 46.272677727610926 ;
createNode joint -n "eyeLFT_bJnt";
	rename -uid "EE690048-48C5-5F40-8BDE-479F44B106E6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 1;
	setAttr ".t" -type "double3" 5.2791419464969476 126.30026917177507 4.9975799792961437 ;
	setAttr ".r" -type "double3" -3.1060104311167141e-18 3.1060104311167148e-18 7.583033279093542e-22 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1.0000000000000002 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1.0000000000000002 0 0 0 0 1.0000000000000002 0
		 5.2791419464969476 126.30026917177507 4.9975799792961437 1;
	setAttr ".liw" yes;
createNode joint -n "eyeRGT_bJnt";
	rename -uid "EAA6BF88-4B9E-EB75-AB4A-ED8735BC2522";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 1;
	setAttr ".t" -type "double3" -5.2791399999999991 126.3 4.99758 ;
	setAttr ".r" -type "double3" 6.407467762939192e-15 6.212020862258855e-18 3.4123186924313371e-21 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 1 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 0 0 0 0 -1 -1.4901160872223127e-08 0
		 0 1.4901160872223127e-08 -1 0 -5.2791399999999991 126.3 4.9975800000000001 1;
	setAttr ".liw" yes;
createNode reverse -n "eyeCenterZroGrpOrientCons_rev";
	rename -uid "C2A4C5AB-4079-E275-E251-E1A303CAF0F4";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 68;
	setAttr -av -k on ".unw" 68;
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
	setAttr -k on ".hwi";
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
	setAttr -k on ".hff";
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
	setAttr -k on ".blen";
	setAttr -k on ".blth";
	setAttr -k on ".blfr";
	setAttr -k on ".blfa";
	setAttr -k on ".blat";
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
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 15 ".u";
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
	setAttr -k on ".ai_surface_shader";
	setAttr -k on ".ai_volume_shader";
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
	setAttr -k on ".ai_surface_shader";
	setAttr -k on ".ai_volume_shader";
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
	setAttr -k on ".exrc";
	setAttr -k on ".expt";
	setAttr -av -cb on ".an";
	setAttr -cb on ".ar";
	setAttr -av -k on ".fs" 1;
	setAttr -av -k on ".ef" 10;
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
	setAttr -cb on ".sosl";
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
	setAttr -cb on ".ihi";
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
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".gsn";
	setAttr -k on ".gsv";
connectAttr "eyeTargetLFT_aimCons.crx" "eyeLFTAim_grp.rx";
connectAttr "eyeTargetLFT_aimCons.cry" "eyeLFTAim_grp.ry";
connectAttr "eyeTargetLFT_aimCons.crz" "eyeLFTAim_grp.rz";
connectAttr "eyeLFT_ctrlShape.gimbal" "eyeLFT_gmbCtrlShape.v";
connectAttr "eyeLFTAim_grp.pim" "eyeTargetLFT_aimCons.cpim";
connectAttr "eyeLFTAim_grp.t" "eyeTargetLFT_aimCons.ct";
connectAttr "eyeLFTAim_grp.rp" "eyeTargetLFT_aimCons.crp";
connectAttr "eyeLFTAim_grp.rpt" "eyeTargetLFT_aimCons.crt";
connectAttr "eyeLFTAim_grp.ro" "eyeTargetLFT_aimCons.cro";
connectAttr "eyeTargetLFT_ctrl.t" "eyeTargetLFT_aimCons.tg[0].tt";
connectAttr "eyeTargetLFT_ctrl.rp" "eyeTargetLFT_aimCons.tg[0].trp";
connectAttr "eyeTargetLFT_ctrl.rpt" "eyeTargetLFT_aimCons.tg[0].trt";
connectAttr "eyeTargetLFT_ctrl.pm" "eyeTargetLFT_aimCons.tg[0].tpm";
connectAttr "eyeTargetLFT_aimCons.w0" "eyeTargetLFT_aimCons.tg[0].tw";
connectAttr "eyeTargetRGT_aimCons.crx" "eyeRGTAim_grp.rx";
connectAttr "eyeTargetRGT_aimCons.cry" "eyeRGTAim_grp.ry";
connectAttr "eyeTargetRGT_aimCons.crz" "eyeRGTAim_grp.rz";
connectAttr "eyeRGT_ctrlShape.gimbal" "eyeRGT_gmbCtrlShape.v";
connectAttr "eyeRGTAim_grp.pim" "eyeTargetRGT_aimCons.cpim";
connectAttr "eyeRGTAim_grp.t" "eyeTargetRGT_aimCons.ct";
connectAttr "eyeRGTAim_grp.rp" "eyeTargetRGT_aimCons.crp";
connectAttr "eyeRGTAim_grp.rpt" "eyeTargetRGT_aimCons.crt";
connectAttr "eyeRGTAim_grp.ro" "eyeTargetRGT_aimCons.cro";
connectAttr "eyeTargetRGT_ctrl.t" "eyeTargetRGT_aimCons.tg[0].tt";
connectAttr "eyeTargetRGT_ctrl.rp" "eyeTargetRGT_aimCons.tg[0].trp";
connectAttr "eyeTargetRGT_ctrl.rpt" "eyeTargetRGT_aimCons.tg[0].trt";
connectAttr "eyeTargetRGT_ctrl.pm" "eyeTargetRGT_aimCons.tg[0].tpm";
connectAttr "eyeTargetRGT_aimCons.w0" "eyeTargetRGT_aimCons.tg[0].tw";
connectAttr "eyeCenterZroGrp_orientCons.ctx" "eyeCenterZro_grp.tx";
connectAttr "eyeCenterZroGrp_orientCons.cty" "eyeCenterZro_grp.ty";
connectAttr "eyeCenterZroGrp_orientCons.ctz" "eyeCenterZro_grp.tz";
connectAttr "eyeCenterZroGrp_orientCons.crx" "eyeCenterZro_grp.rx";
connectAttr "eyeCenterZroGrp_orientCons.cry" "eyeCenterZro_grp.ry";
connectAttr "eyeCenterZroGrp_orientCons.crz" "eyeCenterZro_grp.rz";
connectAttr "eyeCenterZro_grp.ro" "eyeCenterZroGrp_orientCons.cro";
connectAttr "eyeCenterZro_grp.pim" "eyeCenterZroGrp_orientCons.cpim";
connectAttr "eyeCenterZro_grp.rp" "eyeCenterZroGrp_orientCons.crp";
connectAttr "eyeCenterZro_grp.rpt" "eyeCenterZroGrp_orientCons.crt";
connectAttr "eyeCenterLocal_grp.t" "eyeCenterZroGrp_orientCons.tg[0].tt";
connectAttr "eyeCenterLocal_grp.rp" "eyeCenterZroGrp_orientCons.tg[0].trp";
connectAttr "eyeCenterLocal_grp.rpt" "eyeCenterZroGrp_orientCons.tg[0].trt";
connectAttr "eyeCenterLocal_grp.r" "eyeCenterZroGrp_orientCons.tg[0].tr";
connectAttr "eyeCenterLocal_grp.ro" "eyeCenterZroGrp_orientCons.tg[0].tro";
connectAttr "eyeCenterLocal_grp.s" "eyeCenterZroGrp_orientCons.tg[0].ts";
connectAttr "eyeCenterLocal_grp.pm" "eyeCenterZroGrp_orientCons.tg[0].tpm";
connectAttr "eyeCenterZroGrp_orientCons.w0" "eyeCenterZroGrp_orientCons.tg[0].tw"
		;
connectAttr "eyeCenterWorld_grp.t" "eyeCenterZroGrp_orientCons.tg[1].tt";
connectAttr "eyeCenterWorld_grp.rp" "eyeCenterZroGrp_orientCons.tg[1].trp";
connectAttr "eyeCenterWorld_grp.rpt" "eyeCenterZroGrp_orientCons.tg[1].trt";
connectAttr "eyeCenterWorld_grp.r" "eyeCenterZroGrp_orientCons.tg[1].tr";
connectAttr "eyeCenterWorld_grp.ro" "eyeCenterZroGrp_orientCons.tg[1].tro";
connectAttr "eyeCenterWorld_grp.s" "eyeCenterZroGrp_orientCons.tg[1].ts";
connectAttr "eyeCenterWorld_grp.pm" "eyeCenterZroGrp_orientCons.tg[1].tpm";
connectAttr "eyeCenterZroGrp_orientCons.w1" "eyeCenterZroGrp_orientCons.tg[1].tw"
		;
connectAttr "eyeCenterZroGrpOrientCons_rev.ox" "eyeCenterZroGrp_orientCons.w0";
// End of eyeLFTZro_grp_ABC.ma
