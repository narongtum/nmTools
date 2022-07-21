//Maya ASCII 2018ff09 scene
//Name: templateJoint_quaruped.ma
//Last modified: Thu, Jul 23, 2020 09:21:36 AM
//Codeset: 1252
requires maya "2018ff09";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2018.0.0";
requires "stereoCamera" "10.0";
requires "OctanePlugin" "v1.0 RC3c beta";
requires -nodeType "aiOptions" -nodeType "aiAOVDriver" -nodeType "aiAOVFilter" "mtoa" "2.0.1";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201903222215-65bada0e52";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "C86A014E-4699-F17A-7455-878E9A23D810";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 146.28961253427173 71.372735249580131 43.892317913532814 ;
	setAttr ".r" -type "double3" -14.138352727736363 -644.99999999988449 -3.0721799087733357e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "ACA8B39B-45E3-560A-AA08-2AB951E6F44F";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 156.18107318169351;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 1.6370447619706852e-06 33.22329481684713 4.6941348128737275 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "4E27F4AC-4BFB-B822-5235-939C582B6156";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 6.365996599528847 1001.8048062318668 19.41913173933472 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "1EE5DFDC-4202-EAC7-0FF7-86A9F2AC9C80";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1001.8958837980136;
	setAttr ".ow" 18.140993096836038;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 6.365996599528847 -0.091077566146851141 19.419131739334496 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "489DE964-42E9-C808-1C2E-3E9BE354BF21";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -2.0019275572039654 52.240990138653046 1008.7558275564999 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "8B25FDBD-4097-88DD-CFEC-B28D0373566E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 963.43596981240364;
	setAttr ".ow" 2.5545737526452346;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 0.20219079695190345 52.280634830064727 45.319857744096225 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "6FD2E235-4624-513F-C408-3B950E6123BD";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1002.7585673834649 48.026391938680085 34.198536250336481 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "A6BFEFE4-4ACE-3EDC-2B17-679C332302C8";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1002.8057512045197;
	setAttr ".ow" 18.068344842403551;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" -0.047183821054729402 48.051876205030439 41.028319632232105 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "template_ctrl";
	rename -uid "552AB201-4AD4-9077-1E38-C1B0BF2F5EDC";
	setAttr -l on -k off ".v";
createNode nurbsCurve -n "template_ctrlShape" -p "template_ctrl";
	rename -uid "CDB16A94-4601-4314-A470-669D87D68972";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".ovrgb" -type "float3" 0.88571429 0.88571429 0.88571429 ;
	setAttr ".cc" -type "nurbsCurve" 
		1 25 0 no 3
		26 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		26
		-11.828771556225975 0 -11.828771556225943
		-11.828771556225975 0 -11.828771556225943
		-5.9143857781129716 0 -17.743157334338949
		-11.828771556225943 0 -17.743157334338949
		0 0 -29.571928890564887
		11.828771556225943 0 -17.743157334338949
		5.9143857781129716 0 -17.743157334338949
		11.828771556225943 0 -11.744655581661394
		17.743157334338949 0 -5.9143857781129716
		17.743157334338949 0 -11.828771556225943
		29.571928890564887 0 0
		17.743157334338949 0 11.828771556225943
		17.743157334338949 0 5.9143857781129716
		11.828771556225975 0 11.828771556225943
		5.9143857781129716 0 17.743157334338949
		11.828771556225943 0 17.743157334338949
		0 0 29.571928890564887
		-11.828771556225943 0 17.743157334338949
		-5.9143857781129716 0 17.743157334338949
		-11.828771556225975 0 11.828771556225943
		-17.743157334338949 0 5.9143857781129716
		-17.743157334338949 0 11.828771556225943
		-29.571928890564887 0 0
		-17.743157334338949 0 -11.828771556225943
		-17.743157334338949 0 -5.9143857781129716
		-11.828771556225975 0 -11.828771556225943
		;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode joint -n "root" -p "template_ctrl";
	rename -uid "70924AE2-4267-B8B4-1273-2DA218BD6F3E";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode joint -n "body_tmpJnt" -p "root";
	rename -uid "34AB92C9-4E80-F068-AB2F-B1A3941482B6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 42.522633742464386 0.061617580818038593 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.813455445823308 0 1;
	setAttr ".liw" yes;
createNode joint -n "upperBody_tmpJnt" -p "body_tmpJnt";
	rename -uid "0FF7C8BC-4778-8BD9-F9E9-31822B18392F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -0.56806136378330052 9.565067985511158 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.813453674316399 9.8227388198240426 1;
	setAttr ".liw" yes;
createNode joint -n "chest_tmpJnt" -p "upperBody_tmpJnt";
	rename -uid "C7302932-4818-FD0A-BDEB-E18530A4615D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -2.8754278283920698 6.5531568845373105 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 42.544622433140994 22.069059864195697 1;
	setAttr ".liw" yes;
createNode joint -n "upLegFrontLFT_tmpJnt" -p "chest_tmpJnt";
	rename -uid "B43A901E-4FCA-3753-C6CB-0FA367679699";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.5108446358437 -9.2536095550482038 2.4532020870969617 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -17.42837008761984 0.31008886875791697 -179.01232214598113 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.038135510126723025 -0.92276387562020457 0.38347426604369977 0 -0.010187723475372425 0.38337444395253667 0.92353681356753325 0
		 8.8692702724309012 33.74871606997359 -23.928017947855178 1;
	setAttr ".liw" yes;
