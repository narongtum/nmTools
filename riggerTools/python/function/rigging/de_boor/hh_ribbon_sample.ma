//Maya ASCII 2023 scene
//Name: hh_ribbon_sample.ma
//Last modified: Thu, Dec 12, 2024 11:12:04 AM
//Codeset: 1252
requires maya "2023";
requires -nodeType "ikSpringSolver" "ikSpringSolver" "1.0";
requires "mtoa" "5.1.2";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202205052215-234554116d";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 19045)";
fileInfo "UUID" "3D4B7D1D-4B52-BCF4-CEED-CB9D938F7F55";
createNode transform -s -n "persp";
	rename -uid "33D003C8-4EEB-972D-A9F7-E39296BD238E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 10.975334848731109 4.4334422102469313 31.172611515861895 ;
	setAttr ".r" -type "double3" -1.5383527296040382 22.600000000002169 -5.3829741023962817e-17 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "1FFD5A05-4540-5D9C-8D34-C1BE77FD580F";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 34.080438875074528;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "78111352-4183-8D40-C398-39B67A53C976";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "02DB270F-4022-EC69-A33C-0CBDB0BD22A9";
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
	rename -uid "99004422-4D34-B157-8474-72B59AF1F9CF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "2E6D396D-46F5-8461-21B0-0CBD5B3DB12E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "2AB7DC92-4FD3-5D37-EE6F-72B744EB3443";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "DC2D719A-4D00-BA11-4C38-ACBFBFF4D2CF";
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
createNode transform -n "locator1";
	rename -uid "03DB7E57-4D83-CC08-8912-A493AC6A5967";
	setAttr ".t" -type "double3" -12 0 0 ;
createNode locator -n "locatorShape1" -p "locator1";
	rename -uid "BC18E0C0-4B86-C9F8-6B9F-E0BBB3C8E4CE";
	setAttr -k off ".v";
createNode transform -n "locator2";
	rename -uid "AB601CAF-4BA0-1BB5-57A2-49B1611E825C";
createNode locator -n "locatorShape2" -p "locator2";
	rename -uid "6AF0DEE1-498F-E72C-3673-8FBAE91BEC74";
	setAttr -k off ".v";
createNode transform -n "locator3";
	rename -uid "DCBC307C-4035-AA41-B85C-3FB5879D84A5";
	setAttr ".t" -type "double3" 12 0 0 ;
createNode locator -n "locatorShape3" -p "locator3";
	rename -uid "61CAF196-4D6A-299B-39E5-939E94FC26C7";
	setAttr -k off ".v";
createNode transform -n "ribbon_MOD_GRP";
	rename -uid "7F5F3216-454F-4E2E-9192-43B53BDDFCFE";
	setAttr ".t" -type "double3" -12 0 0 ;
createNode transform -n "ribbon_CTLS_GRP" -p "ribbon_MOD_GRP";
	rename -uid "5C15673D-4BBD-B15D-03A4-E6B623A9C990";
createNode transform -n "ribbon_0_CTL" -p "ribbon_CTLS_GRP";
	rename -uid "71ED412D-4EAD-90FE-386F-AEBABCEE0974";
createNode nurbsCurve -n "ribbon_0_CTL0Shape" -p "ribbon_0_CTL";
	rename -uid "2EE6A843-4E72-754F-CFF6-CDACD76E682B";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.7982373409884725e-17 0.7836116248912246 -0.78361162489122449
		4.1550626846842558e-33 1.1081941875543877 -6.7857323231109122e-17
		-4.7982373409884725e-17 0.78361162489122438 0.78361162489122449
		-6.7857323231109146e-17 5.7448982375248304e-17 1.1081941875543881
		-4.7982373409884725e-17 -0.78361162489122449 0.78361162489122449
		-6.7973144778085889e-33 -1.1081941875543884 1.1100856969603225e-16
		4.7982373409884725e-17 -0.78361162489122438 -0.78361162489122449
		6.7857323231109146e-17 -1.511240500779959e-16 -1.1081941875543881
		4.7982373409884725e-17 0.7836116248912246 -0.78361162489122449
		4.1550626846842558e-33 1.1081941875543877 -6.7857323231109122e-17
		-4.7982373409884725e-17 0.78361162489122438 0.78361162489122449
		;
createNode nurbsCurve -n "ribbon_0_CTL1Shape" -p "ribbon_0_CTL";
	rename -uid "864CB46E-4FD8-B4CD-DBA1-B4B435D2C996";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 4.7982373409884731e-17 -0.7836116248912246
		6.7857323231109122e-17 6.7857323231109122e-17 -1.1081941875543877
		-0.78361162489122449 4.7982373409884719e-17 -0.78361162489122438
		-1.1081941875543881 3.5177356190060272e-33 -5.7448982375248304e-17
		-0.78361162489122449 -4.7982373409884725e-17 0.78361162489122449
		-1.1100856969603225e-16 -6.7857323231109171e-17 1.1081941875543884
		0.78361162489122449 -4.7982373409884719e-17 0.78361162489122438
		1.1081941875543881 -9.2536792101100989e-33 1.511240500779959e-16
		0.78361162489122449 4.7982373409884731e-17 -0.7836116248912246
		6.7857323231109122e-17 6.7857323231109122e-17 -1.1081941875543877
		-0.78361162489122449 4.7982373409884719e-17 -0.78361162489122438
		;
createNode nurbsCurve -n "ribbon_0_CTL2Shape" -p "ribbon_0_CTL";
	rename -uid "9402EA8E-41C7-E0ED-5826-EF972CE30077";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-1.1100856969603225e-16 -1.1081941875543884 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "ribbon_1_CTL" -p "ribbon_CTLS_GRP";
	rename -uid "375BE9DD-4639-E1E8-8FA4-5F94876945DB";
	setAttr ".t" -type "double3" 13.048127450807863 18.213904664891675 1.9212716843700974 ;
createNode nurbsCurve -n "ribbon_1_CTL0Shape" -p "ribbon_1_CTL";
	rename -uid "FB10BD6E-4481-58A0-C3B1-2D92C5EE7F35";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.7982373409884725e-17 0.7836116248912246 -0.78361162489122449
		4.1550626846842558e-33 1.1081941875543877 -6.7857323231109122e-17
		-4.7982373409884725e-17 0.78361162489122438 0.78361162489122449
		-6.7857323231109146e-17 5.7448982375248304e-17 1.1081941875543881
		-4.7982373409884725e-17 -0.78361162489122449 0.78361162489122449
		-6.7973144778085889e-33 -1.1081941875543884 1.1100856969603225e-16
		4.7982373409884725e-17 -0.78361162489122438 -0.78361162489122449
		6.7857323231109146e-17 -1.511240500779959e-16 -1.1081941875543881
		4.7982373409884725e-17 0.7836116248912246 -0.78361162489122449
		4.1550626846842558e-33 1.1081941875543877 -6.7857323231109122e-17
		-4.7982373409884725e-17 0.78361162489122438 0.78361162489122449
		;
