//Maya ASCII 2018 scene
//Name: quadruped_tempJoint.ma
//Last modified: Mon, Dec 03, 2018 06:24:33 PM
//Codeset: 1252
requires maya "2018";
requires -nodeType "aiOptions" -nodeType "aiAOVDriver" -nodeType "aiAOVFilter" "mtoa" "2.0.1";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "12614C91-4DDD-7B04-8FF9-7BB390992D58";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 216.66158321973805 150.88065688651255 60.662243785148199 ;
	setAttr ".r" -type "double3" -32.738352728581361 -644.99999999990041 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "4D3590A5-4487-A7DF-749E-CB908BD6EC19";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 256.25934873284405;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 12.891678421187011 2.1001814432651349 26.920710506171243 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "6EF98230-43B3-0DA7-DAF8-F88937D1C278";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "BB494DB0-4ECF-13D6-CD69-15BD65D75720";
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
	rename -uid "69E98580-415B-08F1-5F24-C6BD6C289865";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "149AF8FF-4DEB-6804-5A38-71AFCF0F4262";
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
	rename -uid "6A450A35-486C-1D58-92D3-CC8C7C8E546A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1001.1835112895279 43.857076815290654 -8.7832415848388177 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "65B5E28A-48B9-9AEE-5508-9793FC95CA87";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1001.1835112895279;
	setAttr ".ow" 46.470712778163858;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 43.345159538664618 -9.9208355328969056 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode joint -n "Root";
	rename -uid "283E61F4-4DA1-1AC8-A356-B58CE9119A3D";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode joint -n "body_bind_jnt" -p "Root";
	rename -uid "5AE07A57-4CE1-064D-B604-07B815D843AE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 41.813455445823308 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.813455445823308 0 1;
	setAttr ".liw" yes;
createNode joint -n "upperBody_bind_jnt" -p "body_bind_jnt";
	rename -uid "DEA444A8-4BD6-350A-FEF0-34AEC2DB40D6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -1.7715069091650548e-06 9.8227388198240426 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.813453674316399 9.8227388198240426 1;
	setAttr ".liw" yes;
createNode joint -n "chest_bind_jnt" -p "upperBody_bind_jnt";
	rename -uid "160723E3-43EB-E2BB-471A-93AFA4133BDC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 0.73116875882459453 12.246321044371655 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 42.544622433140994 22.069059864195697 1;
	setAttr ".liw" yes;
createNode joint -n "neck01_bind_jnt" -p "chest_bind_jnt";
	rename -uid "1F6C51D8-445F-BE45-907A-7389A602B119";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 10.793747882463606 1.9384794851511487 ;
	setAttr ".r" -type "double3" 2.3854160110976376e-15 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 6.3825633763616061 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99380179609056485 0.11116649714355208 0
		 0 -0.11116649714355208 0.99380179609056485 0 0 53.3383703156046 24.007539349346846 1;
	setAttr ".liw" yes;
createNode joint -n "neck02_bind_jnt" -p "neck01_bind_jnt";
	rename -uid "E94F8A9A-472C-60B2-1FAB-EDA51FC4F9EF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 15.119351819465237 2.1316282072803006e-14 ;
	setAttr ".r" -type "double3" -1.5902773407317584e-15 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 4.3551515080678715 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.9824903688262423 0.18631337891754973 0
		 0 -0.18631337891754973 0.9824903688262423 0 0 68.364009309514302 25.688304730197807 1;
	setAttr ".liw" yes;
createNode joint -n "head_bind_jnt" -p "neck02_bind_jnt";
	rename -uid "536C8446-4D15-7F17-01F3-F89B186B1456";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 12.435947421601199 -7.1054273576010019e-15 ;
	setAttr ".r" -type "double3" -1.590277340731758e-15 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -10.737714884429492 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 -5.5511151231257827e-17 0 0 5.5511151231257827e-17 1 0
		 0 80.582207878467017 28.00528811435731 1;
	setAttr ".liw" yes;
createNode joint -n "nose_bind_jnt" -p "head_bind_jnt";
	rename -uid "B27F298C-490F-4A9F-4D90-9FA38F89F154";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.8421709430404004e-14 8.9814388531945326 21.566021263963368 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 104.40308072023916 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 -0.24874196627389961 0.96856978799371729 0
		 0 -0.96856978799371729 -0.24874196627389961 0 -2.8421709430404004e-14 89.563646731661549 49.571309378320677 1;
	setAttr ".liw" yes;
createNode joint -n "upLegFrontLFT_bind_jnt" -p "chest_bind_jnt";
	rename -uid "C042685B-4E2D-945D-E637-19B7786DA39E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 10.690866208086986 -9.0885708221889203 1.9015630311164706 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -10.465307771379461 -0.51021781174662184 -175.03650177949831 ;
	setAttr ".bps" -type "matrix" -0.99621052038405389 -0.086517642655293214 0.0089048630255607383 0
		 0.083470386094006643 -0.97981741733735572 -0.18163293569083805 0 0.02443959331597961 -0.1802013490285953 0.98332608024338697 0
		 10.690866208086986 33.456051610952073 23.970622895312168 1;
	setAttr ".liw" yes;
createNode joint -n "midLegFrontLFT_bind_jnt" -p "upLegFrontLFT_bind_jnt";
	rename -uid "994EB259-45AF-3A3B-3C33-EABF8EDAC489";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.4210854715202004e-14 10.916000366210934 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 15.133584976465755 0.031992978194132431 -0.17291184468364915 ;
	setAttr ".bps" -type "matrix" -0.99647137845602762 -0.08345964643066632 0.0089038944070986992 0
		 0.083908262810393625 -0.99314226788822857 0.081411541970217605 0 0.0020482553762935958 0.081871381761240397 0.99664079863229493 0
		 11.602028973256919 22.760364324477646 21.987917702795016 1;
createNode joint -n "legPovFrontLFT_tmpJnt" -p "midLegFrontLFT_bind_jnt";
	rename -uid "1898E08B-4F28-0D56-9A4A-13BA5E031370";
	setAttr ".t" -type "double3" -0.15558468628646338 -1.099464861194356 -13.459335521791749 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.696150820999752 -0.11735647048528088 175.18674122271022 ;
	setAttr ".radi" 10;
createNode joint -n "ankleFrontLFT_bind_jnt" -p "midLegFrontLFT_bind_jnt";
	rename -uid "A875058B-4657-C068-AF81-2090A0DF5802";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.2434497875801753e-14 17.17938804626467 7.1054273576010019e-15 ;
	setAttr ".r" -type "double3" -3.8241200427909004e-14 -7.9513867036587919e-16 2.6535163252731228e-31 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -4.6961508209997485 0.11735647048528054 -4.8132587772897919 ;
	setAttr ".bps" -type "matrix" -0.99897995905891301 0.040510331272858392 0.019948795923974451 0
		 -0.0183692133506747 -0.76814722953186476 0.64000969192926926 0 0.041250616959392236 0.6389904121523925 0.76810783082701695 0
		 13.043521580364626 5.6987879192784341 23.386518173746158 1;
createNode joint -n "footOutFrontLFT_tmpJnt" -p "ankleFrontLFT_bind_jnt";
	rename -uid "F5E36AFF-4A18-C726-A9FF-7994C56E924E";
	setAttr ".t" -type "double3" 4.1092611719088161 5.6601182426940078 3.5962153760768558 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -143.04244682004236 -89.939871926385109 -36.65314946256391 ;
createNode joint -n "footInFrontLFT_tmpJnt" -p "ankleFrontLFT_bind_jnt";
	rename -uid "A39C0B7E-49EC-C242-A46F-FB996FDC8BE3";
	setAttr ".t" -type "double3" -4.1138984753920429 5.6354570554472883 3.5979067511696989 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 53.709598010125781 89.939871926394517 143.34685054944148 ;
createNode joint -n "ballRollFrontLFT_bind_jnt" -p "ankleFrontLFT_bind_jnt";
	rename -uid "E190B20D-4C26-9B9C-DACF-29B668C14078";
	setAttr ".t" -type "double3" 0.10331730382704585 4.320428050055872 3.5997210525228809 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.378578676597414 -0.91878021930051135 -0.36912321887903987 ;
createNode joint -n "toeRollFrontLFT_bind_jnt" -p "ballRollFrontLFT_bind_jnt";
	rename -uid "6204E4E2-4D74-B371-9718-F5885E914355";
	setAttr ".t" -type "double3" -0.14444997634862133 5.3186028600637734 -1.3299374061592464 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.34294163526221538 2.9986977707216328e-14 -0.96726620443527633 ;
createNode joint -n "heelRollFrontLFT_tmpJnt" -p "ankleFrontLFT_bind_jnt";
	rename -uid "E274EF15-4AAF-3CF4-D14B-478AC5ACC0F1";
	setAttr ".t" -type "double3" -0.10723947620795826 5.482071842251302 -1.5759374236308048 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.96441149770746 0.048464874312730416 -0.36273240900801501 ;
createNode joint -n "upLegFrontRGT_bind_jnt" -p "chest_bind_jnt";
	rename -uid "345576C2-4B73-2103-63E9-BCBE38C10757";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -10.6909 -9.0885224331409944 1.9015401358043036 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 169.53469222862054 0.51021781174659975 175.03650177949825 ;
	setAttr ".bps" -type "matrix" -0.99621052038405389 -0.086517642655293214 0.0089048630255607383 0
		 0.083470386094006643 -0.97981741733735572 -0.18163293569083805 0 0.02443959331597961 -0.1802013490285953 0.98332608024338697 0
		 10.690866208086986 33.456051610952073 23.970622895312168 1;
	setAttr ".liw" yes;
createNode joint -n "midLegFrontRGT_bind_jnt" -p "upLegFrontRGT_bind_jnt";
	rename -uid "B4045273-4979-E301-BE94-FFA1BD3452FE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -6.367350554548068e-05 -10.916006640979631 -5.8629767707429892e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 15.133584976465642 0.03199297819352942 -0.17291184468248644 ;
	setAttr ".bps" -type "matrix" -0.99647137845602762 -0.08345964643066632 0.0089038944070986992 0
		 0.083908262810393625 -0.99314226788822857 0.081411541970217605 0 0.0020482553762935958 0.081871381761240397 0.99664079863229493 0
		 11.602028973256919 22.760364324477646 21.987917702795016 1;
createNode joint -n "legPovFrontRGT_tmpJnt" -p "midLegFrontRGT_bind_jnt";
	rename -uid "99DE3E6E-47A3-84D9-ADE4-1F8F7CA106D2";
	setAttr ".t" -type "double3" 0.15556491946425588 1.0993894160337128 13.459324459932795 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.6961508209994465 -0.11735647048554364 175.18674122270895 ;
	setAttr ".radi" 10;
createNode joint -n "ankleFrontRGT_bind_jnt" -p "midLegFrontRGT_bind_jnt";
	rename -uid "4C23F629-4AA1-5721-6784-098B1E204C43";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.5671882649145346e-06 -17.179421992665208 3.2046793094764325e-06 ;
	setAttr ".r" -type "double3" -3.8241200427909004e-14 -7.9513867036587919e-16 2.6535163252731228e-31 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -4.6961508209991623 0.11735647048554237 -4.8132587772910762 ;
	setAttr ".bps" -type "matrix" -0.99897995905891301 0.040510331272858392 0.019948795923974451 0
		 -0.0183692133506747 -0.76814722953186476 0.64000969192926926 0 0.041250616959392236 0.6389904121523925 0.76810783082701695 0
		 13.043521580364626 5.6987879192784341 23.386518173746158 1;
createNode joint -n "footOutFrontRGT_tmpJnt" -p "ankleFrontRGT_bind_jnt";
	rename -uid "97A11463-410A-AD93-7046-F9A8AE3AF707";
	setAttr ".t" -type "double3" -4.1092400000000122 -5.6601203000000266 -3.596199999999957 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -143.04244682045373 -89.939871926385408 -36.653149462164272 ;
createNode joint -n "footInFrontRGT_tmpJnt" -p "ankleFrontRGT_bind_jnt";
	rename -uid "A4FEEAD6-47D8-90BF-42C6-8796A297C048";
	setAttr ".t" -type "double3" 4.1138999999999903 -5.6354591000000385 -3.5978999999999566 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 53.709598010497423 89.939871926394829 143.34685054981404 ;
createNode joint -n "ballRollFrontRGT_bind_jnt" -p "ankleFrontRGT_bind_jnt";
	rename -uid "EFDAC2B1-467B-D873-FB88-568AC0913248";
	setAttr ".t" -type "double3" -0.10330000000000794 -4.320430000000032 -3.5996999999999701 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.378578676596931 -0.91878021930043152 -0.36912321887930472 ;
createNode joint -n "toeRollFrontRGT_bind_jnt" -p "ballRollFrontRGT_bind_jnt";
	rename -uid "E91F6989-4C8D-9938-DE89-15A1A11F41C4";
	setAttr ".t" -type "double3" 0.14444115310285888 -5.318629726200129 1.3299377410250139 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.34294163526406091 2.0332099582611573e-13 -0.9672662044347794 ;
createNode joint -n "heelRollFrontRGT_tmpJnt" -p "ankleFrontRGT_bind_jnt";
	rename -uid "FFB23130-4994-55B0-4406-30B5E05078AA";
	setAttr ".t" -type "double3" 0.10729999999999151 -5.4820739999999866 1.5759000000000434 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.96441149777263 0.048464874312730007 -0.36273240900809584 ;
createNode joint -n "lowerBody_bind_jnt" -p "body_bind_jnt";
	rename -uid "D52C43DF-4A6D-40EF-01BC-B3B0F2C7A002";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -1.7715069091650548e-06 -9.8591880759686319 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.813453674316399 -9.8591880759686319 1;
	setAttr ".liw" yes;
createNode joint -n "hip_bind_jnt" -p "lowerBody_bind_jnt";
	rename -uid "1A937C71-4CD3-539D-3456-7A89CBC96C46";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0 -0.040990685073879263 -11.774254196317081 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 41.77246298924252 -21.633442272285713 1;
	setAttr ".liw" yes;
createNode joint -n "tail01_bind_jnt" -p "hip_bind_jnt";
	rename -uid "38476F7F-4AD6-CD79-B816-4AA845364EF1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.3629055523893127e-31 0 -8.1923846321430887 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -89.999999999999986 0 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 7.3629055523893127e-31 41.77246298924252 -29.825826904428801 1;
	setAttr ".liw" yes;
createNode joint -n "tail02_bind_jnt" -p "tail01_bind_jnt";
	rename -uid "4B2E4AB0-40AB-EF2C-19BE-9DB4E78C0B9B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.1401505270772419e-31 15.22256963067397 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 8.5030560794665545e-31 41.77246298924252 -45.048396535102768 1;
	setAttr ".liw" yes;
createNode joint -n "tail03_bind_jnt" -p "tail02_bind_jnt";
	rename -uid "CCC67A6A-4DE4-AAAB-7270-C8A3BBABE270";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.8548270309372049e-31 13.37591024972069 -1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 1.4357883110403759e-30 41.772462989242506 -58.424306784823457 1;
	setAttr ".liw" yes;
createNode joint -n "tail04_bind_jnt" -p "tail03_bind_jnt";
	rename -uid "0F931C20-4837-583E-2E04-46B2116423B9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.7516230804060213e-46 12.59820143630332 1.4210854715202004e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0
		 1.4357883110403757e-30 41.77246298924252 -71.02250822112677 1;
	setAttr ".liw" yes;
createNode joint -n "upLegBackLFT_bind_jnt" -p "hip_bind_jnt";
	rename -uid "9DFE38FD-428F-A338-2573-53A6D070CABD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 8.8692702724309012 -8.0237469192689304 -2.2945756755694653 ;
	setAttr ".r" -type "double3" -1.4787718548899293e-06 2.4058324859078816e-09 3.6455212003403129e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 22.549378967578026 -0.29904618185507115 -177.75762651566413 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.038135510126723025 -0.92276387562020457 0.38347426604369977 0 -0.010187723475372425 0.38337444395253667 0.92353681356753325 0
		 8.8692702724309012 33.74871606997359 -23.928017947855178 1;
	setAttr ".liw" yes;
createNode joint -n "midLegBackLFT_bind_jnt" -p "upLegBackLFT_bind_jnt";
	rename -uid "4BA2DF77-4888-134C-B3DB-7780377A1348";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -9.0050278345188417e-10 10.992680549622996 -6.1461946643248666e-13 ;
	setAttr ".r" -type "double3" 2.224571181607145e-06 1.2018198987348904e-09 -3.036202408072333e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -62.141777370858939 0 0 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.026827197462727256 -0.77013788114561099 -0.6373130671034799 0 0.028955281358189037 -0.63667635298484737 0.77058731707145456 0
		 9.2884817537506876 23.605067562583631 -19.712607842240914 1;
	setAttr ".liw" yes;
createNode joint -n "lowLegBackLFT_bind_jnt" -p "midLegBackLFT_bind_jnt";
	rename -uid "AA5F5C7E-4146-C0C8-ED32-D69704EE8C0A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 9.0049034895400837e-10 15.082262039184648 -1.3855583347321954e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 27.38358026755991 1.6592473460148247 -1.5379145921097963 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.6930965747606965 11.989646232807946 -29.324730521287474 1;
	setAttr ".liw" yes;
createNode joint -n "ankleBackLFT_bind_jnt" -p "lowLegBackLFT_bind_jnt";
	rename -uid "2ADF23E0-4409-202C-1FC2-79A4510B0FF5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.656667774658672e-09 8.0871154839226911 -7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 12.180693393957604 -2.7702134519866387e-08 -9.961858784222054e-09 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.693096573510088 4.0845955947465722 -31.031074935521517 1;
	setAttr ".liw" yes;
createNode joint -n "footOutBackLFT_tmpJnt" -p "ankleBackLFT_bind_jnt";
	rename -uid "E83CDD90-4D70-68C6-3F63-60A0E1D3B677";
	setAttr ".t" -type "double3" 3.7348075794322328 4.0443870468691747 4.4112183761180752 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -143.04246222373902 -89.939871904661018 -36.65313406472751 ;
createNode joint -n "footInBackLFT_tmpJnt" -p "ankleBackLFT_bind_jnt";
	rename -uid "EE6F6CA5-4B69-942C-340E-AD842BBC260E";
	setAttr ".t" -type "double3" -4.4883381466864449 4.0197155016338764 4.4294447390227063 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 53.709613413753971 89.939871904670511 143.34686594724846 ;
createNode joint -n "heelRollBackLFT_tmpJnt" -p "ankleBackLFT_bind_jnt";
	rename -uid "272EA63C-4888-52C6-B115-2B807043C18B";
	setAttr ".t" -type "double3" -0.48376115308477807 3.8678795177686376 -3.2173132640674531 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.96441149787901 0.048464901390676642 -0.36273241485181335 ;
createNode joint -n "ballRollBackLFT_bind_jnt" -p "ankleBackLFT_bind_jnt";
	rename -uid "44FC08DE-4776-E7AE-46BB-5D8DAFEF8D8F";
	setAttr ".t" -type "double3" -0.49726194405130997 4.0043527837324602 4.254807186231087 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.035894637512541 0.048238606429001671 3.0214641708742593e-05 ;
createNode joint -n "toeRollBackLFT_bind_jnt" -p "ballRollBackLFT_bind_jnt";
	rename -uid "541A19FF-43A2-2E60-E975-25A13B9AE8AD";
	setAttr ".t" -type "double3" -7.1054273576010019e-15 5.7649309771074932 9.8532293435482643e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "legPovBackLFT_tmpJnt" -p "midLegBackLFT_bind_jnt";
	rename -uid "D75EC4CF-48F8-7AC2-EBD3-61A4928950F8";
	setAttr ".t" -type "double3" 0.061630787784155316 -7.5255249386613219 9.0992539240909736 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -39.564273660892198 -1.6592473259987066 178.46208538629409 ;
	setAttr ".radi" 10;
createNode joint -n "upLegBackRGT_bind_jnt" -p "hip_bind_jnt";
	rename -uid "7F6A6EA2-4AB1-B34A-06D5-57A68F113426";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -8.86927 -8.0237629892425204 -2.2945577277142881 ;
	setAttr ".r" -type "double3" -1.4787718548899293e-06 2.4058324859078816e-09 3.6455212003403129e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -157.45062103242211 0.29904618185510168 177.75762651566401 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.038135510126723025 -0.92276387562020457 0.38347426604369977 0 -0.010187723475372425 0.38337444395253667 0.92353681356753325 0
		 8.8692702724309012 33.74871606997359 -23.928017947855178 1;
	setAttr ".liw" yes;
createNode joint -n "midLegBackRGT_bind_jnt" -p "upLegBackRGT_bind_jnt";
	rename -uid "C261AC4E-40CA-14B0-B12E-ABB8409B1477";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 4.7139316095012873e-07 -10.992631857021944 -9.2786775436337621e-06 ;
	setAttr ".r" -type "double3" 2.224571181607145e-06 1.2018198987348904e-09 -3.036202408072333e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -62.141777370858804 1.0330735413832143e-13 -8.6322562387095571e-14 ;
	setAttr ".bps" -type "matrix" -0.9992206428801218 -0.039126277288580792 0.0052193167917971737 0
		 0.026827197462727256 -0.77013788114561099 -0.6373130671034799 0 0.028955281358189037 -0.63667635298484737 0.77058731707145456 0
		 9.2884817537506876 23.605067562583631 -19.712607842240914 1;
	setAttr ".liw" yes;
createNode joint -n "lowLegBackRGT_bind_jnt" -p "midLegBackRGT_bind_jnt";
	rename -uid "9F4DA727-4236-F662-C2BC-FAB7DEA3CC6A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.9776110580238537e-06 -15.082308311389575 -6.7713616051179315e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 27.38358026755991 1.6592473460148398 -1.5379145921098494 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.6930965747606965 11.989646232807946 -29.324730521287474 1;
	setAttr ".liw" yes;
createNode joint -n "ankleBackRGT_bind_jnt" -p "lowLegBackRGT_bind_jnt";
	rename -uid "D712E001-498C-90E2-6C46-85ADDD57246A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.4061178887914139e-09 -8.0870777142162122 6.5018765873503526e-05 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 12.180693393957549 -1.2050587927889972e-14 -1.5972053952630389e-14 ;
	setAttr ".bps" -type "matrix" 1 6.7937953873720147e-11 5.0929299666435668e-10 0 -6.7937953873720147e-11 1 -1.300650487312538e-08 0
		 -5.0929299319490973e-10 1.3006504817614228e-08 1 0 9.693096573510088 4.0845955947465722 -31.031074935521517 1;
	setAttr ".liw" yes;
createNode joint -n "footOutBackRGT_tmpJnt" -p "ankleBackRGT_bind_jnt";
	rename -uid "95521C19-408B-C432-3ACA-63B3B839DF17";
	setAttr ".t" -type "double3" -3.7348099980281813 -4.044391499746256 -4.4112000019021131 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -143.04246222375144 -89.939871904660976 -36.653134064733862 ;
createNode joint -n "footInBackRGT_tmpJnt" -p "ankleBackRGT_bind_jnt";
	rename -uid "255EB9D6-45EE-FEBC-D139-1ABEFFCA575E";
	setAttr ".t" -type "double3" 4.488300001982811 -4.0197199003049304 -4.4294999977141423 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 53.709613413743604 89.93987190467044 143.34686594723544 ;
createNode joint -n "heelRollBackRGT_tmpJnt" -p "ankleBackRGT_bind_jnt";
	rename -uid "B7343118-4FEC-2D9A-4004-5DA4A2BBB322";
	setAttr ".t" -type "double3" 0.4837999980986698 -3.867884000032872 3.217300000246393 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -179.96441149790161 0.048464901390814753 -0.36273241485251795 ;
createNode joint -n "ballRollBackRGT_bind_jnt" -p "ankleBackRGT_bind_jnt";
	rename -uid "2D4E8893-4F06-E3A7-2F48-51A872ACF0B6";
	setAttr ".t" -type "double3" 0.49730000189488344 -4.0043572000337839 -4.2547999997467336 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90.035894637512584 0.04823860642906258 3.0214635832568877e-05 ;
createNode joint -n "toeRollBackRGT_bind_jnt" -p "ballRollBackRGT_bind_jnt";
	rename -uid "0CD06EAB-4D67-E9CD-B239-7DA9E53A5784";
	setAttr ".t" -type "double3" -4.6310732884080608e-05 -5.7650032134865086 5.4135069732508256e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "legPovBackRGT_tmpJnt" -p "midLegBackRGT_bind_jnt";
	rename -uid "19DCB1C0-4E61-F1FD-706B-21922F89D7BB";
	setAttr ".t" -type "double3" -0.061630736540903897 7.5255201589712684 -9.0992491574431789 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -39.564273660892219 -1.6592473259988241 178.46208538629409 ;
	setAttr ".radi" 10;
createNode transform -n "rig_grp";
	rename -uid "DC814CC9-43E0-F25B-1908-3EB1E6E8120B";
createNode transform -n "placement_Zro_grp" -p "rig_grp";
	rename -uid "789D915E-443C-1E20-92E0-B7B7900E3BB9";
createNode transform -n "placement_ctrl" -p "placement_Zro_grp";
	rename -uid "A3BA903A-4E2E-9B5E-2413-C580CA8948A6";
	addAttr -ci true -sn "____Extra____" -ln "____Extra____" -min 0 -max 0 -at "enum";
	addAttr -ci true -sn "IK_FK_Arm_Vis" -ln "IK_FK_Arm_Vis" -min 0 -max 2 -en "Both:IK:FK" 
		-at "enum";
	addAttr -ci true -sn "IK_FK_Arm_L" -ln "IK_FK_Arm_L" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "IK_FK_Arm_R" -ln "IK_FK_Arm_R" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "IK_FK_Leg_Vis" -ln "IK_FK_Leg_Vis" -min 0 -max 2 -en "Both:IK:FK" 
		-at "enum";
	addAttr -ci true -sn "IK_FK_Leg_L" -ln "IK_FK_Leg_L" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "IK_FK_Leg_R" -ln "IK_FK_Leg_R" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "____Prop____" -ln "____Prop____" -min 0 -max 0 -at "enum";
	addAttr -ci true -sn "Prop_Ctrl_Vis" -ln "Prop_Ctrl_Vis" -min 0 -max 1 -en "off:on" 
		-at "enum";
	setAttr -l on -k off ".v";
	setAttr -cb on ".____Extra____";
	setAttr -k on ".IK_FK_Arm_Vis";
	setAttr -k on ".IK_FK_Arm_L";
	setAttr -k on ".IK_FK_Arm_R";
	setAttr -k on ".IK_FK_Leg_Vis";
	setAttr -k on ".IK_FK_Leg_L";
	setAttr -k on ".IK_FK_Leg_R";
	setAttr -cb on ".____Prop____";
	setAttr -k on ".Prop_Ctrl_Vis" 1;
createNode nurbsCurve -n "placement_ctrlShape" -p "placement_ctrl";
	rename -uid "B3EF0827-4E4A-335B-8678-43942E483CF5";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 25 0 no 3
		26 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		26
		-30.54038720847139 0 -30.540387208471355
		-30.54038720847139 0 -30.540387208471355
		-15.270193604235676 0 -45.810580812707045
		-30.540387208471351 0 -45.810580812707045
		0 0 -76.350968021178375
		30.540387208471351 0 -45.810580812707045
		15.270193604235676 0 -45.810580812707045
		30.540387208471351 0 -30.32321043559946
		45.810580812707045 0 -15.270193604235676
		45.810580812707045 0 -30.540387208471351
		76.350968021178375 0 0
		45.810580812707045 0 30.540387208471351
		45.810580812707045 0 15.270193604235676
		30.54038720847139 0 30.540387208471355
		15.270193604235676 0 45.810580812707045
		30.540387208471351 0 45.810580812707045
		0 0 76.350968021178375
		-30.540387208471351 0 45.810580812707045
		-15.270193604235676 0 45.810580812707045
		-30.54038720847139 0 30.540387208471355
		-45.810580812707045 0 15.270193604235676
		-45.810580812707045 0 30.540387208471351
		-76.350968021178375 0 0
		-45.810580812707045 0 -30.540387208471351
		-45.810580812707045 0 -15.270193604235676
		-30.54038720847139 0 -30.540387208471355
		;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "fly_Zro_grp" -p "placement_ctrl";
	rename -uid "979B1135-4438-EF6A-EE3C-ACB5BFD2B5A9";
createNode transform -n "fly_ctrl" -p "fly_Zro_grp";
	rename -uid "20256F3A-46B8-8865-159C-EC846BE1B0A2";
createNode nurbsCurve -n "fly_ctrlShape" -p "fly_ctrl";
	rename -uid "E16BBCE6-4E34-D4A9-A932-56AEEB36DA22";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 47 0 no 3
		48 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
		48
		-35.67429832995245 0 0
		-35.67429832995245 0 0
		-35.235067051796541 0 -5.5806851040567826
		-33.928280278915231 0 -11.023948337701276
		-31.786019694085866 0 -16.195778507759965
		-28.861115266621425 0 -20.968808136097376
		-25.225546497415305 0 -25.225546497415305
		-20.968808136097376 0 -28.861115266621425
		-16.195778507759965 0 -31.786019694085866
		-11.023948337701276 0 -33.928280278915231
		-5.5806851040567826 0 -35.235067051796541
		0 0 -35.67429832995245
		0 0 -35.67429832995245
		0 0 -35.67429832995245
		5.5806851040567826 0 -35.235067051796541
		11.023948337701276 0 -33.928280278915231
		16.195778507759965 0 -31.786019694085866
		20.968808136097376 0 -28.861115266621425
		25.225546497415305 0 -25.225546497415305
		28.861115266621425 0 -20.968808136097376
		31.786019694085866 0 -16.195778507759965
		33.928280278915231 0 -11.023948337701276
		35.235067051796541 0 -5.5806851040567826
		35.67429832995245 0 0
		35.67429832995245 0 0
		35.67429832995245 0 0
		35.235067051796541 0 5.5806851040567826
		33.928280278915231 0 11.023948337701276
		31.786019694085866 0 16.195778507759965
		28.861115266621425 0 20.968808136097376
		25.225546497415305 0 25.225546497415305
		20.968808136097376 0 28.861115266621425
		16.195778507759965 0 31.786019694085866
		11.023948337701276 0 33.928280278915231
		5.5806851040567826 0 35.235067051796541
		0 0 35.67429832995245
		0 0 35.67429832995245
		0 0 35.67429832995245
		-5.5806851040567826 0 35.235067051796541
		-11.023948337701276 0 33.928280278915231
		-16.195778507759965 0 31.786019694085866
		-20.968808136097376 0 28.861115266621425
		-25.225546497415305 0 25.225546497415305
		-28.861115266621425 0 20.968808136097376
		-31.786019694085866 0 16.195778507759965
		-33.928280278915231 0 11.023948337701276
		-35.235067051796541 0 5.5806851040567826
		-35.67429832995245 0 0
		;
createNode transform -n "null_IK_jnt_grp" -p "fly_ctrl";
	rename -uid "727D6A50-4DF5-7DFC-1CEA-8B9C6BBB0B37";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "hips_null_grp" -p "null_IK_jnt_grp";
	rename -uid "3D98EAEB-4B22-8EE5-5A60-A2945B64268A";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "shoulderLFT_null_grp" -p "null_IK_jnt_grp";
	rename -uid "FCB872F7-483A-96F3-D71F-EE9C4ACF04EA";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "shoulderRGT_null_grp" -p "null_IK_jnt_grp";
	rename -uid "3FD88E1D-48ED-78B2-67D2-A3AEEAD38F65";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "null_FK_jnt_grp" -p "fly_ctrl";
	rename -uid "F071678E-423B-16C8-13A0-5DB25C971E53";
createNode transform -n "IK_ctrl_grp" -p "fly_ctrl";
	rename -uid "B84C9570-4E2B-ED58-E44E-E08EB5FEB757";
createNode transform -n "NOTOUCH_grp" -p "fly_ctrl";
	rename -uid "F244AFF5-4A61-AAE9-6453-DAA0BCEE9216";
createNode transform -n "still_grp" -p "rig_grp";
	rename -uid "92FA97CF-481D-300A-7B05-5DA15C7384BF";
createNode transform -n "addRig";
	rename -uid "8536A2AC-4429-2618-EB9C-51AA62CD19F1";
createNode joint -n "ear01RGT_bind_jnt" -p "addRig";
	rename -uid "BBC5D6AC-4FBE-2616-2230-CE9616633D04";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -15.296400000000004 102.795 28.588999999999992 ;
	setAttr ".r" -type "double3" -1.4345195468663017e-31 3.2302508483613845e-16 -5.0888874903416268e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 179.61745568169823 1.2721610290627795e-14 90.560357394487653 ;
	setAttr ".bps" -type "matrix" -0.0097799256116615219 0.99995217538391823 -5.5074815562767733e-17 0
		 0.99992988765238588 0.00977970762888003 0.0066766082841973841 0 0.0066762889779694648 6.5296732357597153e-05 -0.99997771120251455 0
		 -15.296400000000004 102.795 28.588999999999995 1;
	setAttr ".liw" yes;
createNode joint -n "ear02RGT_bind_jnt" -p "ear01RGT_bind_jnt";
	rename -uid "02C12873-4C29-24D0-DA86-89AA53F2C6A6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.5165785855469949e-05 -11.35669544564648 -2.4207433099832087e-05 ;
	setAttr ".r" -type "double3" -3.4758561966312933e-15 1.0496762251958939e-14 -4.9455123502418246e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 1.6014513050932346 0.0063801958237682324 -0.95562733663669808 ;
	setAttr ".bps" -type "matrix" -0.026456209432717901 0.99964997323185678 1.135532369089115e-12 0
		 0.99942375095691383 0.026450222353219619 -0.021273263987407164 0 -0.02126581777559583 -0.00056280992623345956 -0.99977369851347964 0
		 -26.652300000000007 102.68400000000001 28.51320000000003 1;
	setAttr ".liw" yes;
createNode joint -n "ear03RGT_bind_jnt" -p "ear02RGT_bind_jnt";
	rename -uid "7B16753D-4B15-85CC-226D-2DA35810E866";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 0.00055390898879181805 -15.824203337360487 3.2462332345772893e-05 ;
	setAttr ".r" -type "double3" 3.0876810870600876e-12 2.2037765210859579e-13 -9.6003676415380619e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 9.33491281657545 -0.057810764990945014 -2.7179366683727029 ;
	setAttr ".bps" -type "matrix" -0.073839697215691363 0.99727012344454335 -3.9874787499671882e-15 0
		 0.98040380023227236 0.072590883910390147 -0.18313643019133755 0 -0.18263649034410792 -0.013522738554494849 -0.98308750777170051 0
		 -42.467399999999998 102.26599999999996 28.849800000000037 1;
	setAttr ".liw" yes;
createNode joint -n "ear04RGT_bind_jnt" -p "ear03RGT_bind_jnt";
	rename -uid "AC911CEC-4E50-99A6-D9ED-FBB5567EAF98";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -0.0006405375025764215 -12.816507812924257 -3.1036526699779188e-05 ;
	setAttr ".r" -type "double3" 2.0299137046911359e-14 -1.6950181395599026e-14 -4.2423187925186165e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0.0058790387256107716 0.093129123842382491 0.49992959082506006 ;
	setAttr ".bps" -type "matrix" -0.064985617342654525 0.99788620069554723 2.3136874360840665e-16 0
		 0.9809919978766567 0.06388541152867247 -0.18323033126580784 0 -0.18284301911902354 -0.011907336193207364 -0.98307001058125165 0
		 -55.032699999999991 101.33499999999994 31.197000000000056 1;
	setAttr ".liw" yes;
createNode joint -n "ear05RGT_bind_jnt" -p "ear04RGT_bind_jnt";
	rename -uid "982E4E12-4FFD-F8AB-7939-ED925528C56F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.5992971681462222e-07 -10.518847463918426 -2.8578485178343271e-05 ;
	setAttr ".r" -type "double3" -1.7635927227880707e-14 -1.5262862461388065e-14 -4.2433732132960731e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -0.016563456747359675 0.58038154053428648 -1.6347434300805344 ;
	setAttr ".bps" -type "matrix" -0.091087838716388148 0.99572708496010887 0.015184792221870233 0
		 0.97879192446148344 0.092327415191855958 -0.18287158612801541 0 -0.18349216399335092 -0.0017946255416465932 -0.98301953443062484 0
		 -65.351599999999991 100.66299999999994 33.124400000000058 1;
	setAttr ".liw" yes;
createNode joint -n "ear01LFT_bind_jnt" -p "addRig";
	rename -uid "87137AE5-4E69-D583-3332-648BE022BC93";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 15.296432572716764 102.79535322090948 28.589025847201437 ;
	setAttr ".r" -type "double3" -1.2424041724466862e-16 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -0.38254431830206592 -1.2721610290627795e-14 -90.560357394487653 ;
	setAttr ".bps" -type "matrix" -0.0097799256116615219 -0.99995217538391823 5.5508496431761935e-17 0
		 0.99992988765238588 -0.009779707628880141 -0.0066766082842026871 0 0.0066762889779747678 -6.5296732357649195e-05 0.99997771120251444 0
		 15.296432572716764 102.79535322090948 28.589025847201441 1;
	setAttr ".liw" yes;
createNode joint -n "ear02LFT_bind_jnt" -p "ear01LFT_bind_jnt";
	rename -uid "DBA6335B-489E-FC2B-D081-AC8068455C79";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -5.6843418860808015e-14 11.356646778644338 -3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 8.1314381676422765e-17 -6.5047207248264051e-11 1.3775415177090914e-12 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 1.6014513050931076 0.0063801958237703358 -0.95562733663663824 ;
	setAttr ".bps" -type "matrix" -0.026456209432716874 -0.99964997323185678 -1.1354870765433595e-12 0
		 0.99942375095691405 -0.026450222353218714 0.021273263987399659 0 -0.021265817775588329 0.00056280992623328684 0.99977369851347986 0
		 26.652283110194425 102.68428853576992 28.513201965238377 1;
	setAttr ".liw" yes;
createNode joint -n "ear03LFT_bind_jnt" -p "ear02LFT_bind_jnt";
	rename -uid "611CACD4-49D3-BB86-60F3-A987E53CF0FF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -1.4210854715202004e-14 15.824248017812476 3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 3.0843685269353014e-12 2.3459075584138459e-13 -4.9938435711488226e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 9.3349128165757502 -0.057810764990936216 -2.7179366683726931 ;
	setAttr ".bps" -type "matrix" -0.07383969721569017 -0.99727012344454335 4.2392304944183223e-15 0
		 0.98040380023227303 -0.072590883910389079 0.18313643019133533 0 -0.1826364903441057 0.013522738554494734 0.98308750777170095 0
		 42.467412420229081 102.26573365712632 28.84983537072339 1;
	setAttr ".liw" yes;
createNode joint -n "ear04LFT_bind_jnt" -p "ear03LFT_bind_jnt";
	rename -uid "0ECA96F2-4A6D-737A-897B-A49E69857935";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.4210854715202004e-14 12.816411582325003 3.5527136788005009e-15 ;
	setAttr ".r" -type "double3" 5.9908146818423373e-15 -1.1306894095724245e-14 1.1038005802074211e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0.0058790390138615473 0.093129123842463996 0.49992959082544114 ;
	setAttr ".bps" -type "matrix" -0.064985617342646546 -0.99788620069554756 -1.8127860323957634e-16 0
		 0.98099199787573788 -0.063885411528604857 0.18323033127075133 0 -0.18284301912395667 0.01190733619352723 0.98307001058033028 0
		 55.032671040881432 101.33537901180598 31.196987235773278 1;
	setAttr ".liw" yes;
createNode joint -n "ear05LFT_bind_jnt" -p "ear04LFT_bind_jnt";
	rename -uid "14C5A08C-415C-CB58-5303-D0AB20715020";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.8421709430404007e-14 10.518879792118071 -2.1316282072803006e-14 ;
	setAttr ".r" -type "double3" 4.7102648187884982e-15 -1.1564089352057915e-14 6.7810334802167409e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -0.016563457167577619 0.58038154052600344 -1.6347434300839687 ;
	setAttr ".bps" -type "matrix" -0.091087838716389202 -0.99572708496010853 -0.015184792221870748 0
		 0.97879192446190688 -0.092327415191861356 0.18287158612574717 0 -0.18349216399109247 0.0017946255414332726 0.98301953443104673 0
		 65.351607943566066 100.66337604746663 33.124365064680262 1;
	setAttr ".liw" yes;
createNode transform -n "TMP_GRP";
	rename -uid "E3482055-48F3-D9DF-A1DE-A88DEF4457B1";
	setAttr ".v" no;
createNode transform -n "hat_Zro_grp" -p "TMP_GRP";
	rename -uid "98E86B3A-4FD4-C170-B496-3CBE144A17C3";
createNode transform -n "hat_ctrl" -p "hat_Zro_grp";
	rename -uid "EE6B3A7B-44EA-DD8F-7E57-EF88B97758D3";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".t" -type "double3" 2.2815279078562374e-09 0 0 ;
	setAttr ".s" -type "double3" 1 0.99999999999999989 0.99999999999999989 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "hat_ctrlShape" -p "hat_ctrl";
	rename -uid "51BC8851-482D-03C2-2B82-D8B1B63AE822";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		22.031316884150222 -9.5038436378315723 -28.344917748188358
		-0.00010327760446383525 -27.448980390486128 -30.276162285584562
		-22.031457455273262 -9.5038152472454769 -28.344834053399218
		-31.157111137292162 13.720620823613507 -9.1061242133580098
		-22.031345531361382 24.792304823337318 18.945937346534535
		5.500670959966277e-05 21.053057750108113 36.603088003287517
		22.031428808062053 24.792276432751169 18.945853651745409
		31.157061929305712 13.720580673261525 -9.1062425756638312
		22.031316884150222 -9.5038436378315723 -28.344917748188358
		-0.00010327760446383525 -27.448980390486128 -30.276162285584562
		-22.031457455273262 -9.5038152472454769 -28.344834053399218
		;
createNode transform -n "hat_Gimbal_ctrl" -p "hat_ctrl";
	rename -uid "FD2BECA3-4EFD-111D-683F-E8846C907290";
createNode nurbsCurve -n "hat_Gimbal_ctrlShape" -p "hat_Gimbal_ctrl";
	rename -uid "6502EC2A-48DF-D929-3523-20AF72FDA3E1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		14.645096326026893 -3.1633513706959935 -20.411747333868707
		-7.7527022241674368e-05 -15.09220777851665 -21.695523494982893
		-14.645207517787338 -3.1633324983279794 -20.411691698565644
		-20.711397700474205 12.274887162936478 -7.6229450701794859
		-14.645133117447457 19.634682211651121 11.024392026772858
		2.769094739675536e-05 17.149053819517047 22.76181245728695
		14.645170726366738 19.634663339283097 11.024336391469804
		20.711347241476723 12.274860473377618 -7.623023750379569
		14.645096326026893 -3.1633513706959935 -20.411747333868707
		-7.7527022241674368e-05 -15.09220777851665 -21.695523494982893
		-14.645207517787338 -3.1633324983279794 -20.411691698565644
		;
createNode transform -n "neck_Zro_grp" -p "TMP_GRP";
	rename -uid "AE561B13-4DDD-1410-7011-55B1E23E1972";
createNode transform -n "neck_ctrl" -p "neck_Zro_grp";
	rename -uid "ACD66C62-4219-962D-BC1B-8E935A7A1C1A";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" -1.7431519705689263e-21 0 0 ;
	setAttr ".sp" -type "double3" -1.7431519705689263e-21 0 0 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "neck_ctrlShape" -p "neck_ctrl";
	rename -uid "37A91271-48E4-23A3-91C3-72BE428ACDEA";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		7.6491197476025379 -0.7362157757620803 -7.710767200665436
		-1.6021995953391139e-15 3.5928987780361257 -10.879136340338285
		-7.6491197476025254 -0.7362157757620803 -7.7107672006654404
		-10.817488887275369 3.7996275044585031 -0.061647453062877264
		-7.6491197476025325 -0.73621577576208208 7.5874722945396078
		-3.6275739755721916e-15 3.592898778036123 10.75584143421244
		7.6491197476025219 -0.73621577576208208 7.5874722945396122
		10.817488887275369 3.7996275044585031 -0.061647453062868354
		7.6491197476025379 -0.7362157757620803 -7.710767200665436
		-1.6021995953391139e-15 3.5928987780361257 -10.879136340338285
		-7.6491197476025254 -0.7362157757620803 -7.7107672006654404
		;
createNode transform -n "neck_Gimbal_ctrl" -p "neck_ctrl";
	rename -uid "19AB9FAE-4DF4-BB3B-9EA5-67A12FD6516D";
	setAttr ".rp" -type "double3" -1.7431519705689263e-21 0 0 ;
	setAttr ".sp" -type "double3" -1.7431519705689263e-21 0 0 ;
createNode nurbsCurve -n "neck_Gimbal_ctrlShape" -p "neck_Gimbal_ctrl";
	rename -uid "60B8F357-4C25-8622-9B4A-C697B79E28A9";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.5017517854621563 -0.62578340939776822 -6.5541521205656208
		-1.3618699175110421e-15 3.0539639613307061 -9.2472658892875419
		-6.5017517854621465 -0.62578340939776822 -6.5541521205656244
		-9.1948655541840658 3.2296833787897281 -0.052400335103445682
		-6.5017517854621527 -0.62578340939776989 6.4493514503586677
		-3.0834381407091585e-15 3.0539639613307044 9.1424652190805737
		6.5017517854621438 -0.62578340939776989 6.4493514503586704
		9.1948655541840658 3.2296833787897281 -0.052400335103438084
		6.5017517854621563 -0.62578340939776822 -6.5541521205656208
		-1.3618699175110421e-15 3.0539639613307061 -9.2472658892875419
		-6.5017517854621465 -0.62578340939776822 -6.5541521205656244
		;
createNode transform -n "upperChest_Zro_grp" -p "TMP_GRP";
	rename -uid "48258CF3-4D9B-E5BF-782B-BEAEEFB6596A";
createNode transform -n "upperChest_ctrl" -p "upperChest_Zro_grp";
	rename -uid "CA9CA38B-4B6B-998D-3662-CE9F4B1C4132";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
	setAttr ".sp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "upperChest_ctrlShape" -p "upperChest_ctrl";
	rename -uid "CD64B50F-4CAD-497A-287F-59929B6C1B8A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-11.824502873829381 10.529698870871933 8.3936793238746095
		11.82450285672796 10.529698870871933 8.3936793238746095
		11.82450285672796 10.529698870871933 -8.3936793238746059
		-11.824502873829381 10.529698870871933 -8.3936793238746059
		-11.824502873829381 10.529698870871933 8.3936793238746095
		-7.3290278409624099 -3.5143965767700016 8.3936793238746077
		-7.3290278409624099 -3.5143965767700016 -8.3936793238746077
		7.3290278409624126 -3.5143965767700016 -8.3936793238746077
		7.3290278409624126 -3.5143965767700016 8.3936793238746077
		-7.3290278409624099 -3.5143965767700016 8.3936793238746077
		7.3290278409624126 -3.5143965767700016 8.3936793238746077
		11.82450285672796 10.529698870871933 8.3936793238746095
		11.82450285672796 10.529698870871933 -8.3936793238746059
		7.3290278409624126 -3.5143965767700016 -8.3936793238746077
		-7.3290278409624099 -3.5143965767700016 -8.3936793238746077
		-11.824502873829381 10.529698870871933 -8.3936793238746059
		;
createNode transform -n "upperChest_Gimbal_ctrl" -p "upperChest_ctrl";
	rename -uid "BA3E64B4-4649-DD04-2B03-7D81E11F7E33";
	setAttr ".rp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
	setAttr ".sp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
createNode nurbsCurve -n "upperChest_Gimbal_ctrlShape" -p "upperChest_Gimbal_ctrl";
	rename -uid "340B1367-4EE8-2711-8D98-7D913EED8C35";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-10.050827442754974 8.9502440402411416 7.1346274252934183
		10.050827428218765 8.9502440402411416 7.1346274252934183
		10.050827428218765 8.9502440402411416 -7.1346274252934156
		-10.050827442754974 8.9502440402411416 -7.1346274252934156
		-10.050827442754974 8.9502440402411416 7.1346274252934183
		-6.2296736648180486 -2.9872370902545016 7.1346274252934165
		-6.2296736648180486 -2.9872370902545016 -7.1346274252934165
		6.2296736648180513 -2.9872370902545016 -7.1346274252934165
		6.2296736648180513 -2.9872370902545016 7.1346274252934165
		-6.2296736648180486 -2.9872370902545016 7.1346274252934165
		6.2296736648180513 -2.9872370902545016 7.1346274252934165
		10.050827428218765 8.9502440402411416 7.1346274252934183
		10.050827428218765 8.9502440402411416 -7.1346274252934156
		6.2296736648180513 -2.9872370902545016 -7.1346274252934165
		-6.2296736648180486 -2.9872370902545016 -7.1346274252934165
		-10.050827442754974 8.9502440402411416 -7.1346274252934156
		;
createNode transform -n "upperArmLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "0FC1313A-4DCD-6AD8-0307-539DAE1C9E8D";
createNode transform -n "upperArmLFT_FK_ctrl" -p "upperArmLFT_FK_Zro_grp";
	rename -uid "40E45137-4C26-44E5-9811-3B801A9549AB";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" -4.029018738133086e-09 1.9283122858460053e-09 1.5009892426401923e-10 ;
	setAttr ".sp" -type "double3" -4.029018738133086e-09 1.9283122858460053e-09 1.5009892426401923e-10 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "upperArmLFT_FK_ctrlShape" -p "upperArmLFT_FK_ctrl";
	rename -uid "4F70B480-4685-6198-758D-55A7608EEFFE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		0.055087727239956176 -0.63283258277594745 3.9731771760725967
		-0.94028723042602713 -0.5428904853008405 3.9582491719383293
		-1.8580147095934834 -0.30948931684728032 3.9016833259077957
		-2.6727689412162419 0.017283872693386982 3.7731260175178076
		-3.3781790278043284 0.40139322521571608 3.5522090878515771
		-3.9721411623790948 0.81589675858783806 3.2263136478560859
		-4.4587676345813234 1.2377712675652843 2.7940083131433386
		-4.8570263146648935 1.6469270119778385 2.2664897583858798
		-5.1719038844781977 2.0208468885860245 1.6339223375182499
		-5.3925834208429615 2.3202365729113348 0.88135744430007457
		-5.4755003915110647 2.4542202544026144 -0.0042217308998438591
		-5.378741054669935 2.3284147390756407 -0.88959618813580765
		-5.1463032410721983 2.0359719266806962 -1.6413524143444651
		-4.8215492493949252 1.6678871087686069 -2.2723467976393072
		-4.4150638503009594 1.2635917671378458 -2.7973316756312259
		-3.9217088518792118 0.84569251822621649 -3.2258551761366716
		-3.3226951710334935 0.43417347350827701 -3.5462404446658788
		-2.6138903079751601 0.052069778524365694 -3.7596417266512008
		-1.7972025067815278 -0.27356104467204573 -3.8784599039482068
		-0.87868610533902947 -0.50649611236108982 -3.9228265683880612
		0.11680707508729918 -0.59636836300753004 -3.9230236537256955
		0.11625821231681392 -1.2075711715307826 -3.8543806192626451
		0.11426634277020999 -1.7936960454329449 -3.6010495026792499
		0.11103678811557757 -2.3282520648677063 -3.1892380209558211
		0.10671067981757608 -2.7878817449519122 -2.6369423331233763
		0.10147715157552947 -3.1524891658935128 -1.9683083238457246
		0.095564866791941316 -3.4061450820696497 -1.2125499643663511
		0.089232257776559826 -3.5377638460473282 -0.40270226819410898
		0.082756087615705493 -3.541590012399364 0.42584083832953012
		0.076419384239495958 -3.4174563662570887 1.2368695530179745
		0.070499089775925575 -3.1707912201578319 1.9949383049519791
		0.065253986584824106 -2.8123746475122262 2.6669111086663442
		0.060913243763526886 -2.3578654033194666 3.2234281252262118
		0.057666634861928835 -1.8271355463346939 3.6401589050493621
		0.055656036531615397 -1.2433753582785325 3.8988923399114106
		0.055087727239956176 -0.63283258277594745 3.9731771760725967
		1.0505779171423306 -0.54293047165902075 3.9738102554438139
		1.9690868535108697 -0.3095630476393379 3.9315968918334656
		2.7857642109413669 0.01717110229722011 3.8157912183569769
		3.4945595974585673 0.40125518684145678 3.6059280751921885
		4.0935544760355791 0.81573162355354234 3.2893570612580589
		4.5869043989279161 1.2375927222265144 2.8647114880329427
		4.9933656181961137 1.6467197590307969 2.3434827607073991
		5.3181244673371397 2.0206550145691109 1.7159150231392415
		5.5505277023057529 2.3199916916953138 0.96689133168430896
		5.6473749284316712 2.4541379822598772 0.08271800451748175
		5.5643700684787776 2.3281698578596197 -0.80406230075157303
		5.3437251107431418 2.0357800526637826 -1.5593597287234737
		5.0288426834660855 1.6676798558215482 -2.1953537953177755
		4.630608183208281 1.2634132217990712 -2.7266285007416307
		4.1439867865354563 0.84552738319192056 -3.162811762734687
		3.5500434542293999 0.43403543513402254 -3.4925214573252683
		2.8446428441824532 0.05195700812820167 -3.7169765258120391
		2.0298990563228259 -0.2736347754641093 -3.84854633802254
		1.1121790422293283 -0.50653609871926475 -3.9072654848825761
		0.11680707508729918 -0.59636836300753004 -3.9230236537256955
		;
createNode transform -n "upperArmLFT_FK_Gimbal_ctrl" -p "upperArmLFT_FK_ctrl";
	rename -uid "F7F83012-45E6-F8E2-A9BF-31815DF90908";
	setAttr ".rp" -type "double3" -4.029018738133086e-09 1.9283122858460048e-09 1.5009892426401928e-10 ;
	setAttr ".sp" -type "double3" -4.029018738133086e-09 1.9283122858460048e-09 1.5009892426401928e-10 ;
createNode nurbsCurve -n "upperArmLFT_FK_Gimbal_ctrlShape" -p "upperArmLFT_FK_Gimbal_ctrl";
	rename -uid "DEE9C96B-4F9A-2879-A2D4-AE8B3F8B6326";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		0.046824567549609938 -0.53790769507030844 3.377200599684222
		-0.7992441464664759 -0.46145691221646751 3.3645117961700945
		-1.5793125037588138 -0.26306591903094134 3.3164308270441416
		-2.271853600638158 0.014691292078625776 3.2071571149126514
		-2.8714521742380317 0.34118424172260553 3.0193777246963558
		-3.3763199886265829 0.6935122450889093 2.7423666007001879
		-3.7899524899984782 1.0521055777197383 2.374907066194353
		-4.1284723680695121 1.3998879604704093 1.9265162946505126
		-4.3961183024108212 1.7177198555873674 1.3888339869130271
		-4.5836959083208697 1.9722010872638813 0.74915382767757799
		-4.6541753333887579 2.0860872165314692 -0.0035884712423524413
		-4.5719298970737965 1.979152528503541 -0.75615675989292164
		-4.3743577555157227 1.7305761379678384 -1.3951495521702804
		-4.098316862590039 1.4177040427425625 -1.9314947779708964
		-3.7528042733601685 1.0740530023564154 -2.3777319242640269
		-3.3334525247016824 0.71883864078153092 -2.7419768996936562
		-2.8242908959828221 0.36904745277128231 -3.0143043779434819
		-2.2218067623832387 0.044259312034957685 -3.1956954676310052
		-1.5276221313686513 -0.23252688768199203 -3.2966909183334607
		-0.7468831901425278 -0.43052169521767952 -3.3344025831073374
		0.099286013219851477 -0.50691310826715363 -3.334570105644326
		0.098819479864939011 -1.0264354955119182 -3.2762235263507327
		0.09712639075032567 -1.5246416383287564 -3.0608920772548478
		0.094381269293888126 -1.9790142548483036 -2.7108523177899326
		0.090704077240586864 -2.3696994829198785 -2.2414009831323547
		0.086255578234847238 -2.6796157907202391 -1.6730620752463514
		0.08123013616879729 -2.8952233194699555 -1.0306674696888836
		0.075847418505723047 -3.0070992688509826 -0.34229692794247774
		0.070342673868996841 -3.0103515102502123 0.36196471260261542
		0.064956475999218749 -2.9048379110292788 1.0513391200877931
		0.05992422570518393 -2.6951725368449102 1.6956975592316972
		0.055465887992747674 -2.3905184500961454 2.2668744423889073
		0.051776256594645041 -2.0041855925322998 2.7399139064647948
		0.0490166390282867 -1.5530652140952432 3.0941350693144725
		0.047307630447520281 -1.0568690542475059 3.314058488947214
		0.046824567549609938 -0.53790769507030844 3.377200599684222
		0.89299122896662808 -0.46149090062092069 3.3777387171497568
		1.6737238248798862 -0.26312859020419038 3.3418573580809605
		2.367899578695809 0.014595437241883936 3.2434225356259452
		2.9703756572354298 0.34106690910448517 3.0650388639358748
		3.4795213040258894 0.69337188030975783 2.7959535020918653
		3.8988687384843761 1.0519538141817839 2.4350047648505164
		4.2443607748623444 1.3997117954654241 1.9919603466238041
		4.5204057966322155 1.7175567626729911 1.4585277696908698
		4.7179485463555375 1.9719929382302634 0.82185763195417749
		4.8002686885625687 2.0860172852101426 0.070310303862374302
		4.7297145576026081 1.9789443794699237 -0.68345295561632224
		4.5421663435273167 1.7304130450534621 -1.3254557693924378
		4.2745162803418211 1.4175278777375626 -1.866050725997594
		3.9360169551226858 1.0739012388184574 -2.3176342256078706
		3.5223887679507846 0.71869827600237934 -2.6883899983019686
		3.0175369354906372 0.36893012015316606 -2.968643238703963
		2.4179464169507323 0.044163457198218264 -3.1594300469177181
		1.7254141972700494 -0.23258955885524604 -3.2712643872966436
		0.94535218529057607 -0.4305556836221282 -3.3211756621276742
		0.099286013219851477 -0.50691310826715363 -3.334570105644326
		;
createNode transform -n "lowerArmLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "B47EC664-4D6B-8B2D-E918-3D850CA7870F";
createNode transform -n "lowerArmLFT_FK_ctrl" -p "lowerArmLFT_FK_Zro_grp";
	rename -uid "675812C1-42BF-0BA3-26E9-E98A2EB5BA39";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167833e-10 ;
	setAttr ".sp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167833e-10 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmLFT_FK_ctrlShape" -p "lowerArmLFT_FK_ctrl";
	rename -uid "D338E61A-4ACA-9ACE-8812-509386E3C998";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		0.23666589366335758 -0.79750032139760141 4.210437659644918
		-0.61092170000411716 -0.69830425994802714 4.1842992395504561
		-1.3926778721101378 -0.44707304017240068 4.0819446498268146
		-2.0872407852552115 -0.10602451919816278 3.8792859958905539
		-2.6893210333292861 0.28039273259198849 3.560741941396715
		-3.1972109005743277 0.67947747053804375 3.1176065548044885
		-3.6144208235555113 1.065180537854957 2.5529581218790907
		-3.9570256565848703 1.4173061417964057 1.8835456816536573
		-4.2293362537664114 1.7086776524356113 1.10294759420337
		-4.422241630889058 1.8922860120855076 0.20226610795519273
		-4.4987349461922816 1.8637326203625302 -0.81511623960850177
		-4.422241630889058 1.5441936892546979 -1.7814376192848307
		-4.2293362537664114 1.0649013415240525 -2.565795965202295
		-3.9570256565848712 0.52516863418530058 -3.2005552392361643
		-3.6144208235555113 -0.033833286551191923 -3.7100866991997425
		-3.197210900574325 -0.58873779614341493 -4.1096811112940816
		-2.6893210333292821 -1.1148531626224609 -4.3904661181343982
		-2.087240785255212 -1.5866384513688119 -4.5584162549516902
		-1.3926778721101385 -1.976310214559581 -4.6328510629770134
		-0.61092170000411672 -2.2473803682154001 -4.643554315961766
		0.23666589366335744 -2.3495493632476969 -4.634358008755366
		0.23666584576703714 -3.0197405812003519 -4.4342415843701115
		0.23666584576703711 -3.6246092495062103 -4.0324806622528229
		0.23666584576703711 -4.1397943395575298 -3.4637506730162597
		0.23666584576703653 -4.5427851869405247 -2.7529045870210189
		0.2366658457670365 -4.8159619157708926 -1.931020238387182
		0.2366658457670365 -4.9473902139053703 -1.0340071754735811
		0.2366658457670365 -4.9313273645688795 -0.10107441872581548
		0.23667573009651335 -3.8025510416255544 0.51673584862702049
		0.23667573009651385 -3.5899496991527897 1.1370219190669861
		0.23666584576703664 -4.0369603091212536 2.5083433708698748
		0.23666584576703667 -3.5002786917437327 3.188117045906476
		0.23666584576703667 -2.8793435781828927 3.7192887373550789
		0.23666584576703673 -2.2013031794984772 4.0786363342861058
		0.23666584576703667 -1.4957849312785441 4.250455849671658
		0.23666589366335758 -0.79750032139760141 4.210437659644918
		1.0842533915381904 -0.69830425994802925 4.1842992395504579
		1.8660095636442138 -0.44706952729677085 4.0819440334015731
		2.5605724767892823 -0.10602803207378442 3.8792866123157874
		3.162655099989589 0.28039273259198394 3.5607419413967154
		3.670540216982173 0.6794739576624178 3.11760717122973
		4.0877572653420575 1.0651840507305848 2.5529575054538549
		4.4303525978664879 1.4172956031695421 1.8835475309293541
		4.7026774458054028 1.7086987296893426 1.102943895651963
		4.8955614467919881 1.8922579090805167 0.20227103935706958
		4.9721331412607395 1.8638906997655957 -0.81514397874405742
		4.8955614467919863 1.5441655862497066 -1.7814326878829514
		4.7026774458054028 1.064922418777785 -2.5657996637537024
		4.4303525978664879 0.52515809555841964 -3.200553389960449
		4.0877572653420575 -0.033829773675572612 -3.7100873156249854
		3.6705402169821708 -0.58874130901903776 -4.1096804948688259
		3.1626550999895886 -1.1148531626224607 -4.3904661181343982
		2.5605724767892868 -1.5866419642444292 -4.5584156385264638
		1.8660095636442133 -1.9763067016839593 -4.632851679402255
		1.0842533915381907 -2.2473803682153988 -4.6435543159617696
		0.23666589366335744 -2.3495493632476969 -4.634358008755366
		;
createNode transform -n "lowerArmLFT_FK_Gimbal_ctrl" -p "lowerArmLFT_FK_ctrl";
	rename -uid "B4D6E314-4D65-37B8-F3A9-0680E27B34A3";
	setAttr ".rp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167836e-10 ;
	setAttr ".sp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167836e-10 ;
createNode nurbsCurve -n "lowerArmLFT_FK_Gimbal_ctrlShape" -p "lowerArmLFT_FK_Gimbal_ctrl";
	rename -uid "0820C931-41BD-F2F9-81E5-CDA24332ADA7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		0.2011660090095099 -0.67787527289837402 3.5788720106805543
		-0.51928344560784367 -0.59355862066623588 3.5566543536002624
		-1.183776191897961 -0.38001208385695334 3.4696529523351662
		-1.7741546680712741 -0.090120841028851179 3.297393096489345
		-2.2859228789342376 0.23833382299277744 3.0266306501695812
		-2.7176292660925228 0.57755585024692435 2.6499655715661894
		-3.0722577006265279 0.90540345746630069 2.170014403579601
		-3.3634718087014837 1.2047102208165319 1.6010138293879825
		-3.5949358163057927 1.4523760048598566 0.9375054550552383
		-3.7589053868600426 1.6084431105622683 0.17192619174428764
		-3.8239247048677836 1.5841727275977378 -0.69284880368485269
		-3.7589053868600426 1.3125646361560803 -1.5142219764097322
		-3.5949358163057927 0.90516614058503175 -2.1809265704395768
		-3.3634718087014837 0.44639333934709274 -2.7204719533683659
		-3.0722577006265288 -0.028758293278925956 -3.1535736943374073
		-2.7176292660925201 -0.50042712643231546 -3.4932289446175955
		-2.2859228789342336 -0.94762518793950468 -3.7318962004318648
		-1.7741546680712743 -1.3486426833739029 -3.8746538167265623
		-1.1837761918979617 -1.6798636820860564 -3.9379234035480875
		-0.51928344560784323 -1.910273312693503 -3.9470211685851271
		0.20116600900950982 -1.9971169584709556 -3.9392043074596872
		0.20116596829763755 -2.5667794937307113 -3.7691053467322204
		0.20116596829763747 -3.0809178617906916 -3.4276085629325257
		0.20116596829763747 -3.5188251883343131 -2.9441880720814462
		0.201165968297637 -3.8613674086098588 -2.3399688989854925
		0.20116596829763697 -4.0935676281156717 -1.6413672026467305
		0.20116596829763697 -4.2052816815299767 -0.87890609917017004
		0.20116596829763697 -4.1916282595939593 -0.085913255934569333
		0.20117436997769231 -3.2321683850921339 0.43922547131534129
		0.20117436997769272 -3.0514572439902841 0.96646863118931203
		0.20116596829763708 -3.4314162624634776 2.1320918652217675
		0.20116596829763708 -2.9752368876925859 2.7098994890028787
		0.20116596829763708 -2.4474420411658713 3.1613954267341913
		0.20116596829763714 -1.8711077022841189 3.4668408841255642
		0.20116596829763714 -1.2714171912971752 3.6128874722032833
		0.2011660090095099 -0.67787527289837402 3.5788720106805543
		0.92161538220311756 -0.59355862066623766 3.5566543536002637
		1.5861081284932377 -0.38000909791266801 3.4696524283737107
		2.1764866046665459 -0.090123826973129567 3.297393620450793
		2.6882568343868063 0.23833382299277356 3.0266306501695821
		3.119959183830503 0.5775528643026423 2.6499660955276441
		3.474593674936405 0.90540644341058396 2.1700138796181507
		3.7657997075821701 1.204701262983698 1.6010154012723248
		3.9972758283302472 1.4523939205255285 0.93750231128654227
		4.161227229168845 1.6084192230080265 0.17193038343588299
		4.2263131694672831 1.5843070950903433 -0.69287238195007494
		4.1612272291688432 1.3125407486018377 -1.5142177847181346
		3.9972758283302472 0.90518405625070431 -2.1809297142082733
		3.7657997075821701 0.44638438151424387 -2.7204703814840081
		3.4745936749364041 -0.028755307334649538 -3.1535742182988642
		3.1199591838305012 -0.50043011237659496 -3.4932284206561284
		2.6882568343868063 -0.94762518793950434 -3.7318962004318648
		2.1764866046665499 -1.3486456693181776 -3.8746532927651205
		1.5861081284932372 -1.6798606961417784 -3.9379239275095421
		0.92161538220311789 -1.9102733126935016 -3.9470211685851302
		0.20116600900950982 -1.9971169584709556 -3.9392043074596872
		;
createNode transform -n "handLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "B570BFD0-4507-3B6B-B4A1-AEB4948ADA1E";
createNode transform -n "handLFT_FK_ctrl" -p "handLFT_FK_Zro_grp";
	rename -uid "767AE094-4DC7-69AB-E13B-03BFE8C863BE";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
	setAttr ".sp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handLFT_FK_ctrlShape" -p "handLFT_FK_ctrl";
	rename -uid "090E4526-447D-B989-EE3F-ECBE6654E0A0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		0.28991310200090392 -1.6783690561287492 2.8263908460445708
		-0.44363585091491037 -1.6118977274463628 2.8266669243616005
		-1.1202106683948676 -1.4374840365614954 2.8047367415603226
		-1.7213236406449206 -1.1900308229008258 2.7350888367838144
		-2.2423970245001592 -0.89474563437235377 2.6005161872145375
		-2.681952868754665 -0.57063635797361367 2.3900853035473144
		-3.0430292984186491 -0.23452363477310353 2.1013541649855991
		-3.3395383771383389 0.098142818526121167 1.7414190620716103
		-3.575210955315276 0.41142991366673876 1.3017028037534457
		-3.7421618857646699 0.67740655871258715 0.76875225342367792
		-3.8083634108518223 0.83016153847668606 0.12717571671152722
		-3.7421618857646699 0.79222281180615994 -0.53124298694208683
		-3.5752109553152769 0.62377583169261808 -1.1025620568997292
		-3.3395383771383402 0.39240925058971432 -1.5903824100623736
		-3.0430292984186491 0.12797976199869737 -2.0030533358905553
		-2.6819528687546623 -0.15232283743323802 -2.3462265950820504
		-2.2423970245001574 -0.43453179072899706 -2.6102078188999371
		-1.7213236406449206 -0.70165882265821833 -2.7944530071385243
		-1.120210668394868 -0.93307393918659987 -2.9063948109157804
		-0.44363585091491037 -1.1009438716944635 -2.9585556606556511
		0.28991310200090392 -1.1664345953124071 -2.9699345391609251
		0.28991306054879212 -1.6194745118719178 -2.95707887050545
		0.28991306054879212 -2.0654466313236197 -2.807056940645396
		0.28991306054879212 -2.4832877192591489 -2.5374867547579005
		0.28991306054879168 -2.8547400392197599 -2.1601486885213759
		0.28991306054879168 -3.1635630570731328 -1.6915395517207004
		0.28991306054879168 -3.3962645444927015 -1.1521338977332318
		0.28991306054879168 -3.5426742829444415 -0.56550984818094285
		0.28991306054879168 -3.5963912257684623 0.04269472318159534
		0.28991306054879251 -3.5550677825275172 0.64589946459643877
		0.28991306054879168 -3.4205122621059005 1.2177414477744819
		0.28991306054879168 -3.1986048180542821 1.7332249739163186
		0.28991306054879168 -2.8990401623267332 2.1698276070669502
		0.28991306054879168 -2.534915962432827 2.5084613722738327
		0.28991306054879168 -2.1221425287412532 2.7343281542619149
		0.28991310200090392 -1.6783690561287492 2.8263908460445708
		1.0234619720124942 -1.6118977274463653 2.8266669243616005
		1.7000367894924504 -1.4374817344427187 2.8047369448846418
		2.3011497617425016 -1.1900331250195975 2.7350886334594935
		2.8222252011627007 -0.89474563437235644 2.6005161872145384
		3.2617769342872913 -0.57063866009239061 2.390085100222997
		3.6228595306461577 -0.23452133265432856 2.1013543683099232
		3.9193603871059994 0.098135912169807854 1.741418452098638
		4.1550452986727002 0.41144372637937093 1.3017040236993811
		4.3219777290374557 0.67738814176240114 0.76875062682909678
		4.3882470877682733 0.83026513382147382 0.12718486630605197
		4.3219777290374539 0.79220439485597549 -0.53124461353666885
		4.1550452986727002 0.62378964440524953 -1.102560836953794
		3.9193603871059994 0.39240234423338727 -1.5903830200353384
		3.6228595306461577 0.12798206411747065 -2.0030531325662402
		3.2617769342872895 -0.15232513955201565 -2.3462267984063585
		2.8222252011627007 -0.43453179072899706 -2.6102078188999371
		2.3011497617425043 -0.70166112477698661 -2.7944532104628523
		1.7000367894924504 -0.93307163706782503 -2.9063946075914635
		1.0234619720124942 -1.1009438716944617 -2.9585556606556502
		0.28991310200090392 -1.1664345953124071 -2.9699345391609251
		;
createNode transform -n "handLFT_FK_Gimbal_ctrl" -p "handLFT_FK_ctrl";
	rename -uid "2B08827F-4F3D-B113-C8FA-D592DBC64AD1";
	setAttr ".rp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
	setAttr ".sp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
createNode nurbsCurve -n "handLFT_FK_Gimbal_ctrlShape" -p "handLFT_FK_Gimbal_ctrl";
	rename -uid "F7BDA84A-45F7-A275-C7D3-468A926711F7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		0.24642613607511099 -1.4266136974198509 2.4024322213173472
		-0.37709047390333117 -1.3701130680398224 2.4026668878868227
		-0.95217906876129454 -1.2218614307876852 2.3840262325057364
		-1.4631250951738397 -1.0115261991761157 2.3248255134457052
		-1.9060374714507922 -0.7605337889269147 2.2104387613118193
		-2.2796599390671228 -0.48504090398798549 2.0315725101946795
		-2.5865749042815089 -0.1993450892675519 1.7861510424172216
		-2.8386076211932449 0.083421396036789053 1.4802062049403313
		-3.0389293126436421 0.34971542690631408 1.1064473853698913
		-3.1808376035256263 0.57579557519528513 0.65343941758958868
		-3.2371088998497064 0.70563730799476931 0.10809936138426057
		-3.1808376035256263 0.67338939032482215 -0.45155653672131146
		-3.0389293126436434 0.53020945722831159 -0.93717774618530714
		-2.8386076211932467 0.33354786329084324 -1.3518250463735551
		-2.5865749042815089 0.10878279798847883 -1.7025953333275095
		-2.2796599390671206 -0.12947441152866623 -1.9942926036402804
		-1.9060374714507908 -0.36935202183006138 -2.2186766438854839
		-1.4631250951738397 -0.59640999896989944 -2.375285053888283
		-0.95217906876129488 -0.7931128480190236 -2.4704355870989509
		-0.37709047390333117 -0.93580229065070775 -2.5147723093778409
		0.24642613607511099 -0.99146940572595976 -2.5244443561073235
		0.24642610084081595 -1.3765533348015442 -2.5135170377501703
		0.24642610084081595 -1.7556296363354906 -2.3859983973691237
		0.24642610084081595 -2.1107945610806911 -2.156863739364753
		0.24642610084081559 -2.4265290330472098 -1.8361263830637069
		0.24642610084081559 -2.6890285982225763 -1.4378086167831325
		0.24642610084081559 -2.8868248625292101 -0.97931381089378478
		0.24642610084081559 -3.0112731402131896 -0.48068336877433898
		0.24642610084081559 -3.0569325416136062 0.036290516883818465
		0.24642610084081626 -3.0218076148588038 0.54901454708643538
		0.24642610084081559 -2.9074354225004289 1.0350802327877722
		0.24642610084081559 -2.7188140950565534 1.4732412300083331
		0.24642610084081559 -2.4641841376881368 1.8443534681863698
		0.24642610084081559 -2.1546785677783173 2.1321921686122196
		0.24642610084081559 -1.8038211491404788 2.3241789333020901
		0.24642613607511099 -1.4266136974198509 2.4024322213173472
		0.86994267558496274 -1.3701130680398246 2.4026668878868227
		1.4450312704429258 -1.221859473986725 2.384026405331408
		1.9559772968554689 -1.0115281559770717 2.3248253406200314
		2.3988914203626379 -0.76053378892691692 2.2104387613118197
		2.77251039351854 -0.48504286078894587 2.0315723373690102
		3.079430600423577 -0.19934313246659316 1.7861512152428967
		3.3314563284144416 0.083415525633922752 1.4802056864633049
		3.5317885032461369 0.34972716771205142 1.1064484223239364
		3.6736810690561796 0.57577992078762696 0.6534380349841945
		3.7300100239773744 0.7057253640378387 0.10810713853960659
		3.6736810690561783 0.67337373591716532 -0.45155791932670608
		3.5317885032461369 0.53022119803404832 -0.93717670923126239
		3.3314563284144416 0.33354199288796527 -1.3518255648505753
		3.079430600423577 0.10878475478943612 -1.7025951605018419
		2.7725103935185387 -0.12947636832962722 -1.9942927764659422
		2.3988914203626379 -0.36935202183006138 -2.2186766438854839
		1.9559772968554712 -0.59641195577085249 -2.3752852267139621
		1.4450312704429258 -0.79311089121806522 -2.4704354142732816
		0.86994267558496285 -0.9358022906507063 -2.5147723093778405
		0.24642613607511099 -0.99146940572595976 -2.5244443561073235
		;
createNode transform -n "shoulderRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "7D4A8AEA-45CF-252F-0270-04AC01F5F5DB";
createNode transform -n "shoulderRGT_FK_ctrl" -p "shoulderRGT_FK_Zro_grp";
	rename -uid "1DDB4059-4262-6FF5-FD2C-C4B59490DE21";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -1.2579117320701207e-05 0.00020498838092367557 2.2795634506863234e-07 ;
	setAttr ".sp" -type "double3" -1.2579117320701207e-05 0.00020498838092367557 2.2795634506863234e-07 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "shoulderRGT_FK_ctrlShape" -p "shoulderRGT_FK_ctrl";
	rename -uid "A2E7A3F6-42B6-26C9-54CB-61A3A317362A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-1.2579117320701207e-05 -1.5399339446720473 -9.017297582401401
		-1.2579117320701207e-05 -1.0265543003210549 -7.990538293699414
		-1.2579117320701207e-05 0.0002049883809312323 -7.4771586493484188
		-1.2579117320701207e-05 1.0269642770829184 -7.9905382936994114
		-1.2579117320701207e-05 1.540343921433913 -9.0172975824013974
		-1.2579117320701207e-05 1.0269642770829206 -10.044056871103383
		-1.2579117320701207e-05 0.00020498838093434534 -10.557436515454377
		-1.2579117320701207e-05 -1.0265543003210529 -10.044056871103386
		-1.2579117320701207e-05 -1.5399339446720473 -9.017297582401401
		-1.0267718678193074 -1.026554300321054 -9.017297582401401
		-1.5401515121703027 0.00020498838093278884 -9.0172975824013992
		-1.0267718678193074 1.0269642770829195 -9.0172975824013974
		-1.2579117320701207e-05 1.540343921433913 -9.0172975824013974
		1.0267467095846661 1.0269642770829195 -9.0172975824013974
		1.5401263539356593 0.00020498838093278884 -9.0172975824013992
		1.0267467095846661 -1.026554300321054 -9.017297582401401
		-1.2579117320701207e-05 -1.5399339446720473 -9.017297582401401
		;
createNode transform -n "shoulderRGT_FK_Gimbal_ctrl" -p "shoulderRGT_FK_ctrl";
	rename -uid "7BF4C7AC-4252-1AA8-4194-0A8357507771";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -1.2579117320701207e-05 0.00020498838092367557 2.2795634506863234e-07 ;
	setAttr ".sp" -type "double3" -1.2579117320701207e-05 0.00020498838092367557 2.2795634506863234e-07 ;
createNode nurbsCurve -n "shoulderRGT_FK_Gimbal_ctrlShape" -p "shoulderRGT_FK_Gimbal_ctrl";
	rename -uid "D039B18A-4D7F-4DF2-E748-75AB47DCC0B4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-1.2579117320701207e-05 -1.3089131047141018 -7.6647029108477387
		-1.2579117320701207e-05 -0.87254040701575819 -6.7919575154510499
		-1.2579117320701207e-05 0.00020498838093009882 -6.3555848177527041
		-1.2579117320701207e-05 0.87295038377761924 -6.7919575154510481
		-1.2579117320701207e-05 1.3093230814759644 -7.6647029108477343
		-1.2579117320701207e-05 0.87295038377762113 -8.5374483062444231
		-1.2579117320701207e-05 0.0002049883809327449 -8.9738210039427706
		-1.2579117320701207e-05 -0.87254040701575641 -8.5374483062444266
		-1.2579117320701207e-05 -1.3089131047141018 -7.6647029108477387
		-0.87275797451400927 -0.87254040701575752 -7.6647029108477387
		-1.3091306722123552 0.00020498838093142187 -7.6647029108477378
		-0.87275797451400927 0.87295038377762013 -7.6647029108477343
		-1.2579117320701207e-05 1.3093230814759644 -7.6647029108477343
		0.87273281627936805 0.87295038377762013 -7.6647029108477343
		1.3091055139777124 0.00020498838093142187 -7.6647029108477378
		0.87273281627936805 -0.87254040701575752 -7.6647029108477387
		-1.2579117320701207e-05 -1.3089131047141018 -7.6647029108477387
		;
createNode transform -n "shoulderLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "EEB6992A-4E6D-61EA-613F-FA822AFA84BA";
createNode transform -n "shoulderLFT_FK_ctrl" -p "shoulderLFT_FK_Zro_grp";
	rename -uid "F6AD04B9-4EEC-A011-2932-D8ABAFA6DCC4";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" 8.6215869296654414e-09 -5.266550590230743e-09 -5.8162966094266901e-09 ;
	setAttr ".sp" -type "double3" 8.6215869296654414e-09 -5.266550590230743e-09 -5.8162966094266901e-09 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "shoulderLFT_FK_ctrlShape" -p "shoulderLFT_FK_ctrl";
	rename -uid "2F1D1E3E-48DC-DBE7-AC48-BCBB3E8434F9";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		8.6215869296654414e-09 1.5401389277864295 9.0172978045414478
		8.6215869296654414e-09 1.0267592834354362 7.99053851583946
		8.6215869296654414e-09 -5.266550590230743e-09 7.4771588714884674
		8.6215869296654414e-09 -1.0267592939685373 7.99053851583946
		8.6215869296654414e-09 -1.5401389383195307 9.0172978045414478
		8.6215869296654414e-09 -1.0267592939685373 10.044057093243431
		8.6215869296654414e-09 -5.266550590230743e-09 10.557436737594426
		8.6215869296654414e-09 1.0267592834354362 10.044057093243431
		8.6215869296654414e-09 1.5401389277864295 9.0172978045414478
		1.0267592973235737 1.0267592834354362 9.0172978045414478
		1.540138941674567 -5.266550590230743e-09 9.0172978045414478
		1.0267592973235737 -1.0267592939685373 9.0172978045414478
		8.6215869296654414e-09 -1.5401389383195307 9.0172978045414478
		-1.0267592800803997 -1.0267592939685373 9.0172978045414478
		-1.5401389244313932 -5.266550590230743e-09 9.0172978045414478
		-1.0267592800803997 1.0267592834354362 9.0172978045414478
		8.6215869296654414e-09 1.5401389277864295 9.0172978045414478
		;
createNode transform -n "shoulderLFT_FK_Gimbal_ctrl" -p "shoulderLFT_FK_ctrl";
	rename -uid "C62E3020-4988-94C0-8665-31BB11D53090";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" 8.6215869296654414e-09 -5.266550590230743e-09 -5.8162966094266901e-09 ;
	setAttr ".sp" -type "double3" 8.6215869296654414e-09 -5.266550590230743e-09 -5.8162966094266901e-09 ;
createNode nurbsCurve -n "shoulderLFT_FK_Gimbal_ctrlShape" -p "shoulderLFT_FK_Gimbal_ctrl";
	rename -uid "3510EAF1-492C-8367-C596-6D8331607911";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		8.6215869296654414e-09 1.3091180878284825 7.6647031329877864
		8.6215869296654414e-09 0.87274539013013808 6.7919577375910976
		8.6215869296654414e-09 -5.266550590230743e-09 6.3555850398927527
		8.6215869296654414e-09 -0.87274540066323925 6.7919577375910976
		8.6215869296654414e-09 -1.3091180983615835 7.6647031329877864
		8.6215869296654414e-09 -0.87274540066323925 8.5374485283844734
		8.6215869296654414e-09 -5.266550590230743e-09 8.9738212260828174
		8.6215869296654414e-09 0.87274539013013808 8.5374485283844734
		8.6215869296654414e-09 1.3091180878284825 7.6647031329877864
		0.87274540401827561 0.87274539013013808 7.6647031329877864
		1.30911810171662 -5.266550590230743e-09 7.6647031329877864
		0.87274540401827561 -0.87274540066323925 7.6647031329877864
		8.6215869296654414e-09 -1.3091180983615835 7.6647031329877864
		-0.87274538677510172 -0.87274540066323925 7.6647031329877864
		-1.309118084473446 -5.266550590230743e-09 7.6647031329877864
		-0.87274538677510172 0.87274539013013808 7.6647031329877864
		8.6215869296654414e-09 1.3091180878284825 7.6647031329877864
		;
createNode transform -n "lowerArmRGT_prop_Zro_grp" -p "TMP_GRP";
	rename -uid "5282B0F8-4427-DF29-4A04-1FA496062BB3";
createNode transform -n "lowerArmRGT_prop_ctrl" -p "lowerArmRGT_prop_Zro_grp";
	rename -uid "BDFF924F-4F89-6265-1EDE-E2BB3734728A";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 -1.4591127079228084e-14 0 ;
	setAttr ".sp" -type "double3" 0 -1.4591127079228084e-14 0 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmRGT_prop_ctrlShape" -p "lowerArmRGT_prop_ctrl";
	rename -uid "B7990FA8-437B-C7ED-15E6-1D95F6DBE1D0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-3.1838105772299325 3.1838105772299174 -3.1838105772299325
		-3.1838105772299325 3.1838105772299174 3.1838105772299325
		3.1838105772299325 3.1838105772299174 3.1838105772299325
		3.1838105772299325 3.1838105772299174 -3.1838105772299325
		-3.1838105772299325 3.1838105772299174 -3.1838105772299325
		-3.1838105772299325 -3.1838105772299468 -3.1838105772299325
		-3.1838105772299325 -3.1838105772299468 3.1838105772299325
		3.1838105772299325 -3.1838105772299468 3.1838105772299325
		3.1838105772299325 3.1838105772299174 3.1838105772299325
		-3.1838105772299325 3.1838105772299174 3.1838105772299325
		-3.1838105772299325 -3.1838105772299468 3.1838105772299325
		-3.1838105772299325 -3.1838105772299468 -3.1838105772299325
		3.1838105772299325 -3.1838105772299468 -3.1838105772299325
		3.1838105772299325 3.1838105772299174 -3.1838105772299325
		3.1838105772299325 3.1838105772299174 3.1838105772299325
		3.1838105772299325 -3.1838105772299468 3.1838105772299325
		3.1838105772299325 -3.1838105772299468 -3.1838105772299325
		;
createNode transform -n "lowerArmRGT_prop_Gimbal_ctrl" -p "lowerArmRGT_prop_ctrl";
	rename -uid "BAFF0A3D-48ED-E816-4225-ACBE41F67198";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 -1.4591127079228084e-14 0 ;
	setAttr ".sp" -type "double3" 0 -1.4591127079228084e-14 0 ;
createNode nurbsCurve -n "lowerArmRGT_prop_Gimbal_ctrlShape" -p "lowerArmRGT_prop_Gimbal_ctrl";
	rename -uid "B5D04143-4E88-EDEF-1586-CF9C663C1451";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-2.7062389906454425 2.7062389906454278 -2.7062389906454425
		-2.7062389906454425 2.7062389906454278 2.7062389906454425
		2.7062389906454425 2.7062389906454278 2.7062389906454425
		2.7062389906454425 2.7062389906454278 -2.7062389906454425
		-2.7062389906454425 2.7062389906454278 -2.7062389906454425
		-2.7062389906454425 -2.7062389906454571 -2.7062389906454425
		-2.7062389906454425 -2.7062389906454571 2.7062389906454425
		2.7062389906454425 -2.7062389906454571 2.7062389906454425
		2.7062389906454425 2.7062389906454278 2.7062389906454425
		-2.7062389906454425 2.7062389906454278 2.7062389906454425
		-2.7062389906454425 -2.7062389906454571 2.7062389906454425
		-2.7062389906454425 -2.7062389906454571 -2.7062389906454425
		2.7062389906454425 -2.7062389906454571 -2.7062389906454425
		2.7062389906454425 2.7062389906454278 -2.7062389906454425
		2.7062389906454425 2.7062389906454278 2.7062389906454425
		2.7062389906454425 -2.7062389906454571 2.7062389906454425
		2.7062389906454425 -2.7062389906454571 -2.7062389906454425
		;
createNode transform -n "handRGT_prop_Zro_grp" -p "TMP_GRP";
	rename -uid "1BC05DF4-4896-8AE1-8AFE-BEA1A429204B";
createNode transform -n "handRGT_prop_ctrl" -p "handRGT_prop_Zro_grp";
	rename -uid "92686B69-4F3F-96AD-7658-61A5E49ECB34";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 1.0838178593707361e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707361e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handRGT_prop_ctrlShape" -p "handRGT_prop_ctrl";
	rename -uid "9693ABE1-4099-067D-0EB0-A3BD5DD3D6BF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1.565366 3.1307580000000002 4.6961259999999996 6.2614869999999998 7.8268849999999999
		 9.3922439999999998 15.392244 16.957602000000001 18.523 20.088360999999999 21.653728999999998
		 23.219121000000001 24.784486999999999 30.784486999999999 32.349851999999998 33.915246000000003
		 35.480611000000003 37.045976000000003 38.611370000000001 40.176735000000001 41.742100000000001
		 43.307493999999998 44.872858999999998 46.438223999999998 48.003618000000003 49.568983000000003
		 55.568983000000003 57.134349 58.699741000000003 60.265109000000002 61.830469999999998
		 63.395868 64.961225999999996 70.961225999999996 72.526584 74.091982000000002 75.657342999999997
		 77.222712000000001 78.788104000000004 80.353470000000002 86.353470000000002 87.918834000000004
		 89.484228999999999 91.049593999999999 92.614958999999999 94.180352999999997 95.745717999999997
		 101.745718 107.745718 109.311083 110.87647699999999 112.44184199999999 114.00720699999999
		 115.57260100000001 117.13796600000001
		56
		1.0734336049503648 -4.9300622789913673 -4.9230098672712526e-06
		1.0359166500749177 -4.9300622789913673 -0.27753097250316772
		0.92874277713087006 -4.9300622789913673 -0.53626740452143085
		0.75902904932485249 -4.9300622789913673 -0.75903541849106149
		0.53625996671406373 -4.9300622789913673 -0.92874596564445089
		0.27752216310398042 -4.9300622789913673 -1.0359191801641592
		-3.9930884211852243e-06 -4.9300622789913673 -1.0734242068341293
		-3.9930884211852243e-06 4.9483820237706322 -1.0734242068341293
		0.27752216310398042 4.9483820237706322 -1.0359191801641592
		0.53625996671406373 4.9483820237706322 -0.92874596564445089
		0.75902904932485249 4.9483820237706322 -0.75903541849106149
		0.92874277713087006 4.9483820237706322 -0.53626740452143085
		1.0359166500749177 4.9483820237706322 -0.27753097250316772
		1.0734336049503648 4.9483820237706322 -4.9230098672712526e-06
		1.0734336049503648 -4.9300622789913673 -4.9230098672712526e-06
		1.0359192752695403 -4.9300622789913673 0.2775211640030118
		0.92874784979031788 -4.9300622789913673 0.53625896760463354
		0.75903622921179026 -4.9300622789913673 0.75902787131645066
		0.53626875195515167 -4.9300622789913673 0.92874177802397773
		0.27753196212879128 -4.9300622789913673 1.035915650969718
		6.1607630618508252e-06 -4.9300622789913673 1.0734326058439911
		-0.27751999547333955 -4.9300622789913673 1.0359182761634942
		-0.53625779907496152 -4.9300622789913673 0.92874685068427187
		-0.75902688169167343 -4.9300622789913673 0.75903505120254233
		-0.92874060949430515 -4.9300622789913673 0.53626775284910611
		-1.0359144824400457 -4.9300622789913673 0.27753096302274571
		-1.0734314373139913 -4.9300622789913673 5.2308805387129439e-06
		-1.0734314373139913 4.9483820237706322 5.2308805387129439e-06
		-1.0359171076346678 4.9483820237706322 -0.27752117348343375
		-0.92874568215375297 4.9483820237706322 -0.53625861927695839
		-0.75903406157861109 4.9483820237706322 -0.75902823860497004
		-0.53626658431604934 4.9483820237706322 -0.92874089298415674
		-0.27752979449815046 4.9483820237706322 -1.035916554970383
		-3.9930884211852243e-06 4.9483820237706322 -1.0734242068341293
		-3.9930884211852243e-06 -4.9300622789913673 -1.0734242068341293
		-0.27752979449815046 -4.9300622789913673 -1.035916554970383
		-0.53626658431604934 -4.9300622789913673 -0.92874089298415674
		-0.75903406157861109 -4.9300622789913673 -0.75902823860497004
		-0.92874568215375297 -4.9300622789913673 -0.53625861927695839
		-1.0359171076346678 -4.9300622789913673 -0.27752117348343375
		-1.0734314373139913 -4.9300622789913673 5.2308805387129439e-06
		-1.0734314373139913 4.9483820237706322 5.2308805387129439e-06
		-1.0359144824400457 4.9483820237706322 0.27753096302274571
		-0.92874060949430515 4.9483820237706322 0.53626775284910611
		-0.75902688169167343 4.9483820237706322 0.75903505120254233
		-0.53625779907496152 4.9483820237706322 0.92874685068427187
		-0.27751999547333955 4.9483820237706322 1.0359182761634942
		6.1607630618508252e-06 4.9483820237706322 1.0734326058439911
		6.1607630618508252e-06 -4.9300622789913673 1.0734326058439911
		6.1607630618508252e-06 4.9483820237706322 1.0734326058439911
		0.27753196212879128 4.9483820237706322 1.035915650969718
		0.53626875195515167 4.9483820237706322 0.92874177802397773
		0.75903622921179026 4.9483820237706322 0.75902787131645066
		0.92874784979031788 4.9483820237706322 0.53625896760463354
		1.0359192752695403 4.9483820237706322 0.2775211640030118
		1.0734336049503648 4.9483820237706322 -4.9230098672712526e-06
		;
createNode transform -n "handRGT_prop_Gimbal_ctrl" -p "handRGT_prop_ctrl";
	rename -uid "7817331C-414B-89A4-7AD6-EBA8471E886F";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 1.0838178593707364e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707364e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
createNode nurbsCurve -n "handRGT_prop_Gimbal_ctrlShape" -p "handRGT_prop_Gimbal_ctrl";
	rename -uid "44A4D37B-4750-1504-1FCD-41B2497DA2CA";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1.565366 3.1307580000000002 4.6961259999999996 6.2614869999999998 7.8268849999999999
		 9.3922439999999998 15.392244 16.957602000000001 18.523 20.088360999999999 21.653728999999998
		 23.219121000000001 24.784486999999999 30.784486999999999 32.349851999999998 33.915246000000003
		 35.480611000000003 37.045976000000003 38.611370000000001 40.176735000000001 41.742100000000001
		 43.307493999999998 44.872858999999998 46.438223999999998 48.003618000000003 49.568983000000003
		 55.568983000000003 57.134349 58.699741000000003 60.265109000000002 61.830469999999998
		 63.395868 64.961225999999996 70.961225999999996 72.526584 74.091982000000002 75.657342999999997
		 77.222712000000001 78.788104000000004 80.353470000000002 86.353470000000002 87.918834000000004
		 89.484228999999999 91.049593999999999 92.614958999999999 94.180352999999997 95.745717999999997
		 101.745718 107.745718 109.311083 110.87647699999999 112.44184199999999 114.00720699999999
		 115.57260100000001 117.13796600000001
		56
		0.91241872678048896 -4.1905528379911603 -4.1718516151862415e-06
		0.88052931513635913 -4.1905528379911603 -0.23590131392092056
		0.78943152313391851 -4.1905528379911603 -0.45582728113644422
		0.64517485449880352 -4.1905528379911603 -0.64518009301063028
		0.45582113427963306 -4.1905528379911603 -0.7894340580910113
		0.23589400121106227 -4.1905528379911603 -0.88053129043276324
		-3.2315524791018301e-06 -4.1905528379911603 -0.91241056310223778
		-3.2315524791018301e-06 4.206124819356539 -0.91241056310223778
		0.23589400121106227 4.206124819356539 -0.88053129043276324
		0.45582113427963306 4.206124819356539 -0.7894340580910113
		0.64517485449880352 4.206124819356539 -0.64518009301063028
		0.78943152313391851 4.206124819356539 -0.45582728113644422
		0.88052931513635913 4.206124819356539 -0.23590131392092056
		0.91241872678048896 4.206124819356539 -4.1718516151862415e-06
		0.91241872678048896 -4.1905528379911603 -4.1718516151862415e-06
		0.88053154655178811 -4.1905528379911603 0.23589300210933198
		0.78943583489444902 -4.1905528379911603 0.45582013517071052
		0.64518095740270054 -4.1905528379911603 0.64517370332575508
		0.4558286017345578 -4.1905528379911603 0.78943052402715297
		0.2359023303821515 -4.1905528379911603 0.88052831603103243
		5.399221281478812e-06 -4.1905528379911603 0.91241772767416451
		-0.23589183357965968 -4.1905528379911603 0.880530547445742
		-0.45581896664103827 -4.1905528379911603 0.7894348357884029
		-0.64517268686524354 -4.1905528379911603 0.64517980622893301
		-0.78942935549748039 -4.1905528379911603 0.45582760262851207
		-0.88052714750135974 -4.1905528379911603 0.23590133127610588
		-0.91241655914421371 -4.1905528379911603 4.4589552299003258e-06
		-0.91241655914421371 4.206124819356539 4.4589552299003258e-06
		-0.88052937891678884 4.206124819356539 -0.23589298475414672
		-0.78943366725801112 4.206124819356539 -0.4558198136786426
		-0.64517878976914056 4.206124819356539 -0.64517399010745247
		-0.45582643409596302 4.206124819356539 -0.78942974632976137
		-0.23590016275074899 4.206124819356539 -0.88052905901805378
		-3.2315524791018301e-06 4.206124819356539 -0.91241056310223778
		-3.2315524791018301e-06 -4.1905528379911603 -0.91241056310223778
		-0.23590016275074899 -4.1905528379911603 -0.88052905901805378
		-0.45582643409596302 -4.1905528379911603 -0.78942974632976137
		-0.64517878976914056 -4.1905528379911603 -0.64517399010745247
		-0.78943366725801112 -4.1905528379911603 -0.4558198136786426
		-0.88052937891678884 -4.1905528379911603 -0.23589298475414672
		-0.91241655914421371 -4.1905528379911603 4.4589552299003258e-06
		-0.91241655914421371 4.206124819356539 4.4589552299003258e-06
		-0.88052714750135974 4.206124819356539 0.23590133127610588
		-0.78942935549748039 4.206124819356539 0.45582760262851207
		-0.64517268686524354 4.206124819356539 0.64517980622893301
		-0.45581896664103827 4.206124819356539 0.7894348357884029
		-0.23589183357965968 4.206124819356539 0.880530547445742
		5.399221281478812e-06 4.206124819356539 0.91241772767416451
		5.399221281478812e-06 -4.1905528379911603 0.91241772767416451
		5.399221281478812e-06 4.206124819356539 0.91241772767416451
		0.2359023303821515 4.206124819356539 0.88052831603103243
		0.4558286017345578 4.206124819356539 0.78943052402715297
		0.64518095740270054 4.206124819356539 0.64517370332575508
		0.78943583489444902 4.206124819356539 0.45582013517071052
		0.88053154655178811 4.206124819356539 0.23589300210933198
		0.91241872678048896 4.206124819356539 -4.1718516151862415e-06
		;
createNode transform -n "lowerArmLFT_prop_Zro_grp" -p "TMP_GRP";
	rename -uid "EAEB45D1-45F4-264C-DD11-118AE00966DD";
createNode transform -n "lowerArmLFT_prop_ctrl" -p "lowerArmLFT_prop_Zro_grp";
	rename -uid "BF8F1678-47A8-467F-8BC4-6E81025A2B66";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 0 9.1194544245175543e-16 ;
	setAttr ".sp" -type "double3" 0 0 9.1194544245175543e-16 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmLFT_prop_ctrlShape" -p "lowerArmLFT_prop_ctrl";
	rename -uid "202A8B40-4705-AF59-5F30-D6ABA5ED5C9B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-3.1838105772299325 3.1838105772299321 -3.1838105772299317
		-3.1838105772299325 3.1838105772299321 3.1838105772299339
		3.1838105772299325 3.1838105772299321 3.1838105772299339
		3.1838105772299325 3.1838105772299321 -3.1838105772299317
		-3.1838105772299325 3.1838105772299321 -3.1838105772299317
		-3.1838105772299325 -3.1838105772299321 -3.1838105772299317
		-3.1838105772299325 -3.1838105772299321 3.1838105772299339
		3.1838105772299325 -3.1838105772299321 3.1838105772299339
		3.1838105772299325 3.1838105772299321 3.1838105772299339
		-3.1838105772299325 3.1838105772299321 3.1838105772299339
		-3.1838105772299325 -3.1838105772299321 3.1838105772299339
		-3.1838105772299325 -3.1838105772299321 -3.1838105772299317
		3.1838105772299325 -3.1838105772299321 -3.1838105772299317
		3.1838105772299325 3.1838105772299321 -3.1838105772299317
		3.1838105772299325 3.1838105772299321 3.1838105772299339
		3.1838105772299325 -3.1838105772299321 3.1838105772299339
		3.1838105772299325 -3.1838105772299321 -3.1838105772299317
		;
createNode transform -n "lowerArmLFT_prop_Gimbal_ctrl" -p "lowerArmLFT_prop_ctrl";
	rename -uid "8EC21CA2-4F6C-463A-4EC3-C08FC90336A3";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 0 9.1194544245175543e-16 ;
	setAttr ".sp" -type "double3" 0 0 9.1194544245175543e-16 ;
createNode nurbsCurve -n "lowerArmLFT_prop_Gimbal_ctrlShape" -p "lowerArmLFT_prop_Gimbal_ctrl";
	rename -uid "D83F4200-405F-7963-CD78-CB8FD103A389";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-2.7062389906454425 2.706238990645442 -2.7062389906454416
		-2.7062389906454425 2.706238990645442 2.7062389906454443
		2.7062389906454425 2.706238990645442 2.7062389906454443
		2.7062389906454425 2.706238990645442 -2.7062389906454416
		-2.7062389906454425 2.706238990645442 -2.7062389906454416
		-2.7062389906454425 -2.706238990645442 -2.7062389906454416
		-2.7062389906454425 -2.706238990645442 2.7062389906454443
		2.7062389906454425 -2.706238990645442 2.7062389906454443
		2.7062389906454425 2.706238990645442 2.7062389906454443
		-2.7062389906454425 2.706238990645442 2.7062389906454443
		-2.7062389906454425 -2.706238990645442 2.7062389906454443
		-2.7062389906454425 -2.706238990645442 -2.7062389906454416
		2.7062389906454425 -2.706238990645442 -2.7062389906454416
		2.7062389906454425 2.706238990645442 -2.7062389906454416
		2.7062389906454425 2.706238990645442 2.7062389906454443
		2.7062389906454425 -2.706238990645442 2.7062389906454443
		2.7062389906454425 -2.706238990645442 -2.7062389906454416
		;
createNode transform -n "handLFT_prop_Zro_grp" -p "TMP_GRP";
	rename -uid "049A1759-48F0-24C0-D029-649A3A9A1B02";
createNode transform -n "handLFT_prop_ctrl" -p "handLFT_prop_Zro_grp";
	rename -uid "76B2D423-4A4B-FFC7-7790-85A2BB0189A3";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.0838178593707357e-06 6.6101001125733549e-07 8.4711813181491256e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707357e-06 6.6101001125733549e-07 8.4711813181491256e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handLFT_prop_ctrlShape" -p "handLFT_prop_ctrl";
	rename -uid "9E2064D6-4BCE-3224-4955-1C9CD71391FF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1.565366 3.1307580000000002 4.6961259999999996 6.2614869999999998 7.8268849999999999
		 9.3922439999999998 15.392244 16.957602000000001 18.523 20.088360999999999 21.653728999999998
		 23.219121000000001 24.784486999999999 30.784486999999999 32.349851999999998 33.915246000000003
		 35.480611000000003 37.045976000000003 38.611370000000001 40.176735000000001 41.742100000000001
		 43.307493999999998 44.872858999999998 46.438223999999998 48.003618000000003 49.568983000000003
		 55.568983000000003 57.134349 58.699741000000003 60.265109000000002 61.830469999999998
		 63.395868 64.961225999999996 70.961225999999996 72.526584 74.091982000000002 75.657342999999997
		 77.222712000000001 78.788104000000004 80.353470000000002 86.353470000000002 87.918834000000004
		 89.484228999999999 91.049593999999999 92.614958999999999 94.180352999999997 95.745717999999997
		 101.745718 107.745718 109.311083 110.87647699999999 112.44184199999999 114.00720699999999
		 115.57260100000001 117.13796600000001
		56
		1.0734336049503643 -4.9300622789913655 -4.9230098673852454e-06
		1.0359166500749173 -4.9300622789913655 -0.27753097250316777
		0.92874277713086961 -4.9300622789913655 -0.53626740452143085
		0.75902904932485216 -4.9300622789913655 -0.75903541849106149
		0.5362599667140634 -4.9300622789913655 -0.92874596564445089
		0.27752216310398026 -4.9300622789913655 -1.0359191801641592
		-3.9930884211852226e-06 -4.9300622789913655 -1.0734242068341293
		-3.9930884211852226e-06 4.9483820237706304 -1.0734242068341293
		0.27752216310398026 4.9483820237706304 -1.0359191801641592
		0.5362599667140634 4.9483820237706304 -0.92874596564445089
		0.75902904932485216 4.9483820237706304 -0.75903541849106149
		0.92874277713086961 4.9483820237706304 -0.53626740452143085
		1.0359166500749173 4.9483820237706304 -0.27753097250316777
		1.0734336049503643 4.9483820237706304 -4.9230098673852454e-06
		1.0734336049503643 -4.9300622789913655 -4.9230098673852454e-06
		1.0359192752695396 -4.9300622789913655 0.27752116400301163
		0.92874784979031733 -4.9300622789913655 0.53625896760463332
		0.75903622921178993 -4.9300622789913655 0.75902787131645044
		0.53626875195515133 -4.9300622789913655 0.92874177802397728
		0.27753196212879111 -4.9300622789913655 1.0359156509697178
		6.1607630618508227e-06 -4.9300622789913655 1.0734326058439909
		-0.27751999547333944 -4.9300622789913655 1.0359182761634937
		-0.53625779907496118 -4.9300622789913655 0.92874685068427154
		-0.75902688169167298 -4.9300622789913655 0.75903505120254211
		-0.92874060949430448 -4.9300622789913655 0.53626775284910588
		-1.035914482440045 -4.9300622789913655 0.27753096302274555
		-1.0734314373139906 -4.9300622789913655 5.2308805385989485e-06
		-1.0734314373139906 4.9483820237706304 5.2308805385989485e-06
		-1.0359171076346674 4.9483820237706304 -0.2775211734834338
		-0.92874568215375242 4.9483820237706304 -0.53625861927695839
		-0.75903406157861075 4.9483820237706304 -0.75902823860496993
		-0.53626658431604912 4.9483820237706304 -0.92874089298415674
		-0.27752979449815035 4.9483820237706304 -1.035916554970383
		-3.9930884211852226e-06 4.9483820237706304 -1.0734242068341293
		-3.9930884211852226e-06 -4.9300622789913655 -1.0734242068341293
		-0.27752979449815035 -4.9300622789913655 -1.035916554970383
		-0.53626658431604912 -4.9300622789913655 -0.92874089298415674
		-0.75903406157861075 -4.9300622789913655 -0.75902823860496993
		-0.92874568215375242 -4.9300622789913655 -0.53625861927695839
		-1.0359171076346674 -4.9300622789913655 -0.2775211734834338
		-1.0734314373139906 -4.9300622789913655 5.2308805385989485e-06
		-1.0734314373139906 4.9483820237706304 5.2308805385989485e-06
		-1.035914482440045 4.9483820237706304 0.27753096302274555
		-0.92874060949430448 4.9483820237706304 0.53626775284910588
		-0.75902688169167298 4.9483820237706304 0.75903505120254211
		-0.53625779907496118 4.9483820237706304 0.92874685068427154
		-0.27751999547333944 4.9483820237706304 1.0359182761634937
		6.1607630618508227e-06 4.9483820237706304 1.0734326058439909
		6.1607630618508227e-06 -4.9300622789913655 1.0734326058439909
		6.1607630618508227e-06 4.9483820237706304 1.0734326058439909
		0.27753196212879111 4.9483820237706304 1.0359156509697178
		0.53626875195515133 4.9483820237706304 0.92874177802397728
		0.75903622921178993 4.9483820237706304 0.75902787131645044
		0.92874784979031733 4.9483820237706304 0.53625896760463332
		1.0359192752695396 4.9483820237706304 0.27752116400301163
		1.0734336049503643 4.9483820237706304 -4.9230098673852454e-06
		;
createNode transform -n "handLFT_prop_Gimbal_ctrl" -p "handLFT_prop_ctrl";
	rename -uid "34C3932E-43D5-A382-DAB5-34B3D8EA4810";
	setAttr ".rp" -type "double3" 1.0838178593707353e-06 6.6101001125733539e-07 8.4711813181491256e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707353e-06 6.6101001125733539e-07 8.4711813181491256e-08 ;
createNode nurbsCurve -n "handLFT_prop_Gimbal_ctrlShape" -p "handLFT_prop_Gimbal_ctrl";
	rename -uid "8278AC7B-4598-5E74-B237-089417F0499B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1.565366 3.1307580000000002 4.6961259999999996 6.2614869999999998 7.8268849999999999
		 9.3922439999999998 15.392244 16.957602000000001 18.523 20.088360999999999 21.653728999999998
		 23.219121000000001 24.784486999999999 30.784486999999999 32.349851999999998 33.915246000000003
		 35.480611000000003 37.045976000000003 38.611370000000001 40.176735000000001 41.742100000000001
		 43.307493999999998 44.872858999999998 46.438223999999998 48.003618000000003 49.568983000000003
		 55.568983000000003 57.134349 58.699741000000003 60.265109000000002 61.830469999999998
		 63.395868 64.961225999999996 70.961225999999996 72.526584 74.091982000000002 75.657342999999997
		 77.222712000000001 78.788104000000004 80.353470000000002 86.353470000000002 87.918834000000004
		 89.484228999999999 91.049593999999999 92.614958999999999 94.180352999999997 95.745717999999997
		 101.745718 107.745718 109.311083 110.87647699999999 112.44184199999999 114.00720699999999
		 115.57260100000001 117.13796600000001
		56
		0.9124187267804883 -4.1905528379911594 -4.1718516153002344e-06
		0.88052931513635868 -4.1905528379911594 -0.23590131392092062
		0.78943152313391796 -4.1905528379911594 -0.45582728113644422
		0.64517485449880319 -4.1905528379911594 -0.64518009301063028
		0.45582113427963289 -4.1905528379911594 -0.7894340580910113
		0.23589400121106213 -4.1905528379911594 -0.88053129043276324
		-3.2315524791018284e-06 -4.1905528379911594 -0.91241056310223778
		-3.2315524791018284e-06 4.2061248193565373 -0.91241056310223778
		0.23589400121106213 4.2061248193565373 -0.88053129043276324
		0.45582113427963289 4.2061248193565373 -0.7894340580910113
		0.64517485449880319 4.2061248193565373 -0.64518009301063028
		0.78943152313391796 4.2061248193565373 -0.45582728113644422
		0.88052931513635868 4.2061248193565373 -0.23590131392092062
		0.9124187267804883 4.2061248193565373 -4.1718516153002344e-06
		0.9124187267804883 -4.1905528379911594 -4.1718516153002344e-06
		0.88053154655178756 -4.1905528379911594 0.23589300210933184
		0.78943583489444857 -4.1905528379911594 0.45582013517071035
		0.64518095740270021 -4.1905528379911594 0.64517370332575485
		0.45582860173455758 -4.1905528379911594 0.78943052402715275
		0.23590233038215139 -4.1905528379911594 0.88052831603103221
		5.3992212814788094e-06 -4.1905528379911594 0.91241772767416429
		-0.23589183357965959 -4.1905528379911594 0.88053054744574166
		-0.45581896664103805 -4.1905528379911594 0.78943483578840268
		-0.64517268686524309 -4.1905528379911594 0.64517980622893289
		-0.78942935549748006 -4.1905528379911594 0.45582760262851191
		-0.88052714750135941 -4.1905528379911594 0.23590133127610574
		-0.91241655914421305 -4.1905528379911594 4.4589552297863296e-06
		-0.91241655914421305 4.2061248193565373 4.4589552297863296e-06
		-0.88052937891678829 4.2061248193565373 -0.23589298475414677
		-0.78943366725801067 4.2061248193565373 -0.4558198136786426
		-0.64517878976914023 4.2061248193565373 -0.64517399010745247
		-0.4558264340959628 4.2061248193565373 -0.78942974632976126
		-0.23590016275074885 4.2061248193565373 -0.88052905901805378
		-3.2315524791018284e-06 4.2061248193565373 -0.91241056310223778
		-3.2315524791018284e-06 -4.1905528379911594 -0.91241056310223778
		-0.23590016275074885 -4.1905528379911594 -0.88052905901805378
		-0.4558264340959628 -4.1905528379911594 -0.78942974632976126
		-0.64517878976914023 -4.1905528379911594 -0.64517399010745247
		-0.78943366725801067 -4.1905528379911594 -0.4558198136786426
		-0.88052937891678829 -4.1905528379911594 -0.23589298475414677
		-0.91241655914421305 -4.1905528379911594 4.4589552297863296e-06
		-0.91241655914421305 4.2061248193565373 4.4589552297863296e-06
		-0.88052714750135941 4.2061248193565373 0.23590133127610574
		-0.78942935549748006 4.2061248193565373 0.45582760262851191
		-0.64517268686524309 4.2061248193565373 0.64517980622893289
		-0.45581896664103805 4.2061248193565373 0.78943483578840268
		-0.23589183357965959 4.2061248193565373 0.88053054744574166
		5.3992212814788094e-06 4.2061248193565373 0.91241772767416429
		5.3992212814788094e-06 -4.1905528379911594 0.91241772767416429
		5.3992212814788094e-06 4.2061248193565373 0.91241772767416429
		0.23590233038215139 4.2061248193565373 0.88052831603103221
		0.45582860173455758 4.2061248193565373 0.78943052402715275
		0.64518095740270021 4.2061248193565373 0.64517370332575485
		0.78943583489444857 4.2061248193565373 0.45582013517071035
		0.88053154655178756 4.2061248193565373 0.23589300210933184
		0.9124187267804883 4.2061248193565373 -4.1718516153002344e-06
		;
createNode transform -n "upperArmRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "E720A72F-4E80-247B-018C-1EB428468646";
createNode transform -n "upperArmRGT_FK_ctrl" -p "upperArmRGT_FK_Zro_grp";
	rename -uid "AE6348A3-4E74-F41F-BAF0-DA90585C2F4C";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
	setAttr ".sp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "upperArmRGT_FK_ctrlShape" -p "upperArmRGT_FK_ctrl";
	rename -uid "422E37D5-4735-8A61-4F9E-9F883972315A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		-0.054912947813808635 0.63281946616694373 -3.9731774159737929
		0.94046200969045135 0.54287736690263222 -3.9582494118395264
		1.8581894884384165 0.30947619679938693 -3.9016835658089941
		2.6729437194737429 -0.017296994205761106 -3.7731262574190061
		3.3783538053713862 -0.40140634799608321 -3.5522093277527769
		3.9723159392010738 -0.81590988243591434 -3.2263138877572839
		4.458942410644978 -1.2377843922880207 -2.7940085530445358
		4.8572010899930822 -1.6469401374164574 -2.2664899982870774
		5.1720786591342591 -2.0208600145906859 -1.633922577419447
		5.3927581949608649 -2.3202496993126185 -0.88135768420127025
		5.4756751653881288 -2.4542333809529389 0.0042214909986458956
		5.3789158287731418 -2.3284278654520403 0.88959594823461396
		5.146478015701077 -2.0359850526392909 1.6413521744432717
		4.8217240246854445 -1.6679002341434499 2.2723465577381146
		4.4152386263182057 -1.2636048917820193 2.7973314357300323
		3.9218836286475871 -0.84570564198358023 3.2258549362354825
		3.3228699485416353 -0.43418659618894972 3.5462402047646928
		2.6140650861701431 -0.052082899930896896 3.7596414867500103
		1.7973772855618348 0.2735479247335279 3.8784596640470164
		0.87886088453804145 0.50648299407361907 3.9228263284868707
		-0.1166322957267395 0.59635524650942406 3.9230234138245059
		-0.11608343185760539 1.2075580550316951 3.8543803793614551
		-0.11409156125737957 1.7936829289302887 3.6010492627780617
		-0.1108620056419258 2.3282389483592865 3.1892377810546315
		-0.1065358965177315 2.7878686284357244 2.6369420932221832
		-0.10130236762029438 3.1524760493678556 1.9683080839445304
		-0.095390082380757926 3.4061319655334188 1.2125497244651546
		-0.089057473128789921 3.5377507294996589 0.40270202829291318
		-0.082581302961059616 3.541576895840103 -0.42584107823073059
		-0.0762445998079814 3.4174432496864395 -1.2368697929191723
		-0.070324305787746538 3.170778103576537 -1.9949385448531773
		-0.065079203240957825 2.8123615309215109 -2.6669113485675404
		-0.060738461236597791 2.3578522867209375 -3.2234283651274094
		-0.057491853288998543 1.8271224297302742 -3.6401591449505606
		-0.055481256008004125 1.2433622416705497 -3.8988925798126086
		-0.054912947813808635 0.63281946616694373 -3.9731774159737929
		-1.0504031378778358 0.54291735683943632 -3.9738104953450102
		-1.968912074665857 0.3095499344707337 -3.9315971317346605
		-2.7855894326836141 -0.017184213997835342 -3.81579145825817
		-3.4943848198912146 -0.40126829726798829 -3.6059283150933799
		-4.0933796992133091 -0.81574473290331839 -3.2893573011592481
		-4.5867296228640031 -1.2376058306894879 -2.864711727934131
		-4.9931908428675609 -1.6467328667631953 -2.3434830006085865
		-5.3179496926807905 -2.0206681217176881 -1.7159152630404269
		-5.5503529281874728 -2.3200047984261425 -0.96689157158549455
		-5.6472001545545218 -2.4541510888166194 -0.082718244418668568
		-5.564195294375196 -2.3281829645656154 0.80406206085038856
		-5.3435503361139283 -2.0357931597663437 1.5593594888222915
		-5.028667908175259 -1.6676929634901765 2.1953535554165917
		-4.6304334071907203 -1.2634263301834756 2.726628260840446
		-4.1438120097667408 -0.84554049245103191 3.1628115228335072
		-3.549868676721013 -0.4340485454607636 3.4925212174240872
		-2.844468065987221 -0.051970119722963837 3.7169762859108531
		-2.0297242775423365 0.27362166240482727 3.8485460981213531
		-1.1120042630302458 0.50652298401041584 3.9072652449813874
		-0.1166322957267395 0.59635524650942406 3.9230234138245059
		;
createNode transform -n "upperArmRGT_FK_Gimbal_ctrl" -p "upperArmRGT_FK_ctrl";
	rename -uid "A40CE7CD-4008-6D6D-FA98-A493611C78E7";
	setAttr ".rp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
	setAttr ".sp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
createNode nurbsCurve -n "upperArmRGT_FK_Gimbal_ctrlShape" -p "upperArmRGT_FK_Gimbal_ctrl";
	rename -uid "A9807C9B-47A0-29D1-3CCC-329FBCF2E4AE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		-0.046649788294107625 0.53789457844645505 -3.3772008395854178
		0.79941892558451344 0.46144379407179031 -3.3645120360712908
		1.5794872825202837 0.26305279948403176 -3.3164310669453387
		2.2720283789003113 -0.014704412870344049 -3.2071573548138486
		2.8716269519133077 -0.34119736359211789 -3.0193779645975534
		3.3764947656685411 -0.69352536786597418 -2.742366840601385
		3.7901272663958605 -1.0521187012402646 -2.3749073060955483
		4.1286471438417491 -1.3999010845994357 -1.9265165345517097
		4.3962930776117499 -1.7177329801975305 -1.3888342268142235
		4.5838706830643652 -1.9722142122111728 -0.74915406757877345
		4.6543501079275398 -2.0861003416054453 0.0035882313411553985
		4.5721046718048006 -1.9791656534296811 0.75615651999172828
		4.3745325306935445 -1.7305892625388444 1.3951493122690874
		4.0984916383302572 -1.4177171668173794 1.9314945380697033
		3.7529790497181041 -1.0740661258101634 2.3777316843628342
		3.3336273016980784 -0.71885176348149038 2.7419766597924666
		2.8244656736080196 -0.36906057455605434 3.0143041380422955
		2.2219815405922514 -0.044272432736709465 3.1956952277298147
		1.5277969100751896 0.23251376822805161 3.2966906784322703
		0.74705796920496492 0.43050857716712909 3.3344023432061465
		-0.099111234020098846 0.50689999173756339 3.3345698657431373
		-0.098644699731334856 1.0264223789814939 3.2762232864495431
		-0.096951609721142903 1.5246285217952982 3.0608918373536587
		-0.094206487448007234 1.9790011383099464 2.7108520778887435
		-0.090529294692442058 2.3696863663749186 2.2414007432311625
		-0.086080795129620524 2.6796026741672301 1.6730618353451572
		-0.081055352676014519 2.8952102029079594 1.0306672297876878
		-0.075672634811841721 3.0070861522792631 0.34229668804128249
		-0.070167890169270955 3.0103383936686399 -0.36196495250381461
		-0.064781692489154483 2.9048247944380265 -1.05133935998899
		-0.059749442571954837 2.6951594202446092 -1.6956977991328943
		-0.055291105407184446 2.390505333487837 -2.2668746822901022
		-0.051601474703478416 2.0041724759173496 -2.7399141463659915
		-0.048841857948019048 1.5530520974752859 -3.0941353092156696
		-0.047132850259173784 1.0568559376245201 -3.3140587288484107
		-0.046649788294107625 0.53789457844645505 -3.3772008395854178
		-0.8928164498485307 0.46147778551807378 -3.3777389570509517
		-1.6735490461183486 0.26311547650467654 -3.341857597982155
		-2.3677248004334421 -0.014608549693607148 -3.2434227755271383
		-2.9702008795599029 -0.3410800204732371 -3.0650391038370657
		-3.4793465269836825 -0.69338499076326765 -2.7959537419930545
		-3.8986939620867731 -1.0519669238815117 -2.4350050047517047
		-4.2441859990897965 -1.3997249045441629 -1.9919605865249919
		-4.5202310214310417 -1.7175698712554821 -1.4585280095920563
		-4.7177737716117223 -1.9720060464576683 -0.82185787185536407
		-4.8000939140237131 -2.0860303932895734 -0.070310543763561884
		-4.7295397828712868 -1.9789574876762202 0.68345271571513655
		-4.5419915683492098 -1.7304261535968395 1.325455529491254
		-4.27434150460134 -1.4175409867620972 1.8660504860964096
		-3.9358421787644833 -1.0739143484514015 2.3176339857066854
		-3.5222139909540999 -0.71871138637882415 2.6883897584007874
		-3.0173621578652314 -0.36894323143709612 2.9686429988027809
		-2.4177716387415078 -0.044176569559966371 3.1594298070165316
		-1.7252394185633564 0.23257644524865612 3.2712641473954567
		-0.94517740622807911 0.4305425686134064 3.3211754222264847
		-0.099111234020098846 0.50689999173756339 3.3345698657431373
		;
createNode transform -n "lowerArmRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "2FC41558-4227-EE90-BAB1-CCBDCA656C8A";
createNode transform -n "lowerArmRGT_FK_ctrl" -p "lowerArmRGT_FK_Zro_grp";
	rename -uid "807406F1-4706-D69F-BF74-FD81C1A7BED7";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmRGT_FK_ctrlShape" -p "lowerArmRGT_FK_ctrl";
	rename -uid "C9164B35-43A9-090E-F087-71B4A47EFFCD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		-0.23649111548656809 0.79751085576588465 -4.2104365709115745
		0.61109647818090873 0.69831479431629917 -4.1842981508171153
		1.3928526502869294 0.44708357454067699 -4.0819435610934756
		2.0874155634320033 0.10603505356644505 -3.8792849071572131
		2.6894958115060805 -0.28038219822371108 -3.5607408526633746
		3.1973856787511226 -0.67946693616976683 -3.1176054660711499
		3.6145956017323027 -1.0651700034865736 -2.5529570331457516
		3.9572004347616669 -1.4172956074280283 -1.8835445929203163
		4.2295110319432032 -1.7086671180673292 -1.1029465054700294
		4.4224164090658578 -1.8922754777171276 -0.20226501922185064
		4.4989097243690788 -1.863722085994165 0.81511732834184569
		4.4224164090658578 -1.5441831548863238 1.7814387080181762
		4.2295110319432103 -1.0648908071556786 2.5657970539356421
		3.9572004347616736 -0.52515809981692518 3.2005563279695157
		3.6145956017323098 0.033843820919565074 3.710087787933094
		3.1973856787511226 0.58874833051179132 4.1096822000274331
		2.6894958115060805 1.1148636969908248 4.3904672068677524
		2.0874155634320104 1.5866489857371873 4.558417343685047
		1.3928526502869367 1.9763207489279491 4.632852151710372
		0.61109647818091606 2.2473909025836578 4.6435554046951273
		-0.23649111548656077 2.3495598976159626 4.6343590974887254
		-0.23649106759023772 3.0197511155686194 4.4342426731034719
		-0.23649106759023772 3.6246197838745728 4.0324817509861832
		-0.23649106759023772 4.1398048739258941 3.4637517617496192
		-0.23649106759023772 4.5427957213088872 2.7529056757543797
		-0.23649106759023772 4.8159724501392605 1.9310213271205396
		-0.23649106759024502 4.9474007482737496 1.034008264206937
		-0.23649106759024502 4.9313378989372545 0.10107550745917065
		-0.23650095191972206 3.8025615759939204 -0.51673475989366813
		-0.23650095191972206 3.5899602335211638 -1.1370208303336349
		-0.23649106759024502 4.0369708434896276 -2.5083422821365242
		-0.23649106759024502 3.5002892261121015 -3.188115957173129
		-0.23649106759024502 2.8793541125511615 -3.7192876486217341
		-0.23649106759024502 2.2013137138667624 -4.0786352455527615
		-0.23649106759024502 1.4957954656468218 -4.2504547609383145
		-0.23649111548656809 0.79751085576588465 -4.2104365709115745
		-1.084078613361406 0.6983147943163065 -4.1842981508171162
		-1.8658347854674269 0.4470800616650466 -4.0819429446682296
		-2.5603976986124932 0.10603856644206092 -3.8792855235824431
		-3.1624803218128075 -0.2803821982237038 -3.560740852663371
		-3.6703654388053906 -0.67946342329413634 -3.1176060824963825
		-4.0875824871652737 -1.0651735163623062 -2.5529564167205088
		-4.430177819689705 -1.4172850688012608 -1.8835464421960053
		-4.7025026676286261 -1.7086881953210609 -1.102942806918614
		-4.8953866686151999 -1.8922473747122373 -0.20226995062371875
		-4.9719583630839601 -1.8638801653973236 0.81514506747740978
		-4.8953866686151999 -1.5441550518814409 1.7814337766163053
		-4.702502667628611 -1.0649118844095122 2.5658007524870579
		-4.4301778196896979 -0.5251475611901506 3.2005544786938076
		-4.0875824871652666 0.033840308043847078 3.7100884043583435
		-3.6703654388053759 0.58875184338730502 4.1096815836021854
		-3.1624803218127928 1.11486369699073 4.3904672068677586
		-2.5603976986124932 1.5866524986127011 4.5584167272598233
		-1.8658347854674193 1.9763172360522234 4.6328527681356162
		-1.0840786133613916 2.2473909025836578 4.6435554046951308
		-0.23649111548656077 2.3495598976159626 4.6343590974887254
		;
createNode transform -n "lowerArmRGT_FK_Gimbal_ctrl" -p "lowerArmRGT_FK_ctrl";
	rename -uid "2C291582-4D3B-65F1-13B3-70A9010B7F77";
	setAttr ".rp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
createNode nurbsCurve -n "lowerArmRGT_FK_Gimbal_ctrlShape" -p "lowerArmRGT_FK_Gimbal_ctrl";
	rename -uid "1473E1BC-4FAE-CCC7-8025-1ABC797DDA36";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		-0.20099123083275172 0.6778858072666718 -3.5788709219472103
		0.51945822378460349 0.59356915503452412 -3.5566532648669198
		1.1839509700747213 0.38002261822524525 -3.4696518636018268
		1.7743294462480341 0.090131375397148064 -3.2973920077560033
		2.2860976571109997 -0.23832328862448468 -3.02662956143624
		2.7178040442692857 -0.57754531587863189 -2.649964482832849
		3.0724324788032882 -0.90539292309791797 -2.1700133148462606
		3.3636465868782484 -1.2046996864481541 -1.6010127406546411
		3.5951105944825539 -1.4523654704915603 -0.93750436632189693
		3.7590801650368095 -1.6084325761938887 -0.17192510301094488
		3.8240994830445487 -1.5841621932293706 0.69284989241819694
		3.7590801650368095 -1.3125541017877056 1.5142230651430779
		3.5951105944825592 -0.90515560621665703 2.1809276591729239
		3.3636465868782541 -0.44638280497871663 2.7204730421017165
		3.0724324788032948 0.028768827647300089 3.1535747830707579
		2.7178040442692857 0.50043766080069241 3.4932300333509461
		2.2860976571109997 0.94763572230787096 3.731897289165218
		1.7743294462480401 1.348653217742279 3.8746549054599182
		1.1839509700747273 1.6798742164544263 3.9379244922814434
		0.51945822378460971 1.9102838470617785 3.9470222573184865
		-0.2009912308327455 1.9971274928392377 3.9392053961930444
		-0.20099119012087091 2.5667900280989961 3.7691064354655786
		-0.20099119012087091 3.0809283961590568 3.4276096516658838
		-0.20099119012087091 3.5188357227026796 2.9441891608148043
		-0.20099119012087091 3.8613779429782236 2.3399699877188511
		-0.20099119012087091 4.0935781624840413 1.6413682913800867
		-0.20099119012087716 4.205292215898357 0.87890718790352473
		-0.20099119012087716 4.1916387939623361 0.08591434466792322
		-0.20099959180093263 3.2321789194605017 -0.4392243825819897
		-0.20099959180093263 3.051467778358659 -0.96646754245596145
		-0.20099119012087716 3.431426796831853 -2.1320907764884174
		-0.20099119012087716 2.9752474220609559 -2.7098984002695317
		-0.20099119012087716 2.447452575534157 -3.1613943380008456
		-0.20099119012087716 1.8711182366524179 -3.4668397953922194
		-0.20099119012087716 1.271427725665468 -3.612886383469939
		-0.20099123083275172 0.6778858072666718 -3.5788709219472103
		-0.92144060402636407 0.59356915503453034 -3.5566532648669198
		-1.5859333503164814 0.38001963228095936 -3.4696513396403663
		-2.1763118264897878 0.09013436134142154 -3.2973925317174491
		-2.6880820562100549 -0.23832328862447844 -3.0266295614362373
		-3.1197844056537503 -0.57754232993434618 -2.6499650067942961
		-3.4744188967596514 -0.90539590904229061 -2.1700127908848046
		-3.7656249294054178 -1.2046907286154018 -1.6010143125389764
		-3.9971010501535007 -1.4523833861572319 -0.93750122255319379
		-4.1610524509920888 -1.6084086886397322 -0.17192929470253279
		-4.2261383912905357 -1.5842965607220554 0.69287347068342642
		-4.1610524509920888 -1.3125302142335549 1.5142188734514874
		-3.9971010501534883 -0.90517352188241551 2.1809308029416274
		-3.765624929405412 -0.44637384714595818 2.7204714702173645
		-3.4744188967596448 0.02876584170293979 3.1535753070322201
		-3.1197844056537383 0.50044064674487909 3.4932295093894856
		-2.6880820562100425 0.94763572230779036 3.7318972891652229
		-2.1763118264897878 1.3486562036864655 3.8746543814984786
		-1.5859333503164752 1.6798712305100596 3.9379250162429016
		-0.92144060402635175 1.9102838470617785 3.9470222573184892
		-0.2009912308327455 1.9971274928392377 3.9392053961930444
		;
createNode transform -n "handRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "4126F657-43E5-94E1-1A06-62A18F5017E1";
createNode transform -n "handRGT_FK_ctrl" -p "handRGT_FK_Zro_grp";
	rename -uid "3DE13BD7-40B0-2FD5-0C12-AFA02BB56C28";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handRGT_FK_ctrlShape" -p "handRGT_FK_ctrl";
	rename -uid "3D0E9CD2-4B6F-B853-C161-C4B05982A6A3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		-0.28973832396637123 1.6783926746528355 -2.8263904665535495
		0.44381062894945805 1.6119213459704491 -2.8266665448705806
		1.1203854464294123 1.4375076550855699 -2.8047363620693035
		1.7214984186794573 1.1900544414249143 -2.735088457292794
		2.2425718025347008 0.89476925289644982 -2.6005158077235166
		2.6821276467892132 0.57065997649770006 -2.3900849240562918
		3.043204076453192 0.23454725329719017 -2.1013537854945818
		3.3397131551728796 -0.098119200002046852 -1.741418682580588
		3.575385733349818 -0.41140629514265964 -1.3017024242624275
		3.7423366637992186 -0.67738294018852063 -0.76875187393265232
		3.8085381888863656 -0.83013791995261355 -0.12717533722050897
		3.7423366637992186 -0.79219919328209409 0.5312433664331081
		3.5753857333498331 -0.62375221316855822 1.1025624363907505
		3.3397131551728938 -0.39238563206565341 1.5903827895533937
		3.043204076453192 -0.1279561434746303 2.0030537153815891
		2.6821276467892132 0.15234645595732266 2.3462269745730904
		2.2425718025347008 0.43455540925307762 2.6102081983909784
		1.7214984186794722 0.70168244118229695 2.7944533866295655
		1.1203854464294123 0.93309755771067437 2.9063951904068244
		0.44381062894945805 1.1009674902185445 2.9585560401466964
		-0.28973832396635663 1.1664582138364799 2.969934918651973
		-0.28973828251424866 1.6194981303959977 2.957079249996498
		-0.28973828251424866 2.0654702498477091 2.8070573201364408
		-0.28973828251424866 2.4833113377832383 2.5374871342489467
		-0.28973828251424866 2.8547636577438351 2.1601490680124225
		-0.28973828251424866 3.1635866755972151 1.6915399312117263
		-0.28973828251424866 3.3962881630167798 1.1521342772242626
		-0.28973828251424866 3.5426979014685296 0.56551022767197079
		-0.28973828251424866 3.5964148442925374 -0.042694343690568182
		-0.28973828251424866 3.5550914010515986 -0.64589908510540528
		-0.28973828251424866 3.4205358806299904 -1.2177410682834509
		-0.28973828251424866 3.1986284365783675 -1.7332245944252893
		-0.28973828251424866 2.8990637808508031 -2.1698272275759258
		-0.28973828251424866 2.5349395809569097 -2.5084609927828083
		-0.28973828251424866 2.1221661472653484 -2.7343277747708923
		-0.28973832396637123 1.6783926746528355 -2.8263904665535495
		-1.0232871939779553 1.6119213459704491 -2.8266665448705788
		-1.6998620114579095 1.437505352966818 -2.8047365653936209
		-2.3009749837079694 1.1900567435436809 -2.7350882539684687
		-2.8220504231281613 0.89476925289644982 -2.6005158077235122
		-3.2616021562527617 0.57066227861646657 -2.3900847207319682
		-3.6226847526116304 0.23454495117842369 -2.1013539888188992
		-3.9191856090714658 -0.098112293645732818 -1.7414180726076107
		-4.154870520638168 -0.41142010785530225 -1.3017036442083565
		-4.3218029510029288 -0.67736452323834495 -0.76875024733806463
		-4.3880723097337446 -0.83024151529739709 -0.12718448681502587
		-4.3218029510029146 -0.79218077633191852 0.53124499302769712
		-4.154870520638168 -0.62376602588118635 1.1025612164448251
		-3.9191856090714658 -0.3923787257093248 1.5903833995263656
		-3.6226847526116162 -0.12795844559339678 2.0030535120572805
		-3.2616021562527471 0.15234875807608914 2.3462271778974055
		-2.8220504231281613 0.43455540925307762 2.6102081983909842
		-2.3009749837079694 0.70168474330106345 2.7944535899538967
		-1.6998620114579095 0.93309525559190787 2.9063949870825105
		-1.0232871939779553 1.1009674902185445 2.9585560401466964
		-0.28973832396635663 1.1664582138364799 2.969934918651973
		;
createNode transform -n "handRGT_FK_Gimbal_ctrl" -p "handRGT_FK_ctrl";
	rename -uid "202ED45D-4413-7C00-687F-C7B900410032";
	setAttr ".rp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
createNode nurbsCurve -n "handRGT_FK_Gimbal_ctrlShape" -p "handRGT_FK_Gimbal_ctrl";
	rename -uid "2F008617-4B6C-96C0-3217-82A2B9C196EF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55
		56
		-0.24625135804058443 1.4266373159439365 -2.4024318418263255
		0.37726525193787042 1.3701366865639082 -2.4026665083958019
		0.95235384679583135 1.221885049311761 -2.384025853014716
		1.46329987320837 1.0115498177002036 -2.3248251339546835
		1.9062122494853271 0.76055740745100886 -2.2104383818207975
		2.2798347171016626 0.48506452251207155 -2.0315721307036565
		2.5867496823160443 0.19936870779163815 -1.7861506629262029
		2.838782399227779 -0.083397777512713309 -1.480205825449308
		3.0391040906781766 -0.34969180838223413 -1.1064470058788718
		3.181012381560167 -0.57577195667121606 -0.65343903809856285
		3.2372836778842422 -0.70561368947069492 -0.10809898189324105
		3.181012381560167 -0.67336577180075341 0.45155691621233351
		3.0391040906781885 -0.53018583870424796 0.93717812567632952
		2.8387823992277914 -0.33352424476677883 1.3518254258645761
		2.5867496823160443 -0.10875917946440926 1.7025957128185423
		2.2798347171016626 0.12949803005275076 1.9942929831313185
		1.9062122494853271 0.36937564035414244 2.2186770233765229
		1.4632998732083822 0.59643361749397894 2.3752854333793221
		0.95235384679583135 0.79313646654309966 2.4704359665899922
		0.37726525193787042 0.93582590917478947 2.5147726888688835
		-0.24625135804057199 0.99149302425003438 2.5244447355983688
		-0.24625132280628023 1.3765769533256245 2.5135174172412151
		-0.24625132280628023 1.7556532548595789 2.3859987768601663
		-0.24625132280628023 2.1108181796047791 2.1568641188557964
		-0.24625132280628023 2.4265526515712863 1.8361267625547506
		-0.24625132280628023 2.6890522167466591 1.4378089962741589
		-0.24625132280628023 2.8868484810532888 0.97931419038481482
		-0.24625132280628023 3.0112967587372768 0.48068374826536686
		-0.24625132280628023 3.0569561601376831 -0.036290137392791348
		-0.24625132280628023 3.0218312333828852 -0.54901416759540289
		-0.24625132280628023 2.9074590410245182 -1.0350798532967418
		-0.24625132280628023 2.7188377135806383 -1.4732408505173042
		-0.24625132280628023 2.4642077562122093 -1.8443530886953456
		-0.24625132280628023 2.1547021863024001 -2.1321917891211957
		-0.24625132280628023 1.8038447676645726 -2.3241785538110671
		-0.24625135804058443 1.4266373159439365 -2.4024318418263255
		-0.86976789755043082 1.3701366865639082 -2.4026665083958001
		-1.4448564924083918 1.2218830925108217 -2.3840260258403863
		-1.9558025188209427 1.0115517745011551 -2.3248249611290071
		-2.3987166423281057 0.76055740745100886 -2.2104383818207931
		-2.7723356154840162 0.4850664793130231 -2.0315719578779814
		-3.0792558223890545 0.19936675099068665 -1.7861508357518727
		-3.3312815503799142 -0.083391907109846383 -1.4802053069722774
		-3.5316137252116113 -0.34970354918798036 -1.1064480428329113
		-3.6735062910216585 -0.57575630226356667 -0.65343765549316335
		-3.7298352459428523 -0.70570174551376086 -0.10810675904858036
		-3.6735062910216456 -0.67335011739310413 0.45155829881773418
		-3.5316137252116113 -0.53019757950998181 0.93717708872229311
		-3.3312815503799142 -0.33351837436389953 1.3518259443416023
		-3.0792558223890421 -0.10876113626536077 1.70259553999288
		-2.7723356154840038 0.12949998685370229 1.9942931559569865
		-2.3987166423281057 0.36937564035414244 2.2186770233765283
		-1.9558025188209427 0.59643557429493044 2.3752856062050034
		-1.4448564924083918 0.79313450974214816 2.470435793764326
		-0.86976789755043082 0.93582590917478947 2.5147726888688835
		-0.24625135804057199 0.99149302425003438 2.5244447355983688
		;
createNode transform -n "footRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "98B53851-448E-4DA4-DB2D-D788042DF0DB";
createNode transform -n "footRGT_FK_ctrl" -p "footRGT_FK_Zro_grp";
	rename -uid "DD04A9A6-43B8-A1F6-C76C-2C8EF4791FB7";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
	setAttr ".sp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "footRGT_FK_ctrlShape" -p "footRGT_FK_ctrl";
	rename -uid "1A08B106-4279-B4A9-2F91-4F9C85E95F88";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.7011222682495437 -0.66453100014995259 -2.9299522615008424
		0.96283268683878476 1.8091710926789608 -7.1247404080399521
		-2.6257524284141818 -1.1029812139620501 -3.3318298755954472
		-5.6187061471069732 -1.7429236010491032 0.32530298442205352
		-2.9682985075520492 -1.9917830107149133 4.3408972818570337
		0.57130191424555865 -1.9374566627587309 6.2643225804705009
		2.9944065346660036 -1.5785696271722383 4.7196431541563761
		4.9229857127450263 -3.4306870627497075 0.71692864892854891
		3.7011222682495437 -0.66453100014995259 -2.9299522615008424
		0.96283268683878476 1.8091710926789608 -7.1247404080399521
		-2.6257524284141818 -1.1029812139620501 -3.3318298755954472
		;
createNode transform -n "footRGT_FK_Gimbal_ctrl" -p "footRGT_FK_ctrl";
	rename -uid "1E99C58B-493C-7F75-0037-54BAA338FEE7";
	setAttr ".rp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
	setAttr ".sp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
createNode nurbsCurve -n "footRGT_FK_Gimbal_ctrlShape" -p "footRGT_FK_Gimbal_ctrl";
	rename -uid "683BFBEA-4A0B-742B-BEB4-48B33D65CD2C";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.1459556076269233 -0.56485406274931449 -2.4904607224769264
		0.81840946342777832 1.5377927161552616 -6.0560306470351701
		-2.231887884537243 -0.93753674448959745 -2.8320566944573415
		-4.7758985454261156 -1.4814877735135925 0.2765062365575347
		-2.5230520518044304 -1.6930182717295312 3.6897613893772676
		0.48560830672353628 -1.6468408759667763 5.3246728931987146
		2.545247234080914 -1.3417868957182573 4.0116953808317097
		4.1845395354480841 -2.9160867159591066 0.60938805138805585
		3.1459556076269233 -0.56485406274931449 -2.4904607224769264
		0.81840946342777832 1.5377927161552616 -6.0560306470351701
		-2.231887884537243 -0.93753674448959745 -2.8320566944573415
		;
createNode transform -n "toesRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "F9D440BD-4BA4-9448-EA52-1996DB7221FA";
createNode transform -n "toesRGT_FK_ctrl" -p "toesRGT_FK_Zro_grp";
	rename -uid "1A320CA9-4182-C069-CB04-69A30FB990D9";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.7181603029265618e-05 -2.3527289185731402e-06 1.1684328747871983e-06 ;
	setAttr ".sp" -type "double3" 1.7181603029265618e-05 -2.3527289185731402e-06 1.1684328747871983e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "toesRGT_FK_ctrlShape" -p "toesRGT_FK_ctrl";
	rename -uid "DEECE342-471B-2A0B-B7F2-9EA55A60654A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.8013984558348 -1.4688833872512113 -0.29654441811259097
		0.11705469236132696 -1.3908844545646699 1.0655440554065203
		-3.2217367167803452 -1.183020792844494 0.086941842820569396
		-7.0929240647432801 -0.99928898721870973 0.33336058652951883
		-5.0412080845202016 -0.88448612092675016 -4.9133120719565504
		-0.45593729311307868 -0.97611295444972734 -8.2432004891931872
		3.9934943408886747 -1.3132799967080124 -5.4885414421218401
		6.2836149439734772 -1.6341497425608833 -0.51830864912073626
		2.8013984558348 -1.4688833872512113 -0.29654441811259097
		0.11705469236132696 -1.3908844545646699 1.0655440554065203
		-3.2217367167803452 -1.183020792844494 0.086941842820569396
		;
createNode transform -n "toesRGT_FK_Gimbal_ctrl" -p "toesRGT_FK_ctrl";
	rename -uid "4ACC9BF0-4DFE-C3AE-217B-C59435464176";
	setAttr ".rp" -type "double3" 1.7181603029265618e-05 -2.3527289185731402e-06 1.1684328747871983e-06 ;
	setAttr ".sp" -type "double3" 1.7181603029265618e-05 -2.3527289185731402e-06 1.1684328747871983e-06 ;
createNode nurbsCurve -n "toesRGT_FK_Gimbal_ctrlShape" -p "toesRGT_FK_Gimbal_ctrl";
	rename -uid "F1A64F96-4221-3A05-78D2-D382763E17A6";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.3811912647000346 -1.2485512320728673 -0.2520625801307711
		0.099499065747582313 -1.1822521392893071 0.90571262236047378
		-2.7384736320228393 -1.0055680268271576 0.073900741662415184
		-6.028982877791333 -0.84939599204524097 0.28335667381502216
		-4.2850242946017163 -0.75181355569707509 -4.1763150858981355
		-0.38754412190566245 -0.82969636419160664 -7.0067202405492779
		3.3944727669958286 -1.1162883501111482 -4.6652600505386319
		5.3410752796179102 -1.3890276340860888 -0.44056217648769452
		2.3811912647000346 -1.2485512320728673 -0.2520625801307711
		0.099499065747582313 -1.1822521392893071 0.90571262236047378
		-2.7384736320228393 -1.0055680268271576 0.073900741662415184
		;
createNode transform -n "TMP_Hand_ctrl" -p "TMP_GRP";
	rename -uid "D87D417B-4941-011C-CD14-F48C12CC5E0F";
createNode transform -n "pinky01LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "726E6EAF-427F-AD66-6848-05BAA2A8268F";
createNode transform -n "pinky01LFT_ctrl" -p "pinky01LFT_Zro_grp";
	rename -uid "F70EE9C6-4B0B-F354-3D20-C1BA487B817C";
	setAttr ".rp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
createNode nurbsCurve -n "pinky01LFT_ctrlShape" -p "pinky01LFT_ctrl";
	rename -uid "6F355704-457B-1BE3-78A2-F5B2EE6B2362";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0901875015684046 -0.026952990450859339 -0.4371361154626543
		-1.5360101960777439 -0.038115475544569212 -0.61823951831921609
		-1.9795566963832993 -0.027233070178781352 -0.43161424173695911
		-2.1610034781492042 -0.00068053982553290308 0.013417158343856166
		-1.9740614774659462 0.025988003349566701 0.45616132343777832
		-1.5282387829566095 0.037150488443276404 0.6372647262943405
		-1.0846922826510588 0.026268083077488714 0.45063944971208431
		-0.9032455008851461 -0.00028444727575980216 0.0056080496312680269
		-1.0901875015684046 -0.026952990450859339 -0.4371361154626543
		-1.5360101960777439 -0.038115475544569212 -0.61823951831921609
		-1.9795566963832993 -0.027233070178781352 -0.43161424173695911
		;
createNode transform -n "pinky02LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "00423954-451C-E354-00A1-F791036346C8";
createNode transform -n "pinky02LFT_ctrl" -p "pinky02LFT_Zro_grp";
	rename -uid "FCF5D853-4482-1F7E-7441-8AA03F66875F";
	setAttr ".rp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
createNode nurbsCurve -n "pinky02LFT_ctrlShape" -p "pinky02LFT_ctrl";
	rename -uid "0FB4B78A-45F1-5EB1-E51C-F7B4C480B7A8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.1335628744200574 1.096468636699942e-09 -0.44232708258195175
		-1.5913057787480347 1.0920894204455842e-09 -0.62568303153073046
		-2.0446311253109455 1.0877524438944168e-09 -0.4316621547129707
		-2.2279870742597208 1.0859982490904219e-09 0.026080749615005581
		-2.0339661974419645 1.0878544195587324e-09 0.47940609617791918
		-1.5762232931139919 1.0922336358130915e-09 0.66276204512669834
		-1.1228979465510733 1.0965706123642556e-09 0.46874116830893869
		-0.93954199760229484 1.0983248071682559e-09 0.010998263980962344
		-1.1335628744200574 1.096468636699942e-09 -0.44232708258195175
		-1.5913057787480347 1.0920894204455842e-09 -0.62568303153073046
		-2.0446311253109455 1.0877524438944168e-09 -0.4316621547129707
		;
createNode transform -n "pinky03LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "8A86CF3F-4BC8-819F-18F9-2BA1F3CD03BD";
createNode transform -n "pinky03LFT_ctrl" -p "pinky03LFT_Zro_grp";
	rename -uid "8BBB60DF-4BD9-7E58-CEC6-3EA4546478AD";
	setAttr ".rp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
createNode nurbsCurve -n "pinky03LFT_ctrlShape" -p "pinky03LFT_ctrl";
	rename -uid "1D0B8AE6-4429-669D-4548-B99F46D3F14B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0107188330308834 1.0976036857398928e-09 -0.36504588134221677
		-1.3893716771236968 1.0939811223447386e-09 -0.51672109223974516
		-1.7643702410608362 1.0903935003623199e-09 -0.35622366862968358
		-1.9160454519583676 1.0889424000932724e-09 0.022429175463130231
		-1.7555480283483087 1.0904778563948335e-09 0.39742773940027204
		-1.3768951842554953 1.0941004197899879e-09 0.54910295029780054
		-1.0018966203183501 1.0976880417724068e-09 0.38860552668773934
		-0.85022140942082503 1.0991391420414605e-09 0.0099526825949251448
		-1.0107188330308834 1.0976036857398928e-09 -0.36504588134221677
		-1.3893716771236968 1.0939811223447386e-09 -0.51672109223974516
		-1.7643702410608362 1.0903935003623199e-09 -0.35622366862968358
		;
createNode transform -n "ring01LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "713255CD-4BAF-E6B8-F489-FC84B264E6EE";
createNode transform -n "ring01LFT_ctrl" -p "ring01LFT_Zro_grp";
	rename -uid "E8505027-4F85-62EF-33E7-97A2EE5C4F78";
	setAttr ".rp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
createNode nurbsCurve -n "ring01LFT_ctrlShape" -p "ring01LFT_ctrl";
	rename -uid "4D0E64AE-4F01-F47C-CCF3-19BDAE8ACD3A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0901875015684046 -0.026952990450859339 -0.4371361154626543
		-1.5360101960777439 -0.038115475544569212 -0.61823951831921609
		-1.9795566963832993 -0.027233070178781352 -0.43161424173695911
		-2.1610034781492042 -0.00068053982553290308 0.013417158343856166
		-1.9740614774659462 0.025988003349566701 0.45616132343777832
		-1.5282387829566095 0.037150488443276404 0.6372647262943405
		-1.0846922826510588 0.026268083077488714 0.45063944971208431
		-0.9032455008851461 -0.00028444727575980216 0.0056080496312680269
		-1.0901875015684046 -0.026952990450859339 -0.4371361154626543
		-1.5360101960777439 -0.038115475544569212 -0.61823951831921609
		-1.9795566963832993 -0.027233070178781352 -0.43161424173695911
		;
createNode transform -n "ring02LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "E8590351-465B-D601-20C1-9087A1DE6E4D";
createNode transform -n "ring02LFT_ctrl" -p "ring02LFT_Zro_grp";
	rename -uid "03A87BD4-4F0B-B036-9B33-58BC288AA024";
	setAttr ".rp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
createNode nurbsCurve -n "ring02LFT_ctrlShape" -p "ring02LFT_ctrl";
	rename -uid "83D61B4A-481A-0179-1921-0D81ABF221C0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.1335628744200574 1.096468636699942e-09 -0.44232708258195175
		-1.5913057787480347 1.0920894204455842e-09 -0.62568303153073046
		-2.0446311253109455 1.0877524438944168e-09 -0.4316621547129707
		-2.2279870742597208 1.0859982490904219e-09 0.026080749615005581
		-2.0339661974419645 1.0878544195587324e-09 0.47940609617791918
		-1.5762232931139919 1.0922336358130915e-09 0.66276204512669834
		-1.1228979465510733 1.0965706123642556e-09 0.46874116830893869
		-0.93954199760229484 1.0983248071682559e-09 0.010998263980962344
		-1.1335628744200574 1.096468636699942e-09 -0.44232708258195175
		-1.5913057787480347 1.0920894204455842e-09 -0.62568303153073046
		-2.0446311253109455 1.0877524438944168e-09 -0.4316621547129707
		;
createNode transform -n "ring03LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "17D405BB-41FB-15A7-86F2-80A6149D0F7E";
createNode transform -n "ring03LFT_ctrl" -p "ring03LFT_Zro_grp";
	rename -uid "32DD3584-4D57-FD61-17A2-F7B509338A9A";
	setAttr ".rp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
createNode nurbsCurve -n "ring03LFT_ctrlShape" -p "ring03LFT_ctrl";
	rename -uid "A7534F0E-4851-979B-6A11-9AB375CF6179";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0107188330308834 1.0976036857398928e-09 -0.36504588134221677
		-1.3893716771236968 1.0939811223447386e-09 -0.51672109223974516
		-1.7643702410608362 1.0903935003623199e-09 -0.35622366862968358
		-1.9160454519583676 1.0889424000932724e-09 0.022429175463130231
		-1.7555480283483087 1.0904778563948335e-09 0.39742773940027204
		-1.3768951842554953 1.0941004197899879e-09 0.54910295029780054
		-1.0018966203183501 1.0976880417724068e-09 0.38860552668773934
		-0.85022140942082503 1.0991391420414605e-09 0.0099526825949251448
		-1.0107188330308834 1.0976036857398928e-09 -0.36504588134221677
		-1.3893716771236968 1.0939811223447386e-09 -0.51672109223974516
		-1.7643702410608362 1.0903935003623199e-09 -0.35622366862968358
		;
createNode transform -n "pinky01RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "D070EECD-48B6-5995-5774-EBAA63E8F7EF";
createNode transform -n "pinky01RGT_ctrl" -p "pinky01RGT_Zro_grp";
	rename -uid "1A3A8DEE-41DE-92FA-8C1C-E08AA35B6EA3";
	setAttr ".rp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
createNode nurbsCurve -n "pinky01RGT_ctrlShape" -p "pinky01RGT_ctrl";
	rename -uid "87EBC7F6-4220-E469-2121-FB9C3E67C521";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0901874923405379 -0.026952990450859339 0.43713615821505286
		1.5360101868498768 -0.038115475544569212 0.61823956107161482
		1.9795566871554331 -0.027233070178781352 0.43161428448935807
		2.1610034689213378 -0.00068053982553290308 -0.013417115591457085
		1.9740614682380797 0.025988003349566701 -0.45616128068537937
		1.5282387737287435 0.037150488443276404 -0.63726468354194177
		1.0846922734231925 0.026268083077488714 -0.45063940695968563
		0.90324549165727974 -0.00028444727575980216 -0.0056080068788695011
		1.0901874923405379 -0.026952990450859339 0.43713615821505286
		1.5360101868498768 -0.038115475544569212 0.61823956107161482
		1.9795566871554331 -0.027233070178781352 0.43161428448935807
		;
createNode transform -n "pinky02RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "FDEC3C5B-4AA7-D99F-9B3B-42BFDDB2573A";
createNode transform -n "pinky02RGT_ctrl" -p "pinky02RGT_Zro_grp";
	rename -uid "F7491C9C-4DA0-15B1-A9DF-F1BA70210D4E";
	setAttr ".rp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
createNode nurbsCurve -n "pinky02RGT_ctrlShape" -p "pinky02RGT_ctrl";
	rename -uid "754E6694-409F-D20F-51E1-ACB48EDE0A3D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.133562865104994 1.096468636699942e-09 0.44232712987443601
		1.5913057694329711 1.0920894204455842e-09 0.62568307882321517
		2.0446311159958825 1.0877524438944168e-09 0.43166220200545546
		2.2279870649446578 1.0859982490904219e-09 -0.026080702322520737
		2.0339661881269016 1.0878544195587324e-09 -0.47940604888543442
		1.5762232837989292 1.0922336358130915e-09 -0.66276199783421375
		1.1228979372360102 1.0965706123642556e-09 -0.46874112101645438
		0.93954198828723168 1.0983248071682559e-09 -0.01099821668847807
		1.133562865104994 1.096468636699942e-09 0.44232712987443601
		1.5913057694329711 1.0920894204455842e-09 0.62568307882321517
		2.0446311159958825 1.0877524438944168e-09 0.43166220200545546
		;
createNode transform -n "pinky03RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "4F817704-437D-1E5C-C258-90953740731B";
createNode transform -n "pinky03RGT_ctrl" -p "pinky03RGT_Zro_grp";
	rename -uid "32D02A0B-46D8-EE48-F902-93B55082B1AF";
	setAttr ".rp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
createNode nurbsCurve -n "pinky03RGT_ctrlShape" -p "pinky03RGT_ctrl";
	rename -uid "B6A3D1C0-4702-2E16-BBE0-D58A6AA50C5E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0107188236787297 1.0976036857398928e-09 0.36504593220375009
		1.3893716677715429 1.0939811223447386e-09 0.51672114310127859
		1.7643702317086825 1.0903935003623199e-09 0.35622371949121717
		1.9160454426062139 1.0889424000932724e-09 -0.022429124601596566
		1.755548018996155 1.0904778563948335e-09 -0.3974276885387385
		1.376895174903342 1.0941004197899879e-09 -0.549102899436267
		1.0018966109661966 1.0976880417724068e-09 -0.38860547582620608
		0.85022140006867131 1.0991391420414605e-09 -0.0099526317333919496
		1.0107188236787297 1.0976036857398928e-09 0.36504593220375009
		1.3893716677715429 1.0939811223447386e-09 0.51672114310127859
		1.7643702317086825 1.0903935003623199e-09 0.35622371949121717
		;
createNode transform -n "ring01RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "45F4673B-4206-B9F4-1AF3-9F979BC13106";
createNode transform -n "ring01RGT_ctrl" -p "ring01RGT_Zro_grp";
	rename -uid "543DD096-4C2F-8878-A0F6-C096C0D31C86";
	setAttr ".rp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
createNode nurbsCurve -n "ring01RGT_ctrlShape" -p "ring01RGT_ctrl";
	rename -uid "EB6DBAD3-4DFB-552A-51FF-7E86B6735CD2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0901874923405379 -0.026952990450859339 0.43713615821505286
		1.5360101868498768 -0.038115475544569212 0.61823956107161482
		1.9795566871554331 -0.027233070178781352 0.43161428448935807
		2.1610034689213378 -0.00068053982553290308 -0.013417115591457085
		1.9740614682380797 0.025988003349566701 -0.45616128068537937
		1.5282387737287435 0.037150488443276404 -0.63726468354194177
		1.0846922734231925 0.026268083077488714 -0.45063940695968563
		0.90324549165727974 -0.00028444727575980216 -0.0056080068788695011
		1.0901874923405379 -0.026952990450859339 0.43713615821505286
		1.5360101868498768 -0.038115475544569212 0.61823956107161482
		1.9795566871554331 -0.027233070178781352 0.43161428448935807
		;
createNode transform -n "ring02RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "9C5B2E4C-46C0-C177-98E0-4A9EBA7D1795";
createNode transform -n "ring02RGT_ctrl" -p "ring02RGT_Zro_grp";
	rename -uid "58C8FFB5-45C8-5183-7C18-CFA2F5854803";
	setAttr ".rp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
createNode nurbsCurve -n "ring02RGT_ctrlShape" -p "ring02RGT_ctrl";
	rename -uid "5BF72DFC-41A2-80F6-C9E1-6E8F9B5A3EEA";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.133562865104994 1.096468636699942e-09 0.44232712987443601
		1.5913057694329711 1.0920894204455842e-09 0.62568307882321517
		2.0446311159958825 1.0877524438944168e-09 0.43166220200545546
		2.2279870649446578 1.0859982490904219e-09 -0.026080702322520737
		2.0339661881269016 1.0878544195587324e-09 -0.47940604888543442
		1.5762232837989292 1.0922336358130915e-09 -0.66276199783421375
		1.1228979372360102 1.0965706123642556e-09 -0.46874112101645438
		0.93954198828723168 1.0983248071682559e-09 -0.01099821668847807
		1.133562865104994 1.096468636699942e-09 0.44232712987443601
		1.5913057694329711 1.0920894204455842e-09 0.62568307882321517
		2.0446311159958825 1.0877524438944168e-09 0.43166220200545546
		;
createNode transform -n "ring03RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "F1092178-4CE2-4F3B-AEC6-529313E8B5E9";
createNode transform -n "ring03RGT_ctrl" -p "ring03RGT_Zro_grp";
	rename -uid "DD89B118-4BB6-D673-3CE7-1588A7F90DDB";
	setAttr ".rp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
createNode nurbsCurve -n "ring03RGT_ctrlShape" -p "ring03RGT_ctrl";
	rename -uid "CE96AF5C-47D4-A306-8E28-D282F3B82D02";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0107188236787297 1.0976036857398928e-09 0.36504593220375009
		1.3893716677715429 1.0939811223447386e-09 0.51672114310127859
		1.7643702317086825 1.0903935003623199e-09 0.35622371949121717
		1.9160454426062139 1.0889424000932724e-09 -0.022429124601596566
		1.755548018996155 1.0904778563948335e-09 -0.3974276885387385
		1.376895174903342 1.0941004197899879e-09 -0.549102899436267
		1.0018966109661966 1.0976880417724068e-09 -0.38860547582620608
		0.85022140006867131 1.0991391420414605e-09 -0.0099526317333919496
		1.0107188236787297 1.0976036857398928e-09 0.36504593220375009
		1.3893716677715429 1.0939811223447386e-09 0.51672114310127859
		1.7643702317086825 1.0903935003623199e-09 0.35622371949121717
		;
createNode transform -n "index01RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "06036B8E-444C-41D6-BAD6-D7A09D9BB4CF";
createNode transform -n "index01RGT_ctrl" -p "index01RGT_Zro_grp";
	rename -uid "41248148-4CD0-D025-D60F-B9AB94F2DA58";
	setAttr ".rp" -type "double3" -0.00023490122594700306 -5.3593224903946879e-05 1.8251019008019369e-06 ;
	setAttr ".sp" -type "double3" -0.00023490122594700306 -5.3593224903946879e-05 1.8251019008019369e-06 ;
createNode nurbsCurve -n "index01RGT_ctrlShape" -p "index01RGT_ctrl";
	rename -uid "6297E0C5-491B-0F0F-ACA8-488508F7F14D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0926672785774429 -5.3591952787475824e-05 0.43114921271973139
		1.5396147641539069 -5.359142581433023e-05 0.60980772406462824
		1.9819850069281 -5.3591975914412239e-05 0.42009877106778243
		2.1606435182730004 -5.3593281032364968e-05 -0.026848714508862195
		1.9709345652761503 -5.3594576213760153e-05 -0.46921895728305374
		1.5239870796994965 -5.3595103361999275e-05 -0.64787746862795159
		1.0816168369253181 -5.3594553276508391e-05 -0.45816851563109795
		0.90295832558060751 -5.359324836283144e-05 -0.011221030054456807
		1.0926672785774429 -5.3591952787475824e-05 0.43114921271973139
		1.5396147641539069 -5.359142581433023e-05 0.60980772406462824
		1.9819850069281 -5.3591975914412239e-05 0.42009877106778243
		;
createNode transform -n "index02RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "5F8BF5F4-4974-CF8B-397F-62B207C31A62";
	setAttr ".rp" -type "double3" 0 -7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" 0 -7.2955635396140418e-15 0 ;
createNode transform -n "index02RGT_ctrl" -p "index02RGT_Zro_grp";
	rename -uid "F5597C52-49FA-C4D0-FCCF-AE92B95D00C9";
	setAttr ".rp" -type "double3" 0.00012120864448241608 4.9428310970557256e-05 2.8805443260338447e-06 ;
	setAttr ".sp" -type "double3" 0.00012120864448241608 4.9428310970557256e-05 2.8805443260338447e-06 ;
createNode nurbsCurve -n "index02RGT_ctrlShape" -p "index02RGT_ctrl";
	rename -uid "7F7C2A96-45DA-1523-3A2A-F5B18F7023F8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1343087072872562 4.9429564603718085e-05 0.44072588485822856
		1.5923105484890909 4.9430084091615493e-05 0.62343407825165364
		2.0453609587257744 4.9429544511736099e-05 0.42877207306862331
		2.2280691521192022 4.9428261907892457e-05 -0.02922976813338813
		2.0334071469361814 4.9426987650173502e-05 -0.48228017837008624
		1.575405305734157 4.9426468133093844e-05 -0.66498837176351144
		1.1223548954974589 4.9427007683790981e-05 -0.47032636658048194
		0.93964670210404544 4.942829031681688e-05 -0.012324525378469415
		1.1343087072872562 4.9429564603718085e-05 0.44072588485822856
		1.5923105484890909 4.9430084091615493e-05 0.62343407825165364
		2.0453609587257744 4.9429544511736099e-05 0.42877207306862331
		;
createNode transform -n "index03RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "682024A1-4963-000F-7CC0-61AD0A097E52";
createNode transform -n "index03RGT_ctrl" -p "index03RGT_Zro_grp";
	rename -uid "A541709F-4512-BF3D-105A-E9B26818E989";
	setAttr ".rp" -type "double3" -0.00013322877243714874 -8.7433801653780712e-05 -6.0350929155347919e-06 ;
	setAttr ".sp" -type "double3" -0.00013322877243714874 -8.7433801653780712e-05 -6.0350929155347919e-06 ;
createNode nurbsCurve -n "index03RGT_ctrlShape" -p "index03RGT_ctrl";
	rename -uid "CCEFC7CE-41F0-B8DF-3D3C-38A4D1728EFF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.009558514473744 -8.7433701274121958e-05 0.36787118309652411
		1.3877847707372759 -8.7433624874980577e-05 0.52060704991608941
		1.7632316885228392 -8.7434354475107921e-05 0.36116126644773489
		1.915967555342402 -8.7435462218884646e-05 -0.017064989815982309
		1.756521771873895 -8.7436299384800812e-05 -0.39251190760136739
		1.3782955156103485 -8.7436375448346289e-05 -0.54524777442092998
		1.0028485978247856 -8.7435646227588238e-05 -0.38580199095257955
		0.85011273100522233 -8.7434538469220388e-05 -0.0075757346888632717
		1.009558514473744 -8.7433701274121958e-05 0.36787118309652411
		1.3877847707372759 -8.7433624874980577e-05 0.52060704991608941
		1.7632316885228392 -8.7434354475107921e-05 0.36116126644773489
		;
createNode transform -n "middle01RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "FBFC087A-4FCB-6763-B532-9F9161DDDAA5";
createNode transform -n "middle01RGT_ctrl" -p "middle01RGT_Zro_grp";
	rename -uid "EF94BD09-40F2-EBFC-9984-EFBB5E65D6A5";
	setAttr ".rp" -type "double3" 0.00023128282937934106 3.7202749990716172e-05 -1.2259477520336723e-06 ;
	setAttr ".sp" -type "double3" 0.00023128282937934106 3.7202749990716172e-05 -1.2259477520336723e-06 ;
createNode nurbsCurve -n "middle01RGT_ctrlShape" -p "middle01RGT_ctrl";
	rename -uid "FF4AF7AF-42CF-7933-B118-F49DE7E04B41";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.090418779783872 0.026990195571572107 0.43713491089110018
		1.5362414742932078 0.038152680665085287 0.61823831374765736
		1.9797879745987614 0.027270275299421089 0.43161303716539628
		2.1612347563645038 0.0007177449460898822 -0.013418362915407139
		1.9742927556814005 -0.025950798228747574 -0.45616252800933366
		1.5284700611720938 -0.03711328332264012 -0.63726593086589534
		1.0849235608663503 -0.026230877956990514 -0.4506406542836443
		0.90347677910044744 0.00032165239648660268 -0.0056092542028252923
		1.090418779783872 0.026990195571572107 0.43713491089110018
		1.5362414742932078 0.038152680665085287 0.61823831374765736
		1.9797879745987614 0.027270275299421089 0.43161303716539628
		;
createNode transform -n "middle02RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "A8E2126D-4C34-7B8B-CAA3-95A4AC9C38B1";
	setAttr ".sp" -type "double3" 0 0 1.139931803064694e-16 ;
createNode transform -n "middle02RGT_ctrl" -p "middle02RGT_Zro_grp";
	rename -uid "6FC573FA-4B4E-3177-93FD-B19C1E9B22DC";
	setAttr ".rp" -type "double3" 0.00013552500442800012 4.0882473702030109e-05 9.0693690630569376e-07 ;
	setAttr ".sp" -type "double3" 0.00013552500442800012 4.0882473702030109e-05 9.0693690630569376e-07 ;
createNode nurbsCurve -n "middle02RGT_ctrlShape" -p "middle02RGT_ctrl";
	rename -uid "82C0D56C-4C61-CFE7-CA58-ACA4A257AFC1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1336983947431853 4.0883771385803589e-05 0.44232801322605314
		1.5914412990612947 4.0884309083427584e-05 0.62568396219944689
		2.0447666456346218 4.0883749411566204e-05 0.43166308540606119
		2.2281225946081955 4.0882419838884496e-05 -0.0260798189120541
		2.034101717814635 4.0881099108425789e-05 -0.47940516548540024
		1.5763588134965405 4.0880561235708266e-05 -0.6627611144587926
		1.1230334669231843 4.0881121257756694e-05 -0.46874023766540812
		0.93967751794980015 4.0882450699118264e-05 -0.010997333347291423
		1.1336983947431853 4.0883771385803589e-05 0.44232801322605314
		1.5914412990612947 4.0884309083427584e-05 0.62568396219944689
		2.0447666456346218 4.0883749411566204e-05 0.43166308540606119
		;
createNode transform -n "middle03RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "6C3DF05B-47CA-7344-100C-5FBD02450A93";
createNode transform -n "middle03RGT_ctrl" -p "middle03RGT_Zro_grp";
	rename -uid "52FFC4AD-4378-2515-7CC4-18B618F8930D";
	setAttr ".rp" -type "double3" 0.00015678857867411686 3.9471195304878039e-05 8.6916177143620969e-07 ;
	setAttr ".sp" -type "double3" 0.00015678857867411686 3.9471195304878039e-05 8.6916177143620969e-07 ;
createNode nurbsCurve -n "middle03RGT_ctrlShape" -p "middle03RGT_ctrl";
	rename -uid "E8B7ACD1-49A4-EC80-9A69-CD9418F3F123";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0108756169332547 3.9472267147186585e-05 0.36504677593476248
		1.3895284610260603 3.9472711578326296e-05 0.51672198683228676
		1.7645270249633724 3.9472248689410832e-05 0.35622456322222656
		1.9162022358607282 3.9471148430882293e-05 -0.022428280870585966
		1.7557048122506729 3.9470056139109142e-05 -0.39742684480772755
		1.3770519681578526 3.9469611314009007e-05 -0.54910205570525383
		1.0020534042209057 3.9470074742796167e-05 -0.38860463209519469
		0.85037819332317011 3.9471174490635261e-05 -0.0099517880023783662
		1.0108756169332547 3.9472267147186585e-05 0.36504677593476248
		1.3895284610260603 3.9472711578326296e-05 0.51672198683228676
		1.7645270249633724 3.9472248689410832e-05 0.35622456322222656
		;
createNode transform -n "index01LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "7A7DD2A6-495B-6714-F0B4-DEBADD8AD98B";
createNode transform -n "index01LFT_ctrl" -p "index01LFT_Zro_grp";
	rename -uid "7C1425C3-4C63-CED1-C66A-03B05A0760D5";
	setAttr ".rp" -type "double3" -3.9950505942926481e-09 -1.1811334981546642e-09 2.1372413805684899e-08 ;
	setAttr ".sp" -type "double3" -3.9950505942926481e-09 -1.1811334981546642e-09 2.1372413805684899e-08 ;
createNode nurbsCurve -n "index01LFT_ctrlShape" -p "index01LFT_ctrl";
	rename -uid "F0A32217-4797-FBE2-1D05-D8AAA157C03D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0929021837982611 -1.1924678389087238e-09 -0.43114736624541949
		-1.5398496693749053 -1.1970878136773832e-09 -0.60980587759031446
		-1.9822199121490951 -1.201660495907978e-09 -0.42009692459346343
		-2.1608784234939913 -1.2035072703662468e-09 0.026850560983179537
		-1.9711694704971388 -1.2015463216211832e-09 0.46922080375737013
		-1.5242219849204948 -1.1969263468525236e-09 0.6478793151022656
		-1.081851742146305 -1.192353664621929e-09 0.45817036210541434
		-0.90319323080140934 -1.1905068901636577e-09 0.011222876528770817
		-1.0929021837982611 -1.1924678389087238e-09 -0.43114736624541949
		-1.5398496693749053 -1.1970878136773832e-09 -0.60980587759031446
		-1.9822199121490951 -1.201660495907978e-09 -0.42009692459346343
		;
createNode transform -n "index02LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "64DD5F44-4223-7230-AE94-F2B3E8970B28";
createNode transform -n "index02LFT_ctrl" -p "index02LFT_Zro_grp";
	rename -uid "14E4B011-4F4B-F9F5-BBF2-678DFBB254C7";
	setAttr ".rp" -type "double3" -3.7897534362879109e-09 -1.9532922954056448e-09 2.3670962945943756e-08 ;
	setAttr ".sp" -type "double3" -3.7897534362879109e-09 -1.9532922954056448e-09 2.3670962945943756e-08 ;
createNode nurbsCurve -n "index02LFT_ctrlShape" -p "index02LFT_ctrl";
	rename -uid "C5D6926D-4A3D-5AAE-8BCB-95A1F1ABBF6F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.1341875024939709 -1.9705699247334081e-09 -0.44072298048428377
		-1.5921893437215393 -1.9775469172869547e-09 -0.62343117381363844
		-2.045239753931007 -1.9844485039052148e-09 -0.42876916856723057
		-2.2279479472603589 -1.9872318287491028e-09 0.029232672660336738
		-2.0332859420139533 -1.984266457873562e-09 0.48228308286980337
		-1.5752841007863858 -1.9772894653200137e-09 0.66499127619915932
		-1.1222336905769166 -1.9703878787017507e-09 0.47032927095275018
		-0.93952549724756174 -1.9676045538578623e-09 0.012327429725182922
		-1.1341875024939709 -1.9705699247334081e-09 -0.44072298048428377
		-1.5921893437215393 -1.9775469172869547e-09 -0.62343117381363844
		-2.045239753931007 -1.9844485039052148e-09 -0.42876916856723057
		;
createNode transform -n "index03LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "80F2EB54-44DB-3502-C25F-D3A131CD4734";
createNode transform -n "index03LFT_ctrl" -p "index03LFT_Zro_grp";
	rename -uid "4E10795A-43A2-2BF6-2AF5-0EA6EC521081";
	setAttr ".rp" -type "double3" -3.4316579955094944e-09 -3.7519414424075356e-09 2.4841952076989769e-08 ;
	setAttr ".sp" -type "double3" -3.4316579955094944e-09 -3.7519414424075356e-09 2.4841952076989769e-08 ;
createNode nurbsCurve -n "index03LFT_ctrlShape" -p "index03LFT_ctrl";
	rename -uid "B45111C6-4F91-2470-0D97-3AAA7787B918";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0096917467389295 -2.9085465404245378e-09 -0.36787719318016765
		-1.3879180030279539 -2.592613693396748e-09 -0.52061305993705387
		-1.7633649207869193 -2.2790024495481568e-09 -0.36116727640648344
		-1.9161007875438061 -2.1514220222125699e-09 0.017058979882538985
		-1.756655004013236 -2.2846072954298226e-09 0.39250589764150662
		-1.3784287477242156 -2.600540142457609e-09 0.54524176439839334
		-1.0029818299652451 -2.9141513863062036e-09 0.38579598086782274
		-0.8502459632083591 -3.0417318136417913e-09 0.0075697245788007199
		-1.0096917467389295 -2.9085465404245378e-09 -0.36787719318016765
		-1.3879180030279539 -2.592613693396748e-09 -0.52061305993705387
		-1.7633649207869193 -2.2790024495481568e-09 -0.36116727640648344
		;
createNode transform -n "middle01LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "48A8BB78-4125-9C9E-1BA5-3BB4D3834F7D";
createNode transform -n "middle01LFT_ctrl" -p "middle01LFT_Zro_grp";
	rename -uid "6A3E04B6-4080-2ACC-0761-38961DAAE218";
	setAttr ".rp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
createNode nurbsCurve -n "middle01LFT_ctrlShape" -p "middle01LFT_ctrl";
	rename -uid "AB9C936A-40AA-96A0-22BF-BEA62D6330A5";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0901875015684046 -0.026952990450859339 -0.4371361154626543
		-1.5360101960777439 -0.038115475544569212 -0.61823951831921609
		-1.9795566963832993 -0.027233070178781352 -0.43161424173695911
		-2.1610034781492042 -0.00068053982553290308 0.013417158343856166
		-1.9740614774659462 0.025988003349566701 0.45616132343777832
		-1.5282387829566095 0.037150488443276404 0.6372647262943405
		-1.0846922826510588 0.026268083077488714 0.45063944971208431
		-0.9032455008851461 -0.00028444727575980216 0.0056080496312680269
		-1.0901875015684046 -0.026952990450859339 -0.4371361154626543
		-1.5360101960777439 -0.038115475544569212 -0.61823951831921609
		-1.9795566963832993 -0.027233070178781352 -0.43161424173695911
		;
createNode transform -n "middle02LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "7A559C88-4642-0E60-3C52-02BA4DB86BF1";
createNode transform -n "middle02LFT_ctrl" -p "middle02LFT_Zro_grp";
	rename -uid "DF039B54-4E4F-6E82-173E-E4B0453CE9F5";
	setAttr ".rp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
createNode nurbsCurve -n "middle02LFT_ctrlShape" -p "middle02LFT_ctrl";
	rename -uid "E9D1A438-4357-5AEC-8FC8-6E835F9A0A43";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.1335628744200574 1.096468636699942e-09 -0.44232708258195175
		-1.5913057787480347 1.0920894204455842e-09 -0.62568303153073046
		-2.0446311253109455 1.0877524438944168e-09 -0.4316621547129707
		-2.2279870742597208 1.0859982490904219e-09 0.026080749615005581
		-2.0339661974419645 1.0878544195587324e-09 0.47940609617791918
		-1.5762232931139919 1.0922336358130915e-09 0.66276204512669834
		-1.1228979465510733 1.0965706123642556e-09 0.46874116830893869
		-0.93954199760229484 1.0983248071682559e-09 0.010998263980962344
		-1.1335628744200574 1.096468636699942e-09 -0.44232708258195175
		-1.5913057787480347 1.0920894204455842e-09 -0.62568303153073046
		-2.0446311253109455 1.0877524438944168e-09 -0.4316621547129707
		;
createNode transform -n "middle03LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "4DBEF8E2-4948-3BEE-4BBF-BA9C4900CBFC";
createNode transform -n "middle03LFT_ctrl" -p "middle03LFT_Zro_grp";
	rename -uid "40825196-45B0-09A7-C9A0-DFA03C896D7D";
	setAttr ".rp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
createNode nurbsCurve -n "middle03LFT_ctrlShape" -p "middle03LFT_ctrl";
	rename -uid "D4A79425-4E52-AA52-B3CD-60BB4E72AA15";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0107188330308834 1.0976036857398928e-09 -0.36504588134221677
		-1.3893716771236968 1.0939811223447386e-09 -0.51672109223974516
		-1.7643702410608362 1.0903935003623199e-09 -0.35622366862968358
		-1.9160454519583676 1.0889424000932724e-09 0.022429175463130231
		-1.7555480283483087 1.0904778563948335e-09 0.39742773940027204
		-1.3768951842554953 1.0941004197899879e-09 0.54910295029780054
		-1.0018966203183501 1.0976880417724068e-09 0.38860552668773934
		-0.85022140942082503 1.0991391420414605e-09 0.0099526825949251448
		-1.0107188330308834 1.0976036857398928e-09 -0.36504588134221677
		-1.3893716771236968 1.0939811223447386e-09 -0.51672109223974516
		-1.7643702410608362 1.0903935003623199e-09 -0.35622366862968358
		;
createNode transform -n "thumb01LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "E77366A4-4BB3-B3CD-F815-68A2866745A6";
createNode transform -n "thumb01LFT_ctrl" -p "thumb01LFT_Zro_grp";
	rename -uid "4399EA32-4D3A-A73E-AD30-37915B38E9AB";
	setAttr ".rp" -type "double3" -2.9439203906321374e-09 5.3528230229434663e-09 1.6710627530155718e-08 ;
	setAttr ".sp" -type "double3" -2.9439203906321374e-09 5.3528230229434663e-09 1.6710627530155718e-08 ;
createNode nurbsCurve -n "thumb01LFT_ctrlShape" -p "thumb01LFT_ctrl";
	rename -uid "1FEDD270-4260-4AA3-C3AB-BCB7241EA844";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.1616602474445268 0.051623702580986523 -0.1679395995196451
		-1.6372657028702644 0.072735022054913334 -0.23889508907897952
		-2.0235210108503292 0.093698196142086548 0.047545656850566546
		-2.0941630505085969 0.10223328177262837 0.52358953411972842
		-1.8078106730869523 0.093340541540182953 0.91037649570890744
		-1.332205217661214 0.072229222066256066 0.98133198526824061
		-0.94594990968114978 0.051266047979082879 0.69489123933869312
		-0.87530787002288224 0.042730962348541186 0.21884736206953279
		-1.1616602474445268 0.051623702580986523 -0.1679395995196451
		-1.6372657028702644 0.072735022054913334 -0.23889508907897952
		-2.0235210108503292 0.093698196142086548 0.047545656850566546
		;
createNode transform -n "thumb02LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "66EB3869-4F5F-B50D-4EBB-DE8AD923E907";
createNode transform -n "thumb02LFT_ctrl" -p "thumb02LFT_Zro_grp";
	rename -uid "5D39ECB1-45E1-A60D-83CF-C79119CDBC24";
	setAttr ".rp" -type "double3" -1.9689266880710376e-09 3.0822041497437502e-09 1.9249309745344834e-08 ;
	setAttr ".sp" -type "double3" -1.9689266880710376e-09 3.0822041497437502e-09 1.9249309745344834e-08 ;
createNode nurbsCurve -n "thumb02LFT_ctrlShape" -p "thumb02LFT_ctrl";
	rename -uid "F7035904-4EED-F26A-C33C-099E53A10C5E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.1876126378097158 3.1685525146105608e-09 -0.26494200421956526
		-1.6679016255878865 3.2049419460171958e-09 -0.37661321222116723
		-2.0864806942162812 3.1200056134081363e-09 -0.11596108047522312
		-2.1981519022178837 2.9634980684875381e-09 0.36432790730295
		-1.937499770471939 2.8270993084561703e-09 0.78290697593134484
		-1.457210782693769 2.7907098770495345e-09 0.89457818393294564
		-1.0386317140653736 2.8756462096585944e-09 0.63392605218700171
		-0.92696050606377178 3.032153754579193e-09 0.15363706440882915
		-1.1876126378097158 3.1685525146105608e-09 -0.26494200421956526
		-1.6679016255878865 3.2049419460171958e-09 -0.37661321222116723
		-2.0864806942162812 3.1200056134081363e-09 -0.11596108047522312
		;
createNode transform -n "thumb03LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "A1ABAA18-40CF-EBB0-0708-89923775A219";
createNode transform -n "thumb03LFT_ctrl" -p "thumb03LFT_Zro_grp";
	rename -uid "50A219CE-417C-A693-BFDF-0CBFEC3B00D0";
	setAttr ".rp" -type "double3" -1.4237729981369182e-09 3.082281665106359e-09 2.0678795283726441e-08 ;
	setAttr ".sp" -type "double3" -1.4237729981369182e-09 3.082281665106359e-09 2.0678795283726441e-08 ;
createNode nurbsCurve -n "thumb03LFT_ctrlShape" -p "thumb03LFT_ctrl";
	rename -uid "CFFAD807-4C52-D067-A296-28A12A360EE3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-1.0544519667459231 3.1497892776427663e-09 -0.20722477723612825
		-1.4517553208539715 3.179891239150323e-09 -0.29960113110919551
		-1.7980111629768702 3.1096304312127123e-09 -0.083985181476168125
		-1.8903875168499351 2.9801646822164986e-09 0.31331817263187878
		-1.6747715672169079 2.8673332720608752e-09 0.65957401475477284
		-1.2774682131088555 2.8372313105533176e-09 0.75195036862783993
		-0.93121237098596554 2.9074921184909241e-09 0.5363344189948126
		-0.83883601711289857 3.0369578674871378e-09 0.13903106488676592
		-1.0544519667459231 3.1497892776427663e-09 -0.20722477723612825
		-1.4517553208539715 3.179891239150323e-09 -0.29960113110919551
		-1.7980111629768702 3.1096304312127123e-09 -0.083985181476168125
		;
createNode transform -n "thumb01RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "9305110F-4EA2-CCCB-D2BF-D0A6D115A751";
	setAttr ".sp" -type "double3" 0 0 -3.6477817698070209e-15 ;
createNode transform -n "thumb01RGT_ctrl" -p "thumb01RGT_Zro_grp";
	rename -uid "E8CFDD3A-45DC-8CBE-987F-E1A594F14463";
	setAttr ".rp" -type "double3" -0.00021786125293844945 -0.00011590463622923497 6.1617136254591963e-05 ;
	setAttr ".sp" -type "double3" -0.00021786125293844945 -0.00011590463622923497 6.1617136254591963e-05 ;
createNode nurbsCurve -n "thumb01RGT_ctrlShape" -p "thumb01RGT_ctrl";
	rename -uid "5A47C0A9-487E-29E3-7030-ECACD4F0790F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1614423832476304 -0.051739601864934801 0.16800123336643202
		1.6370478386733311 -0.072850921338831795 0.23895672292576273
		2.0233031466534186 -0.09381409542584733 -0.047484023003760034
		2.0939451863116822 -0.10234918105652882 -0.52352790027294527
		1.8075928088900424 -0.093456440824157661 -0.91031486186214761
		1.3319873534643274 -0.07234512135014394 -0.98127035142136176
		0.94573204548426171 -0.051381947262975194 -0.69482960549191908
		0.8750900058259834 -0.042846861632476099 -0.21878572822277031
		1.1614423832476304 -0.051739601864934801 0.16800123336643202
		1.6370478386733311 -0.072850921338831795 0.23895672292576273
		2.0233031466534186 -0.09381409542584733 -0.047484023003760034
		;
createNode transform -n "thumb02RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "8C7C0AC0-47B2-E1D4-7E34-53991320C728";
	setAttr ".sp" -type "double3" 0 -3.6477817698070209e-15 0 ;
createNode transform -n "thumb02RGT_ctrl" -p "thumb02RGT_Zro_grp";
	rename -uid "7D4FFAD2-40F8-1CFA-4488-46B5B7D647B7";
	setAttr ".rp" -type "double3" -1.1832315067075544e-05 1.9991630574129766e-05 -9.6300105969357936e-06 ;
	setAttr ".sp" -type "double3" -1.1832315067075544e-05 1.9991630574129766e-05 -9.6300105969357936e-06 ;
createNode nurbsCurve -n "thumb02RGT_ctrlShape" -p "thumb02RGT_ctrl";
	rename -uid "6D334AB1-4159-A8C1-F8B0-70BADA4ED08F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1876008035324521 1.9988372065391523e-05 0.26493239342856451
		1.6678897913133259 1.9987052969139051e-05 0.37660360141813021
		2.0864688599352426 1.9986023360847834e-05 0.11595146966181831
		2.1981400679247649 1.9985886714942736e-05 -0.36433751811929638
		1.9374879361683359 1.9986722509292962e-05 -0.78291658674115838
		1.4571989483874292 1.9988041663909941e-05 -0.89458779473066574
		1.0386198797654942 1.9989071418112429e-05 -0.63393566297426618
		0.92694867177593243 1.9989208093199781e-05 -0.15364667519331204
		1.1876008035324521 1.9988372065391523e-05 0.26493239342856451
		1.6678897913133259 1.9987052969139051e-05 0.37660360141813021
		2.0864688599352426 1.9986023360847834e-05 0.11595146966181831
		;
createNode transform -n "thumb03RGT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "4AF7A977-47D6-6EBD-904E-AB86DFC6B289";
	setAttr ".rp" -type "double3" 0 7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" 0 7.2955635396140418e-15 0 ;
createNode transform -n "thumb03RGT_ctrl" -p "thumb03RGT_Zro_grp";
	rename -uid "6A8F268E-4D45-33A0-4D00-C7B1B36E413E";
	setAttr ".rp" -type "double3" 6.9766701120598681e-05 4.7022710770836411e-05 -1.8964515567285252e-05 ;
	setAttr ".sp" -type "double3" 6.9766701120598681e-05 4.7022710770836411e-05 -1.8964515567285252e-05 ;
createNode nurbsCurve -n "thumb03RGT_ctrlShape" -p "thumb03RGT_ctrl";
	rename -uid "6BD7D41D-4831-61FF-67D3-82A2256F3205";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.0545217320232669 4.7019829380720872e-05 0.20720583339936466
		1.4518250861313065 4.7018739073341009e-05 0.29958218727241126
		1.7980809282542092 4.7017885288131093e-05 0.083966237639302221
		1.8904572821272667 4.7017768223518539e-05 -0.31333711646866441
		1.6748413324942086 4.701845645780061e-05 -0.6595929585917093
		1.2775379783861947 4.7019546808953861e-05 -0.75196931246462451
		0.93128213626325562 4.7020400564981521e-05 -0.53635336283158852
		0.83890578239023816 4.7020517585820693e-05 -0.13905000872354886
		1.0545217320232669 4.7019829380720872e-05 0.20720583339936466
		1.4518250861313065 4.7018739073341009e-05 0.29958218727241126
		1.7980809282542092 4.7017885288131093e-05 0.083966237639302221
		;
createNode transform -n "TMP_NULL_GRP" -p "TMP_GRP";
	rename -uid "913A9F28-4B1F-3BD4-2860-B38A74FB2417";
createNode transform -n "fingerRGT_Zro_grp" -p "TMP_NULL_GRP";
	rename -uid "D5CE9665-4611-B5BE-87D4-379A7399AD44";
createNode transform -n "fingerLFT_Zro_grp" -p "TMP_NULL_GRP";
	rename -uid "B88D8B6D-4740-45C9-F612-428A0284B4D3";
createNode transform -n "ankleLFT_IK_Zro_grp_Bak" -p "TMP_NULL_GRP";
	rename -uid "40011683-4125-F96E-13B0-C2BC39BD9A1C";
createNode transform -n "TMP_ARM_IK_GRP" -p "TMP_GRP";
	rename -uid "FF24817D-4E77-65F5-E54F-62BCE9B65838";
createNode transform -n "armLFT_pov_Zro_grp" -p "TMP_ARM_IK_GRP";
	rename -uid "D59D3722-4E58-C3DF-807B-2EA510CC39B6";
createNode transform -n "armLFT_pov_ctrl" -p "armLFT_pov_Zro_grp";
	rename -uid "312BF567-4E16-99E7-B130-7D862F75CCAE";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "armLFT_pov_ctrlShape" -p "armLFT_pov_ctrl";
	rename -uid "F6D2D618-4F54-59C0-5B9D-3DB97BCBB15A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 1.7991854165801995 0
		0 -1.7991854165801995 0
		0 0 0
		0 0 -1.7991854165801995
		0 0 1.7991854165801995
		0 0 0
		1.7991854165801995 0 0
		-1.7991854165801995 0 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0.22516301716584575 0
		-1.3689023077892113 0.44478310390029102 0
		-1.2824694403766994 0.65345118916692957 0
		-1.1644572705323701 0.84602736006767465 0
		-1.0177732818894205 1.0177732818894205 0
		-0.84602736006767465 1.1644572705323701 0
		-0.65345118916692957 1.2824694403766994 0
		-0.44478310390029102 1.3689023077892113 0
		-0.22516445651417891 1.4216270765850112 0
		0 1.4393483332641601 0
		0.22516301716584575 1.4216270765850112 0
		0.44478310390029102 1.3689023077892113 0
		0.65345118916692957 1.2824694403766994 0
		0.84602736006767465 1.1644572705323701 0
		1.0177732818894205 1.0177732818894205 0
		1.1644572705323701 0.84602736006767465 0
		1.2824694403766994 0.65345118916692957 0
		1.3689023077892113 0.44478310390029102 0
		1.4216270765850112 0.22516301716584575 0
		1.4393483332641601 0 0
		1.4216270765850112 -0.22516301716584575 0
		1.3689023077892113 -0.44478310390029102 0
		1.2824694403766994 -0.65345118916692957 0
		1.1644572705323701 -0.84602736006767465 0
		1.0177732818894205 -1.0177732818894205 0
		0.84602736006767465 -1.1644572705323701 0
		0.65345118916692957 -1.2824694403766994 0
		0.44478310390029102 -1.3689023077892113 0
		0.22516301716584575 -1.4216270765850112 0
		0 -1.4393483332641601 0
		-0.22516445651417891 -1.4216270765850112 0
		-0.44478310390029102 -1.3689023077892113 0
		-0.65345118916692957 -1.2824694403766994 0
		-0.84602736006767465 -1.1644572705323701 0
		-1.0177732818894205 -1.0177732818894205 0
		-1.1644572705323701 -0.84602736006767465 0
		-1.2824694403766994 -0.65345118916692957 0
		-1.3689023077892113 -0.44478310390029102 0
		-1.4216285159333439 -0.22516301716584575 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		0.22516301716584575 0 1.4216270765850112
		0.44478310390029102 0 1.3689023077892113
		0.65345118916692957 0 1.2824694403766994
		0.84602736006767465 0 1.1644572705323701
		1.0177732818894205 0 1.0177732818894205
		1.1644572705323701 0 0.84602736006767465
		1.2824694403766994 0 0.65345118916692957
		1.3689023077892113 0 0.44478310390029102
		1.4216270765850112 0 0.22516301716584575
		1.4393483332641601 0 0
		1.4216270765850112 0 -0.22516301716584575
		1.3689023077892113 0 -0.44478310390029102
		1.2824694403766994 0 -0.65345118916692957
		1.1644572705323701 0 -0.84602736006767465
		1.0177732818894205 0 -1.0177732818894205
		0.84602736006767465 0 -1.1644572705323701
		0.65345118916692957 0 -1.2824694403766994
		0.44478310390029102 0 -1.3689023077892113
		0.22516301716584575 0 -1.4216270765850112
		0 0 -1.4393483332641601
		-0.22516445651417891 0 -1.4216270765850112
		-0.44478310390029102 0 -1.3689023077892113
		-0.65345118916692957 0 -1.2824694403766994
		-0.84602736006767465 0 -1.1644572705323701
		-1.0177732818894205 0 -1.0177732818894205
		-1.1644572705323701 0 -0.84602736006767465
		-1.2824694403766994 0 -0.65345118916692957
		-1.3689023077892113 0 -0.44478310390029102
		-1.4216285159333439 0 -0.22516301716584575
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		-6.7104002579941741e-09 0.22516301716584575 1.4216270765850112
		-1.3255563327329612e-08 0.44478310390029102 1.3689023077892113
		-1.947438294906409e-08 0.65345118916692957 1.2824694403766994
		-2.5213640493121609e-08 0.84602736006767465 1.1644572705323701
		-3.0331963166208942e-08 1.0177732818894205 1.0177732818894205
		-3.4703551923998864e-08 1.1644572705323701 0.84602736006767465
		-3.822059957632979e-08 1.2824694403766994 0.65345118916692957
		-4.0796457353539337e-08 1.3689023077892113 0.44478310390029102
		-4.2367793928963873e-08 1.4216270765850112 0.22516301716584575
		-4.2895890832438451e-08 1.4393483332641601 0
		-4.2367793928963873e-08 1.4216270765850112 -0.22516301716584575
		-4.0796457353539337e-08 1.3689023077892113 -0.44478310390029102
		-3.822059957632979e-08 1.2824694403766994 -0.65345118916692957
		-3.4703551923998864e-08 1.1644572705323701 -0.84602736006767465
		-3.0331963166208942e-08 1.0177732818894205 -1.0177732818894205
		-2.5213640493121609e-08 0.84602736006767465 -1.1644572705323701
		-1.947438294906409e-08 0.65345118916692957 -1.2824694403766994
		-1.3255563327329612e-08 0.44478310390029102 -1.3689023077892113
		-6.7104002579941741e-09 0.22516301716584575 -1.4216270765850112
		0 0 -1.4393483332641601
		0 -0.22516445651417891 -1.4216270765850112
		0 -0.44478310390029102 -1.3689023077892113
		0 -0.65345118916692957 -1.2824694403766994
		0 -0.84602879941600828 -1.1644572705323701
		0 -1.0177732818894205 -1.0177732818894205
		0 -1.1644572705323701 -0.84602736006767465
		0 -1.2824694403766994 -0.65345118916692957
		0 -1.3689023077892113 -0.44478310390029102
		0 -1.4216285159333439 -0.22516301716584575
		0 -1.4393483332641601 0
		0 -1.4216285159333439 0.22516301716584575
		0 -1.3689023077892113 0.44478310390029102
		0 -1.2824694403766994 0.65345118916692957
		0 -1.1644572705323701 0.84602736006767465
		0 -1.0177732818894205 1.0177732818894205
		0 -0.84602879941600828 1.1644572705323701
		0 -0.65345118916692957 1.2824694403766994
		0 -0.44478310390029102 1.3689023077892113
		0 -0.22516445651417891 1.4216270765850112
		0 0 1.4393483332641601
		;
createNode transform -n "armRGT_pov_Zro_grp" -p "TMP_ARM_IK_GRP";
	rename -uid "6A900203-4B7D-56F6-946F-439BFA9FAA3E";
createNode transform -n "armRGT_pov_ctrl" -p "armRGT_pov_Zro_grp";
	rename -uid "48F9A239-4163-5FEA-64B2-5C9154C7FD3D";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "armRGT_pov_ctrlShape" -p "armRGT_pov_ctrl";
	rename -uid "F8A0ED46-4D52-2A3E-4114-04A5C3F3958A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 1.7991854165801995 0
		0 -1.7991854165801995 0
		0 0 0
		0 0 -1.7991854165801995
		0 0 1.7991854165801995
		0 0 0
		1.7991854165801995 0 0
		-1.7991854165801995 0 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0.22516301716584575 0
		-1.3689023077892113 0.44478310390029102 0
		-1.2824694403766994 0.65345118916692957 0
		-1.1644572705323701 0.84602736006767465 0
		-1.0177732818894205 1.0177732818894205 0
		-0.84602736006767465 1.1644572705323701 0
		-0.65345118916692957 1.2824694403766994 0
		-0.44478310390029102 1.3689023077892113 0
		-0.22516445651417891 1.4216270765850112 0
		0 1.4393483332641601 0
		0.22516301716584575 1.4216270765850112 0
		0.44478310390029102 1.3689023077892113 0
		0.65345118916692957 1.2824694403766994 0
		0.84602736006767465 1.1644572705323701 0
		1.0177732818894205 1.0177732818894205 0
		1.1644572705323701 0.84602736006767465 0
		1.2824694403766994 0.65345118916692957 0
		1.3689023077892113 0.44478310390029102 0
		1.4216270765850112 0.22516301716584575 0
		1.4393483332641601 0 0
		1.4216270765850112 -0.22516301716584575 0
		1.3689023077892113 -0.44478310390029102 0
		1.2824694403766994 -0.65345118916692957 0
		1.1644572705323701 -0.84602736006767465 0
		1.0177732818894205 -1.0177732818894205 0
		0.84602736006767465 -1.1644572705323701 0
		0.65345118916692957 -1.2824694403766994 0
		0.44478310390029102 -1.3689023077892113 0
		0.22516301716584575 -1.4216270765850112 0
		0 -1.4393483332641601 0
		-0.22516445651417891 -1.4216270765850112 0
		-0.44478310390029102 -1.3689023077892113 0
		-0.65345118916692957 -1.2824694403766994 0
		-0.84602736006767465 -1.1644572705323701 0
		-1.0177732818894205 -1.0177732818894205 0
		-1.1644572705323701 -0.84602736006767465 0
		-1.2824694403766994 -0.65345118916692957 0
		-1.3689023077892113 -0.44478310390029102 0
		-1.4216285159333439 -0.22516301716584575 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		0.22516301716584575 0 1.4216270765850112
		0.44478310390029102 0 1.3689023077892113
		0.65345118916692957 0 1.2824694403766994
		0.84602736006767465 0 1.1644572705323701
		1.0177732818894205 0 1.0177732818894205
		1.1644572705323701 0 0.84602736006767465
		1.2824694403766994 0 0.65345118916692957
		1.3689023077892113 0 0.44478310390029102
		1.4216270765850112 0 0.22516301716584575
		1.4393483332641601 0 0
		1.4216270765850112 0 -0.22516301716584575
		1.3689023077892113 0 -0.44478310390029102
		1.2824694403766994 0 -0.65345118916692957
		1.1644572705323701 0 -0.84602736006767465
		1.0177732818894205 0 -1.0177732818894205
		0.84602736006767465 0 -1.1644572705323701
		0.65345118916692957 0 -1.2824694403766994
		0.44478310390029102 0 -1.3689023077892113
		0.22516301716584575 0 -1.4216270765850112
		0 0 -1.4393483332641601
		-0.22516445651417891 0 -1.4216270765850112
		-0.44478310390029102 0 -1.3689023077892113
		-0.65345118916692957 0 -1.2824694403766994
		-0.84602736006767465 0 -1.1644572705323701
		-1.0177732818894205 0 -1.0177732818894205
		-1.1644572705323701 0 -0.84602736006767465
		-1.2824694403766994 0 -0.65345118916692957
		-1.3689023077892113 0 -0.44478310390029102
		-1.4216285159333439 0 -0.22516301716584575
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		-6.7104002579941741e-09 0.22516301716584575 1.4216270765850112
		-1.3255563327329612e-08 0.44478310390029102 1.3689023077892113
		-1.947438294906409e-08 0.65345118916692957 1.2824694403766994
		-2.5213640493121609e-08 0.84602736006767465 1.1644572705323701
		-3.0331963166208942e-08 1.0177732818894205 1.0177732818894205
		-3.4703551923998864e-08 1.1644572705323701 0.84602736006767465
		-3.822059957632979e-08 1.2824694403766994 0.65345118916692957
		-4.0796457353539337e-08 1.3689023077892113 0.44478310390029102
		-4.2367793928963873e-08 1.4216270765850112 0.22516301716584575
		-4.2895890832438451e-08 1.4393483332641601 0
		-4.2367793928963873e-08 1.4216270765850112 -0.22516301716584575
		-4.0796457353539337e-08 1.3689023077892113 -0.44478310390029102
		-3.822059957632979e-08 1.2824694403766994 -0.65345118916692957
		-3.4703551923998864e-08 1.1644572705323701 -0.84602736006767465
		-3.0331963166208942e-08 1.0177732818894205 -1.0177732818894205
		-2.5213640493121609e-08 0.84602736006767465 -1.1644572705323701
		-1.947438294906409e-08 0.65345118916692957 -1.2824694403766994
		-1.3255563327329612e-08 0.44478310390029102 -1.3689023077892113
		-6.7104002579941741e-09 0.22516301716584575 -1.4216270765850112
		0 0 -1.4393483332641601
		0 -0.22516445651417891 -1.4216270765850112
		0 -0.44478310390029102 -1.3689023077892113
		0 -0.65345118916692957 -1.2824694403766994
		0 -0.84602879941600828 -1.1644572705323701
		0 -1.0177732818894205 -1.0177732818894205
		0 -1.1644572705323701 -0.84602736006767465
		0 -1.2824694403766994 -0.65345118916692957
		0 -1.3689023077892113 -0.44478310390029102
		0 -1.4216285159333439 -0.22516301716584575
		0 -1.4393483332641601 0
		0 -1.4216285159333439 0.22516301716584575
		0 -1.3689023077892113 0.44478310390029102
		0 -1.2824694403766994 0.65345118916692957
		0 -1.1644572705323701 0.84602736006767465
		0 -1.0177732818894205 1.0177732818894205
		0 -0.84602879941600828 1.1644572705323701
		0 -0.65345118916692957 1.2824694403766994
		0 -0.44478310390029102 1.3689023077892113
		0 -0.22516445651417891 1.4216270765850112
		0 0 1.4393483332641601
		;
createNode transform -n "handLFT_IK_Zro_grp" -p "TMP_ARM_IK_GRP";
	rename -uid "8F98DF76-486A-A3BF-3532-8C9F15077829";
createNode transform -n "handLFT_IK_ctrl" -p "handLFT_IK_Zro_grp";
	rename -uid "4E38C47C-42C8-FE68-55DA-3FBED24F6F86";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr ".rp" -type "double3" -7.2955635396140418e-15 0 -3.6477817698070209e-15 ;
	setAttr ".sp" -type "double3" -7.2955635396140418e-15 0 -3.6477817698070209e-15 ;
	setAttr -l on -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "handLFT_IK_ctrlShape" -p "handLFT_IK_ctrl";
	rename -uid "A01B7ABA-40CD-35DB-9067-2AB68A5E8424";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-1.0747258225877672 3.3538214121242755 -3.3538214121242773
		-1.0747258225877707 3.3538214121242755 3.3538214121242738
		1.0747258225877525 3.3538214121242755 3.3538214121242738
		1.0747258225877525 3.3538214121242755 -3.3538214121242773
		-1.0747258225877672 3.3538214121242755 -3.3538214121242773
		-1.0747258225877672 -3.3538214121242755 -3.3538214121242773
		-1.0747258225877707 -3.3538214121242755 3.3538214121242738
		1.0747258225877525 -3.3538214121242755 3.3538214121242738
		1.0747258225877525 3.3538214121242755 3.3538214121242738
		-1.0747258225877707 3.3538214121242755 3.3538214121242738
		-1.0747258225877707 -3.3538214121242755 3.3538214121242738
		-1.0747258225877672 -3.3538214121242755 -3.3538214121242773
		1.0747258225877525 -3.3538214121242755 -3.3538214121242773
		1.0747258225877525 3.3538214121242755 -3.3538214121242773
		1.0747258225877525 3.3538214121242755 3.3538214121242738
		1.0747258225877525 -3.3538214121242755 3.3538214121242738
		1.0747258225877525 -3.3538214121242755 -3.3538214121242773
		;
createNode transform -n "handRGT_IK_Zro_grp" -p "TMP_ARM_IK_GRP";
	rename -uid "806F4559-46E5-2125-D4D7-838FCB517123";
createNode transform -n "handRGT_IK_ctrl" -p "handRGT_IK_Zro_grp";
	rename -uid "74371500-46C2-8D51-5362-DA817C2BF81E";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr ".rp" -type "double3" 0 0 -4.5597272122587763e-15 ;
	setAttr ".sp" -type "double3" 0 0 -4.5597272122587763e-15 ;
	setAttr -l on -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "handRGT_IK_ctrlShape" -p "handRGT_IK_ctrl";
	rename -uid "31D3F633-4790-7963-3840-5A85D5E0058B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-1.0747258225877598 3.3538214121242755 -3.3538214121242773
		-1.0747258225877634 3.3538214121242755 3.3538214121242738
		1.0747258225877598 3.3538214121242755 3.3538214121242738
		1.0747258225877598 3.3538214121242755 -3.3538214121242773
		-1.0747258225877598 3.3538214121242755 -3.3538214121242773
		-1.0747258225877598 -3.3538214121242755 -3.3538214121242773
		-1.0747258225877634 -3.3538214121242755 3.3538214121242738
		1.0747258225877598 -3.3538214121242755 3.3538214121242738
		1.0747258225877598 3.3538214121242755 3.3538214121242738
		-1.0747258225877634 3.3538214121242755 3.3538214121242738
		-1.0747258225877634 -3.3538214121242755 3.3538214121242738
		-1.0747258225877598 -3.3538214121242755 -3.3538214121242773
		1.0747258225877598 -3.3538214121242755 -3.3538214121242773
		1.0747258225877598 3.3538214121242755 -3.3538214121242773
		1.0747258225877598 3.3538214121242755 3.3538214121242738
		1.0747258225877598 -3.3538214121242755 3.3538214121242738
		1.0747258225877598 -3.3538214121242755 -3.3538214121242773
		;
createNode transform -n "heelRollLFT_IK_Zro_grp" -p "TMP_GRP";
	rename -uid "96670B71-41B3-3C7B-36DF-3EA154C1D8F6";
	setAttr ".rp" -type "double3" 1.7804609897635273e-14 -2.9980837649287912e-05 -1.966978232882344 ;
	setAttr ".sp" -type "double3" 1.7804609897635273e-14 -2.9980837649287912e-05 -1.966978232882344 ;
createNode transform -n "heelRollLFT_IK_ctrl" -p "heelRollLFT_IK_Zro_grp";
	rename -uid "3966852B-4854-1DB8-37C0-ECA8C7EDC779";
	setAttr ".rp" -type "double3" 1.9628500782578596e-14 -2.9980837649287912e-05 -1.966978232882344 ;
	setAttr ".sp" -type "double3" 1.9628500782578596e-14 -2.9980837649287912e-05 -1.966978232882344 ;
	setAttr ".hdl" -type "double3" 3.8233889867979948e-16 -5.8398960650629661e-07 -0.038314301210149608 ;
createNode nurbsCurve -n "heelRollLFT_IK_ctrlShape" -p "heelRollLFT_IK_ctrl";
	rename -uid "1B1CE26E-4DBC-B550-87D8-29B8E9BB21B4";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.1882832366308287e-06 -0.83365449695924454 -1.9669789818532453
		1.1882280959921423e-06 -0.55577988181672089 -2.5104435293169653
		1.1881178143585409e-06 -3.0300995581501172e-05 -2.7821756277807763
		1.1880075330811682e-06 0.55571951351628446 -2.5104430619355087
		1.1879523920862531e-06 0.8335945960402652 -1.9669782807810599
		1.1880075327249394e-06 0.55571998089774166 -1.4235137333173478
		1.1881178143585409e-06 -2.9599923396723975e-05 -1.1517816348535415
		1.1882280959921423e-06 -0.55577941443526302 -1.4235142006988046
		1.1882832366308287e-06 -0.83365449695924454 -1.9669789818532453
		-0.54346347607653467 -0.55577964823383519 -1.9669788650078808
		-0.81519580833913086 -2.9950621255766059e-05 -1.9669786313171524
		-0.54346347629709768 0.55571974709916871 -1.9669783976264239
		1.1879523920862531e-06 0.8335945960402652 -1.9669782807810599
		0.54346585231216393 0.55571974731485663 -1.9669783976264239
		0.81519818457476068 -2.9950297724596458e-05 -1.9669786313171524
		0.54346585253272683 -0.55577964801814739 -1.9669788650078808
		1.1882832366308287e-06 -0.83365449695924454 -1.9669789818532453
		;
createNode transform -n "footInLFT_IK_Zro_grp" -p "TMP_GRP";
	rename -uid "F8247A2C-433B-1D49-67D3-D3AFCAC426EC";
	setAttr ".rp" -type "double3" 0.5782442789967831 5.5414489490621868e-11 1.0082424592654509e-15 ;
	setAttr ".sp" -type "double3" 0.5782442789967831 5.5414489490621868e-11 1.0082424592654509e-15 ;
createNode transform -n "footInLFT_IK_ctrl" -p "footInLFT_IK_Zro_grp";
	rename -uid "EFC52EC2-4CEB-C043-02D7-32A49CB05D8C";
	setAttr ".rp" -type "double3" 0.57824427899678266 5.5414489490621868e-11 1.0652390494199298e-15 ;
	setAttr ".sp" -type "double3" 0.57824427899678266 5.5414489490621868e-11 1.0652390494199298e-15 ;
	setAttr ".hdl" -type "double3" 0.011263482792111677 1.0794056620744286e-12 2.0749538107740686e-17 ;
createNode nurbsCurve -n "footInLFT_IK_ctrlShape" -p "footInLFT_IK_ctrl";
	rename -uid "E87BD5B0-43E2-8072-93C3-868B75BDC633";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		0.57817921658873583 -0.81519699391706069 -1.2106703378967527e-09
		0.57821148279465884 -0.5434646625929036 -0.54346466501342372
		0.57826015767305083 5.5414934776482439e-11 -0.81519699630945819
		0.57829826086247393 0.54346466270372917 -0.54346466339918698
		0.57830938369045903 0.81519699402788914 1.2106845814782178e-09
		0.57827711748453636 0.54346466270372917 0.54346466501342994
		0.57822844260614392 5.5414934776482439e-11 0.8151969963094603
		0.57819033941672082 -0.54346466259290216 0.54346466339919319
		0.57817921658873583 -0.81519699391706069 -1.2106703378967527e-09
		0.022451215229047524 -0.54342223268812573 -1.033880532007893e-05
		-0.25538024367536638 6.3644912578140946e-05 -1.5506997306176465e-05
		0.022537993296862617 0.5435070926085056 -1.0337191083453024e-05
		0.57830938369045903 0.81519699402788914 1.2106845814782178e-09
		1.1340373850501482 0.54342223279895419 1.0338805334322509e-05
		1.4118688439545619 -6.3644801749696312e-05 1.5506997320492406e-05
		1.1339506069823329 -0.54350709249767726 1.0337191097707739e-05
		0.57817921658873583 -0.81519699391706069 -1.2106703378967527e-09
		;
createNode transform -n "footOutLFT_IK_Zro_grp" -p "TMP_GRP";
	rename -uid "04857DD3-4691-898B-8D21-BFACE26838BD";
	setAttr ".rp" -type "double3" -0.41504239050203406 -1.3009206668331607e-10 3.645632475272038e-05 ;
	setAttr ".sp" -type "double3" -0.41504239050203406 -1.3009206668331607e-10 3.645632475272038e-05 ;
createNode transform -n "footOutLFT_IK_ctrl" -p "footOutLFT_IK_Zro_grp";
	rename -uid "993018DB-43E1-5395-2105-A1B986EA5DC0";
	setAttr ".rp" -type "double3" -0.41504239050203356 -1.3009220917479147e-10 3.6456324751829809e-05 ;
	setAttr ".sp" -type "double3" -0.41504239050203356 -1.3009220917479147e-10 3.6456324751829809e-05 ;
	setAttr ".hdl" -type "double3" -0.0080845120189119261 -2.5340352038938364e-12 7.1012407977175118e-07 ;
createNode nurbsCurve -n "footOutLFT_IK_ctrlShape" -p "footOutLFT_IK_ctrl";
	rename -uid "EC3A3287-459B-0A6C-D5E1-D4AFEC6EEB76";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.41504240573804224 2.3557581282053047e-11 -0.81516054013197914
		-0.41505297742701075 0.54346466417865114 -0.54342820787722446
		-0.4150582632714957 0.81519699617936681 3.6456478623564987e-05
		-0.41505297742701142 0.54346466397377602 0.54350112073203583
		-0.41504240573804302 -2.8375503047705977e-10 0.81523345278191495
		-0.41503183404907379 -0.54346466443884056 0.5435011205271616
		-0.41502654820458923 -0.81519699643955124 3.6456171310775113e-05
		-0.41503183404907346 -0.54346466423396544 -0.54342820808210002
		-0.41504240573804224 2.3557581282053047e-11 -0.81516054013197914
		-0.97079210330844079 -1.0338025901454779e-05 -0.54342820797966307
		-1.2486669520936398 -1.5507127459214806e-05 3.645632496645759e-05
		-0.97079210330844123 -1.0338230776588657e-05 0.54350112062959732
		-0.41504240573804302 -2.8375503047705977e-10 0.81523345278191495
		0.14070729183235606 1.0337765704005582e-05 0.54350112062960021
		0.41858214061755505 1.550686726176561e-05 3.6456324970732335e-05
		0.14070729183235642 1.0337970579139461e-05 -0.54342820797966007
		-0.41504240573804224 2.3557581282053047e-11 -0.81516054013197914
		;
createNode transform -n "look" -p "TMP_GRP";
	rename -uid "4BD5FCE1-477A-A84D-A236-3AAECD95DD6D";
createNode transform -n "ballRollLFT_FK_Zro_grp" -p "look";
	rename -uid "8B7C9783-4A3A-FFEC-D146-6A83788323B7";
createNode transform -n "ballRollLFT_FK_ctrl" -p "ballRollLFT_FK_Zro_grp";
	rename -uid "7C2391EE-4441-0B0B-167B-C9B4DBA6A5D8";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 3.551952682345486e-07 2.0514950947787893e-08 2.3847975888064485e-08 ;
	setAttr ".sp" -type "double3" 3.551952682345486e-07 2.0514950947787893e-08 2.3847975888064485e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "ballRollLFT_FK_ctrlShape" -p "ballRollLFT_FK_ctrl";
	rename -uid "DFDB8433-4FA5-D2D6-086C-5A93B6E9FF85";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.8013809190361956 1.4688810550376148 0.29654561039448712
		-0.11703715556323878 1.3908821223507168 -1.065542863125621
		3.2217542535787733 1.1830184606300838 -0.086940650540908104
		7.0929416015415869 0.999286655003778 -0.33335939425129241
		5.0412256213204483 0.88448378871209343 4.9133132642355379
		0.45595482991456393 0.97611062223568013 8.2432016814738631
		-3.9934768040881705 1.3132776644945705 5.4885426344041681
		-6.2835974071747618 1.6341474103477565 0.51830984140392389
		-2.8013809190361956 1.4688810550376148 0.29654561039448712
		-0.11703715556323878 1.3908821223507168 -1.065542863125621
		3.2217542535787733 1.1830184606300838 -0.086940650540908104
		;
createNode transform -n "ballRollLFT_FK_Gimbal_ctrl" -p "ballRollLFT_FK_ctrl";
	rename -uid "7B7AC032-4037-AB6F-DCCE-F08CFAC3BDAF";
	setAttr ".rp" -type "double3" 3.5519526823454855e-07 2.0514950947787899e-08 2.3847975888064495e-08 ;
	setAttr ".sp" -type "double3" 3.5519526823454855e-07 2.0514950947787899e-08 2.3847975888064495e-08 ;
createNode nurbsCurve -n "ballRollLFT_FK_Gimbal_ctrlShape" -p "ballRollLFT_FK_Gimbal_ctrl";
	rename -uid "75314464-42C4-2B0B-69A1-AAAA5AB78C73";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.3811737279014764 1.2485488998592149 0.2520637724125106
		-0.09948152894946273 1.1822498070753518 -0.9057114300795811
		2.7384911688212474 1.0055656946128142 -0.073899549382575591
		6.0290004145896381 0.84939365983045401 -0.28335548153640217
		4.2850418314016716 0.75181122348252261 4.1763162781774055
		0.38756165870666942 0.82969403197757075 7.0067214328299796
		-3.3944552301956548 1.1162860178976273 4.6652612428207387
		-5.3410577428192578 1.3890253018728353 0.44056336877053165
		-2.3811737279014764 1.2485488998592149 0.2520637724125106
		-0.09948152894946273 1.1822498070753518 -0.9057114300795811
		2.7384911688212474 1.0055656946128142 -0.073899549382575591
		;
createNode transform -n "ankleLFT_FK_Zro_grp" -p "look";
	rename -uid "51A196E5-4809-D8F9-08D7-80A0A18517D9";
createNode transform -n "ankleLFT_FK_ctrl" -p "ankleLFT_FK_Zro_grp";
	rename -uid "68C9CA68-4F27-F8AE-3E38-5A83D9480F49";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -2.1085844389029747e-07 2.9710690976484702e-08 -3.2627855343808004e-09 ;
	setAttr ".sp" -type "double3" -2.1085844389029747e-07 2.9710690976484702e-08 -3.2627855343808004e-09 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "ankleLFT_FK_ctrlShape" -p "ankleLFT_FK_ctrl";
	rename -uid "C8251699-41EA-C5DE-5C32-15AE4FAB8978";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.7011112816764085 0.664512945714956 2.9299435902293363
		-0.96282170026641345 -1.8091891471139716 7.1247317367689265
		2.6257634149872815 1.1029631595270353 3.3318212043250557
		5.6187171336806827 1.7429055466140804 -0.32531165569192322
		2.9683094941264745 1.9917649562799014 -4.3409059531273657
		-0.5712909276708229 1.9374386083237312 -6.2643312517414662
		-2.9943955480915441 1.5785515727372397 -4.7196518254277757
		-4.9229747261712831 3.4306690083147187 -0.71693732020026946
		-3.7011112816764085 0.664512945714956 2.9299435902293363
		-0.96282170026641345 -1.8091891471139716 7.1247317367689265
		2.6257634149872815 1.1029631595270353 3.3318212043250557
		;
createNode transform -n "ankleLFT_FK_Gimbal_ctrl" -p "ankleLFT_FK_ctrl";
	rename -uid "DDE4B74D-43EB-E8B3-0DB0-B5A1A80251DC";
	setAttr ".rp" -type "double3" -2.1085844389029744e-07 2.9710690976484702e-08 -3.2627855343807988e-09 ;
	setAttr ".sp" -type "double3" -2.1085844389029744e-07 2.9710690976484702e-08 -3.2627855343807988e-09 ;
createNode nurbsCurve -n "ankleLFT_FK_Gimbal_ctrlShape" -p "ankleLFT_FK_Gimbal_ctrl";
	rename -uid "2BA5ACE5-4E1B-F464-2A3B-6082DD8AEFA0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.1459446210537143 0.56483600831431613 2.4904520512055175
		-0.81839847685521805 -1.5378107705902724 6.0560219757641702
		2.2318988711104222 0.93751869005458377 2.8320480231868794
		4.7759095319998144 1.4814697190785717 -0.2765149078275525
		2.5230630383787371 1.6930002172945198 -3.6897700606476782
		-0.48559732014896601 1.6468228215317753 -5.3246815644696639
		-2.5452362475065788 1.3417688412832576 -4.0117040521030276
		-4.1845285488743569 2.9160686615241143 -0.60939672265964684
		-3.1459446210537143 0.56483600831431613 2.4904520512055175
		-0.81839847685521805 -1.5378107705902724 6.0560219757641702
		2.2318988711104222 0.93751869005458377 2.8320480231868794
		;
createNode transform -n "TMP_FOOT_IK_GRP" -p "look";
	rename -uid "9BD300EE-4961-C607-0356-E9A23618B80D";
createNode transform -n "toesRollRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "188541F7-493A-7D23-E74D-52B79B44C454";
	setAttr ".rp" -type "double3" 1.1881178101550423e-06 3.0378010915517757e-08 1.2974008952765999 ;
	setAttr ".sp" -type "double3" 1.1881178101550423e-06 3.0378010915517757e-08 1.2974008952765999 ;
createNode transform -n "toesRollRGT_IK_ctrl" -p "toesRollRGT_IK_Zro_grp";
	rename -uid "D4889543-4431-B0A7-2FCC-B0AF3813BE79";
	setAttr ".rp" -type "double3" 1.1881178101550423e-06 3.0378008956259975e-08 1.2974008952765999 ;
	setAttr ".sp" -type "double3" 1.1881178101550423e-06 3.0378008956259975e-08 1.2974008952765999 ;
	setAttr ".hdl" -type "double3" 2.3143064264985471e-08 5.9172601193924201e-10 0.025271763490287074 ;
createNode nurbsCurve -n "toesRollRGT_IK_ctrlshape" -p "toesRollRGT_IK_ctrl";
	rename -uid "7698A4D4-44F5-673A-9366-D0B7AE81BD02";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.1881178141804266e-06 -0.83362451597758969 1.297416429729757
		1.1881178145366552e-06 -0.55573909550341971 1.8408759249369493
		1.1881178145366552e-06 1.5887911462191298e-05 2.1125979190418618
		1.1881178145366552e-06 0.55576029963737561 1.8408552489404681
		1.1881178141804266e-06 0.83362457673360657 1.2973854157350355
		1.1881178141804266e-06 0.55573915625943726 0.75392592052785146
		1.1881178138241978e-06 -1.5827155444635004e-05 0.48220392642294307
		1.1881178141804266e-06 -0.55576023888135806 0.75394659652433249
		1.1881178141804266e-06 -0.83362451597758969 1.297416429729757
		-0.54346347618681634 -0.55574966719238894 1.2974112607306367
		-0.81519580833913108 3.0378008421916936e-08 1.2974009227323962
		-0.54346347618681634 0.55574972794840649 1.2973905847341558
		1.1881178141804266e-06 0.83362457673360657 1.2973854157350355
		0.54346585242244483 0.55574972794840649 1.2973905847341556
		0.81519818457476034 3.0378008421916936e-08 1.2974009227323962
		0.54346585242244483 -0.55574966719238894 1.2974112607306365
		1.1881178141804266e-06 -0.83362451597758969 1.297416429729757
		;
createNode transform -n "heelRollRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "1FEFECBC-43B7-B8C1-CBCA-40A70E288F42";
	setAttr ".rp" -type "double3" 1.1881177855325323e-06 -2.9950459638372393e-05 -1.9669786278212016 ;
	setAttr ".sp" -type "double3" 1.1881177855325323e-06 -2.9950459638372393e-05 -1.9669786278212016 ;
createNode transform -n "heelRollRGT_IK_ctrl" -p "heelRollRGT_IK_Zro_grp";
	rename -uid "CD24749E-4B85-E239-123A-45B3B14E8965";
	setAttr ".rp" -type "double3" 1.1881177827966961e-06 -2.9950459638372393e-05 -1.966978627821202 ;
	setAttr ".sp" -type "double3" 1.1881177827966961e-06 -2.9950459638372393e-05 -1.966978627821202 ;
	setAttr ".hdl" -type "double3" 2.3143063732078749e-08 -5.8339788045619345e-07 -0.038314308903069694 ;
createNode nurbsCurve -n "heelRollRGT_IK_ctrlShape" -p "heelRollRGT_IK_ctrl";
	rename -uid "12FB5AB4-47A9-D0CD-3B5E-2388B8485501";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.1881178147147695e-06 0.83359459589610907 -1.9669941383145255
		1.1881178150709983e-06 0.55573031879987667 -1.4235243051090931
		1.1881178154272269e-06 -1.4092926036411879e-05 -1.1517816350076997
		1.1881178154272269e-06 -0.55576907634091899 -1.4235036291126122
		1.1881178154272269e-06 -0.8336544968150883 -1.9669631243198047
		1.1881178154272269e-06 -0.55579021971885734 -2.5104329575252291
		1.1881178154272269e-06 -4.5807992943950637e-05 -2.7821756276266183
		1.1881178150709983e-06 0.55570917542193832 -2.5104536335217098
		1.1881178147147695e-06 0.83359459589610907 -1.9669941383145255
		0.54346585242244594 0.55571974711090755 -1.9669889693154055
		0.81519818457476068 -2.9950459489468802e-05 -1.9669786313171651
		0.54346585242244627 -0.55577964802988822 -1.9669682933189248
		1.1881178154272269e-06 -0.8336544968150883 -1.9669631243198047
		-0.54346347618681545 -0.55577964802988822 -1.9669682933189248
		-0.81519580833913119 -2.9950459490893718e-05 -1.9669786313171651
		-0.54346347618681579 0.55571974711090755 -1.9669889693154055
		1.1881178147147695e-06 0.83359459589610907 -1.9669941383145255
		;
createNode transform -n "footInRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "E5A5DC99-4CE1-621D-3D9D-069E4F32597F";
	setAttr ".rp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
	setAttr ".sp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
createNode transform -n "footInRGT_IK_ctrl" -p "footInRGT_IK_Zro_grp";
	rename -uid "F9ADE0BF-43BD-D405-2019-988EB30751B1";
	setAttr ".rp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
	setAttr ".sp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
	setAttr ".hdl" -type "double3" -0.011263459649047363 5.9280548005136158e-10 -7.6929200229473111e-09 ;
createNode nurbsCurve -n "footInRGT_IK_ctrlShape" -p "footInRGT_IK_ctrl";
	rename -uid "C1757AF8-49FE-B34E-B37C-D8B30A01CFDD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.57817802128360285 0.81519702440590247 -3.9388995236183297e-07
		-0.57821028748952619 0.54346469318958723 0.54346426996672348
		-0.57825896236791996 3.0595194641153218e-08 0.81519660137060235
		-0.57829706555734561 -0.5434646321070441 0.54346426856817498
		-0.57830818838533204 -0.81519696353905013 -3.9598777491490063e-07
		-0.57827592217940826 -0.54346463232273201 -0.54346505984444249
		-0.57822724730101449 3.0271662046636906e-08 -0.81519739124831714
		-0.57818914411158928 0.54346469297389788 -0.54346505844589432
		-0.57817802128360285 0.81519702440590247 -3.9388995236183297e-07
		-0.022450019923914519 0.54342226317696618 9.9437586276585592e-06
		0.2553814389804972 -6.361442373486228e-05 1.5112058461763315e-05
		-0.022536797991734244 -0.54350706211966515 9.9423600791711045e-06
		-0.57830818838533204 -0.81519696353905013 -3.9598777491490063e-07
		-1.1340361897450202 -0.54342220231011373 -1.0733636354935292e-05
		-1.4118676486494321 6.3675290588700241e-05 -1.5901936189218164e-05
		-1.1339494116772006 0.5435071229865176 -1.0732237806447838e-05
		-0.57817802128360285 0.81519702440590247 -3.9388995236183297e-07
		;
createNode transform -n "footOutRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "DD75A6A4-4D6D-A63A-AD2F-38B53A8ADF25";
	setAttr ".rp" -type "double3" 0.4150435786198432 3.024792013933845e-08 3.6061385896740926e-05 ;
	setAttr ".sp" -type "double3" 0.4150435786198432 3.024792013933845e-08 3.6061385896740926e-05 ;
createNode transform -n "footOutRGT_IK_ctrl" -p "footOutRGT_IK_Zro_grp";
	rename -uid "AFBBB71F-4D80-6A95-EE87-4A81E9402593";
	setAttr ".rp" -type "double3" 0.4150435786198432 3.0247920196335039e-08 3.6061385895850355e-05 ;
	setAttr ".sp" -type "double3" 0.4150435786198432 3.0247920196335039e-08 3.6061385895850355e-05 ;
	setAttr ".hdl" -type "double3" 0.0080845351619761811 5.8919204392246585e-10 7.0243115972076775e-07 ;
createNode nurbsCurve -n "footOutRGT_IK_ctrlShape" -p "footOutRGT_IK_ctrl";
	rename -uid "C1995CEF-4BF2-189A-C19F-B5B72C741C0E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		0.41504360104319299 2.9037248498914973e-08 0.81523305784387901
		0.41505417273209877 -0.54346463476550488 0.54350072488444268
		0.4150594585765417 -0.81519696606154035 3.606017625454582e-05
		0.41505417273207207 -0.54346463315126847 -0.54342860372481616
		0.41504360104315274 3.145860311215591e-08 -0.81516093507001652
		0.41503302935424663 0.54346469526134855 -0.54342860211057875
		0.4150277435098037 0.81519702655737913 3.6062597610762086e-05
		0.41503302935427366 0.54346469364711214 0.5435007264986802
		0.41504360104319299 2.9037248498914973e-08 0.81523305784387901
		0.97079329861358465 1.0367438993039024e-05 0.54350072569156571
		1.2486681473987704 1.5537245203739746e-05 3.6061386936216242e-05
		0.97079329861355801 1.0369053229447851e-05 -0.54342860291769468
		0.41504360104315274 3.145860311215591e-08 -0.81516093507001652
		-0.14070609652723962 -1.0306943141427953e-05 -0.54342860291770179
		-0.41858094531242507 -1.5476749352306788e-05 3.6061386929091665e-05
		-0.14070609652721253 -1.030855737783678e-05 0.5435007256915585
		0.41504360104319299 2.9037248498914973e-08 0.81523305784387901
		;
createNode transform -n "toeRollRGT_IK_Zro_grp" -p "look";
	rename -uid "AFB564E0-4537-AF19-F411-CC8AE2DDC9EB";
	setAttr -av ".v";
	setAttr ".rp" -type "double3" 1.1881178110669878e-06 3.0297128639222848e-08 0.38628357138129188 ;
	setAttr ".sp" -type "double3" 1.1881178110669878e-06 3.0297128639222848e-08 0.38628357138129188 ;
createNode transform -n "toeRollRGT_IK_ctrl" -p "toeRollRGT_IK_Zro_grp";
	rename -uid "5E7B69C5-4833-39C6-B3C3-B8A17A21B8FC";
	setAttr ".rp" -type "double3" 1.1881178128908787e-06 3.0297129305356663e-08 0.3862835713812911 ;
	setAttr ".sp" -type "double3" 1.1881178128908787e-06 3.0297129305356663e-08 0.3862835713812911 ;
createNode nurbsCurve -n "toeRollRGT_IK_ctrlShape" -p "toeRollRGT_IK_ctrl";
	rename -uid "FC0E903C-4ECA-8175-7EC9-6A88D5E4F793";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.1881178112849991e-06 -3.4960167339276236 -7.3654887526784787
		1.1881178113175258e-06 -3.9780393906087657 -7.7399519528584388
		1.1881178113825773e-06 -4.5965736999131765 -7.7505232292310158
		1.1881178114476273e-06 -4.9847673398456722 -7.2688577562786989
		1.1881178114801515e-06 -5.0061086577829812 -6.6588474578088679
		1.1881178114476248e-06 -4.5240860011018462 -6.2843842576289175
		1.1881178113825735e-06 -3.905551691797438 -6.2738129812563503
		1.188117811317523e-06 -3.5173580518649401 -6.7554784542086592
		1.1881178112849991e-06 -3.4960167339276236 -7.3654887526784787
		-0.54346347618682012 -3.7476987212368513 -7.247715203533545
		-0.81519580833913441 -4.2510626958553015 -7.0121681052436724
		-0.54346347618681989 -4.7544266704737552 -6.7766210069538015
		1.1881178114801515e-06 -5.0061086577829812 -6.6588474578088679
		0.54346585242244194 -4.7544266704737552 -6.7766210069538015
		0.81519818457475746 -4.2510626958553015 -7.0121681052436724
		0.54346585242244172 -3.7476987212368513 -7.247715203533545
		1.1881178112849991e-06 -3.4960167339276236 -7.3654887526784787
		;
createNode transform -n "toeRollLFT_IK_Zro_grp" -p "look";
	rename -uid "2BF9B671-4D85-CFC1-AF3E-CD87FB983073";
	setAttr ".rp" -type "double3" -1.2767236194324574e-14 7.1245737691543378e-16 1.2974012902154537 ;
	setAttr ".sp" -type "double3" -1.2767236194324574e-14 7.1245737691543378e-16 1.2974012902154537 ;
createNode transform -n "toeRollLFT_IK_ctrl" -p "toeRollLFT_IK_Zro_grp";
	rename -uid "A49B1033-45FC-3A16-982F-CE9C1C393B85";
	setAttr ".rp" -type "double3" -1.0943345309421062e-14 2.493600819204018e-15 1.2974012902154537 ;
	setAttr ".sp" -type "double3" -1.0943345309421062e-14 2.493600819204018e-15 1.2974012902154537 ;
	setAttr ".hdl" -type "double3" -2.1316282072803005e-16 4.8572257327350599e-17 0.025271771183207087 ;
createNode nurbsCurve -n "toeRollLFT_IK_ctrlShape" -p "toeRollLFT_IK_ctrl";
	rename -uid "60A4A94C-42CB-F059-10FB-DEB5D5882A51";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.1881178154272269e-06 0.83362457673360657 1.2973854157350484
		1.1881178154272269e-06 0.55573915625943726 0.75392592052785612
		1.1881178154272269e-06 -1.5827155444991232e-05 0.48220392642294335
		1.1881178154272269e-06 -0.55576023888135839 0.75394659652433671
		1.1881178154272269e-06 -0.83362451597759002 1.297416429729769
		1.1881178154272269e-06 -0.5557390955034216 1.8408759249369531
		1.1881178154272269e-06 1.5887911461835069e-05 2.1125979190418618
		1.1881178154272269e-06 0.55576029963737561 1.8408552489404724
		1.1881178154272269e-06 0.83362457673360657 1.2973854157350484
		0.54346585242244594 0.55574972794840649 1.2973905847341685
		0.81519818457476034 3.037800806568825e-08 1.2974009227324088
		0.54346585242244594 -0.55574966719238927 1.2974112607306489
		1.1881178154272269e-06 -0.83362451597759002 1.297416429729769
		-0.54346347618681545 -0.55574966719238927 1.2974112607306489
		-0.81519580833913086 3.037800806568825e-08 1.2974009227324088
		-0.54346347618681545 0.55574972794840649 1.2973905847341685
		1.1881178154272269e-06 0.83362457673360657 1.2973854157350484
		;
createNode transform -n "ballRollRGT_FK_Zro_grp" -p "look";
	rename -uid "10385A7C-49D0-744B-F114-038923FD0C56";
createNode transform -n "ballRollRGT_FK_ctrl" -p "ballRollRGT_FK_Zro_grp";
	rename -uid "CE350B45-4D4D-E7D6-99E5-EA92818CF833";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 3.551952682345486e-07 2.0514950947787893e-08 2.3847975888064485e-08 ;
	setAttr ".sp" -type "double3" 3.551952682345486e-07 2.0514950947787893e-08 2.3847975888064485e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "ballRollRGT_FK_ctrlShape" -p "ballRollRGT_FK_ctrl";
	rename -uid "54534CCB-4636-7E4A-E47D-04AC1EDE7A46";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.8013809190361956 1.4688810550376148 0.29654561039448712
		-0.11703715556323878 1.3908821223507168 -1.065542863125621
		3.2217542535787733 1.1830184606300838 -0.086940650540908104
		7.0929416015415869 0.999286655003778 -0.33335939425129241
		5.0412256213204483 0.88448378871209343 4.9133132642355379
		0.45595482991456393 0.97611062223568013 8.2432016814738631
		-3.9934768040881705 1.3132776644945705 5.4885426344041681
		-6.2835974071747618 1.6341474103477565 0.51830984140392389
		-2.8013809190361956 1.4688810550376148 0.29654561039448712
		-0.11703715556323878 1.3908821223507168 -1.065542863125621
		3.2217542535787733 1.1830184606300838 -0.086940650540908104
		;
createNode transform -n "ballRollRGT_FK_Gimbal_ctrl" -p "ballRollRGT_FK_ctrl";
	rename -uid "8F1F57B8-4F0B-4951-1414-A5A5215FA66C";
	setAttr ".rp" -type "double3" 3.5519526823454855e-07 2.0514950947787899e-08 2.3847975888064495e-08 ;
	setAttr ".sp" -type "double3" 3.5519526823454855e-07 2.0514950947787899e-08 2.3847975888064495e-08 ;
createNode nurbsCurve -n "ballRollRGT_FK_Gimbal_ctrlShape" -p "ballRollRGT_FK_Gimbal_ctrl";
	rename -uid "4C9B22D3-40FF-32C7-06D4-728FBF89F09C";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.3811737279014764 1.2485488998592149 0.2520637724125106
		-0.09948152894946273 1.1822498070753518 -0.9057114300795811
		2.7384911688212474 1.0055656946128142 -0.073899549382575591
		6.0290004145896381 0.84939365983045401 -0.28335548153640217
		4.2850418314016716 0.75181122348252261 4.1763162781774055
		0.38756165870666942 0.82969403197757075 7.0067214328299796
		-3.3944552301956548 1.1162860178976273 4.6652612428207387
		-5.3410577428192578 1.3890253018728353 0.44056336877053165
		-2.3811737279014764 1.2485488998592149 0.2520637724125106
		-0.09948152894946273 1.1822498070753518 -0.9057114300795811
		2.7384911688212474 1.0055656946128142 -0.073899549382575591
		;
createNode transform -n "ankleRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "F7B80408-48C7-1D0E-3388-A7BE375A2912";
createNode transform -n "ankleRGT_FK_ctrl" -p "ankleRGT_FK_Zro_grp";
	rename -uid "84ED8578-45C2-C301-76A9-0BA8D5C7B9D4";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -2.1085844389029747e-07 2.9710690976484702e-08 -3.2627855343808004e-09 ;
	setAttr ".sp" -type "double3" -2.1085844389029747e-07 2.9710690976484702e-08 -3.2627855343808004e-09 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "ankleRGT_FK_ctrlShape" -p "ankleRGT_FK_ctrl";
	rename -uid "EE2CD44D-4D30-6E9A-043A-A59FA66A398F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.7011112816764085 0.664512945714956 2.9299435902293363
		-0.96282170026641345 -1.8091891471139716 7.1247317367689265
		2.6257634149872815 1.1029631595270353 3.3318212043250557
		5.6187171336806827 1.7429055466140804 -0.32531165569192322
		2.9683094941264745 1.9917649562799014 -4.3409059531273657
		-0.5712909276708229 1.9374386083237312 -6.2643312517414662
		-2.9943955480915441 1.5785515727372397 -4.7196518254277757
		-4.9229747261712831 3.4306690083147187 -0.71693732020026946
		-3.7011112816764085 0.664512945714956 2.9299435902293363
		-0.96282170026641345 -1.8091891471139716 7.1247317367689265
		2.6257634149872815 1.1029631595270353 3.3318212043250557
		;
createNode transform -n "ankleRGT_FK_Gimbal_ctrl" -p "ankleRGT_FK_ctrl";
	rename -uid "6FC5ABE8-4BAC-F04C-DFE3-2E9781145438";
	setAttr ".rp" -type "double3" -2.1085844389029744e-07 2.9710690976484702e-08 -3.2627855343807988e-09 ;
	setAttr ".sp" -type "double3" -2.1085844389029744e-07 2.9710690976484702e-08 -3.2627855343807988e-09 ;
createNode nurbsCurve -n "ankleRGT_FK_Gimbal_ctrlShape" -p "ankleRGT_FK_Gimbal_ctrl";
	rename -uid "9B1B300C-4D94-0C3D-85B9-95A06F24B695";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.1459446210537143 0.56483600831431613 2.4904520512055175
		-0.81839847685521805 -1.5378107705902724 6.0560219757641702
		2.2318988711104222 0.93751869005458377 2.8320480231868794
		4.7759095319998144 1.4814697190785717 -0.2765149078275525
		2.5230630383787371 1.6930002172945198 -3.6897700606476782
		-0.48559732014896601 1.6468228215317753 -5.3246815644696639
		-2.5452362475065788 1.3417688412832576 -4.0117040521030276
		-4.1845285488743569 2.9160686615241143 -0.60939672265964684
		-3.1459446210537143 0.56483600831431613 2.4904520512055175
		-0.81839847685521805 -1.5378107705902724 6.0560219757641702
		2.2318988711104222 0.93751869005458377 2.8320480231868794
		;
createNode transform -n "IKFKGrp" -p "TMP_GRP";
	rename -uid "C7A0EFF5-4093-C8C3-3E3B-2B805C4CDBE5";
	setAttr ".v" no;
createNode transform -n "FK" -p "IKFKGrp";
	rename -uid "72047CD5-4CB5-FA45-3432-578C6DB6278E";
createNode transform -n "LFT" -p "|TMP_GRP|IKFKGrp|FK";
	rename -uid "733CA225-4C3C-D525-E292-FF89C0A27161";
createNode transform -n "upLegBackLFT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrp|FK|LFT";
	rename -uid "5F3FA736-4CB6-0CF0-24C9-3E874105A3E3";
createNode transform -n "upLegBackLFT_FK_ctrl" -p "upLegBackLFT_FK_Zro_grp";
	rename -uid "9F90E5C1-403C-8F84-7C88-BAA7C2D477D1";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "upLegBackLFT_FK_ctrlShape" -p "upLegBackLFT_FK_ctrl";
	rename -uid "CA8A8A27-4558-58C6-9D96-AA91DEF25068";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.6257081489231364 0.096652831577271489 5.3729580599344029
		-0.014713393902743703 -0.38744265336480144 11.773796545138705
		4.1378686592451412 -0.44942501827285836 5.756501152452377
		13.094587611230942 2.2388542551407546 0.41393449135439198
		4.1892311703385596 -0.098353770313908379 -5.4019782321161776
		-1.0942525569641064 0.43723336169655103 -12.134282392683552
		-4.5743456378297136 0.44772407953622151 -5.7855213246341766
		-5.9221021618687191 3.6674507538558871 -0.074835455990221414
		-4.6257081489231364 0.096652831577271489 5.3729580599344029
		-0.014713393902743703 -0.38744265336480144 11.773796545138705
		4.1378686592451412 -0.44942501827285836 5.756501152452377
		;
createNode transform -n "upLegBackLFT_FK_Gimbal_ctrl" -p "upLegBackLFT_FK_ctrl";
	rename -uid "34BFE490-4717-EB59-0198-EFAFAFF8093D";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
createNode nurbsCurve -n "upLegBackLFT_FK_Gimbal_ctrlShape" -p "upLegBackLFT_FK_Gimbal_ctrl";
	rename -uid "C1A94E08-45B4-BEC5-2BD7-12BA28F58BE6";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.9318519494181596 0.082154971976049845 4.5670143517060833
		-0.012506407650825408 -0.32932619022471205 10.007727064129741
		3.517188337524876 -0.3820112003965605 4.8930259803463612
		11.130399446712806 1.9030261820050105 0.35184431841307379
		3.5608464719542821 -0.083600639631453047 -4.5916814965369088
		-0.9301146962529836 0.37164842257743741 -10.314140033019179
		-3.8881938149887501 0.38056553274115734 -4.9176931251772089
		-5.0337868604219045 3.1173332059128733 -0.063610136829847577
		-3.9318519494181596 0.082154971976049845 4.5670143517060833
		-0.012506407650825408 -0.32932619022471205 10.007727064129741
		3.517188337524876 -0.3820112003965605 4.8930259803463612
		;
createNode transform -n "lowLegBackLFT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrp|FK|LFT";
	rename -uid "E0C2AEA8-4EB2-FD02-66C7-E8B47618FCB9";
createNode transform -n "lowLegBackLFT_FK_ctrl" -p "lowLegBackLFT_FK_Zro_grp";
	rename -uid "4EEDFD1A-4FFB-489C-27F5-BA9DB8BA488B";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowLegBackLFT_FK_ctrlShape" -p "lowLegBackLFT_FK_ctrl";
	rename -uid "4162F594-42D8-2363-2AC7-1D85919BAA96";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		6.2535857091339926 0.42576575955346629 1.7368095944081221
		3.3338712071101759 0.30631580409725961 -1.4623408983774617
		-0.024488954134432063 0.16853961980228996 -5.1883801395094933
		-4.7267989704333164 0.047751391652301363 -1.6382238580866619
		-5.4933799203568796 2.8783703686577495 1.4574319667443068
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		;
createNode transform -n "lowLegBackLFT_FK_Gimbal_ctrl" -p "lowLegBackLFT_FK_ctrl";
	rename -uid "4D296BC5-4F14-E23E-9FA0-CFBE5E8F3386";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
createNode nurbsCurve -n "lowLegBackLFT_FK_Gimbal_ctrlShape" -p "lowLegBackLFT_FK_Gimbal_ctrl";
	rename -uid "3E135590-4ADC-6058-AD37-2A8546D1B789";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		5.3155478767443585 0.36190103881972491 1.4762881412301532
		2.8337905500241134 0.26036857668194918 -1.2429897776375933
		-0.02081558703380279 0.14325882003122503 -4.4101231325998196
		-4.0177791008878545 0.04058882610373471 -1.3924902933904131
		-4.6693729083228828 2.4466149565583657 1.2388171577159102
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		;
createNode transform -n "midLegBackLFT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrp|FK|LFT";
	rename -uid "4A303FC1-4FAC-33AD-9D3D-E784C2F3BB11";
createNode transform -n "midLegBackLFT_FK_ctrl" -p "midLegBackLFT_FK_Zro_grp";
	rename -uid "89344201-4B37-9DB1-A2A3-D4B7744100E0";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "midLegBackLFT_FK_ctrlShape" -p "midLegBackLFT_FK_ctrl";
	rename -uid "6C15B607-4C05-5B49-9E43-80875836DAA8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		6.2535857091339926 0.42576575955346629 1.7368095944081221
		3.3338712071101759 0.30631580409725961 -1.4623408983774617
		-0.024488954134432063 0.16853961980228996 -5.1883801395094933
		-4.7267989704333164 0.047751391652301363 -1.6382238580866619
		-5.4933799203568796 2.8783703686577495 1.4574319667443068
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		;
createNode transform -n "midLegBackLFT_FK_Gimbal_ctrl" -p "midLegBackLFT_FK_ctrl";
	rename -uid "AB6E34A2-43B6-6FAF-B23B-29B28BE3E340";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
createNode nurbsCurve -n "midLegBackLFT_FK_Gimbal_ctrlShape" -p "midLegBackLFT_FK_Gimbal_ctrl";
	rename -uid "C7594B75-4A25-64B9-337E-C7AB0CADE866";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		5.3155478767443585 0.36190103881972491 1.4762881412301532
		2.8337905500241134 0.26036857668194918 -1.2429897776375933
		-0.02081558703380279 0.14325882003122503 -4.4101231325998196
		-4.0177791008878545 0.04058882610373471 -1.3924902933904131
		-4.6693729083228828 2.4466149565583657 1.2388171577159102
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		;
createNode transform -n "RGT" -p "|TMP_GRP|IKFKGrp|FK";
	rename -uid "EB180E89-49B3-B86F-A19D-95BD49EB29FA";
createNode transform -n "midLegBackRGT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrp|FK|RGT";
	rename -uid "0CE1FA4E-4C84-DAF7-305A-AD821BEC2329";
createNode transform -n "midLegBackRGT_FK_ctrl" -p "midLegBackRGT_FK_Zro_grp";
	rename -uid "5E305D5E-477D-159B-F4A0-C5B48C6B1045";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "midLegBackRGT_FK_ctrlShape" -p "midLegBackRGT_FK_ctrl";
	rename -uid "8E5D1A8F-4167-D8F6-A054-058DEA80B601";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		6.2535857091339926 0.42576575955346629 1.7368095944081221
		3.3338712071101759 0.30631580409725961 -1.4623408983774617
		-0.024488954134432063 0.16853961980228996 -5.1883801395094933
		-4.7267989704333164 0.047751391652301363 -1.6382238580866619
		-5.4933799203568796 2.8783703686577495 1.4574319667443068
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		;
createNode transform -n "midLegBackRGT_FK_Gimbal_ctrl" -p "midLegBackRGT_FK_ctrl";
	rename -uid "B46A07C9-40E0-FC49-622E-03A8D756B4BE";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
createNode nurbsCurve -n "midLegBackRGT_FK_Gimbal_ctrlShape" -p "midLegBackRGT_FK_Gimbal_ctrl";
	rename -uid "666C3336-4CE3-D3F9-8128-5B8EB5D40838";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		5.3155478767443585 0.36190103881972491 1.4762881412301532
		2.8337905500241134 0.26036857668194918 -1.2429897776375933
		-0.02081558703380279 0.14325882003122503 -4.4101231325998196
		-4.0177791008878545 0.04058882610373471 -1.3924902933904131
		-4.6693729083228828 2.4466149565583657 1.2388171577159102
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		;
createNode transform -n "lowLegBackRGT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrp|FK|RGT";
	rename -uid "F3637A07-40F8-6EF1-0F17-9AB8E1C6D97B";
	setAttr ".rp" -type "double3" 0 -1.139931803064694e-16 0 ;
	setAttr ".sp" -type "double3" 1.8238908849035105e-15 -1.139931803064694e-16 0 ;
createNode transform -n "lowLegBackRGT_FK_ctrl" -p "lowLegBackRGT_FK_Zro_grp";
	rename -uid "7F0F4C84-4BC4-44A2-6357-F78EBDE30923";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr ".sp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowLegBackRGT_FK_ctrlShape" -p "lowLegBackRGT_FK_ctrl";
	rename -uid "B9FFC28B-4A84-CDB8-9AAB-5BB69FAE6A1E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.8650712827205354 -0.094922294227107018 -4.629642496102246
		-0.44965222940039684 -0.29405724835873842 -8.2286654438004501
		-3.1955988948229654 -0.35348670667207788 -4.8055254558114111
		-6.2535900940786728 -0.42578531906153766 -1.7368078610174549
		-3.3338755920548784 -0.30633536360532704 1.4623426317681247
		0.02448456918973833 -0.16855917931035744 5.1883818729001616
		4.7267945854886424 -0.047770951160355839 1.6382255914773054
		5.493375535412218 -2.8783899281657961 -1.4574302333536628
		4.8650712827205354 -0.094922294227107018 -4.629642496102246
		-0.44965222940039684 -0.29405724835873842 -8.2286654438004501
		-3.1955988948229654 -0.35348670667207788 -4.8055254558114111
		;
createNode transform -n "lowLegBackRGT_FK_Gimbal_ctrl" -p "lowLegBackRGT_FK_ctrl";
	rename -uid "D2CCF4C6-4C5C-917C-BFAD-28B4395BF3A3";
	setAttr ".rp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr ".sp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
createNode nurbsCurve -n "lowLegBackRGT_FK_Gimbal_ctrlShape" -p "lowLegBackRGT_FK_Gimbal_ctrl";
	rename -uid "73840B29-4903-1DB6-0DD5-F5A4D357E02F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.1353099085902878 -0.080687027218528065 -3.9351958476615607
		-0.38220507671250498 -0.24995173823041475 -6.9943653532050343
		-2.7162597423216881 -0.30046677779675329 -4.0846963634143512
		-5.3155522616890396 -0.36192059832779405 -1.4762864078394877
		-2.8337949349688145 -0.26038813619001511 1.2429915110282546
		0.020811202089109908 -0.1432783795392909 4.4101248659904853
		4.0177747159431787 -0.040608385611789574 1.3924920267810581
		4.6693685233782176 -2.446634516066414 -1.2388154243252647
		4.1353099085902878 -0.080687027218528065 -3.9351958476615607
		-0.38220507671250498 -0.24995173823041475 -6.9943653532050343
		-2.7162597423216881 -0.30046677779675329 -4.0846963634143512
		;
createNode transform -n "upLegBackRGT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrp|FK|RGT";
	rename -uid "4072D2B0-4583-78B7-872F-408B22964B8F";
createNode transform -n "upLegBackRGT_FK_ctrl" -p "upLegBackRGT_FK_Zro_grp";
	rename -uid "2CED784A-42DA-173D-CF24-309C59D39674";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
	setAttr ".sp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "upLegBackRGT_FK_ctrlShape" -p "upLegBackRGT_FK_ctrl";
	rename -uid "3CD0B8F8-477A-D34C-F3E2-C79C3F1BCD36";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.6257320496466665 -0.09662662010513734 -5.3729577533584649
		0.014737294626292873 0.38746886483695814 -11.773796238562735
		-4.1378447585215685 0.44945122974495388 -5.7565008458764657
		-13.094563710507288 -2.2388280436686943 -0.41393418477846949
		-4.1892072696149665 0.098379981785949422 5.4019785386921466
		1.094276457687702 -0.43720715022451667 12.134282699259515
		4.5743695385532801 -0.44769786806415457 5.7855216312101527
		5.9221260625922971 -3.6674245423838063 0.074835762566161396
		4.6257320496466665 -0.09662662010513734 -5.3729577533584649
		0.014737294626292873 0.38746886483695814 -11.773796238562735
		-4.1378447585215685 0.44945122974495388 -5.7565008458764657
		;
createNode transform -n "upLegBackRGT_FK_Gimbal_ctrl" -p "upLegBackRGT_FK_ctrl";
	rename -uid "0E5D9EC2-4ABA-92F7-C394-0A9B60760FA1";
	setAttr ".rp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
	setAttr ".sp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
createNode nurbsCurve -n "upLegBackRGT_FK_Gimbal_ctrlShape" -p "upLegBackRGT_FK_Gimbal_ctrl";
	rename -uid "42BF9077-47A7-BE18-502F-83BADC13FF8A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.9318758501416951 -0.082128760503922843 -4.5670140451301435
		0.012530308374377333 0.32935240169685825 -10.007726757553773
		-3.5171644368013046 0.38203741186865464 -4.8930256737704436
		-11.130375545989164 -1.9029999705329461 -0.35184401183714714
		-3.5608225712306933 0.083626851103500904 4.5916818031128761
		0.93013859697657519 -0.37162221110539523 10.31414033959514
		3.8882177157123166 -0.38053932126908752 4.9176934317531815
		5.0338107611454808 -3.1173069944407921 0.063610443405789072
		3.9318758501416951 -0.082128760503922843 -4.5670140451301435
		0.012530308374377333 0.32935240169685825 -10.007726757553773
		-3.5171644368013046 0.38203741186865464 -4.8930256737704436
		;
createNode transform -n "IK" -p "IKFKGrp";
	rename -uid "977BF227-4E96-AC3B-D489-BEB995E098CB";
createNode transform -n "lowLegBackLFT_IK_Zro_grp" -p "|TMP_GRP|IKFKGrp|IK";
	rename -uid "7DC16AC2-47FE-9BA9-5172-A0A282E54557";
createNode transform -n "lowLegBackLFT_IK_ctrl" -p "lowLegBackLFT_IK_Zro_grp";
	rename -uid "2143D10E-4C63-9051-0907-20B8A346F754";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr -l on -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "lowLegBackLFT_IK_ctrlShape" -p "lowLegBackLFT_IK_ctrl";
	rename -uid "417C9813-4FD2-294A-FE89-A5BF1FDEC195";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		;
createNode transform -n "lowLegBackRGT_IK_Zro_grp" -p "|TMP_GRP|IKFKGrp|IK";
	rename -uid "A9275670-4C9A-25EC-AE65-938B5E3D48F5";
createNode transform -n "lowLegBackRGT_IK_ctrl" -p "lowLegBackRGT_IK_Zro_grp";
	rename -uid "866FE511-4264-9D25-5D5C-08BC786C09CE";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr -l on -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "lowLegBackRGT_IK_ctrlShape" -p "lowLegBackRGT_IK_ctrl";
	rename -uid "38E87D09-4049-0B77-05E6-CCA81B4EA6DB";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		;
createNode transform -n "POV" -p "TMP_GRP";
	rename -uid "176000BE-4831-BE51-40CC-E5ACA6F7EFCE";
	setAttr ".v" no;
createNode transform -n "legPovBackLFT_Zro_grp" -p "POV";
	rename -uid "F6752377-4001-C367-B966-DBB36A5538A0";
createNode transform -n "legPovBackLFT_ctrl" -p "legPovBackLFT_Zro_grp";
	rename -uid "085E1C1B-413B-33D8-1D03-8AAF7613002A";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "legPovBackLFT_ctrlShape" -p "legPovBackLFT_ctrl";
	rename -uid "975EC120-4B21-E3A3-4901-298CE4495310";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 1.7991854165801995 0
		0 -1.7991854165801995 0
		0 0 0
		0 0 -1.7991854165801995
		0 0 1.7991854165801995
		0 0 0
		1.7991854165801995 0 0
		-1.7991854165801995 0 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0.22516301716584575 0
		-1.3689023077892113 0.44478310390029102 0
		-1.2824694403766994 0.65345118916692957 0
		-1.1644572705323701 0.84602736006767465 0
		-1.0177732818894205 1.0177732818894205 0
		-0.84602736006767465 1.1644572705323701 0
		-0.65345118916692957 1.2824694403766994 0
		-0.44478310390029102 1.3689023077892113 0
		-0.22516445651417891 1.4216270765850112 0
		0 1.4393483332641601 0
		0.22516301716584575 1.4216270765850112 0
		0.44478310390029102 1.3689023077892113 0
		0.65345118916692957 1.2824694403766994 0
		0.84602736006767465 1.1644572705323701 0
		1.0177732818894205 1.0177732818894205 0
		1.1644572705323701 0.84602736006767465 0
		1.2824694403766994 0.65345118916692957 0
		1.3689023077892113 0.44478310390029102 0
		1.4216270765850112 0.22516301716584575 0
		1.4393483332641601 0 0
		1.4216270765850112 -0.22516301716584575 0
		1.3689023077892113 -0.44478310390029102 0
		1.2824694403766994 -0.65345118916692957 0
		1.1644572705323701 -0.84602736006767465 0
		1.0177732818894205 -1.0177732818894205 0
		0.84602736006767465 -1.1644572705323701 0
		0.65345118916692957 -1.2824694403766994 0
		0.44478310390029102 -1.3689023077892113 0
		0.22516301716584575 -1.4216270765850112 0
		0 -1.4393483332641601 0
		-0.22516445651417891 -1.4216270765850112 0
		-0.44478310390029102 -1.3689023077892113 0
		-0.65345118916692957 -1.2824694403766994 0
		-0.84602736006767465 -1.1644572705323701 0
		-1.0177732818894205 -1.0177732818894205 0
		-1.1644572705323701 -0.84602736006767465 0
		-1.2824694403766994 -0.65345118916692957 0
		-1.3689023077892113 -0.44478310390029102 0
		-1.4216285159333439 -0.22516301716584575 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		0.22516301716584575 0 1.4216270765850112
		0.44478310390029102 0 1.3689023077892113
		0.65345118916692957 0 1.2824694403766994
		0.84602736006767465 0 1.1644572705323701
		1.0177732818894205 0 1.0177732818894205
		1.1644572705323701 0 0.84602736006767465
		1.2824694403766994 0 0.65345118916692957
		1.3689023077892113 0 0.44478310390029102
		1.4216270765850112 0 0.22516301716584575
		1.4393483332641601 0 0
		1.4216270765850112 0 -0.22516301716584575
		1.3689023077892113 0 -0.44478310390029102
		1.2824694403766994 0 -0.65345118916692957
		1.1644572705323701 0 -0.84602736006767465
		1.0177732818894205 0 -1.0177732818894205
		0.84602736006767465 0 -1.1644572705323701
		0.65345118916692957 0 -1.2824694403766994
		0.44478310390029102 0 -1.3689023077892113
		0.22516301716584575 0 -1.4216270765850112
		0 0 -1.4393483332641601
		-0.22516445651417891 0 -1.4216270765850112
		-0.44478310390029102 0 -1.3689023077892113
		-0.65345118916692957 0 -1.2824694403766994
		-0.84602736006767465 0 -1.1644572705323701
		-1.0177732818894205 0 -1.0177732818894205
		-1.1644572705323701 0 -0.84602736006767465
		-1.2824694403766994 0 -0.65345118916692957
		-1.3689023077892113 0 -0.44478310390029102
		-1.4216285159333439 0 -0.22516301716584575
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		-6.7104002579941741e-09 0.22516301716584575 1.4216270765850112
		-1.3255563327329612e-08 0.44478310390029102 1.3689023077892113
		-1.947438294906409e-08 0.65345118916692957 1.2824694403766994
		-2.5213640493121609e-08 0.84602736006767465 1.1644572705323701
		-3.0331963166208942e-08 1.0177732818894205 1.0177732818894205
		-3.4703551923998864e-08 1.1644572705323701 0.84602736006767465
		-3.822059957632979e-08 1.2824694403766994 0.65345118916692957
		-4.0796457353539337e-08 1.3689023077892113 0.44478310390029102
		-4.2367793928963873e-08 1.4216270765850112 0.22516301716584575
		-4.2895890832438451e-08 1.4393483332641601 0
		-4.2367793928963873e-08 1.4216270765850112 -0.22516301716584575
		-4.0796457353539337e-08 1.3689023077892113 -0.44478310390029102
		-3.822059957632979e-08 1.2824694403766994 -0.65345118916692957
		-3.4703551923998864e-08 1.1644572705323701 -0.84602736006767465
		-3.0331963166208942e-08 1.0177732818894205 -1.0177732818894205
		-2.5213640493121609e-08 0.84602736006767465 -1.1644572705323701
		-1.947438294906409e-08 0.65345118916692957 -1.2824694403766994
		-1.3255563327329612e-08 0.44478310390029102 -1.3689023077892113
		-6.7104002579941741e-09 0.22516301716584575 -1.4216270765850112
		0 0 -1.4393483332641601
		0 -0.22516445651417891 -1.4216270765850112
		0 -0.44478310390029102 -1.3689023077892113
		0 -0.65345118916692957 -1.2824694403766994
		0 -0.84602879941600828 -1.1644572705323701
		0 -1.0177732818894205 -1.0177732818894205
		0 -1.1644572705323701 -0.84602736006767465
		0 -1.2824694403766994 -0.65345118916692957
		0 -1.3689023077892113 -0.44478310390029102
		0 -1.4216285159333439 -0.22516301716584575
		0 -1.4393483332641601 0
		0 -1.4216285159333439 0.22516301716584575
		0 -1.3689023077892113 0.44478310390029102
		0 -1.2824694403766994 0.65345118916692957
		0 -1.1644572705323701 0.84602736006767465
		0 -1.0177732818894205 1.0177732818894205
		0 -0.84602879941600828 1.1644572705323701
		0 -0.65345118916692957 1.2824694403766994
		0 -0.44478310390029102 1.3689023077892113
		0 -0.22516445651417891 1.4216270765850112
		0 0 1.4393483332641601
		;
createNode transform -n "legPovBackRGT_Zro_grp" -p "POV";
	rename -uid "BA724B55-44C7-E89E-6FB4-E5BC68AC8E30";
createNode transform -n "legPovBackRGT_ctrl" -p "legPovBackRGT_Zro_grp";
	rename -uid "D299F5A3-43DC-E8E8-9EEF-959DF0630C8B";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "legPovBackRGT_ctrlShape" -p "legPovBackRGT_ctrl";
	rename -uid "9EDDA132-4E51-2C6F-8A7D-B58FCBE27393";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 1.7991854165801995 0
		0 -1.7991854165801995 0
		0 0 0
		0 0 -1.7991854165801995
		0 0 1.7991854165801995
		0 0 0
		1.7991854165801995 0 0
		-1.7991854165801995 0 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0.22516301716584575 0
		-1.3689023077892113 0.44478310390029102 0
		-1.2824694403766994 0.65345118916692957 0
		-1.1644572705323701 0.84602736006767465 0
		-1.0177732818894205 1.0177732818894205 0
		-0.84602736006767465 1.1644572705323701 0
		-0.65345118916692957 1.2824694403766994 0
		-0.44478310390029102 1.3689023077892113 0
		-0.22516445651417891 1.4216270765850112 0
		0 1.4393483332641601 0
		0.22516301716584575 1.4216270765850112 0
		0.44478310390029102 1.3689023077892113 0
		0.65345118916692957 1.2824694403766994 0
		0.84602736006767465 1.1644572705323701 0
		1.0177732818894205 1.0177732818894205 0
		1.1644572705323701 0.84602736006767465 0
		1.2824694403766994 0.65345118916692957 0
		1.3689023077892113 0.44478310390029102 0
		1.4216270765850112 0.22516301716584575 0
		1.4393483332641601 0 0
		1.4216270765850112 -0.22516301716584575 0
		1.3689023077892113 -0.44478310390029102 0
		1.2824694403766994 -0.65345118916692957 0
		1.1644572705323701 -0.84602736006767465 0
		1.0177732818894205 -1.0177732818894205 0
		0.84602736006767465 -1.1644572705323701 0
		0.65345118916692957 -1.2824694403766994 0
		0.44478310390029102 -1.3689023077892113 0
		0.22516301716584575 -1.4216270765850112 0
		0 -1.4393483332641601 0
		-0.22516445651417891 -1.4216270765850112 0
		-0.44478310390029102 -1.3689023077892113 0
		-0.65345118916692957 -1.2824694403766994 0
		-0.84602736006767465 -1.1644572705323701 0
		-1.0177732818894205 -1.0177732818894205 0
		-1.1644572705323701 -0.84602736006767465 0
		-1.2824694403766994 -0.65345118916692957 0
		-1.3689023077892113 -0.44478310390029102 0
		-1.4216285159333439 -0.22516301716584575 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		0.22516301716584575 0 1.4216270765850112
		0.44478310390029102 0 1.3689023077892113
		0.65345118916692957 0 1.2824694403766994
		0.84602736006767465 0 1.1644572705323701
		1.0177732818894205 0 1.0177732818894205
		1.1644572705323701 0 0.84602736006767465
		1.2824694403766994 0 0.65345118916692957
		1.3689023077892113 0 0.44478310390029102
		1.4216270765850112 0 0.22516301716584575
		1.4393483332641601 0 0
		1.4216270765850112 0 -0.22516301716584575
		1.3689023077892113 0 -0.44478310390029102
		1.2824694403766994 0 -0.65345118916692957
		1.1644572705323701 0 -0.84602736006767465
		1.0177732818894205 0 -1.0177732818894205
		0.84602736006767465 0 -1.1644572705323701
		0.65345118916692957 0 -1.2824694403766994
		0.44478310390029102 0 -1.3689023077892113
		0.22516301716584575 0 -1.4216270765850112
		0 0 -1.4393483332641601
		-0.22516445651417891 0 -1.4216270765850112
		-0.44478310390029102 0 -1.3689023077892113
		-0.65345118916692957 0 -1.2824694403766994
		-0.84602736006767465 0 -1.1644572705323701
		-1.0177732818894205 0 -1.0177732818894205
		-1.1644572705323701 0 -0.84602736006767465
		-1.2824694403766994 0 -0.65345118916692957
		-1.3689023077892113 0 -0.44478310390029102
		-1.4216285159333439 0 -0.22516301716584575
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		-6.7104002579941741e-09 0.22516301716584575 1.4216270765850112
		-1.3255563327329612e-08 0.44478310390029102 1.3689023077892113
		-1.947438294906409e-08 0.65345118916692957 1.2824694403766994
		-2.5213640493121609e-08 0.84602736006767465 1.1644572705323701
		-3.0331963166208942e-08 1.0177732818894205 1.0177732818894205
		-3.4703551923998864e-08 1.1644572705323701 0.84602736006767465
		-3.822059957632979e-08 1.2824694403766994 0.65345118916692957
		-4.0796457353539337e-08 1.3689023077892113 0.44478310390029102
		-4.2367793928963873e-08 1.4216270765850112 0.22516301716584575
		-4.2895890832438451e-08 1.4393483332641601 0
		-4.2367793928963873e-08 1.4216270765850112 -0.22516301716584575
		-4.0796457353539337e-08 1.3689023077892113 -0.44478310390029102
		-3.822059957632979e-08 1.2824694403766994 -0.65345118916692957
		-3.4703551923998864e-08 1.1644572705323701 -0.84602736006767465
		-3.0331963166208942e-08 1.0177732818894205 -1.0177732818894205
		-2.5213640493121609e-08 0.84602736006767465 -1.1644572705323701
		-1.947438294906409e-08 0.65345118916692957 -1.2824694403766994
		-1.3255563327329612e-08 0.44478310390029102 -1.3689023077892113
		-6.7104002579941741e-09 0.22516301716584575 -1.4216270765850112
		0 0 -1.4393483332641601
		0 -0.22516445651417891 -1.4216270765850112
		0 -0.44478310390029102 -1.3689023077892113
		0 -0.65345118916692957 -1.2824694403766994
		0 -0.84602879941600828 -1.1644572705323701
		0 -1.0177732818894205 -1.0177732818894205
		0 -1.1644572705323701 -0.84602736006767465
		0 -1.2824694403766994 -0.65345118916692957
		0 -1.3689023077892113 -0.44478310390029102
		0 -1.4216285159333439 -0.22516301716584575
		0 -1.4393483332641601 0
		0 -1.4216285159333439 0.22516301716584575
		0 -1.3689023077892113 0.44478310390029102
		0 -1.2824694403766994 0.65345118916692957
		0 -1.1644572705323701 0.84602736006767465
		0 -1.0177732818894205 1.0177732818894205
		0 -0.84602879941600828 1.1644572705323701
		0 -0.65345118916692957 1.2824694403766994
		0 -0.44478310390029102 1.3689023077892113
		0 -0.22516445651417891 1.4216270765850112
		0 0 1.4393483332641601
		;
createNode transform -n "hip" -p "TMP_GRP";
	rename -uid "8FBC1275-4284-9F3B-C8FA-B8A70C231DAB";
	setAttr ".v" no;
createNode transform -n "lowerBody_Zro_grp" -p "hip";
	rename -uid "8C41D9D6-46C4-76B1-B066-B7B40F05B2C3";
createNode transform -n "lowerBody_ctrl" -p "lowerBody_Zro_grp";
	rename -uid "7DBCD6FC-4E27-F5F2-D4B6-108D470C507D";
	addAttr -ci true -k true -sn "gmbl" -ln "gmbl" -dv 1 -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -k on ".gmbl" 0;
createNode nurbsCurve -n "curveShape3" -p "lowerBody_ctrl";
	rename -uid "0D7760CF-4E34-6B39-CBEB-2CA6550CE7E4";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.3550296885421664 6.355029688542146 -1.8842311049850495
		0 8.9873691748199835 1.7124770682803159
		-6.3550296885421549 6.3550296885421496 -1.88423110498505
		-8.9873691748199871 -3.6526792677085651e-14 1.8842311049850613
		-6.3550296885421593 -6.3550296885421567 -1.8842311049850509
		-2.9516600143099513e-15 -8.9873691748199835 1.7124770682803141
		6.3550296885421549 -6.3550296885421584 -1.8842311049850495
		8.9873691748199871 -4.3998182088307722e-14 1.8842311049850617
		6.3550296885421664 6.355029688542146 -1.8842311049850495
		0 8.9873691748199835 1.7124770682803159
		-6.3550296885421549 6.3550296885421496 -1.88423110498505
		;
createNode transform -n "lowerBody_Gimbal_ctrl" -p "lowerBody_ctrl";
	rename -uid "1277514F-4C69-B1FA-2751-0B90141D87D5";
createNode nurbsCurve -n "lowerBody_Gimbal_ctrlShape" -p "lowerBody_Gimbal_ctrl";
	rename -uid "8F914F1D-439E-D399-5545-0C92D28D8FCF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.7662722664066246 4.7662722664066095 -1.4131733287387871
		0 6.7405268811149881 1.2843578012102368
		-4.7662722664066166 4.7662722664066122 -1.4131733287387875
		-6.7405268811149899 -2.7395094507814243e-14 1.413173328738796
		-4.7662722664066193 -4.7662722664066175 -1.4131733287387882
		-2.2137450107324635e-15 -6.7405268811149881 1.2843578012102355
		4.7662722664066166 -4.7662722664066184 -1.4131733287387871
		6.7405268811149899 -3.2998636566230793e-14 1.4131733287387962
		4.7662722664066246 4.7662722664066095 -1.4131733287387871
		0 6.7405268811149881 1.2843578012102368
		-4.7662722664066166 4.7662722664066122 -1.4131733287387875
		;
createNode transform -n "upperBody_Zro_grp" -p "hip";
	rename -uid "A30A505E-4A76-2F16-64BB-9EB72A864ECA";
createNode transform -n "upperBody_ctrl" -p "upperBody_Zro_grp";
	rename -uid "120B323E-4B6D-78FE-947E-FC8C9D21808B";
	addAttr -ci true -k true -sn "gmbl" -ln "gmbl" -dv 1 -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -k on ".gmbl" 0;
createNode nurbsCurve -n "curveShape1" -p "upperBody_ctrl";
	rename -uid "BD4B4F0D-434B-0851-0669-74ABF9F36FAD";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		11.04043762434277 11.040437624342736 -3.2734287799336377
		-2.3125516762413059e-15 15.613536622879732 2.9750443486017195
		-11.040437624342751 11.04043762434274 -3.2734287799336386
		-15.613536622879741 -6.8500760619372159e-14 3.2734284352074283
		-11.040437624342768 -11.040437624342765 -3.2734287799336377
		-5.2358971393468905e-15 -15.613536622879725 2.9750443486017195
		11.040437624342744 -11.040437624342779 -3.2734287799336403
		15.613536622879741 -8.0484230391419942e-14 3.2734284352074283
		11.04043762434277 11.040437624342736 -3.2734287799336377
		-2.3125516762413059e-15 15.613536622879732 2.9750443486017195
		-11.040437624342751 11.04043762434274 -3.2734287799336386
		;
createNode transform -n "upperBody_Gimbal_ctrl" -p "upperBody_ctrl";
	rename -uid "7B5B4232-4DAE-0B26-3ADB-9A8EEF2D8A66";
createNode nurbsCurve -n "upperBody_Gimbal_ctrlShape" -p "upperBody_Gimbal_ctrl";
	rename -uid "EBFF3EDD-41FA-05EB-9D67-A98B47549658";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		8.2803282182570772 8.2803282182570523 -2.455071584950228
		-1.7344137571809794e-15 11.710152467159798 2.2312832614512894
		-8.280328218257063 8.2803282182570541 -2.4550715849502289
		-11.710152467159805 -5.1375570464529119e-14 2.4550713264055712
		-8.2803282182570754 -8.2803282182570737 -2.455071584950228
		-3.9269228545101677e-15 -11.710152467159794 2.2312832614512894
		8.2803282182570577 -8.2803282182570843 -2.4550715849502303
		11.710152467159805 -6.0363172793564956e-14 2.4550713264055712
		8.2803282182570772 8.2803282182570523 -2.455071584950228
		-1.7344137571809794e-15 11.710152467159798 2.2312832614512894
		-8.280328218257063 8.2803282182570541 -2.4550715849502289
		;
createNode transform -n "chest_Zro_grp" -p "hip";
	rename -uid "05CF5876-4570-C478-98AE-D08DCF325501";
createNode transform -n "chest_ctrl" -p "chest_Zro_grp";
	rename -uid "DD69D076-4751-56D7-F945-628224A26ED9";
	addAttr -ci true -k true -sn "gmbl" -ln "gmbl" -dv 1 -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr -k on ".gmbl" 0;
createNode nurbsCurve -n "curveShape4" -p "chest_ctrl";
	rename -uid "A41BEAA1-4B63-A62F-7A82-C19655428F38";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-17.006898831126108 5.8157138436509683 5.9302131802160396
		17.006898831126108 5.8157138436509683 5.9302131802160396
		17.006898831126108 5.8157138436509683 -8.4914646751478706
		-17.006898831126108 5.8157138436509683 -8.4914646751478706
		-17.006898831126108 5.8157138436509683 5.9302131802160396
		-17.006898831126108 -5.8157138436509683 8.4914646751478706
		-17.006898831126108 -5.8157138436509683 -8.4914646751478706
		17.006898831126108 -5.8157138436509683 -8.4914646751478706
		17.006898831126108 -5.8157138436509683 8.4914646751478706
		-17.006898831126108 -5.8157138436509683 8.4914646751478706
		17.006898831126108 -5.8157138436509683 8.4914646751478706
		17.006898831126108 5.8157138436509683 5.9302131802160396
		17.006898831126108 5.8157138436509683 -8.4914646751478706
		17.006898831126108 -5.8157138436509683 -8.4914646751478706
		-17.006898831126108 -5.8157138436509683 -8.4914646751478706
		-17.006898831126108 5.8157138436509683 -8.4914646751478706
		;
createNode transform -n "chest_Gimbal_ctrl" -p "chest_ctrl";
	rename -uid "3B6880DF-45D3-BB30-52F6-A098EA43C759";
createNode nurbsCurve -n "chest_Gimbal_ctrlShape" -p "chest_Gimbal_ctrl";
	rename -uid "4470DD77-47DA-E62D-DB2A-29B083F7F365";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-12.755174123344581 4.3617853827382262 4.4476598851620297
		12.755174123344581 4.3617853827382262 4.4476598851620297
		12.755174123344581 4.3617853827382262 -6.368598506360903
		-12.755174123344581 4.3617853827382262 -6.368598506360903
		-12.755174123344581 4.3617853827382262 4.4476598851620297
		-12.755174123344581 -4.3617853827382262 6.368598506360903
		-12.755174123344581 -4.3617853827382262 -6.368598506360903
		12.755174123344581 -4.3617853827382262 -6.368598506360903
		12.755174123344581 -4.3617853827382262 6.368598506360903
		-12.755174123344581 -4.3617853827382262 6.368598506360903
		12.755174123344581 -4.3617853827382262 6.368598506360903
		12.755174123344581 4.3617853827382262 4.4476598851620297
		12.755174123344581 4.3617853827382262 -6.368598506360903
		12.755174123344581 -4.3617853827382262 -6.368598506360903
		-12.755174123344581 -4.3617853827382262 -6.368598506360903
		-12.755174123344581 4.3617853827382262 -6.368598506360903
		;
createNode transform -n "body_Zro_grp" -p "hip";
	rename -uid "24809A44-468B-FE61-5F60-929CECD01C76";
createNode transform -n "body_ctrl" -p "body_Zro_grp";
	rename -uid "1A19D44B-48FF-4C38-5C50-A68941C8095B";
	addAttr -ci true -k true -sn "gmbl" -ln "gmbl" -dv 1 -min 0 -max 1 -at "double";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -k on ".gmbl" 0;
createNode nurbsCurve -n "curveShape2" -p "body_ctrl";
	rename -uid "0C73B412-410E-1DA7-1BEA-599DE394A7E0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		8.9668140866523807 8.9668140866523522 -2.6586124850257571
		1.5300422980983061e-16 12.680990092621904 2.4162675854420157
		-8.9668140866523665 8.9668140866523594 -2.6586124850257593
		-12.68099009262191 -5.2189280306686546e-14 2.6586089420119516
		-8.9668140866523771 -8.96681408665237 -2.658612485025758
		-4.0117263682299918e-15 -12.680990092621904 2.4162675854420144
		8.9668140866523629 -8.9668140866523753 -2.6586124850257571
		12.680990092621908 -6.2210663308219853e-14 2.6586089420119516
		8.9668140866523807 8.9668140866523522 -2.6586124850257571
		1.5300422980983061e-16 12.680990092621904 2.4162675854420157
		-8.9668140866523665 8.9668140866523594 -2.6586124850257593
		;
createNode transform -n "body_Gimbal_ctrl" -p "body_ctrl";
	rename -uid "0DB0DA80-4342-73C1-4EF3-6F875076DFE5";
createNode nurbsCurve -n "body_Gimbal_ctrlShape" -p "body_Gimbal_ctrl";
	rename -uid "6C35E7A8-4527-291C-5D55-699DEB436A6C";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		6.7251105649892855 6.7251105649892642 -1.9939593637693178
		1.1475317235737295e-16 9.5107425694664283 1.8122006890815117
		-6.7251105649892748 6.7251105649892695 -1.9939593637693194
		-9.5107425694664318 -3.9141960230014913e-14 1.9939567065089636
		-6.7251105649892828 -6.7251105649892775 -1.9939593637693185
		-3.0087947761724939e-15 -9.5107425694664283 1.8122006890815108
		6.7251105649892722 -6.7251105649892811 -1.9939593637693178
		9.51074256946643 -4.6657997481164883e-14 1.9939567065089636
		6.7251105649892855 6.7251105649892642 -1.9939593637693178
		1.1475317235737295e-16 9.5107425694664283 1.8122006890815117
		-6.7251105649892748 6.7251105649892695 -1.9939593637693194
		;
createNode transform -n "hip_Zro_grp" -p "hip";
	rename -uid "57B8F4BA-4E2F-421B-981F-0A91F6A54AE0";
createNode transform -n "hip_ctrl" -p "hip_Zro_grp";
	rename -uid "0C848AA5-4172-7BF3-E48B-E3B190A0A2FE";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
	setAttr ".sp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "hip_ctrlShape" -p "hip_ctrl";
	rename -uid "EE46DA99-4E55-A8CD-C25C-8FB87C8C31A3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1.565366 3.1307580000000002 4.6961259999999996 6.2614869999999998 7.8268849999999999
		 9.3922439999999998 15.392244 16.957602000000001 18.523 20.088360999999999 21.653728999999998
		 23.219121000000001 24.784486999999999 30.784486999999999 32.349851999999998 33.915246000000003
		 35.480611000000003 37.045976000000003 38.611370000000001 40.176735000000001 41.742100000000001
		 43.307493999999998 44.872858999999998 46.438223999999998 48.003618000000003 49.568983000000003
		 55.568983000000003 57.134349 58.699741000000003 60.265109000000002 61.830469999999998
		 63.395868 64.961225999999996 70.961225999999996 72.526584 74.091982000000002 75.657342999999997
		 77.222712000000001 78.788104000000004 80.353470000000002 86.353470000000002 87.918834000000004
		 89.484228999999999 91.049593999999999 92.614958999999999 94.180352999999997 95.745717999999997
		 101.745718 107.745718 109.311083 110.87647699999999 112.44184199999999 114.00720699999999
		 115.57260100000001 117.13796600000001
		56
		13.810079983186778 -0.34463613519829361 4.0943128577737413
		13.327427980749563 -3.4572299092015029 4.0943127935447619
		11.948614564749967 -6.2149411290357577 4.0943126100590543
		9.7652021938150124 -8.3355044424183138 4.0943123195012365
		6.8992112110720214 -9.6734012706933186 4.0943119381092332
		3.570466472905744 -10.341329847926142 4.0943114951362194
		-1.1018473394408701e-06 -10.538819620923533 4.0943110199959092
		-9.8424676674985356e-07 -10.538819620923537 -4.096312152767088
		3.5704665905063293 -10.341329847926147 -4.0963116776267832
		6.8992113286725907 -9.6734012706933257 -4.0963112346537693
		9.7652023114155888 -8.3355044424183191 -4.0963108532617643
		11.948614682350522 -6.2149411290357612 -4.0963105627039491
		13.327428098350136 -3.4572299092015055 -4.0963103792182132
		13.810080100787351 -0.34463613519829356 -4.0963103149892559
		13.810079983186778 -0.34463613519829361 4.0943128577737413
		13.327428599325357 2.7679561428409882 4.0943127935448507
		11.948615731375563 5.525675685363729 4.0943126100592169
		9.7652037818668678 7.6462366505360198 4.0943123195014488
		6.8992130650100547 8.9841491873752428 4.094311938109481
		3.5704684595818779 9.6520622692161382 4.0943114951364823
		9.2408541940019979e-07 9.8496410393043092 4.0943110199961783
		-3.5704666506764569 9.6520628184581927 4.0943105448558734
		-6.8992113888411257 8.9841502486752951 4.0943101018828649
		-9.7652023715856373 7.6462381527090093 4.0943097204908367
		-11.948614742520327 5.5256775234091711 4.0943094299330474
		-13.327428158520739 2.7679581929880914 4.0943092464473079
		-13.810080160957769 -0.34463401080527806 4.0943091822183373
		-13.810080043357198 -0.34463401080527778 -4.0963139905446493
		-13.327428659495936 -3.4572278590543943 -4.0963139263157711
		-11.948615791545356 -6.2149392909903183 -4.0963137428301142
		-9.7652038420369323 -8.335502940245334 -4.0963134522723754
		-6.8992131251786075 -9.6734002093932769 -4.0963130708803792
		-3.5704685197520196 -10.341329298684093 -4.0963126279073796
		-9.8424676674985356e-07 -10.538819620923537 -4.096312152767088
		-1.1018473394408701e-06 -10.538819620923533 4.0943110199959092
		-3.5704686373525902 -10.341329298684085 4.0943105448556105
		-6.8992132427791724 -9.6734002093932698 4.0943101018826216
		-9.7652039596375033 -8.3355029402453304 4.0943097204906271
		-11.948615909145927 -6.2149392909903129 4.0943094299328751
		-13.327428777096499 -3.4572278590543917 4.0943092464472279
		-13.810080160957769 -0.34463401080527806 4.0943091822183373
		-13.810080043357198 -0.34463401080527778 -4.0963139905446493
		-13.327428040920179 2.7679581929880936 -4.0963139263156831
		-11.948614624919751 5.5256775234091773 -4.0963137428299508
		-9.7652022539850751 7.646238152709012 -4.096313452272156
		-6.8992112712405538 8.9841502486752987 -4.0963130708801208
		-3.570466533075884 9.652062818458198 -4.0963126279071194
		1.0416859920912192e-06 9.8496410393043146 -4.0963121527668189
		9.2408541940019979e-07 9.8496410393043092 4.0943110199961783
		1.0416859920912192e-06 9.8496410393043146 -4.0963121527668189
		3.5704685771824622 9.6520622692161453 -4.0963116776265167
		6.8992131826106169 8.9841491873752481 -4.0963112346535162
		9.7652038994674477 7.646236650536026 -4.0963108532615351
		11.948615848976143 5.5256756853637334 -4.0963105627037875
		13.327428716925947 2.76795614284099 -4.0963103792181448
		13.810080100787351 -0.34463613519829356 -4.0963103149892559
		;
createNode transform -n "hip_Gimbal_ctrl" -p "hip_ctrl";
	rename -uid "E314E3C3-479A-0FA2-7C6A-94B16E236683";
	setAttr ".rp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
	setAttr ".sp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
createNode nurbsCurve -n "hip_Gimbal_ctrlShape" -p "hip_Gimbal_ctrl";
	rename -uid "E991E01C-4680-7B3F-93A0-AB8B62726196";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 55 0 no 3
		56 0 1.565366 3.1307580000000002 4.6961259999999996 6.2614869999999998 7.8268849999999999
		 9.3922439999999998 15.392244 16.957602000000001 18.523 20.088360999999999 21.653728999999998
		 23.219121000000001 24.784486999999999 30.784486999999999 32.349851999999998 33.915246000000003
		 35.480611000000003 37.045976000000003 38.611370000000001 40.176735000000001 41.742100000000001
		 43.307493999999998 44.872858999999998 46.438223999999998 48.003618000000003 49.568983000000003
		 55.568983000000003 57.134349 58.699741000000003 60.265109000000002 61.830469999999998
		 63.395868 64.961225999999996 70.961225999999996 72.526584 74.091982000000002 75.657342999999997
		 77.222712000000001 78.788104000000004 80.353470000000002 86.353470000000002 87.918834000000004
		 89.484228999999999 91.049593999999999 92.614958999999999 94.180352999999997 95.745717999999997
		 101.745718 107.745718 109.311083 110.87647699999999 112.44184199999999 114.00720699999999
		 115.57260100000001 117.13796600000001
		56
		10.327594107514209 0.29294071491857565 -2.6707494275295414
		9.9666523907462583 2.9386454228213039 -2.6707493856294229
		8.9355341545004396 5.2826999596804214 -2.6707492659315228
		7.3027125654505793 7.0851787760555949 -2.6707490763845594
		5.1594381144401433 8.2223910800893467 -2.6707488275814137
		2.6701024556032196 8.7901303707372449 -2.6707485386055714
		-8.2706845580307873e-07 8.9579966777850242 -2.6707482286452096
		-7.391232025240121e-07 8.9579966777850295 2.6724491915006614
		2.6701025435484809 8.7901303707372502 2.6724488815403107
		5.1594382023853873 8.222391080089352 2.6724485925644617
		7.3027126533958349 7.0851787760555993 2.672448343761324
		8.9355342424456996 5.2826999596804232 2.6724481542143499
		9.96665247869152 2.9386454228213048 2.6724480345164419
		10.327594195459467 0.2929407149185756 2.6724479926163309
		10.327594107514209 0.29294071491857565 -2.6707494275295414
		9.9666528533358889 -2.3527627214148139 -2.6707493856294762
		8.9355350269382345 -4.6968243325591406 -2.6707492659316259
		7.3027137530436299 -6.4993011529555877 -2.6707490763846895
		5.1594395008708913 -7.6365268092689282 -2.6707488275815732
		2.6701039412995211 -8.2042529288336929 -2.6707485386057348
		6.8798513216507802e-07 -8.3721948834086408 -2.6707482286453854
		-2.6701025946931156 -8.2042533956894435 -2.6707479186850307
		-5.1594382535288377 -7.6365277113739731 -2.6707476297091892
		-7.3027127045404177 -6.4993024298026265 -2.670747380906032
		-8.9355342935900772 -4.6968258948977688 -2.6707471913590841
		-9.9666525298365052 -2.3527644640398528 -2.6707470716611685
		-10.327594246604308 0.29293890918451232 -2.6707470297610514
		-10.327594158659062 0.29293890918451232 2.6724503903848147
		-9.9666529044808598 2.938643680196261 2.6724503484847557
		-8.9355350780826264 5.2826983973417958 2.672450228786893
		-7.302713804188218 7.0851774992085605 2.6724500392399779
		-5.1594395520143479 8.2223901779843089 2.6724497904368389
		-2.6701039924441652 8.7901299038815033 2.6724495014610037
		-7.391232025240121e-07 8.9579966777850295 2.6724491915006614
		-8.2706845580307873e-07 8.9579966777850242 -2.6707482286452096
		-2.6701040803894172 8.790129903881498 -2.6707479186848588
		-5.1594396399595981 8.2223901779843018 -2.670747629709032
		-7.3027138921334673 7.0851774992085597 -2.6707473809058966
		-8.9355351660278721 5.2826983973417949 -2.6707471913589775
		-9.9666529924261091 2.9386436801962592 -2.6707470716611175
		-10.327594246604308 0.29293890918451232 -2.6707470297610514
		-10.327594158659062 0.29293890918451232 2.6724503903848147
		-9.9666524418912559 -2.3527644640398542 2.6724503484847042
		-8.9355342056448315 -4.6968258948977732 2.6724502287867913
		-7.3027126165951675 -6.4993024298026336 2.6724500392398371
		-5.1594381655835875 -7.6365277113739758 2.6724497904366844
		-2.6701025067478641 -8.2042533956894435 2.6724495014608438
		7.7593038544414581e-07 -8.3721948834086444 2.6724491915004904
		6.8798513216507802e-07 -8.3721948834086408 -2.6707482286453854
		7.7593038544414581e-07 -8.3721948834086444 2.6724491915004904
		2.6701040292447824 -8.2042529288336965 2.6724488815401379
		5.1594395888161353 -7.6365268092689336 2.6724485925643005
		7.3027138409888854 -6.4993011529555949 2.6724483437611726
		8.9355351148834927 -4.6968243325591459 2.6724481542142495
		9.9666529412811471 -2.3527627214148157 2.6724480345163988
		10.327594195459467 0.2929407149185756 2.6724479926163309
		;
createNode transform -n "cog_Zro_grp" -p "hip";
	rename -uid "2338E4A5-4450-B156-5D48-E2B503B988F6";
createNode transform -n "cog_ctrl" -p "cog_Zro_grp";
	rename -uid "AD64AE36-4071-DB04-BF3E-37870963242F";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "cog_ctrlShape" -p "cog_ctrl";
	rename -uid "910547F0-4866-6EA0-2BFA-B0BB6A4D90DD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		9.2966095809929659 -0.66400330843586142 -7.9465558135919476
		23.547135352138657 4.5638374126072438 -7.9465558135919476
		23.547135352138657 4.5638374126072438 7.9465558135919476
		9.2966095809929659 -0.66400330843586142 7.9465558135919476
		9.2640732684855571 -0.66400330843586142 11.168328593221927
		-9.2640732684855571 -0.66400330843586142 11.168328593221927
		-9.2966095809929659 -0.66400330843586142 7.9465558135919476
		-23.547135352138657 4.5638374126072438 7.9465558135919476
		-23.547135352138657 4.5638374126072438 -7.9465558135919476
		-9.2966095809929659 -0.66400330843586142 -7.9465558135919476
		-9.2640732684855571 -0.66400330843586142 -11.168328593221927
		9.2640732684855571 -0.66400330843586142 -11.168328593221927
		9.2966095809929659 -0.66400330843586142 -7.9465558135919476
		;
createNode transform -n "cog_Gimbal_ctrl" -p "cog_ctrl";
	rename -uid "F2F8721F-48E2-2291-191E-3F9F6ED2D6F8";
	setAttr ".rp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
createNode nurbsCurve -n "cog_Gimbal_ctrlShape" -p "cog_Gimbal_ctrl";
	rename -uid "599688E5-4160-6273-DBAE-AEAD685D6DAE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		5.8947759652488845 7.2955635396140418e-15 -5.038736520918552
		14.930721389875076 3.3148589885456698 -5.038736520918552
		14.930721389875076 3.3148589885456698 5.038736520918552
		5.8947759652488845 7.2955635396140418e-15 5.038736520918552
		5.874145404043146 7.2955635396140418e-15 7.0815918846292663
		-5.874145404043146 7.2955635396140418e-15 7.0815918846292663
		-5.8947759652488845 7.2955635396140418e-15 5.038736520918552
		-14.930721389875076 3.3148589885456698 5.038736520918552
		-14.930721389875076 3.3148589885456698 -5.038736520918552
		-5.8947759652488845 7.2955635396140418e-15 -5.038736520918552
		-5.874145404043146 7.2955635396140418e-15 -7.0815918846292663
		5.874145404043146 7.2955635396140418e-15 -7.0815918846292663
		5.8947759652488845 7.2955635396140418e-15 -5.038736520918552
		;
createNode transform -n "IKFKGrpFront" -p "TMP_GRP";
	rename -uid "774E458C-41E4-28B5-FE66-6DBC5491B7B9";
	setAttr ".v" no;
createNode transform -n "FK" -p "IKFKGrpFront";
	rename -uid "4423663C-4062-5444-214B-0F9C39D65C63";
createNode transform -n "LFT" -p "|TMP_GRP|IKFKGrpFront|FK";
	rename -uid "D6BC1FE3-4D6E-1282-99FE-BDA899C3C1FD";
createNode transform -n "upLegFrontLFT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|FK|LFT";
	rename -uid "AFCDC606-477A-DFC8-C00A-DAAA7A0CE9E3";
createNode transform -n "upLegFrontLFT_FK_ctrl" -p "upLegFrontLFT_FK_Zro_grp";
	rename -uid "BE8965D0-4C46-3259-87D5-ECAD3398A1C2";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "upLegFrontLFT_FK_ctrlShape" -p "upLegFrontLFT_FK_ctrl";
	rename -uid "5A0609CC-454D-088A-75D9-A5875834D59E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.6257081489231364 0.096652831577271489 5.3729580599344029
		-0.014713393902743703 -0.38744265336480144 11.773796545138705
		4.1378686592451412 -0.44942501827285836 5.756501152452377
		13.094587611230942 2.2388542551407546 0.41393449135439198
		4.1892311703385596 -0.098353770313908379 -5.4019782321161776
		-1.0942525569641064 0.43723336169655103 -12.134282392683552
		-4.5743456378297136 0.44772407953622151 -5.7855213246341766
		-5.9221021618687191 3.6674507538558871 -0.074835455990221414
		-4.6257081489231364 0.096652831577271489 5.3729580599344029
		-0.014713393902743703 -0.38744265336480144 11.773796545138705
		4.1378686592451412 -0.44942501827285836 5.756501152452377
		;
createNode transform -n "upLegFrontLFT_FK_Gimbal_ctrl" -p "upLegFrontLFT_FK_ctrl";
	rename -uid "C2B2D751-4B55-9DAA-E183-1FA1731A7076";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
createNode nurbsCurve -n "upLegFrontLFT_FK_Gimbal_ctrlShape" -p "upLegFrontLFT_FK_Gimbal_ctrl";
	rename -uid "9576ECE5-4467-5367-6515-D5B164CE6A84";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.9318519494181596 0.082154971976049845 4.5670143517060833
		-0.012506407650825408 -0.32932619022471205 10.007727064129741
		3.517188337524876 -0.3820112003965605 4.8930259803463612
		11.130399446712806 1.9030261820050105 0.35184431841307379
		3.5608464719542821 -0.083600639631453047 -4.5916814965369088
		-0.9301146962529836 0.37164842257743741 -10.314140033019179
		-3.8881938149887501 0.38056553274115734 -4.9176931251772089
		-5.0337868604219045 3.1173332059128733 -0.063610136829847577
		-3.9318519494181596 0.082154971976049845 4.5670143517060833
		-0.012506407650825408 -0.32932619022471205 10.007727064129741
		3.517188337524876 -0.3820112003965605 4.8930259803463612
		;
createNode transform -n "ankleFrontLFT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|FK|LFT";
	rename -uid "A5837845-4E58-0CAA-777D-C29B108CEA33";
createNode transform -n "ankleFrontLFT_FK_ctrl" -p "ankleFrontLFT_FK_Zro_grp";
	rename -uid "F11F5FF9-48AB-61B6-8703-C39DFF24EAEB";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "ankleFrontLFT_FK_ctrlShape" -p "ankleFrontLFT_FK_ctrl";
	rename -uid "00974CE8-4AA1-1817-1267-19B8DA7718B3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		6.2535857091339926 0.42576575955346629 1.7368095944081221
		3.3338712071101759 0.30631580409725961 -1.4623408983774617
		-0.024488954134432063 0.16853961980228996 -5.1883801395094933
		-4.7267989704333164 0.047751391652301363 -1.6382238580866619
		-5.4933799203568796 2.8783703686577495 1.4574319667443068
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		;
createNode transform -n "ankleFrontLFT_FK_Gimbal_ctrl" -p "ankleFrontLFT_FK_ctrl";
	rename -uid "D72B249C-4A6C-4586-4511-70A0D3D54AEA";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
createNode nurbsCurve -n "ankleFrontLFT_FK_Gimbal_ctrlShape" -p "ankleFrontLFT_FK_Gimbal_ctrl";
	rename -uid "208DD7F6-49C2-FC5F-B3AE-47A8EB4130AC";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		5.3155478767443585 0.36190103881972491 1.4762881412301532
		2.8337905500241134 0.26036857668194918 -1.2429897776375933
		-0.02081558703380279 0.14325882003122503 -4.4101231325998196
		-4.0177791008878545 0.04058882610373471 -1.3924902933904131
		-4.6693729083228828 2.4466149565583657 1.2388171577159102
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		;
createNode transform -n "midLegFrontLFT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|FK|LFT";
	rename -uid "AF2CD152-46C2-23A3-C6C2-28AE1DF18969";
createNode transform -n "midLegFrontLFT_FK_ctrl" -p "midLegFrontLFT_FK_Zro_grp";
	rename -uid "762EF3D4-4935-3997-8715-A9A01AFC341B";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "midLegFrontLFT_FK_ctrlShape" -p "midLegFrontLFT_FK_ctrl";
	rename -uid "D776AD71-455E-0B6D-9F95-55AE1B3EBDA8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		6.2535857091339926 0.42576575955346629 1.7368095944081221
		3.3338712071101759 0.30631580409725961 -1.4623408983774617
		-0.024488954134432063 0.16853961980228996 -5.1883801395094933
		-4.7267989704333164 0.047751391652301363 -1.6382238580866619
		-5.4933799203568796 2.8783703686577495 1.4574319667443068
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		;
createNode transform -n "midLegFrontLFT_FK_Gimbal_ctrl" -p "midLegFrontLFT_FK_ctrl";
	rename -uid "3A6ECABC-4477-C177-53AB-708A0737161C";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
createNode nurbsCurve -n "midLegFrontLFT_FK_Gimbal_ctrlShape" -p "midLegFrontLFT_FK_Gimbal_ctrl";
	rename -uid "8F450D58-4873-5DAF-8807-C0AF95E8BF0A";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		5.3155478767443585 0.36190103881972491 1.4762881412301532
		2.8337905500241134 0.26036857668194918 -1.2429897776375933
		-0.02081558703380279 0.14325882003122503 -4.4101231325998196
		-4.0177791008878545 0.04058882610373471 -1.3924902933904131
		-4.6693729083228828 2.4466149565583657 1.2388171577159102
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		;
createNode transform -n "RGT" -p "|TMP_GRP|IKFKGrpFront|FK";
	rename -uid "0846CF71-41A3-5C53-FB4A-02B4753E146D";
createNode transform -n "midLegFrontRGT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|FK|RGT";
	rename -uid "5F996279-4FBC-7252-B7CA-E382AEA6B2CF";
createNode transform -n "midLegFrontRGT_FK_ctrl" -p "midLegFrontRGT_FK_Zro_grp";
	rename -uid "5D294D7A-4AC4-EACD-C757-8E8B9612DDA6";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "midLegFrontRGT_FK_ctrlShape" -p "midLegFrontRGT_FK_ctrl";
	rename -uid "4B7DC35A-4B57-85FD-31B2-7899C9230918";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		6.2535857091339926 0.42576575955346629 1.7368095944081221
		3.3338712071101759 0.30631580409725961 -1.4623408983774617
		-0.024488954134432063 0.16853961980228996 -5.1883801395094933
		-4.7267989704333164 0.047751391652301363 -1.6382238580866619
		-5.4933799203568796 2.8783703686577495 1.4574319667443068
		-4.8650756676652192 0.094902734719055609 4.6296442294928877
		0.4496478444556985 0.2940376888506851 8.2286671771911344
		3.1955945098782741 0.35346714716401367 4.8055271892021008
		;
createNode transform -n "midLegFrontRGT_FK_Gimbal_ctrl" -p "midLegFrontRGT_FK_ctrl";
	rename -uid "6FE2998D-4C3C-7E6D-AA8B-0AA2B0F33F2B";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
createNode nurbsCurve -n "midLegFrontRGT_FK_Gimbal_ctrlShape" -p "midLegFrontRGT_FK_Gimbal_ctrl";
	rename -uid "EB5638C8-4BF8-9E6C-24F4-169D6D667256";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		5.3155478767443585 0.36190103881972491 1.4762881412301532
		2.8337905500241134 0.26036857668194918 -1.2429897776375933
		-0.02081558703380279 0.14325882003122503 -4.4101231325998196
		-4.0177791008878545 0.04058882610373471 -1.3924902933904131
		-4.6693729083228828 2.4466149565583657 1.2388171577159102
		-4.1353142935349716 0.080667467710475824 3.9351975810522037
		0.38220069176780813 0.2499321787223609 6.9943670865957133
		2.7162553573769972 0.3004472182886902 4.0846980968050355
		;
createNode transform -n "ankleFrontRGT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|FK|RGT";
	rename -uid "0A7B46C2-455D-DA68-CB52-4FA758C2D596";
	setAttr ".rp" -type "double3" 0 -1.139931803064694e-16 0 ;
	setAttr ".sp" -type "double3" 1.8238908849035105e-15 -1.139931803064694e-16 0 ;
createNode transform -n "ankleFrontRGT_FK_ctrl" -p "ankleFrontRGT_FK_Zro_grp";
	rename -uid "B73E5056-47D9-DB7E-0CB5-1B856DE5D78B";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr ".sp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "ankleFrontRGT_FK_ctrlShape" -p "ankleFrontRGT_FK_ctrl";
	rename -uid "0C50D9B9-433C-CD4D-6646-FD8AD29832B7";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.8650712827205354 -0.094922294227107018 -4.629642496102246
		-0.44965222940039684 -0.29405724835873842 -8.2286654438004501
		-3.1955988948229654 -0.35348670667207788 -4.8055254558114111
		-6.2535900940786728 -0.42578531906153766 -1.7368078610174549
		-3.3338755920548784 -0.30633536360532704 1.4623426317681247
		0.02448456918973833 -0.16855917931035744 5.1883818729001616
		4.7267945854886424 -0.047770951160355839 1.6382255914773054
		5.493375535412218 -2.8783899281657961 -1.4574302333536628
		4.8650712827205354 -0.094922294227107018 -4.629642496102246
		-0.44965222940039684 -0.29405724835873842 -8.2286654438004501
		-3.1955988948229654 -0.35348670667207788 -4.8055254558114111
		;
createNode transform -n "ankleFrontRGT_FK_Gimbal_ctrl" -p "ankleFrontRGT_FK_ctrl";
	rename -uid "F0093D2A-4D8C-356C-1302-A49378F169CD";
	setAttr ".rp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr ".sp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
createNode nurbsCurve -n "ankleFrontRGT_FK_Gimbal_ctrlShape" -p "ankleFrontRGT_FK_Gimbal_ctrl";
	rename -uid "A577C95A-4EB2-0B2E-A7E1-478FEF98D49A";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		4.1353099085902878 -0.080687027218528065 -3.9351958476615607
		-0.38220507671250498 -0.24995173823041475 -6.9943653532050343
		-2.7162597423216881 -0.30046677779675329 -4.0846963634143512
		-5.3155522616890396 -0.36192059832779405 -1.4762864078394877
		-2.8337949349688145 -0.26038813619001511 1.2429915110282546
		0.020811202089109908 -0.1432783795392909 4.4101248659904853
		4.0177747159431787 -0.040608385611789574 1.3924920267810581
		4.6693685233782176 -2.446634516066414 -1.2388154243252647
		4.1353099085902878 -0.080687027218528065 -3.9351958476615607
		-0.38220507671250498 -0.24995173823041475 -6.9943653532050343
		-2.7162597423216881 -0.30046677779675329 -4.0846963634143512
		;
createNode transform -n "upLegFrontRGT_FK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|FK|RGT";
	rename -uid "3B909BDF-46B2-9B37-5B46-52A767B4A57D";
createNode transform -n "upLegFrontRGT_FK_ctrl" -p "upLegFrontRGT_FK_Zro_grp";
	rename -uid "6EF10360-47E2-02E8-B428-80AC2564D780";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "upLegFrontRGT_FK_ctrlShape" -p "upLegFrontRGT_FK_ctrl";
	rename -uid "739FDF1C-455C-4204-145A-BCA602D513E1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-4.6257081489231364 0.096652831577271489 5.3729580599344029
		-0.014713393902743703 -0.38744265336480144 11.773796545138705
		4.1378686592451412 -0.44942501827285836 5.756501152452377
		13.094587611230942 2.2388542551407546 0.41393449135439198
		4.1892311703385596 -0.098353770313908379 -5.4019782321161776
		-1.0942525569641064 0.43723336169655103 -12.134282392683552
		-4.5743456378297136 0.44772407953622151 -5.7855213246341766
		-5.9221021618687191 3.6674507538558871 -0.074835455990221414
		-4.6257081489231364 0.096652831577271489 5.3729580599344029
		-0.014713393902743703 -0.38744265336480144 11.773796545138705
		4.1378686592451412 -0.44942501827285836 5.756501152452377
		;
createNode transform -n "upLegFrontRGT_FK_Gimbal_ctrl" -p "upLegFrontRGT_FK_ctrl";
	rename -uid "D4A82CBE-41BB-80B2-DDB8-039C3E621FF3";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
createNode nurbsCurve -n "upLegFrontRGT_FK_Gimbal_ctrlShape" -p "upLegFrontRGT_FK_Gimbal_ctrl";
	rename -uid "6218CD2A-4CD4-99E7-558A-359DA2125629";
	setAttr -k off ".v" no;
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-3.9318519494181596 0.082154971976049845 4.5670143517060833
		-0.012506407650825408 -0.32932619022471205 10.007727064129741
		3.517188337524876 -0.3820112003965605 4.8930259803463612
		11.130399446712806 1.9030261820050105 0.35184431841307379
		3.5608464719542821 -0.083600639631453047 -4.5916814965369088
		-0.9301146962529836 0.37164842257743741 -10.314140033019179
		-3.8881938149887501 0.38056553274115734 -4.9176931251772089
		-5.0337868604219045 3.1173332059128733 -0.063610136829847577
		-3.9318519494181596 0.082154971976049845 4.5670143517060833
		-0.012506407650825408 -0.32932619022471205 10.007727064129741
		3.517188337524876 -0.3820112003965605 4.8930259803463612
		;
createNode transform -n "IK" -p "IKFKGrpFront";
	rename -uid "43DE0E82-4142-7EDB-BA20-AA80D7B5BE53";
createNode transform -n "ankleFrontLFT_IK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|IK";
	rename -uid "0240D37D-4C7F-4E78-A4EE-EA8C577435D1";
createNode transform -n "ankleFrontLFT_IK_ctrl" -p "ankleFrontLFT_IK_Zro_grp";
	rename -uid "CC518B7B-4860-31A0-D70D-53942000D7BB";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr -l on -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "ankleFrontLFT_IK_ctrlShape" -p "ankleFrontLFT_IK_ctrl";
	rename -uid "F5C9F2F3-4501-8330-024C-2F9558E25420";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		;
createNode transform -n "ankleFrontRGT_IK_Zro_grp" -p "|TMP_GRP|IKFKGrpFront|IK";
	rename -uid "1019B8E9-4736-DAD6-740F-16B54D4D6708";
createNode transform -n "ankleFrontRGT_IK_ctrl" -p "ankleFrontRGT_IK_Zro_grp";
	rename -uid "D5C4DD6C-4D8B-C5E8-13AC-8FB195173D59";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr -l on -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "ankleFrontRGT_IK_ctrlShape" -p "ankleFrontRGT_IK_ctrl";
	rename -uid "B01C41A3-4C7B-4485-A244-A99206316BE0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 -3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 3.1579939035444724
		3.1579939035444724 3.1579939035444724 -3.1579939035444724
		3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 -3.1579939035444724 -3.1579939035444724
		-3.1579939035444724 3.1579939035444724 -3.1579939035444724
		;
createNode transform -n "POV1" -p "TMP_GRP";
	rename -uid "09C4FF33-47FF-7F5D-8E70-AA86292E5B04";
	setAttr ".v" no;
createNode transform -n "legPovFrontLFT_Zro_grp" -p "POV1";
	rename -uid "11200090-46CD-F410-AD98-738401B832DD";
createNode transform -n "legPovFrontLFT_ctrl" -p "legPovFrontLFT_Zro_grp";
	rename -uid "445C1E8F-47E0-4A53-CF91-8AB2AFE58215";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "legPovFrontLFT_ctrlShape" -p "legPovFrontLFT_ctrl";
	rename -uid "E97D42F2-45EB-A50C-B8D4-AEB04E8C9CDF";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 1.7991854165801995 0
		0 -1.7991854165801995 0
		0 0 0
		0 0 -1.7991854165801995
		0 0 1.7991854165801995
		0 0 0
		1.7991854165801995 0 0
		-1.7991854165801995 0 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0.22516301716584575 0
		-1.3689023077892113 0.44478310390029102 0
		-1.2824694403766994 0.65345118916692957 0
		-1.1644572705323701 0.84602736006767465 0
		-1.0177732818894205 1.0177732818894205 0
		-0.84602736006767465 1.1644572705323701 0
		-0.65345118916692957 1.2824694403766994 0
		-0.44478310390029102 1.3689023077892113 0
		-0.22516445651417891 1.4216270765850112 0
		0 1.4393483332641601 0
		0.22516301716584575 1.4216270765850112 0
		0.44478310390029102 1.3689023077892113 0
		0.65345118916692957 1.2824694403766994 0
		0.84602736006767465 1.1644572705323701 0
		1.0177732818894205 1.0177732818894205 0
		1.1644572705323701 0.84602736006767465 0
		1.2824694403766994 0.65345118916692957 0
		1.3689023077892113 0.44478310390029102 0
		1.4216270765850112 0.22516301716584575 0
		1.4393483332641601 0 0
		1.4216270765850112 -0.22516301716584575 0
		1.3689023077892113 -0.44478310390029102 0
		1.2824694403766994 -0.65345118916692957 0
		1.1644572705323701 -0.84602736006767465 0
		1.0177732818894205 -1.0177732818894205 0
		0.84602736006767465 -1.1644572705323701 0
		0.65345118916692957 -1.2824694403766994 0
		0.44478310390029102 -1.3689023077892113 0
		0.22516301716584575 -1.4216270765850112 0
		0 -1.4393483332641601 0
		-0.22516445651417891 -1.4216270765850112 0
		-0.44478310390029102 -1.3689023077892113 0
		-0.65345118916692957 -1.2824694403766994 0
		-0.84602736006767465 -1.1644572705323701 0
		-1.0177732818894205 -1.0177732818894205 0
		-1.1644572705323701 -0.84602736006767465 0
		-1.2824694403766994 -0.65345118916692957 0
		-1.3689023077892113 -0.44478310390029102 0
		-1.4216285159333439 -0.22516301716584575 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		0.22516301716584575 0 1.4216270765850112
		0.44478310390029102 0 1.3689023077892113
		0.65345118916692957 0 1.2824694403766994
		0.84602736006767465 0 1.1644572705323701
		1.0177732818894205 0 1.0177732818894205
		1.1644572705323701 0 0.84602736006767465
		1.2824694403766994 0 0.65345118916692957
		1.3689023077892113 0 0.44478310390029102
		1.4216270765850112 0 0.22516301716584575
		1.4393483332641601 0 0
		1.4216270765850112 0 -0.22516301716584575
		1.3689023077892113 0 -0.44478310390029102
		1.2824694403766994 0 -0.65345118916692957
		1.1644572705323701 0 -0.84602736006767465
		1.0177732818894205 0 -1.0177732818894205
		0.84602736006767465 0 -1.1644572705323701
		0.65345118916692957 0 -1.2824694403766994
		0.44478310390029102 0 -1.3689023077892113
		0.22516301716584575 0 -1.4216270765850112
		0 0 -1.4393483332641601
		-0.22516445651417891 0 -1.4216270765850112
		-0.44478310390029102 0 -1.3689023077892113
		-0.65345118916692957 0 -1.2824694403766994
		-0.84602736006767465 0 -1.1644572705323701
		-1.0177732818894205 0 -1.0177732818894205
		-1.1644572705323701 0 -0.84602736006767465
		-1.2824694403766994 0 -0.65345118916692957
		-1.3689023077892113 0 -0.44478310390029102
		-1.4216285159333439 0 -0.22516301716584575
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		-6.7104002579941741e-09 0.22516301716584575 1.4216270765850112
		-1.3255563327329612e-08 0.44478310390029102 1.3689023077892113
		-1.947438294906409e-08 0.65345118916692957 1.2824694403766994
		-2.5213640493121609e-08 0.84602736006767465 1.1644572705323701
		-3.0331963166208942e-08 1.0177732818894205 1.0177732818894205
		-3.4703551923998864e-08 1.1644572705323701 0.84602736006767465
		-3.822059957632979e-08 1.2824694403766994 0.65345118916692957
		-4.0796457353539337e-08 1.3689023077892113 0.44478310390029102
		-4.2367793928963873e-08 1.4216270765850112 0.22516301716584575
		-4.2895890832438451e-08 1.4393483332641601 0
		-4.2367793928963873e-08 1.4216270765850112 -0.22516301716584575
		-4.0796457353539337e-08 1.3689023077892113 -0.44478310390029102
		-3.822059957632979e-08 1.2824694403766994 -0.65345118916692957
		-3.4703551923998864e-08 1.1644572705323701 -0.84602736006767465
		-3.0331963166208942e-08 1.0177732818894205 -1.0177732818894205
		-2.5213640493121609e-08 0.84602736006767465 -1.1644572705323701
		-1.947438294906409e-08 0.65345118916692957 -1.2824694403766994
		-1.3255563327329612e-08 0.44478310390029102 -1.3689023077892113
		-6.7104002579941741e-09 0.22516301716584575 -1.4216270765850112
		0 0 -1.4393483332641601
		0 -0.22516445651417891 -1.4216270765850112
		0 -0.44478310390029102 -1.3689023077892113
		0 -0.65345118916692957 -1.2824694403766994
		0 -0.84602879941600828 -1.1644572705323701
		0 -1.0177732818894205 -1.0177732818894205
		0 -1.1644572705323701 -0.84602736006767465
		0 -1.2824694403766994 -0.65345118916692957
		0 -1.3689023077892113 -0.44478310390029102
		0 -1.4216285159333439 -0.22516301716584575
		0 -1.4393483332641601 0
		0 -1.4216285159333439 0.22516301716584575
		0 -1.3689023077892113 0.44478310390029102
		0 -1.2824694403766994 0.65345118916692957
		0 -1.1644572705323701 0.84602736006767465
		0 -1.0177732818894205 1.0177732818894205
		0 -0.84602879941600828 1.1644572705323701
		0 -0.65345118916692957 1.2824694403766994
		0 -0.44478310390029102 1.3689023077892113
		0 -0.22516445651417891 1.4216270765850112
		0 0 1.4393483332641601
		;
createNode transform -n "legPovFrontRGT_Zro_grp" -p "POV1";
	rename -uid "52F3B37B-4E90-EE93-A6ED-87A4AE3100EE";
createNode transform -n "legPovFrontRGT_ctrl" -p "legPovFrontRGT_Zro_grp";
	rename -uid "26B5C5AC-4A91-0AD9-4E9A-A4AD5B89A8B1";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "legPovFrontRGT_ctrlShape" -p "legPovFrontRGT_ctrl";
	rename -uid "084D3AEB-48FD-9CD0-8C8B-999B31E685B0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 138 0 no 3
		139 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54
		 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81
		 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106
		 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127
		 128 129 130 131 132 133 134 135 136 137 138
		139
		0 1.7991854165801995 0
		0 -1.7991854165801995 0
		0 0 0
		0 0 -1.7991854165801995
		0 0 1.7991854165801995
		0 0 0
		1.7991854165801995 0 0
		-1.7991854165801995 0 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0.22516301716584575 0
		-1.3689023077892113 0.44478310390029102 0
		-1.2824694403766994 0.65345118916692957 0
		-1.1644572705323701 0.84602736006767465 0
		-1.0177732818894205 1.0177732818894205 0
		-0.84602736006767465 1.1644572705323701 0
		-0.65345118916692957 1.2824694403766994 0
		-0.44478310390029102 1.3689023077892113 0
		-0.22516445651417891 1.4216270765850112 0
		0 1.4393483332641601 0
		0.22516301716584575 1.4216270765850112 0
		0.44478310390029102 1.3689023077892113 0
		0.65345118916692957 1.2824694403766994 0
		0.84602736006767465 1.1644572705323701 0
		1.0177732818894205 1.0177732818894205 0
		1.1644572705323701 0.84602736006767465 0
		1.2824694403766994 0.65345118916692957 0
		1.3689023077892113 0.44478310390029102 0
		1.4216270765850112 0.22516301716584575 0
		1.4393483332641601 0 0
		1.4216270765850112 -0.22516301716584575 0
		1.3689023077892113 -0.44478310390029102 0
		1.2824694403766994 -0.65345118916692957 0
		1.1644572705323701 -0.84602736006767465 0
		1.0177732818894205 -1.0177732818894205 0
		0.84602736006767465 -1.1644572705323701 0
		0.65345118916692957 -1.2824694403766994 0
		0.44478310390029102 -1.3689023077892113 0
		0.22516301716584575 -1.4216270765850112 0
		0 -1.4393483332641601 0
		-0.22516445651417891 -1.4216270765850112 0
		-0.44478310390029102 -1.3689023077892113 0
		-0.65345118916692957 -1.2824694403766994 0
		-0.84602736006767465 -1.1644572705323701 0
		-1.0177732818894205 -1.0177732818894205 0
		-1.1644572705323701 -0.84602736006767465 0
		-1.2824694403766994 -0.65345118916692957 0
		-1.3689023077892113 -0.44478310390029102 0
		-1.4216285159333439 -0.22516301716584575 0
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		0.22516301716584575 0 1.4216270765850112
		0.44478310390029102 0 1.3689023077892113
		0.65345118916692957 0 1.2824694403766994
		0.84602736006767465 0 1.1644572705323701
		1.0177732818894205 0 1.0177732818894205
		1.1644572705323701 0 0.84602736006767465
		1.2824694403766994 0 0.65345118916692957
		1.3689023077892113 0 0.44478310390029102
		1.4216270765850112 0 0.22516301716584575
		1.4393483332641601 0 0
		1.4216270765850112 0 -0.22516301716584575
		1.3689023077892113 0 -0.44478310390029102
		1.2824694403766994 0 -0.65345118916692957
		1.1644572705323701 0 -0.84602736006767465
		1.0177732818894205 0 -1.0177732818894205
		0.84602736006767465 0 -1.1644572705323701
		0.65345118916692957 0 -1.2824694403766994
		0.44478310390029102 0 -1.3689023077892113
		0.22516301716584575 0 -1.4216270765850112
		0 0 -1.4393483332641601
		-0.22516445651417891 0 -1.4216270765850112
		-0.44478310390029102 0 -1.3689023077892113
		-0.65345118916692957 0 -1.2824694403766994
		-0.84602736006767465 0 -1.1644572705323701
		-1.0177732818894205 0 -1.0177732818894205
		-1.1644572705323701 0 -0.84602736006767465
		-1.2824694403766994 0 -0.65345118916692957
		-1.3689023077892113 0 -0.44478310390029102
		-1.4216285159333439 0 -0.22516301716584575
		-1.4393483332641601 0 0
		-1.4216285159333439 0 0.22516301716584575
		-1.3689023077892113 0 0.44478310390029102
		-1.2824694403766994 0 0.65345118916692957
		-1.1644572705323701 0 0.84602736006767465
		-1.0177732818894205 0 1.0177732818894205
		-0.84602736006767465 0 1.1644572705323701
		-0.65345118916692957 0 1.2824694403766994
		-0.44478310390029102 0 1.3689023077892113
		-0.22516445651417891 0 1.4216270765850112
		0 0 1.4393483332641601
		-6.7104002579941741e-09 0.22516301716584575 1.4216270765850112
		-1.3255563327329612e-08 0.44478310390029102 1.3689023077892113
		-1.947438294906409e-08 0.65345118916692957 1.2824694403766994
		-2.5213640493121609e-08 0.84602736006767465 1.1644572705323701
		-3.0331963166208942e-08 1.0177732818894205 1.0177732818894205
		-3.4703551923998864e-08 1.1644572705323701 0.84602736006767465
		-3.822059957632979e-08 1.2824694403766994 0.65345118916692957
		-4.0796457353539337e-08 1.3689023077892113 0.44478310390029102
		-4.2367793928963873e-08 1.4216270765850112 0.22516301716584575
		-4.2895890832438451e-08 1.4393483332641601 0
		-4.2367793928963873e-08 1.4216270765850112 -0.22516301716584575
		-4.0796457353539337e-08 1.3689023077892113 -0.44478310390029102
		-3.822059957632979e-08 1.2824694403766994 -0.65345118916692957
		-3.4703551923998864e-08 1.1644572705323701 -0.84602736006767465
		-3.0331963166208942e-08 1.0177732818894205 -1.0177732818894205
		-2.5213640493121609e-08 0.84602736006767465 -1.1644572705323701
		-1.947438294906409e-08 0.65345118916692957 -1.2824694403766994
		-1.3255563327329612e-08 0.44478310390029102 -1.3689023077892113
		-6.7104002579941741e-09 0.22516301716584575 -1.4216270765850112
		0 0 -1.4393483332641601
		0 -0.22516445651417891 -1.4216270765850112
		0 -0.44478310390029102 -1.3689023077892113
		0 -0.65345118916692957 -1.2824694403766994
		0 -0.84602879941600828 -1.1644572705323701
		0 -1.0177732818894205 -1.0177732818894205
		0 -1.1644572705323701 -0.84602736006767465
		0 -1.2824694403766994 -0.65345118916692957
		0 -1.3689023077892113 -0.44478310390029102
		0 -1.4216285159333439 -0.22516301716584575
		0 -1.4393483332641601 0
		0 -1.4216285159333439 0.22516301716584575
		0 -1.3689023077892113 0.44478310390029102
		0 -1.2824694403766994 0.65345118916692957
		0 -1.1644572705323701 0.84602736006767465
		0 -1.0177732818894205 1.0177732818894205
		0 -0.84602879941600828 1.1644572705323701
		0 -0.65345118916692957 1.2824694403766994
		0 -0.44478310390029102 1.3689023077892113
		0 -0.22516445651417891 1.4216270765850112
		0 0 1.4393483332641601
		;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "9143242D-43D8-A344-CD8A-03BBFD7C23EC";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "59CE1D99-489F-8F10-323F-CABE1975BEA0";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "3FDCB205-4FF5-5AE2-79BB-508BA0F5CECB";
createNode displayLayerManager -n "layerManager";
	rename -uid "F1BB0B03-420B-32D5-E171-F9B87A558ED5";
createNode displayLayer -n "defaultLayer";
	rename -uid "852C260C-4CB2-5BE7-EF6E-15A2F3E77207";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "48C1CA30-4B4E-37CC-71E1-AD8A6F3AFECD";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "BBE746D0-473C-4743-B98A-03AD9B6AA0FE";
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
	rename -uid "27F4ABC8-4F22-BD36-BBE7-18A7373C240D";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 120 -ast 0 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "1507CAEE-4459-812E-EB35-E0B76D4D3624";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -467.85712426617113 -161.90475547124495 ;
	setAttr ".tgi[0].vh" -type "double2" 448.80950597543642 170.23808847344139 ;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "9C62EF0B-44B6-A87E-9AF4-7285ADB6D1C3";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "DE0578E2-4B07-BA4A-4132-B8A4FCA8E469";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -133.33332803514296 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "936E3716-41F0-4E87-6E73-0C9A8E745269";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -467.85712426617113 -161.90475547124495 ;
	setAttr ".tgi[0].vh" -type "double2" 448.80950597543642 170.23808847344139 ;
createNode objectSet -n "pasted__textureEditorIsolateSelectSet";
	rename -uid "1857777C-4659-A22C-C38A-7AB2FE157877";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "9667570C-4FB7-3A8B-E38B-7A89E9A59DEC";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -133.33332803514296 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "7A15E136-4611-D79C-08AB-B490D15A0551";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -133.33332803514296 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo2";
	rename -uid "63FC53F5-4D0B-8582-690B-51AE05FD9A5C";
	setAttr ".def" no;
	setAttr -s 6 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -8965.9337096598701 3394.0474841802684 ;
	setAttr ".tgi[0].vh" -type "double2" -4262.6371932553784 4667.8569573731511 ;
	setAttr ".tgi[1].tn" -type "string" "Untitled_2";
	setAttr ".tgi[1].vl" -type "double2" -3021.8863268074738 -1078.5713857128526 ;
	setAttr ".tgi[1].vh" -type "double2" 3967.1243844851833 814.28568192890862 ;
	setAttr -s 13 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" 136.584228515625;
	setAttr ".tgi[1].ni[0].y" 278.64724731445313;
	setAttr ".tgi[1].ni[0].nvs" 18306;
	setAttr ".tgi[1].ni[1].x" 785.67388916015625;
	setAttr ".tgi[1].ni[1].y" 557.975830078125;
	setAttr ".tgi[1].ni[1].nvs" 18306;
	setAttr ".tgi[1].ni[2].x" -329.22616577148438;
	setAttr ".tgi[1].ni[2].y" -645.9437255859375;
	setAttr ".tgi[1].ni[2].nvs" 18338;
	setAttr ".tgi[1].ni[3].x" 454.61441040039063;
	setAttr ".tgi[1].ni[3].y" 913.44415283203125;
	setAttr ".tgi[1].ni[3].nvs" 18306;
	setAttr ".tgi[1].ni[4].x" -336.21728515625;
	setAttr ".tgi[1].ni[4].y" 749.25250244140625;
	setAttr ".tgi[1].ni[4].nvs" 18306;
	setAttr ".tgi[1].ni[5].x" 791.8331298828125;
	setAttr ".tgi[1].ni[5].y" -16.145772933959961;
	setAttr ".tgi[1].ni[5].nvs" 18306;
	setAttr ".tgi[1].ni[6].x" 1080.9959716796875;
	setAttr ".tgi[1].ni[6].y" 686.84454345703125;
	setAttr ".tgi[1].ni[6].nvs" 18305;
	setAttr ".tgi[1].ni[7].x" 694.2047119140625;
	setAttr ".tgi[1].ni[7].y" -620.01611328125;
	setAttr ".tgi[1].ni[7].nvs" 18306;
	setAttr ".tgi[1].ni[8].x" 1066.9603271484375;
	setAttr ".tgi[1].ni[8].y" 257.40219116210938;
	setAttr ".tgi[1].ni[8].nvs" 18306;
	setAttr ".tgi[1].ni[9].x" 925.4886474609375;
	setAttr ".tgi[1].ni[9].y" -983.5941162109375;
	setAttr ".tgi[1].ni[9].nvs" 18306;
	setAttr ".tgi[1].ni[10].x" -1075.66357421875;
	setAttr ".tgi[1].ni[10].y" 351.38201904296875;
	setAttr ".tgi[1].ni[10].nvs" 18304;
	setAttr ".tgi[1].ni[11].x" 650.67596435546875;
	setAttr ".tgi[1].ni[11].y" -1134.962890625;
	setAttr ".tgi[1].ni[11].nvs" 18306;
	setAttr ".tgi[1].ni[12].x" 162.0501708984375;
	setAttr ".tgi[1].ni[12].y" 1112.7357177734375;
	setAttr ".tgi[1].ni[12].nvs" 18306;
	setAttr ".tgi[2].tn" -type "string" "Untitled_3";
	setAttr ".tgi[2].vl" -type "double2" -2260.8973460574484 -609.52378530351041 ;
	setAttr ".tgi[2].vh" -type "double2" 1963.2783102647163 534.52378828374253 ;
	setAttr -s 12 ".tgi[2].ni";
	setAttr ".tgi[2].ni[0].x" 426.14068603515625;
	setAttr ".tgi[2].ni[0].y" 438.91098022460938;
	setAttr ".tgi[2].ni[0].nvs" 18306;
	setAttr ".tgi[2].ni[1].x" -259.734375;
	setAttr ".tgi[2].ni[1].y" -505.96978759765625;
	setAttr ".tgi[2].ni[1].nvs" 18306;
	setAttr ".tgi[2].ni[2].x" 151.80900573730469;
	setAttr ".tgi[2].ni[2].y" 705.5516357421875;
	setAttr ".tgi[2].ni[2].nvs" 18306;
	setAttr ".tgi[2].ni[3].x" -713.66094970703125;
	setAttr ".tgi[2].ni[3].y" 515.24188232421875;
	setAttr ".tgi[2].ni[3].nvs" 18306;
	setAttr ".tgi[2].ni[4].x" -822.03961181640625;
	setAttr ".tgi[2].ni[4].y" 25.693260192871094;
	setAttr ".tgi[2].ni[4].nvs" 18306;
	setAttr ".tgi[2].ni[5].x" -631.22821044921875;
	setAttr ".tgi[2].ni[5].y" -362.80340576171875;
	setAttr ".tgi[2].ni[5].nvs" 18306;
	setAttr ".tgi[2].ni[6].x" 367.247802734375;
	setAttr ".tgi[2].ni[6].y" -18.839021682739258;
	setAttr ".tgi[2].ni[6].nvs" 18306;
	setAttr ".tgi[2].ni[7].x" 645.73236083984375;
	setAttr ".tgi[2].ni[7].y" 502.82647705078125;
	setAttr ".tgi[2].ni[7].nvs" 18305;
	setAttr ".tgi[2].ni[8].x" -320.96444702148438;
	setAttr ".tgi[2].ni[8].y" -313.9049072265625;
	setAttr ".tgi[2].ni[8].nvs" 18305;
	setAttr ".tgi[2].ni[9].x" -67.772872924804688;
	setAttr ".tgi[2].ni[9].y" 752.6905517578125;
	setAttr ".tgi[2].ni[9].nvs" 18306;
	setAttr ".tgi[2].ni[10].x" 50.994682312011719;
	setAttr ".tgi[2].ni[10].y" 247.88175964355469;
	setAttr ".tgi[2].ni[10].nvs" 18306;
	setAttr ".tgi[2].ni[11].x" -1011.0081787109375;
	setAttr ".tgi[2].ni[11].y" -322.93817138671875;
	setAttr ".tgi[2].ni[11].nvs" 18306;
	setAttr ".tgi[3].tn" -type "string" "Untitled_4";
	setAttr ".tgi[3].vl" -type "double2" -3755.2654185447268 2096.4284881239878 ;
	setAttr ".tgi[3].vh" -type "double2" -1953.0676879598282 2584.5237068240649 ;
	setAttr -s 24 ".tgi[3].ni";
	setAttr ".tgi[3].ni[0].x" 775.71429443359375;
	setAttr ".tgi[3].ni[0].y" -1898.5714111328125;
	setAttr ".tgi[3].ni[0].nvs" 18304;
	setAttr ".tgi[3].ni[1].x" -2530;
	setAttr ".tgi[3].ni[1].y" 2212.857177734375;
	setAttr ".tgi[3].ni[1].nvs" 18304;
	setAttr ".tgi[3].ni[2].x" -2088.571533203125;
	setAttr ".tgi[3].ni[2].y" 2274.28564453125;
	setAttr ".tgi[3].ni[2].nvs" 18304;
	setAttr ".tgi[3].ni[3].x" -2088.571533203125;
	setAttr ".tgi[3].ni[3].y" 2578.571533203125;
	setAttr ".tgi[3].ni[3].nvs" 18304;
	setAttr ".tgi[3].ni[4].x" -2088.571533203125;
	setAttr ".tgi[3].ni[4].y" 3187.142822265625;
	setAttr ".tgi[3].ni[4].nvs" 18304;
	setAttr ".tgi[3].ni[5].x" -2088.571533203125;
	setAttr ".tgi[3].ni[5].y" 2477.142822265625;
	setAttr ".tgi[3].ni[5].nvs" 18304;
	setAttr ".tgi[3].ni[6].x" -2088.571533203125;
	setAttr ".tgi[3].ni[6].y" 3897.142822265625;
	setAttr ".tgi[3].ni[6].nvs" 18304;
	setAttr ".tgi[3].ni[7].x" -2088.571533203125;
	setAttr ".tgi[3].ni[7].y" 2781.428466796875;
	setAttr ".tgi[3].ni[7].nvs" 18304;
	setAttr ".tgi[3].ni[8].x" -2088.571533203125;
	setAttr ".tgi[3].ni[8].y" 4100;
	setAttr ".tgi[3].ni[8].nvs" 18304;
	setAttr ".tgi[3].ni[9].x" -2088.571533203125;
	setAttr ".tgi[3].ni[9].y" 3592.857177734375;
	setAttr ".tgi[3].ni[9].nvs" 18304;
	setAttr ".tgi[3].ni[10].x" -2088.571533203125;
	setAttr ".tgi[3].ni[10].y" 3998.571533203125;
	setAttr ".tgi[3].ni[10].nvs" 18304;
	setAttr ".tgi[3].ni[11].x" -2088.571533203125;
	setAttr ".tgi[3].ni[11].y" 2071.428466796875;
	setAttr ".tgi[3].ni[11].nvs" 18304;
	setAttr ".tgi[3].ni[12].x" -2088.571533203125;
	setAttr ".tgi[3].ni[12].y" 2984.28564453125;
	setAttr ".tgi[3].ni[12].nvs" 18304;
	setAttr ".tgi[3].ni[13].x" -2088.571533203125;
	setAttr ".tgi[3].ni[13].y" 3795.71435546875;
	setAttr ".tgi[3].ni[13].nvs" 18304;
	setAttr ".tgi[3].ni[14].x" -2088.571533203125;
	setAttr ".tgi[3].ni[14].y" 2680;
	setAttr ".tgi[3].ni[14].nvs" 18304;
	setAttr ".tgi[3].ni[15].x" -2088.571533203125;
	setAttr ".tgi[3].ni[15].y" 3491.428466796875;
	setAttr ".tgi[3].ni[15].nvs" 18304;
	setAttr ".tgi[3].ni[16].x" -2088.571533203125;
	setAttr ".tgi[3].ni[16].y" 2172.857177734375;
	setAttr ".tgi[3].ni[16].nvs" 18304;
	setAttr ".tgi[3].ni[17].x" -2088.571533203125;
	setAttr ".tgi[3].ni[17].y" 3288.571533203125;
	setAttr ".tgi[3].ni[17].nvs" 18304;
	setAttr ".tgi[3].ni[18].x" -2088.571533203125;
	setAttr ".tgi[3].ni[18].y" 3694.28564453125;
	setAttr ".tgi[3].ni[18].nvs" 18304;
	setAttr ".tgi[3].ni[19].x" -2088.571533203125;
	setAttr ".tgi[3].ni[19].y" 1970;
	setAttr ".tgi[3].ni[19].nvs" 18304;
	setAttr ".tgi[3].ni[20].x" -2088.571533203125;
	setAttr ".tgi[3].ni[20].y" 3390;
	setAttr ".tgi[3].ni[20].nvs" 18304;
	setAttr ".tgi[3].ni[21].x" -2088.571533203125;
	setAttr ".tgi[3].ni[21].y" 2882.857177734375;
	setAttr ".tgi[3].ni[21].nvs" 18304;
	setAttr ".tgi[3].ni[22].x" -2530;
	setAttr ".tgi[3].ni[22].y" 2010;
	setAttr ".tgi[3].ni[22].nvs" 18304;
	setAttr ".tgi[3].ni[23].x" -3822.857177734375;
	setAttr ".tgi[3].ni[23].y" 4110;
	setAttr ".tgi[3].ni[23].nvs" 18306;
	setAttr ".tgi[4].tn" -type "string" "Untitled_5";
	setAttr ".tgi[4].vl" -type "double2" -4449.4045851013097 -86.904758451477008 ;
	setAttr ".tgi[4].vh" -type "double2" 864.88091801367261 1352.3808986421639 ;
	setAttr -s 26 ".tgi[4].ni";
	setAttr ".tgi[4].ni[0].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[0].y" 1115.7142333984375;
	setAttr ".tgi[4].ni[0].nvs" 18304;
	setAttr ".tgi[4].ni[1].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[1].y" -231.42857360839844;
	setAttr ".tgi[4].ni[1].nvs" 18304;
	setAttr ".tgi[4].ni[2].x" -2000;
	setAttr ".tgi[4].ni[2].y" 1107.142822265625;
	setAttr ".tgi[4].ni[2].nvs" 18304;
	setAttr ".tgi[4].ni[3].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[3].y" 1217.142822265625;
	setAttr ".tgi[4].ni[3].nvs" 18304;
	setAttr ".tgi[4].ni[4].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[4].y" 507.14285278320313;
	setAttr ".tgi[4].ni[4].nvs" 18304;
	setAttr ".tgi[4].ni[5].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[5].y" 1014.2857055664063;
	setAttr ".tgi[4].ni[5].nvs" 18304;
	setAttr ".tgi[4].ni[6].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[6].nvs" 18304;
	setAttr ".tgi[4].ni[7].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[7].y" 405.71429443359375;
	setAttr ".tgi[4].ni[7].nvs" 18304;
	setAttr ".tgi[4].ni[8].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[8].y" 304.28570556640625;
	setAttr ".tgi[4].ni[8].nvs" 18304;
	setAttr ".tgi[4].ni[9].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[9].y" 1927.142822265625;
	setAttr ".tgi[4].ni[9].nvs" 18304;
	setAttr ".tgi[4].ni[10].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[10].y" 912.85711669921875;
	setAttr ".tgi[4].ni[10].nvs" 18304;
	setAttr ".tgi[4].ni[11].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[11].y" 608.5714111328125;
	setAttr ".tgi[4].ni[11].nvs" 18304;
	setAttr ".tgi[4].ni[12].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[12].y" -101.42857360839844;
	setAttr ".tgi[4].ni[12].nvs" 18304;
	setAttr ".tgi[4].ni[13].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[13].y" 1724.2857666015625;
	setAttr ".tgi[4].ni[13].nvs" 18304;
	setAttr ".tgi[4].ni[14].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[14].y" 1521.4285888671875;
	setAttr ".tgi[4].ni[14].nvs" 18304;
	setAttr ".tgi[4].ni[15].x" -2000;
	setAttr ".tgi[4].ni[15].y" 1345.7142333984375;
	setAttr ".tgi[4].ni[15].nvs" 18304;
	setAttr ".tgi[4].ni[16].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[16].y" 1420;
	setAttr ".tgi[4].ni[16].nvs" 18304;
	setAttr ".tgi[4].ni[17].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[17].y" 101.42857360839844;
	setAttr ".tgi[4].ni[17].nvs" 18304;
	setAttr ".tgi[4].ni[18].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[18].y" 1622.857177734375;
	setAttr ".tgi[4].ni[18].nvs" 18304;
	setAttr ".tgi[4].ni[19].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[19].y" 1825.7142333984375;
	setAttr ".tgi[4].ni[19].nvs" 18304;
	setAttr ".tgi[4].ni[20].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[20].y" 202.85714721679688;
	setAttr ".tgi[4].ni[20].nvs" 18304;
	setAttr ".tgi[4].ni[21].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[21].y" 1318.5714111328125;
	setAttr ".tgi[4].ni[21].nvs" 18304;
	setAttr ".tgi[4].ni[22].x" -2000;
	setAttr ".tgi[4].ni[22].y" 847.14288330078125;
	setAttr ".tgi[4].ni[22].nvs" 18304;
	setAttr ".tgi[4].ni[23].x" -1681.4285888671875;
	setAttr ".tgi[4].ni[23].y" 710;
	setAttr ".tgi[4].ni[23].nvs" 18304;
	setAttr ".tgi[4].ni[24].x" -2307.142822265625;
	setAttr ".tgi[4].ni[24].y" 1517.142822265625;
	setAttr ".tgi[4].ni[24].nvs" 18306;
	setAttr ".tgi[4].ni[25].x" -2000;
	setAttr ".tgi[4].ni[25].y" 1005.7142944335938;
	setAttr ".tgi[4].ni[25].nvs" 18304;
	setAttr ".tgi[5].tn" -type "string" "Untitled_6";
	setAttr ".tgi[5].vl" -type "double2" -3256.105307776269 -1102.0511195306362 ;
	setAttr ".tgi[5].vh" -type "double2" -1603.3393966882954 -286.08475586325454 ;
	setAttr -s 6 ".tgi[5].ni";
	setAttr ".tgi[5].ni[0].x" -2372.857177734375;
	setAttr ".tgi[5].ni[0].y" -992.85711669921875;
	setAttr ".tgi[5].ni[0].nvs" 18304;
	setAttr ".tgi[5].ni[1].x" -2372.857177734375;
	setAttr ".tgi[5].ni[1].y" -472.85714721679688;
	setAttr ".tgi[5].ni[1].nvs" 18304;
	setAttr ".tgi[5].ni[2].x" -2680;
	setAttr ".tgi[5].ni[2].y" -342.85714721679688;
	setAttr ".tgi[5].ni[2].nvs" 18304;
	setAttr ".tgi[5].ni[3].x" -2372.857177734375;
	setAttr ".tgi[5].ni[3].y" -342.85714721679688;
	setAttr ".tgi[5].ni[3].nvs" 18304;
	setAttr ".tgi[5].ni[4].x" -2680;
	setAttr ".tgi[5].ni[4].y" -472.85714721679688;
	setAttr ".tgi[5].ni[4].nvs" 18304;
	setAttr ".tgi[5].ni[5].x" -2372.857177734375;
	setAttr ".tgi[5].ni[5].y" -602.85711669921875;
	setAttr ".tgi[5].ni[5].nvs" 18304;
createNode groupId -n "groupId5";
	rename -uid "0722E277-4496-143C-3BF7-4FA31940332F";
	setAttr ".ihi" 0;
createNode groupId -n "groupId7";
	rename -uid "43F359AE-404E-CE1E-F19B-1DB548BD8313";
	setAttr ".ihi" 0;
createNode groupId -n "groupId8";
	rename -uid "B063F544-493E-C138-A8F6-4AB5E8E236AF";
	setAttr ".ihi" 0;
createNode objectSet -n "textureEditorIsolateSelectSet1";
	rename -uid "3DA04118-4DB6-8C71-2116-848FD28C0FE7";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "8504EC06-4CFB-CE2B-3F17-468F8B5BFCA1";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -559.52378729033182 279.57513087408142 ;
	setAttr ".tgi[0].vh" -type "double2" 697.6190198981584 1562.0914626113304 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "9BC2783D-4F2B-4F52-BA37-EA9708B3FC3F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1611.6640790465733 -604.77306002896853 ;
	setAttr ".tgi[0].vh" -type "double2" -11.66412392536326 185.14288420104066 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -1354.7899169921875;
	setAttr ".tgi[0].ni[0].y" 86.974777221679688;
	setAttr ".tgi[0].ni[0].nvs" 18306;
	setAttr ".tgi[0].ni[1].x" -1009.4117431640625;
	setAttr ".tgi[0].ni[1].y" -101.51261138916016;
	setAttr ".tgi[0].ni[1].nvs" 18306;
	setAttr ".tgi[0].ni[2].x" -1385.88232421875;
	setAttr ".tgi[0].ni[2].y" -425.29409790039063;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" -908.5714111328125;
	setAttr ".tgi[0].ni[3].y" 11.428571701049805;
	setAttr ".tgi[0].ni[3].nvs" 18304;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo3";
	rename -uid "3F860585-444D-33F3-96A0-19BB60E6DC7E";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1621.3977943835537 -730.81772198017416 ;
	setAttr ".tgi[0].vh" -type "double2" -21.397839262343563 50.69486114100512 ;
	setAttr -s 4 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -1482.3529052734375;
	setAttr ".tgi[0].ni[0].y" -512.77313232421875;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" -900;
	setAttr ".tgi[0].ni[1].y" -378.57144165039063;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -1152.2689208984375;
	setAttr ".tgi[0].ni[2].y" -14.3697509765625;
	setAttr ".tgi[0].ni[2].nvs" 18306;
	setAttr ".tgi[0].ni[3].x" -1570.5882568359375;
	setAttr ".tgi[0].ni[3].y" -35.126056671142578;
	setAttr ".tgi[0].ni[3].nvs" 18306;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1.25;
	setAttr -av ".unw" 1.25;
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
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
	setAttr ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -cb on ".an";
	setAttr -cb on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
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
	setAttr -k on ".smv";
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
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off ".ctrs" 256;
	setAttr -av -k off ".btrs" 512;
	setAttr -k off ".fbfm";
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
	setAttr -k off ".enpt";
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
connectAttr "Root.s" "body_bind_jnt.is";
connectAttr "body_bind_jnt.s" "upperBody_bind_jnt.is";
connectAttr "upperBody_bind_jnt.s" "chest_bind_jnt.is";
connectAttr "chest_bind_jnt.s" "neck01_bind_jnt.is";
connectAttr "neck01_bind_jnt.s" "neck02_bind_jnt.is";
connectAttr "neck02_bind_jnt.s" "head_bind_jnt.is";
connectAttr "head_bind_jnt.s" "nose_bind_jnt.is";
connectAttr "chest_bind_jnt.s" "upLegFrontLFT_bind_jnt.is";
connectAttr "upLegFrontLFT_bind_jnt.s" "midLegFrontLFT_bind_jnt.is";
connectAttr "midLegFrontLFT_bind_jnt.s" "legPovFrontLFT_tmpJnt.is";
connectAttr "midLegFrontLFT_bind_jnt.s" "ankleFrontLFT_bind_jnt.is";
connectAttr "ankleFrontLFT_bind_jnt.s" "footOutFrontLFT_tmpJnt.is";
connectAttr "ankleFrontLFT_bind_jnt.s" "footInFrontLFT_tmpJnt.is";
connectAttr "ankleFrontLFT_bind_jnt.s" "ballRollFrontLFT_bind_jnt.is";
connectAttr "ballRollFrontLFT_bind_jnt.s" "toeRollFrontLFT_bind_jnt.is";
connectAttr "ankleFrontLFT_bind_jnt.s" "heelRollFrontLFT_tmpJnt.is";
connectAttr "chest_bind_jnt.s" "upLegFrontRGT_bind_jnt.is";
connectAttr "upLegFrontRGT_bind_jnt.s" "midLegFrontRGT_bind_jnt.is";
connectAttr "midLegFrontRGT_bind_jnt.s" "legPovFrontRGT_tmpJnt.is";
connectAttr "midLegFrontRGT_bind_jnt.s" "ankleFrontRGT_bind_jnt.is";
connectAttr "ankleFrontRGT_bind_jnt.s" "footOutFrontRGT_tmpJnt.is";
connectAttr "ankleFrontRGT_bind_jnt.s" "footInFrontRGT_tmpJnt.is";
connectAttr "ankleFrontRGT_bind_jnt.s" "ballRollFrontRGT_bind_jnt.is";
connectAttr "ballRollFrontRGT_bind_jnt.s" "toeRollFrontRGT_bind_jnt.is";
connectAttr "ankleFrontRGT_bind_jnt.s" "heelRollFrontRGT_tmpJnt.is";
connectAttr "body_bind_jnt.s" "lowerBody_bind_jnt.is";
connectAttr "lowerBody_bind_jnt.s" "hip_bind_jnt.is";
connectAttr "hip_bind_jnt.s" "tail01_bind_jnt.is";
connectAttr "tail01_bind_jnt.s" "tail02_bind_jnt.is";
connectAttr "tail02_bind_jnt.s" "tail03_bind_jnt.is";
connectAttr "tail03_bind_jnt.s" "tail04_bind_jnt.is";
connectAttr "hip_bind_jnt.s" "upLegBackLFT_bind_jnt.is";
connectAttr "upLegBackLFT_bind_jnt.s" "midLegBackLFT_bind_jnt.is";
connectAttr "midLegBackLFT_bind_jnt.s" "lowLegBackLFT_bind_jnt.is";
connectAttr "lowLegBackLFT_bind_jnt.s" "ankleBackLFT_bind_jnt.is";
connectAttr "ankleBackLFT_bind_jnt.s" "footOutBackLFT_tmpJnt.is";
connectAttr "ankleBackLFT_bind_jnt.s" "footInBackLFT_tmpJnt.is";
connectAttr "ankleBackLFT_bind_jnt.s" "heelRollBackLFT_tmpJnt.is";
connectAttr "ankleBackLFT_bind_jnt.s" "ballRollBackLFT_bind_jnt.is";
connectAttr "ballRollBackLFT_bind_jnt.s" "toeRollBackLFT_bind_jnt.is";
connectAttr "midLegBackLFT_bind_jnt.s" "legPovBackLFT_tmpJnt.is";
connectAttr "hip_bind_jnt.s" "upLegBackRGT_bind_jnt.is";
connectAttr "upLegBackRGT_bind_jnt.s" "midLegBackRGT_bind_jnt.is";
connectAttr "midLegBackRGT_bind_jnt.s" "lowLegBackRGT_bind_jnt.is";
connectAttr "lowLegBackRGT_bind_jnt.s" "ankleBackRGT_bind_jnt.is";
connectAttr "ankleBackRGT_bind_jnt.s" "footOutBackRGT_tmpJnt.is";
connectAttr "ankleBackRGT_bind_jnt.s" "footInBackRGT_tmpJnt.is";
connectAttr "ankleBackRGT_bind_jnt.s" "heelRollBackRGT_tmpJnt.is";
connectAttr "ankleBackRGT_bind_jnt.s" "ballRollBackRGT_bind_jnt.is";
connectAttr "ballRollBackRGT_bind_jnt.s" "toeRollBackRGT_bind_jnt.is";
connectAttr "midLegBackRGT_bind_jnt.s" "legPovBackRGT_tmpJnt.is";
connectAttr "ear01RGT_bind_jnt.s" "ear02RGT_bind_jnt.is";
connectAttr "ear02RGT_bind_jnt.s" "ear03RGT_bind_jnt.is";
connectAttr "ear03RGT_bind_jnt.s" "ear04RGT_bind_jnt.is";
connectAttr "ear04RGT_bind_jnt.s" "ear05RGT_bind_jnt.is";
connectAttr "ear01LFT_bind_jnt.s" "ear02LFT_bind_jnt.is";
connectAttr "ear02LFT_bind_jnt.s" "ear03LFT_bind_jnt.is";
connectAttr "ear03LFT_bind_jnt.s" "ear04LFT_bind_jnt.is";
connectAttr "ear04LFT_bind_jnt.s" "ear05LFT_bind_jnt.is";
connectAttr "hat_ctrl.gimbal_controller" "hat_Gimbal_ctrlShape.v";
connectAttr "neck_ctrl.gimbal_controller" "neck_Gimbal_ctrlShape.v";
connectAttr "upperChest_ctrl.gimbal_controller" "upperChest_Gimbal_ctrlShape.v";
connectAttr "upperArmLFT_FK_ctrl.gimbal_controller" "upperArmLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "lowerArmLFT_FK_ctrl.gimbal_controller" "lowerArmLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "handLFT_FK_ctrl.gimbal_controller" "handLFT_FK_Gimbal_ctrlShape.v";
connectAttr "shoulderRGT_FK_ctrl.gimbal_controller" "shoulderRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "shoulderLFT_FK_ctrl.gimbal_controller" "shoulderLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "lowerArmRGT_prop_ctrl.gimbal_controller" "lowerArmRGT_prop_Gimbal_ctrlShape.v"
		;
connectAttr "handRGT_prop_ctrl.gimbal_controller" "handRGT_prop_Gimbal_ctrlShape.v"
		;
connectAttr "lowerArmLFT_prop_ctrl.gimbal_controller" "lowerArmLFT_prop_Gimbal_ctrlShape.v"
		;
connectAttr "handLFT_prop_ctrl.gimbal_controller" "handLFT_prop_Gimbal_ctrlShape.v"
		;
connectAttr "upperArmRGT_FK_ctrl.gimbal_controller" "upperArmRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "lowerArmRGT_FK_ctrl.gimbal_controller" "lowerArmRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "handRGT_FK_ctrl.gimbal_controller" "handRGT_FK_Gimbal_ctrlShape.v";
connectAttr "footRGT_FK_ctrl.gimbal_controller" "footRGT_FK_Gimbal_ctrlShape.v";
connectAttr "toesRGT_FK_ctrl.gimbal_controller" "toesRGT_FK_Gimbal_ctrlShape.v";
connectAttr "ballRollLFT_FK_ctrl.gimbal_controller" "ballRollLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "ankleLFT_FK_ctrl.gimbal_controller" "ankleLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "upLegBackLFT_FK_ctrl.gimbal_controller" "upLegBackLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "lowLegBackLFT_FK_ctrl.gimbal_controller" "lowLegBackLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "midLegBackLFT_FK_ctrl.gimbal_controller" "midLegBackLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "midLegBackRGT_FK_ctrl.gimbal_controller" "midLegBackRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "lowLegBackRGT_FK_ctrl.gimbal_controller" "lowLegBackRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "upLegBackRGT_FK_ctrl.gimbal_controller" "upLegBackRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "lowerBody_ctrl.gmbl" "lowerBody_Gimbal_ctrlShape.v";
connectAttr "upperBody_ctrl.gmbl" "upperBody_Gimbal_ctrlShape.v";
connectAttr "chest_ctrl.gmbl" "chest_Gimbal_ctrlShape.v";
connectAttr "body_ctrl.gmbl" "body_Gimbal_ctrlShape.v";
connectAttr "hip_ctrl.gimbal_controller" "hip_Gimbal_ctrlShape.v";
connectAttr "cog_ctrl.gimbal_controller" "cog_Gimbal_ctrlShape.v";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "lowLegBackLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[0].dn"
		;
connectAttr "footRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[1].dn"
		;
connectAttr "upLegBackRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[3].dn"
		;
connectAttr "ankleLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[5].dn"
		;
connectAttr "ballRollLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[6].dn"
		;
connectAttr "lowLegBackRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[7].dn"
		;
connectAttr "upLegBackLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[8].dn"
		;
connectAttr "legPovBackLFT_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[9].dn"
		;
connectAttr "placement_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[10].dn"
		;
connectAttr "legPovBackRGT_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[11].dn"
		;
connectAttr "lowLegBackRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[12].dn"
		;
connectAttr "lowerArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[0].dn"
		;
connectAttr "handRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[1].dn"
		;
connectAttr "upperArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[2].dn"
		;
connectAttr "armRGT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[5].dn"
		;
connectAttr "lowerArmRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[6].dn"
		;
connectAttr "handLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[7].dn"
		;
connectAttr "handLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[8].dn"
		;
connectAttr "handRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[9].dn"
		;
connectAttr "upperArmRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[10].dn"
		;
connectAttr "armLFT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[11].dn"
		;
connectAttr "placement_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[0].dn"
		;
connectAttr "ballRollLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[2].dn"
		;
connectAttr "lowerArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[3].dn"
		;
connectAttr "lowLegBackLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[4].dn"
		;
connectAttr "legPovBackRGT_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[5].dn"
		;
connectAttr "lowLegBackRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[6].dn"
		;
connectAttr "lowerArmRGT_prop_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[8].dn"
		;
connectAttr "handRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[9].dn"
		;
connectAttr "handRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[10].dn"
		;
connectAttr "handLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[12].dn"
		;
connectAttr "ankleLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[14].dn"
		;
connectAttr "handLFT_prop_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[15].dn"
		;
connectAttr "lowLegBackRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[16].dn"
		;
connectAttr "upLegBackRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[17].dn"
		;
connectAttr "handRGT_prop_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[18].dn"
		;
connectAttr "handLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[20].dn"
		;
connectAttr "placement_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[23].dn"
		;
connectAttr "lowerArmRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[0].dn"
		;
connectAttr "placement_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[1].dn"
		;
connectAttr "ballRollLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[3].dn"
		;
connectAttr "lowerArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[4].dn"
		;
connectAttr "lowLegBackLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[5].dn"
		;
connectAttr "legPovBackRGT_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[6].dn"
		;
connectAttr "lowLegBackRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[7].dn"
		;
connectAttr "handRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[8].dn"
		;
connectAttr "handRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[9].dn"
		;
connectAttr "handLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[10].dn"
		;
connectAttr "upperArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[11].dn"
		;
connectAttr "ankleLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[12].dn"
		;
connectAttr "lowLegBackLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[13].dn"
		;
connectAttr "lowLegBackRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[14].dn"
		;
connectAttr "upLegBackRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[16].dn"
		;
connectAttr "upperArmRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[17].dn"
		;
connectAttr "armLFT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[18].dn"
		;
connectAttr "footRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[19].dn"
		;
connectAttr "upLegBackLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[20].dn"
		;
connectAttr "handLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[21].dn"
		;
connectAttr "legPovBackLFT_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[23].dn"
		;
connectAttr "placement_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[24].dn"
		;
connectAttr "hat_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "hat_Gimbal_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "hat_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "hat_Gimbal_ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "midLegBackRGT_FK_Gimbal_ctrl.msg" "MayaNodeEditorSavedTabsInfo3.tgi[0].ni[0].dn"
		;
connectAttr "midLegBackRGT_FK_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo3.tgi[0].ni[1].dn"
		;
connectAttr "midLegBackRGT_FK_Gimbal_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo3.tgi[0].ni[2].dn"
		;
connectAttr "midLegBackRGT_FK_ctrl.msg" "MayaNodeEditorSavedTabsInfo3.tgi[0].ni[3].dn"
		;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of quadruped_tempJoint.ma