createNode joint -n "midLegFrontLFT_tmpJnt" -p "upLegFrontLFT_tmpJnt";
	rename -uid "D7847498-4CF9-8487-95BA-FBB4C88844B4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.7143402633758428e-15 6.9914256750615378 -0.30871427930261763 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 19.264398249803694 -0.60925348817795688 0.70744930648863258 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.026827197462727256 -0.77013788114561099 -0.6373130671034799 0 0.028955281358189037 -0.63667635298484737 0.77058731707145456 0
		 9.2884817537506876 23.605067562583631 -19.712607842240914 1;
	setAttr ".liw" yes;
createNode joint -n "lowLegFrontLFT_tmpJnt" -p "midLegFrontLFT_tmpJnt";
	rename -uid "2A9434EF-4F41-FA81-3043-E58D9840D81B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.2172489379008766e-15 15.883803208683199 2.8421709430404007e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -15.398987144888212 0.49366597044931054 -0.054296513068015403 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.6930965747606965 11.989646232807946 -29.324730521287474 1;
	setAttr ".liw" yes;
createNode joint -n "ankleFrontLFT_tmpJnt" -p "lowLegFrontLFT_tmpJnt";
	rename -uid "7D79711E-4C75-5B7F-5CA9-1395F3D18BC3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.6645352591003757e-15 4.7679724371821361 -1.0658141036401503e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.693096573510088 4.0845955947465722 -31.031074935521517 1;
	setAttr ".liw" yes;
createNode joint -n "footOutFrontLFT_tmpJnt" -p "ankleFrontLFT_tmpJnt";
	rename -uid "A6D42C06-4921-181D-2707-D985D7D91F7B";
	setAttr ".t" -type "double3" 1.6768657878047792 2.3622536610478777 1.7116380496859924 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.895005531235867 -76.399936074542765 -91.653356255880837 ;
createNode joint -n "heelRollFrontLFT_tmpJnt" -p "ankleFrontLFT_tmpJnt";
	rename -uid "D769E08E-499B-F5CD-F804-F385351B1D4D";
	setAttr ".t" -type "double3" 0.177998817917845 2.6735065935722013 0.63452963098316451 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -166.40056636537886 0.13218532255915544 -2.199751475440006 ;
createNode joint -n "ballRollFrontLFT_tmpJnt" -p "ankleFrontLFT_tmpJnt";
	rename -uid "DF880BF3-417B-E567-59B7-40BADB1A9C9D";
	setAttr ".t" -type "double3" 0.050544651639459003 2.1516928850358927 2.8475373121868697 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 103.59998462912831 0.046886085856577574 -1.8471595730633852 ;
createNode joint -n "toeRollFrontLFT_tmpJnt" -p "ballRollFrontLFT_tmpJnt";
	rename -uid "A3ED1429-48DD-D0A3-B2BB-5AB4E2BCA55F";
	setAttr ".t" -type "double3" -0.045086083585204016 2.1691892776866259 0.0048699503985036004 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "footInFrontLFT_tmpJnt" -p "ankleFrontLFT_tmpJnt";
	rename -uid "A297404F-4132-D625-AA79-99882ED5B3FA";
	setAttr ".t" -type "double3" -1.6837153224325452 2.4690207239904485 1.7054254910809208 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.56215670926540406 76.399936074558497 88.346643744118879 ;
createNode joint -n "legPovFrontLFT_tmpJnt" -p "midLegFrontLFT_tmpJnt";
	rename -uid "C7560217-445A-D8C8-39C3-C5AA2C5DAF75";
	setAttr ".t" -type "double3" -0.013206782857923649 -0.40975503107511457 -12.743434991720546 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.8426214482650205 6.8135929625321164e-13 178.153943212798 ;
	setAttr ".radi" 2;
createNode joint -n "upLegFrontRGT_tmpJnt" -p "chest_tmpJnt";
	rename -uid "10B651E2-4B1E-0849-BE73-6BAE81E237B6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.51084 -9.2536445502890139 2.4531575491334898 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 162.57162991238013 -0.31008886875791664 179.01232214598107 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.038135510126723025 -0.92276387562020457 0.38347426604369977 0 -0.010187723475372425 0.38337444395253667 0.92353681356753325 0
		 8.8692702724309012 33.74871606997359 -23.928017947855178 1;
	setAttr ".liw" yes;
createNode joint -n "midLegFrontRGT_tmpJnt" -p "upLegFrontRGT_tmpJnt";
	rename -uid "024BAA9D-4FD2-8CAF-0368-9F96E2FE4EC6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.5928414364767605e-06 -6.991416255805369 0.30868425681066824 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 19.264398249803619 -0.60925348817788882 0.7074493064885532 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.026827197462727256 -0.77013788114561099 -0.6373130671034799 0 0.028955281358189037 -0.63667635298484737 0.77058731707145456 0
		 9.2884817537506876 23.605067562583631 -19.712607842240914 1;
	setAttr ".liw" yes;