createNode nurbsCurve -n "ribbon_1_CTL1Shape" -p "ribbon_1_CTL";
	rename -uid "33042B9B-4193-9C90-474F-A797807D6515";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 4.7982373409884731e-17 -0.7836116248912246
		6.7857323231109122e-17 6.7857323231109122e-17 -1.1081941875543877
		-0.78361162489122449 4.7982373409884719e-17 -0.78361162489122438
		-1.1081941875543881 3.5177356190060272e-33 -5.7448982375248304e-17
		-0.78361162489122449 -4.7982373409884725e-17 0.78361162489122449
		-1.1100856969603225e-16 -6.7857323231109171e-17 1.1081941875543884
		0.78361162489122449 -4.7982373409884719e-17 0.78361162489122438
		1.1081941875543881 -9.2536792101100989e-33 1.511240500779959e-16
		0.78361162489122449 4.7982373409884731e-17 -0.7836116248912246
		6.7857323231109122e-17 6.7857323231109122e-17 -1.1081941875543877
		-0.78361162489122449 4.7982373409884719e-17 -0.78361162489122438
		;
createNode nurbsCurve -n "ribbon_1_CTL2Shape" -p "ribbon_1_CTL";
	rename -uid "0006ECEF-48C7-FE7B-950C-01BAA2E147BD";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-1.1100856969603225e-16 -1.1081941875543884 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "ribbon_2_CTL" -p "ribbon_CTLS_GRP";
	rename -uid "545B184E-4019-E86F-E74A-4B87EFB732D1";
	setAttr ".t" -type "double3" 24 0 0 ;
createNode nurbsCurve -n "ribbon_2_CTL0Shape" -p "ribbon_2_CTL";
	rename -uid "C5D0396D-49BC-F1E6-8047-2583C9B39931";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.7982373409884725e-17 0.7836116248912246 -0.78361162489122449
		4.1550626846842558e-33 1.1081941875543877 -6.7857323231109122e-17
		-4.7982373409884725e-17 0.78361162489122438 0.78361162489122449
		-6.7857323231109146e-17 5.7448982375248304e-17 1.1081941875543881
		-4.7982373409884725e-17 -0.78361162489122449 0.78361162489122449
		-6.7973144778085889e-33 -1.1081941875543884 1.1100856969603225e-16
		4.7982373409884725e-17 -0.78361162489122438 -0.78361162489122449
		6.7857323231109146e-17 -1.511240500779959e-16 -1.1081941875543881
		4.7982373409884725e-17 0.7836116248912246 -0.78361162489122449
		4.1550626846842558e-33 1.1081941875543877 -6.7857323231109122e-17
		-4.7982373409884725e-17 0.78361162489122438 0.78361162489122449
		;
createNode nurbsCurve -n "ribbon_2_CTL1Shape" -p "ribbon_2_CTL";
	rename -uid "C701B164-426C-2170-C469-289672D4B48E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 4.7982373409884731e-17 -0.7836116248912246
		6.7857323231109122e-17 6.7857323231109122e-17 -1.1081941875543877
		-0.78361162489122449 4.7982373409884719e-17 -0.78361162489122438
		-1.1081941875543881 3.5177356190060272e-33 -5.7448982375248304e-17
		-0.78361162489122449 -4.7982373409884725e-17 0.78361162489122449
		-1.1100856969603225e-16 -6.7857323231109171e-17 1.1081941875543884
		0.78361162489122449 -4.7982373409884719e-17 0.78361162489122438
		1.1081941875543881 -9.2536792101100989e-33 1.511240500779959e-16
		0.78361162489122449 4.7982373409884731e-17 -0.7836116248912246
		6.7857323231109122e-17 6.7857323231109122e-17 -1.1081941875543877
		-0.78361162489122449 4.7982373409884719e-17 -0.78361162489122438
		;
createNode nurbsCurve -n "ribbon_2_CTL2Shape" -p "ribbon_2_CTL";
	rename -uid "C94CBFD9-4A11-058E-644D-9AB7C2A93C62";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-1.1100856969603225e-16 -1.1081941875543884 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "ribbon_JNTS_GRP" -p "ribbon_MOD_GRP";
	rename -uid "36C49375-4287-DB4E-8CC0-F8B9E1023F65";
createNode joint -n "ribbon_0_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "0F6B1287-49AC-A2C4-F317-3CBC71C203F9";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_1_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "B3DC7625-4437-CB89-0004-7EBC2547408B";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_2_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "99D0893D-4778-AEDA-9297-86B237F8D813";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_3_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "A0DB825D-49FD-BE53-ADDE-4CABE588C3AC";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_4_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "FBAEE813-4054-6FD6-5D04-41BAE0CA143B";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_5_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "F7A5FF25-4E01-B854-97C9-CBA2372666DF";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_6_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "05AA55A5-483C-E2EA-F4E1-DA9C3530DAA7";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_7_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "B9269351-43CC-2693-6423-D7920DF248C1";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_8_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "66F6DC50-4CB4-75C6-17FA-DBA388EF0EAE";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode joint -n "ribbon_9_JNT" -p "ribbon_JNTS_GRP";
	rename -uid "4B1FB323-49C2-ECE7-F34E-DDA36E7C7AC3";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D90C47D9-4338-7703-70F9-EAB3DBC318CD";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "01D45373-435C-D877-B72C-129E699D070C";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "88A40B73-4309-03FD-EA64-B5974D748B24";
createNode displayLayerManager -n "layerManager";
	rename -uid "73BB9E4D-4F85-6FE8-30AC-7DBCF64CB888";
createNode displayLayer -n "defaultLayer";
	rename -uid "3949F735-4A65-35BA-C422-4696E35F8DE3";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "29E01AD4-4AE9-7503-A530-C7BCCDE8CDF9";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "7F34DC2D-4C53-F641-F6EA-E3B0698FFF2D";
	setAttr ".g" yes;
createNode multMatrix -n "ribbon_parentOffset_0_MM";
	rename -uid "00E2E658-4367-8EB0-D725-14A0B9C53F9E";
	setAttr -s 2 ".i";
createNode pickMatrix -n "ribbon_translation_0_PM";
	rename -uid "B42A051A-4D34-3F06-6933-308FDBAFBA1C";
	setAttr ".sca" no;
	setAttr ".she" no;
	setAttr ".rot" no;
createNode pickMatrix -n "ribbon_scaleOffset_0_PM";
	rename -uid "975EA1CE-40B4-EB41-1D3D-E196603B2193";
	setAttr ".tra" no;
	setAttr ".she" no;
	setAttr ".rot" no;
