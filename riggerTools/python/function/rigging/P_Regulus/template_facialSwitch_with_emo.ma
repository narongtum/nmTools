//Maya ASCII 2023 scene
//Name: template_facialSwitch_with_emo.ma
//Last modified: Tue, Oct 15, 2024 10:28:09 AM
//Codeset: 1252
requires maya "2023";
requires -nodeType "ikSpringSolver" "ikSpringSolver" "1.0";
requires "stereoCamera" "10.0";
requires "mtoa" "5.1.2";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202205052215-234554116d";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 19045)";
fileInfo "UUID" "107899D9-485E-71A4-1177-339E12924EB2";
createNode transform -n "popUpJnt_grp";
	rename -uid "F7041D27-40AC-ADCE-F275-B58BC73EBD08";
	setAttr ".t" -type "double3" 0 128 0 ;
createNode joint -n "Sweating_pJnt" -p "popUpJnt_grp";
	rename -uid "DC87AF73-4309-E7F6-F116-76A29A442230";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
createNode parentConstraint -n "Sweating_pJnt_parCons" -p "Sweating_pJnt";
	rename -uid "6EDB7526-42D0-A04E-3D8F-7E814A5567CD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SweatingGmbl_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Sigh_pJnt" -p "popUpJnt_grp";
	rename -uid "04B0DD3F-47D3-6CD4-0AD8-CE8A435CA879";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Sigh_pJnt_parCons" -p "Sigh_pJnt";
	rename -uid "1143FD52-420C-613A-1781-2A942C47FD39";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SighGmbl_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Stunned_pJnt" -p "popUpJnt_grp";
	rename -uid "871DC0F2-4EB8-A5DD-AB48-6B997E5AAB34";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Stunned_pJnt_parCons" -p "Stunned_pJnt";
	rename -uid "07076EC4-4D54-8DA0-5095-FFB9ACFBFB5A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "StunnedGmbl_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Shock_pJnt" -p "popUpJnt_grp";
	rename -uid "66D430D8-4606-B8B2-40F4-CC8B45C110BC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Shock_pJnt_parCons" -p "Shock_pJnt";
	rename -uid "9ED58664-4F7B-00CE-4028-F7B4134703B0";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ShockGmbl_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Confused_pJnt" -p "popUpJnt_grp";
	rename -uid "49C5F23B-4BF0-3400-60E3-F6991A640C53";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Confused_pJnt_parCons" -p "Confused_pJnt";
	rename -uid "BBE360F7-4A81-5F68-00F4-FB90D8E07A59";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ConfusedGmbl_ctrlW0" -dv 1 -min 0 
		-at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Uncomfortable_pJnt" -p "popUpJnt_grp";
	rename -uid "F42061FD-416E-6753-C45C-7AA374848F8F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Uncomfortable_pJnt_parCons" -p "Uncomfortable_pJnt";
	rename -uid "55B0E4F7-4AF4-4DA9-3138-59A944BDF41E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "UncomfortableGmbl_ctrlW0" -dv 1 -min 
		0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Joy_pJnt" -p "popUpJnt_grp";
	rename -uid "DE5755D5-4E3D-278E-A35D-4E9654B750AA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Joy_pJnt_parCons" -p "Joy_pJnt";
	rename -uid "995EFD7B-49A0-116B-9324-AC9F7114CFE1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "JoyGmbl_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Love_pJnt" -p "popUpJnt_grp";
	rename -uid "BFAFDDA3-4C8E-949A-D009-498353B4E409";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Love_pJnt_parCons" -p "Love_pJnt";
	rename -uid "9DA9FC53-41D4-A1B0-A579-48AA0F5D38EC";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "LoveGmbl_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "Angry_pJnt" -p "popUpJnt_grp";
	rename -uid "B67AC350-453E-A695-C84D-209C1664CDFD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Angry_pJnt_parCons" -p "Angry_pJnt";
	rename -uid "7557095A-4F52-5671-0D8C-208FC93B2D21";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "AngryGmbl_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "ShyL_pJnt" -p "popUpJnt_grp";
	rename -uid "42CCD9FF-4AA0-0E99-FAB9-29B3C451B11D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "ShyL_pJnt_parCons" -p "ShyL_pJnt";
	rename -uid "AE27BD8D-49C4-4DCE-8DD2-22A60897BE27";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ShyLGmbl_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode joint -n "ShyR_pJnt" -p "popUpJnt_grp";
	rename -uid "EFDC21CB-4F83-9571-F94F-28885AFB1063";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "ShyR_pJnt_parCons" -p "ShyR_pJnt";
	rename -uid "3B9B28D8-4722-1474-3F7A-E1A1FC20DA8C";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ShyRGmbl_ctrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr -k on ".w0";
createNode transform -n "facialRig_grp";
	rename -uid "0B5C6260-4CB2-B158-0500-35B7F6449880";
	setAttr ".t" -type "double3" 0 127.59796533440638 0.45919690286514925 ;
createNode transform -n "facialSwitchZro_grp" -p "facialRig_grp";
	rename -uid "E4664D5B-4564-DADE-9562-5DBF9DECDCD4";
	setAttr ".t" -type "double3" 40 20 0 ;
createNode transform -n "facialSwitch_ctrl" -p "facialSwitchZro_grp";
	rename -uid "0B4924E2-41D6-C325-A326-E4AFA60C346B";
	addAttr -ci true -k true -sn "EYE" -ln "EYE" -nn "-------" -min 0 -max 0 -en "EYE" 
		-at "enum";
	addAttr -ci true -k true -sn "eyeBlink_L" -ln "eyeBlink_L" -min 0 -max 1 -at "float";
	addAttr -ci true -k true -sn "eyeBlink_R" -ln "eyeBlink_R" -min 0 -max 1 -at "float";
	addAttr -ci true -k true -sn "eyeShock_L" -ln "eyeShock_L" -min 0 -max 1 -at "float";
	addAttr -ci true -k true -sn "eyeShock_R" -ln "eyeShock_R" -min 0 -max 1 -at "float";
	addAttr -ci true -k true -sn "eyeAngry_L" -ln "eyeAngry_L" -min 0 -max 1 -at "float";
	addAttr -ci true -k true -sn "eyeAngry_R" -ln "eyeAngry_R" -min 0 -max 1 -at "float";
	addAttr -ci true -k true -sn "POPUP" -ln "POPUP" -nn "-------" -min 0 -max 0 -en 
		"POPUP" -at "enum";
	addAttr -ci true -k true -sn "Sweating" -ln "Sweating" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Sigh" -ln "Sigh" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Stunned" -ln "Stunned" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Shock" -ln "Shock" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Confused" -ln "Confused" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Uncomfortable" -ln "Uncomfortable" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Joy" -ln "Joy" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Love" -ln "Love" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "Angry" -ln "Angry" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "ShyL" -ln "ShyL" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "ShyR" -ln "ShyR" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k on ".EYE";
	setAttr -l on -k on ".POPUP";
	setAttr -k on ".Sweating" yes;
	setAttr -k on ".Sigh";
	setAttr -k on ".Stunned";
	setAttr -k on ".Shock";
	setAttr -k on ".Confused";
	setAttr -k on ".Uncomfortable";
	setAttr -k on ".Joy";
	setAttr -k on ".Love";
	setAttr -k on ".Angry";
	setAttr -k on ".ShyL";
	setAttr -k on ".ShyR";
createNode nurbsCurve -n "facialSwitch_ctrlShape" -p "facialSwitch_ctrl";
	rename -uid "07351FD5-4DB8-9E31-8623-39993C1F8883";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.6959469132232836 1.6959469132232778 -2.7272906438035283e-16
		-1.3269940019596368e-15 11.631315320387689 -1.8704581612246304e-15
		-1.6959469132232732 1.6959469132232778 -2.7272906438035278e-16
		-11.631315320387689 3.3704641873145621e-15 -5.4201197995445053e-31
		-1.6959469132232732 -1.6959469132232778 2.7272906438035283e-16
		-3.504742304159125e-15 -11.63131532038769 1.8704581612246308e-15
		1.6959469132232778 -1.695946913223279 2.7272906438035288e-16
		11.631315320387689 -6.2472021481879082e-15 1.0046267271609514e-30
		1.6959469132232836 1.6959469132232778 -2.7272906438035283e-16
		-1.3269940019596368e-15 11.631315320387689 -1.8704581612246304e-15
		-1.6959469132232732 1.6959469132232778 -2.7272906438035278e-16
		;
createNode transform -n "popUpRig_grp";
	rename -uid "DF55F8F5-4CE8-F6BC-9C02-B6A73724867A";
	setAttr ".t" -type "double3" 0 128 0 ;
createNode transform -n "SweatingZro_grp" -p "popUpRig_grp";
	rename -uid "796657D4-4E42-E9F8-560F-9F8CFE67FE5B";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "SweatingCon_grp" -p "SweatingZro_grp";
	rename -uid "B6B710EB-4361-B0C7-9DA4-7CA2C93BA16C";
createNode transform -n "Sweating_ctrl" -p "SweatingCon_grp";
	rename -uid "3A5A949E-4561-EFF1-5411-50B401A45CD8";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Sweating_ctrlShape" -p "Sweating_ctrl";
	rename -uid "762CFBCA-42CF-A755-EB3B-5AB56AD2D88C";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.8024286372923988 2.0533037468341422 1.2572859306188497e-16
		-3.3129000076438251e-16 7.5619446525653657 1.7780708148620567e-16
		-1.802428637292397 2.0533037468341435 1.2572859306188507e-16
		-2.903810006444338 -1.901718354573716 5.1524043832748845e-32
		-2.053303746834144 -4.7461077230424387 -1.2572859306188502e-16
		-8.7497462604141971e-16 -5.5966139826526344 -1.7780708148620572e-16
		2.0533037468341422 -4.7461077230424396 -1.2572859306188507e-16
		2.903810006444338 -1.9017183545737186 -9.5500530320643249e-32
		1.8024286372923988 2.0533037468341422 1.2572859306188497e-16
		-3.3129000076438251e-16 7.5619446525653657 1.7780708148620567e-16
		-1.802428637292397 2.0533037468341435 1.2572859306188507e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "SweatingGmbl_ctrl" -p "Sweating_ctrl";
	rename -uid "809D8586-46E5-F46D-D63D-C4947177FB38";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "SweatingGmbl_ctrlShape" -p "SweatingGmbl_ctrl";
	rename -uid "135EDC0F-4909-AEFE-DC66-9288160C1AB3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.539977810125609 1.5399778101256065 9.4296444796413734e-17
		-2.4846750057328689e-16 2.1778575048332534 1.3335531111465426e-16
		-1.5399778101256076 1.5399778101256076 9.4296444796413808e-17
		-2.1778575048332534 6.3108861920786327e-16 3.8643032874561634e-32
		-1.5399778101256079 -1.5399778101256074 -9.4296444796413759e-17
		-6.5623096953106483e-16 -2.1778575048332542 -1.3335531111465429e-16
		1.5399778101256065 -1.5399778101256076 -9.4296444796413808e-17
		2.1778575048332534 -1.1697315142676374e-15 -7.162539774048244e-32
		1.539977810125609 1.5399778101256065 9.4296444796413734e-17
		-2.4846750057328689e-16 2.1778575048332534 1.3335531111465426e-16
		-1.5399778101256076 1.5399778101256076 9.4296444796413808e-17
		;
createNode transform -n "SighZro_grp" -p "popUpRig_grp";
	rename -uid "4711E48E-4DC5-DE36-86A1-E582B8E176BB";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "SighCon_grp" -p "SighZro_grp";
	rename -uid "74EF7EAB-4E4A-261F-2E5F-0AAD938257DF";
createNode transform -n "Sigh_ctrl" -p "SighCon_grp";
	rename -uid "734A531E-4D9F-6BA0-8CDD-1EBAEC1D7218";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Sigh_ctrlShape" -p "Sigh_ctrl";
	rename -uid "BF06F702-4269-F4DF-9135-4F8BFB5EE31D";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.5614215412915806 3.5614215412915748 2.1807417454785801e-16
		-5.7461705164466296e-16 5.0366106450222405 3.0840345524889864e-16
		-3.5614215412915775 3.5614215412915775 2.1807417454785818e-16
		-5.0366106450222405 1.4594837588780058e-15 8.9367605685874876e-32
		-3.561421541291578 -3.5614215412915766 -2.1807417454785811e-16
		-1.5176290824346132e-15 -5.0366106450222423 -3.0840345524889874e-16
		3.5614215412915748 -3.5614215412915775 -2.1807417454785818e-16
		5.0366106450222405 -2.705173402531423e-15 -1.6564409742743311e-31
		3.5614215412915806 3.5614215412915748 2.1807417454785801e-16
		-5.7461705164466296e-16 5.0366106450222405 3.0840345524889864e-16
		-3.5614215412915775 3.5614215412915775 2.1807417454785818e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "SighGmbl_ctrl" -p "Sigh_ctrl";
	rename -uid "98229C27-49EB-7017-69C7-4DBA3D070E11";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "SighGmbl_ctrlShape" -p "SighGmbl_ctrl";
	rename -uid "C0D36961-4C5B-0C64-14EF-6586D0DB56C5";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "StunnedZro_grp" -p "popUpRig_grp";
	rename -uid "1D767687-4618-8576-C74D-7CA9944BBF47";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "StunnedCon_grp" -p "StunnedZro_grp";
	rename -uid "33A15278-45E4-89CA-ACD7-3C89F5ABDBF5";
createNode transform -n "Stunned_ctrl" -p "StunnedCon_grp";
	rename -uid "DFB47A85-4BEA-3B87-6C13-F6AA2D5165F0";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Stunned_ctrlShape" -p "Stunned_ctrl";
	rename -uid "365A6BC5-4614-805C-7268-619E5A8658B7";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		7.6061635908498921 5.1306655613688044 3.1416265786129339e-16
		-8.2780650469682396e-16 7.8442517936092919 4.4429309153862005e-16
		-9.9074252139384136 5.1306655613688079 3.1416265786129364e-16
		-10.640964049660935 2.1025657794883946e-15 1.5046941066040931e-31
		-9.9074252139384136 -7.3383613192581327 -3.1416265786129349e-16
		-2.1863312662940781e-15 -7.2558568208883454 -4.4429309153862015e-16
		7.6061635908498708 -5.1306655613688079 -3.1416265786129364e-16
		12.066448180966418 -3.897134852749111e-15 -2.1690629809519153e-31
		7.6061635908498921 5.1306655613688044 3.1416265786129339e-16
		-8.2780650469682396e-16 7.8442517936092919 4.4429309153862005e-16
		-9.9074252139384136 5.1306655613688079 3.1416265786129364e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "StunnedGmbl_ctrl" -p "Stunned_ctrl";
	rename -uid "7F60C214-4B55-2C5F-DA64-D9B2A082D86C";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "StunnedGmbl_ctrlShape" -p "StunnedGmbl_ctrl";
	rename -uid "F021BA62-449C-5DE8-96C8-DCBEB3E9CF38";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "ShockZro_grp" -p "popUpRig_grp";
	rename -uid "1396BA9C-43C2-5D71-96E0-4286B2205CB8";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "ShockCon_grp" -p "ShockZro_grp";
	rename -uid "7B58269E-4FED-4FF1-44B6-718B6C358B54";
createNode transform -n "Shock_ctrl" -p "ShockCon_grp";
	rename -uid "CAC89614-48C9-DF17-D41D-1DB8C5B2F7A8";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Shock_ctrlShape" -p "Shock_ctrl";
	rename -uid "3FA26C9C-4742-F6BD-548B-75A5DA715559";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		5.6442450337862926 7.0287086593586077 4.5888181500815834e-16
		-1.2091359104765188e-15 10.598270240248011 6.4895688631091896e-16
		-6.4080614741023396 9.4588209320069723 4.5888181500815854e-16
		-7.1322407216546999 -0.56649207367280185 2.4249502508521616e-31
		-7.4941087557269608 -7.4941087557269555 -4.5888181500815834e-16
		-3.1934656604829996e-15 -10.598270240248015 -6.4895688631091936e-16
		3.2000886059853277 -3.8871024881662493 -4.5888181500815854e-16
		7.4425633938634874 1.8935162051197891 -2.9411245452844764e-31
		5.6442450337862926 7.0287086593586077 4.5888181500815834e-16
		-1.2091359104765188e-15 10.598270240248011 6.4895688631091896e-16
		-6.4080614741023396 9.4588209320069723 4.5888181500815854e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "ShockGmbl_ctrl" -p "Shock_ctrl";
	rename -uid "ED7F8BD6-4402-4BFF-3E04-378995A4101E";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "ShockGmbl_ctrlShape" -p "ShockGmbl_ctrl";
	rename -uid "15D411DB-4B94-3E9D-BE58-24B48F8114D4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "ConfusedZro_grp" -p "popUpRig_grp";
	rename -uid "D1EE843D-4CA1-579E-F0EC-E7924A77E5C1";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "ConfusedCon_grp" -p "ConfusedZro_grp";
	rename -uid "E67F604D-423E-D601-9B27-DD8143822068";
createNode transform -n "Confused_ctrl" -p "ConfusedCon_grp";
	rename -uid "5E607386-454D-D894-6C6C-4E879FECD48D";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Confused_ctrlShape" -p "Confused_ctrl";
	rename -uid "A16CAFE7-4410-DED7-55FB-419D47B8E9A8";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.2030095481567624 7.4407002401037037 2.1807417454785801e-16
		-5.7461705164466296e-16 8.7368799595412732 3.0840345524889864e-16
		-5.5718060350498213 6.651132253691669 2.1807417454785818e-16
		-5.0366106450222405 1.4594837588780058e-15 8.9367605685874876e-32
		-5.5651752175994247 -7.757778022579128 -2.1807417454785811e-16
		-0.61483317014651706 -8.462492794792702 -3.0840345524889874e-16
		2.014693580122116 -3.604664782080091 -2.1807417454785818e-16
		6.1842760991112202 -0.32004821180112503 -1.6564409742743311e-31
		4.2030095481567624 7.4407002401037037 2.1807417454785801e-16
		-5.7461705164466296e-16 8.7368799595412732 3.0840345524889864e-16
		-5.5718060350498213 6.651132253691669 2.1807417454785818e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "ConfusedGmbl_ctrl" -p "Confused_ctrl";
	rename -uid "2EC0980B-4980-2D59-6072-6CAF2694A98C";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "ConfusedGmbl_ctrlShape" -p "ConfusedGmbl_ctrl";
	rename -uid "022F2FCC-4080-1688-0810-C9A063271058";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "UncomfortableZro_grp" -p "popUpRig_grp";
	rename -uid "648742D0-4DE3-6820-E013-028F24EA8B8A";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "UncomfortableCon_grp" -p "UncomfortableZro_grp";
	rename -uid "148D26A5-45F3-8A75-B665-7FAF80C6FDFD";
createNode transform -n "Uncomfortable_ctrl" -p "UncomfortableCon_grp";
	rename -uid "F9211DA4-4E74-3089-5981-F79F2E682663";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Uncomfortable_ctrlShape" -p "Uncomfortable_ctrl";
	rename -uid "E2AE126B-45CB-2537-9053-3C99C6B2B1F9";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.5614215412915806 3.5614215412915748 2.1807417454785801e-16
		-5.7461705164466296e-16 5.0366106450222405 3.0840345524889864e-16
		-5.4205594687587055 6.2114313859107551 2.1807417454785818e-16
		-5.6184364497314254 -1.2312100390686269 8.9367605685874876e-32
		-1.6834969810852733 -2.5383060102760564 -2.1807417454785811e-16
		1.1902242163847092 -5.4301416237523688 -3.0840345524889874e-16
		5.3679964347614995 -6.1632270988212792 -2.1807417454785818e-16
		6.5140093411235789 -1.9410546383078922 -1.6564409742743311e-31
		3.5614215412915806 3.5614215412915748 2.1807417454785801e-16
		-5.7461705164466296e-16 5.0366106450222405 3.0840345524889864e-16
		-5.4205594687587055 6.2114313859107551 2.1807417454785818e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "UncomfortableGmbl_ctrl" -p "Uncomfortable_ctrl";
	rename -uid "A065D721-4C6D-69C8-2C8B-9D84056B4A86";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "UncomfortableGmbl_ctrlShape" -p "UncomfortableGmbl_ctrl";
	rename -uid "2D300639-40C5-4AD6-3713-009F89D3C6F7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "JoyZro_grp" -p "popUpRig_grp";
	rename -uid "9E0CDD7F-4142-A05B-8533-85BC661A14EF";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "JoyCon_grp" -p "JoyZro_grp";
	rename -uid "22C0B6D4-4AB1-8866-FA54-D4A876781766";
createNode transform -n "Joy_ctrl" -p "JoyCon_grp";
	rename -uid "8364FD61-41E1-4166-723A-B4A3D107BE63";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Joy_ctrlShape" -p "Joy_ctrl";
	rename -uid "A21FC2CD-485E-CFC0-FC3E-E3A76E89D623";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		10.389090024209942 2.8604472280774278 2.1807417454785801e-16
		1.5687745299313836 7.3991452325678795 3.0840345524889864e-16
		-8.4694417470345904 8.1492204966927044 2.1807417454785818e-16
		-9.9446308507652539 4.5877989554011283 8.9367605685874876e-32
		-4.9978828801392687 -1.1401452229460287 -2.1807417454785811e-16
		1.65899179558194 -5.5367151226028772 -3.0840345524889874e-16
		8.8644325245133562 -8.7500222748049179 -2.1807417454785818e-16
		10.339621628244023 -5.1886007335133426 -1.6564409742743311e-31
		10.389090024209942 2.8604472280774278 2.1807417454785801e-16
		1.5687745299313836 7.3991452325678795 3.0840345524889864e-16
		-8.4694417470345904 8.1492204966927044 2.1807417454785818e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "JoyGmbl_ctrl" -p "Joy_ctrl";
	rename -uid "96C1100B-408D-F9DE-4E3D-E1A0BB9EBF55";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "JoyGmbl_ctrlShape" -p "JoyGmbl_ctrl";
	rename -uid "55AA553A-4027-B97E-4457-FE9AF81C63FD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "LoveZro_grp" -p "popUpRig_grp";
	rename -uid "9BC2F2CA-4AE1-C242-8159-D997533DBBDD";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "LoveCon_grp" -p "LoveZro_grp";
	rename -uid "B2BFBB4C-4442-DF88-8718-A394FF56B9C0";
createNode transform -n "Love_ctrl" -p "LoveCon_grp";
	rename -uid "9CC60FB2-46C3-CC2E-343D-43AF176BBDBD";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Love_ctrlShape" -p "Love_ctrl";
	rename -uid "1E860F8B-4B6A-0CAE-9A79-26884CA377A1";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.9533126357727681 4.3524852529850282 2.1807417454785801e-16
		0.46529065279464044 5.7531257989257556 3.0840345524889864e-16
		-5.6734806557522077 5.8170609659996568 2.1807417454785818e-16
		-6.0437462657932031 0.61040544154130461 8.9367605685874876e-32
		-2.2960035383221387 -2.3236339152411856 -2.1807417454785811e-16
		0.93741729995236511 -5.9382056745381604 -3.0840345524889874e-16
		5.7236037553628067 -4.9298335893649021 -2.1807417454785818e-16
		6.9076131984049844 -1.7951309953101342 -1.6564409742743311e-31
		4.9533126357727681 4.3524852529850282 2.1807417454785801e-16
		0.46529065279464044 5.7531257989257556 3.0840345524889864e-16
		-5.6734806557522077 5.8170609659996568 2.1807417454785818e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "LoveGmbl_ctrl" -p "Love_ctrl";
	rename -uid "DAD509AE-4343-784A-E3FE-579BF2CDC08B";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "LoveGmbl_ctrlShape" -p "LoveGmbl_ctrl";
	rename -uid "606C75C2-457D-6F1E-FA34-06A58CB09151";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "AngryZro_grp" -p "popUpRig_grp";
	rename -uid "7DDF2C82-4D97-3888-9277-18A5248DF4C8";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "AngryCon_grp" -p "AngryZro_grp";
	rename -uid "A6680020-4B94-97E9-0F27-A4AEED8423F8";
createNode transform -n "Angry_ctrl" -p "AngryCon_grp";
	rename -uid "954397A9-4CE5-1823-DB28-97B6575CB72C";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "Angry_ctrlShape" -p "Angry_ctrl";
	rename -uid "8CE8372D-4946-152C-B257-FD81D8896906";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.7286574725166926 4.7286574725166854 2.8954676189908849e-16
		-7.6294456682306711e-16 6.6873315294499793 4.0948095761890473e-16
		-4.7286574725166881 4.7286574725166881 2.8954676189908884e-16
		-6.6873315294499793 1.9378213734093316e-15 1.3481638313316787e-31
		-4.7286574725166881 -4.7286574725166872 -2.8954676189908859e-16
		-2.0150235005768284e-15 -6.6873315294499802 -4.0948095761890483e-16
		4.7286574725166854 -4.7286574725166881 -2.8954676189908884e-16
		6.6873315294499793 -3.5917788096756839e-15 -2.0377397510581629e-31
		4.7286574725166926 4.7286574725166854 2.8954676189908849e-16
		-7.6294456682306711e-16 6.6873315294499793 4.0948095761890473e-16
		-4.7286574725166881 4.7286574725166881 2.8954676189908884e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "AngryGmbl_ctrl" -p "Angry_ctrl";
	rename -uid "A614B1BF-4038-A688-1879-31A6911E812A";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "AngryGmbl_ctrlShape" -p "AngryGmbl_ctrl";
	rename -uid "7406AAB5-4B5F-8FA7-3615-CBA5391B7136";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "ShyLZro_grp" -p "popUpRig_grp";
	rename -uid "D8505C1E-4974-6496-B232-689F86BE33DF";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "ShyLCon_grp" -p "ShyLZro_grp";
	rename -uid "C9376E34-4CB1-7807-9013-9CA82E38BF1E";
createNode transform -n "ShyL_ctrl" -p "ShyLCon_grp";
	rename -uid "8351CED0-454E-F2E7-1955-38BD7EEB69A6";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "ShyL_ctrlShape" -p "ShyL_ctrl";
	rename -uid "1EDCE653-43CF-66C7-06C3-BAA4E5307A58";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.4301005617964746 1.5753900629623492 1.4880074373051155e-16
		-3.9208422924097907e-16 1.5754001287682011 2.1043602987489292e-16
		-2.4301005617964719 1.5753900629623492 1.4880074373051172e-16
		-3.4366811724230475 9.9586422479379748e-16 4.5317252160037043e-32
		-2.4301005617964724 -1.6775655565793604 -1.4880074373051165e-16
		-1.0355391079275437e-15 -1.6775756223852123 -2.1043602987489302e-16
		2.4301005617964702 -1.6775655565793604 -1.4880074373051172e-16
		3.4366811724230475 -1.8458481617608312e-15 -1.2868744675453858e-31
		2.4301005617964746 1.5753900629623492 1.4880074373051155e-16
		-3.9208422924097907e-16 1.5754001287682011 2.1043602987489292e-16
		-2.4301005617964719 1.5753900629623492 1.4880074373051172e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "ShyLGmbl_ctrl" -p "ShyL_ctrl";
	rename -uid "104BFACA-4E30-5EFC-FFEC-B49ADAA2C56F";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "ShyLGmbl_ctrlShape" -p "ShyLGmbl_ctrl";
	rename -uid "F5E3D022-4F17-2131-636F-948D61565E4A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "ShyRZro_grp" -p "popUpRig_grp";
	rename -uid "B1337C7B-4DC0-0BBB-DA5A-95B748A87A19";
	setAttr ".t" -type "double3" -9.5367431640625e-07 5.404937744140625 0 ;
createNode transform -n "ShyRCon_grp" -p "ShyRZro_grp";
	rename -uid "DCDF3A0E-495D-A9BF-74FD-C9AB2E5D3AC8";
createNode transform -n "ShyR_ctrl" -p "ShyRCon_grp";
	rename -uid "576E5133-47ED-FB95-D1FC-51BF529E7804";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
createNode nurbsCurve -n "ShyR_ctrlShape" -p "ShyR_ctrl";
	rename -uid "9AC1DBDE-4C8A-6324-B08A-93B3BC740FCB";
	addAttr -ci true -k true -sn "gimbal" -ln "gimbal" -dv 1 -min 0 -max 1 -at "double";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.8119441037424102 1.6257734572754796 1.7218191730147053e-16
		-4.5369272116439122e-16 1.6257790360574438 2.4350200264314236e-16
		-2.8119441037424076 1.6257734572754796 1.7218191730147067e-16
		-3.5352683722728964 1.1523451247493919e-15 6.0185130789657501e-32
		-2.8119441037424076 -1.6257734572754796 -1.7218191730147062e-16
		-1.1982541523215403e-15 -1.6257790360574438 -2.4350200264314241e-16
		2.8119441037424049 -1.6257734572754796 -1.7218191730147067e-16
		3.5352683722728964 -2.1358876815493056e-15 -1.4116105826459342e-31
		2.8119441037424102 1.6257734572754796 1.7218191730147053e-16
		-4.5369272116439122e-16 1.6257790360574438 2.4350200264314236e-16
		-2.8119441037424076 1.6257734572754796 1.7218191730147067e-16
		;
	setAttr -k on ".gimbal" 0;
createNode transform -n "ShyRGmbl_ctrl" -p "ShyR_ctrl";
	rename -uid "F5FC56B1-4AA1-3104-529C-DA870FD88B68";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "ShyRGmbl_ctrlShape" -p "ShyRGmbl_ctrl";
	rename -uid "65537E83-41DB-4E52-37F6-B9A19E71C062";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		-3.7774579837666806 1.0946128191585045e-15 6.7025704264406157e-32
		-2.6710661559686835 -2.6710661559686826 -1.6355563091089358e-16
		-1.13822181182596e-15 -3.7774579837666815 -2.3130259143667403e-16
		2.6710661559686812 -2.671066155968683 -1.6355563091089363e-16
		3.7774579837666806 -2.0288800518985673e-15 -1.2423307307057483e-31
		2.6710661559686857 2.6710661559686812 1.6355563091089351e-16
		-4.3096278873349722e-16 3.7774579837666806 2.3130259143667398e-16
		-2.671066155968683 2.671066155968683 1.6355563091089363e-16
		;
createNode transform -n "C000_Generic_01_PopUp";
	rename -uid "6FCEF355-4058-3B9C-376C-CE9EEA6EBCBE";
createNode transform -n "Sweating" -p "C000_Generic_01_PopUp";
	rename -uid "5EB0E9DD-4BAB-3B46-9C1F-32A7EF540C02";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 133.40495300292969 -2.9802322387695312e-08 ;
	setAttr ".sp" -type "double3" 0 133.40495300292969 -2.9802322387695312e-08 ;
createNode mesh -n "SweatingShape" -p "Sweating";
	rename -uid "97451442-4859-F32D-78ED-96B010BDAFFE";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.39271488785743713 0.53080256511427326 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "polySurfaceShape63" -p "Sweating";
	rename -uid "2578EA95-4318-B35F-AA0E-9286EFD02537";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.375 0.25 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 4 ".uvst[0].uvsp[0:3]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 4 ".pt[0:3]" -type "float3"  -10.741761 31.463142 0 -54.899288 
		-106.0434 0 -5.1272521 25.932753 0 74.360146 -78.728653 0;
	setAttr -s 4 ".vt[0:3]"  -50 -50 50 50 -50 50 -50 50 50 50 50 50;
	setAttr -s 4 ".ed[0:3]"  0 1 0 2 3 0 0 2 0 1 3 0;
	setAttr -ch 4 ".fc[0]" -type "polyFaces" 
		f 4 0 3 -2 -3
		mu 0 4 0 1 3 2;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode mesh -n "SweatingShapeOrig" -p "Sweating";
	rename -uid "C35B2D21-43DB-7FAD-E5CF-6A91B2D94C45";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "cluster1";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "vtx[0:49]";
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 70 ".uvst[0].uvsp[0:69]" -type "float2" 0.42511091 0.01114656
		 0.42654377 0.014756709 0.42239967 0.01397033 0.42459857 0.045732379 0.42210478 0.05832082
		 0.41958788 0.045647442 0.42693594 0.033181489 0.42577758 0.039720178 0.41842714 0.039542973
		 0.41740617 0.032804519 0.42768303 0.026638001 0.41679168 0.02599445 0.41710204 0.019635081
		 0.42756402 0.020241261 0.41825482 0.014355242 0.41988721 0.010940507 0.42258745 0.0084144473
		 0.42773688 0.08648777 0.41459006 0.025621921 0.41509792 0.033370554 0.42661583 0.09385103
		 0.42767218 0.079630196 0.41503441 0.01836203 0.41617209 0.040682554 0.42536217 0.10126701
		 0.42635411 0.073693931 0.41647685 0.012083858 0.42450517 0.070189506 0.41839629 0.0080174878
		 0.42204854 0.11879373 0.41990921 0.059898615 0.42678162 0.047224343 0.42002612 0.10860485
		 0.42402324 0.10849059 0.41738939 0.047105849 0.42800677 0.041019976 0.41874319 0.10191208
		 0.42181611 0.068971246 0.42458549 0.0045004413 0.4191609 0.070333883 0.42683169 0.008578822
		 0.41754961 0.073918961 0.42847306 0.012806915 0.41628107 0.079921216 0.42966044 0.019313723
		 0.41627097 0.086855166 0.42987183 0.026574373 0.41733405 0.094134048 0.42916763 0.033909976
		 0.42194426 0.073059142 0.42999759 0.034179717 0.42874724 0.041879833 0.43069145 0.026550829
		 0.41667247 0.048082232 0.4153465 0.041102886 0.43047437 0.018945009 0.4291763 0.01212997
		 0.42750463 0.007614322 0.41986993 0.0035537258 0.41775313 0.0069529936 0.42750189
		 0.04817754 0.4256793 0.057540715 0.4158186 0.011273116 0.41423982 0.017850503 0.41426894
		 0.033555746 0.4137758 0.025480658 0.42064273 0.0045508519 0.42430556 0.059888124
		 0.4254182 0.003671661 0.41853023 0.057549238;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 50 ".vt[0:49]"  0.012737274 129.75489807 0.53090668 -1.021112442 129.091567993 -0.53090674
		 0.012737274 129.75489807 -0.53090668 -1.63475978 129.75489807 -0.53090668 0.84600264 135.64848328 -0.53090668
		 -0.93484306 135.64845276 -0.53090668 -0.066417694 137.95994568 -0.53090668 1.72259712 133.29978943 -0.53090668
		 -1.77780914 133.29832458 -0.53090668 1.2862072 134.53211975 -0.53090668 -1.34453392 134.53083801 -0.53090668
		 2.12403107 132.046127319 -0.53090668 -2.12403107 132.046768188 -0.53090668 -2.10287285 130.81962585 -0.53090668
		 2.11849213 130.82795715 -0.53090668 1.66023445 129.75489807 -0.53090668 0.98004723 129.091567993 -0.53090668
		 -0.020095825 128.84996033 -0.53090674 1.90463245 132.012374878 0.53090668 2.12403107 132.046127319 0.31166381
		 1.51481628 133.2297821 0.53090668 1.72259712 133.29978943 0.31166381 1.89945424 130.87330627 0.53090668
		 2.11849213 130.82795715 0.31166381 1.4758091 129.88127136 0.53090668 1.66023445 129.75489807 0.31166381
		 -0.06136322 137.35002136 0.53090668 -0.066417694 137.95994568 0.31166381 -0.70880318 135.64845276 0.53090668
		 -0.93484306 135.64845276 0.30486798 0.87006378 129.2905426 0.53090668 0.98004723 129.091567993 0.31166381
		 -0.020116806 129.075454712 0.53090668 -0.020095825 128.84996033 0.31166381 -0.90520668 129.28910828 0.53090668
		 -1.021112442 129.091567993 0.31166381 -1.44885635 129.87678528 0.53090668 -1.63475978 129.75489807 0.31166381
		 -1.8844223 130.86747742 0.53090668 -2.10287285 130.81962585 0.31166381 1.080831528 134.45530701 0.53090668
		 1.2862072 134.53211975 0.31166381 -1.90427577 132.018875122 0.53090668 -2.12403107 132.046768188 0.31166381
		 -1.56849468 133.23265076 0.53090668 -1.77780914 133.29832458 0.31166381 0.61897469 135.64848328 0.53090668
		 0.84600264 135.64848328 0.3038792 -1.11898041 134.53096008 0.53090668 -1.34453392 134.53083801 0.30535901;
	setAttr -s 104 ".ed[0:103]"  1 2 1 2 3 1 1 3 1 4 5 1 4 6 1 6 5 1 7 8 1
		 7 9 1 9 10 1 10 8 1 11 12 1 11 7 1 12 8 1 13 12 1 14 13 1 11 14 1 2 13 1 3 13 1 9 4 1
		 5 10 1 15 2 1 2 16 1 15 16 1 2 14 1 14 15 1 17 2 1 17 1 1 16 17 1 18 19 1 19 21 1
		 21 20 1 20 18 1 18 22 1 22 23 1 23 19 1 21 41 1 41 40 1 40 20 1 22 24 1 24 25 1 25 23 1
		 24 30 1 30 31 1 31 25 1 26 27 1 27 29 1 29 28 1 28 26 1 26 46 1 46 47 1 47 27 1 29 49 1
		 49 48 1 48 28 1 30 32 1 32 33 1 33 31 1 32 34 1 34 35 1 35 33 1 34 36 1 36 37 1 37 35 1
		 36 38 1 38 39 1 39 37 1 38 42 1 42 43 1 43 39 1 41 47 1 46 40 1 42 44 1 44 45 1 45 43 1
		 44 48 1 49 45 1 34 0 1 0 36 1 28 46 1 44 20 1 40 48 1 42 18 1 38 22 1 0 38 1 24 0 1
		 0 30 1 22 0 1 32 0 1 37 3 1 1 35 1 47 4 1 6 27 1 5 29 1 21 7 1 9 41 1 49 10 1 8 45 1
		 19 11 1 12 43 1 13 39 1 23 14 1 31 16 1 15 25 1 17 33 1;
	setAttr -s 56 -ch 208 ".fc[0:55]" -type "polyFaces" 
		f 3 2 -2 -1
		mu 0 3 0 1 2
		f 3 -6 -5 3
		mu 0 3 3 4 5
		f 4 -10 -9 -8 6
		mu 0 4 6 7 8 9
		f 4 12 -7 -12 10
		mu 0 4 10 6 9 11
		f 4 -11 15 14 13
		mu 0 4 10 11 12 13
		f 3 1 17 -17
		mu 0 3 2 1 13
		f 4 -20 -4 -19 8
		mu 0 4 7 3 5 8
		f 3 22 -22 -21
		mu 0 3 14 15 2
		f 3 24 20 23
		mu 0 3 12 14 2
		f 3 -24 16 -15
		mu 0 3 12 2 13
		f 3 26 0 -26
		mu 0 3 16 0 2
		f 3 27 25 21
		mu 0 3 15 16 2
		f 4 28 29 30 31
		mu 0 4 65 18 19 64
		f 4 -29 32 33 34
		mu 0 4 18 65 63 22
		f 4 -31 35 36 37
		mu 0 4 64 19 23 54
		f 4 -34 38 39 40
		mu 0 4 22 63 62 26
		f 4 -40 41 42 43
		mu 0 4 26 62 59 28
		f 4 44 45 46 47
		mu 0 4 61 67 31 60
		f 4 -45 48 49 50
		mu 0 4 30 69 53 34
		f 4 -47 51 52 53
		mu 0 4 60 31 35 51
		f 4 -43 54 55 56
		mu 0 4 28 59 58 66
		f 4 -56 57 58 59
		mu 0 4 38 68 57 40
		f 4 -59 60 61 62
		mu 0 4 40 57 56 42
		f 4 -62 63 64 65
		mu 0 4 42 56 55 44
		f 4 -65 66 67 68
		mu 0 4 44 55 52 46
		f 4 -37 69 -50 70
		mu 0 4 54 23 34 53
		f 4 -68 71 72 73
		mu 0 4 46 52 50 48
		f 4 -73 74 -53 75
		mu 0 4 48 50 51 35
		f 3 76 77 -61
		mu 0 3 39 49 41
		f 3 78 -49 -48
		mu 0 3 32 33 29
		f 4 79 -38 80 -75
		mu 0 4 47 20 24 36
		f 4 81 -32 -80 -72
		mu 0 4 45 17 20 47
		f 4 -67 82 -33 -82
		mu 0 4 45 43 21 17
		f 3 83 -64 -78
		mu 0 3 49 43 41
		f 4 -81 -71 -79 -54
		mu 0 4 36 24 33 32
		f 3 84 85 -42
		mu 0 3 25 49 27
		f 3 86 -85 -39
		mu 0 3 21 49 25
		f 3 -83 -84 -87
		mu 0 3 21 43 49
		f 3 87 -77 -58
		mu 0 3 37 49 39
		f 3 -86 -88 -55
		mu 0 3 27 49 37
		f 4 88 -3 89 -63
		mu 0 4 42 1 0 40
		f 4 90 4 91 -51
		mu 0 4 34 5 4 30
		f 4 -92 5 92 -46
		mu 0 4 67 4 3 31
		f 4 93 7 94 -36
		mu 0 4 19 9 8 23
		f 4 95 9 96 -76
		mu 0 4 35 7 6 48
		f 4 97 11 -94 -30
		mu 0 4 18 11 9 19
		f 4 -97 -13 98 -74
		mu 0 4 48 6 10 46
		f 4 -99 -14 99 -69
		mu 0 4 46 10 13 44
		f 4 100 -16 -98 -35
		mu 0 4 22 12 11 18
		f 4 -100 -18 -89 -66
		mu 0 4 44 13 1 42
		f 4 -95 18 -91 -70
		mu 0 4 23 8 5 34
		f 4 -93 19 -96 -52
		mu 0 4 31 3 7 35
		f 4 101 -23 102 -44
		mu 0 4 28 15 14 26
		f 4 -103 -25 -101 -41
		mu 0 4 26 14 12 22
		f 4 -90 -27 103 -60
		mu 0 4 40 0 16 38
		f 4 -104 -28 -102 -57
		mu 0 4 66 16 15 28;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Sigh" -p "C000_Generic_01_PopUp";
	rename -uid "0EF66C16-48C8-443B-120F-578EB5B7D67B";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" -2.384185791015625e-07 133.40494537353516 0 ;
	setAttr ".sp" -type "double3" -2.384185791015625e-07 133.40494537353516 0 ;
createNode mesh -n "SighShape" -p "Sigh";
	rename -uid "B1DB368C-45FE-82B2-26C6-EDB3B8056491";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.71842053532600403 0.065205838531255722 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "SighShapeOrig" -p "Sigh";
	rename -uid "666841CF-44F6-1C83-47CB-1484220984C3";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "cluster2";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "vtx[0:55]";
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 78 ".uvst[0].uvsp[0:77]" -type "float2" 0.35805768 0.02107206
		 0.35828942 0.013662562 0.36447346 0.014312044 0.36366165 0.02344346 0.35907608 0.034507811
		 0.36632413 0.034354031 0.36645454 0.039789796 0.35591695 0.023642868 0.35129333 0.037294865
		 0.35184306 0.032349974 0.35351548 0.027636826 0.36515996 0.0278382 0.35176426 0.041991115
		 0.35317147 0.046246648 0.35539573 0.049499452 0.35771042 0.050926924 0.36037475 0.051048994
		 0.36335385 0.048876226 0.36551175 0.044708133 0.34875798 0.11382508 0.35829562 0.010688648
		 0.35618287 0.019768089 0.35287014 0.10512757 0.35557318 0.12119955 0.36568815 0.014213324
		 0.35612494 0.10897189 0.36567849 0.022921801 0.35476038 0.022392958 0.3501713 0.099779963
		 0.3602111 0.11150646 0.36649784 0.027836084 0.36148071 0.071996711 0.35471541 0.052087426
		 0.35744163 0.053856194 0.36479011 0.075511843 0.35723048 0.070947044 0.35211307 0.048256934
		 0.36056 0.053922117 0.36779007 0.081182197 0.3645584 0.11009246 0.36770767 0.034693897
		 0.36402589 0.051428318 0.36971211 0.090241075 0.36772603 0.1061523 0.36773807 0.040852189
		 0.36956769 0.099449158 0.36657935 0.046575725 0.35228154 0.026487172 0.34874511 0.09220323
		 0.35335416 0.072874069 0.3504594 0.043181956 0.34870842 0.084031895 0.35049251 0.031791866
		 0.34989285 0.037581086 0.35040146 0.077320457 0.35868809 0.091592252 0.34978798 0.043786347
		 0.34916723 0.037715733 0.34975457 0.03148973 0.35162166 0.025904208 0.35159147 0.049242258
		 0.35407111 0.021882296 0.36712927 0.04753226 0.36437693 0.052720726 0.36843553 0.041415989
		 0.3684119 0.034869373 0.36068016 0.055382609 0.36721951 0.027961314 0.35732031 0.055297256
		 0.35434932 0.053449631 0.36641142 0.023041815 0.35545021 0.019407645 0.3639091 0.0097211152
		 0.35633701 0.01298352 0.35711935 0.012491729 0.36460602 0.011339359 0.36635318 0.015378058
		 0.35895926 0.0092121288;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 56 ".vt[0:55]"  -0.62212753 133.11489868 0.45704123 0.98413944 135.76193237 -0.4570412
		 2.26208305 134.41799927 -0.4570412 4.19207525 135.062759399 -0.4570412 2.079847336 137.43092346 -0.4570412
		 -0.62212753 133.11489868 -0.4570412 2.94146729 131.93634033 -0.45704123 2.5251255 130.69651794 -0.4570412
		 0.10976219 136.30725098 -0.4570412 -3.65867329 135.32165527 -0.4570412 -2.64854932 136.171875 -0.45704123
		 -1.27222157 136.48460388 -0.45704123 2.83353806 133.44969177 -0.45704123 -4.17667103 134.1394043 -0.4570412
		 -4.19207573 132.76504517 -0.4570412 -3.68347836 131.39422607 -0.4570412 -2.83990192 130.43359375 -0.4570412
		 -1.66454589 129.66152954 -0.4570412 -0.0076503754 129.37896729 -0.45704123 1.52526188 129.79293823 -0.45704123
		 2.10950756 137.029205322 0.45704123 2.079847336 137.43092346 0.21177725 3.76117802 135.17741394 0.45704123
		 4.19207525 135.062759399 0.21177725 1.057664871 135.42703247 0.45704123 0.98413944 135.76193237 0.21177725
		 1.89672005 134.55453491 0.45704123 2.26208305 134.41799927 0.21177725 -3.46928978 131.52201843 0.45704123
		 -3.68347836 131.39422607 0.21177725 -2.67750931 130.62037659 0.45704123 -2.83990192 130.43359375 0.21177725
		 2.5929985 133.37471008 0.45704123 2.83353806 133.44969177 0.21177725 -1.57275677 129.89466858 0.45704123
		 -1.66454589 129.66152954 0.21177725 2.31305504 130.83547974 0.45704123 2.5251255 130.69651794 0.21177725
		 1.40448856 130.014389038 0.45704123 1.52526188 129.79293823 0.21177725 0.025417328 136.07081604 0.45704123
		 0.10976219 136.30725098 0.21177725 -3.94631767 132.80773926 0.45704123 -4.19207573 132.76504517 0.21177725
		 -2.53615379 135.94590759 0.45704123 -2.64854932 136.171875 0.21177725 -3.45697951 135.17082214 0.45704123
		 -3.65867329 135.32165527 0.21177725 -1.26029587 136.23582458 0.45704123 -1.27222157 136.48460388 0.21177725
		 -3.93198013 134.086746216 0.45704123 -4.17667103 134.1394043 0.21177725 2.69333172 131.96786499 0.45704123
		 2.94146729 131.93634033 0.21177725 -0.019555092 129.62980652 0.45704123 -0.0076503754 129.37896729 0.21177725;
	setAttr -s 124 ".ed[0:123]"  1 2 1 2 3 1 4 3 1 1 4 1 1 5 1 2 5 1 6 5 1
		 5 7 1 6 7 1 1 8 1 8 5 1 9 5 1 5 10 1 10 9 1 8 11 1 11 5 1 12 5 1 2 12 1 12 6 1 5 13 1
		 13 9 1 5 14 1 14 13 1 5 15 1 15 14 1 15 16 1 5 16 1 16 17 1 5 17 1 17 18 1 5 18 1
		 5 19 1 18 19 1 7 19 1 11 10 1 20 21 1 21 25 1 25 24 1 24 20 1 20 22 1 22 23 1 23 21 1
		 22 26 1 26 27 1 27 23 1 25 41 1 41 40 1 40 24 1 26 32 1 32 33 1 33 27 1 28 29 1 29 31 1
		 31 30 1 30 28 1 28 42 1 42 43 1 43 29 1 31 35 1 35 34 1 34 30 1 32 52 1 52 53 1 53 33 1
		 35 55 1 55 54 1 54 34 1 36 37 1 37 53 1 52 36 1 36 38 1 38 39 1 39 37 1 38 54 1 55 39 1
		 41 49 1 49 48 1 48 40 1 42 50 1 50 51 1 51 43 1 44 45 1 45 47 1 47 46 1 46 44 1 44 48 1
		 49 45 1 47 51 1 50 46 1 24 26 1 24 0 1 0 26 1 52 0 1 0 36 1 40 0 1 46 0 1 0 44 1
		 48 0 1 0 32 1 50 0 1 42 0 1 28 0 1 30 0 1 34 0 1 54 0 1 38 0 1 27 2 1 3 23 1 4 21 1
		 1 25 1 37 7 1 6 53 1 8 41 1 45 10 1 9 47 1 11 49 1 33 12 1 13 51 1 14 43 1 15 29 1
		 16 31 1 17 35 1 18 55 1 19 39 1;
	setAttr -s 70 -ch 248 ".fc[0:69]" -type "polyFaces" 
		f 4 3 2 -2 -1
		mu 0 4 0 1 2 3
		f 3 5 -5 0
		mu 0 3 3 4 0
		f 3 8 -8 -7
		mu 0 3 5 6 4
		f 3 -11 -10 4
		mu 0 3 4 7 0
		f 3 -14 -13 -12
		mu 0 3 8 9 4
		f 3 -16 -15 10
		mu 0 3 4 10 7
		f 3 17 16 -6
		mu 0 3 3 11 4
		f 3 18 6 -17
		mu 0 3 11 5 4
		f 3 20 11 19
		mu 0 3 12 8 4
		f 3 22 -20 21
		mu 0 3 13 12 4
		f 3 24 -22 23
		mu 0 3 14 13 4
		f 3 26 -26 -24
		mu 0 3 4 15 14
		f 3 28 -28 -27
		mu 0 3 4 16 15
		f 3 30 -30 -29
		mu 0 3 4 17 16
		f 3 -33 -31 31
		mu 0 3 18 17 4
		f 3 33 -32 7
		mu 0 3 6 18 4
		f 3 -35 15 12
		mu 0 3 9 10 4
		f 4 35 36 37 38
		mu 0 4 73 74 21 71
		f 4 -36 39 40 41
		mu 0 4 20 77 72 75
		f 4 -41 42 43 44
		mu 0 4 24 76 70 26
		f 4 -38 45 46 47
		mu 0 4 71 21 27 61
		f 4 -44 48 49 50
		mu 0 4 26 70 67 30
		f 4 51 52 53 54
		mu 0 4 69 32 33 68
		f 4 -52 55 56 57
		mu 0 4 32 69 60 36
		f 4 -54 58 59 60
		mu 0 4 68 33 37 66
		f 4 -50 61 62 63
		mu 0 4 30 67 65 40
		f 4 -60 64 65 66
		mu 0 4 66 37 41 63
		f 4 67 68 -63 69
		mu 0 4 64 44 40 65
		f 4 -68 70 71 72
		mu 0 4 44 64 62 46
		f 4 -72 73 -66 74
		mu 0 4 46 62 63 41
		f 4 -47 75 76 77
		mu 0 4 61 27 47 59
		f 4 -57 78 79 80
		mu 0 4 36 60 56 50
		f 4 81 82 83 84
		mu 0 4 58 52 53 57
		f 4 -82 85 -77 86
		mu 0 4 52 58 59 47
		f 4 -84 87 -80 88
		mu 0 4 57 53 50 56
		f 4 89 -43 -40 -39
		mu 0 4 22 25 23 19
		f 3 -90 90 91
		mu 0 3 25 22 55
		f 3 92 93 -70
		mu 0 3 39 55 43
		f 3 -91 -48 94
		mu 0 3 55 22 28
		f 3 95 96 -85
		mu 0 3 54 55 51
		f 3 -95 -78 97
		mu 0 3 55 28 48
		f 3 -92 98 -49
		mu 0 3 25 55 29
		f 3 -99 -93 -62
		mu 0 3 29 55 39
		f 3 99 -96 -89
		mu 0 3 49 55 54
		f 3 100 -100 -79
		mu 0 3 35 55 49
		f 3 101 -101 -56
		mu 0 3 31 55 35
		f 3 -102 -55 102
		mu 0 3 55 31 34
		f 3 -103 -61 103
		mu 0 3 55 34 38
		f 3 -104 -67 104
		mu 0 3 55 38 42
		f 3 105 -105 -74
		mu 0 3 45 55 42
		f 3 -94 -106 -71
		mu 0 3 43 55 45
		f 3 -97 -98 -86
		mu 0 3 51 55 48
		f 4 106 1 107 -45
		mu 0 4 26 3 2 24
		f 4 -108 -3 108 -42
		mu 0 4 75 2 1 20
		f 4 -109 -4 109 -37
		mu 0 4 74 1 0 21
		f 4 110 -9 111 -69
		mu 0 4 44 6 5 40
		f 4 -110 9 112 -46
		mu 0 4 21 0 7 27
		f 4 113 13 114 -83
		mu 0 4 52 9 8 53
		f 4 -113 14 115 -76
		mu 0 4 27 7 10 47
		f 4 116 -18 -107 -51
		mu 0 4 30 11 3 26
		f 4 -112 -19 -117 -64
		mu 0 4 40 5 11 30
		f 4 -115 -21 117 -88
		mu 0 4 53 8 12 50
		f 4 -118 -23 118 -81
		mu 0 4 50 12 13 36
		f 4 -119 -25 119 -58
		mu 0 4 36 13 14 32
		f 4 -120 25 120 -53
		mu 0 4 32 14 15 33
		f 4 -121 27 121 -59
		mu 0 4 33 15 16 37
		f 4 -122 29 122 -65
		mu 0 4 37 16 17 41
		f 4 -123 32 123 -75
		mu 0 4 41 17 18 46
		f 4 -124 -34 -111 -73
		mu 0 4 46 18 6 44
		f 4 -116 34 -114 -87
		mu 0 4 47 10 9 52;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Stunned" -p "C000_Generic_01_PopUp";
	rename -uid "CACBD6C4-43C6-42F4-5993-A2879A9DF49B";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 133.4049186706543 0 ;
	setAttr ".sp" -type "double3" 0 133.4049186706543 0 ;
createNode mesh -n "StunnedShape" -p "Stunned";
	rename -uid "2CDB469A-46E3-29C8-FA73-4B80105C442D";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.72156170010566711 0.062456253916025162 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dr" 1;
	setAttr ".vcs" 2;
createNode mesh -n "StunnedShapeOrig" -p "Stunned";
	rename -uid "21A02E49-490D-9029-04B4-8C89FE16FE86";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "cluster3";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 1 "vtx[0:111]";
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 182 ".uvst[0].uvsp[0:181]" -type "float2" 0.35485223 0.016353309
		 0.35444853 0.013902083 0.35545355 0.007425651 0.3569369 0.0086096153 0.35394683 0.010254517
		 0.35346892 0.0054512396 0.35993633 0.032006383 0.35432908 0.046980321 0.35359049
		 0.043886721 0.36104622 0.055513442 0.35979238 0.055938363 0.36790296 0.026563793
		 0.3670893 0.012088154 0.35359645 0.031113267 0.35667711 0.052816272 0.35876411 0.05558598
		 0.36710948 0.0449121 0.36758757 0.042706311 0.36182806 0.0080395639 0.3648968 0.0090422481
		 0.36619744 0.0101059 0.36086419 0.034582034 0.3604508 0.027840167 0.35984546 0.028343648
		 0.36019829 0.034383371 0.36004421 0.028013751 0.36070296 0.034432989 0.36133996 0.034241568
		 0.36069754 0.027687535 0.35938269 0.02927199 0.35962096 0.033690229 0.36171222 0.028338343
		 0.36110628 0.02783832 0.36151746 0.034255818 0.36205855 0.033454463 0.36240515 0.032299981
		 0.36308295 0.10662049 0.36003917 0.10784042 0.35914364 0.097239345 0.36189184 0.033577185
		 0.3613635 0.027886137 0.35915658 0.029969558 0.35955963 0.033356767 0.3600778 0.034122299
		 0.35950312 0.028815106 0.35898057 0.095932841 0.3582111 0.08414495 0.36227462 0.032540958
		 0.36194071 0.028579369 0.36141354 0.083182603 0.36226463 0.094292969 0.35811538 0.082870901
		 0.35827062 0.081620619 0.36078092 0.031134788 0.35865346 0.080584385 0.35920537 0.079920001
		 0.35984236 0.079728559 0.36046749 0.080039248 0.3609857 0.08080475 0.36131781 0.081908584
		 0.36078092 0.031134754 0.36242777 0.095599473 0.36078081 0.031134799 0.36333472 0.10783106
		 0.36333561 0.10914207 0.36308563 0.11035401 0.36262274 0.11128241 0.36201751 0.11178589
		 0.36136204 0.11178768 0.36075604 0.11128771 0.36029178 0.11036205 0.36004013 0.10915148
		 0.35389474 0.070586286 0.36800125 0.011310145 0.36692688 0.0089047849 0.35483992
		 0.068673998 0.35297528 0.088232696 0.3689796 0.026573628 0.35276535 0.10704225 0.36854425
		 0.04344815 0.36486268 0.072218925 0.35720587 0.0062848441 0.35578728 0.0054009259
		 0.36649522 0.070484363 0.35979199 0.068541966 0.36211529 0.0060822368 0.35636264
		 0.068296388 0.36543468 0.0072591864 0.36324942 0.12078184 0.35855874 0.057515323
		 0.35986373 0.057899475 0.36218256 0.12145364 0.3653582 0.11687338 0.35605228 0.054493845
		 0.36145875 0.057342291 0.36080992 0.12128007 0.35329491 0.10950333 0.36791149 0.046225309
		 0.36613747 0.078742079 0.353697 0.016744874 0.35257629 0.031279385 0.36771366 0.093391567
		 0.36710268 0.076331921 0.35348469 0.014344908 0.3526504 0.04448092 0.36846402 0.10675198
		 0.35345265 0.048115492 0.3677111 0.11001152 0.35385692 0.0037428364 0.35206872 0.0076393373
		 0.36769059 0.072284035 0.35296717 0.010735437 0.3524791 0.010994136 0.36742383 0.068297483
		 0.35299435 0.014477894 0.35591054 0.0044109598 0.3682588 0.046932817 0.3617219 0.058176517
		 0.35574549 0.05529815 0.35304242 0.04868573 0.35217607 0.044713676 0.35207081 0.031396002
		 0.3531971 0.016659565 0.36901554 0.043736994 0.35991046 0.058810711 0.35842597 0.058482111
		 0.36568278 0.0064078905 0.3672953 0.0083282441 0.36225751 0.0051157698 0.35728711
		 0.0052884743 0.36949298 0.026580095 0.36846444 0.011030957 0.35240525 0.0058901459
		 0.35476351 0.003458865 0.3620128 0.10519475 0.36135733 0.1051966 0.36075199 0.10570008
		 0.36028922 0.10662842 0.35913265 0.030483991 0.3591336 0.031795055 0.35938525 0.033005625
		 0.35984951 0.033931285 0.36045551 0.034431249 0.36111099 0.034429461 0.36171621 0.03392598
		 0.3621791 0.032997578 0.36242908 0.031785637 0.36242819 0.030474633 0.36217642 0.029264063
		 0.36261874 0.10569477 0.36012161 0.099014729 0.36078751 0.099213392 0.36144078 0.098887175
		 0.36198187 0.098085821 0.36232847 0.096931338 0.36250445 0.030968115 0.36234131 0.029661611
		 0.36186403 0.093210727 0.36128682 0.092517495 0.36062086 0.092318892 0.35996753 0.092645109
		 0.35942644 0.093446463 0.3590799 0.094600916 0.35905725 0.031301484 0.35922033 0.032607988
		 0.35954428 0.098321587 0.35922751 0.032252979 0.35854322 0.085248739 0.35906139 0.086014271
		 0.35968655 0.08632496 0.36032355 0.08613354 0.36087543 0.085469157 0.36125821 0.08443293
		 0.36242995 0.031290632 0.36233422 0.030016612 0.3620021 0.028912779 0.3614839 0.028147276
		 0.36085877 0.027836587 0.36022177 0.02802803 0.35966986 0.028692413 0.35928702 0.029728647
		 0.35913178 0.030978929;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 112 ".vt[0:111]"  -3.88196731 132.50445557 0.46397027 4.99817657 134.38381958 0.46397027
		 4.28346634 132.67907715 0.46397027 1.28124237 132.91165161 0.46397027 3.2873404 133.68374634 0.46397027
		 -0.366889 134.13934326 0.46397027 -2.41784573 133.57965088 0.46397027 -0.55957317 133.37683105 0.46397027
		 -2.8632021 134.18612671 0.46397027 3.57732654 132.97512817 0.46397027 0.6058321 132.50875854 0.46397027
		 3.58337688 134.38989258 0.46397027 4.29203987 134.67987061 0.46397027 4.99211216 132.96905518 0.46397027
		 -3.13822365 132.39056396 0.46397027 -4.21339989 133.85467529 0.46397027 -4.32731724 133.1109314 0.46397027
		 -3.6069479 134.30001831 0.46397027 5.28815746 133.67520142 0.46397027 1.071013451 134.34957886 0.46397027
		 0.30852318 134.54223633 0.46397027 1.47392273 133.67416382 0.46397027 -0.15665531 132.70144653 0.46397027
		 -2.53176188 132.83590698 0.46397027 0.70892811 134.52172852 0.46397027 1.33963776 134.0519104 0.46397027
		 1.45341969 133.27374268 0.46397027 0.98361021 132.64303589 0.46397027 0.20542718 132.52926636 0.46397027
		 -0.42528823 132.99905396 0.46397027 -0.53906631 133.7772522 0.46397027 -0.069257736 134.40795898 0.46397027
		 -3.22374082 134.31704712 0.46397027 -2.58020115 133.92715454 0.46397027 -2.40083504 133.19644165 0.46397027
		 -2.79069614 132.55291748 0.46397027 -3.52142167 132.37356567 0.46397027 -4.16496181 132.76342773 0.46397027
		 -4.34431934 133.49411011 0.46397027 -3.95446682 134.13769531 0.46397027 3.3651247 134.066314697 0.46397027
		 3.90886283 134.6053772 0.46397027 4.67455387 134.60211182 0.46397027 5.21364212 134.058349609 0.46397027
		 5.21036816 133.29269409 0.46397027 4.66662788 132.75360107 0.46397027 3.90095139 132.75689697 0.46397027
		 3.36184859 133.30059814 0.46397027 -3.37258124 133.3453064 0.46397027 0.45717809 133.52548218 0.46397027
		 4.28774738 133.67950439 0.46397027 -6.20690632 129.71508789 -0.46397027 -3.78527331 129.13412476 -0.46397024
		 -6.48249149 128.80761719 -0.46397024 -4.33617115 128.48269653 -0.46397027 -5.53885841 127.86237335 -0.46397027
		 -7.32245541 127.7543869 -0.46397024 0.45745182 133.5166626 -0.46397024 4.64176464 129.38650513 -0.46397027
		 5.57853699 130.064178467 -0.46397024 7.34692287 131.865448 -0.46397024 8.37491703 134.14990234 -0.46397024
		 8.13683224 135.057159424 -0.46397024 3.73295569 138.86291504 -0.46397024 -8.37491703 135.46734619 -0.46397024
		 -8.30372334 134.45394897 -0.46397027 -7.82639027 132.40872192 -0.46397027 -7.8302412 136.26754761 -0.46397024
		 -2.68976974 137.84259033 -0.46397024 0.57356453 129.053649902 -0.46397027 8.28982639 133.39013672 -0.46397024
		 2.84244347 139.055450439 -0.46397024 -7.67949581 136.063049316 0.46397027 -7.8302412 136.26754761 0.22428937
		 -2.62889671 137.6105957 0.46397027 -2.68976974 137.84259033 0.22428937 -5.94662476 129.74734497 0.46397027
		 -6.20690632 129.71508789 0.22428937 -7.6015501 132.49990845 0.46397027 -7.82639027 132.40872192 0.22428937
		 -8.065970421 134.48980713 0.46397027 -8.30372334 134.45394897 0.22428937 8.0576334 133.47036743 0.46397027
		 8.28982639 133.39013672 0.22428937 8.13175869 134.13226318 0.46397027 8.37491703 134.14990234 0.22428937
		 2.84279919 138.81015015 0.46397027 2.84244347 139.055450439 0.22428937 -3.8947382 129.37588501 0.46397027
		 -3.78527331 129.13412476 0.22428937 0.56598568 129.29351807 0.46397027 0.57356453 129.053649902 0.22428937
		 4.55550957 129.61993408 0.46397027 4.64176464 129.38650513 0.22428937 5.42166805 130.246521 0.46397027
		 5.57853699 130.064178467 0.22428937 7.92387152 134.92440796 0.46397027 8.13683224 135.057159424 0.22428937
		 3.62251854 138.64157104 0.46397027 3.73295569 138.86291504 0.22428937 7.15714455 132.014282227 0.46397027
		 7.34692287 131.865448 0.22428937 -8.13000011 135.40124512 0.46397027 -8.37491703 135.46734619 0.22428937
		 -6.26648808 128.69406128 0.46397027 -6.48249149 128.80761719 0.22428937 -4.48840618 128.67385864 0.46397027
		 -4.33617115 128.48269653 0.22428937 -6.799119 128.0262146 0.46397027 -7.32245541 127.7543869 0.22428937
		 -5.60379696 128.098571777 0.46397027 -5.53885841 127.86237335 0.22428937;
	setAttr -s 263 ".ed";
	setAttr ".ed[0:165]"  9 46 1 2 45 1 13 44 1 18 43 1 1 42 1 12 41 1 11 40 1
		 4 47 1 7 29 1 10 27 1 3 26 1 19 24 1 5 30 1 17 39 1 15 38 1 16 37 1 0 36 1 14 35 1
		 6 33 1 8 32 1 20 31 1 21 25 1 22 28 1 23 34 1 24 20 1 25 19 1 26 21 1 27 3 1 28 10 1
		 29 22 1 30 7 1 31 5 1 32 17 1 33 8 1 34 6 1 35 23 1 36 14 1 37 0 1 38 16 1 39 15 1
		 40 4 1 41 11 1 42 12 1 43 1 1 44 18 1 45 13 1 46 2 1 47 9 1 11 19 1 40 25 1 21 4 1
		 47 26 1 3 9 1 46 27 1 24 41 1 34 7 1 30 6 1 33 5 1 31 8 1 32 20 1 23 29 1 35 22 1
		 28 14 1 17 48 1 39 48 1 15 48 1 38 48 1 16 48 1 37 48 1 0 48 1 36 48 1 14 48 1 35 48 1
		 23 48 1 34 48 1 6 48 1 33 48 1 8 48 1 32 48 1 19 49 1 24 49 1 20 49 1 31 49 1 5 49 1
		 30 49 1 7 49 1 29 49 1 22 49 1 28 49 1 10 49 1 27 49 1 3 49 1 26 49 1 21 49 1 25 49 1
		 9 50 1 46 50 1 2 50 1 45 50 1 13 50 1 44 50 1 18 50 1 43 50 1 1 50 1 42 50 1 12 50 1
		 41 50 1 11 50 1 40 50 1 4 50 1 47 50 1 51 52 1 51 53 1 53 54 1 52 54 1 53 55 1 53 56 1
		 55 56 1 54 55 1 57 58 1 58 59 1 57 59 1 57 60 1 57 61 1 57 62 1 61 62 1 57 63 1 57 64 1
		 65 57 1 66 57 1 57 52 1 67 68 1 67 57 1 57 68 1 57 69 1 52 69 1 69 58 1 59 60 1 70 61 1
		 57 70 1 60 70 1 62 63 1 57 71 1 63 71 1 68 71 1 66 65 1 65 64 1 64 67 1 57 51 1 51 66 1
		 72 73 1 73 103 1 103 102 1 102 72 1 72 74 1 74 75 1 75 73 1 74 86 1 86 87 1 87 75 1
		 76 77 1 77 105 1 105 104 1 104 76 1 76 78 1 78 79 1;
	setAttr ".ed[166:262]" 79 77 1 78 80 1 80 81 1 81 79 1 80 102 1 103 81 1 82 83 1
		 83 85 1 85 84 1 84 82 1 82 100 1 100 101 1 101 83 1 85 97 1 97 96 1 96 84 1 86 98 1
		 98 99 1 99 87 1 88 89 1 89 91 1 91 90 1 90 88 1 88 106 1 106 107 1 107 89 1 91 93 1
		 93 92 1 92 90 1 93 95 1 95 94 1 94 92 1 95 101 1 100 94 1 97 99 1 98 96 1 105 109 1
		 109 108 1 108 104 1 106 110 1 110 111 1 111 107 1 109 111 1 110 108 1 88 76 1 104 106 1
		 110 104 1 45 92 1 94 13 1 44 100 1 100 18 1 43 84 1 84 1 1 96 1 1 98 12 1 42 98 1
		 102 15 1 39 102 1 80 16 1 38 80 1 78 0 1 37 78 1 36 88 1 88 14 1 98 41 1 46 92 1
		 92 2 1 72 17 1 17 74 1 28 90 1 90 10 1 18 82 1 96 42 1 86 24 1 74 20 1 74 32 1 36 76 1
		 77 51 1 53 105 1 107 54 1 52 89 1 56 109 1 55 111 1 93 58 1 59 95 1 85 61 1 62 97 1
		 75 68 1 67 73 1 69 91 1 60 101 1 83 70 1 63 99 1 71 87 1 81 65 1 66 79 1 103 64 1;
	setAttr -s 153 -ch 526 ".fc[0:152]" -type "polyFaces" 
		f 4 114 -114 -113 111
		mu 0 4 0 1 2 3
		f 3 117 -117 115
		mu 0 3 4 5 2
		f 3 118 -116 113
		mu 0 3 1 4 2
		f 3 121 -121 -120
		mu 0 3 6 7 8
		f 3 -126 -124 124
		mu 0 3 9 10 6
		f 3 -134 -133 131
		mu 0 3 11 6 12
		f 3 134 -136 -131
		mu 0 3 6 13 0
		f 3 119 -137 -135
		mu 0 3 6 8 13
		f 3 -138 -122 122
		mu 0 3 14 7 6
		f 3 -140 123 -139
		mu 0 3 15 6 10
		f 3 -141 -123 139
		mu 0 3 15 14 6
		f 3 -142 -125 126
		mu 0 3 16 9 6
		f 3 -144 -127 142
		mu 0 3 17 16 6
		f 3 144 -143 133
		mu 0 3 11 17 6
		f 3 145 128 -130
		mu 0 3 18 19 6
		f 3 146 -128 -129
		mu 0 3 19 20 6
		f 3 147 132 127
		mu 0 3 20 12 6
		f 3 -149 130 -112
		mu 0 3 3 6 0
		f 3 149 129 148
		mu 0 3 3 18 6
		f 4 50 -41 49 -22
		mu 0 4 151 135 136 150
		f 4 56 -35 55 -31
		mu 0 4 160 169 170 159
		f 4 48 -26 -50 -7
		mu 0 4 137 165 150 136
		f 4 -48 51 -11 52
		mu 0 4 149 134 152 153
		f 4 -52 -8 -51 -27
		mu 0 4 152 134 135 151
		f 4 -53 -28 -54 -1
		mu 0 4 149 153 154 36
		f 4 -55 -12 -49 -42
		mu 0 4 37 38 165 137
		f 4 -56 -24 60 -9
		mu 0 4 159 170 171 158
		f 4 58 -34 57 -32
		mu 0 4 162 167 168 161
		f 4 -58 -19 -57 -13
		mu 0 4 161 168 169 160
		f 4 -60 -20 -59 -21
		mu 0 4 45 46 167 162
		f 4 -61 -36 61 -30
		mu 0 4 158 171 172 157
		f 4 -62 -18 -63 -23
		mu 0 4 157 172 49 50
		f 3 13 64 -64
		mu 0 3 181 180 53
		f 3 39 65 -65
		mu 0 3 180 179 53
		f 3 14 66 -66
		mu 0 3 179 178 53
		f 3 38 67 -67
		mu 0 3 178 177 53
		f 3 15 68 -68
		mu 0 3 177 176 53
		f 3 37 69 -69
		mu 0 3 176 175 53
		f 3 16 70 -70
		mu 0 3 175 174 53
		f 3 36 71 -71
		mu 0 3 174 173 53
		f 3 17 72 -72
		mu 0 3 173 47 53
		f 3 35 73 -73
		mu 0 3 47 39 53
		f 3 23 74 -74
		mu 0 3 39 27 53
		f 3 34 75 -75
		mu 0 3 27 26 53
		f 3 18 76 -76
		mu 0 3 26 43 53
		f 3 33 77 -77
		mu 0 3 43 42 53
		f 3 19 78 -78
		mu 0 3 42 166 53
		f 3 32 63 -79
		mu 0 3 166 181 53
		f 3 11 80 -80
		mu 0 3 30 164 60
		f 3 24 81 -81
		mu 0 3 164 163 60
		f 3 20 82 -82
		mu 0 3 163 41 60
		f 3 31 83 -83
		mu 0 3 41 44 60
		f 3 12 84 -84
		mu 0 3 44 25 60
		f 3 30 85 -85
		mu 0 3 25 28 60
		f 3 8 86 -86
		mu 0 3 28 40 60
		f 3 29 87 -87
		mu 0 3 40 48 60
		f 3 22 88 -88
		mu 0 3 48 156 60
		f 3 28 89 -89
		mu 0 3 156 155 60
		f 3 9 90 -90
		mu 0 3 155 35 60
		f 3 27 91 -91
		mu 0 3 35 34 60
		f 3 10 92 -92
		mu 0 3 34 33 60
		f 3 26 93 -93
		mu 0 3 33 21 60
		f 3 21 94 -94
		mu 0 3 21 24 60
		f 3 25 79 -95
		mu 0 3 24 30 60
		f 3 0 96 -96
		mu 0 3 31 148 62
		f 3 46 97 -97
		mu 0 3 148 147 62
		f 3 1 98 -98
		mu 0 3 147 146 62
		f 3 45 99 -99
		mu 0 3 146 145 62
		f 3 2 100 -100
		mu 0 3 145 144 62
		f 3 44 101 -101
		mu 0 3 144 143 62
		f 3 3 102 -102
		mu 0 3 143 142 62
		f 3 43 103 -103
		mu 0 3 142 141 62
		f 3 4 104 -104
		mu 0 3 141 140 62
		f 3 42 105 -105
		mu 0 3 140 139 62
		f 3 5 106 -106
		mu 0 3 139 138 62
		f 3 41 107 -107
		mu 0 3 138 29 62
		f 3 6 108 -108
		mu 0 3 29 23 62
		f 3 40 109 -109
		mu 0 3 23 22 62
		f 3 7 110 -110
		mu 0 3 22 32 62
		f 3 47 95 -111
		mu 0 3 32 31 62
		f 4 150 151 152 153
		mu 0 4 131 73 74 127
		f 4 -151 154 155 156
		mu 0 4 73 131 130 77
		f 4 -156 157 158 159
		mu 0 4 77 130 123 79
		f 4 160 161 162 163
		mu 0 4 129 81 82 115
		f 4 -161 164 165 166
		mu 0 4 81 129 128 85
		f 4 -166 167 168 169
		mu 0 4 85 128 126 87
		f 4 -169 170 -153 171
		mu 0 4 87 126 127 74
		f 4 172 173 174 175
		mu 0 4 125 89 90 124
		f 4 -173 176 177 178
		mu 0 4 89 125 118 93
		f 4 -175 179 180 181
		mu 0 4 124 90 94 117
		f 4 -159 182 183 184
		mu 0 4 79 123 116 97
		f 4 185 186 187 188
		mu 0 4 122 99 100 121
		f 4 -186 189 190 191
		mu 0 4 99 122 114 103
		f 4 -188 192 193 194
		mu 0 4 121 100 104 120
		f 4 -194 195 196 197
		mu 0 4 120 104 106 119
		f 4 -197 198 -178 199
		mu 0 4 119 106 93 118
		f 4 -181 200 -184 201
		mu 0 4 117 94 97 116
		f 4 -163 202 203 204
		mu 0 4 115 82 108 133
		f 4 -191 205 206 207
		mu 0 4 103 114 112 111
		f 4 -204 208 -207 209
		mu 0 4 109 132 111 112
		f 4 210 -164 211 -190
		mu 0 4 98 80 83 102
		f 3 212 -205 -210
		mu 0 3 110 83 113
		f 3 -212 -213 -206
		mu 0 3 102 83 110
		f 4 -46 213 -198 214
		mu 0 4 65 64 105 107
		f 3 -45 215 216
		mu 0 3 67 66 92
		f 3 217 218 -44
		mu 0 3 68 91 69
		f 3 219 -219 -182
		mu 0 3 95 69 91
		f 3 220 -43 221
		mu 0 3 96 71 70
		f 3 222 -40 223
		mu 0 3 75 54 52
		f 3 224 -39 225
		mu 0 3 86 56 55
		f 3 226 -38 227
		mu 0 3 84 58 57
		f 3 228 229 -37
		mu 0 3 59 98 49
		f 3 230 -6 -221
		mu 0 3 96 37 71
		f 3 231 232 -47
		mu 0 3 36 105 63
		f 3 -155 233 234
		mu 0 3 76 72 51
		f 3 235 236 -29
		mu 0 3 50 101 61
		f 4 62 -230 -189 -236
		mu 0 4 50 49 98 101
		f 5 53 -10 -237 -195 -232
		mu 0 5 36 154 61 101 105
		f 3 -214 -2 -233
		mu 0 3 105 64 63
		f 4 -216 -3 -215 -200
		mu 0 4 92 66 65 107
		f 4 -176 -218 -4 237
		mu 0 4 88 91 68 67
		f 3 -238 -217 -177
		mu 0 3 88 67 92
		f 3 238 -5 -220
		mu 0 3 95 70 69
		f 3 -222 -239 -202
		mu 0 3 96 70 95
		f 4 239 54 -231 -183
		mu 0 4 78 38 37 96
		f 4 240 -25 -240 -158
		mu 0 4 76 45 38 78
		f 3 241 59 -241
		mu 0 3 76 46 45
		f 3 -235 -33 -242
		mu 0 3 76 51 46
		f 4 -228 -16 -225 -168
		mu 0 4 84 57 56 86
		f 4 -226 -15 -223 -171
		mu 0 4 86 55 54 75
		f 4 -224 -14 -234 -154
		mu 0 4 75 52 51 72
		f 3 -211 -229 242
		mu 0 3 80 98 59
		f 4 -243 -17 -227 -165
		mu 0 4 80 59 58 84
		f 4 243 112 244 -162
		mu 0 4 81 3 2 82
		f 4 245 -115 246 -192
		mu 0 4 103 1 0 99
		f 4 -245 116 247 -203
		mu 0 4 82 2 5 108
		f 4 -248 -118 248 -209
		mu 0 4 132 5 4 111
		f 4 -249 -119 -246 -208
		mu 0 4 111 4 1 103
		f 4 249 120 250 -196
		mu 0 4 104 8 7 106
		f 4 251 125 252 -180
		mu 0 4 90 10 9 94
		f 4 253 -132 254 -157
		mu 0 4 77 11 12 73
		f 4 -247 135 255 -187
		mu 0 4 99 0 13 100
		f 4 -256 136 -250 -193
		mu 0 4 100 13 8 104
		f 4 -251 137 256 -199
		mu 0 4 106 7 14 93
		f 4 257 138 -252 -174
		mu 0 4 89 15 10 90
		f 4 -257 140 -258 -179
		mu 0 4 93 14 15 89
		f 4 -253 141 258 -201
		mu 0 4 94 9 16 97
		f 4 -259 143 259 -185
		mu 0 4 97 16 17 79
		f 4 -260 -145 -254 -160
		mu 0 4 79 17 11 77
		f 4 260 -146 261 -170
		mu 0 4 87 19 18 85
		f 4 262 -147 -261 -172
		mu 0 4 74 20 19 87
		f 4 -255 -148 -263 -152
		mu 0 4 73 12 20 74
		f 4 -262 -150 -244 -167
		mu 0 4 85 18 3 81;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 51 
		21 0 
		22 0 
		23 0 
		24 0 
		25 0 
		26 0 
		27 0 
		28 0 
		29 0 
		30 0 
		31 0 
		32 0 
		33 0 
		34 0 
		35 0 
		39 0 
		40 0 
		41 0 
		42 0 
		43 0 
		44 0 
		47 0 
		48 0 
		53 0 
		60 0 
		62 0 
		138 0 
		139 0 
		140 0 
		141 0 
		142 0 
		143 0 
		144 0 
		145 0 
		146 0 
		147 0 
		148 0 
		155 0 
		156 0 
		163 0 
		164 0 
		166 0 
		173 0 
		174 0 
		175 0 
		176 0 
		177 0 
		178 0 
		179 0 
		180 0 
		181 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Shock" -p "C000_Generic_01_PopUp";
	rename -uid "275180E9-4D9F-BD3D-E675-47AA171D32E6";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
	setAttr ".sp" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
createNode mesh -n "ShockShape" -p "Shock";
	rename -uid "96C3B539-4AE9-DF66-EFE1-16B3E27CBC93";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.96776577830314636 0.030974924564361572 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "ShockShapeOrig" -p "Shock";
	rename -uid "01553E51-4F48-2D86-7C50-9FACBF958898";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".gtag[0].gtagnm" -type "string" "front";
	setAttr ".gtag[0].gtagcmp" -type "componentList" 4 "f[0]" "f[8:11]" "f[28]" "f[36:39]";
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 112 ".uvst[0].uvsp[0:111]" -type "float2" 0.48344892 0.02386567
		 0.48741633 0.031009972 0.4840852 0.039381981 0.48060077 0.029002368 0.48556137 0.04750067
		 0.48193249 0.047200024 0.48374087 0.013950229 0.48843217 0.012151554 0.48876381 0.052282989
		 0.47825807 0.051566541 0.48038933 0.031748846 0.48392394 0.023871556 0.48795488 0.030701384
		 0.48293456 0.037351862 0.48548007 0.047475278 0.48195666 0.04750061 0.48345906 0.013645291
		 0.48804373 0.011426985 0.48896235 0.05323863 0.47821903 0.051342547 0.48431006 0.090254389
		 0.48506004 0.020286873 0.47898826 0.02542603 0.47804838 0.034101814 0.48431006 0.099354357
		 0.48930037 0.034008592 0.48208612 0.042066306 0.48753688 0.042078376 0.4814845 0.071722582
		 0.49061203 0.011933997 0.48326316 0.0096819699 0.48609567 0.073483303 0.4814724 0.11779654
		 0.48826069 0.055399895 0.47615358 0.050270379 0.48051298 0.055467486 0.48379016 0.11254561
		 0.48512369 0.052133203 0.48878273 0.11247885 0.48233533 0.051926553 0.48438638 0.090240143
		 0.47864881 0.028624788 0.48120362 0.040497094 0.48538977 0.042348385 0.48429647 0.09935008
		 0.48543566 0.020302761 0.48924631 0.034600906 0.48938704 0.024114568 0.48253244 0.070834696
		 0.49025279 0.011050344 0.48284546 0.0093827844 0.48706457 0.073270649 0.48130238
		 0.11868447 0.48834383 0.05637151 0.47606725 0.050118506 0.48026267 0.055650651 0.48396808
		 0.11248428 0.48494133 0.052357137 0.48886079 0.11405605 0.48222616 0.05215776 0.48221168
		 0.05419755 0.4914341 0.11853892 0.48475879 0.054495871 0.49215388 0.048566401 0.48020664
		 0.012607604 0.48643243 0.0054358244 0.48085988 0.020403378 0.48844004 0.099750295
		 0.48724687 0.08976882 0.47831646 0.037412986 0.48235661 0.053948343 0.49126408 0.11693364
		 0.48502415 0.054268718 0.49196476 0.048332512 0.48055333 0.012856007 0.48702037 0.0061165541
		 0.48922524 0.024739534 0.48842645 0.099856108 0.48714405 0.089663014 0.48054212 0.019573741
		 0.48218337 0.020747591 0.48946655 0.02713256 0.48422599 0.041251391 0.47865838 0.034894034
		 0.48902744 0.02743119 0.48596925 0.042380601 0.47860172 0.031686693 0.48183641 0.020289347
		 0.48898989 0.037579313 0.48672339 0.019601453 0.47994071 0.040988475 0.47829923 0.026110072
		 0.48053586 0.041511655 0.48971739 0.036598176 0.47874531 0.022814274 0.48635402 0.019569233
		 0.48166302 0.012605786 0.48805481 0.007816717 0.48350555 0.0074877292 0.49165618
		 0.013538793 0.47853321 0.055231392 0.4909656 0.052129388 0.47580105 0.045328081 0.48678797
		 0.05583328 0.47840938 0.055097342 0.49120116 0.052916586 0.4756119 0.045565605 0.48673028
		 0.056514025 0.48133072 0.01235047 0.48754644 0.0070474744 0.48301175 0.0071413815
		 0.49133712 0.012654454;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 60 ".vt[0:59]"  -5.56692505 128.96563721 -0.66225982 -4.03004837 128.58572388 -0.66225982
		 -3.061288834 130.97738647 -0.66225982 -5.26300049 131.14834595 -0.66225982 -2.082845688 128.82846069 -0.66225982
		 2.18890572 135.7038269 -0.66225982 0.15196609 128.3616333 -0.66225982 3.56987071 135.1178894 -0.66225982
		 1.55225372 137.57073975 -0.66225982 5.56692314 135.81744385 -0.66225982 -3.31118584 126.12652588 -0.66225815
		 -1.88168526 125.38870239 -0.66225815 -0.37605095 127.45822906 -0.66225815 -2.48828316 128.21975708 -0.66225815
		 -4.88688469 131.86468506 -0.66225982 -2.38017464 139.5039978 -0.66225982 -2.65207481 132.0037536621 -0.66225982
		 -0.94651991 139.44497681 -0.66225982 -3.4521122 141.4211731 -0.66225982 0.83257866 140.45462036 -0.66225982
		 -5.19843864 129.21505737 0.66225827 -5.56692505 128.96563721 0.33169141 -4.22886848 128.97540283 0.66225827
		 -4.03004837 128.58572388 0.33169141 -4.97848511 130.79467773 0.66225827 -5.26300049 131.14834595 0.33169141
		 -3.53727531 130.68276978 0.66225827 -3.061288834 130.97738647 0.33169141 -1.62425411 129.070373535 0.66225827
		 -2.082845688 128.82846069 0.33169141 0.010189056 128.72894287 0.66225827 0.15196609 128.3616333 0.33169141
		 1.92373383 135.45724487 0.66225815 2.18890572 135.7038269 0.33169141 3.55847192 134.76364136 0.66225827
		 3.56987071 135.1178894 0.33169141 1.52168095 136.63623047 0.66225827 1.55225372 137.57073975 0.33169141
		 4.67778111 135.1557312 0.66225827 5.56692314 135.81744385 0.33169141 -2.89433098 126.28338623 0.66225982
		 -3.31118584 126.12652588 0.33169302 -1.98212433 125.81253052 0.66225982 -1.88168526 125.38870239 0.33169302
		 -2.29817581 127.79983521 0.66225982 -2.48828316 128.21975708 0.33169302 -0.90242761 127.29660034 0.66225982
		 -0.37605095 127.45822906 0.33169302 -4.49926567 132.22000122 0.66225827 -4.88688469 131.86468506 0.33169141
		 -2.87888908 132.3208313 0.66225827 -2.65207481 132.0037536621 0.33169141 -2.57848358 139.18130493 0.66225815
		 -2.38017464 139.5039978 0.33169141 -0.86561966 139.11080933 0.66225827 -0.94651991 139.44497681 0.33169141
		 -3.26876831 140.41589355 0.66225827 -3.4521122 141.4211731 0.33169141 0.16117096 139.69351196 0.66225827
		 0.83257866 140.45462036 0.33169141;
	setAttr -s 108 ".ed[0:107]"  0 1 1 1 2 1 3 2 1 0 3 1 4 5 1 4 6 1 7 6 1
		 5 7 1 5 8 1 4 8 1 6 9 1 7 9 1 10 11 1 11 12 1 13 12 1 10 13 1 14 15 1 14 16 1 17 16 1
		 15 17 1 15 18 1 14 18 1 16 19 1 17 19 1 20 21 1 21 23 1 23 22 1 22 20 1 20 24 1 24 25 1
		 25 21 1 23 27 1 27 26 1 26 22 1 24 26 1 27 25 1 28 29 1 29 31 1 31 30 1 30 28 1 28 36 1
		 36 37 1 37 29 1 31 39 1 39 38 1 38 30 1 32 33 1 33 37 1 36 32 1 32 34 1 34 35 1 35 33 1
		 34 38 1 39 35 1 40 41 1 41 43 1 43 42 1 42 40 1 40 44 1 44 45 1 45 41 1 43 47 1 47 46 1
		 46 42 1 44 46 1 47 45 1 48 49 1 49 51 1 51 50 1 50 48 1 48 56 1 56 57 1 57 49 1 51 59 1
		 59 58 1 58 50 1 52 53 1 53 57 1 56 52 1 52 54 1 54 55 1 55 53 1 54 58 1 59 55 1 32 28 1
		 30 34 1 52 48 1 50 54 1 21 0 1 1 23 1 2 27 1 3 25 1 29 4 1 6 31 1 35 7 1 5 33 1 8 37 1
		 9 39 1 41 10 1 11 43 1 12 47 1 13 45 1 49 14 1 16 51 1 55 17 1 15 53 1 18 57 1 19 59 1;
	setAttr -s 56 -ch 216 ".fc[0:55]" -type "polyFaces" 
		f 4 3 2 -2 -1
		mu 0 4 0 1 2 3
		f 4 7 6 -6 4
		mu 0 4 4 5 6 7
		f 3 9 -9 -5
		mu 0 3 7 8 4
		f 3 11 -11 -7
		mu 0 3 5 9 6
		f 4 15 14 -14 -13
		mu 0 4 10 11 12 13
		f 4 19 18 -18 16
		mu 0 4 14 15 16 17
		f 3 21 -21 -17
		mu 0 3 17 18 14
		f 3 23 -23 -19
		mu 0 3 15 19 16
		f 4 24 25 26 27
		mu 0 4 79 87 22 94
		f 4 -25 28 29 30
		mu 0 4 21 95 76 84
		f 4 -27 31 32 33
		mu 0 4 23 86 26 92
		f 4 -30 34 -33 35
		mu 0 4 25 93 27 85
		f 4 36 37 38 39
		mu 0 4 75 97 30 98
		f 4 -37 40 41 42
		mu 0 4 29 99 73 101
		f 4 -39 43 44 45
		mu 0 4 74 96 34 102
		f 4 46 47 -42 48
		mu 0 4 72 37 33 103
		f 4 -47 49 50 51
		mu 0 4 37 72 70 39
		f 4 -51 52 -45 53
		mu 0 4 39 70 35 100
		f 4 54 55 56 57
		mu 0 4 69 83 42 90
		f 4 -55 58 59 60
		mu 0 4 41 91 66 80
		f 4 -57 61 62 63
		mu 0 4 43 82 46 88
		f 4 -60 64 -63 65
		mu 0 4 45 89 47 81
		f 4 66 67 68 69
		mu 0 4 65 109 50 110
		f 4 -67 70 71 72
		mu 0 4 49 111 63 105
		f 4 -69 73 74 75
		mu 0 4 64 108 54 106
		f 4 76 77 -72 78
		mu 0 4 62 57 53 107
		f 4 -77 79 80 81
		mu 0 4 57 62 60 59
		f 4 -81 82 -75 83
		mu 0 4 59 60 55 104
		f 4 -28 -34 -35 -29
		mu 0 4 20 78 77 24
		f 4 84 -40 85 -50
		mu 0 4 36 28 31 38
		f 3 -85 -49 -41
		mu 0 3 28 36 32
		f 3 -86 -46 -53
		mu 0 3 38 31 71
		f 4 -58 -64 -65 -59
		mu 0 4 40 68 67 44
		f 4 86 -70 87 -80
		mu 0 4 56 48 51 58
		f 3 -87 -79 -71
		mu 0 3 48 56 52
		f 3 -88 -76 -83
		mu 0 3 58 51 61
		f 4 88 0 89 -26
		mu 0 4 87 0 3 22
		f 4 -90 1 90 -32
		mu 0 4 86 3 2 26
		f 4 -91 -3 91 -36
		mu 0 4 85 2 1 25
		f 4 -92 -4 -89 -31
		mu 0 4 84 1 0 21
		f 4 92 5 93 -38
		mu 0 4 97 7 6 30
		f 4 94 -8 95 -52
		mu 0 4 39 5 4 37
		f 4 -96 8 96 -48
		mu 0 4 37 4 8 33
		f 4 -97 -10 -93 -43
		mu 0 4 101 8 7 29
		f 4 -94 10 97 -44
		mu 0 4 96 6 9 34
		f 4 -98 -12 -95 -54
		mu 0 4 100 9 5 39
		f 4 98 12 99 -56
		mu 0 4 83 10 13 42
		f 4 -100 13 100 -62
		mu 0 4 82 13 12 46
		f 4 -101 -15 101 -66
		mu 0 4 81 12 11 45
		f 4 -102 -16 -99 -61
		mu 0 4 80 11 10 41
		f 4 102 17 103 -68
		mu 0 4 109 17 16 50
		f 4 104 -20 105 -82
		mu 0 4 59 15 14 57
		f 4 -106 20 106 -78
		mu 0 4 57 14 18 53
		f 4 -107 -22 -103 -73
		mu 0 4 105 18 17 49
		f 4 -104 22 107 -74
		mu 0 4 108 16 19 54
		f 4 -108 -24 -105 -84
		mu 0 4 104 19 15 59;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Confused" -p "C000_Generic_01_PopUp";
	rename -uid "6020A2B0-4356-ADA3-CFAD-B4B541DF3992";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 133.40493011474609 0 ;
	setAttr ".sp" -type "double3" 0 133.40493011474609 0 ;
createNode mesh -n "ConfusedShape" -p "Confused";
	rename -uid "35CEAB98-4B61-E924-C70D-87A141B0E9D7";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.90470807690052346 0.031107727694287046 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "ConfusedShapeOrig" -p "Confused";
	rename -uid "90E28362-4123-F833-4F6E-799B209F1CC3";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 114 ".uvst[0].uvsp[0:113]" -type "float2" 0.44469512 0.024211228
		 0.44799128 0.026029289 0.4476192 0.032075107 0.44313678 0.023255229 0.44302514 0.029933155
		 0.44357997 0.030484378 0.45014814 0.028549612 0.45041278 0.037860334 0.44993091 0.037994862
		 0.45479769 0.028798997 0.45376974 0.034284472 0.45774561 0.033924043 0.45616633 0.036540031
		 0.4588629 0.026977956 0.46125454 0.032683074 0.46330702 0.023374259 0.46035749 0.023709327
		 0.45716003 0.039043605 0.46408165 0.035140991 0.45241198 0.022313852 0.45722097 0.030609891
		 0.45182338 0.040327653 0.448401 0.029253066 0.46456057 0.073445678 0.4433676 0.020386636
		 0.44138977 0.029840469 0.46628541 0.084600031 0.46256238 0.075256675 0.4449178 0.021174639
		 0.44291818 0.032756269 0.46597362 0.085327983 0.45634472 0.082598358 0.44825104 0.023885101
		 0.45566216 0.093089283 0.45052028 0.025373459 0.4465988 0.035214245 0.45822316 0.089186668
		 0.44820571 0.10185528 0.45455748 0.025052965 0.44919142 0.040267885 0.45972002 0.10699719
		 0.45066512 0.040729225 0.45935902 0.10781848 0.45088974 0.10782081 0.45373857 0.037598431
		 0.45573613 0.03942138 0.44294536 0.10684603 0.44646192 0.084628761 0.45831031 0.023118883
		 0.45689666 0.041447461 0.45840114 0.041025162 0.45184678 0.086321682 0.46024472 0.02133283
		 0.44357279 0.097970724 0.45879811 0.036748707 0.46150285 0.035794079 0.44275874 0.080676407
		 0.46399397 0.03739655 0.46617863 0.033329725 0.46486244 0.022618979 0.45205811 0.072798461
		 0.45098096 0.08304216 0.45407948 0.018447541 0.44673076 0.025391486 0.44570827 0.033963628
		 0.45024478 0.094653398 0.45892912 0.034404747 0.44965172 0.043012083 0.45479849 0.044467241
		 0.45888841 0.026743576 0.45353141 0.044122487 0.44622934 0.031937517 0.4507418 0.018452227
		 0.46567449 0.035001993 0.45780563 0.04118979 0.46356797 0.02049166 0.45011824 0.041277945
		 0.44236785 0.032239676 0.44160447 0.022785485 0.44826686 0.02367714 0.4589327 0.024242718
		 0.45899975 0.036903083 0.44838715 0.042632326 0.45689884 0.094653398 0.44653702 0.023146249
		 0.45582902 0.082850307 0.44965249 0.017756097 0.45516807 0.017748207 0.4603883 0.020416737
		 0.4632442 0.019450843 0.46551052 0.023164541 0.4632479 0.037993729 0.43954352 0.074762464
		 0.46163219 0.036942542 0.45910352 0.03776443 0.45626467 0.041786134 0.44055685 0.10596114
		 0.45852077 0.021850318 0.45556146 0.040563822 0.45442295 0.024099529 0.45376557 0.038829803
		 0.4508951 0.041769505 0.45065981 0.042123079 0.44878715 0.041026592 0.44630587 0.036150873
		 0.45046073 0.024240732 0.44269255 0.033726335 0.44822836 0.02233237 0.44843853 0.022925258
		 0.44503474 0.020004213 0.44242916 0.033555686 0.44079489 0.029299378 0.44097418 0.023574054
		 0.44394198 0.019441009;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 69 ".vt[0:68]"  -2.42641401 131.55599976 -0.6607486 0.26142311 132.92077637 -0.66074872
		 -1.38075066 133.95089722 -0.66074872 -2.75004005 130.52383423 -0.66074872 -0.32546234 130.086853027 -0.66074872
		 -0.049937248 130.38821411 -0.66074872 0.36517715 134.39859009 -0.66074872 3.507056 133.12225342 -0.66074872
		 3.209512 132.7883606 -0.66074872 3.14075398 136.12213135 -0.66074872 1.32767475 136.61456299 -0.66074872
		 2.64264393 138.81484985 -0.66074872 0.77709484 138.62908936 -0.66074872 -1.96476221 138.55291748 -0.66074872
		 -0.8620019 136.78591919 -0.66074872 -3.28016782 134.63433838 -0.66074872 -0.37646532 135.081787109 -0.66074872
		 2.25252819 140.05480957 -0.66074872 -3.507056 139.86672974 -0.66074872 -3.18853474 127.15706635 -0.66074705
		 -1.065144539 126.75505066 -0.66074705 -0.1638689 129.24984741 -0.66074705 -3.081913948 129.74276733 -0.66074705
		 -2.38632536 130.74398804 0.66074717 -2.75004005 130.52383423 0.37956074 -0.42828986 130.39111328 0.66074717
		 -0.32546234 130.086853027 0.37956074 -2.16264725 131.45739746 0.66074717 -2.42641401 131.55599976 0.3795608
		 -1.17797089 133.71261597 0.66074717 -1.38075066 133.95089722 0.37956074 -0.31806326 130.51165771 0.66074717
		 -0.049937248 130.38821411 0.37956074 0.56827927 134.16040039 0.66074717 0.36517715 134.39859009 0.37956074
		 0.014090538 133.21334839 0.66074717 0.26142311 132.92077637 0.37956074 3.088546753 133.075256348 0.66074717
		 3.209512 132.7883606 0.37956074 2.86268711 136.079467773 0.66074717 3.14075398 136.12213135 0.37956074
		 3.21253014 133.21438599 0.66074717 3.507056 133.12225342 0.37956074 1.7426405 136.86413574 0.66074717
		 1.32767475 136.61456299 0.37956074 2.36927128 138.74682617 0.66074717 2.64264393 138.81484985 0.37956074
		 -1.24323797 137.097808838 0.66074717 -0.8620019 136.78591919 0.37956074 0.89400291 138.3510437 0.66074717
		 0.77709484 138.62908936 0.37956074 -2.064898491 138.26882935 0.66074717 -1.96476221 138.55291748 0.37956074
		 -3.19817924 139.23422241 0.66074717 -3.507056 139.86672974 0.37956074 -3.012839794 134.96005249 0.66074717
		 -3.28016782 134.63433838 0.37956074 -0.73419571 135.31115723 0.66074717 -0.37646532 135.081787109 0.37956074
		 2.12081814 139.53652954 0.66074717 2.25252819 140.05480957 0.37956074 -2.89758015 127.38815308 0.66074872
		 -3.18853474 127.15706635 0.37956235 -1.248209 127.075866699 0.66074872 -1.065144539 126.75505066 0.37956235
		 -2.81411266 129.41235352 0.66074872 -3.081913948 129.74276733 0.37956235 -0.5427413 129.028686523 0.66074872
		 -0.1638689 129.24984741 0.37956235;
	setAttr -s 143 ".ed[0:142]"  0 1 1 2 1 1 0 2 1 3 4 1 0 4 1 3 0 1 0 5 1
		 5 1 1 6 1 1 2 6 1 7 6 1 6 8 1 8 7 1 6 9 1 10 9 1 6 10 1 9 11 1 12 11 1 10 12 1 1 8 1
		 4 5 1 12 13 1 14 13 1 10 14 1 13 15 1 14 15 1 15 16 1 14 16 1 11 17 1 12 17 1 13 18 1
		 15 18 1 9 7 1 19 20 1 20 21 1 22 21 1 19 22 1 23 24 1 24 26 1 26 25 1 25 23 1 23 27 1
		 27 28 1 28 24 1 26 32 1 32 31 1 31 25 1 27 29 1 29 30 1 30 28 1 29 33 1 33 34 1 34 30 1
		 32 36 1 36 35 1 35 31 1 33 43 1 43 44 1 44 34 1 36 38 1 38 37 1 37 35 1 38 42 1 42 41 1
		 41 37 1 39 40 1 40 46 1 46 45 1 45 39 1 39 41 1 42 40 1 43 47 1 47 48 1 48 44 1 46 60 1
		 60 59 1 59 45 1 47 57 1 57 58 1 58 48 1 49 50 1 50 52 1 52 51 1 51 49 1 49 59 1 60 50 1
		 52 54 1 54 53 1 53 51 1 54 56 1 56 55 1 55 53 1 56 58 1 57 55 1 61 62 1 62 64 1 64 63 1
		 63 61 1 61 65 1 65 66 1 66 62 1 64 68 1 68 67 1 67 63 1 65 67 1 68 66 1 27 35 1 35 29 1
		 25 27 1 27 31 1 35 33 1 41 33 1 33 37 1 33 39 1 39 43 1 45 49 1 49 43 1 51 47 1 51 55 1
		 55 47 1 30 2 1 0 28 1 24 3 1 4 26 1 32 5 1 1 36 1 34 6 1 38 8 1 7 42 1 44 10 1 40 9 1
		 11 46 1 50 12 1 13 52 1 48 14 1 56 15 1 16 58 1 17 60 1 18 54 1 62 19 1 20 64 1 21 68 1
		 22 66 1;
	setAttr -s 78 -ch 286 ".fc[0:77]" -type "polyFaces" 
		f 3 2 1 -1
		mu 0 3 0 1 2
		f 3 5 4 -4
		mu 0 3 3 0 4
		f 3 0 -8 -7
		mu 0 3 0 2 5
		f 3 9 8 -2
		mu 0 3 1 6 2
		f 3 -13 -12 -11
		mu 0 3 7 8 6
		f 3 15 14 -14
		mu 0 3 6 9 10
		f 4 18 17 -17 -15
		mu 0 4 9 11 12 10
		f 3 11 -20 -9
		mu 0 3 6 8 2
		f 3 6 -21 -5
		mu 0 3 0 5 4
		f 4 23 22 -22 -19
		mu 0 4 9 13 14 11
		f 3 25 -25 -23
		mu 0 3 13 15 14
		f 3 27 -27 -26
		mu 0 3 13 16 15
		f 3 29 -29 -18
		mu 0 3 11 17 12
		f 3 31 -31 24
		mu 0 3 15 18 14
		f 3 32 10 13
		mu 0 3 10 7 6
		f 4 36 35 -35 -34
		mu 0 4 19 20 21 22
		f 4 37 38 39 40
		mu 0 4 112 78 25 111
		f 4 -38 41 42 43
		mu 0 4 24 113 109 28
		f 4 -40 44 45 46
		mu 0 4 110 77 29 106
		f 4 -43 47 48 49
		mu 0 4 28 109 107 79
		f 4 -49 50 51 52
		mu 0 4 32 108 105 34
		f 4 -46 53 54 55
		mu 0 4 106 29 35 104
		f 4 -52 56 57 58
		mu 0 4 34 105 99 38
		f 4 -55 59 60 61
		mu 0 4 104 35 39 103
		f 4 -61 62 63 64
		mu 0 4 102 76 41 101
		f 4 65 66 67 68
		mu 0 4 100 44 45 98
		f 4 -66 69 -64 70
		mu 0 4 44 100 101 41
		f 4 -58 71 72 73
		mu 0 4 38 99 97 48
		f 4 -68 74 75 76
		mu 0 4 98 45 49 95
		f 4 -73 77 78 79
		mu 0 4 48 97 88 52
		f 4 80 81 82 83
		mu 0 4 94 54 55 93
		f 4 -81 84 -76 85
		mu 0 4 54 94 50 74
		f 4 -83 86 87 88
		mu 0 4 93 55 57 91
		f 4 -88 89 90 91
		mu 0 4 58 73 59 90
		f 4 -91 92 -79 93
		mu 0 4 89 75 52 88
		f 4 94 95 96 97
		mu 0 4 86 72 63 84
		f 4 -95 98 99 100
		mu 0 4 62 87 80 69
		f 4 -97 101 102 103
		mu 0 4 64 71 67 82
		f 4 -100 104 -103 105
		mu 0 4 66 81 68 70
		f 3 106 107 -48
		mu 0 3 27 36 31
		f 3 -41 108 -42
		mu 0 3 23 26 27
		f 3 109 -56 -107
		mu 0 3 27 30 36
		f 3 -108 110 -51
		mu 0 3 31 36 33
		f 3 111 112 -65
		mu 0 3 42 33 40
		f 3 113 114 -57
		mu 0 3 33 43 37
		f 4 -115 -69 115 116
		mu 0 4 37 43 46 53
		f 3 -111 -62 -113
		mu 0 3 33 36 40
		f 3 -109 -47 -110
		mu 0 3 27 26 30
		f 4 -117 -84 117 -72
		mu 0 4 37 53 56 47
		f 3 -118 118 119
		mu 0 3 47 56 60
		f 3 -120 -94 -78
		mu 0 3 47 60 51
		f 3 -116 -77 -85
		mu 0 3 53 46 96
		f 3 -119 -89 -92
		mu 0 3 60 56 92
		f 3 -114 -112 -70
		mu 0 3 43 33 42
		f 4 -98 -104 -105 -99
		mu 0 4 61 85 83 65
		f 4 120 -3 121 -50
		mu 0 4 79 1 0 28
		f 4 122 3 123 -39
		mu 0 4 78 3 4 25
		f 4 -122 -6 -123 -44
		mu 0 4 28 0 3 24
		f 4 124 7 125 -54
		mu 0 4 29 5 2 35
		f 4 126 -10 -121 -53
		mu 0 4 34 6 1 32
		f 4 127 12 128 -63
		mu 0 4 76 8 7 41
		f 4 129 -16 -127 -59
		mu 0 4 38 9 6 34
		f 4 130 16 131 -67
		mu 0 4 44 10 12 45
		f 4 -126 19 -128 -60
		mu 0 4 35 2 8 39
		f 4 -124 20 -125 -45
		mu 0 4 77 4 5 29
		f 4 132 21 133 -82
		mu 0 4 54 11 14 55
		f 4 134 -24 -130 -74
		mu 0 4 48 13 9 38
		f 4 135 26 136 -93
		mu 0 4 75 15 16 52
		f 4 -137 -28 -135 -80
		mu 0 4 52 16 13 48
		f 4 -132 28 137 -75
		mu 0 4 45 12 17 49
		f 4 -138 -30 -133 -86
		mu 0 4 74 17 11 54
		f 4 -134 30 138 -87
		mu 0 4 55 14 18 57
		f 4 -139 -32 -136 -90
		mu 0 4 73 18 15 59
		f 4 -129 -33 -131 -71
		mu 0 4 41 7 10 44
		f 4 139 33 140 -96
		mu 0 4 72 19 22 63
		f 4 -141 34 141 -102
		mu 0 4 71 22 21 67
		f 4 -142 -36 142 -106
		mu 0 4 70 21 20 66
		f 4 -143 -37 -140 -101
		mu 0 4 69 20 19 62;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Uncomfortable" -p "C000_Generic_01_PopUp";
	rename -uid "0A363426-4C14-AFF0-8079-46966A187709";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 133.40494537353516 5.9604644775390625e-08 ;
	setAttr ".sp" -type "double3" 0 133.40494537353516 5.9604644775390625e-08 ;
createNode mesh -n "UncomfortableShape" -p "Uncomfortable";
	rename -uid "9A24416C-4600-0950-1C7A-1EA76C1CF735";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.84404897592988681 0.093468675277090713 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "UncomfortableShapeOrig" -p "Uncomfortable";
	rename -uid "F8DE763B-4A5A-3713-A975-70A56C2FD66F";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 162 ".uvst[0].uvsp[0:161]" -type "float2" 0.42721179 0.04622861
		 0.42418656 0.049356446 0.42077693 0.049557231 0.41805193 0.046597086 0.42132643 0.021006115
		 0.42518583 0.011021793 0.42753407 0.01908049 0.41831151 0.028812684 0.42900011 0.026956499
		 0.41678587 0.03522943 0.42961416 0.03450916 0.4292002 0.04041785 0.41676983 0.041175358
		 0.43027201 0.026449159 0.43170223 0.031795815 0.43152729 0.035997435 0.43012717 0.039613098
		 0.41769674 0.03727936 0.4130365 0.030532166 0.41697612 0.025096893 0.42197701 0.042029165
		 0.42081788 0.021957591 0.42549774 0.042924225 0.42465034 0.021003053 0.42773834 0.022519462
		 0.42838994 0.041644625 0.41832712 0.037664101 0.4169437 0.032974608 0.41687366 0.029090807
		 0.41771618 0.025965005 0.42723277 0.026323862 0.43090299 0.030265458 0.42815414 0.035976328
		 0.42425928 0.023510545 0.42552504 0.039070196 0.42095849 0.022734061 0.42307803 0.040767126
		 0.42028907 0.040286139 0.41890243 0.024198808 0.41754416 0.087441273 0.43193927 0.035439029
		 0.43144211 0.026417673 0.42071226 0.081748731 0.4158335 0.092723884 0.43113282 0.042656735
		 0.42985836 0.01759278 0.42459109 0.076705463 0.41578063 0.10007929 0.42855814 0.049787596
		 0.41753885 0.10664161 0.4246501 0.053823464 0.42826608 0.074456774 0.42767265 0.008887291
		 0.4191837 0.018369466 0.42777756 0.085154317 0.41608748 0.027123474 0.42826834 0.096004851
		 0.42054561 0.11134202 0.42014131 0.053807788 0.42396429 0.11248057 0.41650978 0.049445391
		 0.4266803 0.10942563 0.41470411 0.042569265 0.4281663 0.10400308 0.41457018 0.035127781
		 0.41756737 0.089739278 0.42514983 0.016534664 0.42056724 0.017229594 0.4204013 0.083661713
		 0.41627729 0.095917664 0.42894772 0.018767998 0.41617641 0.020576186 0.42406929 0.078638934
		 0.41644278 0.10269207 0.4321321 0.023955509 0.41790456 0.10853894 0.4337413 0.031457826
		 0.42777169 0.076223001 0.41186717 0.025617711 0.41669717 0.041707121 0.4277232 0.085930608
		 0.4216058 0.04647579 0.42777091 0.096610785 0.41988468 0.11071435 0.43340203 0.037456445
		 0.42232028 0.11035255 0.43163761 0.042603537 0.42417148 0.10837353 0.42945626 0.045558698
		 0.42631 0.10364822 0.42585322 0.047413073 0.41996536 0.10000664 0.42282012 0.045125246
		 0.42606506 0.043674782 0.4182063 0.095738418 0.42244771 0.1023296 0.41930595 0.043938018
		 0.42919162 0.040144674 0.41649541 0.090448059 0.42476448 0.10149823 0.41668728 0.040407047
		 0.42714062 0.098232076 0.41492614 0.033740923 0.41593805 0.084607743 0.43247125 0.034826197
		 0.42791578 0.021645248 0.41901055 0.08510083 0.42440203 0.019065231 0.42243299 0.08461003
		 0.42811093 0.09466213 0.4149802 0.028064944 0.42808005 0.091046527 0.416172 0.023515046
		 0.42740789 0.088564299 0.41765985 0.020820864 0.42582771 0.085741803 0.42031261 0.018760704
		 0.43167511 0.025254458 0.41186818 0.035215989 0.42301401 0.0083295628 0.4200677 0.016943999
		 0.42443702 0.017168298 0.41719291 0.019441769 0.41547462 0.022477552 0.42817524 0.019722514
		 0.43112651 0.02248501 0.43222103 0.037886739 0.42962721 0.041882478 0.41605404 0.04148344
		 0.41890422 0.045640454 0.42629525 0.045497373 0.42272767 0.046944872 0.42596963 0.049233362
		 0.42144194 0.048415326 0.42988446 0.047238998 0.43231627 0.043828316 0.43422905 0.038001865
		 0.43467394 0.031238347 0.4163107 0.04355517 0.41226301 0.0382194 0.41237929 0.022611566
		 0.41585675 0.018685564 0.43284866 0.022967443 0.42945942 0.017087407 0.42044821 0.015326604
		 0.42532215 0.014655516 0.41363332 0.035063796 0.41515234 0.026435286 0.41383889 0.043167636
		 0.41583398 0.050770998 0.4198803 0.055559307 0.42484024 0.055558518 0.41830108 0.017316006
		 0.42146596 0.0090003982 0.42916515 0.010157563 0.43082526 0.016986944 0.42914328
		 0.05123809 0.43198785 0.043638833 0.43241873 0.02614405 0.43290779 0.035747342 0.4140704
		 0.03413593 0.4140698 0.027604401;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 117 ".vt[0:116]"  -3.76390934 138.13368225 -0.35701975 -0.665061 137.84390259 -0.35701975
		 -1.57124233 138.42626953 -0.35701975 -2.71093655 138.50935364 -0.35701975 -4.19956875 133.88269043 -0.35701978
		 -2.4202795 134.093032837 -0.35701978 -3.4829452 132.68089294 -0.35701981 -4.53434849 135.15063477 -0.35701975
		 -1.33028698 135.097076416 -0.35701975 -4.65825939 136.35346985 -0.35701975 -0.57499218 135.9745636 -0.35701975
		 -0.35203838 136.90643311 -0.35701975 -4.50549221 137.29129028 -0.35701975 2.057592392 135.692276 -0.35701978
		 3.4212296 133.87081909 -0.35701978 3.42169666 134.66275024 -0.35701975 3.0066385269 135.30203247 -0.35701975
		 -1.38106823 133.18336487 -0.35701975 -0.072569847 131.94444275 -0.35701975 -1.72070205 131.80645752 -0.35701975
		 -0.72849941 134.30526733 -0.35701975 1.45977688 132.043579102 -0.35701975 0.10315229 135.20388794 -0.35701978
		 2.48341751 132.55978394 -0.35701978 3.14979839 133.25865173 -0.35701981 1.015841484 135.66650391 -0.35701981
		 4.45750332 130.56062317 -0.58338261 4.016903877 128.45993042 -0.58338261 4.47318172 128.92506409 -0.58338261
		 4.65825939 129.61853027 -0.58338261 1.22338009 131.17326355 -0.58338261 1.16319954 129.71655273 -0.58338261
		 0.23670673 130.46368408 -0.58338261 2.19526482 131.40901184 -0.58338261 1.86452293 128.94926453 -0.58338261
		 3.07964921 131.51811218 -0.58338261 2.79367828 128.32234192 -0.58338261 3.52884316 128.30053711 -0.58338261
		 3.97087979 131.22171021 -0.58338261 -4.44248676 136.34713745 0.58338273 -4.65825939 136.35346985 0.36939618
		 -4.32319736 135.18913269 0.58338273 -4.53434849 135.15063477 0.36939618 -4.30418873 137.19612122 0.58338273
		 -4.50549221 137.29129028 0.36939618 -3.63987041 137.95074463 0.58338273 -3.76390934 138.13368225 0.36939618
		 -3.46234226 133.064163208 0.58338273 -3.4829452 132.68089294 0.36939618 -2.57956791 134.23724365 0.58338273
		 -2.4202795 134.093032837 0.36939618 -2.68150997 138.29264832 0.58338273 -2.71093655 138.50935364 0.36939618
		 -1.64111614 138.21681213 0.58338273 -1.57124233 138.42626953 0.36939618 -0.84415919 137.70463562 0.58338273
		 -0.665061 137.84390259 0.36939618 -0.57439327 136.89674377 0.58338273 -0.35203838 136.90643311 0.36939618
		 -4.00035762787 133.96643066 0.58338273 -4.19956875 133.88269043 0.36939618 -0.77102947 136.074813843 0.58338273
		 -0.57499218 135.9745636 0.36939618 -1.48438168 135.24606323 0.58338273 -1.33028698 135.097076416 0.36939618
		 0.23413181 135.03036499 0.58338273 0.10315229 135.20388794 0.36939618 -0.55540562 134.17726135 0.58338273
		 -0.72849941 134.30526733 0.36939618 1.069466591 135.45378113 0.58338273 1.015841484 135.66650391 0.36939618
		 2.017861366 135.47723389 0.58338273 2.057592392 135.692276 0.36939618 -1.44156933 132.044555664 0.58338273
		 -1.72070205 131.80645752 0.36939618 -0.088406563 132.15785217 0.58338273 -0.072569847 131.94444275 0.36939618
		 2.86351585 135.12950134 0.58338273 3.0066385269 135.30203247 0.36939618 3.20767498 134.59942627 0.58338273
		 3.42169666 134.66275024 0.36939618 3.20726967 133.91619873 0.58338273 3.4212296 133.87081909 0.36939618
		 2.96925735 133.37939453 0.58338273 3.14979839 133.25865173 0.36939618 -1.1806612 133.10231018 0.58338273
		 -1.38106823 133.18336487 0.36939618 2.35405827 132.73420715 0.58338273 2.48341751 132.55978394 0.36939618
		 1.40240192 132.25430298 0.58338273 1.45977688 132.043579102 0.36939618 3.057929993 131.29981995 0.35701981
		 3.07964921 131.51811218 0.1430333 2.2337141 131.19815063 0.35701981 2.19526482 131.40901184 0.1430333
		 3.8388443 131.040100098 0.35701981 3.97087979 131.22171021 0.1430333 4.25782776 130.47090149 0.35701981
		 4.45750332 130.56062317 0.1430333 0.58967304 130.45394897 0.35701981 0.23670673 130.46368408 0.1430333
		 1.31017983 129.8729248 0.35701981 1.16319954 129.71655273 0.1430333 4.43827629 129.62413025 0.35701981
		 4.65825939 129.61853027 0.1430333 4.2809639 129.034698486 0.35701981 4.47318172 128.92506409 0.1430333
		 3.9007616 128.64712524 0.35701981 4.016903877 128.45993042 0.1430333 3.49788284 128.51551819 0.35701981
		 3.52884316 128.30053711 0.1430333 1.31441021 130.97515869 0.35701981 1.22338009 131.17326355 0.1430333
		 2.86198425 128.53442383 0.35701981 2.79367828 128.32234192 0.1430333 2.0053021908 129.1124115 0.35701981
		 1.86452293 128.94926453 0.1430333;
	setAttr -s 225 ".ed";
	setAttr ".ed[0:165]"  0 1 1 2 1 1 3 2 1 0 3 1 4 5 1 4 6 1 6 5 1 7 8 1 7 4 1
		 5 8 1 9 10 1 9 7 1 10 8 1 11 10 1 12 11 1 9 12 1 1 11 1 12 0 1 13 14 1 15 14 1 16 15 1
		 13 16 1 17 18 1 17 19 1 19 18 1 20 21 1 20 17 1 18 21 1 22 23 1 22 20 1 23 21 1 24 23 1
		 25 24 1 22 25 1 14 24 1 25 13 1 26 27 1 28 27 1 29 28 1 26 29 1 30 31 1 30 32 1 32 31 1
		 33 34 1 33 30 1 31 34 1 35 36 1 35 33 1 36 34 1 37 36 1 38 37 1 35 38 1 27 37 1 38 26 1
		 39 40 1 40 42 1 42 41 1 41 39 1 39 43 1 43 44 1 44 40 1 42 60 1 60 59 1 59 41 1 43 45 1
		 45 46 1 46 44 1 45 51 1 51 52 1 52 46 1 47 48 1 48 50 1 50 49 1 49 47 1 47 59 1 60 48 1
		 50 64 1 64 63 1 63 49 1 51 53 1 53 54 1 54 52 1 53 55 1 55 56 1 56 54 1 55 57 1 57 58 1
		 58 56 1 57 61 1 61 62 1 62 58 1 61 63 1 64 62 1 65 66 1 66 68 1 68 67 1 67 65 1 65 69 1
		 69 70 1 70 66 1 68 86 1 86 85 1 85 67 1 69 71 1 71 72 1 72 70 1 71 77 1 77 78 1 78 72 1
		 73 74 1 74 76 1 76 75 1 75 73 1 73 85 1 86 74 1 76 90 1 90 89 1 89 75 1 77 79 1 79 80 1
		 80 78 1 79 81 1 81 82 1 82 80 1 81 83 1 83 84 1 84 82 1 83 87 1 87 88 1 88 84 1 87 89 1
		 90 88 1 91 92 1 92 94 1 94 93 1 93 91 1 91 95 1 95 96 1 96 92 1 94 112 1 112 111 1
		 111 93 1 95 97 1 97 98 1 98 96 1 97 103 1 103 104 1 104 98 1 99 100 1 100 102 1 102 101 1
		 101 99 1 99 111 1 112 100 1 102 116 1 116 115 1 115 101 1 103 105 1 105 106 1 106 104 1
		 105 107 1 107 108 1 108 106 1 107 109 1 109 110 1 110 108 1;
	setAttr ".ed[166:224]" 109 113 1 113 114 1 114 110 1 113 115 1 116 114 1 45 55 1
		 49 59 1 63 41 1 61 39 1 57 43 1 71 81 1 75 85 1 89 67 1 87 65 1 83 69 1 97 107 1
		 101 111 1 115 93 1 113 91 1 109 95 1 56 1 1 2 54 1 3 52 1 0 46 1 60 4 1 6 48 1 5 50 1
		 42 7 1 8 64 1 40 9 1 10 62 1 11 58 1 44 12 1 82 14 1 15 80 1 16 78 1 13 72 1 86 17 1
		 19 74 1 18 76 1 68 20 1 21 90 1 66 22 1 23 88 1 24 84 1 70 25 1 108 27 1 28 106 1
		 29 104 1 26 98 1 112 30 1 32 100 1 31 102 1 94 33 1 34 116 1 92 35 1 36 114 1 37 110 1
		 96 38 1;
	setAttr -s 114 -ch 450 ".fc[0:113]" -type "polyFaces" 
		f 4 3 2 1 -1
		mu 0 4 0 1 2 3
		f 3 -7 -6 4
		mu 0 3 4 5 6
		f 4 -10 -5 -9 7
		mu 0 4 7 4 6 8
		f 4 12 -8 -12 10
		mu 0 4 9 7 8 10
		f 4 -11 15 14 13
		mu 0 4 9 10 11 12
		f 4 17 0 16 -15
		mu 0 4 11 0 3 12
		f 4 21 20 19 -19
		mu 0 4 13 14 15 16
		f 3 -25 -24 22
		mu 0 3 17 18 19
		f 4 -28 -23 -27 25
		mu 0 4 20 17 19 21
		f 4 30 -26 -30 28
		mu 0 4 22 20 21 23
		f 4 -29 33 32 31
		mu 0 4 22 23 24 25
		f 4 35 18 34 -33
		mu 0 4 24 13 16 25
		f 4 39 38 37 -37
		mu 0 4 26 27 28 29
		f 3 -43 -42 40
		mu 0 3 30 31 32
		f 4 -46 -41 -45 43
		mu 0 4 33 30 32 34
		f 4 48 -44 -48 46
		mu 0 4 35 33 34 36
		f 4 -47 51 50 49
		mu 0 4 35 36 37 38
		f 4 53 36 52 -51
		mu 0 4 37 26 29 38
		f 4 54 55 56 57
		mu 0 4 159 40 41 158
		f 4 -55 58 59 60
		mu 0 4 40 159 157 44
		f 4 -57 61 62 63
		mu 0 4 158 41 45 155
		f 4 -60 64 65 66
		mu 0 4 44 157 156 48
		f 4 -66 67 68 69
		mu 0 4 48 156 151 50
		f 4 70 71 72 73
		mu 0 4 153 119 53 152
		f 4 -71 74 -63 75
		mu 0 4 52 154 155 45
		f 4 -73 76 77 78
		mu 0 4 152 53 55 147
		f 4 -69 79 80 81
		mu 0 4 50 151 150 58
		f 4 -81 82 83 84
		mu 0 4 58 150 149 60
		f 4 -84 85 86 87
		mu 0 4 60 149 148 62
		f 4 -87 88 89 90
		mu 0 4 62 148 146 64
		f 4 -90 91 -78 92
		mu 0 4 64 146 147 55
		f 4 93 94 95 96
		mu 0 4 145 66 67 144
		f 4 -94 97 98 99
		mu 0 4 66 145 143 70
		f 4 -96 100 101 102
		mu 0 4 144 67 71 141
		f 4 -99 103 104 105
		mu 0 4 70 143 142 74
		f 4 -105 106 107 108
		mu 0 4 74 142 137 76
		f 4 109 110 111 112
		mu 0 4 139 118 79 138
		f 4 -110 113 -102 114
		mu 0 4 78 140 141 71
		f 4 -112 115 116 117
		mu 0 4 138 79 81 133
		f 4 -108 118 119 120
		mu 0 4 76 137 136 84
		f 4 -120 121 122 123
		mu 0 4 84 136 135 86
		f 4 -123 124 125 126
		mu 0 4 86 135 134 88
		f 4 -126 127 128 129
		mu 0 4 88 134 132 90
		f 4 -129 130 -117 131
		mu 0 4 90 132 133 81
		f 4 132 133 134 135
		mu 0 4 131 92 93 130
		f 4 -133 136 137 138
		mu 0 4 92 131 129 96
		f 4 -135 139 140 141
		mu 0 4 130 93 97 127
		f 4 -138 142 143 144
		mu 0 4 96 129 128 100
		f 4 -144 145 146 147
		mu 0 4 100 128 160 102
		f 4 148 149 150 151
		mu 0 4 125 117 105 124
		f 4 -149 152 -141 153
		mu 0 4 104 126 127 97
		f 4 -151 154 155 156
		mu 0 4 124 105 107 121
		f 4 -147 157 158 159
		mu 0 4 102 160 161 110
		f 4 -159 160 161 162
		mu 0 4 110 161 123 112
		f 4 -162 163 164 165
		mu 0 4 112 123 122 114
		f 4 -165 166 167 168
		mu 0 4 114 122 120 116
		f 4 -168 169 -156 170
		mu 0 4 116 120 121 107
		f 4 171 -83 -80 -68
		mu 0 4 47 59 57 49
		f 3 172 -75 -74
		mu 0 3 54 46 51
		f 4 173 -64 -173 -79
		mu 0 4 56 42 46 54
		f 4 174 -58 -174 -92
		mu 0 4 63 39 42 56
		f 4 -89 175 -59 -175
		mu 0 4 63 61 43 39
		f 4 -176 -86 -172 -65
		mu 0 4 43 61 59 47
		f 4 176 -122 -119 -107
		mu 0 4 73 85 83 75
		f 3 177 -114 -113
		mu 0 3 80 72 77
		f 4 178 -103 -178 -118
		mu 0 4 82 68 72 80
		f 4 179 -97 -179 -131
		mu 0 4 89 65 68 82
		f 4 -128 180 -98 -180
		mu 0 4 89 87 69 65
		f 4 -181 -125 -177 -104
		mu 0 4 69 87 85 73
		f 4 181 -161 -158 -146
		mu 0 4 99 111 109 101
		f 3 182 -153 -152
		mu 0 3 106 98 103
		f 4 183 -142 -183 -157
		mu 0 4 108 94 98 106
		f 4 184 -136 -184 -170
		mu 0 4 115 91 94 108
		f 4 -167 185 -137 -185
		mu 0 4 115 113 95 91
		f 4 -186 -164 -182 -143
		mu 0 4 95 113 111 99
		f 4 186 -2 187 -85
		mu 0 4 60 3 2 58
		f 4 -188 -3 188 -82
		mu 0 4 58 2 1 50
		f 4 -189 -4 189 -70
		mu 0 4 50 1 0 48
		f 4 190 5 191 -76
		mu 0 4 45 6 5 52
		f 4 -192 6 192 -72
		mu 0 4 119 5 4 53
		f 4 193 8 -191 -62
		mu 0 4 41 8 6 45
		f 4 -193 9 194 -77
		mu 0 4 53 4 7 55
		f 4 195 11 -194 -56
		mu 0 4 40 10 8 41
		f 4 -195 -13 196 -93
		mu 0 4 55 7 9 64
		f 4 -197 -14 197 -91
		mu 0 4 64 9 12 62
		f 4 198 -16 -196 -61
		mu 0 4 44 11 10 40
		f 4 -198 -17 -187 -88
		mu 0 4 62 12 3 60
		f 4 -190 -18 -199 -67
		mu 0 4 48 0 11 44
		f 4 199 -20 200 -124
		mu 0 4 86 16 15 84
		f 4 -201 -21 201 -121
		mu 0 4 84 15 14 76
		f 4 -202 -22 202 -109
		mu 0 4 76 14 13 74
		f 4 203 23 204 -115
		mu 0 4 71 19 18 78
		f 4 -205 24 205 -111
		mu 0 4 118 18 17 79
		f 4 206 26 -204 -101
		mu 0 4 67 21 19 71
		f 4 -206 27 207 -116
		mu 0 4 79 17 20 81
		f 4 208 29 -207 -95
		mu 0 4 66 23 21 67
		f 4 -208 -31 209 -132
		mu 0 4 81 20 22 90
		f 4 -210 -32 210 -130
		mu 0 4 90 22 25 88
		f 4 211 -34 -209 -100
		mu 0 4 70 24 23 66
		f 4 -211 -35 -200 -127
		mu 0 4 88 25 16 86
		f 4 -203 -36 -212 -106
		mu 0 4 74 13 24 70
		f 4 212 -38 213 -163
		mu 0 4 112 29 28 110
		f 4 -214 -39 214 -160
		mu 0 4 110 28 27 102
		f 4 -215 -40 215 -148
		mu 0 4 102 27 26 100
		f 4 216 41 217 -154
		mu 0 4 97 32 31 104
		f 4 -218 42 218 -150
		mu 0 4 117 31 30 105
		f 4 219 44 -217 -140
		mu 0 4 93 34 32 97
		f 4 -219 45 220 -155
		mu 0 4 105 30 33 107
		f 4 221 47 -220 -134
		mu 0 4 92 36 34 93
		f 4 -221 -49 222 -171
		mu 0 4 107 33 35 116
		f 4 -223 -50 223 -169
		mu 0 4 116 35 38 114
		f 4 224 -52 -222 -139
		mu 0 4 96 37 36 92
		f 4 -224 -53 -213 -166
		mu 0 4 114 38 29 112
		f 4 -216 -54 -225 -145
		mu 0 4 100 26 37 96;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Joy" -p "C000_Generic_01_PopUp";
	rename -uid "95032F3F-426F-E64B-8FC2-369147831ADC";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 4.76837158203125e-07 133.40494537353516 0 ;
	setAttr ".sp" -type "double3" 4.76837158203125e-07 133.40494537353516 0 ;
createNode mesh -n "JoyShape" -p "Joy";
	rename -uid "B97D8550-4DCA-094B-AD5C-A793BAEF9566";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.59519696235656738 0.032434791326522827 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dr" 1;
	setAttr ".vcs" 2;
createNode mesh -n "JoyShapeOrig" -p "Joy";
	rename -uid "6A06BBE5-4D71-8BEA-693D-F997AD10EB62";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 516 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" 0.38318938 0.03488043 0.38211736
		 0.032521933 0.38443172 0.026343584 0.39900619 0.021504432 0.40007764 0.023843944
		 0.39765522 0.027058154 0.38859016 0.012362659 0.39021087 0.010938957 0.39114052 0.016342461
		 0.39063197 0.047315836 0.38867837 0.049005032 0.38675469 0.042254925 0.39826137 0.044103503
		 0.39744923 0.046979249 0.39481726 0.042254329 0.40056401 0.026940525 0.40030283 0.030422747
		 0.39944106 0.033498019 0.39613539 0.048949301 0.39420125 0.049682736 0.39270443 0.049136817
		 0.38283989 0.038722932 0.38527566 0.018044561 0.38691181 0.017428637 0.39213163 0.011082843
		 0.39364645 0.012977362 0.39480254 0.016085058 0.39572924 0.019271702 0.39734551 0.019991875
		 0.39828914 0.036131948 0.39852208 0.040234089 0.38291582 0.04329133 0.38503462 0.048922777
		 0.38357255 0.046542764 0.3867895 0.049646258 0.38165128 0.022199094 0.3833127 0.019512862
		 0.38104343 0.025369555 0.38118953 0.029026151 0.38739198 0.015038908 0.39045924 0.031985819
		 0.39305127 0.035306871 0.39128712 0.037678599 0.39090797 0.03066957 0.38851389 0.024973214
		 0.38873759 0.023650646 0.39052761 0.02419436 0.39445361 0.035169363 0.39414811 0.036505878
		 0.39416081 0.024797082 0.39476383 0.025895894 0.39395294 0.027788013 0.38750744 0.033516705
		 0.38677496 0.032432199 0.38771668 0.029355288 0.38970965 0.039114654 0.3889575 0.038933516
		 0.38936827 0.036021054 0.39359769 0.037568033 0.3928324 0.038163602 0.39202994 0.03815037
		 0.38828176 0.038234413 0.38770548 0.036852121 0.38749489 0.035554051 0.38765201 0.025372982
		 0.39244032 0.023225725 0.39284942 0.024463922 0.39515299 0.027528822 0.39513034 0.029209375
		 0.39476854 0.03083244 0.39429742 0.032166898 0.39446893 0.033565819 0.39054143 0.038669646
		 0.38677201 0.026477784 0.38612235 0.02947548 0.38628572 0.027765363 0.386305 0.031060934
		 0.39078319 0.021275908 0.39171991 0.021962732 0.38998884 0.021459848 0.38924751 0.022266209
		 0.39341292 0.024362475 0.39011052 0.026043497 0.39210322 0.025369428 0.39106157 0.031738624
		 0.39202419 0.038545713 0.39157143 0.039517179 0.39012599 0.03764616 0.3888692 0.025062822
		 0.38939527 0.024143569 0.38709298 0.034283295 0.3867847 0.032859251 0.3878583 0.031854346
		 0.39456597 0.031929925 0.3949891 0.033443585 0.39357167 0.03537254 0.39375186 0.02535852
		 0.39436829 0.026102565 0.39344215 0.028306082 0.39007977 0.023654841 0.39085892 0.023739181
		 0.39155152 0.024379425 0.39481696 0.027235769 0.39504573 0.028883688 0.39497438 0.030173078
		 0.39285004 0.038873032 0.38827923 0.036992267 0.38816586 0.035598233 0.3867667 0.031139903
		 0.38711539 0.029701933 0.38774684 0.028578661 0.38841668 0.027789906 0.38854194 0.026441589
		 0.39294386 0.025094084 0.39382917 0.038605168 0.39497802 0.036517099 0.39450237 0.037870839
		 0.39512894 0.03500025 0.38933423 0.039977923 0.38865712 0.038650438 0.39005843 0.040438786
		 0.39085844 0.040318295 0.38765696 0.035245642 0.38513455 0.090702713 0.38518044 0.094308674
		 0.29327589 0.032413751 0.38677308 0.076961622 0.38981447 0.083707929 0.29678071 0.022722304
		 0.39245674 0.085876524 0.39532885 0.084235013 0.30162209 0.02584511 0.3875266 0.084930152
		 0.39043757 0.085976481 0.38746741 0.087608367 0.38602874 0.089736462 0.38601384 0.095179319
		 0.3865428 0.10072893 0.38837793 0.10253209 0.2962575 0.042147279 0.38664934 0.098231405
		 0.38941553 0.10145819 0.3878167 0.089789599 0.39066264 0.088122964 0.39195764 0.10114235
		 0.39314494 0.098005235 0.30172604 0.039066404 0.39096761 0.10055473 0.39260933 0.09563458
		 0.39253458 0.092447609 0.39136481 0.087086648 0.39345667 0.08983779 0.38751534 0.095361918
		 0.3901355 0.099128395 0.3914907 0.093471497 0.29800814 0.03272453 0.38117135 0.09208262
		 0.38632223 0.10672212 0.39492548 0.10232526 0.39067432 0.080609754 0.38547677 0.013524026
		 0.38437229 0.015418857 0.39261946 0.078317389 0.39063928 0.076772645 0.38663727 0.012308747
		 0.38235331 0.017358482 0.3948878 0.077291623 0.39518154 0.092819422 0.38091815 0.036229432
		 0.38137168 0.039499104 0.39726719 0.095662773 0.39711639 0.09063682 0.38059136 0.033049613
		 0.39853805 0.087344587 0.37975448 0.028954327 0.38044974 0.020632923 0.39745721 0.078923985
		 0.37962544 0.024569482 0.39859253 0.082813367 0.38384482 0.085083783 0.3970221 0.015644908
		 0.39577502 0.013584256 0.38363048 0.080698863 0.38177142 0.085270137 0.39837974 0.017587632
		 0.37982824 0.086562812 0.40014523 0.019716799 0.38359269 0.099856168 0.40047687 0.037118882
		 0.40090641 0.03425619 0.38144609 0.099541515 0.38287303 0.10492516 0.39995807 0.041310668
		 0.40170383 0.030761063 0.37972391 0.097818404 0.37867856 0.089755595 0.40141115 0.02263841
		 0.37856987 0.09405607 0.401997 0.026542664 0.38974342 0.073433593 0.38814896 0.0096515417
		 0.39437196 0.010525227 0.38378188 0.076359674 0.38772199 0.071802124 0.39011472 0.0079805106
		 0.38514861 0.072762474 0.39251798 0.0083143711 0.38161206 0.044476748 0.39859146
		 0.10004359 0.39075789 0.10478711 0.39076835 0.051885009 0.39279824 0.052061677 0.38998577
		 0.11026871 0.3929114 0.10836369 0.38851422 0.051984549 0.39495373 0.10962147 0.38635951
		 0.052419543 0.38245925 0.04836756 0.39857107 0.10439318 0.38425487 0.051407814 0.39706275
		 0.10831702 0.383167 0.1093533 0.3995046 0.045644879 0.39450285 0.052406728 0.38888064
		 0.11265624 0.38452706 0.11246598 0.39847916 0.049096048 0.38654622 0.11387688 0.39681754
		 0.051504672 0.3892808 0.08883357 0.39393485 0.020694405 0.39318377 0.020289242 0.39052278
		 0.087369859 0.389258 0.086321652 0.39439219 0.021692276 0.39215273 0.019358397 0.39155769
		 0.086901903 0.39131707 0.094115913 0.38703784 0.021709204 0.38652626 0.023180634
		 0.39258856 0.095849335 0.39253497 0.092742205 0.38778594 0.020968705 0.39316532 0.091282189
		 0.38872367 0.01974979 0.39088118 0.018696159 0.39269793 0.087626308 0.3897658 0.018841207
		 0.3931891 0.089309007 0.3863343 0.090720743;
	setAttr ".uvst[0].uvsp[250:499]" 0.39633775 0.032987356 0.39637399 0.031278491
		 0.3862088 0.08814919 0.38511819 0.090830058 0.39601186 0.034578741 0.38424876 0.091408461
		 0.39563906 0.036536992 0.38625139 0.09725076 0.39169568 0.04180944 0.3924312 0.041186631
		 0.38497543 0.09706372 0.3858372 0.10016733 0.39059222 0.041773856 0.39335144 0.040646613
		 0.38421395 0.096301854 0.38375548 0.092778116 0.39513898 0.038265824 0.38370824 0.094652951
		 0.39434752 0.039706111 0.38887444 0.084892273 0.39517447 0.022951752 0.39648092 0.029196799
		 0.38627797 0.086162239 0.38800132 0.084187508 0.39593151 0.024564385 0.38686755 0.084610581
		 0.39641115 0.026954591 0.38565868 0.024989873 0.39318931 0.097836792 0.3894105 0.099336922
		 0.38558418 0.035620987 0.38624492 0.037187457 0.38895527 0.10256946 0.39069062 0.10146278
		 0.3853139 0.033440709 0.39159936 0.10202241 0.38495901 0.031396449 0.3850835 0.026832759
		 0.39318046 0.099729836 0.3848111 0.029210955 0.39251751 0.10145456 0.38596863 0.10214674
		 0.3894617 0.041795135 0.38670975 0.038582206 0.38848418 0.10358709 0.38656363 0.10350829
		 0.38844872 0.04139781 0.38745013 0.10412782 0.38752434 0.040356696 0.39004558 0.087008163
		 0.38650504 0.037999317 0.38707504 0.038934961 0.39119726 0.085650757 0.39002448 0.084679708
		 0.38630286 0.036780253 0.3877826 0.04054831 0.39216298 0.085213944 0.39194638 0.09194348
		 0.39266026 0.042491138 0.39338982 0.041622236 0.39312637 0.093552001 0.39307588 0.090669252
		 0.39186957 0.042549491 0.39366466 0.089305803 0.3908222 0.042880356 0.38875154 0.042116076
		 0.3932277 0.085890338 0.38974419 0.042858779 0.39368671 0.08746247 0.38729247 0.088772729
		 0.3868244 0.025504045 0.38645843 0.026951306 0.38717589 0.086384699 0.38616315 0.088874355
		 0.38741568 0.024380259 0.38535136 0.089414433 0.38811779 0.022972628 0.38721451 0.094870962
		 0.39255312 0.02150704 0.39179698 0.021468453 0.3860299 0.094697423 0.38682994 0.097580232
		 0.39350009 0.022394501 0.39089683 0.021209583 0.38531882 0.093985982 0.3848905 0.090694405
		 0.38888672 0.02186577 0.38484627 0.092445828 0.38985223 0.021239363 0.3896659 0.083343938
		 0.38586774 0.035083786 0.38595569 0.028664492 0.3872405 0.084530637 0.38885003 0.082685508
		 0.38552508 0.033099011 0.38779125 0.083080724 0.3855761 0.030657127 0.39449528 0.040743679
		 0.39368713 0.095406927 0.39016491 0.096820839 0.39662418 0.031609014 0.39636099 0.029740587
		 0.3897422 0.099822439 0.39135349 0.098794438 0.3964358 0.033705518 0.39220196 0.099316902
		 0.39634854 0.035750821 0.39535359 0.039602116 0.3936789 0.097175397 0.39605266 0.037757471
		 0.39305973 0.098786332 0.38695261 0.099428304 0.39448252 0.023251198 0.39623374 0.028171346
		 0.38930207 0.10077365 0.38750848 0.10070011 0.3952814 0.024381183 0.38833636 0.1012786
		 0.3958776 0.026000969 0.39178503 0.089903861 0.38478312 0.093785018 0.38755363 0.086306661
		 0.39158547 0.098850667 0.38733056 0.10102522 0.38851759 0.094109297 0.39237458 0.088018842
		 0.38585168 0.091635123 0.38843268 0.084667966 0.39218891 0.096353807 0.38822514 0.098379947
		 0.3893308 0.091936931 0.38512161 0.030539736 0.38551924 0.028479569 0.39075175 0.043795884
		 0.38963094 0.043637455 0.39674494 0.036110803 0.39642 0.038205102 0.39626771 0.025508247
		 0.39662668 0.027777508 0.38974038 0.020339899 0.39082912 0.020329997 0.39558655 0.023831688
		 0.39477977 0.02253177 0.39673802 0.029280268 0.39377421 0.021685444 0.39569885 0.040217116
		 0.39478722 0.041406438 0.39683869 0.034050241 0.39723551 0.031538472 0.39369565 0.042283759
		 0.38512126 0.033139691 0.38541153 0.035250053 0.38600695 0.026726954 0.38586286 0.036855504
		 0.38873044 0.021115236 0.38789514 0.022148803 0.39170638 0.020575516 0.3926692 0.020329669
		 0.38719133 0.023583733 0.38636425 0.0247766 0.38855922 0.042942435 0.38755348 0.041315824
		 0.39178911 0.043421268 0.39282358 0.043756664 0.3868542 0.039725617 0.38589394 0.038693145
		 0.39687753 0.0266698 0.39694411 0.028991163 0.38859296 0.018799514 0.38970631 0.017987728
		 0.38449618 0.031391144 0.38435739 0.02909714 0.38725388 0.041175842 0.38641536 0.039307833
		 0.39465365 0.040478826 0.39361095 0.041437984 0.38827282 0.042196512 0.38932985 0.042752147
		 0.38598081 0.037964344 0.39048061 0.04270041 0.38461405 0.026538938 0.38523018 0.024605185
		 0.38484806 0.033455133 0.38500431 0.03622508 0.38608474 0.022809684 0.39631397 0.024172813
		 0.39558139 0.022394121 0.39686024 0.031097472 0.39480373 0.021238387 0.39545476 0.038855731
		 0.39603475 0.037141979 0.39271587 0.041970789 0.39184132 0.043055534 0.39640298 0.035156548
		 0.39694434 0.033289611 0.39088675 0.017726749 0.39220658 0.018413931 0.38767472 0.020052373
		 0.3866007 0.020622492 0.39322451 0.019329697 0.39437789 0.019484937 0.39262837 0.0073457509
		 0.39456543 0.0096234232 0.3792569 0.028882712 0.37917539 0.024300426 0.38618702 0.053327382
		 0.38398844 0.052216291 0.39705965 0.052386403 0.39466822 0.053329468 0.40249467 0.02637887
		 0.40219438 0.030768454 0.39880461 0.049785614 0.3999266 0.046202362 0.39296645 0.052968502
		 0.40038913 0.041801453 0.38208508 0.049036682 0.3811869 0.044957578 0.38837153 0.052916825
		 0.39078969 0.052841485 0.38094515 0.04001987 0.39009953 0.0070406049 0.38802058 0.0086855888
		 0.39599174 0.012664899 0.38652045 0.011363223 0.40184158 0.022267938 0.4005565 0.019132733
		 0.40140501 0.034243494 0.40099075 0.037295163 0.39877039 0.016960919 0.39735362 0.014806092
		 0.38002837 0.02011469 0.38197872 0.016710877 0.3801018 0.032989681 0.38040632 0.03644526
		 0.38397747 0.014795333 0.38519591 0.012515098 0.30192107 0.028624564 0.30110127 0.031365573
		 0.30077422 0.024828494 0.39326391 0.087019593 0.3000997 0.032544494 0.29973182 0.026200294
		 0.29984722 0.039683253 0.29896384 0.038388044 0.30129665 0.034530431 0.30192047 0.036811769
		 0.30085623 0.040118605 0.39286527 0.10022491 0.29833478 0.040819287 0.29734135 0.042047143;
	setAttr ".uvst[0].uvsp[500:515]" 0.2954554 0.038023353 0.29620951 0.035032064
		 0.38729283 0.1024673 0.29544395 0.040528625 0.29470617 0.035078049 0.29384261 0.034336865
		 0.29451448 0.029651314 0.29629838 0.029432803 0.38468823 0.092304051 0.29365987 0.030750036
		 0.29876572 0.02523464 0.29907149 0.027339727 0.2958675 0.027311951 0.29582483 0.024633795
		 0.29805851 0.023068339 0.38855276 0.083168536;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 381 ".vt";
	setAttr ".vt[0:165]"  2.74890518 137.85079956 0.38367072 5.70806503 136.01071167 0.38367072
		 5.043987274 132.61805725 0.38367072 1.53713787 132.26100159 0.38367072 -0.065811157 135.506073 0.38367072
		 1.17987251 134.88301086 0.38367072 4.9026413 135.58633423 0.38367072 4.59018707 133.39555359 0.38367072
		 2.032600403 133.094451904 0.38367072 2.86978531 136.48628235 0.38367072 2.18945694 134.11776733 0.38367072
		 3.24725723 133.8551178 0.38367072 4.31665802 134.44448853 0.38367072 3.52665329 135.42121887 0.38367072
		 2.45036316 135.24240112 0.38367072 1.49952304 135.30137634 0.38367072 1.3126297 134.39859009 0.38367072
		 2.018714905 135.35403442 0.38367072 1.7673111 134.18148804 0.38367072 2.56845093 136.29507446 0.38367072
		 3.27027893 136.31710815 0.38367072 2.40045929 135.9367981 0.38367072 3.4579277 136.0028381348 0.38367072
		 4.54818726 135.8586731 0.38367072 4.93925476 135.16529846 0.38367072 4.065162659 135.7895813 0.38367072
		 4.75350952 134.75009155 0.38367072 4.16498947 133.26229858 0.38367072 4.74840546 133.7585144 0.38367072
		 3.6924057 133.44425964 0.38367072 4.6122818 134.13685608 0.38367072 2.0035896301 133.83340454 0.38367072
		 3.071376801 133.43800354 0.38367072 1.79258335 133.39555359 0.38367072 2.58457184 133.050750732 0.38367072
		 3.17405319 134.66726685 0.38367072 -6.54154205 139.39405823 0.38367084 -5.14834499 138.52772522 0.38367084
		 -5.46099854 136.93041992 0.38367084 -7.11205387 136.7623291 0.38367084 -7.86673641 138.29011536 0.38367084
		 -6.40285254 138.015640259 0.38367084 6.25473404 130.20155334 0.38367084 7.6631813 129.32571411 0.38367084
		 7.34710693 127.71095276 0.38367084 5.67797852 127.54101563 0.38367084 4.91503143 129.085510254 0.38367084
		 6.39494371 128.80804443 0.38367084 1.53713787 132.26100159 -0.38367078 3.22967124 132.13772583 -0.38367078
		 2.94081497 131.54977417 -0.38367078 1.51769638 138.39553833 -0.38367078 2.74890518 137.85079956 -0.38367078
		 2.18295288 138.93466187 -0.38367078 -0.79535675 134.20236206 -0.38367078 -0.065811157 135.506073 -0.38367078
		 -1.19791794 135.056411743 -0.38367078 5.043987274 132.61805725 -0.38367078 5.69041443 134.20024109 -0.38367084
		 6.29978561 133.5459137 -0.38367084 6.20452881 137.40866089 -0.38367081 5.70806503 136.01071167 -0.38367078
		 6.90484285 136.86367798 -0.38367078 3.10419083 139.033950806 -0.38367078 3.93758368 138.58584595 -0.38367078
		 4.34575272 137.87417603 -0.38367078 7.2555809 136.017669678 -0.38367081 7.052792072 135.011260986 -0.38367081
		 6.55923843 134.49923706 -0.38367078 3.70450211 131.51980591 -0.38367078 0.18671417 133.29527283 -0.38367078
		 0.48497581 133.87435913 -0.38367081 -1.05563736 136.16557312 -0.38367078 -0.31072617 136.80154419 -0.38367078
		 0.58464241 136.91543579 -0.38367078 1.29990959 136.88644409 -0.38367078 1.29183578 137.56069946 -0.38367078
		 4.43490982 137.19247437 -0.38367078 5.26324081 137.47950745 -0.38367081 4.64999008 131.019271851 -0.38367081
		 6.38644791 131.77334595 -0.38367078 5.58506775 131.081283569 -0.38367081 6.6152916 132.69642639 -0.38367078
		 0.43558502 131.27027893 -0.38367084 0.027275085 132.34054565 -0.38367084 1.30361557 130.82772827 -0.38367078
		 2.2765274 130.90661621 -0.38367078 -0.046607971 133.85379028 -0.38367084 3.15326691 134.67294312 -0.38367078
		 -6.40285254 138.015640259 -0.38367066 -6.54154205 139.39405823 -0.38367066 -5.747756 139.084091187 -0.38367066
		 -7.11205387 136.7623291 -0.38367066 -6.31519413 136.70429993 -0.38367066 -6.45118856 136.42747498 -0.38367066
		 -7.12120628 139.6505127 -0.38367072 -6.80799866 139.90435791 -0.38367072 -8.21021175 137.67633057 -0.38367066
		 -7.86673641 138.29011536 -0.3836706 -8.39974117 138.078414917 -0.38367066 -5.46099854 136.93041992 -0.38367066
		 -5.1566534 137.67532349 -0.38367069 -4.86975765 137.36729431 -0.38367066 -4.91460323 139.18589783 -0.38367066
		 -5.14834499 138.52772522 -0.38367066 -4.58489132 138.92929077 -0.38367066 -6.37427139 139.95108032 -0.38367066
		 -5.98190212 139.74009705 -0.38367066 -5.78973389 139.40505981 -0.38367066 -4.4197607 138.5309906 -0.38367069
		 -4.51523495 138.057159424 -0.38367069 -4.74760342 137.81608582 -0.38367069 -6.091639519 136.4133606 -0.38367066
		 -7.74784374 137.24926758 -0.38367066 -7.6074214 137.52191162 -0.38367066 -8.33275509 138.60063171 -0.38367066
		 -7.98204327 138.90003967 -0.38367066 -7.56049585 138.95365906 -0.38367069 -7.22374249 138.94004822 -0.38367069
		 -7.22754383 139.25747681 -0.38367066 -5.35777187 139.21925354 -0.38367066 -5.64649487 136.17770386 -0.38367066
		 -4.82895565 136.53269958 -0.38367066 -5.2062521 136.20690918 -0.38367066 -4.72121334 136.96731567 -0.38367066
		 -7.63067532 136.2959137 -0.38367069 -7.82290936 136.79978943 -0.38367066 -7.22199774 136.087524414 -0.38367072
		 -6.76394176 136.12464905 -0.38367066 -7.8576951 137.51220703 -0.38367066 6.39494371 128.80804443 -0.38367066
		 6.25473404 130.20155334 -0.38367066 7.057209492 129.88819885 -0.38367066 5.67797852 127.54101563 -0.38367066
		 6.48355865 127.48232269 -0.38367066 6.34607649 127.20246124 -0.38367066 5.66872406 130.46080017 -0.38367066
		 5.98536301 130.71740723 -0.38367066 4.56779861 128.46499634 -0.38367066 4.91503143 129.085510254 -0.38367066
		 4.376194 128.87150574 -0.38367066 7.34710693 127.71095276 -0.38367066 7.65478563 128.463974 -0.38367066
		 7.94481993 128.15257263 -0.38367066 7.89948273 129.99110413 -0.38367066 7.6631813 129.32571411 -0.38367066
		 8.23280334 129.73167419 -0.38367066 6.42383528 130.76464844 -0.38367066 6.82049942 130.55137634 -0.38367066
		 7.014774323 130.21266174 -0.38367066 8.39974213 129.32902527 -0.38367066 8.30322266 128.8500061 -0.38367066
		 8.068313599 128.60630798 -0.38367066 6.70956087 127.18820953 -0.38367066 5.035228729 128.033279419 -0.38367066
		 5.17718887 128.30891418 -0.38367066 4.44391251 129.39942932 -0.38367066 4.79846191 129.70210266 -0.38367066
		 5.22462845 129.7563324 -0.38367066 5.56506729 129.74253845 -0.38367072 5.56122208 130.063461304 -0.38367072
		 7.45146561 130.024810791 -0.38367066 7.15958023 126.94998169 -0.38367069 7.98606873 127.30888367 -0.38367066
		 7.60464048 126.97949219 -0.38367069 8.094989777 127.74822998 -0.38367066;
	setAttr ".vt[166:331]" 5.15367889 127.069488525 -0.38367066 4.95933914 127.57885742 -0.38367066
		 5.56682968 126.85881042 -0.38367069 6.029899597 126.89635468 -0.38367072 4.92417145 128.29908752 -0.38367066
		 0.72954941 134.030075073 0.38367072 0.48497581 133.87435913 0.23753449 0.32709122 133.24865723 0.38367072
		 0.18671417 133.29527283 0.23753449 3.20222855 132.4132843 0.38367072 3.22967124 132.13772583 0.23753449
		 2.82087708 131.63703918 0.38367072 2.94081497 131.54977417 0.23753449 0.177948 132.35559082 0.38367072
		 0.027275085 132.34054565 0.23753449 0.55207062 131.37495422 0.38367072 0.43558502 131.27027893 0.23753449
		 1.44787979 136.73419189 0.38367072 1.29990959 136.88644409 0.23753449 1.43820381 137.54214478 0.38367072
		 1.29183578 137.56069946 0.23753449 4.31327057 136.9956665 0.38367072 4.43490982 137.19247437 0.23753449
		 4.20460129 137.82655334 0.38367072 4.34575272 137.87417603 0.23753449 1.64641762 138.31176758 0.38367072
		 1.51769638 138.39553833 0.23753449 2.24147415 138.79399109 0.38367072 2.18295288 138.93466187 0.23753449
		 -0.016958237 134.0012054443 0.38367072 -0.046607971 133.85379028 0.23753449 0.5909481 136.76893616 0.38367072
		 0.58464241 136.91543579 0.23753449 -0.68572235 134.3125 0.38367072 -0.79535675 134.20236206 0.23753449
		 -1.047540545 135.08013916 0.38367072 -1.19791794 135.056411743 0.23753449 3.8009913 131.63407898 0.38367072
		 3.70450211 131.51980591 0.23753449 5.43019104 134.26519775 0.38367072 5.69041443 134.20024109 0.23753449
		 6.17295456 133.46769714 0.38367072 6.29978561 133.5459137 0.23753449 4.68170547 131.16783142 0.38367072
		 4.64999008 131.019271851 0.23753449 5.52658081 131.22389221 0.38367072 5.58506775 131.081283569 0.23753449
		 5.2824707 137.33152771 0.38367072 5.26324081 137.47950745 0.23753449 6.4784317 134.62597656 0.38367072
		 6.55923843 134.49923706 0.23753449 6.14958572 137.26625061 0.38367072 6.20452881 137.40866089 0.23753449
		 6.78462982 136.77204895 0.38367072 6.90484285 136.86367798 0.23753449 3.07485199 138.88381958 0.38367072
		 3.10419083 139.033950806 0.23753449 3.83159637 138.47691345 0.38367072 3.93758368 138.58584595 0.23753449
		 7.10352373 136.0028381348 0.38367072 7.2555809 136.017669678 0.23753449 6.91796494 135.081954956 0.38367072
		 7.052792072 135.011260986 0.23753449 6.46260071 132.68782043 0.38367072 6.6152916 132.69642639 0.23753449
		 6.25577927 131.85359192 0.38367072 6.38644791 131.77334595 0.23753449 2.21250916 131.048034668 0.38367072
		 2.2765274 130.90661621 0.23753449 1.33309186 130.97671509 0.38367072 1.30361557 130.82772827 0.23753449
		 -0.91786569 136.091033936 0.38367072 -1.05563736 136.16557312 0.23753449 -0.24901199 136.66207886 0.38367072
		 -0.31072617 136.80154419 0.23753449 -7.36283302 137.67764282 0.38367084 -7.6074214 137.52191162 0.23753454
		 -7.6074667 137.20266724 0.38367084 -7.74784374 137.24926758 0.23753454 -6.3426404 136.97984314 0.38367084
		 -6.31519413 136.70429993 0.23753454 -6.57112885 136.51472473 0.38367084 -6.45118856 136.42747498 0.23753454
		 -7.6722374 136.81481934 0.38367084 -7.82290936 136.79978943 0.23753454 -7.51418686 136.40054321 0.38367084
		 -7.63067532 136.2959137 0.23753454 -7.075773239 138.78779602 0.38367084 -7.22374249 138.94004822 0.23753454
		 -7.08117485 139.23892212 0.38367084 -7.22754383 139.25747681 0.23753454 -5.86939526 138.88728333 0.38367084
		 -5.747756 139.084091187 0.23753454 -5.93088531 139.35743713 0.38367084 -5.78973389 139.40505981 0.23753454
		 -6.99248409 139.56672668 0.38367084 -7.12120628 139.6505127 0.23753454 -6.74947929 139.76368713 0.38367084
		 -6.80799866 139.90435791 0.23753454 -7.82804871 137.65962219 0.38367084 -7.8576951 137.51220703 0.23753454
		 -7.55418682 138.80714417 0.38367084 -7.56049585 138.95365906 0.23753454 -8.1005764 137.78648376 0.38367084
		 -8.21021175 137.67633057 0.23753454 -8.24936485 138.10214233 0.38367084 -8.39974117 138.078414917 0.23753454
		 -5.99514866 136.52763367 0.38367084 -6.091639519 136.4133606 0.23753454 -5.41688061 137.74032593 0.38367084
		 -5.1566534 137.67532349 0.23753454 -4.99658966 137.28904724 0.38367084 -4.86975765 137.36729431 0.23753454
		 -5.61478043 136.32626343 0.38367084 -5.64649487 136.17770386 0.23753454 -5.26473713 136.3494873 0.38367084
		 -5.2062521 136.20690918 0.23753454 -5.33853817 139.071273804 0.38367084 -5.35777187 139.21925354 0.23753454
		 -4.8284111 137.94282532 0.38367084 -4.74760342 137.81608582 0.23753454 -4.96955204 139.043487549 0.38367084
		 -4.91460323 139.18589783 0.23753454 -4.70510387 138.83766174 0.38367084 -4.58489132 138.92929077 0.23753454
		 -6.40361214 139.80091858 0.38367084 -6.37427139 139.95108032 0.23753454 -6.087890625 139.63116455 0.38367084
		 -5.98190212 139.74009705 0.23753454 -4.57181835 138.51617432 0.38367084 -4.4197607 138.5309906 0.23753454
		 -4.65006351 138.12783813 0.38367084 -4.51523495 138.057159424 0.23753454 -4.87390709 136.95870972 0.38367084
		 -4.72121334 136.96731567 0.23753454 -4.95962143 136.61296082 0.38367084 -4.82895565 136.53269958 0.23753454
		 -6.82795954 136.26608276 0.38367084 -6.76394176 136.12464905 0.23753454 -7.19252014 136.23651123 0.38367084
		 -7.22199774 136.087524414 0.23753454 -8.19498158 138.52610779 0.38367084 -8.33275509 138.60063171 0.23753454
		 -7.92033386 138.7605896 0.38367084 -7.98204327 138.90003967 0.23753454 5.421772 128.46461487 0.38367084
		 5.17718887 128.30891418 0.23753454 5.17560577 127.98667145 0.38367084 5.035228729 128.033279419 0.23753454
		 6.45611191 127.75788116 0.38367084 6.48355865 127.48232269 0.23753454 6.22613907 127.28975677 0.38367084
		 6.34607649 127.20246124 0.23753454 5.11001205 127.59390259 0.38367084 4.95933914 127.57885742 0.23753454
		 5.2701683 127.17411804 0.38367084 5.15367889 127.069488525 0.23753454 5.71303558 129.59028625 0.38367084
		 5.56506729 129.74253845 0.23753454 5.70759201 130.044906616 0.38367084 5.56122208 130.063461304 0.23753454
		 6.93556976 129.69136047 0.38367084 7.057209492 129.88819885 0.23753454 6.87362242 130.16503906 0.38367084
		 7.014774323 130.21266174 0.23753454 5.7974472 130.37702942 0.38367084;
	setAttr ".vt[332:380]" 5.66872406 130.46080017 0.23753454 6.043876648 130.57675171 0.38367084
		 5.98536301 130.71740723 0.23753454 4.95381546 128.44647217 0.38367084 4.92417145 128.29908752 0.23753454
		 5.23093414 129.60978699 0.38367084 5.22462845 129.7563324 0.23753454 4.67743301 128.57514954 0.38367084
		 4.56779861 128.46499634 0.23753454 4.52656937 128.89523315 0.38367084 4.376194 128.87150574 0.23753454
		 6.80605316 127.3024826 0.38367084 6.70956087 127.18820953 0.23753454 7.39455843 128.52897644 0.38367084
		 7.65478563 128.463974 0.23753454 7.81798983 128.074325562 0.38367084 7.94481993 128.15257263 0.23753454
		 7.1912961 127.09853363 0.38367084 7.15958023 126.94998169 0.23753454 7.54615831 127.12207031 0.38367084
		 7.60464048 126.97949219 0.23753454 7.4706955 129.8768158 0.38367084 7.45146561 130.024810791 0.23753454
		 7.98750305 128.73306274 0.38367084 8.068313599 128.60630798 0.23753454 7.84453583 129.84869385 0.38367084
		 7.89948273 129.99110413 0.23753454 8.11259079 129.64004517 0.38367084 8.23280334 129.73167419 0.23753454
		 6.39449263 130.61451721 0.38367084 6.42383528 130.76464844 0.23753454 6.71451521 130.44244385 0.38367084
		 6.82049942 130.55137634 0.23753454 8.24768448 129.31420898 0.38367084 8.39974213 129.32902527 0.23753454
		 8.168396 128.92070007 0.38367084 8.30322266 128.8500061 0.23753454 7.94229889 127.73961639 0.38367084
		 8.094989777 127.74822998 0.23753454 7.85540438 127.38912201 0.38367084 7.98606873 127.30888367 0.23753454
		 5.96588135 127.037765503 0.38367084 6.029899597 126.89635468 0.23753454 5.59630966 127.0077972412 0.38367084
		 5.56682968 126.85881042 0.23753454 4.58168793 129.3249054 0.38367084 4.44391251 129.39942932 0.23753454
		 4.86017227 129.56263733 0.38367084 4.79846191 129.70210266 0.23753454;
	setAttr -s 905 ".ed";
	setAttr ".ed[0:165]"  4 5 1 3 8 1 6 1 1 7 2 1 9 0 1 14 17 1 5 16 1 10 31 1
		 8 34 1 11 29 1 7 28 1 12 26 1 6 23 1 13 22 1 9 19 1 15 5 1 16 18 1 17 15 1 18 10 1
		 17 18 1 16 15 1 19 21 1 20 9 1 19 20 1 21 14 1 22 20 1 21 22 1 23 25 1 24 6 1 23 24 1
		 25 13 1 26 24 1 25 26 1 27 7 1 28 30 1 27 28 1 29 27 1 30 12 1 29 30 1 31 33 1 32 11 1
		 31 32 1 33 8 1 34 32 1 33 34 1 10 14 1 14 13 1 13 12 1 12 11 1 10 11 1 14 35 1 11 35 1
		 35 13 1 12 35 1 35 10 1 15 4 1 4 16 1 33 3 1 3 34 1 27 2 1 2 28 1 24 1 1 1 23 1 20 0 1
		 0 19 1 40 41 1 41 37 1 41 38 1 39 41 1 46 47 1 47 43 1 47 44 1 45 47 1 48 49 1 48 50 1
		 49 50 1 51 52 1 52 53 1 51 53 1 54 55 1 55 56 1 54 56 1 57 58 1 57 59 1 58 59 1 60 61 1
		 61 62 1 60 62 1 52 63 1 53 63 1 64 52 1 52 65 1 65 64 1 61 66 1 62 66 1 67 61 1 61 68 1
		 68 67 1 69 57 1 49 57 1 49 69 1 70 48 1 71 48 1 71 70 1 55 72 1 56 72 1 73 55 1 55 74 1
		 74 73 1 75 52 1 76 52 1 75 76 1 52 77 1 77 65 1 77 61 1 78 61 1 77 78 1 61 58 1 58 68 1
		 79 57 1 69 79 1 57 80 1 57 81 1 81 80 1 82 57 1 80 82 1 48 83 1 48 84 1 84 83 1 48 85 1
		 83 85 1 86 48 1 85 86 1 71 55 1 87 55 1 71 87 1 55 75 1 75 74 1 78 60 1 66 67 1 59 82 1
		 79 81 1 50 86 1 70 84 1 87 54 1 72 73 1 76 51 1 63 64 1 55 88 1 88 48 1 49 88 1 58 88 1
		 77 88 1 52 88 1 75 88 1 88 61 1 88 57 1 71 88 1 89 90 1 89 91 1 90 91 1 92 93 1 92 94 1
		 93 94 1 95 90 1 90 96 1;
	setAttr ".ed[166:331]" 95 96 1 97 98 1 98 99 1 97 99 1 100 101 1 100 102 1
		 101 102 1 103 104 1 104 105 1 103 105 1 90 106 1 96 106 1 107 90 1 90 108 1 108 107 1
		 104 109 1 105 109 1 110 104 1 104 111 1 111 110 1 112 100 1 93 100 1 93 112 1 113 92 1
		 114 92 1 114 113 1 98 115 1 99 115 1 116 98 1 98 117 1 117 116 1 118 90 1 119 90 1
		 118 119 1 91 108 1 91 104 1 120 104 1 91 120 1 104 101 1 101 111 1 121 100 1 112 121 1
		 100 122 1 100 123 1 123 122 1 124 100 1 122 124 1 92 125 1 92 126 1 126 125 1 92 127 1
		 125 127 1 128 92 1 127 128 1 114 98 1 129 98 1 114 129 1 98 118 1 118 117 1 120 103 1
		 109 110 1 102 124 1 121 123 1 94 128 1 113 126 1 129 97 1 115 116 1 119 95 1 106 107 1
		 89 100 1 101 89 1 118 89 1 114 89 1 98 89 1 89 93 1 92 89 1 89 104 1 130 131 1 130 132 1
		 131 132 1 133 134 1 133 135 1 134 135 1 136 131 1 131 137 1 136 137 1 138 139 1 139 140 1
		 138 140 1 141 142 1 141 143 1 142 143 1 144 145 1 145 146 1 144 146 1 131 147 1 137 147 1
		 148 131 1 131 149 1 149 148 1 145 150 1 146 150 1 151 145 1 145 152 1 152 151 1 153 141 1
		 134 141 1 134 153 1 154 133 1 155 133 1 155 154 1 139 156 1 140 156 1 157 139 1 139 158 1
		 158 157 1 159 131 1 160 131 1 159 160 1 132 149 1 132 145 1 161 145 1 132 161 1 145 142 1
		 142 152 1 162 141 1 153 162 1 141 163 1 141 164 1 164 163 1 165 141 1 163 165 1 133 166 1
		 133 167 1 167 166 1 133 168 1 166 168 1 169 133 1 168 169 1 155 139 1 170 139 1 155 170 1
		 139 159 1 159 158 1 161 144 1 150 151 1 143 165 1 162 164 1 135 169 1 154 167 1 170 138 1
		 156 157 1 160 136 1 147 148 1 130 141 1 142 130 1 159 130 1 155 130 1 139 130 1 130 134 1
		 133 130 1 130 145 1 171 172 1 172 174 1 174 173 1 173 171 1;
	setAttr ".ed[332:497]" 171 195 1 195 196 1 196 172 1 174 180 1 180 179 1 179 173 1
		 175 176 1 176 204 1 204 203 1 203 175 1 175 177 1 177 178 1 178 176 1 177 233 1 233 234 1
		 234 178 1 180 182 1 182 181 1 181 179 1 182 236 1 236 235 1 235 181 1 183 184 1 184 198 1
		 198 197 1 197 183 1 183 185 1 185 186 1 186 184 1 185 191 1 191 192 1 192 186 1 187 188 1
		 188 190 1 190 189 1 189 187 1 187 213 1 213 214 1 214 188 1 190 224 1 224 223 1 223 189 1
		 191 193 1 193 194 1 194 192 1 193 221 1 221 222 1 222 194 1 195 199 1 199 200 1 200 196 1
		 198 240 1 240 239 1 239 197 1 199 201 1 201 202 1 202 200 1 201 237 1 237 238 1 238 202 1
		 204 210 1 210 209 1 209 203 1 205 206 1 206 216 1 216 215 1 215 205 1 205 207 1 207 208 1
		 208 206 1 207 229 1 229 230 1 230 208 1 210 212 1 212 211 1 211 209 1 212 232 1 232 231 1
		 231 211 1 213 217 1 217 218 1 218 214 1 216 228 1 228 227 1 227 215 1 217 219 1 219 220 1
		 220 218 1 219 225 1 225 226 1 226 220 1 221 223 1 224 222 1 225 227 1 228 226 1 229 231 1
		 232 230 1 233 235 1 236 234 1 237 239 1 240 238 1 241 242 1 242 244 1 244 243 1 243 241 1
		 241 265 1 265 266 1 266 242 1 244 250 1 250 249 1 249 243 1 245 246 1 246 274 1 274 273 1
		 273 245 1 245 247 1 247 248 1 248 246 1 247 303 1 303 304 1 304 248 1 250 252 1 252 251 1
		 251 249 1 252 306 1 306 305 1 305 251 1 253 254 1 254 268 1 268 267 1 267 253 1 253 255 1
		 255 256 1 256 254 1 255 261 1 261 262 1 262 256 1 257 258 1 258 260 1 260 259 1 259 257 1
		 257 283 1 283 284 1 284 258 1 260 294 1 294 293 1 293 259 1 261 263 1 263 264 1 264 262 1
		 263 291 1 291 292 1 292 264 1 265 269 1 269 270 1 270 266 1 268 310 1 310 309 1 309 267 1
		 269 271 1 271 272 1 272 270 1 271 307 1 307 308 1 308 272 1 274 280 1;
	setAttr ".ed[498:663]" 280 279 1 279 273 1 275 276 1 276 286 1 286 285 1 285 275 1
		 275 277 1 277 278 1 278 276 1 277 299 1 299 300 1 300 278 1 280 282 1 282 281 1 281 279 1
		 282 302 1 302 301 1 301 281 1 283 287 1 287 288 1 288 284 1 286 298 1 298 297 1 297 285 1
		 287 289 1 289 290 1 290 288 1 289 295 1 295 296 1 296 290 1 291 293 1 294 292 1 295 297 1
		 298 296 1 299 301 1 302 300 1 303 305 1 306 304 1 307 309 1 310 308 1 311 312 1 312 314 1
		 314 313 1 313 311 1 311 335 1 335 336 1 336 312 1 314 320 1 320 319 1 319 313 1 315 316 1
		 316 344 1 344 343 1 343 315 1 315 317 1 317 318 1 318 316 1 317 373 1 373 374 1 374 318 1
		 320 322 1 322 321 1 321 319 1 322 376 1 376 375 1 375 321 1 323 324 1 324 338 1 338 337 1
		 337 323 1 323 325 1 325 326 1 326 324 1 325 331 1 331 332 1 332 326 1 327 328 1 328 330 1
		 330 329 1 329 327 1 327 353 1 353 354 1 354 328 1 330 364 1 364 363 1 363 329 1 331 333 1
		 333 334 1 334 332 1 333 361 1 361 362 1 362 334 1 335 339 1 339 340 1 340 336 1 338 380 1
		 380 379 1 379 337 1 339 341 1 341 342 1 342 340 1 341 377 1 377 378 1 378 342 1 344 350 1
		 350 349 1 349 343 1 345 346 1 346 356 1 356 355 1 355 345 1 345 347 1 347 348 1 348 346 1
		 347 369 1 369 370 1 370 348 1 350 352 1 352 351 1 351 349 1 352 372 1 372 371 1 371 351 1
		 353 357 1 357 358 1 358 354 1 356 368 1 368 367 1 367 355 1 357 359 1 359 360 1 360 358 1
		 359 365 1 365 366 1 366 360 1 361 363 1 364 362 1 365 367 1 368 366 1 369 371 1 372 370 1
		 373 375 1 376 374 1 377 379 1 380 378 1 175 3 1 3 177 1 191 0 1 0 193 1 199 4 1 4 201 1
		 205 2 1 2 207 1 217 1 1 1 219 1 0 221 1 223 0 1 0 189 1 1 225 1 227 1 1 1 215 1 203 2 1
		 2 175 1 173 3 1 3 171 1 4 237 1;
	setAttr ".ed[664:829]" 239 4 1 4 197 1 183 0 1 0 185 1 0 187 1 187 1 1 1 213 1
		 1 205 1 209 2 1 231 2 1 2 211 1 229 2 1 181 3 1 3 179 1 235 3 1 233 3 1 171 4 1 4 195 1
		 4 183 1 183 17 1 14 183 1 175 32 1 34 175 1 175 27 1 29 175 1 205 30 1 28 205 1 205 24 1
		 26 205 1 23 187 1 187 25 1 187 20 1 22 187 1 21 183 1 183 15 1 19 183 1 13 187 1
		 12 205 1 11 175 1 171 31 1 10 171 1 18 171 1 16 171 1 171 33 1 41 257 1 257 36 1
		 245 39 1 39 247 1 261 36 1 36 263 1 269 40 1 40 271 1 275 38 1 38 277 1 287 37 1
		 37 289 1 36 291 1 293 36 1 36 259 1 37 295 1 297 37 1 37 285 1 273 38 1 38 245 1
		 243 39 1 39 241 1 40 307 1 309 40 1 40 267 1 253 36 1 36 255 1 257 37 1 37 283 1
		 37 275 1 279 38 1 301 38 1 38 281 1 299 38 1 251 39 1 39 249 1 305 39 1 303 39 1
		 241 40 1 40 265 1 40 253 1 275 41 1 253 41 1 241 41 1 41 245 1 47 327 1 327 42 1
		 315 45 1 45 317 1 331 42 1 42 333 1 339 46 1 46 341 1 345 44 1 44 347 1 357 43 1
		 43 359 1 42 361 1 363 42 1 42 329 1 43 365 1 367 43 1 43 355 1 343 44 1 44 315 1
		 313 45 1 45 311 1 46 377 1 379 46 1 46 337 1 323 42 1 42 325 1 327 43 1 43 353 1
		 43 345 1 349 44 1 371 44 1 44 351 1 369 44 1 321 45 1 45 319 1 375 45 1 373 45 1
		 311 46 1 46 335 1 46 323 1 345 47 1 323 47 1 311 47 1 47 315 1 178 50 1 49 176 1
		 194 53 1 51 192 1 202 56 1 54 200 1 208 59 1 58 206 1 220 62 1 60 218 1 222 63 1
		 190 65 1 64 224 1 226 66 1 216 68 1 67 228 1 69 204 1 172 71 1 70 174 1 238 72 1
		 198 74 1 73 240 1 186 76 1 75 184 1 188 77 1 214 78 1 79 210 1 212 81 1 80 232 1
		 82 230 1 180 84 1 83 182 1;
	setAttr ".ed[830:904]" 85 236 1 86 234 1 196 87 1 248 94 1 93 246 1 264 96 1
		 95 262 1 272 99 1 97 270 1 278 102 1 101 276 1 290 105 1 103 288 1 292 106 1 260 108 1
		 107 294 1 296 109 1 286 111 1 110 298 1 112 274 1 242 114 1 113 244 1 308 115 1 268 117 1
		 116 310 1 256 119 1 118 254 1 258 91 1 284 120 1 121 280 1 282 123 1 122 302 1 124 300 1
		 250 126 1 125 252 1 127 306 1 128 304 1 266 129 1 318 135 1 134 316 1 334 137 1 136 332 1
		 342 140 1 138 340 1 348 143 1 142 346 1 360 146 1 144 358 1 362 147 1 330 149 1 148 364 1
		 366 150 1 356 152 1 151 368 1 153 344 1 312 155 1 154 314 1 378 156 1 338 158 1 157 380 1
		 326 160 1 159 324 1 328 132 1 354 161 1 162 350 1 352 164 1 163 372 1 165 370 1 320 167 1
		 166 322 1 168 376 1 169 374 1 336 170 1 42 47 1 36 41 1;
	setAttr -s 530 -ch 1810 ".fc";
	setAttr ".fc[0:499]" -type "polyFaces" 
		f 3 75 -75 73
		mu 0 3 0 1 2
		f 3 78 -78 -77
		mu 0 3 3 4 5
		f 3 81 -81 -80
		mu 0 3 6 7 8
		f 3 84 -84 82
		mu 0 3 9 10 11
		f 3 87 -87 -86
		mu 0 3 12 13 14
		f 3 89 -89 77
		mu 0 3 4 15 5
		f 3 -93 -92 -91
		mu 0 3 16 17 5
		f 3 94 -94 86
		mu 0 3 13 18 14
		f 3 -98 -97 -96
		mu 0 3 19 20 14
		f 3 -101 99 -99
		mu 0 3 21 0 11
		f 3 -104 102 -102
		mu 0 3 22 23 2
		f 3 105 -105 80
		mu 0 3 7 24 8
		f 3 -109 -108 -107
		mu 0 3 25 26 8
		f 3 111 110 -110
		mu 0 3 27 28 5
		f 3 -114 -113 91
		mu 0 3 17 29 5
		f 3 116 115 -115
		mu 0 3 29 30 14
		f 3 -119 -118 96
		mu 0 3 20 9 14
		f 3 -121 98 -120
		mu 0 3 31 21 11
		f 3 -124 -123 121
		mu 0 3 32 33 11
		f 3 -126 -122 -125
		mu 0 3 34 32 11
		f 3 -129 -128 126
		mu 0 3 35 36 2
		f 3 -131 -127 129
		mu 0 3 37 35 2
		f 3 -133 -130 -132
		mu 0 3 38 37 2
		f 3 135 134 -134
		mu 0 3 23 39 8
		f 3 -138 -137 107
		mu 0 3 26 27 8
		f 3 138 85 -116
		mu 0 3 30 12 14
		f 3 139 95 93
		mu 0 3 18 19 14
		f 3 140 124 83
		mu 0 3 10 34 11
		f 3 -142 119 122
		mu 0 3 33 31 11
		f 3 142 131 74
		mu 0 3 1 38 2
		f 3 -144 101 127
		mu 0 3 36 22 2
		f 3 144 79 -135
		mu 0 3 39 6 8
		f 3 145 106 104
		mu 0 3 24 25 8
		f 3 146 76 -111
		mu 0 3 28 3 5
		f 3 147 90 88
		mu 0 3 15 16 5
		f 3 136 154 -149
		mu 0 3 8 27 40
		f 3 133 148 -158
		mu 0 3 23 8 40
		f 3 157 149 -103
		mu 0 3 23 40 2
		f 3 -74 -150 -151
		mu 0 3 0 2 40
		f 3 -100 150 156
		mu 0 3 11 0 40
		f 3 -83 -157 -152
		mu 0 3 9 11 40
		f 3 117 151 155
		mu 0 3 14 9 40
		f 3 114 -156 -153
		mu 0 3 29 14 40
		f 3 112 152 -154
		mu 0 3 5 29 40
		f 3 109 153 -155
		mu 0 3 27 5 40
		f 3 160 -160 158
		mu 0 3 41 42 43
		f 3 163 -163 161
		mu 0 3 44 45 46
		f 3 166 -166 -165
		mu 0 3 47 48 41
		f 3 169 -169 -168
		mu 0 3 49 50 51
		f 3 172 -172 170
		mu 0 3 52 53 54
		f 3 175 -175 -174
		mu 0 3 55 56 57
		f 3 177 -177 165
		mu 0 3 48 58 41
		f 3 -181 -180 -179
		mu 0 3 59 60 41
		f 3 182 -182 174
		mu 0 3 56 61 57
		f 3 -186 -185 -184
		mu 0 3 62 63 57
		f 3 -189 187 -187
		mu 0 3 64 44 54
		f 3 -192 190 -190
		mu 0 3 65 66 46
		f 3 193 -193 168
		mu 0 3 50 67 51
		f 3 -197 -196 -195
		mu 0 3 68 69 51
		f 3 199 198 -198
		mu 0 3 70 71 41
		f 3 -201 -161 179
		mu 0 3 60 42 41
		f 3 203 202 -202
		mu 0 3 42 72 57
		f 3 -206 -205 184
		mu 0 3 63 52 57
		f 3 -208 186 -207
		mu 0 3 73 64 54
		f 3 -211 -210 208
		mu 0 3 74 75 54
		f 3 -213 -209 -212
		mu 0 3 76 74 54
		f 3 -216 -215 213
		mu 0 3 77 78 46
		f 3 -218 -214 216
		mu 0 3 79 77 46
		f 3 -220 -217 -219
		mu 0 3 80 79 46
		f 3 222 221 -221
		mu 0 3 66 81 51
		f 3 -225 -224 195
		mu 0 3 69 70 51
		f 3 225 173 -203
		mu 0 3 72 55 57
		f 3 226 183 181
		mu 0 3 61 62 57
		f 3 227 211 171
		mu 0 3 53 76 54
		f 3 -229 206 209
		mu 0 3 75 73 54
		f 3 229 218 162
		mu 0 3 45 80 46
		f 3 -231 189 214
		mu 0 3 78 65 46
		f 3 231 167 -222
		mu 0 3 81 49 51
		f 3 232 194 192
		mu 0 3 67 68 51
		f 3 233 164 -199
		mu 0 3 71 47 41
		f 3 234 178 176
		mu 0 3 58 59 41
		f 3 -237 -171 -236
		mu 0 3 43 52 54
		f 3 197 -159 -238
		mu 0 3 70 41 43
		f 3 220 239 -239
		mu 0 3 66 51 43
		f 3 235 -188 -241
		mu 0 3 43 54 44
		f 3 238 -242 -191
		mu 0 3 66 43 46
		f 3 240 -162 241
		mu 0 3 43 44 46
		f 3 242 204 236
		mu 0 3 43 57 52
		f 3 201 -243 159
		mu 0 3 42 57 43
		f 3 223 237 -240
		mu 0 3 51 70 43
		f 3 245 -245 243
		mu 0 3 82 83 84
		f 3 248 -248 246
		mu 0 3 85 86 87
		f 3 251 -251 -250
		mu 0 3 88 89 82
		f 3 254 -254 -253
		mu 0 3 90 91 92
		f 3 257 -257 255
		mu 0 3 93 94 95
		f 3 260 -260 -259
		mu 0 3 96 97 98
		f 3 262 -262 250
		mu 0 3 89 99 82
		f 3 -266 -265 -264
		mu 0 3 100 101 82
		f 3 267 -267 259
		mu 0 3 97 102 98
		f 3 -271 -270 -269
		mu 0 3 103 104 98
		f 3 -274 272 -272
		mu 0 3 105 85 95
		f 3 -277 275 -275
		mu 0 3 106 107 87
		f 3 278 -278 253
		mu 0 3 91 108 92
		f 3 -282 -281 -280
		mu 0 3 109 110 92
		f 3 284 283 -283
		mu 0 3 111 112 82
		f 3 -286 -246 264
		mu 0 3 101 83 82
		f 3 288 287 -287
		mu 0 3 83 113 98
		f 3 -291 -290 269
		mu 0 3 104 93 98
		f 3 -293 271 -292
		mu 0 3 114 105 95
		f 3 -296 -295 293
		mu 0 3 115 116 95
		f 3 -298 -294 -297
		mu 0 3 117 115 95
		f 3 -301 -300 298
		mu 0 3 118 119 87
		f 3 -303 -299 301
		mu 0 3 120 118 87
		f 3 -305 -302 -304
		mu 0 3 121 120 87
		f 3 307 306 -306
		mu 0 3 107 122 92
		f 3 -310 -309 280
		mu 0 3 110 111 92
		f 3 310 258 -288
		mu 0 3 113 96 98
		f 3 311 268 266
		mu 0 3 102 103 98
		f 3 312 296 256
		mu 0 3 94 117 95
		f 3 -314 291 294
		mu 0 3 116 114 95
		f 3 314 303 247
		mu 0 3 86 121 87
		f 3 -316 274 299
		mu 0 3 119 106 87
		f 3 316 252 -307
		mu 0 3 122 90 92
		f 3 317 279 277
		mu 0 3 108 109 92
		f 3 318 249 -284
		mu 0 3 112 88 82
		f 3 319 263 261
		mu 0 3 99 100 82
		f 3 -322 -256 -321
		mu 0 3 84 93 95
		f 3 282 -244 -323
		mu 0 3 111 82 84
		f 3 305 324 -324
		mu 0 3 107 92 84
		f 3 320 -273 -326
		mu 0 3 84 95 85
		f 3 323 -327 -276
		mu 0 3 107 84 87
		f 3 325 -247 326
		mu 0 3 84 85 87
		f 3 327 289 321
		mu 0 3 84 98 93
		f 3 286 -328 244
		mu 0 3 83 98 84
		f 3 308 322 -325
		mu 0 3 92 111 84
		f 3 23 22 14
		mu 0 3 509 505 125
		f 3 56 -7 -1
		mu 0 3 126 127 515
		f 3 57 1 -43
		mu 0 3 129 130 489
		f 3 20 15 6
		mu 0 3 514 513 128
		f 4 -20 17 -21 16
		mu 0 4 510 512 513 514
		f 4 26 25 -24 21
		mu 0 4 506 504 505 509
		f 3 29 28 12
		mu 0 3 503 499 139
		f 4 32 31 -30 27
		mu 0 4 500 498 499 503
		f 4 5 19 18 45
		mu 0 4 507 512 510 511
		f 3 -36 33 10
		mu 0 3 496 495 146
		f 4 -39 36 35 34
		mu 0 4 492 494 495 496
		f 4 -42 39 44 43
		mu 0 4 487 491 488 486
		f 3 -45 42 8
		mu 0 3 486 488 131
		f 4 46 13 -27 24
		mu 0 4 507 501 504 506
		f 4 47 11 -33 30
		mu 0 4 501 493 498 500
		f 4 48 9 38 37
		mu 0 4 493 490 494 492
		f 4 -50 7 41 40
		mu 0 4 490 511 491 487
		f 3 54 49 51
		mu 0 3 155 511 490
		f 3 53 -52 -49
		mu 0 3 493 155 490
		f 3 -53 -54 -48
		mu 0 3 501 155 493
		f 3 50 52 -47
		mu 0 3 507 155 501
		f 3 -46 -55 -51
		mu 0 3 507 511 155
		f 3 64 -15 4
		mu 0 3 156 123 508
		f 3 0 -16 55
		mu 0 3 126 515 132
		f 3 62 -13 2
		mu 0 3 157 137 502
		f 3 -5 -23 63
		mu 0 3 156 508 124
		f 3 60 -11 3
		mu 0 3 158 144 497
		f 3 -29 61 -3
		mu 0 3 502 138 157
		f 3 58 -9 -2
		mu 0 3 130 151 489
		f 3 -34 59 -4
		mu 0 3 497 145 158
		f 4 328 329 330 331
		mu 0 4 485 160 161 484
		f 4 -329 332 333 334
		mu 0 4 160 485 473 164
		f 4 -331 335 336 337
		mu 0 4 484 161 165 481
		f 4 338 339 340 341
		mu 0 4 483 168 169 469
		f 4 -339 342 343 344
		mu 0 4 168 483 482 172
		f 4 -344 345 346 347
		mu 0 4 172 482 453 174
		f 4 -337 348 349 350
		mu 0 4 481 165 175 480
		f 4 -350 351 352 353
		mu 0 4 480 175 177 454
		f 4 354 355 356 357
		mu 0 4 479 180 181 472
		f 4 -355 358 359 360
		mu 0 4 180 479 478 184
		f 4 -360 361 362 363
		mu 0 4 184 478 475 186
		f 4 364 365 366 367
		mu 0 4 477 188 189 476
		f 4 -365 368 369 370
		mu 0 4 188 477 464 192
		f 4 -367 371 372 373
		mu 0 4 476 189 193 460
		f 4 -363 374 375 376
		mu 0 4 186 475 474 196
		f 4 -376 377 378 379
		mu 0 4 196 474 459 198
		f 4 -334 380 381 382
		mu 0 4 164 473 471 200
		f 4 -357 383 384 385
		mu 0 4 472 181 201 452
		f 4 -382 386 387 388
		mu 0 4 200 471 470 204
		f 4 -388 389 390 391
		mu 0 4 204 470 451 206
		f 4 -341 392 393 394
		mu 0 4 469 169 207 466
		f 4 395 396 397 398
		mu 0 4 468 210 211 463
		f 4 -396 399 400 401
		mu 0 4 210 468 467 214
		f 4 -401 402 403 404
		mu 0 4 214 467 455 216
		f 4 -394 405 406 407
		mu 0 4 466 207 217 465
		f 4 -407 408 409 410
		mu 0 4 465 217 219 456
		f 4 -370 411 412 413
		mu 0 4 192 464 462 222
		f 4 -398 414 415 416
		mu 0 4 463 211 223 458
		f 4 -413 417 418 419
		mu 0 4 222 462 461 226
		f 4 -419 420 421 422
		mu 0 4 226 461 457 228
		f 4 -379 423 -373 424
		mu 0 4 198 459 460 193
		f 4 -422 425 -416 426
		mu 0 4 228 457 458 223
		f 4 -404 427 -410 428
		mu 0 4 216 455 456 219
		f 4 -347 429 -353 430
		mu 0 4 174 453 454 177
		f 4 -391 431 -385 432
		mu 0 4 206 451 452 201
		f 4 433 434 435 436
		mu 0 4 450 230 231 449
		f 4 -434 437 438 439
		mu 0 4 230 450 438 234
		f 4 -436 440 441 442
		mu 0 4 449 231 235 446
		f 4 443 444 445 446
		mu 0 4 448 238 239 434
		f 4 -444 447 448 449
		mu 0 4 238 448 447 242
		f 4 -449 450 451 452
		mu 0 4 242 447 418 244
		f 4 -442 453 454 455
		mu 0 4 446 235 245 445
		f 4 -455 456 457 458
		mu 0 4 445 245 247 419
		f 4 459 460 461 462
		mu 0 4 444 250 251 437
		f 4 -460 463 464 465
		mu 0 4 250 444 443 254
		f 4 -465 466 467 468
		mu 0 4 254 443 440 256
		f 4 469 470 471 472
		mu 0 4 442 258 259 441
		f 4 -470 473 474 475
		mu 0 4 258 442 429 262
		f 4 -472 476 477 478
		mu 0 4 441 259 263 425
		f 4 -468 479 480 481
		mu 0 4 256 440 439 266
		f 4 -481 482 483 484
		mu 0 4 266 439 424 268
		f 4 -439 485 486 487
		mu 0 4 234 438 436 270
		f 4 -462 488 489 490
		mu 0 4 437 251 271 417
		f 4 -487 491 492 493
		mu 0 4 270 436 435 274
		f 4 -493 494 495 496
		mu 0 4 274 435 416 276
		f 4 -446 497 498 499
		mu 0 4 434 239 277 431
		f 4 500 501 502 503
		mu 0 4 433 280 281 428
		f 4 -501 504 505 506
		mu 0 4 280 433 432 284
		f 4 -506 507 508 509
		mu 0 4 284 432 420 286
		f 4 -499 510 511 512
		mu 0 4 431 277 287 430
		f 4 -512 513 514 515
		mu 0 4 430 287 289 421
		f 4 -475 516 517 518
		mu 0 4 262 429 427 292
		f 4 -503 519 520 521
		mu 0 4 428 281 293 423
		f 4 -518 522 523 524
		mu 0 4 292 427 426 296
		f 4 -524 525 526 527
		mu 0 4 296 426 422 298
		f 4 -484 528 -478 529
		mu 0 4 268 424 425 263
		f 4 -527 530 -521 531
		mu 0 4 298 422 423 293
		f 4 -509 532 -515 533
		mu 0 4 286 420 421 289
		f 4 -452 534 -458 535
		mu 0 4 244 418 419 247
		f 4 -496 536 -490 537
		mu 0 4 276 416 417 271
		f 4 538 539 540 541
		mu 0 4 415 300 301 414
		f 4 -539 542 543 544
		mu 0 4 300 415 403 304
		f 4 -541 545 546 547
		mu 0 4 414 301 305 411
		f 4 548 549 550 551
		mu 0 4 413 308 309 399
		f 4 -549 552 553 554
		mu 0 4 308 413 412 312
		f 4 -554 555 556 557
		mu 0 4 312 412 383 314
		f 4 -547 558 559 560
		mu 0 4 411 305 315 410
		f 4 -560 561 562 563
		mu 0 4 410 315 317 384
		f 4 564 565 566 567
		mu 0 4 409 320 321 402
		f 4 -565 568 569 570
		mu 0 4 320 409 408 324
		f 4 -570 571 572 573
		mu 0 4 324 408 405 326
		f 4 574 575 576 577
		mu 0 4 407 328 329 406
		f 4 -575 578 579 580
		mu 0 4 328 407 394 332
		f 4 -577 581 582 583
		mu 0 4 406 329 333 390
		f 4 -573 584 585 586
		mu 0 4 326 405 404 336
		f 4 -586 587 588 589
		mu 0 4 336 404 389 338
		f 4 -544 590 591 592
		mu 0 4 304 403 401 340
		f 4 -567 593 594 595
		mu 0 4 402 321 341 382
		f 4 -592 596 597 598
		mu 0 4 340 401 400 344
		f 4 -598 599 600 601
		mu 0 4 344 400 381 346
		f 4 -551 602 603 604
		mu 0 4 399 309 347 396
		f 4 605 606 607 608
		mu 0 4 398 350 351 393
		f 4 -606 609 610 611
		mu 0 4 350 398 397 354
		f 4 -611 612 613 614
		mu 0 4 354 397 385 356
		f 4 -604 615 616 617
		mu 0 4 396 347 357 395
		f 4 -617 618 619 620
		mu 0 4 395 357 359 386
		f 4 -580 621 622 623
		mu 0 4 332 394 392 362
		f 4 -608 624 625 626
		mu 0 4 393 351 363 388
		f 4 -623 627 628 629
		mu 0 4 362 392 391 366
		f 4 -629 630 631 632
		mu 0 4 366 391 387 368
		f 4 -589 633 -583 634
		mu 0 4 338 389 390 333
		f 4 -632 635 -626 636
		mu 0 4 368 387 388 363
		f 4 -614 637 -620 638
		mu 0 4 356 385 386 359
		f 4 -557 639 -563 640
		mu 0 4 314 383 384 317
		f 4 -601 641 -595 642
		mu 0 4 346 381 382 341
		f 3 643 644 -343
		mu 0 3 167 130 171
		f 3 645 646 -375
		mu 0 3 185 156 195
		f 3 647 648 -387
		mu 0 3 199 126 203
		f 3 649 650 -400
		mu 0 3 209 158 213
		f 3 651 652 -418
		mu 0 3 221 157 225
		f 3 -647 653 -378
		mu 0 3 195 156 197
		f 3 654 655 -374
		mu 0 3 194 156 190
		f 3 -653 656 -421
		mu 0 3 225 157 227
		f 3 657 658 -417
		mu 0 3 224 157 212
		f 3 659 660 -342
		mu 0 3 170 158 167
		f 3 661 662 -332
		mu 0 3 162 130 159
		f 3 -649 663 -390
		mu 0 3 203 126 205
		f 3 664 665 -386
		mu 0 3 202 126 182
		f 3 666 667 -359
		mu 0 3 179 156 183
		f 3 -656 668 -368
		mu 0 3 190 156 187
		f 3 669 670 -369
		mu 0 3 187 157 191
		f 3 -659 671 -399
		mu 0 3 212 157 209
		f 3 672 -660 -395
		mu 0 3 208 158 170
		f 3 673 674 -411
		mu 0 3 220 158 218
		f 3 675 -674 -428
		mu 0 3 215 158 220
		f 3 676 677 -351
		mu 0 3 176 130 166
		f 3 678 -677 -354
		mu 0 3 178 130 176
		f 3 679 -679 -430
		mu 0 3 173 130 178
		f 3 680 681 -333
		mu 0 3 159 126 163
		f 3 -666 682 -358
		mu 0 3 182 126 179
		f 3 -671 -652 -412
		mu 0 3 191 157 221
		f 3 -657 -658 -426
		mu 0 3 227 157 224
		f 3 -651 -676 -403
		mu 0 3 213 158 215
		f 3 -675 -673 -408
		mu 0 3 218 158 208
		f 3 -645 -680 -346
		mu 0 3 171 130 173
		f 3 -678 -662 -338
		mu 0 3 166 130 162
		f 3 -682 -648 -381
		mu 0 3 163 126 199
		f 3 -664 -665 -432
		mu 0 3 205 126 202
		f 3 -668 -646 -362
		mu 0 3 183 156 185
		f 3 -654 -655 -424
		mu 0 3 197 156 194
		f 3 683 -6 684
		mu 0 3 179 134 142
		f 3 685 -44 686
		mu 0 3 167 149 151
		f 3 687 -37 688
		mu 0 3 167 145 148
		f 3 689 -35 690
		mu 0 3 209 147 144
		f 3 691 -32 692
		mu 0 3 209 138 141
		f 3 693 694 -28
		mu 0 3 137 187 140
		f 3 695 -26 696
		mu 0 3 187 124 136
		f 3 697 -685 -25
		mu 0 3 135 179 142
		f 3 698 -18 -684
		mu 0 3 179 132 134
		f 3 699 -698 -22
		mu 0 3 123 179 135
		f 3 -697 -14 700
		mu 0 3 187 136 152
		f 3 -695 -701 -31
		mu 0 3 140 187 152
		f 3 -693 -12 701
		mu 0 3 209 141 153
		f 3 -38 -690 -702
		mu 0 3 153 147 209
		f 3 -689 -10 702
		mu 0 3 167 148 154
		f 3 -41 -686 -703
		mu 0 3 154 149 167
		f 3 703 -8 704
		mu 0 3 159 150 143
		f 3 705 -705 -19
		mu 0 3 133 159 143
		f 3 706 -706 -17
		mu 0 3 127 159 133
		f 3 707 -40 -704
		mu 0 3 159 129 150
		f 3 -56 -699 -683
		mu 0 3 126 132 179
		f 3 -707 -57 -681
		mu 0 3 159 127 126
		f 3 -663 -58 -708
		mu 0 3 159 130 129
		f 3 -687 -59 -644
		mu 0 3 167 151 130
		f 3 -60 -688 -661
		mu 0 3 158 145 167
		f 3 -691 -61 -650
		mu 0 3 209 144 158
		f 3 -62 -692 -672
		mu 0 3 157 138 209
		f 3 -694 -63 -670
		mu 0 3 187 137 157
		f 3 -64 -696 -669
		mu 0 3 156 124 187
		f 3 -700 -65 -667
		mu 0 3 179 123 156
		f 3 710 711 -448
		mu 0 3 237 369 241
		f 3 712 713 -480
		mu 0 3 255 370 265
		f 3 714 715 -492
		mu 0 3 269 371 273
		f 3 716 717 -505
		mu 0 3 279 372 283
		f 3 718 719 -523
		mu 0 3 291 373 295
		f 3 -714 720 -483
		mu 0 3 265 370 267
		f 3 721 722 -479
		mu 0 3 264 370 260
		f 3 -720 723 -526
		mu 0 3 295 373 297
		f 3 724 725 -522
		mu 0 3 294 373 282
		f 3 726 727 -447
		mu 0 3 240 372 237
		f 3 728 729 -437
		mu 0 3 232 369 229
		f 3 -716 730 -495
		mu 0 3 273 371 275
		f 3 731 732 -491
		mu 0 3 272 371 252
		f 3 733 734 -464
		mu 0 3 249 370 253
		f 3 -723 -710 -473
		mu 0 3 260 370 257
		f 3 735 736 -474
		mu 0 3 257 373 261
		f 3 -726 737 -504
		mu 0 3 282 373 279
		f 3 738 -727 -500
		mu 0 3 278 372 240
		f 3 739 740 -516
		mu 0 3 290 372 288
		f 3 741 -740 -533
		mu 0 3 285 372 290
		f 3 742 743 -456
		mu 0 3 246 369 236
		f 3 744 -743 -459
		mu 0 3 248 369 246
		f 3 745 -745 -535
		mu 0 3 243 369 248
		f 3 746 747 -438
		mu 0 3 229 371 233
		f 3 -733 748 -463
		mu 0 3 252 371 249
		f 3 -737 -719 -517
		mu 0 3 261 373 291
		f 3 -724 -725 -531
		mu 0 3 297 373 294
		f 3 -718 -742 -508
		mu 0 3 283 372 285
		f 3 -741 -739 -513
		mu 0 3 288 372 278
		f 3 -712 -746 -451
		mu 0 3 241 369 243
		f 3 -744 -729 -443
		mu 0 3 236 369 232
		f 3 -748 -715 -486
		mu 0 3 233 371 269
		f 3 -731 -732 -537
		mu 0 3 275 371 272
		f 3 -735 -713 -467
		mu 0 3 253 370 255
		f 3 -721 -722 -529
		mu 0 3 267 370 264
		f 3 67 -717 749
		mu 0 3 374 372 279
		f 3 751 -66 -747
		mu 0 3 229 374 371
		f 3 752 -728 -68
		mu 0 3 374 237 372
		f 3 -730 68 -752
		mu 0 3 229 369 374
		f 3 -69 -711 -753
		mu 0 3 374 369 237
		f 3 -750 -738 -67
		mu 0 3 374 279 373
		f 3 -709 66 -736
		mu 0 3 257 374 373
		f 3 65 -751 -749
		mu 0 3 371 374 249
		f 3 755 756 -553
		mu 0 3 307 375 311
		f 3 757 758 -585
		mu 0 3 325 376 335
		f 3 759 760 -597
		mu 0 3 339 377 343
		f 3 761 762 -610
		mu 0 3 349 378 353
		f 3 763 764 -628
		mu 0 3 361 379 365
		f 3 -759 765 -588
		mu 0 3 335 376 337
		f 3 766 767 -584
		mu 0 3 334 376 330
		f 3 -765 768 -631
		mu 0 3 365 379 367
		f 3 769 770 -627
		mu 0 3 364 379 352
		f 3 771 772 -552
		mu 0 3 310 378 307
		f 3 773 774 -542
		mu 0 3 302 375 299
		f 3 -761 775 -600
		mu 0 3 343 377 345
		f 3 776 777 -596
		mu 0 3 342 377 322
		f 3 778 779 -569
		mu 0 3 319 376 323
		f 3 -768 -755 -578
		mu 0 3 330 376 327
		f 3 780 781 -579
		mu 0 3 327 379 331
		f 3 -771 782 -609
		mu 0 3 352 379 349
		f 3 783 -772 -605
		mu 0 3 348 378 310
		f 3 784 785 -621
		mu 0 3 360 378 358
		f 3 786 -785 -638
		mu 0 3 355 378 360
		f 3 787 788 -561
		mu 0 3 316 375 306
		f 3 789 -788 -564
		mu 0 3 318 375 316
		f 3 790 -790 -640
		mu 0 3 313 375 318
		f 3 791 792 -543
		mu 0 3 299 377 303
		f 3 -778 793 -568
		mu 0 3 322 377 319
		f 3 -782 -764 -622
		mu 0 3 331 379 361
		f 3 -769 -770 -636
		mu 0 3 367 379 364
		f 3 -763 -787 -613
		mu 0 3 353 378 355
		f 3 -786 -784 -618
		mu 0 3 358 378 348
		f 3 -757 -791 -556
		mu 0 3 311 375 313
		f 3 -789 -774 -548
		mu 0 3 306 375 302
		f 3 -793 -760 -591
		mu 0 3 303 377 339
		f 3 -776 -777 -642
		mu 0 3 345 377 342
		f 3 -780 -758 -572
		mu 0 3 323 376 325
		f 3 -766 -767 -634
		mu 0 3 337 376 334
		f 3 71 -762 794
		mu 0 3 380 378 349
		f 3 796 -70 -792
		mu 0 3 299 380 377
		f 3 797 -773 -72
		mu 0 3 380 307 378
		f 3 -775 72 -797
		mu 0 3 299 375 380
		f 3 -73 -756 -798
		mu 0 3 380 375 307
		f 3 -795 -783 -71
		mu 0 3 380 349 379
		f 3 -754 70 -781
		mu 0 3 327 380 379
		f 3 69 -796 -794
		mu 0 3 377 380 319
		f 4 798 -76 799 -345
		mu 0 4 172 1 0 168
		f 4 800 -79 801 -377
		mu 0 4 196 4 3 186
		f 4 802 -82 803 -389
		mu 0 4 204 7 6 200
		f 4 804 -85 805 -402
		mu 0 4 214 10 9 210
		f 4 806 -88 807 -420
		mu 0 4 226 13 12 222
		f 4 808 -90 -801 -380
		mu 0 4 198 15 4 196
		f 4 809 92 810 -372
		mu 0 4 189 17 16 193
		f 4 811 -95 -807 -423
		mu 0 4 228 18 13 226
		f 4 812 97 813 -415
		mu 0 4 211 20 19 223
		f 4 -800 100 814 -340
		mu 0 4 168 0 21 169
		f 4 815 103 816 -330
		mu 0 4 160 23 22 161
		f 4 817 -106 -803 -392
		mu 0 4 206 24 7 204
		f 4 818 108 819 -384
		mu 0 4 181 26 25 201
		f 4 820 -112 821 -361
		mu 0 4 184 28 27 180
		f 4 822 113 -810 -366
		mu 0 4 188 29 17 189
		f 4 823 -117 -823 -371
		mu 0 4 192 30 29 188
		f 4 -806 118 -813 -397
		mu 0 4 210 9 20 211
		f 4 -815 120 824 -393
		mu 0 4 169 21 31 207
		f 4 825 123 826 -409
		mu 0 4 217 33 32 219
		f 4 -827 125 827 -429
		mu 0 4 219 32 34 216
		f 4 828 128 829 -349
		mu 0 4 165 36 35 175
		f 4 -830 130 830 -352
		mu 0 4 175 35 37 177
		f 4 -831 132 831 -431
		mu 0 4 177 37 38 174
		f 4 832 -136 -816 -335
		mu 0 4 164 39 23 160
		f 4 -822 137 -819 -356
		mu 0 4 180 27 26 181
		f 4 -808 -139 -824 -414
		mu 0 4 222 12 30 192
		f 4 -814 -140 -812 -427
		mu 0 4 223 19 18 228
		f 4 -828 -141 -805 -405
		mu 0 4 216 34 10 214
		f 4 -825 141 -826 -406
		mu 0 4 207 31 33 217
		f 4 -832 -143 -799 -348
		mu 0 4 174 38 1 172
		f 4 -817 143 -829 -336
		mu 0 4 161 22 36 165
		f 4 -804 -145 -833 -383
		mu 0 4 200 6 39 164
		f 4 -820 -146 -818 -433
		mu 0 4 201 25 24 206
		f 4 -802 -147 -821 -364
		mu 0 4 186 3 28 184
		f 4 -811 -148 -809 -425
		mu 0 4 193 16 15 198
		f 4 833 -164 834 -450
		mu 0 4 242 45 44 238
		f 4 835 -167 836 -482
		mu 0 4 266 48 47 256
		f 4 837 -170 838 -494
		mu 0 4 274 50 49 270
		f 4 839 -173 840 -507
		mu 0 4 284 53 52 280
		f 4 841 -176 842 -525
		mu 0 4 296 56 55 292
		f 4 843 -178 -836 -485
		mu 0 4 268 58 48 266
		f 4 844 180 845 -477
		mu 0 4 259 60 59 263
		f 4 846 -183 -842 -528
		mu 0 4 298 61 56 296
		f 4 847 185 848 -520
		mu 0 4 281 63 62 293
		f 4 -835 188 849 -445
		mu 0 4 238 44 64 239
		f 4 850 191 851 -435
		mu 0 4 230 66 65 231
		f 4 852 -194 -838 -497
		mu 0 4 276 67 50 274
		f 4 853 196 854 -489
		mu 0 4 251 69 68 271
		f 4 855 -200 856 -466
		mu 0 4 254 71 70 250
		f 4 857 200 -845 -471
		mu 0 4 258 42 60 259
		f 4 858 -204 -858 -476
		mu 0 4 262 72 42 258
		f 4 -841 205 -848 -502
		mu 0 4 280 52 63 281
		f 4 -850 207 859 -498
		mu 0 4 239 64 73 277
		f 4 860 210 861 -514
		mu 0 4 287 75 74 289
		f 4 -862 212 862 -534
		mu 0 4 289 74 76 286
		f 4 863 215 864 -454
		mu 0 4 235 78 77 245
		f 4 -865 217 865 -457
		mu 0 4 245 77 79 247
		f 4 -866 219 866 -536
		mu 0 4 247 79 80 244
		f 4 867 -223 -851 -440
		mu 0 4 234 81 66 230
		f 4 -857 224 -854 -461
		mu 0 4 250 70 69 251
		f 4 -843 -226 -859 -519
		mu 0 4 292 55 72 262
		f 4 -849 -227 -847 -532
		mu 0 4 293 62 61 298
		f 4 -863 -228 -840 -510
		mu 0 4 286 76 53 284
		f 4 -860 228 -861 -511
		mu 0 4 277 73 75 287
		f 4 -867 -230 -834 -453
		mu 0 4 244 80 45 242
		f 4 -852 230 -864 -441
		mu 0 4 231 65 78 235
		f 4 -839 -232 -868 -488
		mu 0 4 270 49 81 234
		f 4 -855 -233 -853 -538
		mu 0 4 271 68 67 276
		f 4 -837 -234 -856 -469
		mu 0 4 256 47 71 254
		f 4 -846 -235 -844 -530
		mu 0 4 263 59 58 268
		f 4 868 -249 869 -555
		mu 0 4 312 86 85 308
		f 4 870 -252 871 -587
		mu 0 4 336 89 88 326
		f 4 872 -255 873 -599
		mu 0 4 344 91 90 340
		f 4 874 -258 875 -612
		mu 0 4 354 94 93 350
		f 4 876 -261 877 -630
		mu 0 4 366 97 96 362
		f 4 878 -263 -871 -590
		mu 0 4 338 99 89 336
		f 4 879 265 880 -582
		mu 0 4 329 101 100 333
		f 4 881 -268 -877 -633
		mu 0 4 368 102 97 366
		f 4 882 270 883 -625
		mu 0 4 351 104 103 363;
	setAttr ".fc[500:529]"
		f 4 -870 273 884 -550
		mu 0 4 308 85 105 309
		f 4 885 276 886 -540
		mu 0 4 300 107 106 301
		f 4 887 -279 -873 -602
		mu 0 4 346 108 91 344
		f 4 888 281 889 -594
		mu 0 4 321 110 109 341
		f 4 890 -285 891 -571
		mu 0 4 324 112 111 320
		f 4 892 285 -880 -576
		mu 0 4 328 83 101 329
		f 4 893 -289 -893 -581
		mu 0 4 332 113 83 328
		f 4 -876 290 -883 -607
		mu 0 4 350 93 104 351
		f 4 -885 292 894 -603
		mu 0 4 309 105 114 347
		f 4 895 295 896 -619
		mu 0 4 357 116 115 359
		f 4 -897 297 897 -639
		mu 0 4 359 115 117 356
		f 4 898 300 899 -559
		mu 0 4 305 119 118 315
		f 4 -900 302 900 -562
		mu 0 4 315 118 120 317
		f 4 -901 304 901 -641
		mu 0 4 317 120 121 314
		f 4 902 -308 -886 -545
		mu 0 4 304 122 107 300
		f 4 -892 309 -889 -566
		mu 0 4 320 111 110 321
		f 4 -878 -311 -894 -624
		mu 0 4 362 96 113 332
		f 4 -884 -312 -882 -637
		mu 0 4 363 103 102 368
		f 4 -898 -313 -875 -615
		mu 0 4 356 117 94 354
		f 4 -895 313 -896 -616
		mu 0 4 347 114 116 357
		f 4 -902 -315 -869 -558
		mu 0 4 314 121 86 312
		f 4 -887 315 -899 -546
		mu 0 4 301 106 119 305
		f 4 -874 -317 -903 -593
		mu 0 4 340 90 122 304
		f 4 -890 -318 -888 -643
		mu 0 4 341 109 108 346
		f 4 -872 -319 -891 -574
		mu 0 4 326 88 112 324
		f 4 -881 -320 -879 -635
		mu 0 4 333 100 99 338
		f 3 753 754 903
		mu 0 3 380 327 376
		f 3 795 -904 -779
		mu 0 3 319 380 376
		f 3 708 709 904
		mu 0 3 374 257 370
		f 3 750 -905 -734
		mu 0 3 249 374 370;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Love" -p "C000_Generic_01_PopUp";
	rename -uid "877B7DDA-40A6-4E6D-2947-1A98355EBBC8";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 133.40493774414062 0 ;
	setAttr ".sp" -type "double3" 0 133.40493774414062 0 ;
createNode mesh -n "LoveShape" -p "Love";
	rename -uid "F22FB1C9-4BA8-07A6-A0BE-C5ACD7270B22";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.65611976385116577 0.096367985010147095 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dr" 1;
	setAttr ".vcs" 2;
createNode mesh -n "LoveShapeOrig" -p "Love";
	rename -uid "0DEADFD3-42DF-B7A8-08F0-2F9439C9D5A6";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 164 ".uvst[0].uvsp[0:163]" -type "float2" 0.32760444 0.0089368522
		 0.32954261 0.0077236295 0.33590904 0.031303287 0.32997826 0.053100944 0.32782578
		 0.052110553 0.32532668 0.011788279 0.32840967 0.030243456 0.32512587 0.049129963
		 0.32161951 0.021265745 0.32174543 0.039915204 0.33337048 0.0084275007 0.33500454
		 0.011228502 0.33610159 0.015176058 0.33661723 0.019188404 0.33643141 0.039981902
		 0.33611843 0.044746578 0.33492398 0.049185991 0.33342454 0.051644683 0.3315655 0.0073721707
		 0.33634967 0.024570465 0.33625683 0.03597182 0.33176649 0.052949548 0.31945127 0.029746354
		 0.3300947 0.020122249 0.33097482 0.02028266 0.33218378 0.031145394 0.32878566 0.038693577
		 0.32788664 0.038001597 0.32898754 0.020567086 0.32905281 0.028996691 0.32685474 0.036441326
		 0.3267906 0.023597687 0.32577062 0.031853706 0.33213949 0.021143757 0.33293235 0.023071617
		 0.33314258 0.02484642 0.3329348 0.027594015 0.33208346 0.033869535 0.33166319 0.036428452
		 0.33097577 0.037881434 0.32990408 0.038695961 0.32538921 0.026935473 0.33128631 0.076518655
		 0.32020718 0.02000773 0.31807998 0.029622972 0.33732152 0.078052074 0.32390952 0.07584244
		 0.32426006 0.0097489059 0.32032305 0.041149199 0.33834818 0.092198789 0.32098609
		 0.077798456 0.32684183 0.0063987374 0.32405525 0.051123857 0.33847108 0.10627598
		 0.32708222 0.054687023 0.33692145 0.11248285 0.31922019 0.081174135 0.32915017 0.0048072338
		 0.31800881 0.085166007 0.33160847 0.0044930577 0.33478144 0.11558223 0.32967544 0.056005597
		 0.33185151 0.055811167 0.33285457 0.11689353 0.31764868 0.089239478 0.33385959 0.0057981014
		 0.32648653 0.1005078 0.33782366 0.031158805 0.33782598 0.024309039 0.32325268 0.10034096
		 0.32633114 0.10529202 0.33773914 0.036237359 0.33788958 0.018585742 0.32104903 0.09966433
		 0.31825173 0.093598664 0.33593151 0.0090934336 0.31956005 0.097247899 0.3373251 0.013738394
		 0.32643986 0.10853708 0.33779916 0.040630758 0.33392361 0.054323912 0.33092004 0.11689293
		 0.32725182 0.11237711 0.33733159 0.046105266 0.32903731 0.11559677 0.33580762 0.051354527
		 0.3295359 0.087851815 0.32568163 0.021748334 0.32426444 0.026142195 0.33209491 0.088591456
		 0.32623225 0.08743535 0.32846576 0.018105738 0.32435501 0.032457978 0.33248299 0.094671376
		 0.32498375 0.088223279 0.32997215 0.017515577 0.32579523 0.038045168 0.33248395 0.10094003
		 0.32714826 0.040178955 0.33180636 0.10354115 0.32424569 0.089586362 0.33120966 0.017668713
		 0.32363591 0.09212707 0.33279687 0.019118391 0.33091426 0.1047871 0.32840079 0.041126937
		 0.32995689 0.041175067 0.32967985 0.10530065 0.32378957 0.09482298 0.33390981 0.021861121
		 0.32751137 0.097830325 0.33392084 0.031982481 0.33422154 0.027700648 0.32538277 0.097485885
		 0.32744366 0.10108598 0.33328074 0.035109252 0.33426285 0.024265781 0.33474708 0.023892522
		 0.327793 0.10341693 0.33244294 0.038173407 0.33144325 0.040041834 0.33164698 0.040997863
		 0.33086866 0.091192901 0.32931209 0.094067194 0.33279389 0.03903681 0.32848787 0.10471405
		 0.32998151 0.042227894 0.33369237 0.035793871 0.33432585 0.021257505 0.32428759 0.096263669
		 0.33474809 0.027498081 0.33455443 0.032396287 0.33309609 0.018185727 0.32824779 0.042087048
		 0.32681209 0.041122496 0.33129752 0.016670786 0.32989579 0.016357385 0.32534233 0.038665533
		 0.3238053 0.032626778 0.32820541 0.017113172 0.32379064 0.025939286 0.32524028 0.02106104
		 0.33619058 0.052239895 0.33413064 0.055440426 0.33785856 0.04671061 0.3383655 0.040966213
		 0.3318758 0.05700922 0.3383157 0.036488354 0.33781841 0.013142049 0.33845791 0.018221617
		 0.33631262 0.0081868768 0.33406979 0.0046507716 0.33840927 0.024041414 0.33846569
		 0.031283081 0.33161554 0.0033020675 0.32951909 0.057139754 0.32675242 0.055743575
		 0.32897136 0.003675878 0.32649675 0.0053564608 0.32359982 0.051904559 0.3197532 0.04160136
		 0.32379574 0.0089595318 0.31757501 0.029643774 0.31964254 0.01952219;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 124 ".vt[0:123]"  -1.20785916 134.90135193 0.30317521 2.94077778 129.73161316 0.30317521
		 -4.84444523 135.89697266 -0.30317521 -0.95793957 137.035842896 -0.30317521 -4.788517 136.68920898 -0.30317521
		 2.6101656 135.52804565 -0.30317521 2.55379295 136.38671875 -0.30317521 -4.48448181 134.96737671 -0.30317521
		 -1.20785916 134.90135193 -0.30317521 2.1558609 134.49806213 -0.30317521 -2.94767475 133.27780151 -0.30317521
		 0.44589326 133.12983704 -0.30317521 -4.096268654 137.92848206 -0.30317521 -2.061676979 138.15989685 -0.30317521
		 -2.69009113 138.28520203 -0.30317521 -3.41623688 138.23413086 -0.30317521 -0.095637798 137.75521851 -0.30317521
		 1.91103125 137.49708557 -0.30317521 1.34856176 137.83963013 -0.30317521 0.56482649 137.95387268 -0.30317521
		 -4.54129791 137.40388489 -0.30317521 -1.51868629 137.67765808 -0.30317521 -0.5239892 137.44595337 -0.30317521
		 2.31707954 137.0075836182 -0.30317521 -1.51191807 131.93447876 -0.30317521 1.58573627 130.88282776 -0.30317521
		 3.4735918 130.59370422 -0.30317521 1.76775825 131.2101593 -0.30317521 4.69714451 129.23731995 -0.30317521
		 4.84444523 129.61543274 -0.30317521 1.55399406 130.4138031 -0.30317521 2.94077778 129.73161316 -0.30317521
		 4.29746342 128.88792419 -0.30317521 1.87337577 129.38517761 -0.30317521 3.2937746 128.64463806 -0.30317521
		 2.16346073 131.53382874 -0.30317521 3.29423261 131.13703918 -0.30317521 2.98287678 131.47322083 -0.30317521
		 2.66243458 131.59634399 -0.30317521 3.8632288 130.70562744 -0.30317521 4.82933903 130.073059082 -0.30317521
		 4.61949253 130.47676086 -0.30317521 4.30744267 130.68199158 -0.30317521 2.21869755 128.52467346 -0.30317521
		 -2.84948635 133.37461853 0.30317521 -2.94767475 133.27780151 0.16539337 -1.49429321 132.10667419 0.30317521
		 -1.51191807 131.93447876 0.16539337 -4.36527348 135.04107666 0.30317521 -4.48448181 134.96737671 0.16539337
		 0.3666358 133.24287415 0.30317521 0.44589326 133.12983704 0.16539337 2.043420792 134.58454895 0.30317521
		 2.1558609 134.49806213 0.16539337 -4.65235901 136.66136169 0.30317521 -4.788517 136.68920898 0.16539337
		 -4.70483589 135.91799927 0.30317521 -4.84444523 135.89697266 0.16539337 2.417665 136.35702515 0.30317521
		 2.55379295 136.38671875 0.16539337 2.47046614 135.55273438 0.30317521 2.6101656 135.52804565 0.16539337
		 -4.41952705 137.3344574 0.30317521 -4.54129791 137.40388489 0.16539337 -0.96743399 136.83729553 0.30317521
		 -0.95793957 137.035842896 0.16539337 -1.61670303 137.58044434 0.30317521 -1.51868629 137.67765808 0.16539337
		 -3.38211536 138.098403931 0.30317521 -3.41623688 138.23413086 0.16539337 -2.69888711 138.1464386 0.30317521
		 -2.69009113 138.28520203 0.16539337 -0.43596175 137.33956909 0.30317521 -0.5239892 137.44595337 0.16539337
		 2.19646597 136.93717957 0.30317521 2.31707954 137.0075836182 0.16539337 0.57521772 137.81314087 0.30317521
		 0.56482649 137.95387268 0.16539337 1.30088949 137.70732117 0.30317521 1.34856176 137.83963013 0.16539337
		 -4.011361122 137.81559753 0.30317521 -4.096268654 137.92848206 0.16539337 -2.12524605 138.032058716 0.30317521
		 -2.061676979 138.15989685 0.16539337 -0.033765793 137.62995911 0.30317521 -0.095637798 137.75521851 0.16539337
		 1.81969404 137.3914032 0.30317521 1.91103125 137.49708557 0.16539337 2.0033140182 129.43133545 0.30317521
		 1.87337577 129.38517761 0.16539337 2.30754614 128.67321777 0.30317521 2.21869755 128.52467346 0.16539337
		 1.69319582 130.43013 0.30317521 1.55399406 130.4138031 0.16539337 3.2698102 128.78059387 0.30317521
		 3.2937746 128.64463806 0.16539337 4.23219776 129.013870239 0.30317521 4.29746342 128.88792419 0.16539337
		 1.8753767 131.12017822 0.30317521 1.76775825 131.2101593 0.16539337 1.72112358 130.8427887 0.30317521
		 1.58573627 130.88282776 0.16539337 4.70580673 129.63912964 0.30317521 4.84444523 129.61543274 0.16539337
		 4.58102512 129.31881714 0.30317521 4.69714451 129.23731995 0.16539337 2.21997261 131.40205383 0.30317521
		 2.16346073 131.53382874 0.16539337 3.38428688 130.42469788 0.30317521 3.4735918 130.59370422 0.16539337
		 3.17278647 131.06539917 0.30317521 3.29423261 131.13703918 0.16539337 2.64527464 131.45533752 0.30317521
		 2.66243458 131.59634399 0.16539337 2.90355682 131.35609436 0.30317521 2.98287678 131.47322083 0.16539337
		 3.87902141 130.56680298 0.30317521 3.8632288 130.70562744 0.16539337 4.69266415 130.037261963 0.30317521
		 4.82933903 130.073059082 0.16539337 4.262887 130.54638672 0.30317521 4.30744267 130.68199158 0.16539337
		 4.5137949 130.38136292 0.30317521 4.61949253 130.47676086 0.16539337;
	setAttr -s 260 ".ed";
	setAttr ".ed[0:165]"  2 3 1 4 3 1 2 4 1 3 5 1 5 6 1 3 6 1 7 8 1 2 8 1 7 2 1
		 8 5 1 8 9 1 9 5 1 10 8 1 10 7 1 8 11 1 11 9 1 12 13 1 13 14 1 15 14 1 12 15 1 16 17 1
		 17 18 1 19 18 1 16 19 1 20 21 1 21 13 1 20 12 1 3 21 1 4 20 1 22 23 1 23 17 1 22 16 1
		 6 23 1 3 22 1 10 24 1 24 8 1 24 11 1 8 3 1 25 26 1 27 26 1 25 27 1 26 28 1 28 29 1
		 26 29 1 30 31 1 25 31 1 30 25 1 31 28 1 31 32 1 32 28 1 33 31 1 33 30 1 31 34 1 34 32 1
		 35 36 1 36 37 1 38 37 1 35 38 1 39 40 1 40 41 1 42 41 1 39 42 1 26 36 1 27 35 1 29 40 1
		 26 39 1 33 43 1 43 31 1 43 34 1 31 26 1 44 45 1 45 47 1 47 46 1 46 44 1 44 48 1 48 49 1
		 49 45 1 47 51 1 51 50 1 50 46 1 48 56 1 56 57 1 57 49 1 51 53 1 53 52 1 52 50 1 53 61 1
		 61 60 1 60 52 1 54 55 1 55 57 1 56 54 1 54 62 1 62 63 1 63 55 1 58 59 1 59 75 1 75 74 1
		 74 58 1 58 60 1 61 59 1 62 80 1 80 81 1 81 63 1 64 65 1 65 67 1 67 66 1 66 64 1 64 72 1
		 72 73 1 73 65 1 67 83 1 83 82 1 82 66 1 68 69 1 69 81 1 80 68 1 68 70 1 70 71 1 71 69 1
		 70 82 1 83 71 1 72 84 1 84 85 1 85 73 1 75 87 1 87 86 1 86 74 1 76 77 1 77 85 1 84 76 1
		 76 78 1 78 79 1 79 77 1 78 86 1 87 79 1 88 89 1 89 91 1 91 90 1 90 88 1 88 92 1 92 93 1
		 93 89 1 91 95 1 95 94 1 94 90 1 92 100 1 100 101 1 101 93 1 95 97 1 97 96 1 96 94 1
		 97 105 1 105 104 1 104 96 1 98 99 1 99 101 1 100 98 1 98 106 1 106 107 1 107 99 1
		 102 103 1 103 119 1 119 118 1 118 102 1 102 104 1;
	setAttr ".ed[166:259]" 105 103 1 106 112 1 112 113 1 113 107 1 108 109 1 109 111 1
		 111 110 1 110 108 1 108 116 1 116 117 1 117 109 1 111 115 1 115 114 1 114 110 1 112 114 1
		 115 113 1 116 120 1 120 121 1 121 117 1 119 123 1 123 122 1 122 118 1 120 122 1 123 121 1
		 56 64 1 64 54 1 64 60 1 58 64 1 48 0 1 0 56 1 60 0 1 0 52 1 44 0 1 0 50 1 80 82 1
		 84 86 1 62 66 1 72 74 1 46 0 1 0 64 1 100 108 1 108 98 1 108 104 1 102 108 1 92 1 1
		 1 100 1 104 1 1 1 96 1 88 1 1 1 94 1 106 110 1 116 118 1 90 1 1 1 108 1 55 4 1 2 57 1
		 61 5 1 6 59 1 7 49 1 53 9 1 10 45 1 51 11 1 83 13 1 14 71 1 15 69 1 12 81 1 87 17 1
		 18 79 1 19 77 1 16 85 1 67 21 1 20 63 1 65 3 1 75 23 1 22 73 1 24 47 1 99 27 1 25 101 1
		 105 28 1 29 103 1 30 93 1 97 32 1 33 89 1 95 34 1 111 36 1 37 115 1 38 113 1 35 107 1
		 119 40 1 41 123 1 42 121 1 39 117 1 109 26 1 43 91 1;
	setAttr -s 140 -ch 520 ".fc[0:139]" -type "polyFaces" 
		f 3 2 1 -1
		mu 0 3 0 1 2
		f 3 5 -5 -4
		mu 0 3 2 3 4
		f 3 8 7 -7
		mu 0 3 5 0 6
		f 3 -12 -11 9
		mu 0 3 4 7 6
		f 3 13 6 -13
		mu 0 3 8 5 6
		f 3 -16 -15 10
		mu 0 3 7 9 6
		f 4 19 18 -18 -17
		mu 0 4 10 11 12 13
		f 4 23 22 -22 -21
		mu 0 4 14 15 16 17
		f 4 26 16 -26 -25
		mu 0 4 18 10 13 19
		f 4 28 24 -28 -2
		mu 0 4 1 18 19 2
		f 4 31 20 -31 -30
		mu 0 4 20 14 17 21
		f 4 33 29 -33 -6
		mu 0 4 2 20 21 3
		f 3 12 -36 -35
		mu 0 3 8 6 22
		f 3 -37 35 14
		mu 0 3 9 22 6
		f 3 0 -38 -8
		mu 0 3 0 2 6
		f 3 3 -10 37
		mu 0 3 2 4 6
		f 3 40 39 -39
		mu 0 3 23 24 25
		f 3 43 -43 -42
		mu 0 3 25 26 27
		f 3 46 45 -45
		mu 0 3 28 23 29
		f 3 -50 -49 47
		mu 0 3 27 30 29
		f 3 51 44 -51
		mu 0 3 31 28 29
		f 3 -54 -53 48
		mu 0 3 30 32 29
		f 4 57 56 -56 -55
		mu 0 4 33 34 35 36
		f 4 61 60 -60 -59
		mu 0 4 37 38 39 40
		f 4 63 54 -63 -40
		mu 0 4 24 33 36 25
		f 4 65 58 -65 -44
		mu 0 4 25 37 40 26
		f 3 50 -68 -67
		mu 0 3 31 29 41
		f 3 -69 67 52
		mu 0 3 32 41 29
		f 3 38 -70 -46
		mu 0 3 23 25 29
		f 3 41 -48 69
		mu 0 3 25 27 29
		f 4 70 71 72 73
		mu 0 4 163 43 44 162
		f 4 -71 74 75 76
		mu 0 4 43 163 161 47
		f 4 -73 77 78 79
		mu 0 4 162 44 48 160
		f 4 -76 80 81 82
		mu 0 4 47 161 158 51
		f 4 -79 83 84 85
		mu 0 4 160 48 52 159
		f 4 -85 86 87 88
		mu 0 4 159 52 54 156
		f 4 89 90 -82 91
		mu 0 4 157 57 51 158
		f 4 -90 92 93 94
		mu 0 4 57 157 154 59
		f 4 95 96 97 98
		mu 0 4 155 61 62 146
		f 4 -96 99 -88 100
		mu 0 4 61 155 156 54
		f 4 -94 101 102 103
		mu 0 4 59 154 151 65
		f 4 104 105 106 107
		mu 0 4 153 67 68 152
		f 4 -105 108 109 110
		mu 0 4 67 153 147 71
		f 4 -107 111 112 113
		mu 0 4 152 68 72 149
		f 4 114 115 -103 116
		mu 0 4 150 75 65 151
		f 4 -115 117 118 119
		mu 0 4 75 150 148 77
		f 4 -119 120 -113 121
		mu 0 4 77 148 149 72
		f 4 -110 122 123 124
		mu 0 4 71 147 145 79
		f 4 -98 125 126 127
		mu 0 4 146 62 80 143
		f 4 128 129 -124 130
		mu 0 4 144 83 79 145
		f 4 -129 131 132 133
		mu 0 4 83 144 142 85
		f 4 -133 134 -127 135
		mu 0 4 85 142 143 80
		f 4 136 137 138 139
		mu 0 4 141 87 88 140
		f 4 -137 140 141 142
		mu 0 4 87 141 139 91
		f 4 -139 143 144 145
		mu 0 4 140 88 92 138
		f 4 -142 146 147 148
		mu 0 4 91 139 136 95
		f 4 -145 149 150 151
		mu 0 4 138 92 96 137
		f 4 -151 152 153 154
		mu 0 4 137 96 98 134
		f 4 155 156 -148 157
		mu 0 4 135 101 95 136
		f 4 -156 158 159 160
		mu 0 4 101 135 132 103
		f 4 161 162 163 164
		mu 0 4 133 105 106 126
		f 4 -162 165 -154 166
		mu 0 4 105 133 134 98
		f 4 -160 167 168 169
		mu 0 4 103 132 128 109
		f 4 170 171 172 173
		mu 0 4 131 111 112 130
		f 4 -171 174 175 176
		mu 0 4 111 131 127 115
		f 4 -173 177 178 179
		mu 0 4 130 112 116 117
		f 4 -169 180 -179 181
		mu 0 4 109 128 117 116
		f 4 -176 182 183 184
		mu 0 4 115 127 124 119
		f 4 -164 185 186 187
		mu 0 4 126 106 120 121
		f 4 -184 188 -187 189
		mu 0 4 119 124 121 120
		f 3 190 191 -92
		mu 0 3 50 66 56
		f 3 192 -100 193
		mu 0 3 66 55 60
		f 3 194 195 -81
		mu 0 3 46 122 50
		f 3 196 197 -89
		mu 0 3 55 122 53
		f 3 198 -195 -75
		mu 0 3 42 122 46
		f 3 -198 199 -86
		mu 0 3 53 122 49
		f 4 200 -121 -118 -117
		mu 0 4 64 73 76 74
		f 4 201 -135 -132 -131
		mu 0 4 78 81 84 82
		f 4 202 -114 -201 -102
		mu 0 4 58 69 73 64
		f 4 -192 -108 -203 -93
		mu 0 4 56 66 69 58
		f 4 203 -128 -202 -123
		mu 0 4 70 63 81 78
		f 4 -194 -99 -204 -109
		mu 0 4 66 60 63 70
		f 3 -74 204 -199
		mu 0 3 42 45 122
		f 3 -200 -205 -80
		mu 0 3 49 122 45
		f 3 -196 205 -191
		mu 0 3 50 122 66
		f 3 -206 -197 -193
		mu 0 3 66 122 55
		f 3 206 207 -158
		mu 0 3 94 110 100
		f 3 208 -166 209
		mu 0 3 110 99 104
		f 3 210 211 -147
		mu 0 3 90 123 94
		f 3 212 213 -155
		mu 0 3 99 123 97
		f 3 214 -211 -141
		mu 0 3 86 123 90
		f 3 -214 215 -152
		mu 0 3 97 123 93
		f 4 216 -180 -181 -168
		mu 0 4 102 113 129 108
		f 4 217 -188 -189 -183
		mu 0 4 114 107 125 118
		f 4 -208 -174 -217 -159
		mu 0 4 100 110 113 102
		f 4 -210 -165 -218 -175
		mu 0 4 110 104 107 114
		f 3 -140 218 -215
		mu 0 3 86 89 123
		f 3 -216 -219 -146
		mu 0 3 93 123 89
		f 3 -212 219 -207
		mu 0 3 94 123 110
		f 3 -220 -213 -209
		mu 0 3 110 123 99
		f 4 220 -3 221 -91
		mu 0 4 57 1 0 51
		f 4 222 4 223 -101
		mu 0 4 54 4 3 61
		f 4 -222 -9 224 -83
		mu 0 4 51 0 5 47
		f 4 225 11 -223 -87
		mu 0 4 52 7 4 54
		f 4 -225 -14 226 -77
		mu 0 4 47 5 8 43
		f 4 227 15 -226 -84
		mu 0 4 48 9 7 52
		f 4 228 17 229 -122
		mu 0 4 72 13 12 77
		f 4 -230 -19 230 -120
		mu 0 4 77 12 11 75
		f 4 -231 -20 231 -116
		mu 0 4 75 11 10 65
		f 4 232 21 233 -136
		mu 0 4 80 17 16 85
		f 4 -234 -23 234 -134
		mu 0 4 85 16 15 83
		f 4 -235 -24 235 -130
		mu 0 4 83 15 14 79
		f 4 236 25 -229 -112
		mu 0 4 68 19 13 72
		f 4 -232 -27 237 -104
		mu 0 4 65 10 18 59
		f 4 238 27 -237 -106
		mu 0 4 67 2 19 68
		f 4 -238 -29 -221 -95
		mu 0 4 59 18 1 57
		f 4 239 30 -233 -126
		mu 0 4 62 21 17 80
		f 4 -236 -32 240 -125
		mu 0 4 79 14 20 71
		f 4 -224 32 -240 -97
		mu 0 4 61 3 21 62
		f 4 -241 -34 -239 -111
		mu 0 4 71 20 2 67
		f 4 -227 34 241 -72
		mu 0 4 43 8 22 44
		f 4 -242 36 -228 -78
		mu 0 4 44 22 9 48
		f 4 242 -41 243 -157
		mu 0 4 101 24 23 95
		f 4 244 42 245 -167
		mu 0 4 98 27 26 105
		f 4 -244 -47 246 -149
		mu 0 4 95 23 28 91
		f 4 247 49 -245 -153
		mu 0 4 96 30 27 98
		f 4 -247 -52 248 -143
		mu 0 4 91 28 31 87
		f 4 249 53 -248 -150
		mu 0 4 92 32 30 96
		f 4 250 55 251 -178
		mu 0 4 112 36 35 116
		f 4 -252 -57 252 -182
		mu 0 4 116 35 34 109
		f 4 -253 -58 253 -170
		mu 0 4 109 34 33 103
		f 4 254 59 255 -186
		mu 0 4 106 40 39 120
		f 4 -256 -61 256 -190
		mu 0 4 120 39 38 119
		f 4 -257 -62 257 -185
		mu 0 4 119 38 37 115
		f 4 258 62 -251 -172
		mu 0 4 111 25 36 112
		f 4 -254 -64 -243 -161
		mu 0 4 103 33 24 101
		f 4 -246 64 -255 -163
		mu 0 4 105 26 40 106
		f 4 -258 -66 -259 -177
		mu 0 4 115 37 25 111
		f 4 -249 66 259 -138
		mu 0 4 87 31 41 88
		f 4 -260 68 -250 -144
		mu 0 4 88 41 32 92;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "Angry" -p "C000_Generic_01_PopUp";
	rename -uid "7A13D8D6-4FE7-4EC1-9EA4-BC906819101A";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 9.5367431640625e-07 133.40494537353516 -5.9604644775390625e-08 ;
	setAttr ".sp" -type "double3" 9.5367431640625e-07 133.40494537353516 -5.9604644775390625e-08 ;
createNode mesh -n "AngryShape" -p "Angry";
	rename -uid "8976671F-432D-3DC5-CDA7-16BF23934383";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.65781503915786743 0.029327303171157837 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dr" 1;
	setAttr ".vcs" 2;
createNode mesh -n "AngryShapeOrig" -p "Angry";
	rename -uid "FBF827E8-403E-A4CD-9F97-DEAD484A1D2D";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 252 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" 0.32772914 0.034686081 0.32779834
		 0.024567157 0.32939145 0.02480562 0.32934961 0.034874588 0.33094814 0.034478925 0.33087036
		 0.024761491 0.33362469 0.02377522 0.33403888 0.032732658 0.32148626 0.027502827 0.32451382
		 0.023810722 0.32392201 0.033100374 0.32047996 0.030735411 0.31973472 0.028644346
		 0.33800635 0.028565504 0.33740065 0.03025461 0.33645549 0.027140349 0.33626649 0.023508653
		 0.33752063 0.024630964 0.3217068 0.023445286 0.32028893 0.024547435 0.33810338 0.026471227
		 0.31967226 0.026369058 0.32992518 0.034510627 0.32841727 0.03492415 0.32827803 0.024984896
		 0.32988352 0.024678603 0.32686499 0.034566298 0.32369253 0.032412738 0.32430196 0.023670644
		 0.32703099 0.024774536 0.3361232 0.027703479 0.33359772 0.032906353 0.33316728 0.023742005
		 0.33705842 0.03096129 0.33783269 0.028967857 0.31984761 0.028032914 0.32142022 0.026881248
		 0.32039616 0.0297876 0.32173625 0.023236468 0.32045296 0.024199948 0.33593637 0.023665473
		 0.33733892 0.024844185 0.31981832 0.025963947 0.33793205 0.026703164 0.33129242 0.02696415
		 0.33159456 0.029521979 0.32712021 0.030716278 0.32702115 0.027409546 0.33122429 0.032376103
		 0.33048829 0.039841838 0.32632771 0.039361261 0.32690147 0.033638053 0.32815924 0.014410682
		 0.3307049 0.020576008 0.32632115 0.020420723 0.32982686 0.012728624 0.32887301 0.011069931
		 0.32857814 0.047839977 0.32792744 0.044796444 0.32942191 0.046629019 0.32611707 0.044399582
		 0.32664058 0.046863399 0.32618442 0.014489286 0.32680759 0.011810176 0.32754692 0.048022516
		 0.32775226 0.010742538 0.32936239 0.10187989 0.32754955 0.037065536 0.32937744 0.03727746
		 0.32727462 0.10247791 0.33346111 0.096198589 0.32343057 0.035397559 0.33115527 0.0368177
		 0.32521594 0.10178612 0.32886988 0.093724623 0.3277826 0.022071108 0.32435122 0.021407954
		 0.33149892 0.089663498 0.32731521 0.094808489 0.32938567 0.022148557 0.32571614 0.094264612
		 0.33086959 0.022017024 0.33458403 0.034963354 0.32183439 0.096092567 0.33819768 0.031709038
		 0.31940758 0.088920057 0.32390809 0.08981058 0.33381864 0.021371752 0.32253546 0.085334316
		 0.33681312 0.021710314 0.33639038 0.090024151 0.31964979 0.032135583 0.32127377 0.021530285
		 0.3333379 0.085310593 0.33658743 0.086992025 0.31871226 0.029094025 0.33595455 0.084640101
		 0.31873575 0.025843002 0.31955037 0.023266651 0.33481497 0.083944902 0.33898029 0.029257305
		 0.3194114 0.086441249 0.33906659 0.026293591 0.32007295 0.084393024 0.32124966 0.083948597
		 0.33836618 0.023573078 0.32927543 0.084772982 0.33010873 0.0368855 0.33408037 0.035187125
		 0.33325875 0.090728171 0.32732958 0.083877295 0.32839388 0.037268922 0.32533711 0.084672511
		 0.3266103 0.036870718 0.32884824 0.092623681 0.32988346 0.022113204 0.32826355 0.022214323
		 0.3272379 0.09142869 0.33123672 0.097121693 0.33335108 0.021367982 0.32701948 0.022115484
		 0.32590348 0.09247493 0.32217032 0.091064438 0.32309669 0.034648329 0.31959987 0.097573578
		 0.31952897 0.031010911 0.32415944 0.021361992 0.32419932 0.09704677 0.32131946 0.021349669
		 0.32268113 0.10120707 0.33778831 0.032494992 0.33625162 0.096606493 0.33315617 0.10110901
		 0.3364777 0.02177614 0.33879924 0.029681355 0.33641547 0.099589489 0.33889699 0.026493207
		 0.33576471 0.10189678 0.33462781 0.10254106 0.33818063 0.023798287 0.31957948 0.10000131
		 0.31882972 0.028413191 0.3202154 0.1020584 0.31889865 0.025412932 0.31973097 0.022892416
		 0.32137787 0.10254551 0.32383686 0.090525351 0.33250341 0.026598714 0.33184728 0.019688599
		 0.3264401 0.083319001 0.32320166 0.093611225 0.33265629 0.029581301 0.32403046 0.097051777
		 0.33244243 0.032816596 0.32706577 0.091242529 0.32569918 0.02746091 0.32575175 0.030671723
		 0.3267228 0.094763815 0.32975298 0.086585179 0.32515034 0.020115681 0.32564899 0.033594616
		 0.32760328 0.097488202 0.32713878 0.10477214 0.33161876 0.040838473 0.33033466 0.10982131
		 0.33007857 0.048263989 0.32517144 0.039633386 0.3299793 0.10103391 0.32519665 0.045233823
		 0.33213997 0.10375974 0.33062747 0.011339404 0.32984728 0.076887198 0.33209664 0.082956523
		 0.32527241 0.013421319 0.32926622 0.0091837198 0.3313331 0.076561064 0.32768175 0.0088253543
		 0.33247393 0.077848464 0.33279252 0.080097206 0.32631084 0.010124423 0.33153504 0.10986174
		 0.32881668 0.049830578 0.33255243 0.1086043 0.32730982 0.04986275 0.3260124 0.048327558
		 0.33279335 0.10630499 0.33508641 0.087692007 0.32077324 0.086981401 0.33493388 0.098836154
		 0.32093531 0.099519297 0.33096039 0.079491265 0.33129692 0.10718024 0.32717434 0.051045664
		 0.32568428 0.049235977 0.32468036 0.045827784 0.32893845 0.050809644 0.33049759 0.049175762
		 0.32605109 0.0091386363 0.32762811 0.0076089427 0.32476744 0.012771033 0.3294656
		 0.0082351193 0.33110842 0.010538928 0.32449749 0.019872226 0.33247867 0.019214235
		 0.32451156 0.039859451 0.32497403 0.033662863 0.33223054 0.041369267 0.33312038 0.033040635
		 0.32502702 0.030708589 0.32502601 0.027418546 0.33331755 0.029567622 0.33318034 0.026402943
		 0.31830594 0.02509582 0.31927517 0.022211343 0.32102472 0.020282611 0.31832722 0.028610229
		 0.31904078 0.031795725 0.33867836 0.02325733 0.33950901 0.026345953 0.33681419 0.020728797
		 0.33928439 0.030045986 0.33821711 0.033414334 0.33348337 0.020046115 0.33433101 0.036447793
		 0.32403034 0.020048618 0.32696635 0.020745412 0.32278645 0.035852969 0.32645565 0.038208187
		 0.32826698 0.020748824 0.32992125 0.020750791 0.3283751 0.038608491 0.33022302 0.038228989
		 0.33886394 0.023023397 0.33968106 0.026153274 0.33715519 0.020723954 0.33947662 0.029605873
		 0.33865967 0.032599226 0.31813398 0.02554667 0.31908503 0.022611387 0.32096848 0.020454429
		 0.31820735 0.029337257 0.31918409 0.033005811 0.32423016 0.020054646 0.32316944 0.036642805
		 0.33397207 0.020054229 0.33087865 0.020588122 0.33486941 0.036188491 0.3313078 0.038175337
		 0.32934013 0.020752817 0.32774237 0.020702139;
	setAttr ".uvst[0].uvsp[250:251]" 0.32940218 0.038600385 0.32743564 0.03844025;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 192 ".vt";
	setAttr ".vt[0:165]"  -3.47476959 135.39425659 0.28013742 -3.30058002 130.90258789 0.28013742
		 0.07775116 137.31440735 0.28013742 3.43666816 134.42228699 0.28013742 3.31060028 131.46257019 0.28013742
		 -0.70537567 129.58668518 0.28013742 -0.94174957 132.6714325 -0.28013766 -0.84881967 133.39154053 -0.28013766
		 -2.38572884 133.36943054 -0.28013766 -2.52739143 132.94404602 -0.28013766 -0.9789753 134.10514832 -0.28013766
		 -1.93148994 135.20504761 -0.28013766 -3.10962677 134.28153992 -0.28013766 -2.45932007 133.76846313 -0.28013766
		 -3.30058002 130.90258789 -0.28013772 -1.84645653 131.32637024 -0.28013766 -3.12698936 132.14492798 -0.28013766
		 -2.85289764 130.34440613 -0.28013766 -3.43260217 130.26080322 -0.28013766 -3.61612701 135.98297119 -0.28013766
		 -3.47476959 135.39425659 -0.28013772 -3.12891865 135.99125671 -0.28013766 -3.84677696 134.71960449 -0.28013766
		 -4.11945152 135.20913696 -0.28013772 -3.81640148 131.54574585 -0.28013772 -4.06435585 130.98913574 -0.28013778
		 -4.032870293 135.70547485 -0.28013772 -3.91076779 130.50961304 -0.28013766 0.59885406 133.67437744 -0.28013766
		 1.34523773 135.047790527 -0.28013766 0.92125702 135.19358826 -0.28013766 -0.029670715 133.98597717 -0.28013766
		 -0.49163058 134.54870605 -0.28013766 0.75270844 135.49436951 -0.28013766 0.79190826 136.34858704 -0.28013766
		 -0.63135529 136.02532959 -0.28013766 3.43666816 134.42228699 -0.28013772 2.34424591 135.11669922 -0.28013772
		 2.21689606 133.60223389 -0.28013766 3.60825372 133.72763062 -0.28013766 4.026725769 134.13742065 -0.28013766
		 -0.60660553 137.40222168 -0.28013766 -0.30411527 137.78424072 -0.28013766 0.07775116 137.31440735 -0.28013772
		 0.83965307 137.20028687 -0.28013766 0.61634064 137.71417236 -0.28013766 3.23897552 135.22270203 -0.28013778
		 3.83174896 135.08164978 -0.28013766 0.16944122 137.94682312 -0.28013766 4.11945343 134.66842651 -0.28013766
		 -0.27448273 132.50737 -0.28013766 0.56777191 131.44467163 -0.28013766 0.92661285 131.71957397 -0.28013766
		 0.13791656 132.97857666 -0.28013766 0.8406601 132.98721313 -0.28013766 1.34793866 131.67195129 -0.28013766
		 2.16266608 131.25965881 -0.28013766 2.42613983 132.63829041 -0.28013766 -0.70537567 129.58668518 -0.28013772
		 0.29837799 130.40161133 -0.28013766 -0.9524917 131.2171936 -0.28013766 -1.40923309 129.71534729 -0.28013766
		 -1.20731354 129.1655426 -0.28013766 3.67154694 132.050567627 -0.28013766 3.89574432 131.61793518 -0.28013766
		 3.31060028 131.46257019 -0.28013772 2.89377594 130.81466675 -0.28013742 3.45404816 130.80734253 -0.28013742
		 0.10564424 129.43844604 -0.28013742 -0.2662735 128.95578003 -0.28013742 3.84963226 131.11938477 -0.28013742
		 -0.76117706 128.86306763 -0.28013742 -1.098697543 132.73054504 0.28013766 -0.94174957 132.6714325 0.11691542
		 -1.013950348 133.38723755 0.28013766 -0.84881967 133.39154053 0.11691542 -2.38091278 132.86730957 0.28013766
		 -2.52739143 132.94404602 0.11691542 -2.21759415 133.35771179 0.28013766 -2.38572884 133.36943054 0.11691542
		 -1.13154793 134.031997681 0.28013766 -0.9789753 134.10514832 0.11691542 -2.040031433 135.081069946 0.28013766
		 -1.93148994 135.20504761 0.11691542 -2.30995464 133.85852051 0.28013766 -2.45932007 133.76846313 0.11691542
		 -3.016981125 134.41635132 0.28013766 -3.10962677 134.28153992 0.11691542 -1.97249603 131.43144226 0.28013766
		 -1.84645653 131.32637024 0.11691542 -3.0068340302 132.033096313 0.28013766 -3.12698936 132.14492798 0.11691542
		 -2.92882442 130.49836731 0.28013766 -2.85289764 130.34440613 0.11691542 -3.40388179 130.42985535 0.28013766
		 -3.43260217 130.26080322 0.11691542 -3.68202472 131.4462738 0.28013766 -3.81640148 131.54574585 0.11691542
		 -3.88991451 130.97961426 0.28013766 -4.06435585 130.98913574 0.11691542 -3.77581978 130.62339783 0.28013766
		 -3.91076779 130.50961304 0.11691542 -3.17644334 135.82720947 0.28013766 -3.12891865 135.99125671 0.11691542
		 -3.56549668 135.8205719 0.28013766 -3.61612701 135.98297119 0.11691542 -3.72558498 134.83746338 0.28013766
		 -3.84677696 134.71960449 0.11691542 -3.94872093 135.23805237 0.28013766 -4.11945152 135.20913696 0.11691542
		 -3.8841114 135.60842896 0.28013766 -4.032870293 135.70547485 0.11691542 0.64051247 133.83590698 0.28013766
		 0.59885406 133.67437744 0.11691542 0.074239731 134.11663818 0.28013766 -0.029670715 133.98597717 0.11691542
		 1.32345772 134.88269043 0.28013766 1.34523773 135.047790527 0.11691542 0.80929947 135.05947876 0.28013766
		 0.92125702 135.19358826 0.11691542 -0.33383179 134.61372375 0.28013766 -0.49163058 134.54870605 0.11691542
		 -0.46799466 136.031570435 0.28013766 -0.63135529 136.02532959 0.11691542 0.5875206 135.45527649 0.28013766
		 0.75270844 135.49436951 0.11691542 0.62889481 136.35687256 0.28013766 0.79190826 136.34858704 0.11691542
		 2.21318841 133.76577759 0.28013766 2.21689606 133.60223389 0.11691542 2.35947037 134.95414734 0.28013766
		 2.34424591 135.11669922 0.11691542 3.5356369 133.88496399 0.28013766 3.60825372 133.72763062 0.11691542
		 3.87497687 134.2172699 0.28013766 4.026725769 134.13742065 0.11691542 3.22939301 135.057189941 0.28013766
		 3.23897552 135.22270203 0.11691542 3.73337936 134.93725586 0.28013766 3.83174896 135.08164978 0.11691542
		 3.94710541 134.6302948 0.28013766 4.11945343 134.66842651 0.11691542 -0.44440079 137.34414673 0.28013766
		 -0.60660553 137.40222168 0.11691542 -0.20585825 137.64541626 0.28013766 -0.30411527 137.78424072 0.11691542
		 0.67451859 137.17074585 0.28013766 0.83965307 137.20028687 0.11691542 0.48968509 137.59608459 0.28013766
		 0.61634064 137.71417236 0.11691542 0.15619659 137.76966858 0.28013766 0.16944122 137.94682312 0.11691542
		 -0.1389637 132.41438293 0.28013766 -0.27448273 132.50737 0.11691542 0.21276474 132.81626892 0.28013766
		 0.13791656 132.97857666 0.11691542 0.42381477 131.54000854 0.28013766 0.56777191 131.44467163 0.11691542
		 0.87957382 131.8891449 0.28013766 0.92661285 131.71957397 0.11691542 0.82390404 132.82377625 0.28013766
		 0.8406601 132.98721313 0.11691542 2.3731041 132.48283386 0.28013766 2.42613983 132.63829041 0.11691542
		 1.39544296 131.83084106 0.28013766 1.34793866 131.67195129 0.11691542;
	setAttr ".vt[166:191]" 2.24206924 131.40240479 0.28013766 2.16266608 131.25965881 0.11691542
		 -0.80082321 131.15493774 0.28013766 -0.9524917 131.2171936 0.11691542 0.13921356 130.43806458 0.28013766
		 0.29837799 130.40161133 0.11691542 -1.23714447 129.7202301 0.28013766 -1.40923309 129.71534729 0.11691542
		 -1.072216034 129.27114868 0.28013766 -1.20731354 129.1655426 0.11691542 -0.046922684 129.50785828 0.28013766
		 0.10564424 129.43844604 0.11691542 -0.35754776 129.10473633 0.28013766 -0.2662735 128.95578003 0.11691542
		 -0.72519302 129.035873413 0.28013766 -0.76117706 128.86306763 0.11691542 3.55200577 131.92649841 0.28013766
		 3.67154694 132.050567627 0.11691542 3.72880912 131.58532715 0.28013766 3.89574432 131.61793518 0.11691542
		 2.94052505 130.97729492 0.28013766 2.89377594 130.81466675 0.11691542 3.39836121 130.97131348 0.28013766
		 3.45404816 130.80734253 0.11691542 3.69355369 131.2041626 0.28013766 3.84963226 131.11938477 0.11691542;
	setAttr -s 414 ".ed";
	setAttr ".ed[0:165]"  6 7 1 7 8 1 9 8 1 6 9 1 10 11 1 11 12 1 13 12 1 10 13 1
		 14 15 1 15 16 1 14 16 1 7 10 1 8 13 1 17 14 1 14 18 1 17 18 1 19 20 1 21 20 1 21 19 1
		 20 11 1 11 21 1 6 15 1 9 16 1 20 22 1 20 23 1 22 23 1 16 24 1 14 24 1 25 14 1 24 25 1
		 26 20 1 19 26 1 26 23 1 14 27 1 27 25 1 18 27 1 15 17 1 20 12 1 12 22 1 28 29 1 29 30 1
		 31 30 1 28 31 1 32 33 1 33 34 1 35 34 1 32 35 1 36 37 1 38 37 1 36 38 1 30 33 1 31 32 1
		 39 40 1 36 40 1 39 36 1 41 42 1 41 43 1 42 43 1 35 41 1 43 35 1 29 37 1 28 38 1 44 45 1
		 43 45 1 43 44 1 36 46 1 37 46 1 46 47 1 47 36 1 42 48 1 48 43 1 48 45 1 49 47 1 36 49 1
		 40 49 1 38 39 1 34 44 1 43 34 1 50 51 1 51 52 1 53 52 1 50 53 1 54 55 1 55 56 1 57 56 1
		 54 57 1 58 59 1 60 59 1 58 60 1 52 55 1 53 54 1 61 62 1 58 62 1 61 58 1 63 64 1 63 65 1
		 64 65 1 57 63 1 65 57 1 51 59 1 50 60 1 66 67 1 65 67 1 65 66 1 58 68 1 59 68 1 68 69 1
		 69 58 1 64 70 1 70 65 1 70 67 1 71 69 1 58 71 1 62 71 1 60 61 1 56 66 1 65 56 1 72 73 1
		 73 75 1 75 74 1 74 72 1 72 88 1 88 89 1 89 73 1 75 81 1 81 80 1 80 74 1 76 77 1 77 91 1
		 91 90 1 90 76 1 76 78 1 78 79 1 79 77 1 78 84 1 84 85 1 85 79 1 81 83 1 83 82 1 82 80 1
		 83 103 1 103 102 1 102 82 1 84 86 1 86 87 1 87 85 1 86 106 1 106 107 1 107 87 1 88 92 1
		 92 93 1 93 89 1 91 97 1 97 96 1 96 90 1 92 94 1 94 95 1 95 93 1 94 100 1 100 101 1
		 101 95 1 97 99 1 99 98 1 98 96 1 99 101 1 100 98 1;
	setAttr ".ed[166:331]" 103 105 1 105 104 1 104 102 1 105 111 1 111 110 1 110 104 1
		 106 108 1 108 109 1 109 107 1 108 110 1 111 109 1 112 113 1 113 129 1 129 128 1 128 112 1
		 112 114 1 114 115 1 115 113 1 114 120 1 120 121 1 121 115 1 116 117 1 117 119 1 119 118 1
		 118 116 1 116 130 1 130 131 1 131 117 1 119 125 1 125 124 1 124 118 1 120 122 1 122 123 1
		 123 121 1 122 142 1 142 143 1 143 123 1 125 127 1 127 126 1 126 124 1 127 147 1 147 146 1
		 146 126 1 129 133 1 133 132 1 132 128 1 130 136 1 136 137 1 137 131 1 133 135 1 135 134 1
		 134 132 1 135 141 1 141 140 1 140 134 1 136 138 1 138 139 1 139 137 1 138 140 1 141 139 1
		 142 144 1 144 145 1 145 143 1 144 150 1 150 151 1 151 145 1 147 149 1 149 148 1 148 146 1
		 149 151 1 150 148 1 152 153 1 153 169 1 169 168 1 168 152 1 152 154 1 154 155 1 155 153 1
		 154 160 1 160 161 1 161 155 1 156 157 1 157 159 1 159 158 1 158 156 1 156 170 1 170 171 1
		 171 157 1 159 165 1 165 164 1 164 158 1 160 162 1 162 163 1 163 161 1 162 182 1 182 183 1
		 183 163 1 165 167 1 167 166 1 166 164 1 167 187 1 187 186 1 186 166 1 169 173 1 173 172 1
		 172 168 1 170 176 1 176 177 1 177 171 1 173 175 1 175 174 1 174 172 1 175 181 1 181 180 1
		 180 174 1 176 178 1 178 179 1 179 177 1 178 180 1 181 179 1 182 184 1 184 185 1 185 183 1
		 184 190 1 190 191 1 191 185 1 187 189 1 189 188 1 188 186 1 189 191 1 190 188 1 74 78 1
		 76 72 1 82 86 1 84 80 1 1 88 1 88 90 1 90 1 1 92 1 1 1 94 1 104 0 1 0 102 1 0 82 1
		 106 0 1 0 108 1 96 1 1 98 1 1 110 0 1 100 1 1 86 0 1 112 116 1 118 114 1 120 124 1
		 126 122 1 3 130 1 130 128 1 128 3 1 134 3 1 3 132 1 142 2 1 2 144 1 122 2 1 148 2 1
		 2 146 1 3 136 1 3 138 1;
	setAttr ".ed[332:413]" 2 150 1 3 140 1 2 126 1 152 156 1 158 154 1 160 164 1
		 166 162 1 5 170 1 170 168 1 168 5 1 174 5 1 5 172 1 182 4 1 4 184 1 162 4 1 188 4 1
		 4 186 1 5 176 1 5 178 1 4 190 1 5 180 1 4 166 1 73 6 1 7 75 1 79 8 1 9 77 1 81 10 1
		 11 83 1 87 12 1 13 85 1 95 18 1 17 93 1 103 21 1 19 105 1 89 15 1 16 91 1 109 23 1
		 22 107 1 24 97 1 25 99 1 26 111 1 27 101 1 117 29 1 30 119 1 115 31 1 28 113 1 125 33 1
		 34 127 1 123 35 1 32 121 1 133 39 1 40 135 1 145 42 1 41 143 1 131 37 1 38 129 1
		 147 44 1 45 149 1 137 46 1 139 47 1 151 48 1 141 49 1 157 51 1 52 159 1 155 53 1
		 50 153 1 165 55 1 56 167 1 163 57 1 54 161 1 173 61 1 62 175 1 185 64 1 63 183 1
		 171 59 1 60 169 1 187 66 1 67 189 1 177 68 1 179 69 1 191 70 1 181 71 1;
	setAttr -s 228 -ch 828 ".fc[0:227]" -type "polyFaces" 
		f 4 3 2 -2 -1
		mu 0 4 0 1 2 3
		f 4 7 6 -6 -5
		mu 0 4 4 5 6 7
		f 3 10 -10 -9
		mu 0 3 8 9 10
		f 4 1 12 -8 -12
		mu 0 4 3 2 5 4
		f 3 15 -15 -14
		mu 0 3 11 12 8
		f 3 -19 17 -17
		mu 0 3 13 14 15
		f 3 -18 -21 -20
		mu 0 3 15 14 7
		f 4 9 -23 -4 21
		mu 0 4 10 9 1 0
		f 3 25 -25 23
		mu 0 3 16 17 15
		f 3 27 -27 -11
		mu 0 3 8 18 9
		f 3 -30 -28 -29
		mu 0 3 19 18 8
		f 3 -32 16 -31
		mu 0 3 20 13 15
		f 3 -33 30 24
		mu 0 3 17 20 15
		f 3 34 28 33
		mu 0 3 21 19 8
		f 3 35 -34 14
		mu 0 3 12 21 8
		f 3 36 13 8
		mu 0 3 10 11 8
		f 3 38 -24 37
		mu 0 3 6 16 15
		f 3 5 -38 19
		mu 0 3 7 6 15
		f 4 42 41 -41 -40
		mu 0 4 22 23 24 25
		f 4 46 45 -45 -44
		mu 0 4 26 27 28 29
		f 3 49 48 -48
		mu 0 3 30 31 32
		f 4 51 43 -51 -42
		mu 0 4 23 26 29 24
		f 3 54 53 -53
		mu 0 3 33 30 34
		f 3 57 -57 55
		mu 0 3 35 36 37
		f 3 59 58 56
		mu 0 3 36 27 37
		f 4 -62 39 60 -49
		mu 0 4 31 22 25 32
		f 3 -65 63 -63
		mu 0 3 38 36 39
		f 3 47 66 -66
		mu 0 3 30 32 40
		f 3 68 65 67
		mu 0 3 41 30 40
		f 3 70 -58 69
		mu 0 3 42 36 35
		f 3 -64 -71 71
		mu 0 3 39 36 42
		f 3 -74 -69 -73
		mu 0 3 43 30 41
		f 3 -54 73 -75
		mu 0 3 34 30 43
		f 3 -50 -55 -76
		mu 0 3 31 30 33
		f 3 -78 64 -77
		mu 0 3 28 36 38
		f 3 -60 77 -46
		mu 0 3 27 36 28
		f 4 81 80 -80 -79
		mu 0 4 44 45 46 47
		f 4 85 84 -84 -83
		mu 0 4 48 49 50 51
		f 3 88 87 -87
		mu 0 3 52 53 54
		f 4 90 82 -90 -81
		mu 0 4 45 48 51 46
		f 3 93 92 -92
		mu 0 3 55 52 56
		f 3 96 -96 94
		mu 0 3 57 58 59
		f 3 98 97 95
		mu 0 3 58 49 59
		f 4 -101 78 99 -88
		mu 0 4 53 44 47 54
		f 3 -104 102 -102
		mu 0 3 60 58 61
		f 3 86 105 -105
		mu 0 3 52 54 62
		f 3 107 104 106
		mu 0 3 63 52 62
		f 3 109 -97 108
		mu 0 3 64 58 57
		f 3 -103 -110 110
		mu 0 3 61 58 64
		f 3 -113 -108 -112
		mu 0 3 65 52 63
		f 3 -93 112 -114
		mu 0 3 56 52 65
		f 3 -89 -94 -115
		mu 0 3 53 52 55
		f 3 -117 103 -116
		mu 0 3 50 58 60
		f 3 -99 116 -85
		mu 0 3 49 58 50
		f 4 117 118 119 120
		mu 0 4 251 67 68 250
		f 4 -118 121 122 123
		mu 0 4 67 251 243 71
		f 4 -120 124 125 126
		mu 0 4 250 68 72 247
		f 4 127 128 129 130
		mu 0 4 249 75 76 242
		f 4 -128 131 132 133
		mu 0 4 75 249 248 79
		f 4 -133 134 135 136
		mu 0 4 79 248 245 81
		f 4 -126 137 138 139
		mu 0 4 247 72 82 246
		f 4 -139 140 141 142
		mu 0 4 246 82 84 236
		f 4 -136 143 144 145
		mu 0 4 81 245 244 87
		f 4 -145 146 147 148
		mu 0 4 87 244 234 89
		f 4 -123 149 150 151
		mu 0 4 71 243 241 91
		f 4 -130 152 153 154
		mu 0 4 242 76 92 239
		f 4 -151 155 156 157
		mu 0 4 91 241 240 95
		f 4 -157 158 159 160
		mu 0 4 95 240 237 97
		f 4 -154 161 162 163
		mu 0 4 239 92 98 238
		f 4 -163 164 -160 165
		mu 0 4 238 98 97 237
		f 4 -142 166 167 168
		mu 0 4 236 84 100 235
		f 4 -168 169 170 171
		mu 0 4 235 100 102 233
		f 4 -148 172 173 174
		mu 0 4 89 234 232 105
		f 4 -174 175 -171 176
		mu 0 4 105 232 233 102
		f 4 177 178 179 180
		mu 0 4 231 107 108 223
		f 4 -178 181 182 183
		mu 0 4 107 231 230 111
		f 4 -183 184 185 186
		mu 0 4 111 230 227 113
		f 4 187 188 189 190
		mu 0 4 229 115 116 228
		f 4 -188 191 192 193
		mu 0 4 115 229 222 119
		f 4 -190 194 195 196
		mu 0 4 228 116 120 225
		f 4 -186 197 198 199
		mu 0 4 113 227 226 123
		f 4 -199 200 201 202
		mu 0 4 123 226 216 125
		f 4 -196 203 204 205
		mu 0 4 225 120 126 224
		f 4 -205 206 207 208
		mu 0 4 224 126 128 214
		f 4 -180 209 210 211
		mu 0 4 223 108 130 221
		f 4 -193 212 213 214
		mu 0 4 119 222 219 133
		f 4 -211 215 216 217
		mu 0 4 221 130 134 220
		f 4 -217 218 219 220
		mu 0 4 220 134 136 218
		f 4 -214 221 222 223
		mu 0 4 133 219 217 139
		f 4 -223 224 -220 225
		mu 0 4 139 217 218 136
		f 4 -202 226 227 228
		mu 0 4 125 216 215 141
		f 4 -228 229 230 231
		mu 0 4 141 215 212 143
		f 4 -208 232 233 234
		mu 0 4 214 128 144 213
		f 4 -234 235 -231 236
		mu 0 4 213 144 143 212
		f 4 237 238 239 240
		mu 0 4 211 147 148 203
		f 4 -238 241 242 243
		mu 0 4 147 211 210 151
		f 4 -243 244 245 246
		mu 0 4 151 210 207 153
		f 4 247 248 249 250
		mu 0 4 209 155 156 208
		f 4 -248 251 252 253
		mu 0 4 155 209 202 159
		f 4 -250 254 255 256
		mu 0 4 208 156 160 205
		f 4 -246 257 258 259
		mu 0 4 153 207 206 163
		f 4 -259 260 261 262
		mu 0 4 163 206 196 165
		f 4 -256 263 264 265
		mu 0 4 205 160 166 204
		f 4 -265 266 267 268
		mu 0 4 204 166 168 194
		f 4 -240 269 270 271
		mu 0 4 203 148 170 201
		f 4 -253 272 273 274
		mu 0 4 159 202 199 173
		f 4 -271 275 276 277
		mu 0 4 201 170 174 200
		f 4 -277 278 279 280
		mu 0 4 200 174 176 198
		f 4 -274 281 282 283
		mu 0 4 173 199 197 179
		f 4 -283 284 -280 285
		mu 0 4 179 197 198 176
		f 4 -262 286 287 288
		mu 0 4 165 196 195 181
		f 4 -288 289 290 291
		mu 0 4 181 195 192 183
		f 4 -268 292 293 294
		mu 0 4 194 168 184 193
		f 4 -294 295 -291 296
		mu 0 4 193 184 183 192
		f 4 -121 297 -132 298
		mu 0 4 66 69 78 74
		f 4 -140 299 -144 300
		mu 0 4 73 83 86 80
		f 3 301 302 303
		mu 0 3 186 70 77
		f 4 -127 -301 -135 -298
		mu 0 4 69 73 80 78
		f 3 304 305 -156
		mu 0 3 90 186 94
		f 3 306 307 -169
		mu 0 3 101 187 85
		f 3 308 -143 -308
		mu 0 3 187 83 85
		f 4 -122 -299 -131 -303
		mu 0 4 70 66 74 77
		f 3 309 310 -173
		mu 0 3 88 187 104
		f 3 -304 -155 311
		mu 0 3 186 77 93
		f 3 312 -312 -164
		mu 0 3 99 186 93
		f 3 313 -307 -172
		mu 0 3 103 187 101
		f 3 -311 -314 -176
		mu 0 3 104 187 103
		f 3 314 -313 -166
		mu 0 3 96 186 99
		f 3 -306 -315 -159
		mu 0 3 94 186 96
		f 3 -302 -305 -150
		mu 0 3 70 186 90
		f 3 315 -310 -147
		mu 0 3 86 187 88
		f 3 -309 -316 -300
		mu 0 3 83 187 86
		f 4 316 -191 317 -182
		mu 0 4 106 114 117 110
		f 4 318 -206 319 -198
		mu 0 4 112 121 127 122
		f 3 320 321 322
		mu 0 3 188 118 109
		f 4 -318 -197 -319 -185
		mu 0 4 110 117 121 112
		f 3 -218 323 324
		mu 0 3 131 135 188
		f 3 -227 325 326
		mu 0 3 140 124 189
		f 3 -326 -201 327
		mu 0 3 189 124 122
		f 4 -322 -192 -317 -181
		mu 0 4 109 118 114 106
		f 3 -235 328 329
		mu 0 3 129 145 189
		f 3 330 -213 -321
		mu 0 3 188 132 118
		f 3 -222 -331 331
		mu 0 3 138 132 188
		f 3 -230 -327 332
		mu 0 3 142 140 189
		f 3 -237 -333 -329
		mu 0 3 145 142 189
		f 3 -225 -332 333
		mu 0 3 137 138 188
		f 3 -221 -334 -324
		mu 0 3 135 137 188
		f 3 -212 -325 -323
		mu 0 3 109 131 188
		f 3 -209 -330 334
		mu 0 3 127 129 189
		f 3 -320 -335 -328
		mu 0 3 122 127 189
		f 4 335 -251 336 -242
		mu 0 4 146 154 157 150
		f 4 337 -266 338 -258
		mu 0 4 152 161 167 162
		f 3 339 340 341
		mu 0 3 190 158 149
		f 4 -337 -257 -338 -245
		mu 0 4 150 157 161 152
		f 3 -278 342 343
		mu 0 3 171 175 190
		f 3 -287 344 345
		mu 0 3 180 164 191
		f 3 -345 -261 346
		mu 0 3 191 164 162
		f 4 -341 -252 -336 -241
		mu 0 4 149 158 154 146
		f 3 -295 347 348
		mu 0 3 169 185 191
		f 3 349 -273 -340
		mu 0 3 190 172 158
		f 3 -282 -350 350
		mu 0 3 178 172 190
		f 3 -290 -346 351
		mu 0 3 182 180 191
		f 3 -297 -352 -348
		mu 0 3 185 182 191
		f 3 -285 -351 352
		mu 0 3 177 178 190
		f 3 -281 -353 -343
		mu 0 3 175 177 190
		f 3 -272 -344 -342
		mu 0 3 149 171 190
		f 3 -269 -349 353
		mu 0 3 167 169 191
		f 3 -339 -354 -347
		mu 0 3 162 167 191
		f 4 354 0 355 -119
		mu 0 4 67 0 3 68
		f 4 356 -3 357 -134
		mu 0 4 79 2 1 75
		f 4 358 4 359 -138
		mu 0 4 72 4 7 82
		f 4 360 -7 361 -146
		mu 0 4 87 6 5 81
		f 4 -356 11 -359 -125
		mu 0 4 68 3 4 72
		f 4 -362 -13 -357 -137
		mu 0 4 81 5 2 79
		f 4 362 -16 363 -158
		mu 0 4 95 12 11 91
		f 4 364 18 365 -167
		mu 0 4 84 14 13 100
		f 4 -360 20 -365 -141
		mu 0 4 82 7 14 84
		f 4 366 -22 -355 -124
		mu 0 4 71 10 0 67
		f 4 -358 22 367 -129
		mu 0 4 75 1 9 76
		f 4 368 -26 369 -175
		mu 0 4 105 17 16 89
		f 4 -368 26 370 -153
		mu 0 4 76 9 18 92
		f 4 -371 29 371 -162
		mu 0 4 92 18 19 98
		f 4 -366 31 372 -170
		mu 0 4 100 13 20 102
		f 4 -373 32 -369 -177
		mu 0 4 102 20 17 105
		f 4 -372 -35 373 -165
		mu 0 4 98 19 21 97
		f 4 -374 -36 -363 -161
		mu 0 4 97 21 12 95
		f 4 -364 -37 -367 -152
		mu 0 4 91 11 10 71
		f 4 -370 -39 -361 -149
		mu 0 4 89 16 6 87
		f 4 374 40 375 -189
		mu 0 4 115 25 24 116
		f 4 376 -43 377 -184
		mu 0 4 111 23 22 107
		f 4 378 44 379 -204
		mu 0 4 120 29 28 126
		f 4 380 -47 381 -200
		mu 0 4 123 27 26 113
		f 4 -376 50 -379 -195
		mu 0 4 116 24 29 120
		f 4 -382 -52 -377 -187
		mu 0 4 113 26 23 111
		f 4 382 52 383 -216
		mu 0 4 130 33 34 134
		f 4 384 -56 385 -229
		mu 0 4 141 35 37 125
		f 4 -386 -59 -381 -203
		mu 0 4 125 37 27 123
		f 4 386 -61 -375 -194
		mu 0 4 119 32 25 115
		f 4 -378 61 387 -179
		mu 0 4 107 22 31 108
		f 4 388 62 389 -233
		mu 0 4 128 38 39 144
		f 4 390 -67 -387 -215
		mu 0 4 133 40 32 119
		f 4 391 -68 -391 -224
		mu 0 4 139 41 40 133
		f 4 392 -70 -385 -232
		mu 0 4 143 42 35 141
		f 4 -390 -72 -393 -236
		mu 0 4 144 39 42 143
		f 4 393 72 -392 -226
		mu 0 4 136 43 41 139
		f 4 -384 74 -394 -219
		mu 0 4 134 34 43 136
		f 4 -388 75 -383 -210
		mu 0 4 108 31 33 130
		f 4 -380 76 -389 -207
		mu 0 4 126 28 38 128
		f 4 394 79 395 -249
		mu 0 4 155 47 46 156
		f 4 396 -82 397 -244
		mu 0 4 151 45 44 147
		f 4 398 83 399 -264
		mu 0 4 160 51 50 166
		f 4 400 -86 401 -260
		mu 0 4 163 49 48 153
		f 4 -396 89 -399 -255
		mu 0 4 156 46 51 160
		f 4 -402 -91 -397 -247
		mu 0 4 153 48 45 151
		f 4 402 91 403 -276
		mu 0 4 170 55 56 174
		f 4 404 -95 405 -289
		mu 0 4 181 57 59 165
		f 4 -406 -98 -401 -263
		mu 0 4 165 59 49 163
		f 4 406 -100 -395 -254
		mu 0 4 159 54 47 155
		f 4 -398 100 407 -239
		mu 0 4 147 44 53 148
		f 4 408 101 409 -293
		mu 0 4 168 60 61 184
		f 4 410 -106 -407 -275
		mu 0 4 173 62 54 159
		f 4 411 -107 -411 -284
		mu 0 4 179 63 62 173
		f 4 412 -109 -405 -292
		mu 0 4 183 64 57 181
		f 4 -410 -111 -413 -296
		mu 0 4 184 61 64 183
		f 4 413 111 -412 -286
		mu 0 4 176 65 63 179
		f 4 -404 113 -414 -279
		mu 0 4 174 56 65 176
		f 4 -408 114 -403 -270
		mu 0 4 148 53 55 170
		f 4 -400 115 -409 -267
		mu 0 4 166 50 60 168;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "ShyL" -p "C000_Generic_01_PopUp";
	rename -uid "7EC73BE4-4CB8-6C22-E4C7-C39F8DF696B8";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" -4.76837158203125e-07 133.40493774414062 0 ;
	setAttr ".sp" -type "double3" -4.76837158203125e-07 133.40493774414062 0 ;
createNode mesh -n "ShyLShape" -p "ShyL";
	rename -uid "D8A62111-4F4F-7823-6ED8-788FEECE5125";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.78337683058887864 0.094797529316767937 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "ShyLShapeOrig" -p "ShyL";
	rename -uid "8227E17C-42E9-C6B8-7A49-F58E684DACCE";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 126 ".uvst[0].uvsp[0:125]" -type "float2" 0.39944556 0.038607687
		 0.38511628 0.03864494 0.39262205 0.033262879 0.3858344 0.027365789 0.40017343 0.027064756
		 0.38452578 0.036969543 0.3842141 0.032898396 0.38488641 0.028763145 0.40104455 0.033386201
		 0.4003602 0.03715089 0.40084088 0.029186517 0.38905951 0.080899715 0.39987335 0.040983975
		 0.40109676 0.038734287 0.38960803 0.079274856 0.38921383 0.11083484 0.38457763 0.040742308
		 0.3898313 0.11170977 0.38368404 0.038459033 0.3943173 0.078777611 0.4006817 0.024950057
		 0.38538802 0.024987906 0.39431706 0.10871488 0.39346993 0.077822238 0.40172622 0.027750984
		 0.38414592 0.027249351 0.39380774 0.11045301 0.39185199 0.11177284 0.38302431 0.032844245
		 0.40222847 0.03360039 0.39139006 0.077979118 0.39153418 0.094906241 0.39545459 0.019292131
		 0.39547682 0.048072845 0.39277261 0.033002943 0.38981265 0.046637148 0.38966036 0.01783241
		 0.39463571 0.049259543 0.39259171 0.049887538 0.39051485 0.048539549 0.39283389 0.016071837
		 0.39472386 0.017450023 0.39072526 0.016487163 0.3890453 0.080824561 0.39664823 0.018436365
		 0.39552015 0.015973825 0.38959676 0.079190925 0.38920021 0.11092129 0.39653033 0.049152941
		 0.38982096 0.11180097 0.39538491 0.050949037 0.39433157 0.07869114 0.38859755 0.016815495
		 0.38861912 0.047535419 0.39433104 0.1087901 0.39347962 0.077730589 0.39000177 0.014713068
		 0.38975593 0.050029159 0.39381903 0.11053756 0.39185262 0.11186448 0.39256647 0.052277744
		 0.39293987 0.013692785 0.39138851 0.077888265 0.39153329 0.094906777 0.38982511 0.046553791
		 0.38979656 0.018027902 0.39248186 0.03297314 0.39540875 0.019441083 0.39557591 0.04799664
		 0.39062929 0.016850322 0.39265394 0.01622504 0.39471215 0.017556787 0.39242688 0.049736142
		 0.39055127 0.048374295 0.39451873 0.049325287 0.38907391 0.080974549 0.38864243 0.04740721
		 0.38976443 0.049843609 0.38961959 0.07935901 0.38922298 0.11074406 0.38875198 0.016956836
		 0.38983685 0.11161453 0.38988626 0.01517579 0.3943029 0.078867242 0.39662907 0.049005449
		 0.39659131 0.018545777 0.39429826 0.10863876 0.39346033 0.077916667 0.39523438 0.051086485
		 0.39546353 0.016077489 0.3937915 0.110367 0.39184639 0.11167842 0.3926779 0.013855077
		 0.39232245 0.052093625 0.39139202 0.07807149 0.39153287 0.094904989 0.3957153 0.052011669
		 0.39227664 0.053347051 0.3892228 0.05085808 0.39268738 0.012612857 0.39596015 0.015017867
		 0.38936865 0.014322132 0.39728311 0.018272638 0.39730403 0.049133837 0.38807899 0.016723096
		 0.38795471 0.047635436 0.38951564 0.013781954 0.39298633 0.012429465 0.39606827 0.014954556
		 0.39255637 0.053530455 0.38925409 0.051096261 0.39590698 0.051810145 0.38792086 0.047807783
		 0.38791651 0.016685169 0.39720941 0.049388051 0.39734226 0.018207747 0.40219182 0.026787683
		 0.40285796 0.033694863 0.40160599 0.039822519 0.38240075 0.032821923 0.38361546 0.026248053
		 0.383255 0.039497912 0.38525328 0.023596823 0.40074819 0.023595273 0.38446119 0.042095244
		 0.39998904 0.042364657;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 96 ".vt[0:95]"  -0.039979935 133.42608643 0.12728143 -0.89583212 132.8510437 -0.12728131
		 -0.039979935 133.42608643 -0.12728131 0.23491001 134.55065918 -0.12728131 -0.27311039 132.25280762 -0.12728143
		 0.84143692 133.96615601 -0.12728135 0.39755535 134.55706787 -0.12728131 0.65493202 134.39532471 -0.12728131
		 0.84995031 134.14846802 -0.12728135 -0.89278603 132.67279053 -0.12728135 -0.71986961 132.44314575 -0.12728143
		 -0.4676151 132.26516724 -0.12728143 -0.81893158 132.82852173 0.12728143 -0.89583212 132.8510437 0.050776422
		 0.27696705 134.47573853 0.12728143 0.23491001 134.55065918 0.050776422 -0.31286812 132.33200073 0.12728143
		 -0.27311039 132.25280762 0.050776422 0.76598358 133.99047852 0.12728143 0.84143692 133.96615601 0.050776422
		 0.37690544 134.47970581 0.12728143 0.39755535 134.55706787 0.050776422 0.6030674 134.33755493 0.12728143
		 0.65493202 134.39532471 0.050776422 0.77219486 134.12347412 0.12728143 0.84995031 134.14846802 0.050776422
		 -0.81671721 132.69897461 0.12728143 -0.89278603 132.67279053 0.050776422 -0.66596603 132.49874878 0.12728143
		 -0.71986961 132.44314575 0.050776422 -0.44118023 132.34014893 0.12728143 -0.4676151 132.26516724 0.050776422
		 -1.36877728 133.42608643 0.12728143 -2.2246294 132.8510437 -0.12728131 -1.36877728 133.42608643 -0.12728131
		 -1.093887448 134.55065918 -0.12728131 -1.60190785 132.25280762 -0.12728143 -0.48736 133.96615601 -0.12728135
		 -0.93124205 134.55706787 -0.12728131 -0.67386532 134.39532471 -0.12728131 -0.47884652 134.14846802 -0.12728135
		 -2.22158337 132.67279053 -0.12728135 -2.048666 132.44314575 -0.12728143 -1.79641151 132.26516724 -0.12728143
		 -2.14772797 132.82852173 0.12728143 -2.2246294 132.8510437 0.050776422 -1.051830292 134.47573853 0.12728143
		 -1.093887448 134.55065918 0.050776422 -1.64166451 132.33200073 0.12728143 -1.60190785 132.25280762 0.050776422
		 -0.56281281 133.99047852 0.12728143 -0.48736 133.96615601 0.050776422 -0.95189184 134.47970581 0.12728143
		 -0.93124205 134.55706787 0.050776422 -0.72572899 134.33755493 0.12728143 -0.67386532 134.39532471 0.050776422
		 -0.55660248 134.12347412 0.12728143 -0.47884652 134.14846802 0.050776422 -2.14551449 132.69897461 0.12728143
		 -2.22158337 132.67279053 0.050776422 -1.99476242 132.49874878 0.12728143 -2.048666 132.44314575 0.050776422
		 -1.76997674 132.34014893 0.12728143 -1.79641151 132.26516724 0.050776422 1.33469784 133.42608643 0.12728143
		 0.4788456 132.8510437 -0.12728131 1.33469784 133.42608643 -0.12728131 1.60958862 134.55065918 -0.12728131
		 1.10156715 132.25280762 -0.12728143 2.216115 133.96615601 -0.12728135 1.77223396 134.55706787 -0.12728131
		 2.02960968 134.39532471 -0.12728131 2.22462845 134.14846802 -0.12728135 0.48189163 132.67279053 -0.12728135
		 0.654809 132.44314575 -0.12728143 0.90706348 132.26516724 -0.12728143 0.55574608 132.82852173 0.12728143
		 0.4788456 132.8510437 0.050776422 1.6516453 134.47573853 0.12728143 1.60958862 134.55065918 0.050776422
		 1.061810493 132.33200073 0.12728143 1.10156715 132.25280762 0.050776422 2.14066172 133.99047852 0.12728143
		 2.216115 133.96615601 0.050776422 1.75158358 134.47970581 0.12728143 1.77223396 134.55706787 0.050776422
		 1.97774601 134.33755493 0.12728143 2.02960968 134.39532471 0.050776422 2.146873 134.12347412 0.12728143
		 2.22462845 134.14846802 0.050776422 0.55796051 132.69897461 0.12728143 0.48189163 132.67279053 0.050776422
		 0.70871258 132.49874878 0.12728143 0.654809 132.44314575 0.050776422 0.93349785 132.34014893 0.12728143
		 0.90706348 132.26516724 0.050776422;
	setAttr -s 210 ".ed";
	setAttr ".ed[0:165]"  1 2 1 3 2 1 1 3 1 2 4 1 4 5 1 2 5 1 6 2 1 2 7 1 6 7 1
		 2 8 1 7 8 1 2 9 1 9 10 1 2 10 1 11 2 1 10 11 1 3 6 1 5 8 1 4 11 1 1 9 1 12 13 1 13 27 1
		 27 26 1 26 12 1 12 14 1 14 15 1 15 13 1 14 20 1 20 21 1 21 15 1 16 17 1 17 19 1 19 18 1
		 18 16 1 16 30 1 30 31 1 31 17 1 19 25 1 25 24 1 24 18 1 20 22 1 22 23 1 23 21 1 22 24 1
		 25 23 1 27 29 1 29 28 1 28 26 1 29 31 1 30 28 1 12 0 1 0 14 1 0 16 1 18 0 1 20 0 1
		 0 22 1 0 24 1 0 26 1 28 0 1 30 0 1 15 3 1 1 13 1 17 4 1 5 19 1 23 7 1 6 21 1 25 8 1
		 27 9 1 10 29 1 11 31 1 33 34 1 35 34 1 33 35 1 34 36 1 36 37 1 34 37 1 38 34 1 34 39 1
		 38 39 1 34 40 1 39 40 1 34 41 1 41 42 1 34 42 1 43 34 1 42 43 1 35 38 1 37 40 1 36 43 1
		 33 41 1 44 45 1 45 59 1 59 58 1 58 44 1 44 46 1 46 47 1 47 45 1 46 52 1 52 53 1 53 47 1
		 48 49 1 49 51 1 51 50 1 50 48 1 48 62 1 62 63 1 63 49 1 51 57 1 57 56 1 56 50 1 52 54 1
		 54 55 1 55 53 1 54 56 1 57 55 1 59 61 1 61 60 1 60 58 1 61 63 1 62 60 1 44 32 1 32 46 1
		 32 48 1 50 32 1 52 32 1 32 54 1 32 56 1 32 58 1 60 32 1 62 32 1 47 35 1 33 45 1 49 36 1
		 37 51 1 55 39 1 38 53 1 57 40 1 59 41 1 42 61 1 43 63 1 65 66 1 67 66 1 65 67 1 66 68 1
		 68 69 1 66 69 1 70 66 1 66 71 1 70 71 1 66 72 1 71 72 1 66 73 1 73 74 1 66 74 1 75 66 1
		 74 75 1 67 70 1 69 72 1 68 75 1 65 73 1 76 77 1 77 91 1 91 90 1 90 76 1 76 78 1 78 79 1;
	setAttr ".ed[166:209]" 79 77 1 78 84 1 84 85 1 85 79 1 80 81 1 81 83 1 83 82 1
		 82 80 1 80 94 1 94 95 1 95 81 1 83 89 1 89 88 1 88 82 1 84 86 1 86 87 1 87 85 1 86 88 1
		 89 87 1 91 93 1 93 92 1 92 90 1 93 95 1 94 92 1 76 64 1 64 78 1 64 80 1 82 64 1 84 64 1
		 64 86 1 64 88 1 64 90 1 92 64 1 94 64 1 79 67 1 65 77 1 81 68 1 69 83 1 87 71 1 70 85 1
		 89 72 1 91 73 1 74 93 1 75 95 1;
	setAttr -s 120 -ch 420 ".fc[0:119]" -type "polyFaces" 
		f 3 2 1 -1
		mu 0 3 0 1 2
		f 3 5 -5 -4
		mu 0 3 2 3 4
		f 3 8 -8 -7
		mu 0 3 5 6 2
		f 3 7 10 -10
		mu 0 3 2 6 7
		f 3 13 -13 -12
		mu 0 3 2 8 9
		f 3 -16 -14 -15
		mu 0 3 10 8 2
		f 3 16 6 -2
		mu 0 3 1 5 2
		f 3 9 -18 -6
		mu 0 3 2 7 3
		f 3 18 14 3
		mu 0 3 4 10 2
		f 3 11 -20 0
		mu 0 3 2 9 0
		f 4 20 21 22 23
		mu 0 4 125 12 13 118
		f 4 -21 24 25 26
		mu 0 4 12 125 124 16
		f 4 -26 27 28 29
		mu 0 4 16 124 121 18
		f 4 30 31 32 33
		mu 0 4 123 20 21 122
		f 4 -31 34 35 36
		mu 0 4 20 123 116 24
		f 4 -33 37 38 39
		mu 0 4 122 21 25 120
		f 4 -29 40 41 42
		mu 0 4 18 121 119 28
		f 4 -42 43 -39 44
		mu 0 4 28 119 120 25
		f 4 -23 45 46 47
		mu 0 4 118 13 29 117
		f 4 -47 48 -36 49
		mu 0 4 117 29 24 116
		f 3 50 51 -25
		mu 0 3 11 31 15
		f 3 52 -34 53
		mu 0 3 31 19 22
		f 3 54 55 -41
		mu 0 3 17 31 27
		f 3 56 -44 -56
		mu 0 3 31 26 27
		f 3 57 -48 58
		mu 0 3 31 14 30
		f 3 59 -59 -50
		mu 0 3 23 31 30
		f 3 -52 -55 -28
		mu 0 3 15 31 17
		f 3 -54 -40 -57
		mu 0 3 31 22 26
		f 3 -53 -60 -35
		mu 0 3 19 31 23
		f 3 -51 -24 -58
		mu 0 3 31 11 14
		f 4 60 -3 61 -27
		mu 0 4 16 1 0 12
		f 4 62 4 63 -32
		mu 0 4 20 4 3 21
		f 4 64 -9 65 -43
		mu 0 4 28 6 5 18
		f 4 66 -11 -65 -45
		mu 0 4 25 7 6 28
		f 4 67 12 68 -46
		mu 0 4 13 9 8 29
		f 4 -69 15 69 -49
		mu 0 4 29 8 10 24
		f 4 -66 -17 -61 -30
		mu 0 4 18 5 1 16
		f 4 -64 17 -67 -38
		mu 0 4 21 3 7 25
		f 4 -70 -19 -63 -37
		mu 0 4 24 10 4 20
		f 4 -62 19 -68 -22
		mu 0 4 12 0 9 13
		f 3 72 71 -71
		mu 0 3 32 33 34
		f 3 75 -75 -74
		mu 0 3 34 35 36
		f 3 78 -78 -77
		mu 0 3 37 38 34
		f 3 77 80 -80
		mu 0 3 34 38 39
		f 3 83 -83 -82
		mu 0 3 34 40 41
		f 3 -86 -84 -85
		mu 0 3 42 40 34
		f 3 86 76 -72
		mu 0 3 33 37 34
		f 3 79 -88 -76
		mu 0 3 34 39 35
		f 3 88 84 73
		mu 0 3 36 42 34
		f 3 81 -90 70
		mu 0 3 34 41 32
		f 4 90 91 92 93
		mu 0 4 115 44 45 108
		f 4 -91 94 95 96
		mu 0 4 44 115 114 48
		f 4 -96 97 98 99
		mu 0 4 48 114 111 50
		f 4 100 101 102 103
		mu 0 4 113 52 53 112
		f 4 -101 104 105 106
		mu 0 4 52 113 106 56
		f 4 -103 107 108 109
		mu 0 4 112 53 57 110
		f 4 -99 110 111 112
		mu 0 4 50 111 109 60
		f 4 -112 113 -109 114
		mu 0 4 60 109 110 57
		f 4 -93 115 116 117
		mu 0 4 108 45 61 107
		f 4 -117 118 -106 119
		mu 0 4 107 61 56 106
		f 3 120 121 -95
		mu 0 3 43 63 47
		f 3 122 -104 123
		mu 0 3 63 51 54
		f 3 124 125 -111
		mu 0 3 49 63 59
		f 3 126 -114 -126
		mu 0 3 63 58 59
		f 3 127 -118 128
		mu 0 3 63 46 62
		f 3 129 -129 -120
		mu 0 3 55 63 62
		f 3 -122 -125 -98
		mu 0 3 47 63 49
		f 3 -124 -110 -127
		mu 0 3 63 54 58
		f 3 -123 -130 -105
		mu 0 3 51 63 55
		f 3 -121 -94 -128
		mu 0 3 63 43 46
		f 4 130 -73 131 -97
		mu 0 4 48 33 32 44
		f 4 132 74 133 -102
		mu 0 4 52 36 35 53
		f 4 134 -79 135 -113
		mu 0 4 60 38 37 50
		f 4 136 -81 -135 -115
		mu 0 4 57 39 38 60
		f 4 137 82 138 -116
		mu 0 4 45 41 40 61
		f 4 -139 85 139 -119
		mu 0 4 61 40 42 56
		f 4 -136 -87 -131 -100
		mu 0 4 50 37 33 48
		f 4 -134 87 -137 -108
		mu 0 4 53 35 39 57
		f 4 -140 -89 -133 -107
		mu 0 4 56 42 36 52
		f 4 -132 89 -138 -92
		mu 0 4 44 32 41 45
		f 3 142 141 -141
		mu 0 3 64 65 66
		f 3 145 -145 -144
		mu 0 3 66 67 68
		f 3 148 -148 -147
		mu 0 3 69 70 66
		f 3 147 150 -150
		mu 0 3 66 70 71
		f 3 153 -153 -152
		mu 0 3 66 72 73
		f 3 -156 -154 -155
		mu 0 3 74 72 66
		f 3 156 146 -142
		mu 0 3 65 69 66
		f 3 149 -158 -146
		mu 0 3 66 71 67
		f 3 158 154 143
		mu 0 3 68 74 66
		f 3 151 -160 140
		mu 0 3 66 73 64
		f 4 160 161 162 163
		mu 0 4 105 76 77 98
		f 4 -161 164 165 166
		mu 0 4 76 105 104 80
		f 4 -166 167 168 169
		mu 0 4 80 104 101 82
		f 4 170 171 172 173
		mu 0 4 103 84 85 102
		f 4 -171 174 175 176
		mu 0 4 84 103 96 88
		f 4 -173 177 178 179
		mu 0 4 102 85 89 100
		f 4 -169 180 181 182
		mu 0 4 82 101 99 92
		f 4 -182 183 -179 184
		mu 0 4 92 99 100 89
		f 4 -163 185 186 187
		mu 0 4 98 77 93 97
		f 4 -187 188 -176 189
		mu 0 4 97 93 88 96
		f 3 190 191 -165
		mu 0 3 75 95 79
		f 3 192 -174 193
		mu 0 3 95 83 86
		f 3 194 195 -181
		mu 0 3 81 95 91
		f 3 196 -184 -196
		mu 0 3 95 90 91
		f 3 197 -188 198
		mu 0 3 95 78 94
		f 3 199 -199 -190
		mu 0 3 87 95 94
		f 3 -192 -195 -168
		mu 0 3 79 95 81
		f 3 -194 -180 -197
		mu 0 3 95 86 90
		f 3 -193 -200 -175
		mu 0 3 83 95 87
		f 3 -191 -164 -198
		mu 0 3 95 75 78
		f 4 200 -143 201 -167
		mu 0 4 80 65 64 76
		f 4 202 144 203 -172
		mu 0 4 84 68 67 85
		f 4 204 -149 205 -183
		mu 0 4 92 70 69 82
		f 4 206 -151 -205 -185
		mu 0 4 89 71 70 92
		f 4 207 152 208 -186
		mu 0 4 77 73 72 93
		f 4 -209 155 209 -189
		mu 0 4 93 72 74 88
		f 4 -206 -157 -201 -170
		mu 0 4 82 69 65 80
		f 4 -204 157 -207 -178
		mu 0 4 85 67 71 89
		f 4 -210 -159 -203 -177
		mu 0 4 88 74 68 84
		f 4 -202 159 -208 -162
		mu 0 4 76 64 73 77;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -n "ShyR" -p "C000_Generic_01_PopUp";
	rename -uid "84A697C8-4DC5-4B1E-01A3-6DB1AC8042E2";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 133.40493774414062 0 ;
	setAttr ".sp" -type "double3" 0 133.40493774414062 0 ;
createNode mesh -n "ShyRShape" -p "ShyR";
	rename -uid "C4DBC23A-4585-2A6A-3F23-B0B9FB0B3D6D";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcol" yes;
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
createNode mesh -n "ShyRShapeOrig" -p "ShyR";
	rename -uid "E18A70F2-4548-C4FF-5ED4-A2B3D7E2AF95";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 126 ".uvst[0].uvsp[0:125]" -type "float2" 0.39944556 0.038607687
		 0.38511628 0.03864494 0.39262205 0.033262879 0.3858344 0.027365789 0.40017343 0.027064756
		 0.38452578 0.036969543 0.3842141 0.032898396 0.38488641 0.028763145 0.40104455 0.033386201
		 0.4003602 0.03715089 0.40084088 0.029186517 0.38905951 0.080899715 0.39987335 0.040983975
		 0.40109676 0.038734287 0.38960803 0.079274856 0.38921383 0.11083484 0.38457763 0.040742308
		 0.3898313 0.11170977 0.38368404 0.038459033 0.3943173 0.078777611 0.4006817 0.024950057
		 0.38538802 0.024987906 0.39431706 0.10871488 0.39346993 0.077822238 0.40172622 0.027750984
		 0.38414592 0.027249351 0.39380774 0.11045301 0.39185199 0.11177284 0.38302431 0.032844245
		 0.40222847 0.03360039 0.39139006 0.077979118 0.39153418 0.094906241 0.39545459 0.019292131
		 0.39547682 0.048072845 0.39277261 0.033002943 0.38981265 0.046637148 0.38966036 0.01783241
		 0.39463571 0.049259543 0.39259171 0.049887538 0.39051485 0.048539549 0.39283389 0.016071837
		 0.39472386 0.017450023 0.39072526 0.016487163 0.3890453 0.080824561 0.39664823 0.018436365
		 0.39552015 0.015973825 0.38959676 0.079190925 0.38920021 0.11092129 0.39653033 0.049152941
		 0.38982096 0.11180097 0.39538491 0.050949037 0.39433157 0.07869114 0.38859755 0.016815495
		 0.38861912 0.047535419 0.39433104 0.1087901 0.39347962 0.077730589 0.39000177 0.014713068
		 0.38975593 0.050029159 0.39381903 0.11053756 0.39185262 0.11186448 0.39256647 0.052277744
		 0.39293987 0.013692785 0.39138851 0.077888265 0.39153329 0.094906777 0.38982511 0.046553791
		 0.38979656 0.018027902 0.39248186 0.03297314 0.39540875 0.019441083 0.39557591 0.04799664
		 0.39062929 0.016850322 0.39265394 0.01622504 0.39471215 0.017556787 0.39242688 0.049736142
		 0.39055127 0.048374295 0.39451873 0.049325287 0.38907391 0.080974549 0.38864243 0.04740721
		 0.38976443 0.049843609 0.38961959 0.07935901 0.38922298 0.11074406 0.38875198 0.016956836
		 0.38983685 0.11161453 0.38988626 0.01517579 0.3943029 0.078867242 0.39662907 0.049005449
		 0.39659131 0.018545777 0.39429826 0.10863876 0.39346033 0.077916667 0.39523438 0.051086485
		 0.39546353 0.016077489 0.3937915 0.110367 0.39184639 0.11167842 0.3926779 0.013855077
		 0.39232245 0.052093625 0.39139202 0.07807149 0.39153287 0.094904989 0.3957153 0.052011669
		 0.39227664 0.053347051 0.3892228 0.05085808 0.39268738 0.012612857 0.39596015 0.015017867
		 0.38936865 0.014322132 0.39728311 0.018272638 0.39730403 0.049133837 0.38807899 0.016723096
		 0.38795471 0.047635436 0.38951564 0.013781954 0.39298633 0.012429465 0.39606827 0.014954556
		 0.39255637 0.053530455 0.38925409 0.051096261 0.39590698 0.051810145 0.38792086 0.047807783
		 0.38791651 0.016685169 0.39720941 0.049388051 0.39734226 0.018207747 0.40219182 0.026787683
		 0.40285796 0.033694863 0.40160599 0.039822519 0.38240075 0.032821923 0.38361546 0.026248053
		 0.383255 0.039497912 0.38525328 0.023596823 0.40074819 0.023595273 0.38446119 0.042095244
		 0.39998904 0.042364657;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcol" yes;
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 96 ".vt[0:95]"  -1.3687768 133.42607117 0.12728143 -2.22462893 132.85102844 -0.12728131
		 -1.3687768 133.42607117 -0.12728131 -1.093885899 134.55064392 -0.12728131 -1.60190725 132.25280762 -0.12728143
		 -0.48735952 133.96615601 -0.12728135 -0.93124098 134.55706787 -0.12728131 -0.67386484 134.39532471 -0.12728131
		 -0.47884607 134.14846802 -0.12728135 -2.22158289 132.67279053 -0.12728135 -2.048665524 132.44314575 -0.12728143
		 -1.79641104 132.26516724 -0.12728143 -2.14772797 132.82850647 0.12728143 -2.22462893 132.85102844 0.050776422
		 -1.051829457 134.47573853 0.12728143 -1.093885899 134.55064392 0.050776422 -1.64166415 132.33200073 0.12728143
		 -1.60190725 132.25280762 0.050776422 -0.56281281 133.99046326 0.12728143 -0.48735952 133.96615601 0.050776422
		 -0.95189136 134.47969055 0.12728143 -0.93124098 134.55706787 0.050776422 -0.72572851 134.33755493 0.12728143
		 -0.67386484 134.39532471 0.050776422 -0.55660152 134.12347412 0.12728143 -0.47884607 134.14846802 0.050776422
		 -2.14551401 132.69895935 0.12728143 -2.22158289 132.67279053 0.050776422 -1.99476194 132.49874878 0.12728143
		 -2.048665524 132.44314575 0.050776422 -1.76997674 132.34014893 0.12728143 -1.79641104 132.26516724 0.050776422
		 -0.039979935 133.42607117 0.12728143 -0.89583212 132.85102844 -0.12728131 -0.039979935 133.42607117 -0.12728131
		 0.23491096 134.55064392 -0.12728131 -0.27311039 132.25280762 -0.12728143 0.8414374 133.96615601 -0.12728135
		 0.3975558 134.55706787 -0.12728131 0.65493202 134.39532471 -0.12728131 0.84995031 134.14846802 -0.12728135
		 -0.89278603 132.67279053 -0.12728135 -0.71986866 132.44314575 -0.12728143 -0.46761417 132.26516724 -0.12728143
		 -0.8189311 132.82850647 0.12728143 -0.89583212 132.85102844 0.050776422 0.27696705 134.47573853 0.12728143
		 0.23491096 134.55064392 0.050776422 -0.31286716 132.33200073 0.12728143 -0.27311039 132.25280762 0.050776422
		 0.76598406 133.99046326 0.12728143 0.8414374 133.96615601 0.050776422 0.37690544 134.47969055 0.12728143
		 0.3975558 134.55706787 0.050776422 0.60306787 134.33755493 0.12728143 0.65493202 134.39532471 0.050776422
		 0.77219534 134.12347412 0.12728143 0.84995031 134.14846802 0.050776422 -0.81671721 132.69895935 0.12728143
		 -0.89278603 132.67279053 0.050776422 -0.66596508 132.49874878 0.12728143 -0.71986866 132.44314575 0.050776422
		 -0.44117975 132.34014893 0.12728143 -0.46761417 132.26516724 0.050776422 1.33469784 133.42607117 0.12728143
		 0.47884607 132.85102844 -0.12728131 1.33469784 133.42607117 -0.12728131 1.60958922 134.55064392 -0.12728131
		 1.10156775 132.25280762 -0.12728143 2.21611547 133.96615601 -0.12728135 1.77223444 134.55706787 -0.12728131
		 2.029610157 134.39532471 -0.12728131 2.22462893 134.14846802 -0.12728135 0.48189163 132.67279053 -0.12728135
		 0.65480947 132.44314575 -0.12728143 0.90706348 132.26516724 -0.12728143 0.55574703 132.82850647 0.12728143
		 0.47884607 132.85102844 0.050776422 1.6516453 134.47573853 0.12728143 1.60958922 134.55064392 0.050776422
		 1.061810493 132.33200073 0.12728143 1.10156775 132.25280762 0.050776422 2.14066267 133.99046326 0.12728143
		 2.21611547 133.96615601 0.050776422 1.75158358 134.47969055 0.12728143 1.77223444 134.55706787 0.050776422
		 1.97774661 134.33755493 0.12728143 2.029610157 134.39532471 0.050776422 2.14687395 134.12347412 0.12728143
		 2.22462893 134.14846802 0.050776422 0.55796051 132.69895935 0.12728143 0.48189163 132.67279053 0.050776422
		 0.70871258 132.49874878 0.12728143 0.65480947 132.44314575 0.050776422 0.93349844 132.34014893 0.12728143
		 0.90706348 132.26516724 0.050776422;
	setAttr -s 210 ".ed";
	setAttr ".ed[0:165]"  1 2 1 3 2 1 1 3 1 2 4 1 4 5 1 2 5 1 6 2 1 2 7 1 6 7 1
		 2 8 1 7 8 1 2 9 1 9 10 1 2 10 1 11 2 1 10 11 1 3 6 1 5 8 1 4 11 1 1 9 1 12 13 1 13 27 1
		 27 26 1 26 12 1 12 14 1 14 15 1 15 13 1 14 20 1 20 21 1 21 15 1 16 17 1 17 19 1 19 18 1
		 18 16 1 16 30 1 30 31 1 31 17 1 19 25 1 25 24 1 24 18 1 20 22 1 22 23 1 23 21 1 22 24 1
		 25 23 1 27 29 1 29 28 1 28 26 1 29 31 1 30 28 1 12 0 1 0 14 1 0 16 1 18 0 1 20 0 1
		 0 22 1 0 24 1 0 26 1 28 0 1 30 0 1 15 3 1 1 13 1 17 4 1 5 19 1 23 7 1 6 21 1 25 8 1
		 27 9 1 10 29 1 11 31 1 33 34 1 35 34 1 33 35 1 34 36 1 36 37 1 34 37 1 38 34 1 34 39 1
		 38 39 1 34 40 1 39 40 1 34 41 1 41 42 1 34 42 1 43 34 1 42 43 1 35 38 1 37 40 1 36 43 1
		 33 41 1 44 45 1 45 59 1 59 58 1 58 44 1 44 46 1 46 47 1 47 45 1 46 52 1 52 53 1 53 47 1
		 48 49 1 49 51 1 51 50 1 50 48 1 48 62 1 62 63 1 63 49 1 51 57 1 57 56 1 56 50 1 52 54 1
		 54 55 1 55 53 1 54 56 1 57 55 1 59 61 1 61 60 1 60 58 1 61 63 1 62 60 1 44 32 1 32 46 1
		 32 48 1 50 32 1 52 32 1 32 54 1 32 56 1 32 58 1 60 32 1 62 32 1 47 35 1 33 45 1 49 36 1
		 37 51 1 55 39 1 38 53 1 57 40 1 59 41 1 42 61 1 43 63 1 65 66 1 67 66 1 65 67 1 66 68 1
		 68 69 1 66 69 1 70 66 1 66 71 1 70 71 1 66 72 1 71 72 1 66 73 1 73 74 1 66 74 1 75 66 1
		 74 75 1 67 70 1 69 72 1 68 75 1 65 73 1 76 77 1 77 91 1 91 90 1 90 76 1 76 78 1 78 79 1;
	setAttr ".ed[166:209]" 79 77 1 78 84 1 84 85 1 85 79 1 80 81 1 81 83 1 83 82 1
		 82 80 1 80 94 1 94 95 1 95 81 1 83 89 1 89 88 1 88 82 1 84 86 1 86 87 1 87 85 1 86 88 1
		 89 87 1 91 93 1 93 92 1 92 90 1 93 95 1 94 92 1 76 64 1 64 78 1 64 80 1 82 64 1 84 64 1
		 64 86 1 64 88 1 64 90 1 92 64 1 94 64 1 79 67 1 65 77 1 81 68 1 69 83 1 87 71 1 70 85 1
		 89 72 1 91 73 1 74 93 1 75 95 1;
	setAttr -s 120 -ch 420 ".fc[0:119]" -type "polyFaces" 
		f 3 2 1 -1
		mu 0 3 0 1 2
		f 3 5 -5 -4
		mu 0 3 2 3 4
		f 3 8 -8 -7
		mu 0 3 5 6 2
		f 3 7 10 -10
		mu 0 3 2 6 7
		f 3 13 -13 -12
		mu 0 3 2 8 9
		f 3 -16 -14 -15
		mu 0 3 10 8 2
		f 3 16 6 -2
		mu 0 3 1 5 2
		f 3 9 -18 -6
		mu 0 3 2 7 3
		f 3 18 14 3
		mu 0 3 4 10 2
		f 3 11 -20 0
		mu 0 3 2 9 0
		f 4 20 21 22 23
		mu 0 4 125 12 13 118
		f 4 -21 24 25 26
		mu 0 4 12 125 124 16
		f 4 -26 27 28 29
		mu 0 4 16 124 121 18
		f 4 30 31 32 33
		mu 0 4 123 20 21 122
		f 4 -31 34 35 36
		mu 0 4 20 123 116 24
		f 4 -33 37 38 39
		mu 0 4 122 21 25 120
		f 4 -29 40 41 42
		mu 0 4 18 121 119 28
		f 4 -42 43 -39 44
		mu 0 4 28 119 120 25
		f 4 -23 45 46 47
		mu 0 4 118 13 29 117
		f 4 -47 48 -36 49
		mu 0 4 117 29 24 116
		f 3 50 51 -25
		mu 0 3 11 31 15
		f 3 52 -34 53
		mu 0 3 31 19 22
		f 3 54 55 -41
		mu 0 3 17 31 27
		f 3 56 -44 -56
		mu 0 3 31 26 27
		f 3 57 -48 58
		mu 0 3 31 14 30
		f 3 59 -59 -50
		mu 0 3 23 31 30
		f 3 -52 -55 -28
		mu 0 3 15 31 17
		f 3 -54 -40 -57
		mu 0 3 31 22 26
		f 3 -53 -60 -35
		mu 0 3 19 31 23
		f 3 -51 -24 -58
		mu 0 3 31 11 14
		f 4 60 -3 61 -27
		mu 0 4 16 1 0 12
		f 4 62 4 63 -32
		mu 0 4 20 4 3 21
		f 4 64 -9 65 -43
		mu 0 4 28 6 5 18
		f 4 66 -11 -65 -45
		mu 0 4 25 7 6 28
		f 4 67 12 68 -46
		mu 0 4 13 9 8 29
		f 4 -69 15 69 -49
		mu 0 4 29 8 10 24
		f 4 -66 -17 -61 -30
		mu 0 4 18 5 1 16
		f 4 -64 17 -67 -38
		mu 0 4 21 3 7 25
		f 4 -70 -19 -63 -37
		mu 0 4 24 10 4 20
		f 4 -62 19 -68 -22
		mu 0 4 12 0 9 13
		f 3 72 71 -71
		mu 0 3 32 33 34
		f 3 75 -75 -74
		mu 0 3 34 35 36
		f 3 78 -78 -77
		mu 0 3 37 38 34
		f 3 77 80 -80
		mu 0 3 34 38 39
		f 3 83 -83 -82
		mu 0 3 34 40 41
		f 3 -86 -84 -85
		mu 0 3 42 40 34
		f 3 86 76 -72
		mu 0 3 33 37 34
		f 3 79 -88 -76
		mu 0 3 34 39 35
		f 3 88 84 73
		mu 0 3 36 42 34
		f 3 81 -90 70
		mu 0 3 34 41 32
		f 4 90 91 92 93
		mu 0 4 115 44 45 108
		f 4 -91 94 95 96
		mu 0 4 44 115 114 48
		f 4 -96 97 98 99
		mu 0 4 48 114 111 50
		f 4 100 101 102 103
		mu 0 4 113 52 53 112
		f 4 -101 104 105 106
		mu 0 4 52 113 106 56
		f 4 -103 107 108 109
		mu 0 4 112 53 57 110
		f 4 -99 110 111 112
		mu 0 4 50 111 109 60
		f 4 -112 113 -109 114
		mu 0 4 60 109 110 57
		f 4 -93 115 116 117
		mu 0 4 108 45 61 107
		f 4 -117 118 -106 119
		mu 0 4 107 61 56 106
		f 3 120 121 -95
		mu 0 3 43 63 47
		f 3 122 -104 123
		mu 0 3 63 51 54
		f 3 124 125 -111
		mu 0 3 49 63 59
		f 3 126 -114 -126
		mu 0 3 63 58 59
		f 3 127 -118 128
		mu 0 3 63 46 62
		f 3 129 -129 -120
		mu 0 3 55 63 62
		f 3 -122 -125 -98
		mu 0 3 47 63 49
		f 3 -124 -110 -127
		mu 0 3 63 54 58
		f 3 -123 -130 -105
		mu 0 3 51 63 55
		f 3 -121 -94 -128
		mu 0 3 63 43 46
		f 4 130 -73 131 -97
		mu 0 4 48 33 32 44
		f 4 132 74 133 -102
		mu 0 4 52 36 35 53
		f 4 134 -79 135 -113
		mu 0 4 60 38 37 50
		f 4 136 -81 -135 -115
		mu 0 4 57 39 38 60
		f 4 137 82 138 -116
		mu 0 4 45 41 40 61
		f 4 -139 85 139 -119
		mu 0 4 61 40 42 56
		f 4 -136 -87 -131 -100
		mu 0 4 50 37 33 48
		f 4 -134 87 -137 -108
		mu 0 4 53 35 39 57
		f 4 -140 -89 -133 -107
		mu 0 4 56 42 36 52
		f 4 -132 89 -138 -92
		mu 0 4 44 32 41 45
		f 3 142 141 -141
		mu 0 3 64 65 66
		f 3 145 -145 -144
		mu 0 3 66 67 68
		f 3 148 -148 -147
		mu 0 3 69 70 66
		f 3 147 150 -150
		mu 0 3 66 70 71
		f 3 153 -153 -152
		mu 0 3 66 72 73
		f 3 -156 -154 -155
		mu 0 3 74 72 66
		f 3 156 146 -142
		mu 0 3 65 69 66
		f 3 149 -158 -146
		mu 0 3 66 71 67
		f 3 158 154 143
		mu 0 3 68 74 66
		f 3 151 -160 140
		mu 0 3 66 73 64
		f 4 160 161 162 163
		mu 0 4 105 76 77 98
		f 4 -161 164 165 166
		mu 0 4 76 105 104 80
		f 4 -166 167 168 169
		mu 0 4 80 104 101 82
		f 4 170 171 172 173
		mu 0 4 103 84 85 102
		f 4 -171 174 175 176
		mu 0 4 84 103 96 88
		f 4 -173 177 178 179
		mu 0 4 102 85 89 100
		f 4 -169 180 181 182
		mu 0 4 82 101 99 92
		f 4 -182 183 -179 184
		mu 0 4 92 99 100 89
		f 4 -163 185 186 187
		mu 0 4 98 77 93 97
		f 4 -187 188 -176 189
		mu 0 4 97 93 88 96
		f 3 190 191 -165
		mu 0 3 75 95 79
		f 3 192 -174 193
		mu 0 3 95 83 86
		f 3 194 195 -181
		mu 0 3 81 95 91
		f 3 196 -184 -196
		mu 0 3 95 90 91
		f 3 197 -188 198
		mu 0 3 95 78 94
		f 3 199 -199 -190
		mu 0 3 87 95 94
		f 3 -192 -195 -168
		mu 0 3 79 95 81
		f 3 -194 -180 -197
		mu 0 3 95 86 90
		f 3 -193 -200 -175
		mu 0 3 83 95 87
		f 3 -191 -164 -198
		mu 0 3 95 75 78
		f 4 200 -143 201 -167
		mu 0 4 80 65 64 76
		f 4 202 144 203 -172
		mu 0 4 84 68 67 85
		f 4 204 -149 205 -183
		mu 0 4 92 70 69 82
		f 4 206 -151 -205 -185
		mu 0 4 89 71 70 92
		f 4 207 152 208 -186
		mu 0 4 77 73 72 93
		f 4 -209 155 209 -189
		mu 0 4 93 72 74 88
		f 4 -206 -157 -201 -170
		mu 0 4 82 69 65 80
		f 4 -204 157 -207 -178
		mu 0 4 85 67 71 89
		f 4 -210 -159 -203 -177
		mu 0 4 88 74 68 84
		f 4 -202 159 -208 -162
		mu 0 4 76 64 73 77;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".vcs" 2;
createNode transform -s -n "persp";
	rename -uid "1D965218-44CE-006C-61BD-FDA2B7042A23";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 46.696100231144719 181.82162799571648 66.830845041874412 ;
	setAttr ".r" -type "double3" -27.938352729602347 22.600000000000005 8.6127585638339117e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "2B8A6CB3-4E54-425B-02C5-A1AF22B23B4E";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 161.59667814055203;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "E8045911-404A-843E-7560-E5BD0A5DD352";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "969516DE-4BEB-3C75-89B6-629D25A87CD2";
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
	rename -uid "383A31C1-45F9-3B4B-1D5A-4E9504A17AD4";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "D6BFA45C-412E-34FE-F4FE-13AC86C80694";
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
	rename -uid "3D6B4126-4792-8EC6-C71E-E3AAA2CDA04E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "27AD070D-42D0-6BDA-2E42-D68E76DD369C";
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
createNode transform -n "popup_grp";
	rename -uid "BE9649C2-4E4C-B55D-45A5-058169C0AC70";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 1 0 ;
createNode transform -n "popupLocation_grp" -p "popup_grp";
	rename -uid "3F94870A-446B-4E7B-3DBA-E0861F50FB51";
	setAttr ".t" -type "double3" -9.5367431640625e-07 133.40493774414062 0 ;
createNode transform -n "popupA_loc" -p "popupLocation_grp";
	rename -uid "69861019-4DD4-C964-662F-2597B89565EB";
	setAttr ".t" -type "double3" 30 12 8 ;
createNode locator -n "popupA_locShape" -p "popupA_loc";
	rename -uid "981AFE6F-4DFC-35FC-36A9-39B30D047D33";
	setAttr -k off ".v";
createNode transform -n "popupB_loc" -p "popupLocation_grp";
	rename -uid "D463A857-4BC8-007B-DE87-ECB5396780A3";
	setAttr ".t" -type "double3" -10 0 18 ;
createNode locator -n "popupB_locShape" -p "popupB_loc";
	rename -uid "DA0AE478-4ADD-D532-2B74-1496B4AD1488";
	setAttr -k off ".v";
createNode transform -n "popupC_loc" -p "popupLocation_grp";
	rename -uid "8E065E49-4278-C6DC-55FF-D4BFFDDF818B";
	setAttr ".t" -type "double3" -9.6514766375573124 -18 15.314481726101235 ;
createNode locator -n "popupC_locShape" -p "popupC_loc";
	rename -uid "E7DAD332-4D9D-D6EF-9F8E-5993AC496B5F";
	setAttr -k off ".v";
createNode transform -n "popupD_loc" -p "popupLocation_grp";
	rename -uid "B1779275-4A9F-DFAE-DAAE-3683DBD08FF9";
	setAttr ".t" -type "double3" 10.430294765331771 -11.114391092215911 14.106335098820983 ;
createNode locator -n "popupD_locShape" -p "popupD_loc";
	rename -uid "85B4BA55-4661-2783-79CD-9DB75AA4FCF0";
	setAttr -k off ".v";
createNode transform -n "popupE_loc" -p "popupLocation_grp";
	rename -uid "2926B70E-414C-E1CC-B53E-9C95F1AC2654";
	setAttr ".t" -type "double3" -10.028916770710742 -9 14.977582462302749 ;
createNode locator -n "popupE_locShape" -p "popupE_loc";
	rename -uid "423B096B-4FC1-2718-8DB1-939B01540D60";
	setAttr -k off ".v";
createNode condition -n "popupSweating_cnd";
	rename -uid "288A9F28-457F-3351-40C8-CAA8A8E6CB31";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupSigh_cnd";
	rename -uid "0D71CF99-4786-9866-A946-A8BFE5301FF2";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupStunned_cnd";
	rename -uid "22190162-4A27-5658-968B-7EB1D267D2DB";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupShock_cnd";
	rename -uid "766B1BDF-4DA7-CF46-4B39-BF89F47E5FE0";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupConfused_cnd";
	rename -uid "3C7721D4-4CEE-446E-2756-E090F897E5B4";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupUncomfortable_cnd";
	rename -uid "46953C80-482B-DBE2-D7F1-378397FE1C96";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupJoy_cnd";
	rename -uid "06516CC0-45C3-63E0-BBFF-398894E801BD";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupLove_cnd";
	rename -uid "BF78BC01-4DDD-043B-BF2B-4A816B565224";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupAngry_cnd";
	rename -uid "6A9844DC-4860-0B48-A762-93898A16D3EA";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupShyL_cnd";
	rename -uid "B19467E6-4317-7C27-E976-28A16E897E2C";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode condition -n "popupShyR_cnd";
	rename -uid "980D5966-4085-CC61-F20D-70951F12CB94";
	setAttr ".st" 1;
	setAttr ".cf" -type "float3" 0 0 0 ;
createNode skinCluster -n "Sweating_skc";
	rename -uid "93D296D9-460B-E3DE-58F9-6AB50EC11471";
	setAttr -s 50 ".wl";
	setAttr ".wl[0:49].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoG01_bind";
	rename -uid "AE1D4F16-4B3D-8DEC-D138-088E884ECC86";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode materialInfo -n "materialInfo71";
	rename -uid "A40B9DCA-453D-8A80-3ECD-B38E1F8B008F";
createNode shadingEngine -n "SH_C001_Ashford_01_Head";
	rename -uid "0B1F89FB-4B38-14D0-DCC3-08A970B79793";
	setAttr ".ihi" 0;
	setAttr -s 11 ".dsm";
	setAttr ".ro" yes;
createNode lambert -n "M_C001_Ashford_01_Head";
	rename -uid "160DF3DE-483B-D6FA-3AB0-BB9CDA172748";
	setAttr ".ambc" -type "float3" 1 1 1 ;
createNode file -n "file2";
	rename -uid "BFCE1E31-4DF7-C238-0F3E-97A96CD9E68D";
	setAttr ".ftn" -type "string" "D:/svn_true/P_Regulus/Content/Characters/CH023_Jeff/01/Texture/CH023_Jeff_01_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "F44780FD-4E23-43E1-2DEE-2BB46B650A5F";
createNode skinCluster -n "Sigh_skc";
	rename -uid "5E15F9A7-4618-A1BE-D0E5-A8BC25DB605F";
	setAttr -s 56 ".wl";
	setAttr ".wl[0:55].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoH01_bind";
	rename -uid "03F162CF-4586-934E-387A-0AB6F137BB36";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "Stunned_skc";
	rename -uid "D18A1302-41CB-C076-03C1-AA9BBA0DB26A";
	setAttr -s 112 ".wl";
	setAttr ".wl[0:111].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoI01_bind";
	rename -uid "96D80C9C-4286-11F3-ABDA-72BD7AB7E1B0";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "Shock_skc";
	rename -uid "9491FADA-443B-E089-8AD6-958ED7398F7B";
	setAttr ".bw[5]"  nan;
	setAttr -s 60 ".wl";
	setAttr ".wl[0:59].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoJ01_bind";
	rename -uid "58A06AC3-4FB0-CFB0-F73D-7189D552AF6F";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "Confused_skc";
	rename -uid "21BFEB83-43C3-AA27-6818-9EAA027022D9";
	setAttr -s 69 ".wl";
	setAttr ".wl[0:68].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoK01_bind";
	rename -uid "A662CA01-4833-BBB3-7DB4-6C9831A93594";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "Uncomfortable_skc";
	rename -uid "8AADB7CF-47DA-F1F0-C412-15BC8E9D0041";
	setAttr ".bw[16]"  3.3604601320000001e-06;
	setAttr -s 117 ".wl";
	setAttr ".wl[0:116].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoA01_bind";
	rename -uid "90FBF5A1-4B8F-883A-F789-398D178E2109";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "Joy_skc";
	rename -uid "0FEF3D6E-4A0C-2F5B-A4CD-0B83DB804D6B";
	setAttr -s 39 ".bw";
	setAttr ".bw[267]" 1;
	setAttr ".bw[268]" 1;
	setAttr ".bw[270]" 1;
	setAttr ".bw[271]" 1;
	setAttr ".bw[273]" 1;
	setAttr ".bw[274]" 1;
	setAttr ".bw[276]" 1;
	setAttr ".bw[277]" 1;
	setAttr ".bw[278]" 1;
	setAttr ".bw[279]" 1;
	setAttr ".bw[280]" 1;
	setAttr ".bw[282]" 1;
	setAttr ".bw[283]" 1;
	setAttr ".bw[285]" 1;
	setAttr ".bw[286]" 1;
	setAttr ".bw[288]" 1;
	setAttr ".bw[289]" 1;
	setAttr ".bw[291]" 1;
	setAttr ".bw[292]" 1;
	setAttr ".bw[294]" 1;
	setAttr ".bw[295]" 1;
	setAttr ".bw[297]" 1;
	setAttr ".bw[298]" 1;
	setAttr ".bw[300]" 1;
	setAttr ".bw[301]" 1;
	setAttr ".bw[303]" 1;
	setAttr ".bw[304]" 1;
	setAttr ".bw[306]" 1;
	setAttr ".bw[307]" 1;
	setAttr ".bw[309]" 1;
	setAttr ".bw[310]" 1;
	setAttr ".bw[312]" 1;
	setAttr ".bw[313]" 1;
	setAttr ".bw[315]" 1;
	setAttr ".bw[316]" 1;
	setAttr ".bw[318]" 1;
	setAttr ".bw[319]" 1;
	setAttr ".bw[321]" 1;
	setAttr ".bw[322]" 1;
	setAttr -s 381 ".wl";
	setAttr ".wl[0:380].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoB01_bind";
	rename -uid "F9A84F67-4473-0393-BE94-5981D3EB23B9";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "Love_skc";
	rename -uid "AD6F9E6F-4B12-74DF-BD68-CCBBD9F26368";
	setAttr -s 124 ".wl";
	setAttr ".wl[0:123].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoC01_bind";
	rename -uid "E262F03F-43C1-87DC-C202-9A958FAE1205";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "Angry_skc";
	rename -uid "37C6DC6F-4299-AF9F-0FB4-269CAB0A93A0";
	setAttr -s 8 ".bw";
	setAttr ".bw[24]" 1;
	setAttr ".bw[25]" 1;
	setAttr ".bw[26]" 1;
	setAttr ".bw[27]" 1;
	setAttr ".bw[184]" 0.0027685672935733275;
	setAttr ".bw[186]" 0.0017058497740572792;
	setAttr ".bw[188]" 0.0018103562741779303;
	setAttr ".bw[190]" 0.0018099753629416326;
	setAttr -s 192 ".wl";
	setAttr ".wl[0:191].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoD01_bind";
	rename -uid "0073609B-4EB8-288F-3A3B-F68B6AF0BCBE";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "ShyL_skc";
	rename -uid "9D45EB1A-490D-5F0C-F017-95B96AD4EDE5";
	setAttr -s 96 ".wl";
	setAttr ".wl[0:95].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoE01_bind";
	rename -uid "9421931E-4446-E96C-5AB5-669178A5A5CE";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode skinCluster -n "ShyR_skc";
	rename -uid "32DE05B5-468A-5342-0FC0-D7AFE5124FD2";
	setAttr -s 96 ".wl";
	setAttr ".wl[0:95].w"
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1;
	setAttr -k off ".wl[0].w";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 9.5367431640625e-07 -133.40493774414062 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".dpf[0]"  4;
	setAttr ".mmi" yes;
	setAttr ".mi" 4;
	setAttr ".ucm" yes;
createNode dagPose -n "emoF01_bind";
	rename -uid "35D60F05-414B-5FFD-60C9-E09A83EC2C86";
	setAttr -s 2 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -9.5367431640625e-07 133.40493774414062 0 1;
	setAttr -s 2 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 128 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -9.5367431640625e-07 5.404937744140625
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 2 ".m";
	setAttr -s 2 ".p";
	setAttr -s 2 ".g[0:1]" yes no;
	setAttr ".bp" yes;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "97BFA42E-4B78-2D06-373F-A389ADEE6E47";
	setAttr -s 3 ".lnk";
	setAttr -s 3 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "E5D9FCB9-4B3D-AAEB-D711-3BA13F9298BE";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "E93ACA4D-4303-995A-95E9-4E846CF1C032";
createNode displayLayerManager -n "layerManager";
	rename -uid "4C3597D6-48A4-2FBC-01E2-91B50AFE0F5B";
createNode displayLayer -n "defaultLayer";
	rename -uid "6D61F15A-4F49-824D-4E2D-B5A7D9B1E79E";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "068C3F2E-4C15-3F3E-7230-13B2C71CBB4A";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "024EDB86-42D4-DDCE-0768-25A42FB9A91F";
	setAttr ".g" yes;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "26CA0291-48FA-6F06-2B8A-2A973639D23A";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 235 -ast 0 -aet 391 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "A591BE91-4A23-59D5-3E69-28AC844E5E09";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1133.3332882987147 -553.57140657447724 ;
	setAttr ".tgi[0].vh" -type "double2" 1133.3332882987147 553.57140657447724 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -247.14285278320312;
	setAttr ".tgi[0].ni[0].y" 162.85714721679688;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 60;
	setAttr ".tgi[0].ni[1].y" -97.142860412597656;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 60;
	setAttr ".tgi[0].ni[2].y" 162.85714721679688;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 60;
	setAttr ".tgi[0].ni[3].y" 32.857143402099609;
	setAttr ".tgi[0].ni[3].nvs" 18304;
createNode polyTweakUV -n "polyTweakUV1";
	rename -uid "DD7FBFB4-4742-589E-6183-03901019869D";
	setAttr ".uopa" yes;
	setAttr -s 70 ".uvtk[0:69]" -type "float2" 0 0.49295062 0 0.49122226
		 0 0.49159858 0 0.47639337 0 0.47036687 0 0.47643396 0 0.48240182 0 0.4792715 0 0.47935638
		 0 0.48258221 0 0.48553437 0 0.48584247 0 0.48888689 0 0.48859659 0 0.49141443 0 0.4930492
		 0 0.49425852 0 0.45688277 0 0.48602086 0 0.48231134 0 0.45335782 0 0.46016562 0 0.48949632
		 0 0.47881094 0 0.44980747 0 0.46300733 0 0.49250171 0 0.46468502 0 0.49444833 0 0.44141716
		 0 0.46961159 0 0.47567913 0 0.44629467 0 0.44634956 0 0.47573575 0 0.47864929 0 0.44949877
		 0 0.46526837 0 0.49613217 0 0.46461588 0 0.49417961 0 0.4628998 0 0.49215567 0 0.46002626
		 0 0.48904064 0 0.4567067 0 0.4855648 0 0.45322233 0 0.48205313 0 0.46331131 0 0.48192394
		 0 0.47823772 0 0.48557612 0 0.47526839 0 0.47860971 0 0.48921719 0 0.49247959 0 0.4946416
		 0 0.49658531 0 0.49495807 0 0.47522292 0 0.47074047 0 0.49288994 0 0.48974103 0 0.48222259
		 0 0.48608834 0 0.49610806 0 0.46961647 0 0.49652898 0 0.47073635;
createNode polyTweakUV -n "polyTweakUV2";
	rename -uid "F4C9CCB4-4C6F-6F6A-2AE2-7DA6DD2997E3";
	setAttr ".uopa" yes;
	setAttr -s 78 ".uvtk[0:77]" -type "float2" 0 0.48819903 0 0.49174589
		 0 0.49143523 0 0.48706362 0 0.48176685 0 0.48184034 0 0.47923818 0 0.48696822 0 0.4804326
		 0 0.48279995 0 0.48505607 0 0.48495984 0 0.47818437 0 0.47614715 0 0.47459003 0 0.47390667
		 0 0.47384813 0 0.47488829 0 0.47688368 0 0.44379574 0 0.49316961 0 0.48882324 0 0.44795936
		 0 0.4402653 0 0.49148235 0 0.44611889 0 0.48731342 0 0.48756659 0 0.45051938 0 0.44490558
		 0 0.48496071 0 0.4638201 0 0.47335109 0 0.47250435 0 0.46213716 0 0.46432239 0 0.47518495
		 0 0.4724727 0 0.45942271 0 0.44558263 0 0.4816778 0 0.47366652 0 0.45508605 0 0.44746888
		 0 0.4787297 0 0.45067781 0 0.47598961 0 0.48560658 0 0.45414668 0 0.46340007 0 0.47761431
		 0 0.45805854 0 0.48306713 0 0.48029557 0 0.46127135 0 0.45443904 0 0.47732505 0 0.48023108
		 0 0.48321161 0 0.48588562 0 0.47471306 0 0.48781106 0 0.47553179 0 0.47304788 0 0.47845975
		 0 0.48159382 0 0.47177365 0 0.48490092 0 0.47181436 0 0.4726989 0 0.48725587 0 0.48899564
		 0 0.49363297 0 0.49207115 0 0.49230644 0 0.49285811 0 0.49092472 0 0.49387652;
createNode polyTweakUV -n "polyTweakUV3";
	rename -uid "C6D9F64A-422E-3F45-3304-8AA0977F12CA";
	setAttr ".uopa" yes;
	setAttr -s 182 ".uvtk[0:181]" -type "float2" 0 0.49045801 0 0.4916313
		 0 0.49473166 0 0.49416512 0 0.49337769 0 0.49567696 0 0.48296437 0 0.47579589 0 0.47727683
		 0 0.47171095 0 0.47150758 0 0.48556983 0 0.49249974 0 0.48339197 0 0.47300217 0 0.47167614
		 0 0.47678617 0 0.47784194 0 0.4944379 0 0.49395776 0 0.49344862 0 0.48173141 0 0.48495901
		 0 0.48471779 0 0.48182654 0 0.48487568 0 0.48180273 0 0.48189437 0 0.48503184 0 0.48427337
		 0 0.48215836 0 0.48472035 0 0.48495972 0 0.48188758 0 0.48227102 0 0.48282367 0 0.44724476
		 0 0.44666058 0 0.45173562 0 0.48221245 0 0.48493671 0 0.48393935 0 0.48231801 0 0.48195153
		 0 0.48449218 0 0.45236105 0 0.45800442 0 0.48270842 0 0.48460507 0 0.45846492 0 0.45314616
		 0 0.45861423 0 0.4592126 0 0.48338154 0 0.45970869 0 0.46002698 0 0.46011865 0 0.45996964
		 0 0.45960319 0 0.45907491 0 0.48338169 0 0.45252073 0 0.48338175 0 0.44666505 0 0.44603759
		 0 0.44545722 0 0.44501305 0 0.44477206 0 0.44477111 0 0.44501036 0 0.44545346 0 0.44603306
		 0 0.46449524 0 0.49287206 0 0.4940238 0 0.46541071 0 0.45604742 0 0.48556513 0 0.4470427
		 0 0.47748682 0 0.46371353 0 0.49527779 0 0.49570099 0 0.46454406 0 0.46547389 0 0.49537501
		 0 0.46559143 0 0.49481142 0 0.44046533 0 0.47075245 0 0.47056857 0 0.44014376 0 0.44233638
		 0 0.47219905 0 0.47083548 0 0.44022667 0 0.44586432 0 0.47615746 0 0.46059072 0 0.49027056
		 0 0.48331246 0 0.45357764 0 0.46174467 0 0.49141926 0 0.47699246 0 0.4471817 0 0.47525248
		 0 0.44562137 0 0.49649489 0 0.49462938 0 0.46368235 0 0.49314725 0 0.4930234 0 0.46559072
		 0 0.49135566 0 0.49617505 0 0.47581866 0 0.47043601 0 0.47181401 0 0.47497955 0 0.47688106
		 0 0.48325658 0 0.49031132 0 0.4773486 0 0.47013256 0 0.47028968 0 0.49521893 0 0.49429965
		 0 0.49583754 0 0.4957549 0 0.485562 0 0.49300575 0 0.49546695 0 0.49663076 0 0.44792724
		 0 0.4479264 0 0.44768536 0 0.44724089 0 0.48369324 0 0.48306555 0 0.48248607 0 0.48204279
		 0 0.48180348 0 0.48180437 0 0.48204535 0 0.48248982 0 0.48307002 0 0.48369753 0 0.48427713
		 0 0.44768804 0 0.45088565 0 0.45079064 0 0.45094669 0 0.4513303 0 0.45188326 0 0.48346132
		 0 0.48408699 0 0.45366418 0 0.45399624 0 0.45409125 0 0.45393503 0 0.45355141 0 0.45299882
		 0 0.48330176 0 0.48267639 0 0.45121759 0 0.48284644 0 0.4574759 0 0.45710951 0 0.45696068
		 0 0.45705235 0 0.4573704 0 0.45786637 0 0.48330709 0 0.483917 0 0.48444542 0 0.48481187
		 0 0.48496068 0 0.48486885 0 0.48455077 0 0.48405483 0 0.48345637;
createNode polyTweakUV -n "polyTweakUV4";
	rename -uid "A9E3C493-4BA5-5A83-C153-7CBE92735DCA";
	setAttr ".uopa" yes;
	setAttr -s 112 ".uvtk[0:111]" -type "float2" 0 0.48686159 0 0.48344132
		 0 0.47943351 0 0.48440245 0 0.47554687 0 0.47569075 0 0.49160835 0 0.49246934 0 0.47325733
		 0 0.47360048 0 0.48308772 0 0.48685884 0 0.48358905 0 0.48040545 0 0.47555897 0 0.47554693
		 0 0.49175423 0 0.49281633 0 0.47279999 0 0.47370777 0 0.45507967 0 0.48857477 0 0.48611447
		 0 0.48196113 0 0.45072311 0 0.48200577 0 0.4781484 0 0.47814259 0 0.46395129 0 0.49257362
		 0 0.49365163 0 0.4631083 0 0.44189447 0 0.47176525 0 0.47422102 0 0.47173283 0 0.44440824
		 0 0.47332904 0 0.44444019 0 0.4734281 0 0.45508647 0 0.48458332 0 0.4788996 0 0.47801337
		 0 0.45072508 0 0.4885672 0 0.48172238 0 0.48674229 0 0.46437621 0 0.49299663 0 0.49379504
		 0 0.46321017 0 0.44146919 0 0.47130004 0 0.47429356 0 0.47164521 0 0.4444375 0 0.47322187
		 0 0.44368505 0 0.47331735 0 0.47234079 0 0.44153911 0 0.47219798 0 0.47503665 0 0.49225098
		 0 0.49568433 0 0.4885191 0 0.45053363 0 0.45531189 0 0.48037601 0 0.47246012 0 0.44230741
		 0 0.47230676 0 0.47514859 0 0.49213213 0 0.49535841 0 0.48644316 0 0.45048285 0 0.4553625
		 0 0.48891625 0 0.48835436 0 0.4852975 0 0.47853851 0 0.48158187 0 0.48515466 0 0.47799802
		 0 0.48311734 0 0.4885737 0 0.48029655 0 0.48890302 0 0.47866434 0 0.485787 0 0.47841397
		 0 0.48076612 0 0.48736486 0 0.48891827 0 0.49225205 0 0.4945446 0 0.49470216 0 0.49180537
		 0 0.47184595 0 0.473331 0 0.47658685 0 0.47155783 0 0.47191015 0 0.47295406 0 0.47647324
		 0 0.47123191 0 0.49237409 0 0.49491289 0 0.49486771 0 0.49222857;
createNode polyTweakUV -n "polyTweakUV5";
	rename -uid "92029E27-4CED-D426-161B-36B6E20828EC";
	setAttr ".uopa" yes;
	setAttr -s 114 ".uvtk[0:113]" -type "float2" 0 0.48669603 0 0.48582581
		 0 0.48293141 0 0.48715374 0 0.48395684 0 0.48369309 0 0.48461917 0 0.48016188 0 0.48009756
		 0 0.48449984 0 0.48187378 0 0.48204622 0 0.48079398 0 0.48537168 0 0.48264042 0 0.48709676
		 0 0.48693633 0 0.47959545 0 0.4814637 0 0.48760429 0 0.48363274 0 0.47898066 0 0.48428258
		 0 0.46312636 0 0.48852709 0 0.48400119 0 0.45778644 0 0.46225941 0 0.48814985 0 0.48260537
		 0 0.45743805 0 0.45874476 0 0.48685223 0 0.45372248 0 0.48613974 0 0.48142865 0 0.45559078
		 0 0.44952589 0 0.48629311 0 0.4790093 0 0.4470644 0 0.47878847 0 0.44667107 0 0.44667017
		 0 0.48028728 0 0.47941467 0 0.44713664 0 0.45777273 0 0.48721898 0 0.47844461 0 0.47864684
		 0 0.45696211 0 0.48807403 0 0.45138556 0 0.48069403 0 0.48115107 0 0.45966476 0 0.4803839
		 0 0.48233095 0 0.48745835 0 0.46343619 0 0.45853227 0 0.48945525 0 0.48613119 0 0.48202726
		 0 0.45297372 0 0.48181632 0 0.47769567 0 0.47699898 0 0.48548371 0 0.47716415 0 0.48299724
		 0 0.48945305 0 0.48153028 0 0.47856805 0 0.48847678 0 0.47852585 0 0.48285279 0 0.48737869
		 0 0.48695177 0 0.48668095 0 0.48062018 0 0.47787738 0 0.45297372 0 0.48720586 0 0.45862412
		 0 0.48978633 0 0.48979014 0 0.48851272 0 0.48897514 0 0.48719716 0 0.4800981 0 0.46249586
		 0 0.48060128 0 0.48020783 0 0.47828248 0 0.44756025 0 0.48782632 0 0.47886768 0 0.48674962
		 0 0.47969785 0 0.47829053 0 0.47812125 0 0.47864613 0 0.48098031 0 0.48668203 0 0.48214087
		 0 0.48759547 0 0.48731169 0 0.48871017 0 0.48222265 0 0.48426023 0 0.48700127 0 0.48897979;
createNode polyTweakUV -n "polyTweakUV6";
	rename -uid "63A1246B-482E-0249-D62B-C7B0F791BD0F";
	setAttr ".uopa" yes;
	setAttr -s 162 ".uvtk[0:161]" -type "float2" 0 0.47615594 0 0.47465831
		 0 0.47456241 0 0.47597951 0 0.48823044 0 0.49301028 0 0.48915228 0 0.48449314 0 0.48538181
		 0 0.48142123 0 0.48176605 0 0.47893754 0 0.47857502 0 0.48562485 0 0.48306525 0 0.48105365
		 0 0.47932279 0 0.48044011 0 0.48367 0 0.48627207 0 0.47816622 0 0.48777488 0 0.47773781
		 0 0.48823199 0 0.48750606 0 0.47835037 0 0.48025578 0 0.4825007 0 0.4843601 0 0.48585641
		 0 0.48568466 0 0.48379764 0 0.48106372 0 0.48703158 0 0.47958264 0 0.48740333 0 0.47877046
		 0 0.47900069 0 0.48670197 0 0.45642626 0 0.4813211 0 0.48563984 0 0.45915151 0 0.45389724
		 0 0.47786582 0 0.48986447 0 0.46156585 0 0.45037603 0 0.47445208 0 0.44723457 0 0.47252008
		 0 0.46264237 0 0.49403208 0 0.4894928 0 0.45752114 0 0.48530203 0 0.45232671 0 0.44498444
		 0 0.47252753 0 0.44443917 0 0.47461578 0 0.44590187 0 0.4779076 0 0.44849777 0 0.48147017
		 0 0.4553262 0 0.49037099 0 0.49003828 0 0.4582355 0 0.45236844 0 0.48930195 0 0.48843619
		 0 0.46064025 0 0.44912541 0 0.48681837 0 0.44632638 0 0.4832269 0 0.46179664 0 0.48602292
		 0 0.47832042 0 0.45714957 0 0.47603756 0 0.45203656 0 0.44528472 0 0.48035529 0 0.44545794
		 0 0.47789109 0 0.44640553 0 0.4764764 0 0.44866747 0 0.47558886 0 0.45041096 0 0.47668406
		 0 0.47737843 0 0.45245433 0 0.44929874 0 0.4772523 0 0.47906843 0 0.45498675 0 0.44969678
		 0 0.47894263 0 0.45126027 0 0.48213392 0 0.45778286 0 0.48161429 0 0.48792443 0 0.45754671
		 0 0.48915955 0 0.45778149 0 0.45296955 0 0.48485106 0 0.45470047 0 0.4870294 0 0.45588875
		 0 0.48831901 0 0.45723969 0 0.48930541 0 0.48619664 0 0.48142791 0 0.49429899 0 0.49017519
		 0 0.49006784 0 0.48897943 0 0.48752594 0 0.48884493 0 0.48752257 0 0.48014924 0 0.47823644
		 0 0.47842735 0 0.47643727 0 0.47650599 0 0.47581297 0 0.47471726 0 0.47510904 0 0.47567222
		 0 0.47730473 0 0.48009413 0 0.4833321 0 0.47743565 0 0.47998998 0 0.48746178 0 0.48934147
		 0 0.4872914 0 0.49010652 0 0.49094927 0 0.49127054 0 0.48150072 0 0.48563147 0 0.47762108
		 0 0.47398129 0 0.47168905 0 0.47168946 0 0.48999709 0 0.49397784 0 0.49342388 0 0.49015445
		 0 0.47375751 0 0.47739556 0 0.48577088 0 0.48117355 0 0.48194495 0 0.48507169;
createNode polyTweakUV -n "polyTweakUV7";
	rename -uid "882A2955-4EA2-4507-079D-B3BCEC342D86";
	setAttr ".uopa" yes;
	setAttr -s 516 ".uvtk";
	setAttr ".uvtk[0:249]" -type "float2" 0 0.48158836 0 0.48271745 0 0.48567531
		 0 0.48799184 0 0.48687187 0 0.48533314 0 0.49236831 0 0.49304998 0 0.49046302 0 0.47563532
		 0 0.4748266 0 0.47805813 0 0.47717318 0 0.47579643 0 0.47805837 0 0.48538956 0 0.48372248
		 0 0.48225027 0 0.47485331 0 0.47450212 0 0.47476354 0 0.47974905 0 0.48964819 0 0.48994309
		 0 0.49298108 0 0.49207407 0 0.49058634 0 0.48906073 0 0.48871619 0 0.48098928 0 0.47902551
		 0 0.47756198 0 0.47486606 0 0.47600535 0 0.4745197 0 0.48765936 0 0.48894534 0 0.48614156
		 0 0.48439106 0 0.4910872 0 0.48297426 0 0.48138437 0 0.48024884 0 0.48360428 0 0.48633131
		 0 0.48696449 0 0.4867042 0 0.48145017 0 0.48081043 0 0.48641559 0 0.48588964 0 0.48498374
		 0 0.4822413 0 0.48276046 0 0.48423347 0 0.47956142 0 0.47964814 0 0.48104236 0 0.48030183
		 0 0.48001674 0 0.48002318 0 0.47998282 0 0.48064461 0 0.48126605 0 0.48613998 0 0.48716787
		 0 0.48657519 0 0.48510781 0 0.48430339 0 0.48352623 0 0.4828876 0 0.48221776 0 0.47977456
		 0 0.48561096 0 0.48417598 0 0.48499459 0 0.48341689 0 0.48810139 0 0.48777232 0 0.4880133
		 0 0.48762718 0 0.48662376 0 0.48581904 0 0.48614174 0 0.48309249 0 0.47983372 0 0.47936881
		 0 0.48026443 0 0.48628855 0 0.48672852 0 0.48187441 0 0.48255593 0 0.48303723 0 0.48300111
		 0 0.48227638 0 0.48135275 0 0.48614699 0 0.48579073 0 0.48473591 0 0.48696256 0 0.48692226
		 0 0.48661563 0 0.48524833 0 0.48445937 0 0.48384207 0 0.4796772 0 0.48057759 0 0.48124504
		 0 0.48337922 0 0.48406744 0 0.48460537 0 0.48498297 0 0.48562843 0 0.48627356 0 0.47980541
		 0 0.48080504 0 0.48015696 0 0.48153096 0 0.47914827 0 0.47978359 0 0.47892767 0 0.47898507
		 0 0.48141354 0 0.45486486 0 0.45313871 0 0.48276937 0 0.46144307 0 0.45821339 0 0.48740891
		 0 0.45717537 0 0.4579612 0 0.48591396 0 0.45762837 0 0.45712739 0 0.45634627 0 0.45532769
		 0 0.45272177 0 0.45006502 0 0.44920182 0 0.47810975 0 0.45126069 0 0.44971591 0 0.45530212
		 0 0.45610005 0 0.44986725 0 0.45136905 0 0.47958457 0 0.45014864 0 0.45250398 0 0.45402956
		 0 0.45659602 0 0.45527905 0 0.45263445 0 0.45083141 0 0.45353937 0 0.4826206 0 0.45420426
		 0 0.44719595 0 0.44930089 0 0.45969677 0 0.49181223 0 0.49090523 0 0.46079397 0 0.46153367
		 0 0.49239412 0 0.48997688 0 0.46128529 0 0.45385164 0 0.4809427 0 0.47937736 0 0.45249045
		 0 0.45489639 0 0.48246497 0 0.45647264 0 0.48442551 0 0.48840901 0 0.46050364 0 0.48652458
		 0 0.45864165 0 0.4575547 0 0.49079722 0 0.49178356 0 0.45965409 0 0.45746565 0 0.48986697
		 0 0.45684683 0 0.48884761 0 0.45048296 0 0.48051691 0 0.48188728 0 0.45063347 0 0.44805628
		 0 0.47851011 0 0.48356047 0 0.45145839 0 0.45531845 0 0.48744899 0 0.45325971 0 0.48558012
		 0 0.4631322 0 0.49366611 0 0.49324793 0 0.4617312 0 0.46391296 0 0.49446622 0 0.46345323
		 0 0.49430627 0 0.47699443 0 0.45039308 0 0.44812256 0 0.47344789 0 0.47336331 0 0.44549817
		 0 0.44641006 0 0.47340021 0 0.44580805 0 0.47319195 0 0.47513184 0 0.44831085 0 0.47367635
		 0 0.44643253 0 0.4459362 0 0.47643527 0 0.47319826 0 0.44435525 0 0.4444465 0 0.47478315
		 0 0.44377089 0 0.47362998 0 0.4557597 0 0.48837975 0 0.4885737 0 0.45646048 0 0.45696223
		 0 0.48790196 0 0.48901924 0 0.45668453 0 0.45323098 0 0.48789379 0 0.48718959 0 0.45240104
		 0 0.45388871 0 0.4882485 0 0.45458746 0 0.48883182 0 0.48933622 0 0.45633769 0 0.4892669
		 0 0.45553213 0 0.45485628;
	setAttr ".uvtk[250:499]" 0 0.48249474 0 0.48331282 0 0.45608741 0 0.45480388
		 0 0.48173293 0 0.45452708 0 0.48079547 0 0.45173025 0 0.47827151 0 0.4785696 0 0.45181966
		 0 0.45033383 0 0.47828838 0 0.47882804 0 0.45218456 0 0.45387143 0 0.47996786 0 0.45297396
		 0 0.47927836 0 0.45764667 0 0.48729897 0 0.48430946 0 0.45703846 0 0.45798379 0 0.48652706
		 0 0.45778149 0 0.48538288 0 0.4863233 0 0.45144975 0 0.45073152 0 0.48123404 0 0.48048398
		 0 0.44918412 0 0.44971383 0 0.48227772 0 0.44944602 0 0.48325637 0 0.485441 0 0.45054352
		 0 0.48430258 0 0.44971782 0 0.44938624 0 0.47827819 0 0.47981623 0 0.44869685 0 0.44873464
		 0 0.47846845 0 0.44843787 0 0.47896686 0 0.45663345 0 0.48009533 0 0.47964752 0 0.4572835
		 0 0.45774817 0 0.48067904 0 0.47887504 0 0.45749235 0 0.45427078 0 0.477945 0 0.47836107
		 0 0.45350099 0 0.45488083 0 0.47791716 0 0.45553356 0 0.4777588 0 0.47812456 0 0.45716858
		 0 0.47776905 0 0.45641601 0 0.45578891 0 0.48607728 0 0.48538443 0 0.45693189 0 0.45574027
		 0 0.48661521 0 0.45548171 0 0.48728889 0 0.45286936 0 0.48799059 0 0.48800918 0 0.45295262
		 0 0.4515723 0 0.48756593 0 0.4881331 0 0.4532932 0 0.45486885 0 0.48781905 0 0.45403033
		 0 0.4881188 0 0.45838779 0 0.48149127 0 0.4845643 0 0.45781952 0 0.45870292 0 0.48244143
		 0 0.4585138 0 0.48361039 0 0.47878164 0 0.45261282 0 0.45193613 0 0.48315465 0 0.4840492
		 0 0.45049888 0 0.45099103 0 0.48215079 0 0.45074111 0 0.48117185 0 0.47932822 0 0.45176613
		 0 0.48021126 0 0.45099497 0 0.45068783 0 0.4871558 0 0.48480022 0 0.4500438 0 0.4500789
		 0 0.48661488 0 0.4498018 0 0.4858394 0 0.45524734 0 0.45338929 0 0.45696938 0 0.45096445
		 0 0.44992316 0 0.45323414 0 0.45614982 0 0.4544186 0 0.45775378 0 0.45215952 0 0.45118952
		 0 0.454274 0 0.48366636 0 0.48465285 0 0.47732034 0 0.47739622 0 0.48099935 0 0.47999698
		 0 0.48607534 0 0.48498893 0 0.48854944 0 0.48855421 0 0.48687786 0 0.48750019 0 0.4842695
		 0 0.48790523 0 0.47903383 0 0.47846419 0 0.48198599 0 0.48318827 0 0.47804421 0 0.48242164
		 0 0.48141146 0 0.48549178 0 0.48064286 0 0.48817828 0 0.48768339 0 0.48843667 0 0.48855427
		 0 0.48699659 0 0.48642558 0 0.4777289 0 0.47850776 0 0.47749981 0 0.47733924 0 0.47926909
		 0 0.47976339 0 0.48551914 0 0.48440787 0 0.48928699 0 0.48967534 0 0.48325881 0 0.48435709
		 0 0.47857472 0 0.47946891 0 0.47890839 0 0.4784492 0 0.47808608 0 0.47782013 0 0.48011211
		 0 0.4778448 0 0.48558164 0 0.48650753 0 0.48227081 0 0.48094466 0 0.487367 0 0.48671454
		 0 0.4875659 0 0.48339942 0 0.48811933 0 0.47968546 0 0.48050573 0 0.47819415 0 0.47767481
		 0 0.48145625 0 0.48235002 0 0.48980039 0 0.48947135 0 0.48868704 0 0.4884142 0 0.48903301
		 0 0.48895863 0 0.49477017 0 0.49367976 0 0.48445976 0 0.48665333 0 0.47275749 0 0.47328934
		 0 0.47320786 0 0.47275636 0 0.48565832 0 0.4835569 0 0.47445312 0 0.4761683 0 0.47292921
		 0 0.47827521 0 0.4748114 0 0.47676429 0 0.47295401 0 0.47299013 0 0.47912809 0 0.49491617
		 0 0.49412876 0 0.4922235 0 0.49284685 0 0.48762646 0 0.48912725 0 0.48189336 0 0.48043242
		 0 0.4901669 0 0.49119866 0 0.48865712 0 0.49028653 0 0.48249367 0 0.48083934 0 0.49120378
		 0 0.4922953 0 0.48458326 0 0.48327109 0 0.48640057 0 0.45662814 0 0.4827067 0 0.48574397
		 0 0.47928923 0 0.47990936 0 0.48175591 0 0.48066381 0 0.47908086 0 0.45030642 0 0.47874537
		 0 0.47815761;
	setAttr ".uvtk[500:515]" 0 0.48008391 0 0.48151594 0 0.449233 0 0.47888458
		 0 0.4814938 0 0.48184881 0 0.48409176 0 0.48419642 0 0.45409822 0 0.48356572 0 0.48620626
		 0 0.48519826 0 0.48521179 0 0.48649383 0 0.48724324 0 0.45847178;
createNode polyTweakUV -n "polyTweakUV8";
	rename -uid "F40D5F79-4C2E-51F0-9B57-B5ABC229DFFB";
	setAttr ".uopa" yes;
	setAttr -s 164 ".uvtk[0:163]" -type "float2" 0 0.49400824 0 0.49458921
		 0 0.48330095 0 0.47286591 0 0.47334 0 0.4926433 0 0.48380837 0 0.47476682 0 0.48810622
		 0 0.47917816 0 0.49425215 0 0.49291134 0 0.49102157 0 0.48910072 0 0.47914627 0 0.47686538
		 0 0.47474006 0 0.47356305 0 0.49475747 0 0.48652408 0 0.4810659 0 0.47293821 0 0.48404625
		 0 0.48865366 0 0.48857686 0 0.48337659 0 0.47976303 0 0.48009428 0 0.4884406 0 0.4844051
		 0 0.48084119 0 0.4869898 0 0.48303735 0 0.48816451 0 0.4872418 0 0.4863919 0 0.48507661
		 0 0.48207229 0 0.48084745 0 0.48015186 0 0.47976202 0 0.48539203 0 0.46165532 0 0.48870867
		 0 0.48410532 0 0.46092099 0 0.46197903 0 0.4936195 0 0.47858736 0 0.45414853 0 0.46104258
		 0 0.49522337 0 0.47381225 0 0.44740963 0 0.47210667 0 0.44443822 0 0.45942646 0 0.4959853
		 0 0.4575156 0 0.49613568 0 0.44295436 0 0.47147527 0 0.47156838 0 0.44232672 0 0.45556551
		 0 0.49551088 0 0.45017105 0 0.48337004 0 0.48664913 0 0.45025092 0 0.44788051 0 0.48093894
		 0 0.48938909 0 0.45057493 0 0.45347857 0 0.4939335 0 0.45173156 0 0.49170962 0 0.44632715
		 0 0.47883555 0 0.47228029 0 0.4423269 0 0.44448876 0 0.4762148 0 0.44294745 0 0.4737018
		 0 0.45622963 0 0.48787513 0 0.48577183 0 0.45587569 0 0.45642895 0 0.48961899 0 0.48274809
		 0 0.45296508 0 0.45605206 0 0.48990136 0 0.48007342 0 0.44996387 0 0.47905186 0 0.44871891
		 0 0.45539922 0 0.48982805 0 0.45418286 0 0.4891341 0 0.44812226 0 0.47859806 0 0.47857514
		 0 0.44787633 0 0.4528923 0 0.48782119 0 0.45145273 0 0.48297575 0 0.48502547 0 0.45161754
		 0 0.44989425 0 0.48147893 0 0.48667014 0 0.48684862 0 0.44877833 0 0.48001194 0 0.47911757
		 0 0.4786599 0 0.45463014 0 0.4532541 0 0.47959879 0 0.44815737 0 0.47807115 0 0.48115116
		 0 0.48811021 0 0.4522028 0 0.48512274 0 0.48277771 0 0.48958078 0 0.47813851 0 0.47860017
		 0 0.49030596 0 0.49045599 0 0.47977641 0 0.48266733 0 0.49009418 0 0.48586884 0 0.48820421
		 0 0.47327802 0 0.47174588 0 0.47592518 0 0.47867504 0 0.4709948 0 0.48081878 0 0.4919951
		 0 0.48956349 0 0.49436733 0 0.4960601 0 0.48677734 0 0.48331067 0 0.49670577 0 0.47093228
		 0 0.4716008 0 0.49652687 0 0.49572256 0 0.47343865 0 0.47837099 0 0.49399763 0 0.48409548
		 0 0.48894092;
createNode polyTweakUV -n "polyTweakUV9";
	rename -uid "9590B433-43F7-7713-4F14-0A871DCDA3E2";
	setAttr ".uopa" yes;
	setAttr -s 252 ".uvtk";
	setAttr ".uvtk[0:249]" -type "float2" 0 0.48168162 0 0.48652565 0 0.48641163
		 0 0.48159128 0 0.48178083 0 0.48643276 0 0.48690483 0 0.48261675 0 0.48512045 0 0.48688781
		 0 0.4824405 0 0.48357272 0 0.48457396 0 0.48461151 0 0.48380294 0 0.48529375 0 0.48703229
		 0 0.48649517 0 0.48706263 0 0.48653507 0 0.4856143 0 0.48566318 0 0.48176563 0 0.48156741
		 0 0.48632577 0 0.48647249 0 0.48173892 0 0.48276973 0 0.48695493 0 0.48642635 0 0.48502433
		 0 0.4825336 0 0.48692065 0 0.48346484 0 0.4844189 0 0.48486662 0 0.48541784 0 0.48402664
		 0 0.48716289 0 0.48670143 0 0.48695725 0 0.48639321 0 0.48585695 0 0.48550308 0 0.48537827
		 0 0.48415357 0 0.48358184 0 0.48516509 0 0.48278746 0 0.47921327 0 0.47944349 0 0.48218337
		 0 0.49138796 0 0.48843625 0 0.48851082 0 0.49219298 0 0.4929871 0 0.47538435 0 0.47684133
		 0 0.47596404 0 0.47703141 0 0.47585201 0 0.49135011 0 0.49263275 0 0.47529694 0 0.4931438
		 0 0.44951391 0 0.48054242 0 0.48044094 0 0.44922799 0 0.45223385 0 0.48134089 0 0.48066103
		 0 0.44955879 0 0.45341831 0 0.4877207 0 0.48803815 0 0.45536226 0 0.4528994 0 0.48768345
		 0 0.45315957 0 0.48774651 0 0.48154867 0 0.45228451 0 0.48310679 0 0.45571828 0 0.45529193
		 0 0.48805538 0 0.45743495 0 0.48789337 0 0.45518965 0 0.48290235 0 0.4879795 0 0.45744634
		 0 0.45664138 0 0.48435843 0 0.45776737 0 0.48591483 0 0.48714817 0 0.4580999 0 0.48428032
		 0 0.45690501 0 0.4856993 0 0.45788556 0 0.45809817 0 0.48700148 0 0.45770353 0 0.48062852
		 0 0.48144165 0 0.45485282 0 0.45813233 0 0.48044491 0 0.45775175 0 0.48063567 0 0.45394516
		 0 0.48770055 0 0.48765197 0 0.45451719 0 0.45179188 0 0.48805717 0 0.4876993 0 0.45401639
		 0 0.45469159 0 0.48169953 0 0.45157564 0 0.48344088 0 0.48806009 0 0.4518277 0 0.48806605
		 0 0.44983608 0 0.48273039 0 0.45203882 0 0.44988304 0 0.4878619 0 0.48407745 0 0.45061064
		 0 0.48560381 0 0.44950604 0 0.44919759 0 0.48689368 0 0.45041329 0 0.48468459 0 0.44942856
		 0 0.48612088 0 0.48732743 0 0.4491955 0 0.45494992 0 0.48555326 0 0.48886114 0 0.45839959
		 0 0.45347238 0 0.48412535 0 0.45182538 0 0.48257646 0 0.45460641 0 0.48514026 0 0.48360321
		 0 0.45292068 0 0.45683616 0 0.48865688 0 0.48220399 0 0.45161641 0 0.4481293 0 0.47873631
		 0 0.44571221 0 0.47518152 0 0.47931316 0 0.44991899 0 0.47663188 0 0.44861406 0 0.49285811
		 0 0.46147883 0 0.45857322 0 0.49186158 0 0.49389035 0 0.46163493 0 0.49406171 0 0.4610185
		 0 0.4599421 0 0.49343973 0 0.44569302 0 0.47443157 0 0.44629484 0 0.47441599 0 0.47515103
		 0 0.44739562 0 0.45630604 0 0.45664632 0 0.45097119 0 0.45064408 0 0.4602322 0 0.44697672
		 0 0.47384962 0 0.47471601 0 0.47634763 0 0.47396284 0 0.47474504 0 0.49391162 0 0.49464399
		 0 0.4921729 0 0.49434426 0 0.49324131 0 0.48877323 0 0.48908827 0 0.47920483 0 0.48217127
		 0 0.47848198 0 0.48246935 0 0.48358548 0 0.48516074 0 0.48413199 0 0.48564693 0 0.48627266
		 0 0.4876534 0 0.48857686 0 0.48459014 0 0.48306507 0 0.48715281 0 0.48567408 0 0.48836312
		 0 0.4839029 0 0.48229033 0 0.48868996 0 0.48083818 0 0.48868889 0 0.48835519 0 0.48112288
		 0 0.4799954 0 0.48835358 0 0.48835281 0 0.47980371 0 0.47998539 0 0.48726469 0 0.48576632
		 0 0.4883655 0 0.48411348 0 0.48268062 0 0.48605677 0 0.48746189 0 0.48849455 0 0.48424202
		 0 0.48248577 0 0.48868603 0 0.4807449 0 0.4886862 0 0.48843047 0 0.48096225 0 0.48001119
		 0 0.48835185 0 0.48837593;
	setAttr ".uvtk[250:251]" 0 0.47980753 0 0.47988439;
createNode polyTweakUV -n "polyTweakUV10";
	rename -uid "CC962E4D-4BB9-AC98-4637-E5A69D29E061";
	setAttr ".uopa" yes;
	setAttr -s 126 ".uvtk[0:125]" -type "float2" 0 0.47980416 0 0.47978622
		 0 0.48236287 0 0.48518586 0 0.48533016 0 0.48058841 0 0.48253727 0 0.48451686 0 0.48230368
		 0 0.48050159 0 0.48431432 0 0.45955795 0 0.47866651 0 0.47974348 0 0.46033579 0 0.44522721
		 0 0.47878224 0 0.44480824 0 0.47987533 0 0.46057379 0 0.48634243 0 0.48632413 0 0.44624209
		 0 0.4610312 0 0.48500162 0 0.48524177 0 0.44540995 0 0.4447782 0 0.48256323 0 0.48220119
		 0 0.4609561 0 0.45285267 0 0.48905089 0 0.47527289 0 0.48248714 0 0.47596025 0 0.48974991
		 0 0.47470489 0 0.47440419 0 0.4750495 0 0.4905926 0 0.48993284 0 0.49039364 0 0.45959395
		 0 0.48946068 0 0.49063963 0 0.46037596 0 0.44518566 0 0.47475576 0 0.44476461 0 0.47389612
		 0 0.46061528 0 0.4902367 0 0.47553006 0 0.44620609 0 0.46107495 0 0.49124318 0 0.47433636
		 0 0.44536948 0 0.44473416 0 0.47325984 0 0.49173161 0 0.46099955 0 0.45285243 0 0.4760001
		 0 0.48965618 0 0.48250163 0 0.48897967 0 0.47530946 0 0.49021995 0 0.49051929 0 0.48988169
		 0 0.47447667 0 0.47512868 0 0.4746733 0 0.45952189 0 0.47559163 0 0.47442511 0 0.4602955
		 0 0.44527066 0 0.49016887 0 0.44485396 0 0.49102163 0 0.46053076 0 0.47482643 0 0.48940828
		 0 0.44627839 0 0.46098584 0 0.47383019 0 0.4905901 0 0.44545114 0 0.44482327 0 0.49165389
		 0 0.47334805 0 0.46091181 0 0.4528532 0 0.47338721 0 0.47274801 0 0.47393957 0 0.49224848
		 0 0.49109727 0 0.49143034 0 0.48953906 0 0.47476503 0 0.49028099 0 0.47548231 0 0.49168894
		 0 0.49233642 0 0.49112743 0 0.47266015 0 0.47382548 0 0.47348377 0 0.47539985 0 0.49029893
		 0 0.47464338 0 0.48957005 0 0.48546255 0 0.48215613 0 0.47922269 0 0.48257387 0 0.48572117
		 0 0.47937796 0 0.48699018 0 0.48699096 0 0.4781346 0 0.47800562;
createNode polyTweakUV -n "polyTweakUV11";
	rename -uid "69D99E21-48EA-4A3E-0F4E-B08286445242";
	setAttr ".uopa" yes;
	setAttr -s 126 ".uvtk[0:125]" -type "float2" 0 0.47980416 0 0.47978622
		 0 0.48236287 0 0.48518586 0 0.48533016 0 0.48058841 0 0.48253727 0 0.48451686 0 0.48230368
		 0 0.48050159 0 0.48431432 0 0.45955795 0 0.47866651 0 0.47974348 0 0.46033579 0 0.44522721
		 0 0.47878224 0 0.44480824 0 0.47987533 0 0.46057379 0 0.48634243 0 0.48632413 0 0.44624209
		 0 0.4610312 0 0.48500162 0 0.48524177 0 0.44540995 0 0.4447782 0 0.48256323 0 0.48220119
		 0 0.4609561 0 0.45285267 0 0.48905089 0 0.47527289 0 0.48248714 0 0.47596025 0 0.48974991
		 0 0.47470489 0 0.47440419 0 0.4750495 0 0.4905926 0 0.48993284 0 0.49039364 0 0.45959395
		 0 0.48946068 0 0.49063963 0 0.46037596 0 0.44518566 0 0.47475576 0 0.44476461 0 0.47389612
		 0 0.46061528 0 0.4902367 0 0.47553006 0 0.44620609 0 0.46107495 0 0.49124318 0 0.47433636
		 0 0.44536948 0 0.44473416 0 0.47325984 0 0.49173161 0 0.46099955 0 0.45285243 0 0.4760001
		 0 0.48965618 0 0.48250163 0 0.48897967 0 0.47530946 0 0.49021995 0 0.49051929 0 0.48988169
		 0 0.47447667 0 0.47512868 0 0.4746733 0 0.45952189 0 0.47559163 0 0.47442511 0 0.4602955
		 0 0.44527066 0 0.49016887 0 0.44485396 0 0.49102163 0 0.46053076 0 0.47482643 0 0.48940828
		 0 0.44627839 0 0.46098584 0 0.47383019 0 0.4905901 0 0.44545114 0 0.44482327 0 0.49165389
		 0 0.47334805 0 0.46091181 0 0.4528532 0 0.47338721 0 0.47274801 0 0.47393957 0 0.49224848
		 0 0.49109727 0 0.49143034 0 0.48953906 0 0.47476503 0 0.49028099 0 0.47548231 0 0.49168894
		 0 0.49233642 0 0.49112743 0 0.47266015 0 0.47382548 0 0.47348377 0 0.47539985 0 0.49029893
		 0 0.47464338 0 0.48957005 0 0.48546255 0 0.48215613 0 0.47922269 0 0.48257387 0 0.48572117
		 0 0.47937796 0 0.48699018 0 0.48699096 0 0.4781346 0 0.47800562;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av -k on ".unw";
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
	setAttr -s 3 ".st";
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
	setAttr -s 6 ".s";
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
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
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
connectAttr "Sweating_pJnt_parCons.ctx" "Sweating_pJnt.tx";
connectAttr "Sweating_pJnt_parCons.cty" "Sweating_pJnt.ty";
connectAttr "Sweating_pJnt_parCons.ctz" "Sweating_pJnt.tz";
connectAttr "Sweating_pJnt_parCons.crx" "Sweating_pJnt.rx";
connectAttr "Sweating_pJnt_parCons.cry" "Sweating_pJnt.ry";
connectAttr "Sweating_pJnt_parCons.crz" "Sweating_pJnt.rz";
connectAttr "Sweating_ctrl.s" "Sweating_pJnt.s";
connectAttr "Sweating_pJnt.ro" "Sweating_pJnt_parCons.cro";
connectAttr "Sweating_pJnt.pim" "Sweating_pJnt_parCons.cpim";
connectAttr "Sweating_pJnt.rp" "Sweating_pJnt_parCons.crp";
connectAttr "Sweating_pJnt.rpt" "Sweating_pJnt_parCons.crt";
connectAttr "Sweating_pJnt.jo" "Sweating_pJnt_parCons.cjo";
connectAttr "SweatingGmbl_ctrl.t" "Sweating_pJnt_parCons.tg[0].tt";
connectAttr "SweatingGmbl_ctrl.rp" "Sweating_pJnt_parCons.tg[0].trp";
connectAttr "SweatingGmbl_ctrl.rpt" "Sweating_pJnt_parCons.tg[0].trt";
connectAttr "SweatingGmbl_ctrl.r" "Sweating_pJnt_parCons.tg[0].tr";
connectAttr "SweatingGmbl_ctrl.ro" "Sweating_pJnt_parCons.tg[0].tro";
connectAttr "SweatingGmbl_ctrl.s" "Sweating_pJnt_parCons.tg[0].ts";
connectAttr "SweatingGmbl_ctrl.pm" "Sweating_pJnt_parCons.tg[0].tpm";
connectAttr "Sweating_pJnt_parCons.w0" "Sweating_pJnt_parCons.tg[0].tw";
connectAttr "Sigh_pJnt_parCons.ctx" "Sigh_pJnt.tx";
connectAttr "Sigh_pJnt_parCons.cty" "Sigh_pJnt.ty";
connectAttr "Sigh_pJnt_parCons.ctz" "Sigh_pJnt.tz";
connectAttr "Sigh_pJnt_parCons.crx" "Sigh_pJnt.rx";
connectAttr "Sigh_pJnt_parCons.cry" "Sigh_pJnt.ry";
connectAttr "Sigh_pJnt_parCons.crz" "Sigh_pJnt.rz";
connectAttr "Sigh_ctrl.s" "Sigh_pJnt.s";
connectAttr "Sigh_pJnt.ro" "Sigh_pJnt_parCons.cro";
connectAttr "Sigh_pJnt.pim" "Sigh_pJnt_parCons.cpim";
connectAttr "Sigh_pJnt.rp" "Sigh_pJnt_parCons.crp";
connectAttr "Sigh_pJnt.rpt" "Sigh_pJnt_parCons.crt";
connectAttr "Sigh_pJnt.jo" "Sigh_pJnt_parCons.cjo";
connectAttr "SighGmbl_ctrl.t" "Sigh_pJnt_parCons.tg[0].tt";
connectAttr "SighGmbl_ctrl.rp" "Sigh_pJnt_parCons.tg[0].trp";
connectAttr "SighGmbl_ctrl.rpt" "Sigh_pJnt_parCons.tg[0].trt";
connectAttr "SighGmbl_ctrl.r" "Sigh_pJnt_parCons.tg[0].tr";
connectAttr "SighGmbl_ctrl.ro" "Sigh_pJnt_parCons.tg[0].tro";
connectAttr "SighGmbl_ctrl.s" "Sigh_pJnt_parCons.tg[0].ts";
connectAttr "SighGmbl_ctrl.pm" "Sigh_pJnt_parCons.tg[0].tpm";
connectAttr "Sigh_pJnt_parCons.w0" "Sigh_pJnt_parCons.tg[0].tw";
connectAttr "Stunned_pJnt_parCons.ctx" "Stunned_pJnt.tx";
connectAttr "Stunned_pJnt_parCons.cty" "Stunned_pJnt.ty";
connectAttr "Stunned_pJnt_parCons.ctz" "Stunned_pJnt.tz";
connectAttr "Stunned_pJnt_parCons.crx" "Stunned_pJnt.rx";
connectAttr "Stunned_pJnt_parCons.cry" "Stunned_pJnt.ry";
connectAttr "Stunned_pJnt_parCons.crz" "Stunned_pJnt.rz";
connectAttr "Stunned_ctrl.s" "Stunned_pJnt.s";
connectAttr "Stunned_pJnt.ro" "Stunned_pJnt_parCons.cro";
connectAttr "Stunned_pJnt.pim" "Stunned_pJnt_parCons.cpim";
connectAttr "Stunned_pJnt.rp" "Stunned_pJnt_parCons.crp";
connectAttr "Stunned_pJnt.rpt" "Stunned_pJnt_parCons.crt";
connectAttr "Stunned_pJnt.jo" "Stunned_pJnt_parCons.cjo";
connectAttr "StunnedGmbl_ctrl.t" "Stunned_pJnt_parCons.tg[0].tt";
connectAttr "StunnedGmbl_ctrl.rp" "Stunned_pJnt_parCons.tg[0].trp";
connectAttr "StunnedGmbl_ctrl.rpt" "Stunned_pJnt_parCons.tg[0].trt";
connectAttr "StunnedGmbl_ctrl.r" "Stunned_pJnt_parCons.tg[0].tr";
connectAttr "StunnedGmbl_ctrl.ro" "Stunned_pJnt_parCons.tg[0].tro";
connectAttr "StunnedGmbl_ctrl.s" "Stunned_pJnt_parCons.tg[0].ts";
connectAttr "StunnedGmbl_ctrl.pm" "Stunned_pJnt_parCons.tg[0].tpm";
connectAttr "Stunned_pJnt_parCons.w0" "Stunned_pJnt_parCons.tg[0].tw";
connectAttr "Shock_pJnt_parCons.ctx" "Shock_pJnt.tx";
connectAttr "Shock_pJnt_parCons.cty" "Shock_pJnt.ty";
connectAttr "Shock_pJnt_parCons.ctz" "Shock_pJnt.tz";
connectAttr "Shock_pJnt_parCons.crx" "Shock_pJnt.rx";
connectAttr "Shock_pJnt_parCons.cry" "Shock_pJnt.ry";
connectAttr "Shock_pJnt_parCons.crz" "Shock_pJnt.rz";
connectAttr "Shock_ctrl.s" "Shock_pJnt.s";
connectAttr "Shock_pJnt.ro" "Shock_pJnt_parCons.cro";
connectAttr "Shock_pJnt.pim" "Shock_pJnt_parCons.cpim";
connectAttr "Shock_pJnt.rp" "Shock_pJnt_parCons.crp";
connectAttr "Shock_pJnt.rpt" "Shock_pJnt_parCons.crt";
connectAttr "Shock_pJnt.jo" "Shock_pJnt_parCons.cjo";
connectAttr "ShockGmbl_ctrl.t" "Shock_pJnt_parCons.tg[0].tt";
connectAttr "ShockGmbl_ctrl.rp" "Shock_pJnt_parCons.tg[0].trp";
connectAttr "ShockGmbl_ctrl.rpt" "Shock_pJnt_parCons.tg[0].trt";
connectAttr "ShockGmbl_ctrl.r" "Shock_pJnt_parCons.tg[0].tr";
connectAttr "ShockGmbl_ctrl.ro" "Shock_pJnt_parCons.tg[0].tro";
connectAttr "ShockGmbl_ctrl.s" "Shock_pJnt_parCons.tg[0].ts";
connectAttr "ShockGmbl_ctrl.pm" "Shock_pJnt_parCons.tg[0].tpm";
connectAttr "Shock_pJnt_parCons.w0" "Shock_pJnt_parCons.tg[0].tw";
connectAttr "Confused_pJnt_parCons.ctx" "Confused_pJnt.tx";
connectAttr "Confused_pJnt_parCons.cty" "Confused_pJnt.ty";
connectAttr "Confused_pJnt_parCons.ctz" "Confused_pJnt.tz";
connectAttr "Confused_pJnt_parCons.crx" "Confused_pJnt.rx";
connectAttr "Confused_pJnt_parCons.cry" "Confused_pJnt.ry";
connectAttr "Confused_pJnt_parCons.crz" "Confused_pJnt.rz";
connectAttr "Confused_ctrl.s" "Confused_pJnt.s";
connectAttr "Confused_pJnt.ro" "Confused_pJnt_parCons.cro";
connectAttr "Confused_pJnt.pim" "Confused_pJnt_parCons.cpim";
connectAttr "Confused_pJnt.rp" "Confused_pJnt_parCons.crp";
connectAttr "Confused_pJnt.rpt" "Confused_pJnt_parCons.crt";
connectAttr "Confused_pJnt.jo" "Confused_pJnt_parCons.cjo";
connectAttr "ConfusedGmbl_ctrl.t" "Confused_pJnt_parCons.tg[0].tt";
connectAttr "ConfusedGmbl_ctrl.rp" "Confused_pJnt_parCons.tg[0].trp";
connectAttr "ConfusedGmbl_ctrl.rpt" "Confused_pJnt_parCons.tg[0].trt";
connectAttr "ConfusedGmbl_ctrl.r" "Confused_pJnt_parCons.tg[0].tr";
connectAttr "ConfusedGmbl_ctrl.ro" "Confused_pJnt_parCons.tg[0].tro";
connectAttr "ConfusedGmbl_ctrl.s" "Confused_pJnt_parCons.tg[0].ts";
connectAttr "ConfusedGmbl_ctrl.pm" "Confused_pJnt_parCons.tg[0].tpm";
connectAttr "Confused_pJnt_parCons.w0" "Confused_pJnt_parCons.tg[0].tw";
connectAttr "Uncomfortable_pJnt_parCons.ctx" "Uncomfortable_pJnt.tx";
connectAttr "Uncomfortable_pJnt_parCons.cty" "Uncomfortable_pJnt.ty";
connectAttr "Uncomfortable_pJnt_parCons.ctz" "Uncomfortable_pJnt.tz";
connectAttr "Uncomfortable_pJnt_parCons.crx" "Uncomfortable_pJnt.rx";
connectAttr "Uncomfortable_pJnt_parCons.cry" "Uncomfortable_pJnt.ry";
connectAttr "Uncomfortable_pJnt_parCons.crz" "Uncomfortable_pJnt.rz";
connectAttr "Uncomfortable_ctrl.s" "Uncomfortable_pJnt.s";
connectAttr "Uncomfortable_pJnt.ro" "Uncomfortable_pJnt_parCons.cro";
connectAttr "Uncomfortable_pJnt.pim" "Uncomfortable_pJnt_parCons.cpim";
connectAttr "Uncomfortable_pJnt.rp" "Uncomfortable_pJnt_parCons.crp";
connectAttr "Uncomfortable_pJnt.rpt" "Uncomfortable_pJnt_parCons.crt";
connectAttr "Uncomfortable_pJnt.jo" "Uncomfortable_pJnt_parCons.cjo";
connectAttr "UncomfortableGmbl_ctrl.t" "Uncomfortable_pJnt_parCons.tg[0].tt";
connectAttr "UncomfortableGmbl_ctrl.rp" "Uncomfortable_pJnt_parCons.tg[0].trp";
connectAttr "UncomfortableGmbl_ctrl.rpt" "Uncomfortable_pJnt_parCons.tg[0].trt";
connectAttr "UncomfortableGmbl_ctrl.r" "Uncomfortable_pJnt_parCons.tg[0].tr";
connectAttr "UncomfortableGmbl_ctrl.ro" "Uncomfortable_pJnt_parCons.tg[0].tro";
connectAttr "UncomfortableGmbl_ctrl.s" "Uncomfortable_pJnt_parCons.tg[0].ts";
connectAttr "UncomfortableGmbl_ctrl.pm" "Uncomfortable_pJnt_parCons.tg[0].tpm";
connectAttr "Uncomfortable_pJnt_parCons.w0" "Uncomfortable_pJnt_parCons.tg[0].tw"
		;
connectAttr "Joy_pJnt_parCons.ctx" "Joy_pJnt.tx";
connectAttr "Joy_pJnt_parCons.cty" "Joy_pJnt.ty";
connectAttr "Joy_pJnt_parCons.ctz" "Joy_pJnt.tz";
connectAttr "Joy_pJnt_parCons.crx" "Joy_pJnt.rx";
connectAttr "Joy_pJnt_parCons.cry" "Joy_pJnt.ry";
connectAttr "Joy_pJnt_parCons.crz" "Joy_pJnt.rz";
connectAttr "Joy_ctrl.s" "Joy_pJnt.s";
connectAttr "Joy_pJnt.ro" "Joy_pJnt_parCons.cro";
connectAttr "Joy_pJnt.pim" "Joy_pJnt_parCons.cpim";
connectAttr "Joy_pJnt.rp" "Joy_pJnt_parCons.crp";
connectAttr "Joy_pJnt.rpt" "Joy_pJnt_parCons.crt";
connectAttr "Joy_pJnt.jo" "Joy_pJnt_parCons.cjo";
connectAttr "JoyGmbl_ctrl.t" "Joy_pJnt_parCons.tg[0].tt";
connectAttr "JoyGmbl_ctrl.rp" "Joy_pJnt_parCons.tg[0].trp";
connectAttr "JoyGmbl_ctrl.rpt" "Joy_pJnt_parCons.tg[0].trt";
connectAttr "JoyGmbl_ctrl.r" "Joy_pJnt_parCons.tg[0].tr";
connectAttr "JoyGmbl_ctrl.ro" "Joy_pJnt_parCons.tg[0].tro";
connectAttr "JoyGmbl_ctrl.s" "Joy_pJnt_parCons.tg[0].ts";
connectAttr "JoyGmbl_ctrl.pm" "Joy_pJnt_parCons.tg[0].tpm";
connectAttr "Joy_pJnt_parCons.w0" "Joy_pJnt_parCons.tg[0].tw";
connectAttr "Love_pJnt_parCons.ctx" "Love_pJnt.tx";
connectAttr "Love_pJnt_parCons.cty" "Love_pJnt.ty";
connectAttr "Love_pJnt_parCons.ctz" "Love_pJnt.tz";
connectAttr "Love_pJnt_parCons.crx" "Love_pJnt.rx";
connectAttr "Love_pJnt_parCons.cry" "Love_pJnt.ry";
connectAttr "Love_pJnt_parCons.crz" "Love_pJnt.rz";
connectAttr "Love_ctrl.s" "Love_pJnt.s";
connectAttr "Love_pJnt.ro" "Love_pJnt_parCons.cro";
connectAttr "Love_pJnt.pim" "Love_pJnt_parCons.cpim";
connectAttr "Love_pJnt.rp" "Love_pJnt_parCons.crp";
connectAttr "Love_pJnt.rpt" "Love_pJnt_parCons.crt";
connectAttr "Love_pJnt.jo" "Love_pJnt_parCons.cjo";
connectAttr "LoveGmbl_ctrl.t" "Love_pJnt_parCons.tg[0].tt";
connectAttr "LoveGmbl_ctrl.rp" "Love_pJnt_parCons.tg[0].trp";
connectAttr "LoveGmbl_ctrl.rpt" "Love_pJnt_parCons.tg[0].trt";
connectAttr "LoveGmbl_ctrl.r" "Love_pJnt_parCons.tg[0].tr";
connectAttr "LoveGmbl_ctrl.ro" "Love_pJnt_parCons.tg[0].tro";
connectAttr "LoveGmbl_ctrl.s" "Love_pJnt_parCons.tg[0].ts";
connectAttr "LoveGmbl_ctrl.pm" "Love_pJnt_parCons.tg[0].tpm";
connectAttr "Love_pJnt_parCons.w0" "Love_pJnt_parCons.tg[0].tw";
connectAttr "Angry_pJnt_parCons.ctx" "Angry_pJnt.tx";
connectAttr "Angry_pJnt_parCons.cty" "Angry_pJnt.ty";
connectAttr "Angry_pJnt_parCons.ctz" "Angry_pJnt.tz";
connectAttr "Angry_pJnt_parCons.crx" "Angry_pJnt.rx";
connectAttr "Angry_pJnt_parCons.cry" "Angry_pJnt.ry";
connectAttr "Angry_pJnt_parCons.crz" "Angry_pJnt.rz";
connectAttr "Angry_ctrl.s" "Angry_pJnt.s";
connectAttr "Angry_pJnt.ro" "Angry_pJnt_parCons.cro";
connectAttr "Angry_pJnt.pim" "Angry_pJnt_parCons.cpim";
connectAttr "Angry_pJnt.rp" "Angry_pJnt_parCons.crp";
connectAttr "Angry_pJnt.rpt" "Angry_pJnt_parCons.crt";
connectAttr "Angry_pJnt.jo" "Angry_pJnt_parCons.cjo";
connectAttr "AngryGmbl_ctrl.t" "Angry_pJnt_parCons.tg[0].tt";
connectAttr "AngryGmbl_ctrl.rp" "Angry_pJnt_parCons.tg[0].trp";
connectAttr "AngryGmbl_ctrl.rpt" "Angry_pJnt_parCons.tg[0].trt";
connectAttr "AngryGmbl_ctrl.r" "Angry_pJnt_parCons.tg[0].tr";
connectAttr "AngryGmbl_ctrl.ro" "Angry_pJnt_parCons.tg[0].tro";
connectAttr "AngryGmbl_ctrl.s" "Angry_pJnt_parCons.tg[0].ts";
connectAttr "AngryGmbl_ctrl.pm" "Angry_pJnt_parCons.tg[0].tpm";
connectAttr "Angry_pJnt_parCons.w0" "Angry_pJnt_parCons.tg[0].tw";
connectAttr "ShyL_pJnt_parCons.ctx" "ShyL_pJnt.tx";
connectAttr "ShyL_pJnt_parCons.cty" "ShyL_pJnt.ty";
connectAttr "ShyL_pJnt_parCons.ctz" "ShyL_pJnt.tz";
connectAttr "ShyL_pJnt_parCons.crx" "ShyL_pJnt.rx";
connectAttr "ShyL_pJnt_parCons.cry" "ShyL_pJnt.ry";
connectAttr "ShyL_pJnt_parCons.crz" "ShyL_pJnt.rz";
connectAttr "ShyL_ctrl.s" "ShyL_pJnt.s";
connectAttr "ShyL_pJnt.ro" "ShyL_pJnt_parCons.cro";
connectAttr "ShyL_pJnt.pim" "ShyL_pJnt_parCons.cpim";
connectAttr "ShyL_pJnt.rp" "ShyL_pJnt_parCons.crp";
connectAttr "ShyL_pJnt.rpt" "ShyL_pJnt_parCons.crt";
connectAttr "ShyL_pJnt.jo" "ShyL_pJnt_parCons.cjo";
connectAttr "ShyLGmbl_ctrl.t" "ShyL_pJnt_parCons.tg[0].tt";
connectAttr "ShyLGmbl_ctrl.rp" "ShyL_pJnt_parCons.tg[0].trp";
connectAttr "ShyLGmbl_ctrl.rpt" "ShyL_pJnt_parCons.tg[0].trt";
connectAttr "ShyLGmbl_ctrl.r" "ShyL_pJnt_parCons.tg[0].tr";
connectAttr "ShyLGmbl_ctrl.ro" "ShyL_pJnt_parCons.tg[0].tro";
connectAttr "ShyLGmbl_ctrl.s" "ShyL_pJnt_parCons.tg[0].ts";
connectAttr "ShyLGmbl_ctrl.pm" "ShyL_pJnt_parCons.tg[0].tpm";
connectAttr "ShyL_pJnt_parCons.w0" "ShyL_pJnt_parCons.tg[0].tw";
connectAttr "ShyR_pJnt_parCons.ctx" "ShyR_pJnt.tx";
connectAttr "ShyR_pJnt_parCons.cty" "ShyR_pJnt.ty";
connectAttr "ShyR_pJnt_parCons.ctz" "ShyR_pJnt.tz";
connectAttr "ShyR_pJnt_parCons.crx" "ShyR_pJnt.rx";
connectAttr "ShyR_pJnt_parCons.cry" "ShyR_pJnt.ry";
connectAttr "ShyR_pJnt_parCons.crz" "ShyR_pJnt.rz";
connectAttr "ShyR_ctrl.s" "ShyR_pJnt.s";
connectAttr "ShyR_pJnt.ro" "ShyR_pJnt_parCons.cro";
connectAttr "ShyR_pJnt.pim" "ShyR_pJnt_parCons.cpim";
connectAttr "ShyR_pJnt.rp" "ShyR_pJnt_parCons.crp";
connectAttr "ShyR_pJnt.rpt" "ShyR_pJnt_parCons.crt";
connectAttr "ShyR_pJnt.jo" "ShyR_pJnt_parCons.cjo";
connectAttr "ShyRGmbl_ctrl.t" "ShyR_pJnt_parCons.tg[0].tt";
connectAttr "ShyRGmbl_ctrl.rp" "ShyR_pJnt_parCons.tg[0].trp";
connectAttr "ShyRGmbl_ctrl.rpt" "ShyR_pJnt_parCons.tg[0].trt";
connectAttr "ShyRGmbl_ctrl.r" "ShyR_pJnt_parCons.tg[0].tr";
connectAttr "ShyRGmbl_ctrl.ro" "ShyR_pJnt_parCons.tg[0].tro";
connectAttr "ShyRGmbl_ctrl.s" "ShyR_pJnt_parCons.tg[0].ts";
connectAttr "ShyRGmbl_ctrl.pm" "ShyR_pJnt_parCons.tg[0].tpm";
connectAttr "ShyR_pJnt_parCons.w0" "ShyR_pJnt_parCons.tg[0].tw";
connectAttr "popupSweating_cnd.oc" "SweatingCon_grp.t";
connectAttr "Sweating_ctrlShape.gimbal" "SweatingGmbl_ctrlShape.v";
connectAttr "popupSigh_cnd.oc" "SighCon_grp.t";
connectAttr "Sigh_ctrlShape.gimbal" "SighGmbl_ctrlShape.v";
connectAttr "popupStunned_cnd.oc" "StunnedCon_grp.t";
connectAttr "Stunned_ctrlShape.gimbal" "StunnedGmbl_ctrlShape.v";
connectAttr "popupShock_cnd.oc" "ShockCon_grp.t";
connectAttr "Shock_ctrlShape.gimbal" "ShockGmbl_ctrlShape.v";
connectAttr "popupConfused_cnd.oc" "ConfusedCon_grp.t";
connectAttr "Confused_ctrlShape.gimbal" "ConfusedGmbl_ctrlShape.v";
connectAttr "popupUncomfortable_cnd.oc" "UncomfortableCon_grp.t";
connectAttr "Uncomfortable_ctrlShape.gimbal" "UncomfortableGmbl_ctrlShape.v";
connectAttr "popupJoy_cnd.oc" "JoyCon_grp.t";
connectAttr "Joy_ctrlShape.gimbal" "JoyGmbl_ctrlShape.v";
connectAttr "popupLove_cnd.oc" "LoveCon_grp.t";
connectAttr "Love_ctrlShape.gimbal" "LoveGmbl_ctrlShape.v";
connectAttr "popupAngry_cnd.oc" "AngryCon_grp.t";
connectAttr "Angry_ctrlShape.gimbal" "AngryGmbl_ctrlShape.v";
connectAttr "popupShyL_cnd.oc" "ShyLCon_grp.t";
connectAttr "ShyL_ctrlShape.gimbal" "ShyLGmbl_ctrlShape.v";
connectAttr "popupShyR_cnd.oc" "ShyRCon_grp.t";
connectAttr "ShyR_ctrlShape.gimbal" "ShyRGmbl_ctrlShape.v";
connectAttr "polyTweakUV1.out" "SweatingShape.i";
connectAttr "polyTweakUV1.uvtk[0]" "SweatingShape.uvst[0].uvtw";
connectAttr "polyTweakUV2.out" "SighShape.i";
connectAttr "polyTweakUV2.uvtk[0]" "SighShape.uvst[0].uvtw";
connectAttr "polyTweakUV3.out" "StunnedShape.i";
connectAttr "polyTweakUV3.uvtk[0]" "StunnedShape.uvst[0].uvtw";
connectAttr "polyTweakUV4.out" "ShockShape.i";
connectAttr "polyTweakUV4.uvtk[0]" "ShockShape.uvst[0].uvtw";
connectAttr "polyTweakUV5.out" "ConfusedShape.i";
connectAttr "polyTweakUV5.uvtk[0]" "ConfusedShape.uvst[0].uvtw";
connectAttr "polyTweakUV6.out" "UncomfortableShape.i";
connectAttr "polyTweakUV6.uvtk[0]" "UncomfortableShape.uvst[0].uvtw";
connectAttr "polyTweakUV7.out" "JoyShape.i";
connectAttr "polyTweakUV7.uvtk[0]" "JoyShape.uvst[0].uvtw";
connectAttr "polyTweakUV8.out" "LoveShape.i";
connectAttr "polyTweakUV8.uvtk[0]" "LoveShape.uvst[0].uvtw";
connectAttr "polyTweakUV9.out" "AngryShape.i";
connectAttr "polyTweakUV9.uvtk[0]" "AngryShape.uvst[0].uvtw";
connectAttr "polyTweakUV10.out" "ShyLShape.i";
connectAttr "polyTweakUV10.uvtk[0]" "ShyLShape.uvst[0].uvtw";
connectAttr "polyTweakUV11.out" "ShyRShape.i";
connectAttr "polyTweakUV11.uvtk[0]" "ShyRShape.uvst[0].uvtw";
connectAttr "facialSwitch_ctrl.Sweating" "popupSweating_cnd.ft";
connectAttr "popupB_loc.t" "popupSweating_cnd.ct";
connectAttr "facialSwitch_ctrl.Sigh" "popupSigh_cnd.ft";
connectAttr "popupC_loc.t" "popupSigh_cnd.ct";
connectAttr "facialSwitch_ctrl.Stunned" "popupStunned_cnd.ft";
connectAttr "popupA_loc.t" "popupStunned_cnd.ct";
connectAttr "facialSwitch_ctrl.Shock" "popupShock_cnd.ft";
connectAttr "popupA_loc.t" "popupShock_cnd.ct";
connectAttr "facialSwitch_ctrl.Confused" "popupConfused_cnd.ft";
connectAttr "popupA_loc.t" "popupConfused_cnd.ct";
connectAttr "facialSwitch_ctrl.Uncomfortable" "popupUncomfortable_cnd.ft";
connectAttr "popupA_loc.t" "popupUncomfortable_cnd.ct";
connectAttr "facialSwitch_ctrl.Joy" "popupJoy_cnd.ft";
connectAttr "popupA_loc.t" "popupJoy_cnd.ct";
connectAttr "facialSwitch_ctrl.Love" "popupLove_cnd.ft";
connectAttr "popupA_loc.t" "popupLove_cnd.ct";
connectAttr "facialSwitch_ctrl.Angry" "popupAngry_cnd.ft";
connectAttr "popupB_loc.t" "popupAngry_cnd.ct";
connectAttr "facialSwitch_ctrl.ShyL" "popupShyL_cnd.ft";
connectAttr "popupD_loc.t" "popupShyL_cnd.ct";
connectAttr "facialSwitch_ctrl.ShyR" "popupShyR_cnd.ft";
connectAttr "popupE_loc.t" "popupShyR_cnd.ct";
connectAttr "SweatingShapeOrig.w" "Sweating_skc.ip[0].ig";
connectAttr "SweatingShapeOrig.o" "Sweating_skc.orggeom[0]";
connectAttr "emoG01_bind.msg" "Sweating_skc.bp";
connectAttr "Sweating_pJnt.wm" "Sweating_skc.ma[0]";
connectAttr "Sweating_pJnt.liw" "Sweating_skc.lw[0]";
connectAttr "Sweating_pJnt.obcc" "Sweating_skc.ifcl[0]";
connectAttr "Sweating_pJnt.msg" "Sweating_skc.ptt";
connectAttr "popUpJnt_grp.msg" "emoG01_bind.m[0]";
connectAttr "Sweating_pJnt.msg" "emoG01_bind.m[1]";
connectAttr "emoG01_bind.w" "emoG01_bind.p[0]";
connectAttr "emoG01_bind.m[0]" "emoG01_bind.p[1]";
connectAttr "Sweating_pJnt.bps" "emoG01_bind.wm[1]";
connectAttr "SH_C001_Ashford_01_Head.msg" "materialInfo71.sg";
connectAttr "M_C001_Ashford_01_Head.msg" "materialInfo71.m";
connectAttr "file2.msg" "materialInfo71.t" -na;
connectAttr "M_C001_Ashford_01_Head.oc" "SH_C001_Ashford_01_Head.ss";
connectAttr "ShyRShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "SighShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "LoveShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "StunnedShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "ShyLShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "ShockShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "JoyShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "SweatingShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "AngryShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "UncomfortableShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "ConfusedShape.iog" "SH_C001_Ashford_01_Head.dsm" -na;
connectAttr "file2.oc" "M_C001_Ashford_01_Head.c";
connectAttr ":defaultColorMgtGlobals.cme" "file2.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "file2.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "file2.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "file2.ws";
connectAttr "place2dTexture1.c" "file2.c";
connectAttr "place2dTexture1.tf" "file2.tf";
connectAttr "place2dTexture1.rf" "file2.rf";
connectAttr "place2dTexture1.mu" "file2.mu";
connectAttr "place2dTexture1.mv" "file2.mv";
connectAttr "place2dTexture1.s" "file2.s";
connectAttr "place2dTexture1.wu" "file2.wu";
connectAttr "place2dTexture1.wv" "file2.wv";
connectAttr "place2dTexture1.re" "file2.re";
connectAttr "place2dTexture1.of" "file2.of";
connectAttr "place2dTexture1.r" "file2.ro";
connectAttr "place2dTexture1.n" "file2.n";
connectAttr "place2dTexture1.vt1" "file2.vt1";
connectAttr "place2dTexture1.vt2" "file2.vt2";
connectAttr "place2dTexture1.vt3" "file2.vt3";
connectAttr "place2dTexture1.vc1" "file2.vc1";
connectAttr "place2dTexture1.o" "file2.uv";
connectAttr "place2dTexture1.ofs" "file2.fs";
connectAttr "SighShapeOrig.w" "Sigh_skc.ip[0].ig";
connectAttr "SighShapeOrig.o" "Sigh_skc.orggeom[0]";
connectAttr "emoH01_bind.msg" "Sigh_skc.bp";
connectAttr "Sigh_pJnt.wm" "Sigh_skc.ma[0]";
connectAttr "Sigh_pJnt.liw" "Sigh_skc.lw[0]";
connectAttr "Sigh_pJnt.obcc" "Sigh_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoH01_bind.m[0]";
connectAttr "Sigh_pJnt.msg" "emoH01_bind.m[1]";
connectAttr "emoH01_bind.w" "emoH01_bind.p[0]";
connectAttr "emoH01_bind.m[0]" "emoH01_bind.p[1]";
connectAttr "StunnedShapeOrig.w" "Stunned_skc.ip[0].ig";
connectAttr "StunnedShapeOrig.o" "Stunned_skc.orggeom[0]";
connectAttr "emoI01_bind.msg" "Stunned_skc.bp";
connectAttr "Stunned_pJnt.wm" "Stunned_skc.ma[0]";
connectAttr "Stunned_pJnt.liw" "Stunned_skc.lw[0]";
connectAttr "Stunned_pJnt.obcc" "Stunned_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoI01_bind.m[0]";
connectAttr "Stunned_pJnt.msg" "emoI01_bind.m[1]";
connectAttr "emoI01_bind.w" "emoI01_bind.p[0]";
connectAttr "emoI01_bind.m[0]" "emoI01_bind.p[1]";
connectAttr "ShockShapeOrig.w" "Shock_skc.ip[0].ig";
connectAttr "ShockShapeOrig.o" "Shock_skc.orggeom[0]";
connectAttr "emoJ01_bind.msg" "Shock_skc.bp";
connectAttr "Shock_pJnt.wm" "Shock_skc.ma[0]";
connectAttr "Shock_pJnt.liw" "Shock_skc.lw[0]";
connectAttr "Shock_pJnt.obcc" "Shock_skc.ifcl[0]";
connectAttr "Shock_pJnt.msg" "Shock_skc.ptt";
connectAttr "popUpJnt_grp.msg" "emoJ01_bind.m[0]";
connectAttr "Shock_pJnt.msg" "emoJ01_bind.m[1]";
connectAttr "emoJ01_bind.w" "emoJ01_bind.p[0]";
connectAttr "emoJ01_bind.m[0]" "emoJ01_bind.p[1]";
connectAttr "ConfusedShapeOrig.w" "Confused_skc.ip[0].ig";
connectAttr "ConfusedShapeOrig.o" "Confused_skc.orggeom[0]";
connectAttr "emoK01_bind.msg" "Confused_skc.bp";
connectAttr "Confused_pJnt.wm" "Confused_skc.ma[0]";
connectAttr "Confused_pJnt.liw" "Confused_skc.lw[0]";
connectAttr "Confused_pJnt.obcc" "Confused_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoK01_bind.m[0]";
connectAttr "Confused_pJnt.msg" "emoK01_bind.m[1]";
connectAttr "emoK01_bind.w" "emoK01_bind.p[0]";
connectAttr "emoK01_bind.m[0]" "emoK01_bind.p[1]";
connectAttr "UncomfortableShapeOrig.w" "Uncomfortable_skc.ip[0].ig";
connectAttr "UncomfortableShapeOrig.o" "Uncomfortable_skc.orggeom[0]";
connectAttr "emoA01_bind.msg" "Uncomfortable_skc.bp";
connectAttr "Uncomfortable_pJnt.wm" "Uncomfortable_skc.ma[0]";
connectAttr "Uncomfortable_pJnt.liw" "Uncomfortable_skc.lw[0]";
connectAttr "Uncomfortable_pJnt.obcc" "Uncomfortable_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoA01_bind.m[0]";
connectAttr "Uncomfortable_pJnt.msg" "emoA01_bind.m[1]";
connectAttr "emoA01_bind.w" "emoA01_bind.p[0]";
connectAttr "emoA01_bind.m[0]" "emoA01_bind.p[1]";
connectAttr "JoyShapeOrig.w" "Joy_skc.ip[0].ig";
connectAttr "JoyShapeOrig.o" "Joy_skc.orggeom[0]";
connectAttr "emoB01_bind.msg" "Joy_skc.bp";
connectAttr "Joy_pJnt.wm" "Joy_skc.ma[0]";
connectAttr "Joy_pJnt.liw" "Joy_skc.lw[0]";
connectAttr "Joy_pJnt.obcc" "Joy_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoB01_bind.m[0]";
connectAttr "Joy_pJnt.msg" "emoB01_bind.m[1]";
connectAttr "emoB01_bind.w" "emoB01_bind.p[0]";
connectAttr "emoB01_bind.m[0]" "emoB01_bind.p[1]";
connectAttr "LoveShapeOrig.w" "Love_skc.ip[0].ig";
connectAttr "LoveShapeOrig.o" "Love_skc.orggeom[0]";
connectAttr "emoC01_bind.msg" "Love_skc.bp";
connectAttr "Love_pJnt.wm" "Love_skc.ma[0]";
connectAttr "Love_pJnt.liw" "Love_skc.lw[0]";
connectAttr "Love_pJnt.obcc" "Love_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoC01_bind.m[0]";
connectAttr "Love_pJnt.msg" "emoC01_bind.m[1]";
connectAttr "emoC01_bind.w" "emoC01_bind.p[0]";
connectAttr "emoC01_bind.m[0]" "emoC01_bind.p[1]";
connectAttr "AngryShapeOrig.w" "Angry_skc.ip[0].ig";
connectAttr "AngryShapeOrig.o" "Angry_skc.orggeom[0]";
connectAttr "emoD01_bind.msg" "Angry_skc.bp";
connectAttr "Angry_pJnt.wm" "Angry_skc.ma[0]";
connectAttr "Angry_pJnt.liw" "Angry_skc.lw[0]";
connectAttr "Angry_pJnt.obcc" "Angry_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoD01_bind.m[0]";
connectAttr "Angry_pJnt.msg" "emoD01_bind.m[1]";
connectAttr "emoD01_bind.w" "emoD01_bind.p[0]";
connectAttr "emoD01_bind.m[0]" "emoD01_bind.p[1]";
connectAttr "ShyLShapeOrig.w" "ShyL_skc.ip[0].ig";
connectAttr "ShyLShapeOrig.o" "ShyL_skc.orggeom[0]";
connectAttr "emoE01_bind.msg" "ShyL_skc.bp";
connectAttr "ShyL_pJnt.wm" "ShyL_skc.ma[0]";
connectAttr "ShyL_pJnt.liw" "ShyL_skc.lw[0]";
connectAttr "ShyL_pJnt.obcc" "ShyL_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoE01_bind.m[0]";
connectAttr "ShyL_pJnt.msg" "emoE01_bind.m[1]";
connectAttr "emoE01_bind.w" "emoE01_bind.p[0]";
connectAttr "emoE01_bind.m[0]" "emoE01_bind.p[1]";
connectAttr "ShyRShapeOrig.w" "ShyR_skc.ip[0].ig";
connectAttr "ShyRShapeOrig.o" "ShyR_skc.orggeom[0]";
connectAttr "emoF01_bind.msg" "ShyR_skc.bp";
connectAttr "ShyR_pJnt.wm" "ShyR_skc.ma[0]";
connectAttr "ShyR_pJnt.liw" "ShyR_skc.lw[0]";
connectAttr "ShyR_pJnt.obcc" "ShyR_skc.ifcl[0]";
connectAttr "popUpJnt_grp.msg" "emoF01_bind.m[0]";
connectAttr "ShyR_pJnt.msg" "emoF01_bind.m[1]";
connectAttr "emoF01_bind.w" "emoF01_bind.p[0]";
connectAttr "emoF01_bind.m[0]" "emoF01_bind.p[1]";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "SH_C001_Ashford_01_Head.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "SH_C001_Ashford_01_Head.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "layerManager.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "shapeEditorManager.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "defaultLayer.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "poseInterpolatorManager.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "Sweating_skc.og[0]" "polyTweakUV1.ip";
connectAttr "Sigh_skc.og[0]" "polyTweakUV2.ip";
connectAttr "Stunned_skc.og[0]" "polyTweakUV3.ip";
connectAttr "Shock_skc.og[0]" "polyTweakUV4.ip";
connectAttr "Confused_skc.og[0]" "polyTweakUV5.ip";
connectAttr "Uncomfortable_skc.og[0]" "polyTweakUV6.ip";
connectAttr "Joy_skc.og[0]" "polyTweakUV7.ip";
connectAttr "Love_skc.og[0]" "polyTweakUV8.ip";
connectAttr "Angry_skc.og[0]" "polyTweakUV9.ip";
connectAttr "ShyL_skc.og[0]" "polyTweakUV10.ip";
connectAttr "ShyR_skc.og[0]" "polyTweakUV11.ip";
connectAttr "SH_C001_Ashford_01_Head.pa" ":renderPartition.st" -na;
connectAttr "M_C001_Ashford_01_Head.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "file2.msg" ":defaultTextureList1.tx" -na;
// End of template_facialSwitch_with_emo.ma