createNode joint -n "lowLegFrontRGT_tmpJnt" -p "midLegFrontRGT_tmpJnt";
	rename -uid "780109E6-46F1-F82C-3528-0885D36550D1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.9850382636809059e-06 -15.88377381649704 -3.3972045340391333e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -15.398987144887931 0.49366597044904248 -0.054296513067877528 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.6930965747606965 11.989646232807946 -29.324730521287474 1;
	setAttr ".liw" yes;
createNode joint -n "ankleFrontRGT_tmpJnt" -p "lowLegFrontRGT_tmpJnt";
	rename -uid "078982F7-4516-016F-8257-48AC7AD87D71";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.6446415891380184e-06 -4.767975521819956 4.2697112677458904e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.693096573510088 4.0845955947465722 -31.031074935521517 1;
	setAttr ".liw" yes;
createNode joint -n "footOutFrontRGT_tmpJnt" -p "ankleFrontRGT_tmpJnt";
	rename -uid "13B9A3D0-4C41-13C3-BE94-87BE65663835";
	setAttr ".t" -type "double3" -1.6768631848471873 -2.3622580630821619 -1.7116306105619667 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -89.895005531236947 -76.399936074542921 -91.653356255879942 ;
createNode joint -n "heelRollFrontRGT_tmpJnt" -p "ankleFrontRGT_tmpJnt";
	rename -uid "892884DC-41F8-9CC6-8778-33974FA6E028";
	setAttr ".t" -type "double3" -0.17799887046921903 -2.673504843317581 -0.63454733938197272 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -166.40056636537909 0.13218532255941487 -2.1997514754401042 ;
createNode joint -n "ballRollFrontRGT_tmpJnt" -p "ankleFrontRGT_tmpJnt";
	rename -uid "319F62AE-47BC-E65F-3552-D4A07F97C730";
	setAttr ".t" -type "double3" -0.050538506282474138 -2.151684382288388 -2.8475837686573815 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 103.59998462912823 0.046886085856609354 -1.8471595730634658 ;
createNode joint -n "toeRollFrontRGT_tmpJnt" -p "ballRollFrontRGT_tmpJnt";
	rename -uid "5AD50B5D-4C2D-D778-00F7-999E6DD1D879";
	setAttr ".t" -type "double3" 0.045086287148115467 -2.1691662862139651 -0.0048699597831265637 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "footInFrontRGT_tmpJnt" -p "ankleFrontRGT_tmpJnt";
	rename -uid "FB6470DD-4104-8454-9A27-C4BF1A1A0C2C";
	setAttr ".t" -type "double3" 1.6837220344050516 -2.4690240377743957 -1.7054231285077766 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.56215670926650885 76.399936074558653 88.346643744120001 ;
createNode joint -n "legPovFrontRGT_tmpJnt" -p "midLegFrontRGT_tmpJnt";
	rename -uid "955B12E6-490E-279B-9A33-7F8840D0E251";
	setAttr ".t" -type "double3" 0.013206764416510808 0.40975445891018225 12.743417197317086 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.8426214482641836 3.6539106711657043e-14 178.15394321279808 ;
	setAttr ".radi" 2;
createNode joint -n "neck01_tmpJnt" -p "upperBody_tmpJnt";
	rename -uid "2C356822-4FBF-CDAD-CF79-C8AB2222C501";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -0.20006343852002573 6.033261179627404 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 138.93366584309084 0 180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99380179609056485 0.11116649714355208 0
		 0 -0.11116649714355208 0.99380179609056485 0 0 53.3383703156046 24.007539349346846 1;
	setAttr ".liw" yes;
createNode joint -n "neck02_tmpJnt" -p "neck01_tmpJnt";
	rename -uid "B1563170-4DBC-80A4-20DF-79B22D306AEB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.3665827156630354e-30 7.2947118848452632 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -13.978153191333972 2.9025768952439802e-15 2.3676908623536401e-14 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.9824903688262423 0.18631337891754973 0
		 0 -0.18631337891754973 0.9824903688262423 0 0 68.364009309514302 25.688304730197807 1;
	setAttr ".liw" yes;
createNode joint -n "head01_tmpJnt" -p "neck02_tmpJnt";
	rename -uid "6BB3FD63-4C93-F6CD-3B47-F29AF58824DC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.8886090522101181e-31 5.9392333699496973 -1.7763568394002505e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -42.223380831249514 1.1455949482719527e-15 2.9670760516497164e-15 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 -5.5511151231257827e-17 0 0 5.5511151231257827e-17 1 0
		 0 80.582207878467017 28.00528811435731 1;
	setAttr ".liw" yes;
createNode joint -n "nose_tmpJnt" -p "head01_tmpJnt";
	rename -uid "4579F4F5-4B4A-EEBD-B64C-909FB620127F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.16945561786269178 13.480374579909277 0.69654524415382679 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 -0.24874196627389961 0.96856978799371729 0
		 0 -0.96856978799371729 -0.24874196627389961 0 -2.8421709430404004e-14 89.563646731661549 49.571309378320677 1;
	setAttr ".liw" yes;
createNode joint -n "ear01LFT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "A112DF02-4D5F-F0B6-20B7-B78231BCB563";
	setAttr ".t" -type "double3" -3.6627625226974474 0.76203455705579515 3.3011893334259028 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 71.147229944414278 -7.7221068377576598 80.513330617177218 ;