createNode multMatrix -n "ribbon_parentOffset_1_MM";
	rename -uid "F576071F-40E6-ECD9-F76E-BB875D67BF22";
	setAttr -s 2 ".i";
createNode pickMatrix -n "ribbon_translation_1_PM";
	rename -uid "1F846713-443C-9E10-5B81-0DB5014E0BE3";
	setAttr ".sca" no;
	setAttr ".she" no;
	setAttr ".rot" no;
createNode pickMatrix -n "ribbon_scaleOffset_1_PM";
	rename -uid "C748CE57-4449-2B67-5312-DC94EE188C48";
	setAttr ".tra" no;
	setAttr ".she" no;
	setAttr ".rot" no;
createNode multMatrix -n "ribbon_parentOffset_2_MM";
	rename -uid "23EADDF6-4607-F497-8EEE-35BBE872A54C";
	setAttr -s 2 ".i";
createNode pickMatrix -n "ribbon_translation_2_PM";
	rename -uid "EF88F1E4-4B36-0758-21C5-D69B1E9CCBAD";
	setAttr ".sca" no;
	setAttr ".she" no;
	setAttr ".rot" no;
createNode pickMatrix -n "ribbon_scaleOffset_2_PM";
	rename -uid "304AA745-409C-312C-D52B-DC9A4A9ABB79";
	setAttr ".tra" no;
	setAttr ".she" no;
	setAttr ".rot" no;
createNode wtAddMatrix -n "ribbon_position_0_WAM";
	rename -uid "CA96EEAC-429C-5E58-D517-36926248AFA2";
	setAttr ".i[0].w" 1;
createNode wtAddMatrix -n "ribbon_tangent_0_WAM";
	rename -uid "B7000063-4386-A75F-2196-B2BC62F22F86";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.998001;
	setAttr ".i[1].w" 0.001998;
	setAttr ".i[2].w" 1e-06;
createNode wtAddMatrix -n "ribbon_up_0_WAM";
	rename -uid "4E1D56C1-4E7C-778C-98BB-82883F79EA03";
	setAttr ".i[0].w" 1;
createNode multMatrix -n "ribbon_upOffset_0_MM";
	rename -uid "DB886C56-4E73-6600-D25C-EEBB4CD31299";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 12 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_0_AM";
	rename -uid "D831D689-4B7E-475C-A5E0-A983DC8A3C21";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 0 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 1 0 ;
createNode wtAddMatrix -n "ribbon_scale_0_WAM";
	rename -uid "EF6DC346-4B16-5072-785C-D0B1EE77B255";
	setAttr ".i[0].w" 1;
createNode multMatrix -n "ribbon_scale_0_MM";
	rename -uid "52AB04EA-4464-182B-3EBF-1C9EDFB82287";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_1_WAM";
	rename -uid "CA9A7C10-4E5B-AA7A-0AB7-BC8EE1B1735F";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.79012345679012341;
	setAttr ".i[1].w" 0.19753086419753085;
	setAttr ".i[2].w" 0.012345679012345678;
createNode wtAddMatrix -n "ribbon_tangent_1_WAM";
	rename -uid "52C7256E-40EC-0617-12DD-A5BF01974466";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.78834667901234579;
	setAttr ".i[1].w" 0.19908441975308641;
	setAttr ".i[2].w" 0.0125689012345679;
createNode wtAddMatrix -n "ribbon_up_1_WAM";
	rename -uid "A22ABCB5-4974-D786-4E25-B8A762F51627";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.79012345679012341;
	setAttr ".i[1].w" 0.19753086419753085;
	setAttr ".i[2].w" 0.012345679012345678;
createNode multMatrix -n "ribbon_upOffset_1_MM";
	rename -uid "942C8DB2-4ED9-1597-95AA-208605E494DC";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.3333333333333339 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_1_AM";
	rename -uid "DD0A5775-4F91-1C5A-B182-CD9E8FFCB980";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 1 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 0 1 ;
createNode wtAddMatrix -n "ribbon_scale_1_WAM";
	rename -uid "5B767230-414E-EE04-D32B-C8BEC55E49C0";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.79012345679012341;
	setAttr ".i[1].w" 0.19753086419753085;
	setAttr ".i[2].w" 0.012345679012345678;
createNode multMatrix -n "ribbon_scale_1_MM";
	rename -uid "54D5F4A3-4065-3985-C458-778D1F49AC4C";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_2_WAM";
	rename -uid "5EB7AA58-4108-4D2B-93C3-AF84D24C585F";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.60493827160493829;
	setAttr ".i[1].w" 0.34567901234567899;
	setAttr ".i[2].w" 0.049382716049382713;
createNode wtAddMatrix -n "ribbon_tangent_2_WAM";
	rename -uid "9038C428-405F-9FB5-03E9-C7AF68363025";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.60338371604938268;
	setAttr ".i[1].w" 0.34678812345679011;
	setAttr ".i[2].w" 0.049828160493827156;
createNode wtAddMatrix -n "ribbon_up_2_WAM";
	rename -uid "6F41C875-4AA0-CE11-6EF8-498911D78F23";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.60493827160493829;
	setAttr ".i[1].w" 0.34567901234567899;
	setAttr ".i[2].w" 0.049382716049382713;
createNode multMatrix -n "ribbon_upOffset_2_MM";
	rename -uid "5EFC0BF5-4824-58C2-D908-2F980F3756D5";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 6.666666666666667 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_2_AM";
	rename -uid "62D390F9-4578-0C18-DE5C-A1BA53ABC991";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 1 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 0 1 ;
createNode wtAddMatrix -n "ribbon_scale_2_WAM";
	rename -uid "A8DF4B2E-4720-8251-7085-4FA9BDDCDC9A";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.60493827160493829;
	setAttr ".i[1].w" 0.34567901234567899;
	setAttr ".i[2].w" 0.049382716049382713;
createNode multMatrix -n "ribbon_scale_2_MM";
	rename -uid "692BD1BF-40B9-4E8B-F133-0EB171231FE0";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_3_WAM";
	rename -uid "0FB4AE08-4CAB-FD7C-81D9-87B339A18AF2";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.44444444444444453;
	setAttr ".i[1].w" 0.44444444444444448;
	setAttr ".i[2].w" 0.1111111111111111;
createNode wtAddMatrix -n "ribbon_tangent_3_WAM";
	rename -uid "621C9D45-43A1-0B07-1A1D-75A83EA4C637";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.44311211111111104;
	setAttr ".i[1].w" 0.44510911111111107;
	setAttr ".i[2].w" 0.11177877777777777;
createNode wtAddMatrix -n "ribbon_up_3_WAM";
	rename -uid "E7327FF5-4850-9839-834C-66994090D813";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.44444444444444453;
	setAttr ".i[1].w" 0.44444444444444448;
	setAttr ".i[2].w" 0.1111111111111111;