createNode joint -n "ear02LFT_tmpJnt" -p "ear01LFT_tmpJnt";
	rename -uid "1E0148B2-4794-0201-7144-84A51CAA4544";
	setAttr ".t" -type "double3" 0 2.5565818146421719 2.3092638912203256e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.9319374011584749 1.4952361601611506 -4.9319171624858162 ;
createNode joint -n "ear03LFT_tmpJnt" -p "ear02LFT_tmpJnt";
	rename -uid "6FC6CDD8-4B14-9559-DE71-BA9CCBC89D71";
	setAttr ".t" -type "double3" -3.5527136788005009e-15 3.7658064900335972 -2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "ear01RGT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "7C929D15-432A-28CC-8A52-A490857CEA28";
	setAttr ".t" -type "double3" 3.6627600000000013 0.76204208737096124 3.3011483675797706 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -108.85277005558575 7.7221068377576501 -80.513330617177203 ;
createNode joint -n "ear02RGT_tmpJnt" -p "ear01RGT_tmpJnt";
	rename -uid "0D04ADAB-45B1-9B05-1CBC-AD9D33866FEA";
	setAttr ".t" -type "double3" -4.2743059900374192e-06 -2.5566170182325152 -1.2870423958588617e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.9319374011584691 1.4952361601611612 -4.9319171624857523 ;
createNode joint -n "ear03RGT_tmpJnt" -p "ear02RGT_tmpJnt";
	rename -uid "508FA1DF-4479-E799-B6BE-498FA4E9CEC3";
	setAttr ".t" -type "double3" 1.0112154615882218e-05 -3.7658136449224671 3.6705371249112773e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "eyeLFT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "6BEA0C09-4C6E-8CEA-0412-F2AFE9593C8C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.0642565488815299 7.0751272728810051 2.5387948892623982 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 82.732131820507377 -6.9603338649154421e-15 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "jaw01Lwr_tmpJnt" -p "head01_tmpJnt";
	rename -uid "A435FCB9-423D-4E99-FC47-688D92F154F9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -6.3153605333213656e-17 0.73595664306286679 0.95262693456805181 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000007 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 82.732131820507377 -6.9603338649154421e-15 -180 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -5.6817911712458105e-17 -0.46395345786243802 0.8858595763085072 0 1.0848650946202438e-16 0.8858595763085072 0.46395345786243802 0
		 -2.281527907856237e-09 138.24609308456581 1.2332340767044465 1;
createNode joint -n "jaw02Lwr_tmpJnt" -p "jaw01Lwr_tmpJnt";
	rename -uid "0000FEA2-40B1-E5A3-82D6-0FB884932798";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.10674670847709687 -2.054940770223169 0.85797032006855112 ;
	setAttr ".r" -type "double3" 17.811815764611801 0 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661394e-09 134.88585971678842 7.6491683844072185 1;
createNode joint -n "jaw03Lwr_tmpJnt" -p "jaw02Lwr_tmpJnt";
	rename -uid "CDD00359-4702-2A06-26F6-83B6646EF291";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.2969585611357585e-15 0.069343837048732648 12.197282466947506 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 6.1629758220391547e-33 0
		 -1.3928325357808493e-30 -1.1435297153639112e-14 1.0000000000000002 0 1.2246467991473532e-16 1 1.1379786002407855e-14 0
		 -2.2815283193661419e-09 134.88585971678845 9.7309712720145338 1;
createNode joint -n "eye_tmpJnt" -p "head01_tmpJnt";
	rename -uid "8B700230-4171-978B-0042-ED80057D07A0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.9882211822581064e-16 19.633923899514524 4.1406283814256213 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 82.732131820507377 -6.9603338649154421e-15 -180 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetRGT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "D8C78D95-4886-D917-2D35-52BFF8013F88";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.0654054180920047 -0.00010040181384598861 3.5233875692510861e-15 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.99999914622637 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "eyeTargetLFT_tmpJnt" -p "eye_tmpJnt";
	rename -uid "EEDA2799-404D-C802-E215-14B8480607B4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.0636983050613118 2.8447350408247754e-14 2.9118728190098176e-17 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "jaw01Upr_tmpJnt" -p "head01_tmpJnt";
	rename -uid "448D4422-421D-AF61-CC38-B3BDE1B3DDA8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -2.3474816374188701e-16 2.5105443812836197 -0.4777718631384682 ;
	setAttr ".r" -type "double3" -11.217140439825878 0 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -82.732131820507377 1.4124500153760508e-30 1.7655625192200634e-31 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 0 0 -2.4651903288156624e-32 -2.2204460492503136e-16 1.0000000000000002 0
		 1.2246467991473532e-16 1 2.2204460492503131e-16 0 -2.2815279078562374e-09 137.53090779923286 7.8685026751330751 1;
createNode joint -n "jaw02Upr_tmpJnt" -p "jaw01Upr_tmpJnt";
	rename -uid "CA71604B-4C3C-F4EE-2EC3-238A70A913ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.047183821054730402 -0.92808445207336698 12.375796853492099 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" -1 1.2246467991473532e-16 0 0 -2.4651903288156624e-32 -2.2204460492503136e-16 1.0000000000000002 0
		 1.2246467991473532e-16 1 2.2204460492503131e-16 0 -2.2815279078562374e-09 137.53090779923286 10.215768076274593 1;