createNode multMatrix -n "ribbon_upOffset_3_MM";
	rename -uid "6D15825F-4824-88B7-3611-2581C593FC25";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 0.99999999999999978 0 0 0 0 0.99999999999999978 0 0
		 0 0 0.99999999999999978 0 4 0 0 0.99999999999999978;
createNode aimMatrix -n "ribbon_pointOnCurve_3_AM";
	rename -uid "AB22604E-4B2B-D3D5-5ACD-43A737783D7B";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 0 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 1 0 ;
createNode wtAddMatrix -n "ribbon_scale_3_WAM";
	rename -uid "148E9FA8-41E8-08C7-8829-51988ED6EEBF";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.44444444444444453;
	setAttr ".i[1].w" 0.44444444444444448;
	setAttr ".i[2].w" 0.1111111111111111;
createNode multMatrix -n "ribbon_scale_3_MM";
	rename -uid "8D6737A8-497B-1B9C-7312-71BE63A93947";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_4_WAM";
	rename -uid "32ABC0B0-4B1F-7297-AE4D-0E8ECAD426F9";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.30864197530864201;
	setAttr ".i[1].w" 0.49382716049382713;
	setAttr ".i[2].w" 0.19753086419753085;
createNode wtAddMatrix -n "ribbon_tangent_4_WAM";
	rename -uid "D7B14460-42B9-D5CD-FAD3-BFB4239461CC";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.30753186419753087;
	setAttr ".i[1].w" 0.49404738271604937;
	setAttr ".i[2].w" 0.19842075308641974;
createNode wtAddMatrix -n "ribbon_up_4_WAM";
	rename -uid "4A16765B-44E3-C708-5EA1-C6B80B2D12D6";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.30864197530864201;
	setAttr ".i[1].w" 0.49382716049382713;
	setAttr ".i[2].w" 0.19753086419753085;
createNode multMatrix -n "ribbon_upOffset_4_MM";
	rename -uid "92C26A62-46C3-6FFE-4458-FC88E89EF3BE";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 1.3333333333333339 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_4_AM";
	rename -uid "9E424725-49A5-D009-6908-32939B8C7BD5";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 0 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 1 0 ;
createNode wtAddMatrix -n "ribbon_scale_4_WAM";
	rename -uid "43ED69B1-49B6-A131-27E9-60A9A7714F4D";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.30864197530864201;
	setAttr ".i[1].w" 0.49382716049382713;
	setAttr ".i[2].w" 0.19753086419753085;
createNode multMatrix -n "ribbon_scale_4_MM";
	rename -uid "CDF7ED47-491B-5594-22F3-B6AB87CA0AF5";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_5_WAM";
	rename -uid "2D715B95-422A-96EC-FA7C-818630A3207D";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.19753086419753085;
	setAttr ".i[1].w" 0.49382716049382713;
	setAttr ".i[2].w" 0.30864197530864201;
createNode wtAddMatrix -n "ribbon_tangent_5_WAM";
	rename -uid "5154D466-4216-512A-8681-70A3D608FAC6";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.19664297530864194;
	setAttr ".i[1].w" 0.49360293827160495;
	setAttr ".i[2].w" 0.30975408641975311;
createNode wtAddMatrix -n "ribbon_up_5_WAM";
	rename -uid "06778022-42BC-0083-AF75-48AA6C27FE13";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.19753086419753085;
	setAttr ".i[1].w" 0.49382716049382713;
	setAttr ".i[2].w" 0.30864197530864201;
createNode multMatrix -n "ribbon_upOffset_5_MM";
	rename -uid "72C02F6B-46E6-ADFA-ABA6-74A1E881CD1B";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.3333333333333339 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_5_AM";
	rename -uid "1D1961D4-49DB-1B85-4D10-C18FF06A6861";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 0 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 1 0 ;
createNode wtAddMatrix -n "ribbon_scale_5_WAM";
	rename -uid "59295FB6-496C-C616-993C-C4A57092434E";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.19753086419753085;
	setAttr ".i[1].w" 0.49382716049382713;
	setAttr ".i[2].w" 0.30864197530864201;
createNode multMatrix -n "ribbon_scale_5_MM";
	rename -uid "8D3411AC-4E03-49E1-D08C-CF9B7D8F22B3";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_6_WAM";
	rename -uid "DC7C3830-48CE-2ECD-EC3C-D1AEBD72D314";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.11111111111111113;
	setAttr ".i[1].w" 0.44444444444444448;
	setAttr ".i[2].w" 0.44444444444444442;
createNode wtAddMatrix -n "ribbon_tangent_6_WAM";
	rename -uid "8765965F-473B-DA2C-B9E1-A9B78FE4CCA3";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.11044544444444447;
	setAttr ".i[1].w" 0.44377577777777782;
	setAttr ".i[2].w" 0.44577877777777775;
createNode wtAddMatrix -n "ribbon_up_6_WAM";
	rename -uid "85CC13B7-46B9-6150-2466-F28AA9732E22";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.11111111111111113;
	setAttr ".i[1].w" 0.44444444444444448;
	setAttr ".i[2].w" 0.44444444444444442;
createNode multMatrix -n "ribbon_upOffset_6_MM";
	rename -uid "5AA84C54-4A89-D4F8-6534-77B7EC3A81EB";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -4 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_6_AM";
	rename -uid "E7FF60B2-4558-96FA-362C-838A45862990";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 0 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 1 0 ;
createNode wtAddMatrix -n "ribbon_scale_6_WAM";
	rename -uid "FA0F32F2-4F05-E811-7F37-F0A91AFBA4BC";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.11111111111111113;
	setAttr ".i[1].w" 0.44444444444444448;
	setAttr ".i[2].w" 0.44444444444444442;
createNode multMatrix -n "ribbon_scale_6_MM";
	rename -uid "5B95B7FA-4AA3-785D-074D-E18742BBB15B";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_7_WAM";
	rename -uid "9A5A00B5-4C7F-8972-7394-4F8EED1C0812";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.049382716049382713;
	setAttr ".i[1].w" 0.34567901234567899;
	setAttr ".i[2].w" 0.60493827160493829;
createNode wtAddMatrix -n "ribbon_tangent_7_WAM";
	rename -uid "F08D6A9F-4FB7-237E-3FBE-F098BDAAF6FB";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.048939271604938266;
	setAttr ".i[1].w" 0.34456590123456787;
	setAttr ".i[2].w" 0.60649482716049385;
createNode wtAddMatrix -n "ribbon_up_7_WAM";
	rename -uid "85225F21-46BF-7EEC-6DCD-938B07EEAD3D";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.049382716049382713;
	setAttr ".i[1].w" 0.34567901234567899;
	setAttr ".i[2].w" 0.60493827160493829;