createNode joint -n "eyeRGT_tmpJnt" -p "head01_tmpJnt";
	rename -uid "B812437C-4F84-B5AF-D24C-299BCEB07616";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.0642600000000009 7.0751102421626619 2.5387788423790028 ;
	setAttr ".s" -type "double3" 1 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 82.732131820507377 180.00000000000003 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 2.7979812622070313 142.32405853271484 7.1008777618408212 1;
createNode joint -n "lowerBody_tmpJnt" -p "body_tmpJnt";
	rename -uid "08D9E9B8-4BC5-CEF3-0250-8FAE4B3B7553";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0.64561641986981755 -9.232497993596656 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.813453674316399 -9.8591880759686319 1;
	setAttr ".liw" yes;
createNode joint -n "hip_tmpJnt" -p "lowerBody_tmpJnt";
	rename -uid "0A0DA47A-4826-9EDC-AFB7-83A335F926AF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -1.4847134886481825 -11.011724039572917 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.77246298924252 -21.633442272285713 1;
	setAttr ".liw" yes;
createNode joint -n "upLegBackLFT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "1E315EE3-4262-76FD-D02D-B4ACBDB35CB8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.1809427761387505 -0.8002282181522844 1.6319205531498397 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -1.307584688249412 0.13810672678800576 -173.97183410509271 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.038135510126723025 -0.92276387562020457 0.38347426604369977 0 -0.010187723475372425 0.38337444395253667 0.92353681356753325 0
		 8.8692702724309012 33.74871606997359 -23.928017947855178 1;
	setAttr ".liw" yes;
createNode joint -n "midLegBackLFT_tmpJnt" -p "upLegBackLFT_tmpJnt";
	rename -uid "F607F418-46AF-E4EC-7983-A7B9AD1954F2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 3.5527136788005009e-15 18.850734045955271 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -39.376618547422353 -1.2999199400978965 -7.6130686291791854 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.026827197462727256 -0.77013788114561099 -0.6373130671034799 0 0.028955281358189037 -0.63667635298484737 0.77058731707145456 0
		 9.2884817537506876 23.605067562583631 -19.712607842240914 1;
	setAttr ".liw" yes;
createNode joint -n "lowLegBackLFT_tmpJnt" -p "midLegBackLFT_tmpJnt";
	rename -uid "31D4574D-4A99-D3A7-8497-5BABA4C3189A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 8.8817841970012523e-16 13.076992636102144 -1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 33.352612713057539 0.015295480271502321 2.0252450437798233 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.6930965747606965 11.989646232807946 -29.324730521287474 1;
	setAttr ".liw" yes;
createNode joint -n "ankleBackLFT_tmpJnt" -p "lowLegBackLFT_tmpJnt";
	rename -uid "AA262AEA-4405-A939-8657-0196C9F22C23";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.9936057773011271e-15 9.2862242564926696 2.1316282072803006e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.693096573510088 4.0845955947465722 -31.031074935521517 1;
	setAttr ".liw" yes;
createNode joint -n "heelRollBackLFT_tmpJnt" -p "ankleBackLFT_tmpJnt";
	rename -uid "BA3B4EDF-4496-EDBF-A296-AE83661ABD34";
	setAttr ".t" -type "double3" -0.1031651093541468 2.7264616899373193 -0.06799608377291122 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -172.60772726934638 0.094512923414069999 -0.32572013907101199 ;
createNode joint -n "footOutBackLFT_tmpJnt" -p "heelRollBackLFT_tmpJnt";
	rename -uid "568ACE68-4428-8E79-C85B-A5B4451525AC";
	setAttr ".t" -type "double3" 1.3987144204173028 -0.12035756562737293 -1.0525940168890955 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.66715117803399238 89.999999999984311 0 ;
createNode joint -n "ballRollBackLFT_tmpJnt" -p "heelRollBackLFT_tmpJnt";
	rename -uid "EA4EEA60-4F61-0A87-7BB3-D68C71735D2F";
	setAttr ".t" -type "double3" -0.48692165798102399 -0.35425424661813026 -2.086357988051581 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000156 3.9937082123298732e-14 -0.3627625709024091 ;
createNode joint -n "toeRollBackLFT_tmpJnt" -p "ballRollBackLFT_tmpJnt";
	rename -uid "BAAFEC4C-4CD6-397B-1FB1-C8956ECC4446";
	setAttr ".t" -type "double3" -0.01980394643007681 2.7378249303265432 0.020646226180422327 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "footInBackLFT_tmpJnt" -p "heelRollBackLFT_tmpJnt";
	rename -uid "98044122-4ED1-C2FF-11BD-60A6153171DA";
	setAttr ".t" -type "double3" -1.7252825484694974 -0.10685900868241271 -0.89462724588433673 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.999999999982748 -89.999999999999943 0 ;
createNode joint -n "legPovBackLFT_tmpJnt" -p "midLegBackLFT_tmpJnt";
	rename -uid "AC93AE6A-4DAB-0A80-AC9A-10824C85B950";
	setAttr ".t" -type "double3" 0.24875829171426389 -6.9547671274777025 8.0881379085183092 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -40.709438225003538 -6.5579061838425907e-13 -177.95151634559937 ;
	setAttr ".radi" 2;
createNode joint -n "tail01_tmpJnt" -p "hip_tmpJnt";
	rename -uid "F991081E-4689-BE67-9839-7B81E1B94AA2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.3629055523893127e-31 -0.42681142073712408 -2.3186230787228546 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 7.3629055523893127e-31 41.77246298924252 -29.825826904428801 1;
	setAttr ".liw" yes;