createNode multMatrix -n "ribbon_upOffset_7_MM";
	rename -uid "04B37D15-492C-51FF-5A51-CF97CF538887";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -6.6666666666666679 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_7_AM";
	rename -uid "E1018B07-4446-FB71-9827-0F80F1A54A3F";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 0 0 0 ;
	setAttr ".sm" 1;
createNode wtAddMatrix -n "ribbon_scale_7_WAM";
	rename -uid "DC78076A-4589-F326-26CF-838FB9723B65";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.049382716049382713;
	setAttr ".i[1].w" 0.34567901234567899;
	setAttr ".i[2].w" 0.60493827160493829;
createNode multMatrix -n "ribbon_scale_7_MM";
	rename -uid "F79ED877-49DB-9EC8-E022-849CD1102202";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_8_WAM";
	rename -uid "D9C385BD-4767-C799-537C-6299D97D5015";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.01234567901234569;
	setAttr ".i[1].w" 0.19753086419753094;
	setAttr ".i[2].w" 0.79012345679012341;
createNode wtAddMatrix -n "ribbon_tangent_8_WAM";
	rename -uid "34755898-4C46-8236-AB77-48866C831460";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.012124456790123467;
	setAttr ".i[1].w" 0.19597330864197537;
	setAttr ".i[2].w" 0.7919022345679011;
createNode wtAddMatrix -n "ribbon_up_8_WAM";
	rename -uid "5711C883-4298-DA47-B862-4BA7EBCF4E87";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.01234567901234569;
	setAttr ".i[1].w" 0.19753086419753094;
	setAttr ".i[2].w" 0.79012345679012341;
createNode multMatrix -n "ribbon_upOffset_8_MM";
	rename -uid "2FA05795-4EAC-E749-6A9D-B8B876E64475";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.3333333333333321 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_8_AM";
	rename -uid "00C5D255-4231-E928-35B4-74A0FB7F961E";
	setAttr ".pmi" -type "double3" 0 1 0 ;
	setAttr ".smi" -type "double3" 0 0 1 ;
	setAttr ".sm" 2;
	setAttr ".smiv" -type "double3" 0 0 1 ;
createNode wtAddMatrix -n "ribbon_scale_8_WAM";
	rename -uid "B581A768-4477-DB1A-CD18-78A73F7D2304";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 0.01234567901234569;
	setAttr ".i[1].w" 0.19753086419753094;
	setAttr ".i[2].w" 0.79012345679012341;
createNode multMatrix -n "ribbon_scale_8_MM";
	rename -uid "A17055D3-4A9A-A5A0-5764-E99476FC3E3F";
	setAttr -s 2 ".i";
createNode wtAddMatrix -n "ribbon_position_9_WAM";
	rename -uid "3639017F-419E-5AC9-ABD5-AEB06E31C072";
	setAttr ".i[2].w" 1;
createNode wtAddMatrix -n "ribbon_tangent_9_WAM";
	rename -uid "5FA213C5-4C19-2BF7-8279-DBB28EF00C49";
	setAttr -s 3 ".i";
	setAttr ".i[0].w" 4.0000000000000074e-06;
	setAttr ".i[1].w" 0.0039920000000000034;
	setAttr ".i[2].w" 0.996004;
createNode wtAddMatrix -n "ribbon_up_9_WAM";
	rename -uid "5D60711B-4025-A898-7C2D-4AB8DA13CE37";
	setAttr ".i[2].w" 1;
createNode multMatrix -n "ribbon_upOffset_9_MM";
	rename -uid "600E2FAF-41E2-0E42-D2A3-7E80B943931D";
	setAttr -s 2 ".i";
	setAttr ".i[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -12 0 0 1;
createNode aimMatrix -n "ribbon_pointOnCurve_9_AM";
	rename -uid "C96EAFF7-4CE2-10D5-6C18-55853E82FC96";
	setAttr ".pmi" -type "double3" 0 -1 0 ;
	setAttr ".smi" -type "double3" 0 0 0 ;
	setAttr ".sm" 1;
	setAttr ".smiv" -type "double3" 0 1 0 ;
createNode wtAddMatrix -n "ribbon_scale_9_WAM";
	rename -uid "EF89C733-4E02-DE16-110A-BC9B61DEBEE9";
	setAttr ".i[2].w" 1;