createNode joint -n "tail02_tmpJnt" -p "tail01_tmpJnt";
	rename -uid "B28FDD32-40FA-2B33-6C45-929C7950B492";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.1401505270772419e-31 9.109358768595385 -0.14251290769978794 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 8.5030560794665545e-31 41.77246298924252 -45.048396535102768 1;
	setAttr ".liw" yes;
createNode joint -n "tail03_tmpJnt" -p "tail02_tmpJnt";
	rename -uid "9EAF81B0-4215-B80E-BE2C-9D9E23E44305";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.8548270309372049e-31 9.2904556162580505 0.25453623841667761 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 1.4357883110403759e-30 41.772462989242506 -58.424306784823457 1;
	setAttr ".liw" yes;
createNode joint -n "tail04_tmpJnt" -p "tail03_tmpJnt";
	rename -uid "45CAEB32-4EB2-567F-FBE3-73A2A92A25D8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -3.5032461608120427e-46 7.100057059925085 0.12160698672242884 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 1.4357883110403757e-30 41.77246298924252 -71.02250822112677 1;
	setAttr ".liw" yes;
createNode joint -n "upLegBackRGT_tmpJnt" -p "hip_tmpJnt";
	rename -uid "A970B79F-431D-10ED-A325-E2AE262D629E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.18094 -0.80023667368602247 1.6319044523515345 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 178.69241531175118 -0.13810672678800576 173.97183410509268 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.038135510126723025 -0.92276387562020457 0.38347426604369977 0 -0.010187723475372425 0.38337444395253667 0.92353681356753325 0
		 8.8692702724309012 33.74871606997359 -23.928017947855178 1;
	setAttr ".liw" yes;
createNode joint -n "midLegBackRGT_tmpJnt" -p "upLegBackRGT_tmpJnt";
	rename -uid "B92928C1-4D15-A184-858C-4597FC1492FA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 8.9327615171441721e-07 -18.850728567293142 3.3721998285329846e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -39.376618547422915 -1.2999199400979318 -7.6130686291791632 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.026827197462727256 -0.77013788114561099 -0.6373130671034799 0 0.028955281358189037 -0.63667635298484737 0.77058731707145456 0
		 9.2884817537506876 23.605067562583631 -19.712607842240914 1;
	setAttr ".liw" yes;
createNode joint -n "lowLegBackRGT_tmpJnt" -p "midLegBackRGT_tmpJnt";
	rename -uid "2B47CA4D-4971-A265-D949-56901FB7390F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.6837685183901385e-06 -13.076965170450142 -6.6566689994829176e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 33.352612713057567 0.015295480271538788 2.025245043779702 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.6930965747606965 11.989646232807946 -29.324730521287474 1;
	setAttr ".liw" yes;
createNode joint -n "ankleBackRGT_tmpJnt" -p "lowLegBackRGT_tmpJnt";
	rename -uid "0838F031-49A6-44E2-E490-C8863E10F31D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -9.8699586548178786e-07 -9.2861980493763312 1.8928393995309989e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.2074182697257331e-06 1.7198233630857089e-21 -1.471083031009957e-23 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.693096573510088 4.0845955947465722 -31.031074935521517 1;
	setAttr ".liw" yes;
createNode joint -n "heelRollBackRGT_tmpJnt" -p "ankleBackRGT_tmpJnt";
	rename -uid "DCD060EB-4A7A-1625-A533-03984F52FC8E";
	setAttr ".t" -type "double3" 0.10317387924901755 -2.7264707251489551 0.068033892601071955 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -172.60772726934621 0.094512923414241515 -0.32572013907132236 ;
createNode joint -n "footOutBackRGT_tmpJnt" -p "heelRollBackRGT_tmpJnt";
	rename -uid "FF208855-405A-351E-362B-EE8F46E57AEB";
	setAttr ".t" -type "double3" -1.3987202921583286 0.12035693393450209 1.0526089606109146 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.66715117803106028 89.999999999984468 0 ;
createNode joint -n "ballRollBackRGT_tmpJnt" -p "heelRollBackRGT_tmpJnt";
	rename -uid "F03A5610-4C9D-7004-1DCF-96A36D54FA7D";
	setAttr ".t" -type "double3" 0.48691940182918181 0.35425383139167071 2.0863692372299418 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90.000000000000355 9.3572912651994639e-13 -0.36276257090281966 ;
createNode joint -n "toeRollBackRGT_tmpJnt" -p "ballRollBackRGT_tmpJnt";
	rename -uid "D3A165DD-4B28-9883-330C-54B2E5B46277";
	setAttr ".t" -type "double3" 0.019805106350196944 -2.7378977676567899 -0.020646157812706192 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "footInBackRGT_tmpJnt" -p "heelRollBackRGT_tmpJnt";
	rename -uid "BC5A268C-4538-98CE-D6B2-09918BADF4D5";
	setAttr ".t" -type "double3" 1.7252749965133507 0.1068582341981042 0.89467475644164196 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 89.99999999998235 -89.999999999999787 0 ;
createNode joint -n "legPovBackRGT_tmpJnt" -p "midLegBackRGT_tmpJnt";
	rename -uid "3AE54692-4828-86C9-011D-BDB5C0ACA3F9";
	setAttr ".t" -type "double3" -0.24875950688245663 6.9548011010662982 -8.0881774185500248 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -40.709438225003559 -4.1049033857638516e-14 -177.95151634559946 ;
	setAttr ".radi" 2;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "3DD3D2F5-463F-41DD-9213-A1BB49798348";
	setAttr -s 3 ".lnk";
	setAttr -s 3 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "1402BF98-4ECA-DA53-B5E0-7A8D734448D0";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 0 ;
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "974285E3-4BC2-8AAC-C458-04AFEE197C83";
createNode displayLayerManager -n "layerManager";
	rename -uid "44E5CFB9-47E1-666E-24A6-48B18ED6F5F2";
createNode displayLayer -n "defaultLayer";
	rename -uid "C92AB413-4548-94A9-53B1-95B25CFE2336";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "4C9F9B25-44EE-4697-56CC-D0BE39814383";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "784969E9-49FB-3DAF-B005-DEB29DB35970";
	setAttr ".g" yes;
createNode aiOptions -s -n "defaultArnoldRenderOptions";
	rename -uid "E3166578-4291-3965-1911-53B229A66039";
	setAttr ".version" -type "string" "3.0.1";
createNode aiAOVFilter -s -n "defaultArnoldFilter";
	rename -uid "7201C8D0-41B9-5784-DF7D-3E9C6B3CE918";
	setAttr ".ai_translator" -type "string" "gaussian";
createNode aiAOVDriver -s -n "defaultArnoldDriver";
	rename -uid "CF08C53F-4FD7-4506-29D0-AE91E1E73591";
	setAttr ".ai_translator" -type "string" "exr";
createNode aiAOVDriver -s -n "defaultArnoldDisplayDriver";
	rename -uid "10B8DF56-488D-128E-5D45-93BB4C25B8DA";
	setAttr ".output_mode" 0;
	setAttr ".ai_translator" -type "string" "maya";
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "DA1DF14E-4012-8B1F-6C34-24B5BA691C17";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 1 -ast 0 -aet 1 ";
	setAttr ".st" 6;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
	rename -uid "D9F89D14-46AB-576A-598D-A2B55BB62951";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
	rename -uid "1F6DD84D-413E-9B97-887A-46929A8FD725";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
	rename -uid "FE73F180-4978-41E0-7F31-8F849FC6A397";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
	rename -uid "858907B7-4AAF-1CFC-7EFB-AD80B3AAE671";