createNode multMatrix -n "ribbon_scale_9_MM";
	rename -uid "16D9A3BD-4041-3175-3DB4-38A925F21E59";
	setAttr -s 2 ".i";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "1B042AD8-43E2-11C9-FB32-BCB9CA778247";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"updateModelPanelBar\" \n            -camera \"|persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n"
		+ "            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n"
		+ "            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 876\n            -height 1104\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n"
		+ "            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n"
		+ "            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n"
		+ "            -captureSequenceNumber -1\n            -width 644\n            -height 1104\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n"
		+ "            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n"
		+ "            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n"
		+ "            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"|persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n"
		+ "            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n"
		+ "            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n"
		+ "            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 0\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1759\n            -height 1104\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n"
		+ "            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n"
		+ "            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n"
		+ "            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n"
		+ "            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -ufeFilter \"USD\" \"InactivePrims\" -ufeFilterValue 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n"
		+ "                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n"
		+ "                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -keyMinScale 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n"
		+ "                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n"
		+ "                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n"
		+ "                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n"
		+ "                -additiveGraphingMode 0\n                -connectedGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -showUnitConversions 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n"
		+ "                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -connectedGraphingMode 1\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n"
		+ "                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -showUnitConversions 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"vertical2\\\" -ps 1 50 100 -ps 2 50 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Top View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Top View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -camera \\\"|persp\\\" \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 0\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 876\\n    -height 1104\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Top View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"updateModelPanelBar\\\" \\n    -camera \\\"|persp\\\" \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 0\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 876\\n    -height 1104\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Script Editor\")) \n\t\t\t\t\t\"scriptedPanel\"\n\t\t\t\t\t\"$panelName = `scriptedPanel -unParent  -type \\\"scriptEditorPanel\\\" -l (localizedPanelLabel(\\\"Script Editor\\\")) -mbv $menusOkayInPanels `\"\n\t\t\t\t\t\"scriptedPanel -edit -l (localizedPanelLabel(\\\"Script Editor\\\")) -mbv $menusOkayInPanels  $panelName\"\n\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "170839D2-4015-1892-B2AD-D1AC114EB100";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 100 -ast 0 -aet 391 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "56F4B0FA-4A10-80C4-94C9-B3B55AACABB7";
	setAttr -s 2 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 26.004772457536255 -660.44281564292976 ;
	setAttr ".tgi[0].vh" -type "double2" 2293.2315996198381 458.88135322921522 ;
	setAttr -s 21 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 447.14285278320312;
	setAttr ".tgi[0].ni[0].y" -197.14285278320312;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 140;
	setAttr ".tgi[0].ni[1].y" 55.714286804199219;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 140;
	setAttr ".tgi[0].ni[2].y" -45.714286804199219;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 754.28570556640625;
	setAttr ".tgi[0].ni[3].y" -94.285713195800781;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 140;
	setAttr ".tgi[0].ni[4].y" -248.57142639160156;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" 447.14285278320312;
	setAttr ".tgi[0].ni[5].y" 5.7142858505249023;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 1061.4285888671875;
	setAttr ".tgi[0].ni[6].y" -358.57144165039062;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" 1061.4285888671875;
	setAttr ".tgi[0].ni[7].y" -155.71427917480469;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" 1368.5714111328125;
	setAttr ".tgi[0].ni[8].y" -207.14285278320312;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" 1677.142822265625;
	setAttr ".tgi[0].ni[9].y" -105.71428680419922;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 1061.4285888671875;
	setAttr ".tgi[0].ni[10].y" 47.142856597900391;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 140;
	setAttr ".tgi[0].ni[11].y" -147.14285278320312;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 754.28570556640625;
	setAttr ".tgi[0].ni[12].y" 108.57142639160156;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" 754.28570556640625;
	setAttr ".tgi[0].ni[13].y" 7.1428570747375488;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" 1061.4285888671875;
	setAttr ".tgi[0].ni[14].y" -54.285713195800781;
	setAttr ".tgi[0].ni[14].nvs" 18304;
	setAttr ".tgi[0].ni[15].x" 1061.4285888671875;
	setAttr ".tgi[0].ni[15].y" 148.57142639160156;
	setAttr ".tgi[0].ni[15].nvs" 18304;
	setAttr ".tgi[0].ni[16].x" 1984.2857666015625;
	setAttr ".tgi[0].ni[16].y" -105.71428680419922;
	setAttr ".tgi[0].ni[16].nvs" 18304;
	setAttr ".tgi[0].ni[17].x" 447.14285278320312;
	setAttr ".tgi[0].ni[17].y" -95.714286804199219;
	setAttr ".tgi[0].ni[17].nvs" 18304;
	setAttr ".tgi[0].ni[18].x" 1061.4285888671875;
	setAttr ".tgi[0].ni[18].y" -257.14285278320312;
	setAttr ".tgi[0].ni[18].nvs" 18304;
	setAttr ".tgi[0].ni[19].x" 754.28570556640625;
	setAttr ".tgi[0].ni[19].y" 210;
	setAttr ".tgi[0].ni[19].nvs" 18304;
	setAttr ".tgi[0].ni[20].x" 1368.5714111328125;
	setAttr ".tgi[0].ni[20].y" -4.2857141494750977;
	setAttr ".tgi[0].ni[20].nvs" 18304;
	setAttr ".tgi[1].tn" -type "string" "Untitled_2";
	setAttr ".tgi[1].vl" -type "double2" 4753.9850973343546 -836.21634907227372 ;
	setAttr ".tgi[1].vh" -type "double2" 6353.9850524555641 -46.300404842264541 ;
	setAttr -s 19 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" 3604.28564453125;
	setAttr ".tgi[1].ni[0].y" -447.14285278320312;
	setAttr ".tgi[1].ni[0].nvs" 18304;
	setAttr ".tgi[1].ni[1].x" 3604.28564453125;
	setAttr ".tgi[1].ni[1].y" -548.5714111328125;
	setAttr ".tgi[1].ni[1].nvs" 18304;
	setAttr ".tgi[1].ni[2].x" 5448.5712890625;
	setAttr ".tgi[1].ni[2].y" -417.14285278320312;
	setAttr ".tgi[1].ni[2].nvs" 18304;
	setAttr ".tgi[1].ni[3].x" 4218.5712890625;
	setAttr ".tgi[1].ni[3].y" -380;
	setAttr ".tgi[1].ni[3].nvs" 18304;
	setAttr ".tgi[1].ni[4].x" 4832.85693359375;
	setAttr ".tgi[1].ni[4].y" -475.71429443359375;
	setAttr ".tgi[1].ni[4].nvs" 18304;
	setAttr ".tgi[1].ni[5].x" 3911.428466796875;
	setAttr ".tgi[1].ni[5].y" -307.14285278320312;
	setAttr ".tgi[1].ni[5].nvs" 18304;
	setAttr ".tgi[1].ni[6].x" 4218.5712890625;
	setAttr ".tgi[1].ni[6].y" -177.14285278320312;
	setAttr ".tgi[1].ni[6].nvs" 18304;
	setAttr ".tgi[1].ni[7].x" 4218.5712890625;
	setAttr ".tgi[1].ni[7].y" -481.42855834960938;
	setAttr ".tgi[1].ni[7].nvs" 18304;
	setAttr ".tgi[1].ni[8].x" 3911.428466796875;
	setAttr ".tgi[1].ni[8].y" -510;
	setAttr ".tgi[1].ni[8].nvs" 18304;
	setAttr ".tgi[1].ni[9].x" 4525.71435546875;
	setAttr ".tgi[1].ni[9].y" -310;
	setAttr ".tgi[1].ni[9].nvs" 18304;
	setAttr ".tgi[1].ni[10].x" 4525.71435546875;
	setAttr ".tgi[1].ni[10].y" -527.14288330078125;
	setAttr ".tgi[1].ni[10].nvs" 18304;
	setAttr ".tgi[1].ni[11].x" 3604.28564453125;
	setAttr ".tgi[1].ni[11].y" -345.71429443359375;
	setAttr ".tgi[1].ni[11].nvs" 18304;
	setAttr ".tgi[1].ni[12].x" 4525.71435546875;
	setAttr ".tgi[1].ni[12].y" -411.42855834960938;
	setAttr ".tgi[1].ni[12].nvs" 18304;
	setAttr ".tgi[1].ni[13].x" 4218.5712890625;
	setAttr ".tgi[1].ni[13].y" -278.57144165039062;
	setAttr ".tgi[1].ni[13].nvs" 18304;
	setAttr ".tgi[1].ni[14].x" 3911.428466796875;
	setAttr ".tgi[1].ni[14].y" -408.57144165039062;
	setAttr ".tgi[1].ni[14].nvs" 18304;
	setAttr ".tgi[1].ni[15].x" 3604.28564453125;
	setAttr ".tgi[1].ni[15].y" -244.28572082519531;
	setAttr ".tgi[1].ni[15].nvs" 18304;
	setAttr ".tgi[1].ni[16].x" 5141.4287109375;
	setAttr ".tgi[1].ni[16].y" -420;
	setAttr ".tgi[1].ni[16].nvs" 18304;
	setAttr ".tgi[1].ni[17].x" 4525.71435546875;
	setAttr ".tgi[1].ni[17].y" -208.57142639160156;
	setAttr ".tgi[1].ni[17].nvs" 18304;
	setAttr ".tgi[1].ni[18].x" 4832.85693359375;
	setAttr ".tgi[1].ni[18].y" -365.71429443359375;
	setAttr ".tgi[1].ni[18].nvs" 18304;
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
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".fs" 1;
	setAttr ".ef" 10;
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
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
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "ribbon_scale_0_MM.o" "ribbon_0_JNT.opm";
connectAttr "ribbon_scale_1_MM.o" "ribbon_1_JNT.opm";
connectAttr "ribbon_scale_2_MM.o" "ribbon_2_JNT.opm";
connectAttr "ribbon_scale_3_MM.o" "ribbon_3_JNT.opm";
connectAttr "ribbon_scale_4_MM.o" "ribbon_4_JNT.opm";
connectAttr "ribbon_scale_5_MM.o" "ribbon_5_JNT.opm";
connectAttr "ribbon_scale_6_MM.o" "ribbon_6_JNT.opm";
connectAttr "ribbon_scale_7_MM.o" "ribbon_7_JNT.opm";
connectAttr "ribbon_scale_8_MM.o" "ribbon_8_JNT.opm";
connectAttr "ribbon_scale_9_MM.o" "ribbon_9_JNT.opm";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "ribbon_0_CTL.wm" "ribbon_parentOffset_0_MM.i[0]";
connectAttr "ribbon_MOD_GRP.wim" "ribbon_parentOffset_0_MM.i[1]";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_translation_0_PM.imat";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_scaleOffset_0_PM.imat";
connectAttr "ribbon_1_CTL.wm" "ribbon_parentOffset_1_MM.i[0]";
connectAttr "ribbon_MOD_GRP.wim" "ribbon_parentOffset_1_MM.i[1]";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_translation_1_PM.imat";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_scaleOffset_1_PM.imat";
connectAttr "ribbon_2_CTL.wm" "ribbon_parentOffset_2_MM.i[0]";
connectAttr "ribbon_MOD_GRP.wim" "ribbon_parentOffset_2_MM.i[1]";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_translation_2_PM.imat";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_scaleOffset_2_PM.imat";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_0_WAM.i[0].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_0_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_0_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_0_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_0_WAM.i[0].m";
connectAttr "ribbon_up_0_WAM.o" "ribbon_upOffset_0_MM.i[1]";
connectAttr "ribbon_position_0_WAM.o" "ribbon_pointOnCurve_0_AM.imat";
connectAttr "ribbon_tangent_0_WAM.o" "ribbon_pointOnCurve_0_AM.pmat";
connectAttr "ribbon_upOffset_0_MM.o" "ribbon_pointOnCurve_0_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_0_WAM.i[0].m";
connectAttr "ribbon_scale_0_WAM.o" "ribbon_scale_0_MM.i[0]";
connectAttr "ribbon_pointOnCurve_0_AM.tmat" "ribbon_scale_0_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_1_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_1_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_1_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_1_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_1_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_1_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_1_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_1_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_1_WAM.i[2].m";
connectAttr "ribbon_up_1_WAM.o" "ribbon_upOffset_1_MM.i[1]";
connectAttr "ribbon_position_1_WAM.o" "ribbon_pointOnCurve_1_AM.imat";
connectAttr "ribbon_tangent_1_WAM.o" "ribbon_pointOnCurve_1_AM.pmat";
connectAttr "ribbon_upOffset_1_MM.o" "ribbon_pointOnCurve_1_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_1_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_1_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_1_WAM.i[2].m";
connectAttr "ribbon_scale_1_WAM.o" "ribbon_scale_1_MM.i[0]";
connectAttr "ribbon_pointOnCurve_1_AM.tmat" "ribbon_scale_1_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_2_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_2_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_2_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_2_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_2_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_2_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_2_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_2_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_2_WAM.i[2].m";
connectAttr "ribbon_up_2_WAM.o" "ribbon_upOffset_2_MM.i[1]";
connectAttr "ribbon_position_2_WAM.o" "ribbon_pointOnCurve_2_AM.imat";
connectAttr "ribbon_tangent_2_WAM.o" "ribbon_pointOnCurve_2_AM.pmat";
connectAttr "ribbon_upOffset_2_MM.o" "ribbon_pointOnCurve_2_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_2_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_2_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_2_WAM.i[2].m";
connectAttr "ribbon_scale_2_WAM.o" "ribbon_scale_2_MM.i[0]";
connectAttr "ribbon_pointOnCurve_2_AM.tmat" "ribbon_scale_2_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_3_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_3_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_3_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_3_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_3_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_3_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_3_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_3_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_3_WAM.i[2].m";
connectAttr "ribbon_up_3_WAM.o" "ribbon_upOffset_3_MM.i[1]";
connectAttr "ribbon_position_3_WAM.o" "ribbon_pointOnCurve_3_AM.imat";
connectAttr "ribbon_tangent_3_WAM.o" "ribbon_pointOnCurve_3_AM.pmat";
connectAttr "ribbon_upOffset_3_MM.o" "ribbon_pointOnCurve_3_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_3_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_3_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_3_WAM.i[2].m";
connectAttr "ribbon_scale_3_WAM.o" "ribbon_scale_3_MM.i[0]";
connectAttr "ribbon_pointOnCurve_3_AM.tmat" "ribbon_scale_3_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_4_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_4_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_4_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_4_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_4_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_4_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_4_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_4_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_4_WAM.i[2].m";
connectAttr "ribbon_up_4_WAM.o" "ribbon_upOffset_4_MM.i[1]";
connectAttr "ribbon_position_4_WAM.o" "ribbon_pointOnCurve_4_AM.imat";
connectAttr "ribbon_tangent_4_WAM.o" "ribbon_pointOnCurve_4_AM.pmat";
connectAttr "ribbon_upOffset_4_MM.o" "ribbon_pointOnCurve_4_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_4_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_4_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_4_WAM.i[2].m";
connectAttr "ribbon_scale_4_WAM.o" "ribbon_scale_4_MM.i[0]";
connectAttr "ribbon_pointOnCurve_4_AM.tmat" "ribbon_scale_4_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_5_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_5_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_5_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_5_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_5_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_5_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_5_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_5_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_5_WAM.i[2].m";
connectAttr "ribbon_up_5_WAM.o" "ribbon_upOffset_5_MM.i[1]";
connectAttr "ribbon_position_5_WAM.o" "ribbon_pointOnCurve_5_AM.imat";
connectAttr "ribbon_tangent_5_WAM.o" "ribbon_pointOnCurve_5_AM.pmat";
connectAttr "ribbon_upOffset_5_MM.o" "ribbon_pointOnCurve_5_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_5_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_5_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_5_WAM.i[2].m";
connectAttr "ribbon_scale_5_WAM.o" "ribbon_scale_5_MM.i[0]";
connectAttr "ribbon_pointOnCurve_5_AM.tmat" "ribbon_scale_5_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_6_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_6_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_6_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_6_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_6_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_6_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_6_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_6_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_6_WAM.i[2].m";
connectAttr "ribbon_up_6_WAM.o" "ribbon_upOffset_6_MM.i[1]";
connectAttr "ribbon_position_6_WAM.o" "ribbon_pointOnCurve_6_AM.imat";
connectAttr "ribbon_tangent_6_WAM.o" "ribbon_pointOnCurve_6_AM.pmat";
connectAttr "ribbon_upOffset_6_MM.o" "ribbon_pointOnCurve_6_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_6_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_6_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_6_WAM.i[2].m";
connectAttr "ribbon_scale_6_WAM.o" "ribbon_scale_6_MM.i[0]";
connectAttr "ribbon_pointOnCurve_6_AM.tmat" "ribbon_scale_6_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_7_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_7_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_7_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_7_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_7_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_7_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_7_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_7_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_7_WAM.i[2].m";
connectAttr "ribbon_up_7_WAM.o" "ribbon_upOffset_7_MM.i[1]";
connectAttr "ribbon_position_7_WAM.o" "ribbon_pointOnCurve_7_AM.imat";
connectAttr "ribbon_tangent_7_WAM.o" "ribbon_pointOnCurve_7_AM.pmat";
connectAttr "ribbon_upOffset_7_MM.o" "ribbon_pointOnCurve_7_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_7_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_7_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_7_WAM.i[2].m";
connectAttr "ribbon_scale_7_WAM.o" "ribbon_scale_7_MM.i[0]";
connectAttr "ribbon_pointOnCurve_7_AM.tmat" "ribbon_scale_7_MM.i[1]";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_position_8_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_position_8_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_8_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_8_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_8_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_8_WAM.i[2].m";
connectAttr "ribbon_parentOffset_0_MM.o" "ribbon_up_8_WAM.i[0].m";
connectAttr "ribbon_parentOffset_1_MM.o" "ribbon_up_8_WAM.i[1].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_8_WAM.i[2].m";
connectAttr "ribbon_up_8_WAM.o" "ribbon_upOffset_8_MM.i[1]";
connectAttr "ribbon_position_8_WAM.o" "ribbon_pointOnCurve_8_AM.imat";
connectAttr "ribbon_tangent_8_WAM.o" "ribbon_pointOnCurve_8_AM.pmat";
connectAttr "ribbon_upOffset_8_MM.o" "ribbon_pointOnCurve_8_AM.smat";
connectAttr "ribbon_scaleOffset_0_PM.tmat" "ribbon_scale_8_WAM.i[0].m";
connectAttr "ribbon_scaleOffset_1_PM.tmat" "ribbon_scale_8_WAM.i[1].m";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_8_WAM.i[2].m";
connectAttr "ribbon_scale_8_WAM.o" "ribbon_scale_8_MM.i[0]";
connectAttr "ribbon_pointOnCurve_8_AM.tmat" "ribbon_scale_8_MM.i[1]";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_position_9_WAM.i[2].m";
connectAttr "ribbon_translation_0_PM.tmat" "ribbon_tangent_9_WAM.i[0].m";
connectAttr "ribbon_translation_1_PM.tmat" "ribbon_tangent_9_WAM.i[1].m";
connectAttr "ribbon_translation_2_PM.tmat" "ribbon_tangent_9_WAM.i[2].m";
connectAttr "ribbon_parentOffset_2_MM.o" "ribbon_up_9_WAM.i[2].m";
connectAttr "ribbon_up_9_WAM.o" "ribbon_upOffset_9_MM.i[1]";
connectAttr "ribbon_position_9_WAM.o" "ribbon_pointOnCurve_9_AM.imat";
connectAttr "ribbon_tangent_9_WAM.o" "ribbon_pointOnCurve_9_AM.pmat";
connectAttr "ribbon_upOffset_9_MM.o" "ribbon_pointOnCurve_9_AM.smat";
connectAttr "ribbon_scaleOffset_2_PM.tmat" "ribbon_scale_9_WAM.i[2].m";
connectAttr "ribbon_scale_9_WAM.o" "ribbon_scale_9_MM.i[0]";
connectAttr "ribbon_pointOnCurve_9_AM.tmat" "ribbon_scale_9_MM.i[1]";
connectAttr "ribbon_parentOffset_2_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "ribbon_1_CTL.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "ribbon_0_CTL.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "ribbon_up_6_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "ribbon_2_CTL.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn";
connectAttr "ribbon_parentOffset_1_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "ribbon_scaleOffset_2_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "ribbon_scaleOffset_1_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "ribbon_scale_6_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "ribbon_scale_6_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "ribbon_position_6_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "ribbon_MOD_GRP.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn";
connectAttr "ribbon_translation_1_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "ribbon_translation_2_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn"
		;
connectAttr "ribbon_upOffset_6_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "ribbon_tangent_6_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn"
		;
connectAttr "ribbon_6_JNT.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn";
connectAttr "ribbon_parentOffset_0_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn"
		;
connectAttr "ribbon_scaleOffset_0_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn"
		;
connectAttr "ribbon_translation_0_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn"
		;
connectAttr "ribbon_pointOnCurve_6_AM.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[20].dn"
		;
connectAttr "ribbon_MOD_GRP.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[0].dn";
connectAttr "ribbon_2_CTL.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[1].dn";
connectAttr "ribbon_0_JNT.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[2].dn";
connectAttr "ribbon_translation_1_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[3].dn"
		;
connectAttr "ribbon_scale_0_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[4].dn"
		;
connectAttr "ribbon_parentOffset_0_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[5].dn"
		;
connectAttr "ribbon_up_0_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[6].dn";
connectAttr "ribbon_translation_2_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[7].dn"
		;
connectAttr "ribbon_parentOffset_2_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[8].dn"
		;
connectAttr "ribbon_upOffset_0_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[9].dn"
		;
connectAttr "ribbon_scaleOffset_0_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[10].dn"
		;
connectAttr "ribbon_1_CTL.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[11].dn";
connectAttr "ribbon_tangent_0_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[12].dn"
		;
connectAttr "ribbon_translation_0_PM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[13].dn"
		;
connectAttr "ribbon_parentOffset_1_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[14].dn"
		;
connectAttr "ribbon_0_CTL.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[15].dn";
connectAttr "ribbon_scale_0_MM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[16].dn"
		;
connectAttr "ribbon_position_0_WAM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[17].dn"
		;
connectAttr "ribbon_pointOnCurve_0_AM.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[18].dn"
		;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of hh_ribbon_sample.ma