lockNode -l 1 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "34468406-41CE-0A52-0079-3A9164D94E94";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -873.80948908745438 -302.38094036541332 ;
	setAttr ".tgi[0].vh" -type "double2" 832.14282407647238 315.4761779402935 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "7AA8F52E-4265-6F86-FFCF-3AA19F7812FF";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n"
		+ "            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n"
		+ "            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n"
		+ "            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n"
		+ "            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n"
		+ "            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n"
		+ "            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n"
		+ "            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n"
		+ "            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1135\n            -height 718\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n"
		+ "            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n"
		+ "            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n"
		+ "            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n"
		+ "                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n"
		+ "                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -autoFitTime 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n"
		+ "                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n"
		+ "                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n"
		+ "                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n"
		+ "                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n"
		+ "                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n"
		+ "\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n"
		+ "                -editorMode \"default\" \n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n"
		+ "                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n"
		+ "                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n"
		+ "                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n"
		+ "                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n"
		+ "            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n"
		+ "            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n"
		+ "\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 0\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1135\\n    -height 718\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 0\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1135\\n    -height 718\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
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
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -cb on ".macc";
	setAttr -cb on ".macd";
	setAttr -cb on ".macq";
	setAttr -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -cb on ".ren";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -cb on ".an";
	setAttr -cb on ".ar";
	setAttr -k on ".fs" 1;
	setAttr -k on ".ef" 10;
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -cb on ".pff";
	setAttr -cb on ".peie";
	setAttr -cb on ".ifp";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -cb on ".sosl";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".afp";
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
	setAttr -k on ".bls";
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
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -cb on ".ope";
	setAttr -cb on ".oppf";
	setAttr -cb on ".hbl";
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
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "root.s" "body_tmpJnt.is";
connectAttr "body_tmpJnt.s" "upperBody_tmpJnt.is";
connectAttr "upperBody_tmpJnt.s" "chest_tmpJnt.is";
connectAttr "chest_tmpJnt.s" "upLegFrontLFT_tmpJnt.is";
connectAttr "upLegFrontLFT_tmpJnt.s" "midLegFrontLFT_tmpJnt.is";
connectAttr "midLegFrontLFT_tmpJnt.s" "lowLegFrontLFT_tmpJnt.is";
connectAttr "lowLegFrontLFT_tmpJnt.s" "ankleFrontLFT_tmpJnt.is";
connectAttr "ankleFrontLFT_tmpJnt.s" "footOutFrontLFT_tmpJnt.is";
connectAttr "ankleFrontLFT_tmpJnt.s" "heelRollFrontLFT_tmpJnt.is";
connectAttr "ankleFrontLFT_tmpJnt.s" "ballRollFrontLFT_tmpJnt.is";
connectAttr "ballRollFrontLFT_tmpJnt.s" "toeRollFrontLFT_tmpJnt.is";
connectAttr "ankleFrontLFT_tmpJnt.s" "footInFrontLFT_tmpJnt.is";
connectAttr "midLegFrontLFT_tmpJnt.s" "legPovFrontLFT_tmpJnt.is";
connectAttr "chest_tmpJnt.s" "upLegFrontRGT_tmpJnt.is";
connectAttr "upLegFrontRGT_tmpJnt.s" "midLegFrontRGT_tmpJnt.is";
connectAttr "midLegFrontRGT_tmpJnt.s" "lowLegFrontRGT_tmpJnt.is";
connectAttr "lowLegFrontRGT_tmpJnt.s" "ankleFrontRGT_tmpJnt.is";
connectAttr "ankleFrontRGT_tmpJnt.s" "footOutFrontRGT_tmpJnt.is";
connectAttr "ankleFrontRGT_tmpJnt.s" "heelRollFrontRGT_tmpJnt.is";
connectAttr "ankleFrontRGT_tmpJnt.s" "ballRollFrontRGT_tmpJnt.is";
connectAttr "ballRollFrontRGT_tmpJnt.s" "toeRollFrontRGT_tmpJnt.is";
connectAttr "ankleFrontRGT_tmpJnt.s" "footInFrontRGT_tmpJnt.is";
connectAttr "midLegFrontRGT_tmpJnt.s" "legPovFrontRGT_tmpJnt.is";
connectAttr "upperBody_tmpJnt.s" "neck01_tmpJnt.is";
connectAttr "neck01_tmpJnt.s" "neck02_tmpJnt.is";
connectAttr "neck02_tmpJnt.s" "head01_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "nose_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "ear01LFT_tmpJnt.is";
connectAttr "ear01LFT_tmpJnt.s" "ear02LFT_tmpJnt.is";
connectAttr "ear02LFT_tmpJnt.s" "ear03LFT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "ear01RGT_tmpJnt.is";
connectAttr "ear01RGT_tmpJnt.s" "ear02RGT_tmpJnt.is";
connectAttr "ear02RGT_tmpJnt.s" "ear03RGT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eyeLFT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "jaw01Lwr_tmpJnt.is";
connectAttr "jaw01Lwr_tmpJnt.s" "jaw02Lwr_tmpJnt.is";
connectAttr "jaw02Lwr_tmpJnt.s" "jaw03Lwr_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eye_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTargetRGT_tmpJnt.is";
connectAttr "eye_tmpJnt.s" "eyeTargetLFT_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "jaw01Upr_tmpJnt.is";
connectAttr "jaw01Upr_tmpJnt.s" "jaw02Upr_tmpJnt.is";
connectAttr "head01_tmpJnt.s" "eyeRGT_tmpJnt.is";
connectAttr "body_tmpJnt.s" "lowerBody_tmpJnt.is";
connectAttr "lowerBody_tmpJnt.s" "hip_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "upLegBackLFT_tmpJnt.is";
connectAttr "upLegBackLFT_tmpJnt.s" "midLegBackLFT_tmpJnt.is";
connectAttr "midLegBackLFT_tmpJnt.s" "lowLegBackLFT_tmpJnt.is";
connectAttr "lowLegBackLFT_tmpJnt.s" "ankleBackLFT_tmpJnt.is";
connectAttr "ankleBackLFT_tmpJnt.s" "heelRollBackLFT_tmpJnt.is";
connectAttr "heelRollBackLFT_tmpJnt.s" "footOutBackLFT_tmpJnt.is";
connectAttr "heelRollBackLFT_tmpJnt.s" "ballRollBackLFT_tmpJnt.is";
connectAttr "ballRollBackLFT_tmpJnt.s" "toeRollBackLFT_tmpJnt.is";
connectAttr "heelRollBackLFT_tmpJnt.s" "footInBackLFT_tmpJnt.is";
connectAttr "midLegBackLFT_tmpJnt.s" "legPovBackLFT_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "tail01_tmpJnt.is";
connectAttr "tail01_tmpJnt.s" "tail02_tmpJnt.is";
connectAttr "tail02_tmpJnt.s" "tail03_tmpJnt.is";
connectAttr "tail03_tmpJnt.s" "tail04_tmpJnt.is";
connectAttr "hip_tmpJnt.s" "upLegBackRGT_tmpJnt.is";
connectAttr "upLegBackRGT_tmpJnt.s" "midLegBackRGT_tmpJnt.is";
connectAttr "midLegBackRGT_tmpJnt.s" "lowLegBackRGT_tmpJnt.is";
connectAttr "lowLegBackRGT_tmpJnt.s" "ankleBackRGT_tmpJnt.is";
connectAttr "ankleBackRGT_tmpJnt.s" "heelRollBackRGT_tmpJnt.is";
connectAttr "heelRollBackRGT_tmpJnt.s" "footOutBackRGT_tmpJnt.is";
connectAttr "heelRollBackRGT_tmpJnt.s" "ballRollBackRGT_tmpJnt.is";
connectAttr "ballRollBackRGT_tmpJnt.s" "toeRollBackRGT_tmpJnt.is";
connectAttr "heelRollBackRGT_tmpJnt.s" "footInBackRGT_tmpJnt.is";
connectAttr "midLegBackRGT_tmpJnt.s" "legPovBackRGT_tmpJnt.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of templateJoint_quaruped.ma
