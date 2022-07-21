//Maya ASCII 2018 scene
//Name: PH_tmpRig.ma
//Last modified: Tue, Mar 31, 2020 01:45:14 PM
//Codeset: 1252
requires maya "2018";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201706261615-f9658c4cfc";
fileInfo "osv" "Microsoft Windows 8 Business Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "2D6D14BE-4B29-5D1E-1AD4-D8BF00A3B904";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 29.282757607837457 59.148800333751922 96.160081317494075 ;
	setAttr ".r" -type "double3" -20.73835272410415 15.399999999999878 1.2371265336508069e-15 ;
	setAttr ".rp" -type "double3" 1.7763568394002505e-15 1.4210854715202004e-14 0 ;
	setAttr ".rpt" -type "double3" -6.1675713290967487e-15 -7.6392622767091535e-16 -2.1301843335633544e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "C4371FD8-44BB-7D89-A3E7-7CA2A4B29179";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 111.89967636707189;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "8CACD926-443F-73B0-68D1-D4BDACFFF6CA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -0.23494417861397415 1000.1004780318015 -0.948543681654066 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "4CFA1815-4438-1078-90BF-9A92EAE5EB70";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 998.81860235870181;
	setAttr ".ow" 4.0844317194600839;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" -0.23494417861397415 1.2818756730996035 -0.94854368165428782 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "EC2024EB-4F23-DBDF-9D3E-468A205BD4E1";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 7.0393312990369061 42.823672995478482 1010.0579764380777 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "52CE32F1-45C6-27ED-1469-62996C141BD3";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1033.8685004248941;
	setAttr ".ow" 48.518894196818032;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 11.979297637939453 39.147418975830078 -23.810523986816406 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "5909DEBA-411B-F308-C1F4-6E9E061ADA2C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1019047084848 1.4772921242660217 0.032289173302723274 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "27819C82-4729-DD9E-D8BA-7ABFC1A4BE50";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.2171739597709;
	setAttr ".ow" 0.18880106349664882;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" -0.1152692512861364 1.5590317636892939 0.023889414052405925 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode joint -n "Root";
	rename -uid "D23B19DC-4D53-AF8B-0207-62A0911E5051";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".ds" 2;
createNode joint -n "hips_bind_jnt" -p "Root";
	rename -uid "546DB058-461D-A0FC-8060-058E4EC8962C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -7.3033888267402698e-08 31.400761937092575 -0.21280631102242031 ;
	setAttr ".r" -type "double3" 7.9513867036587959e-16 2.3696978997167331e-23 -7.5811819526093913e-22 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.1020197208586096 0 2.5027930092184574e-06 ;
	setAttr ".bps" -type "matrix" 0.999999999999999 4.3681978506758875e-08 -1.0339757656912844e-25 0
		 -4.3652584966257738e-08 0.99932710143848846 -0.036678935788093427 0 -1.6022084847462857e-09 0.036678935788093385 0.99932710143848946 0
		 -2.2925493639760144e-09 0.98567662923369526 -0.0066800355911254784 1;
	setAttr ".typ" 2;
createNode joint -n "spine_bind_jnt" -p "hips_bind_jnt";
	rename -uid "0EC8477B-433A-4103-90E8-B6B8686B3F88";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.20399801014066e-10 4.0961312911968406 -5.3290705182007514e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -7.8214511510486222 0 -7.366832548334181e-06 ;
	setAttr ".bps" -type "matrix" 0.99999999999999645 -8.4806986646923665e-08 4.7160118999740459e-09 0
		 8.4350896260493619e-08 0.9850388137788616 -0.17233262996056778 0 9.9695562801776755e-09 0.17233262996056756 0.98503881377886537 0
		 -7.9091098764356313e-09 1.1141685457823336 -0.011396155818018811 1;
	setAttr ".typ" 6;
createNode joint -n "chest_bind_jnt" -p "spine_bind_jnt";
	rename -uid "79A64829-4546-FDEC-BCE9-2B8CDC3B862D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.4545009617016249e-09 2.9684415206549133 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 2.5851625346526181 -2.3696978997167319e-23 4.9321179788118586e-06 ;
	setAttr ".bps" -type "matrix" 1 -1.3173131271227588e-11 -1.0118673478036657e-08 0
		 -1.2793703381278857e-09 0.99180926465271968 -0.1277277673375346 0 1.0037476676158627e-08 0.12772776733753458 0.99180926465271968 0
		 1.2192575637080415e-10 1.2059544760917069 -0.027454112664318964 1;
	setAttr ".typ" 6;
createNode joint -n "upperChest_bind_jnt" -p "chest_bind_jnt";
	rename -uid "90D71345-463E-7317-1967-89B47C80063C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.4075134204749769e-10 3.88955559338185 6.2172489379008766e-15 ;
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999978 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -1.7104208681928166 7.7294889757915758e-06 0.00051780730074336946 ;
	setAttr ".bps" -type "matrix" 0.99999999995914035 8.946174699022918e-06 -1.2982510601657979e-06 0
		 -9.039020688050583e-06 0.98755493818287321 -0.15727442255152937 0 -1.2491021436604778e-07 0.15727442255683807 0.98755493822338669 0
		 -4.4973919466356928e-11 1.3270484180849538 -0.043048904324501619 1;
	setAttr ".typ" 6;
createNode joint -n "shoulderLFT_bind_jnt" -p "upperChest_bind_jnt";
	rename -uid "E7917A9C-4023-E991-9AF0-E59BDAF878A3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.0065404562017091 4.8484121582706337 0.20824867837233274 ;
	setAttr ".r" -type "double3" 4.7708320222646996e-15 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 9.0487292054473887 7.1568281012489354e-06 -0.00051789773636379266 ;
	setAttr ".bps" -type "matrix" 1 -2.6999175193730823e-21 3.4410713482205951e-22 0
		 2.3392667722999623e-21 1 2.7755575615628914e-17 0 -5.2939559203393771e-22 -5.5511151231257827e-17 1 0
		 0.094374571040978295 1.4783760071826626 -0.060529427389821311 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
createNode joint -n "upperArmLFT_bind_jnt" -p "shoulderLFT_bind_jnt";
	rename -uid "EC32A558-49C4-6597-68BF-FFADD5E75FB7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.6788849653721831 -1.5799325400410424 -1.4825520293677883 ;
	setAttr ".r" -type "double3" -7.9513867036587899e-16 -8.6209107383792118e-35 -1.2424041724466859e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -5.8156100842384273 0 -135.34136554001958 ;
	setAttr ".bps" -type "matrix" -0.71130711484803544 -0.70288134728883234 -1.9509121149343582e-17 0
		 0.69926371496426432 -0.7076461162722516 -0.10132734605808799 0 0.071221101514510624 -0.072074862179787036 0.99485313938330844 0
		 0.17846534272552578 1.4287815870343819 -0.10706705249262538 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "lowerArmLFT_bind_jnt" -p "upperArmLFT_bind_jnt";
	rename -uid "ECDA88B6-44DF-5830-7753-B4A45BA4C1B3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 1.4210854715202004e-14 9.0007754724599174 1.7763568394002505e-15 ;
	setAttr ".r" -type "double3" -2.914287084275877e-15 -2.1981099156554027e-11 8.4005002819461187e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 7.9710219023899196 -0.0871604080287042 0.85579165049282158 ;
	setAttr ".bps" -type "matrix" -0.70067453505519717 -0.71348104104116439 -3.8393008390535943e-13 0
		 0.71297593946350124 -0.70017849971198198 0.037621513622082187 0 -0.026842236704896355 0.026360436564951462 0.99929206026705897 0
		 0.37603270172136105 1.2288458956726285 -0.1356957024945443 1;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
createNode joint -n "handLFT_bind_jnt" -p "lowerArmLFT_bind_jnt";
	rename -uid "170B3493-41A8-D59A-E6C3-D890280779C2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -1.4210854715202004e-14 8.1628253843265171 3.1086244689504383e-15 ;
	setAttr ".r" -type "double3" 1.7839865931587934e-13 -2.1793657639056979e-11 -2.977328418955583e-12 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -9.9199297159977196 0.097700791689205355 -0.47770140908522479 ;
	setAttr ".bps" -type "matrix" -0.70654772468504623 -0.70766251971204674 -0.0020176563585532943 0
		 0.70136943397129015 -0.69987938507718517 -0.13509168529104024 0 0.094187206313683075 -0.096863845364399973 0.9908310479733895 0
		 0.55872054701291063 1.0494371746320499 -0.12605583545303281 1;
	setAttr ".sd" 1;
	setAttr ".typ" 8;
createNode joint -n "thumb01LFT_bind_jnt" -p "handLFT_bind_jnt";
	rename -uid "83F25EC1-4EAC-0C2A-D9E3-B18EF5D20702";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.73141604159112461 0.42837937742218202 1.1133215878830285 ;
	setAttr ".r" -type "double3" -2.3854160110976374e-14 -2.0673605429512861e-14 -9.5416640443905456e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 84.172401040981711 34.777634815723282 60.461817651065637 ;
	setAttr ".bps" -type "matrix" 0.16137725013615598 -0.73145486855443087 -0.66251879853066264 0
		 0.32308970033709838 -0.59516592983149352 0.73579247176353879 0 -0.93250760247548481 -0.33279316584905128 0.14027929316042789 0
		 0.55522155872465173 1.0203933723147014 -0.093291754995556087 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb02LFT_bind_jnt" -p "thumb01LFT_bind_jnt";
	rename -uid "1E3CE97A-42AD-BF82-3EA4-0CBD61710D29";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 7.1054273576010019e-15 0.80985095183309141 4.6185277824406512e-14 ;
	setAttr ".r" -type "double3" 1.0038625713369221e-14 -2.5121412366871997e-14 2.1530864308501071e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 2.6494155225342428 2.8216501305138544 -7.6410594753925123 ;
	setAttr ".bps" -type "matrix" 0.1627470260179093 -0.62865722038361593 -0.76046269124913124 0
		 0.29852711301821566 -0.70323992013502745 0.6452404028898765 0 -0.94042276041966133 -0.33202968841359076 0.073221019500129159 0
		 0.5634349494514973 1.0052634244274341 -0.074586884310540419 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb03LFT_bind_jnt" -p "thumb02LFT_bind_jnt";
	rename -uid "E3F4035F-4ACE-B1EA-A5C8-30966055BCAD";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 5.3290705182007514e-15 0.9189507607718852 -2.1316282072803006e-14 ;
	setAttr ".r" -type "double3" 7.1873081376040803e-15 -5.5162745256632876e-15 1.4039167148647554e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -4.245283464838959 -1.3647452562242535 3.7194892236682722 ;
	setAttr ".bps" -type "matrix" 0.15932053844130956 -0.68067049716867067 -0.71505569035909766 0
		 0.35646907139074174 -0.63577748564254377 0.68462894321805268 0 -0.92062303206719398 -0.36397068980097835 0.14134556870735848 0
		 0.5720462807069755 0.98497772292738628 -0.055974240411881364 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "index01LFT_bind_jnt" -p "handLFT_bind_jnt";
	rename -uid "7F80D0D0-4B1D-ADC6-9A9A-ABB7073FF51E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.29014614751170598 2.6200783703395327 1.2956152878955693 ;
	setAttr ".r" -type "double3" -4.6590156466751451e-15 3.9597905784220773e-13 -2.1120870931593681e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 12.093016137008592 1.8069651895962151 -14.233000025178573 ;
	setAttr ".bps" -type "matrix" -0.85984578673077472 -0.51055383951287159 6.9458327978111356e-15 0
		 0.50895177870333264 -0.85714768688202314 0.079157626464615105 0 -0.040414230118228978 0.068063351603211267 0.99686211191542851 0
		 0.61380005003251747 0.98149108969298737 -0.096888060271310125 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index02LFT_bind_jnt" -p "index01LFT_bind_jnt";
	rename -uid "5278B7F7-4BE8-8D79-26BF-7BBC16BF18ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -1.4210854715202004e-14 1.1203331132569616 -1.3322676295501878e-15 ;
	setAttr ".r" -type "double3" 5.0342217067539729e-14 -5.9237830942257995e-14 3.5346398706107963e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.965433721454025 0.67402478521147624 8.5200070397695722 ;
	setAttr ".bps" -type "matrix" -0.77442402293795143 -0.63266692081742293 -1.0182826803983858e-15 0
		 0.63244298026061196 -0.77414990563989439 0.026604516849927366 0 -0.016831797755279567 0.020603176967240573 0.99964603719675782 0
		 0.63169860962359892 0.95134735192847464 -0.094104284767125776 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index03LFT_bind_jnt" -p "index02LFT_bind_jnt";
	rename -uid "C5629980-4B26-9ABB-5DAF-F79D2D7B2A34";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.8421709430404007e-14 0.55099525098453306 4.4408920985006262e-16 ;
	setAttr ".r" -type "double3" -5.8955353852991151e-15 1.7972261567414184e-12 -1.2318815914830195e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 2.6420620992190598 -0.013341275258029223 -0.5012954533172983 ;
	setAttr ".bps" -type "matrix" -0.77993161543518652 -0.62586474197278485 3.1473277760027396e-14 0
		 0.62421065355067462 -0.77787034601287497 0.072655246112376864 0 -0.045472356861067431 0.056666123470286739 0.99735711518610515 0
		 0.64263725404957706 0.93795776454352275 -0.093644136802756905 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "middle01LFT_bind_jnt" -p "handLFT_bind_jnt";
	rename -uid "FCB84C76-4570-5ECC-E224-099C9A04605A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.3980509220138444 2.5561864900366515 0.41063905255891076 ;
	setAttr ".r" -type "double3" -6.6592863643142385e-15 -1.5902773407317576e-15 1.2945851476894471e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 7.1260549836948979 -1.4705288020426792 -18.795155678898002 ;
	setAttr ".bps" -type "matrix" -0.89213148785722352 -0.44677580274361822 0.067028281019673147 0
		 0.4474891390544406 -0.89427646832407759 -0.0048029813794138593 0 0.0620876702894574 0.025709536841625566 0.99773951556176055 0
		 0.607383729494957 0.98318862996598999 -0.12414884066837194 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle02LFT_bind_jnt" -p "middle01LFT_bind_jnt";
	rename -uid "F3C07CB3-40B9-0E29-E998-EF83E256A1A5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 3.907985046680551e-14 1.3852834025652747 4.4408920985006262e-16 ;
	setAttr ".r" -type "double3" -4.8860455966245105e-15 -2.4917968683633847e-15 4.7746538709679383e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0.12061910514726989 -0.027920839249272047 3.9324903012787011 ;
	setAttr ".bps" -type "matrix" -0.85931138466729473 -0.50704170314619135 0.067027273939688742 0
		 0.50774930732865797 -0.86147404127536631 -0.0072881490075927969 0 0.061437652042087794 0.027770262499628984 0.99772452482248675 0
		 0.62684250031077016 0.94430160607114422 -0.12435769515385092 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle03LFT_bind_jnt" -p "middle02LFT_bind_jnt";
	rename -uid "EBA76618-4785-46B5-08E9-3887BAF3BCF2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.2632564145606011e-14 0.63987722844060357 2.2204460492503131e-15 ;
	setAttr ".r" -type "double3" -8.1843374859925452e-15 -1.7642139248742954e-15 -1.4352874202190342e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.5843569614906592 -0.097633733441022053 8.5477923470692545 ;
	setAttr ".bps" -type "matrix" -0.77419155398932871 -0.62940598148263449 0.066899538155879582 0
		 0.62636219646643376 -0.77705190229193588 -0.06213485320034625 0 0.091092461649321541 -0.0062009368941682193 0.99582313279633217 0
		 0.637041093479357 0.92699813929048458 -0.12450408406193531 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "ring01LFT_bind_jnt" -p "handLFT_bind_jnt";
	rename -uid "BAEAC734-4F83-09A6-DE70-7999F7DCFEE2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.51571608418731074 2.5495257494891899 -0.40086610285405389 ;
	setAttr ".r" -type "double3" -8.0507790374545269e-15 -4.2738703532166017e-15 -9.255911084727813e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 1.7540683161680906 -3.3345328845401276 -19.313753301290003 ;
	setAttr ".bps" -type "matrix" -0.89175580717150216 -0.44125301229117236 0.10033623233841904 0
		 0.43249087604286246 -0.89630811262255017 -0.097894889481930522 0 0.13312859390671938 -0.043903831165040985 0.9901258662884489 0
		 0.60222816638646748 0.98318862995779244 -0.14936780434170979 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "ring02LFT_bind_jnt" -p "ring01LFT_bind_jnt";
	rename -uid "E8491E71-4FAD-DFD7-225B-0399570ACA76";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.7763568394002505e-14 1.2995727447960697 5.3290705182007514e-15 ;
	setAttr ".r" -type "double3" -8.9701581250650741e-15 -4.0253895187272635e-15 -1.3914926731402882e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 2.2686282810612011 -1.4970626300708871 13.524765769490752 ;
	setAttr ".bps" -type "matrix" -0.76214220299620961 -0.63956129606931977 0.10050179591537936 0
		 0.63461556086959403 -0.76873332538860928 -0.079449130512181554 0 0.12807166866350833 0.0032284682285524322 0.99175966074379218 0
		 0.61987114133706878 0.94662475669482649 -0.1533613153695596 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "ring03LFT_bind_jnt" -p "ring02LFT_bind_jnt";
	rename -uid "9DE6ACFE-4941-364D-CB45-C8AB3892B4AE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -7.1054273576010019e-15 0.62158940740042645 -2.2204460492503131e-15 ;
	setAttr ".r" -type "double3" -1.6850106588808186e-15 -5.6715750472191224e-15 7.4350124694856387e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.5211847300896082 -0.15476661047207893 2.2345630547344104 ;
	setAttr ".bps" -type "matrix" -0.73646998052226353 -0.66903716873650365 0.10000617300237107 0
		 0.65748552927677428 -0.74271398992862814 -0.1268412707124065 0 0.15913750840445257 -0.027662176583576677 0.98686881468890375 0
		 0.63225364870025635 0.93162536706607468 -0.15491151285009072 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "pinky01LFT_bind_jnt" -p "handLFT_bind_jnt";
	rename -uid "40D11B60-4D8D-A698-93EF-1BAA7757EE42";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0.67819019846618289 2.531018449989503 -1.0351027140324094 ;
	setAttr ".r" -type "double3" -1.5107634736951701e-14 -9.5416640443905487e-15 -5.2677936911739478e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -3.9652092481270693 -11.202288567747154 -24.747852527312144 ;
	setAttr ".bps" -type "matrix" -0.89915146136844115 -0.36183821282293732 0.24617017946960879 0
		 0.32140556496697326 -0.92774385287173577 -0.18970979486301698 0 0.29702712389150165 -0.091457373676538167 0.95047905630420526 0
		 0.59634208869939209 0.98191452106171684 -0.16902589308320845 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "pinky02LFT_bind_jnt" -p "pinky01LFT_bind_jnt";
	rename -uid "C4709324-4877-7CF4-58F6-018AB742190E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 3.5527136788005009e-14 1.0112418154289458 4.4408920985006262e-15 ;
	setAttr ".r" -type "double3" -1.5505204072134644e-14 -5.1684013573782151e-15 -2.6090487621380409e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.7539460991008133 -5.1530792180715093 22.842899960420628 ;
	setAttr ".bps" -type "matrix" -0.67433910621176096 -0.69902673360833312 0.23796721525115141 0
		 0.62725810396131698 -0.71230733996321816 -0.31490558021314619 0 0.3896332132254347 -0.063086283258637244 0.91880687852030907 0
		 0.60654449664186771 0.9524650581873112 -0.17504786945463421 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "pinky03LFT_bind_jnt" -p "pinky02LFT_bind_jnt";
	rename -uid "9D888DEB-4542-04C8-4A41-35A9C168EC6E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.1054273576010019e-15 0.38079617301105806 -4.9960036108132044e-15 ;
	setAttr ".r" -type "double3" -1.2026472389283922e-14 -1.3977046940025221e-14 -5.5970307968723211e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 1.4708903178473958 2.0013117996087941 -6.9584720828762547 ;
	setAttr ".bps" -type "matrix" -0.75851660665725018 -0.6050081527520712 0.24211090956149983 0
		 0.55009074603179875 -0.79364981607129681 -0.25984637880904982 0 0.34936045648491687 -0.063914822643292082 0.93480595146325807 0
		 0.61404228416770845 0.94395065390235589 -0.17881202190835113 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "handLFT_prop_jnt" -p "handLFT_bind_jnt";
	rename -uid "0BBA2B51-4C65-7899-86DF-D489E185FD5D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.0339313567084361 2.5477173890242479 0.27040484702505729 ;
	setAttr ".r" -type "double3" -6.361109362927032e-15 -1.590277340731758e-15 2.2363275104040355e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.5835049064630917 -5.4045404030608175 135.21073176310816 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 9.0147846190488966e-10 -1.3877787807814457e-17 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 1.3877787807814457e-17 1.1076510713196976e-15 0.99999999999999989 0
		 79.702359949404638 138.65563836087185 -4.351286576303516 1;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
createNode joint -n "lowerArmLFT_prop_jnt" -p "lowerArmLFT_bind_jnt";
	rename -uid "84AE2AAE-4478-CBE5-C47A-1D9BDDBD6885";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 7.8586906226973952e-07 1.2966988656160083e-06 -1.9488631153308233e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" 1.5110613202795689 1.5381316190278416 134.50143208808024 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 9.0147846190488966e-10 -1.3877787807814457e-17 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 1.3877787807814457e-17 1.1076510713196976e-15 0.99999999999999989 0
		 79.702359949404638 138.65563836087185 -4.351286576303516 1;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
createNode joint -n "upperArmArmorLFT_bind_jnt" -p "shoulderLFT_bind_jnt";
	rename -uid "059083C2-43C7-7FCD-F0BA-77A26903FC5B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.6788849653721831 -1.5799325400410709 -1.4825520293677883 ;
	setAttr ".r" -type "double3" -1.5902773407317584e-15 1.2051320472732857e-15 4.4648899947302623e-18 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -0.72880333638483596 0.24622404707936724 -135.47830756280553 ;
	setAttr ".bps" -type "matrix" -0.71297844704362678 -0.70117277923743326 -0.004297407091800899 0
		 0.70116150253662068 -0.71288902377667185 -0.012719557356000015 0 0.0058550330355315785 -0.012081946664261902 0.99990986851463504 0
		 0.17846534272552572 1.4287815870343814 -0.10706705249262534 1;
createNode joint -n "shoulderRGT_bind_jnt" -p "upperChest_bind_jnt";
	rename -uid "4E062801-42F3-9DCA-425A-CBAA3EC26621";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -3.0064536705331975 4.8485919890442162 0.20827029637402372 ;
	setAttr ".r" -type "double3" -2.5444437452217249e-14 -3.6398559739649089e-20 -2.9118847791719209e-19 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -170.95127079455261 7.1568281012489354e-06 -0.00051789773636379266 ;
	setAttr ".bps" -type "matrix" 1 -2.6999175193730823e-21 3.4410713482205951e-22 0
		 -2.3525016621008107e-21 -1 8.3266726846886741e-17 0 7.1468404924581591e-22 -5.5511151231257827e-17 -0.99999999999999989 0
		 -0.094374599940238627 1.4783800000000002 -0.060529399999999879 1;
	setAttr ".sd" 1;
	setAttr ".typ" 9;
createNode joint -n "upperArmRGT_bind_jnt" -p "shoulderRGT_bind_jnt";
	rename -uid "5E0C503E-493C-0435-A00C-C6BB5145391B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.6788731245943405 1.5801102977257528 1.4825512296661922 ;
	setAttr ".r" -type "double3" 1.033680271475643e-14 3.975693351829396e-16 3.5862988671657541e-32 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -5.8156100842383394 0 -135.34136554001958 ;
	setAttr ".bps" -type "matrix" -0.71130711484803544 0.70288134728883234 -5.8526873916324205e-17 0
		 0.69926371496426454 0.7076461162722516 0.10132734605808637 0 0.071221101514509555 0.072074862179785842 -0.99485313938330844 0
		 -0.17846499994023846 1.4287800000000008 -0.10706699999999988 1;
	setAttr ".sd" 1;
	setAttr ".typ" 10;
createNode joint -n "lowerArmRGT_bind_jnt" -p "upperArmRGT_bind_jnt";
	rename -uid "056181F2-4A4A-1FD8-4450-D4A448C81793";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0.00014196471789773568 -9.00066257820761 2.2706050587295579e-05 ;
	setAttr ".r" -type "double3" -1.1011146698199664e-14 1.6002165741113319e-14 -5.1008456305014276e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 7.971021902389805 -0.08716040802868634 0.85579165049273631 ;
	setAttr ".bps" -type "matrix" -0.70067453505519817 0.71348104104116328 3.8398711293963217e-13 0
		 0.71297593946350024 0.70017849971198276 -0.037621513622081881 0 -0.026842236704896147 -0.026360436564951212 -0.99929206026705897 0
		 -0.37603299994023875 1.2288500000000007 -0.13569599999999979 1;
	setAttr ".sd" 1;
	setAttr ".typ" 11;
createNode joint -n "handRGT_bind_jnt" -p "lowerArmRGT_bind_jnt";
	rename -uid "071E140A-4F5F-1C28-5EA1-D9AF2F9D6DE8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -2.5616678961171147e-05 -8.1628575856170436 -3.0263480557124467e-06 ;
	setAttr ".r" -type "double3" 1.9904353414890749e-13 -2.1779109086197636e-11 -2.9955746772331823e-12 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -9.9199297159977746 0.09770079168919453 -0.47770140908509562 ;
	setAttr ".bps" -type "matrix" -0.70654772468504534 0.70766251971204752 0.0020176563585525584 0
		 0.70136943397129103 0.69987938507718406 0.13509168529104124 0 0.094187206313684393 0.0968638453644 -0.99083104797338928 0
		 -0.55872099994023883 1.0494399999999997 -0.12605599999999983 1;
	setAttr ".sd" 1;
	setAttr ".typ" 8;
createNode joint -n "thumb01RGT_bind_jnt" -p "handRGT_bind_jnt";
	rename -uid "0EC83AAE-4E1A-1D8D-2C0C-50A5FF1C00C9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.73155601838343642 -0.42851678543404148 -1.1133444508914545 ;
	setAttr ".r" -type "double3" 3.1805546814635219e-15 2.8624992133171654e-14 1.9083328088781101e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 84.172401040981768 34.777634815723211 60.461817651065651 ;
	setAttr ".bps" -type "matrix" 0.16137725013615631 0.73145486855443087 0.66251879853066231 0
		 0.323089700337098 0.5951659298314933 -0.73579247176353879 0 -0.9325076024754847 0.33279316584905105 -0.14027929316042764 0
		 -0.55522199994023802 1.0203899999999999 -0.093291799999999758 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb02RGT_bind_jnt" -p "thumb01RGT_bind_jnt";
	rename -uid "7E4E119B-4BBE-3317-1EB4-3A918AE1761D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.4131168200037791e-06 -0.80984860542181103 -1.2290798775183021e-05 ;
	setAttr ".r" -type "double3" -2.015179567708525e-14 1.7194873746662136e-14 -8.8583417495448761e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 2.649415522533896 2.8216501305138215 -7.641059475392499 ;
	setAttr ".bps" -type "matrix" 0.16274702601790922 0.62865722038361627 0.7604626912491308 0
		 0.29852711301822099 0.70323992013502501 -0.64524040288987627 0 -0.94042276041965944 0.33202968841359448 -0.07322101950013328 0
		 -0.56343499994023849 1.0052600000000005 -0.074586899999999956 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "thumb03RGT_bind_jnt" -p "thumb02RGT_bind_jnt";
	rename -uid "D0A7457D-48BE-AC04-1502-F8A0E579B684";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 7.7207137595181052e-05 -0.91886583836555147 2.9097601121463867e-05 ;
	setAttr ".r" -type "double3" -1.8959087671536433e-14 1.5207027070747436e-14 -2.3102505586646135e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -4.2452834648382956 -1.3647452562242564 3.7194892236681918 ;
	setAttr ".bps" -type "matrix" 0.1593205384413095 0.68067049716867001 0.71505569035909822 0
		 0.35646907139073669 0.63577748564254633 -0.68462894321805279 0 -0.92062303206719565 0.36397068980097463 -0.14134556870735457 0
		 -0.57204599994023875 0.98497800000000046 -0.055974199999999696 1;
	setAttr ".sd" 1;
	setAttr ".typ" 14;
createNode joint -n "index01RGT_bind_jnt" -p "handRGT_bind_jnt";
	rename -uid "92DAEE26-41EC-2410-849C-329C547ABA2B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.29022317900013661 -2.6201315884087037 -1.2956267137440154 ;
	setAttr ".r" -type "double3" -1.8344097606175318e-14 -4.5720473546037973e-15 4.5198663793610435e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 12.093016137008586 1.8069651895962473 -14.233000025178637 ;
	setAttr ".bps" -type "matrix" -0.85984578673077494 0.51055383951287137 -7.0776717819853729e-15 0
		 0.50895177870333252 0.85714768688202292 -0.079157626464613773 0 -0.040414230118228173 -0.068063351603210184 -0.99686211191542851 0
		 -0.61379999994023815 0.98149099999999989 -0.09688809999999981 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index02RGT_bind_jnt" -p "index01RGT_bind_jnt";
	rename -uid "496540B1-42EF-0E33-B1CA-52A5B2D24991";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 7.7985585136275404e-06 -1.1203474763472805 3.5770585271599487e-07 ;
	setAttr ".r" -type "double3" 3.2078875732573365e-14 4.181932444455546e-13 -2.0813375898912997e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.9654337214539566 0.6740247852114587 8.5200070397695491 ;
	setAttr ".bps" -type "matrix" -0.77442402293795198 0.63266692081742237 8.1011586328116891e-16 0
		 0.63244298026061152 0.7741499056398945 -0.026604516849927241 0 -0.016831797755279307 -0.020603176967240629 -0.99964603719675771 0
		 -0.63169899994023826 0.95134700000000016 -0.09410429999999971 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "index03RGT_bind_jnt" -p "index02RGT_bind_jnt";
	rename -uid "6D8F1DB2-4AD2-A825-29D2-918A75DEB3E4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -4.0598617445652962e-06 -0.55096782516593201 -2.3881983368667647e-06 ;
	setAttr ".r" -type "double3" -1.5314063102088516e-14 -4.117016826445206e-14 3.6950361905302096e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 2.6420620992195714 -0.013341275258028562 -0.50129545331707248 ;
	setAttr ".bps" -type "matrix" -0.77993161543518452 0.6258647419727873 -3.1775688850987915e-14 0
		 0.62421065355067684 0.77787034601287208 -0.072655246112385649 0 -0.045472356861072878 -0.056666123470293622 -0.99735711518610437 0
		 -0.64263699994023926 0.93795800000000085 -0.0936440999999998 1;
	setAttr ".sd" 1;
	setAttr ".typ" 19;
createNode joint -n "middle01RGT_bind_jnt" -p "handRGT_bind_jnt";
	rename -uid "F406A401-458F-FB5C-4AC3-EB9CE1F4278A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.39811038225104056 -2.5562371346656159 -0.41064624630199109 ;
	setAttr ".r" -type "double3" 2.0872390097104318e-15 -1.033680271475643e-14 1.0187714214062828e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 7.1260549836947593 -1.470528802042645 -18.795155678898013 ;
	setAttr ".bps" -type "matrix" -0.89213148785722329 0.44677580274361867 -0.067028281019673189 0
		 0.44748913905444093 0.89427646832407692 0.0048029813794173842 0 0.062087670289459031 -0.025709536841622443 -0.99773951556176055 0
		 -0.60738399994023873 0.98318900000000009 -0.1241489999999998 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle02RGT_bind_jnt" -p "middle01RGT_bind_jnt";
	rename -uid "25164B3C-452C-1437-09F2-F481B2408154";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 7.1643875045879213e-06 -1.3852860112681356 4.1523052720648934e-06 ;
	setAttr ".r" -type "double3" 2.577464518566623e-14 -1.2330861411533363e-14 1.1933798622973462e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0.12061910514531438 -0.027920839249288436 3.9324903012786216 ;
	setAttr ".bps" -type "matrix" -0.85931138466729529 0.50704170314619057 -0.067027273939688839 0
		 0.50774930732865509 0.8614740412753672 0.0072881490076302773 0 0.061437652042107001 -0.027770262499596608 -0.99772452482248652 0
		 -0.62684299994023807 0.94430200000000009 -0.12435799999999972 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "middle03RGT_bind_jnt" -p "middle02RGT_bind_jnt";
	rename -uid "AAE75DA5-4F83-FA60-B2AE-D38D76D04C4D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" -2.5681520220643961e-05 -0.63988217709311357 -1.0728586013808439e-05 ;
	setAttr ".r" -type "double3" -1.4629309130559757e-15 -1.523187515419638e-14 1.7159154626704302e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.5843569614879223 -0.097633733441345558 8.547792347069274 ;
	setAttr ".bps" -type "matrix" -0.77419155398932904 0.62940598148263394 -0.06689953815587972 0
		 0.62636219646643454 0.77705190229193577 0.062134853200335738 0 0.091092461649315074 0.0062009368941599308 -0.99582313279633283 0
		 -0.63704099994023899 0.9269980000000011 -0.12450399999999996 1;
	setAttr ".sd" 1;
	setAttr ".typ" 20;
createNode joint -n "ring01RGT_bind_jnt" -p "handRGT_bind_jnt";
	rename -uid "93AD5826-473E-5E1D-BE89-288278588B43";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.51578538036251587 -2.5495667885556896 0.40086136669122663 ;
	setAttr ".r" -type "double3" 3.9061187181723816e-14 9.44227171059482e-15 -1.0833764383735101e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 1.7540683161670951 -3.3345328845400908 -19.313753301290038 ;
	setAttr ".bps" -type "matrix" -0.89175580717150216 0.44125301229117242 -0.10033623233841912 0
		 0.43249087604286018 0.89630811262254906 0.097894889481948841 0 0.13312859390672743 0.043903831165057472 -0.99012586628844701 0
		 -0.60222799994023801 0.98318900000000009 -0.14936799999999975 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "ring02RGT_bind_jnt" -p "ring01RGT_bind_jnt";
	rename -uid "57DF5E91-45FF-27F4-2823-91B43E717EE1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -2.703382680380173e-06 -1.299575115026947 -1.6402593808084731e-05 ;
	setAttr ".r" -type "double3" -1.3169484227934873e-15 -1.4411888400381559e-14 -1.2889943289134371e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 2.2686282810625049 -1.4970626300711436 13.524765769490712 ;
	setAttr ".bps" -type "matrix" -0.76214220299620961 0.63956129606931955 -0.1005017959153796 0
		 0.63461556086959459 0.76873332538860895 0.079449130512176849 0 0.12807166866350547 -0.0032284682285562694 -0.9917596607437924 0
		 -0.61987099994023775 0.94662500000000005 -0.15336099999999964 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "ring03RGT_bind_jnt" -p "ring02RGT_bind_jnt";
	rename -uid "78887C31-48B8-8972-09DB-E3B0302A2135";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 2.0944147323120887e-06 -0.62161634596117032 2.3408065565000413e-05 ;
	setAttr ".r" -type "double3" 3.8471045199811639e-14 -6.9326152822525137e-15 1.2126641225687436e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.5211847300899759 -0.154766610472065 2.2345630547343753 ;
	setAttr ".bps" -type "matrix" -0.73646998052226398 0.66903716873650287 -0.1000061730023713 0
		 0.65748552927677362 0.74271398992862825 0.12684127071240808 0 0.15913750840445373 0.027662176583577763 -0.98686881468890342 0
		 -0.63225399994023812 0.93162500000000026 -0.15491199999999963 1;
	setAttr ".sd" 1;
	setAttr ".typ" 21;
createNode joint -n "pinky01RGT_bind_jnt" -p "handRGT_bind_jnt";
	rename -uid "D4571DF4-4C79-3636-1F50-A4BEC920EA38";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.67825528535665569 -2.5310584149946003 1.0350952796761685 ;
	setAttr ".r" -type "double3" 1.5902773407317584e-14 -2.1667528767470207e-14 -2.2860236773019057e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -3.965209248126865 -11.202288567747102 -24.747852527312176 ;
	setAttr ".bps" -type "matrix" -0.89915146136844104 0.3618382128229376 -0.24617017946960876 0
		 0.32140556496697448 0.92774385287173544 0.18970979486301459 0 0.29702712389150099 0.091457373676535655 -0.9504790563042057 0
		 -0.59634199994023807 0.9819150000000002 -0.16902599999999968 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "pinky02RGT_bind_jnt" -p "pinky01RGT_bind_jnt";
	rename -uid "1B54DAC6-4AAD-6152-8697-2D96DB3CEC20";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -1.7691436951849937e-05 -1.0112536561434275 3.0106309361066508e-06 ;
	setAttr ".r" -type "double3" 1.1529510720305249e-14 -9.7901448788798878e-15 2.422688136271037e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -2.7539460991006317 -5.1530792180714586 22.842899960420571 ;
	setAttr ".bps" -type "matrix" -0.67433910621176141 0.69902673360833212 -0.23796721525115178 0
		 0.62725810396131865 0.71230733996321871 0.31490558021314091 0 0.38963321322543143 0.063086283258633163 -0.91880687852031073 0
		 -0.60654399994023889 0.95246500000000034 -0.17504799999999973 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "pinky03RGT_bind_jnt" -p "pinky02RGT_bind_jnt";
	rename -uid "1F77FC01-4BFE-B85A-1475-78B363A985FB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 1.2411723041338973e-05 -0.38078971534468398 -6.287235861046625e-06 ;
	setAttr ".r" -type "double3" -1.2722218725854064e-14 -9.9765055047468933e-15 -2.7143425157528979e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 1.4708903178467991 2.0013117996087466 -6.9584720828762308 ;
	setAttr ".bps" -type "matrix" -0.75851660665725018 0.60500815275207087 -0.24211090956150022 0
		 0.55009074603179708 0.79364981607129603 0.25984637880905426 0 0.34936045648491992 0.063914822643295732 -0.93480595146325673 0
		 -0.61404199994023911 0.94395100000000065 -0.17881199999999989 1;
	setAttr ".sd" 1;
	setAttr ".typ" 22;
createNode joint -n "handRGT_prop_jnt" -p "handRGT_bind_jnt";
	rename -uid "3657F1E3-481B-191B-85E4-32A158A26788";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.0340086011762395 -2.5477728097507955 -0.27042283549160651 ;
	setAttr ".r" -type "double3" -4.7708320221952767e-15 -1.033680271475643e-14 1.8934239588087498e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -5.5835049064633138 -5.4045404030608832 135.2107317631081 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 9.0147846190488966e-10 -1.3877787807814457e-17 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 1.3877787807814457e-17 1.1076510713196976e-15 0.99999999999999989 0
		 79.702359949404638 138.65563836087185 -4.351286576303516 1;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
createNode joint -n "lowerArmRGT_prop_jnt" -p "lowerArmRGT_bind_jnt";
	rename -uid "40F5A4FD-40AE-FCD3-ACCE-A287BF331BFB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -0.00011261534088902181 -0.0001012659516774761 -2.1385137092266859e-06 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -178.48893867972046 1.5381316190278245 134.50143208808032 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 9.0147846190488966e-10 -1.3877787807814457e-17 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 1.3877787807814457e-17 1.1076510713196976e-15 0.99999999999999989 0
		 79.702359949404638 138.65563836087185 -4.351286576303516 1;
	setAttr ".sd" 1;
	setAttr ".typ" 15;
createNode joint -n "upperArmArmorRGT_bind_jnt" -p "shoulderRGT_bind_jnt";
	rename -uid "4E3CE770-4B72-B26A-D94A-6D811E2B82D3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -2.6788731245943458 1.5801102977257528 1.4825512296661914 ;
	setAttr ".r" -type "double3" 1.0634979716143634e-14 -2.3605679276487015e-15 -2.5437643053890066e-14 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1.0000000000000002 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -0.72880333638970585 0.24622404707936221 -135.47830756280555 ;
	setAttr ".bps" -type "matrix" -0.71297844704362701 0.70117277923743293 0.0042974070918007324 0
		 0.70116150253661991 0.71288902377667096 0.012719557356084927 0 0.0058550330355912348 0.012081946664322329 -0.99990986851463404 0
		 -0.17846499994023873 1.4287800000000006 -0.10706699999999986 1;
createNode joint -n "neck_bind_jnt" -p "upperChest_bind_jnt";
	rename -uid "F19DB528-4D25-1A47-2BF2-FC9451545D58";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -5.8004816227974487e-18 5.8823735701447148 -1.3322676295501878e-14 ;
	setAttr ".r" -type "double3" 3.1805546814127094e-15 -2.4265706493099335e-20 -1.9690565521319039e-19 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 26.491738530267572 0.00010994992472408334 -0.00046709157465712797 ;
	setAttr ".bps" -type "matrix" 0.9999999999979976 5.9353675367225716e-07 -1.911211276998669e-06 0
		 6.6556704403451233e-09 0.95401558342435089 0.29975701256767184 0 2.0012421456029937e-06 -0.29975701256708431 0.95401558342243653 0
		 -1.6690907772453011e-06 1.5093994140624982 -0.072089463472365736 1;
	setAttr ".typ" 7;
createNode joint -n "head_bind_jnt" -p "neck_bind_jnt";
	rename -uid "FEC7262B-4ABC-8446-7720-1DB1720F4048";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 2.3716922523120409e-20 4.1401281408699688 -1.0658141036401503e-14 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -0.00011410985748880617 0 ;
	setAttr ".bps" -type "matrix" 1 -3.4571309739065954e-09 -1.1200784223661676e-08 0
		 6.6556704403451249e-09 0.95401558342435111 0.2997570125676719 0 9.6494234431533527e-09 -0.29975701256767195 0.95401558342435089 0
		 -1.668225809594059e-06 1.633382809249937 -0.033133189806495787 1;
	setAttr ".typ" 8;
createNode joint -n "upperLegLFT_bind_jnt" -p "hips_bind_jnt";
	rename -uid "A84DBE2D-43AC-5390-98B7-5E9E6C6B4114";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 3.7567331423397712 -2.1070183535039462 -0.26123625241420223 ;
	setAttr ".r" -type "double3" 1.590277340731758e-15 -7.7650260777917851e-19 -6.2120208622334296e-18 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -170.76919270493914 -0.00097950429435360894 0.026686849053254785 ;
	setAttr ".bps" -type "matrix" 0.99999989136108991 0.0004661306772952277 -3.3881317890172014e-21 0
		 0.0004625273520130363 -0.99226960226782857 -0.12410005029690663 0 -5.7846840497268892e-05 0.12410003681481241 -0.99226971006692832 0
		 0.11792465696133267 0.91928060635633702 -0.012448843568563472 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "lowerLegLFT_bind_jnt" -p "upperLegLFT_bind_jnt";
	rename -uid "E6428A2E-4582-65A0-440B-16B790A24087";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 3.5527136788005009e-14 13.015634370667442 1.5099033134902129e-14 ;
	setAttr ".r" -type "double3" -7.1045135473098511e-16 4.0194228726890883e-12 -7.41890004037422e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 3.327023980913669 0.052858169303995652 0.42264326845868161 ;
	setAttr ".bps" -type "matrix" 0.99997572462694451 -0.0069677942576739389 -7.1332154592818053e-14 0
		 -0.0068520994557113588 -0.98337190580528155 -0.18147380969698709 0 0.0012644721690547324 0.18146940435255737 -0.98339577810465639 0
		 0.11811362877594783 0.51387542002335296 -0.063151600056886192 1;
	setAttr ".sd" 1;
	setAttr ".typ" 3;
createNode joint -n "footLFT_bind_jnt" -p "lowerLegLFT_bind_jnt";
	rename -uid "C5F5FAF7-4C97-256B-F5F5-41BEB02F7727";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.7763568394002505e-15 12.403087901018662 1.1546319456101628e-14 ;
	setAttr ".r" -type "double3" -3.1806420380068905e-14 -1.987846675914697e-16 1.9257264672923639e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -37.184377683135757 -0.15174942855128754 -0.82235128182753059 ;
	setAttr ".bps" -type "matrix" 0.99997091310744268 0.0076271186608833468 -1.7347234759768071e-18 0
		 0.0068120632633016298 -0.89311120285631818 0.44978436514249487 0 0.0034305587247518902 -0.44977128231299213 -0.89313718144155385 0
		 0.11544586265727222 0.13101374830927504 -0.13380581108604422 1;
	setAttr ".sd" 1;
	setAttr ".typ" 4;
createNode joint -n "toesLFT_bind_jnt" -p "footLFT_bind_jnt";
	rename -uid "608DD74A-4E97-47AD-98D1-23B3434DCE77";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -4.4408920985006262e-16 4.6842896276879697 -4.2188474935755949e-15 ;
	setAttr ".r" -type "double3" 6.3611093629270335e-15 3.975693351829395e-16 1.5902773407317584e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -63.847232765595663 -1.6861104490142387 -0.34099311739101351 ;
	setAttr ".bps" -type "matrix" 0.99958066308065874 -0.00029738189782785654 -0.02895530278269421 0
		 0.028956829854641444 0.010265529621693248 0.99952794903712217 0 4.1991150140363587e-15 -0.9999472638422453 0.010269836143143363 0
		 0.11644751424813578 -0.00031008451219602384 -0.067669134505594725 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "toesTipLFT_bind_jnt" -p "toesLFT_bind_jnt";
	rename -uid "0980F705-4AD4-C250-16B5-8F9DC6AD9B8D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 2.2204460492503131e-15 6.2898314820554928 1.9637069748057456e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -89.41157138884931 -1.987846675914698e-16 1.659336085528166 ;
	setAttr ".bps" -type "matrix" 1 4.1945614563945702e-15 -3.6774356158123114e-16 0
		 -4.1945567601546071e-15 1 -9.298117831235686e-16 0 3.6925223662400209e-16 1.1709383462843448e-15 1.0000000000000004 0
		 0.12216472625732186 0.0017167329788212778 0.12967681884765692 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "upperLegRGT_bind_jnt" -p "hips_bind_jnt";
	rename -uid "A2AB8A2D-48C9-EF7F-BAED-6AB27890744D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -3.7567441092663874 -2.1070055445379836 -0.26123439337757226 ;
	setAttr ".r" -type "double3" -3.1805546814635168e-15 1.1647539116687687e-18 1.5517919302337029e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 9.230807294975401 0.00097968789354431506 -0.026691851261282141 ;
	setAttr ".bps" -type "matrix" 0.99999989136109002 -0.00046613067712510239 3.3881317890172014e-21 0
		 0.00046252735184422613 0.99226960226782801 0.12410005029690796 0 -5.7846840476156968e-05 -0.12410003681481374 0.99226971006692788 0
		 -0.11792499999999997 0.91928100000000013 -0.012448800000000013 1;
	setAttr ".sd" 1;
	setAttr ".typ" 2;
createNode joint -n "lowerLegRGT_bind_jnt" -p "upperLegRGT_bind_jnt";
	rename -uid "CCBDA8D6-44D8-0789-2CEE-6FAEBEB06474";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -8.8582310686646792e-07 -13.015660263765557 1.8414152354040425e-06 ;
	setAttr ".r" -type "double3" 6.2523019349866074e-15 3.9681768065860932e-12 -7.325401361371525e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 3.327023980913379 0.052858169302726896 0.42264326844811445 ;
	setAttr ".bps" -type "matrix" 0.99997572462694462 0.0069677942576583064 7.0427821560747894e-14 0
		 -0.0068520994556958278 0.98337190580528189 0.18147380969698357 0 0.0012644721690527616 -0.18146940435255388 0.98339577810465684 0
		 -0.11811400000000001 0.51387499999999986 -0.06315160000000003 1;
	setAttr ".sd" 1;
	setAttr ".typ" 3;
createNode joint -n "footRGT_bind_jnt" -p "lowerLegRGT_bind_jnt";
	rename -uid "1A616FBC-4E20-BD44-5ADD-A79569144C8B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 7.5996939763456339e-06 -12.403068001539113 -9.7939106122879593e-06 ;
	setAttr ".r" -type "double3" -6.259232220786399e-14 -1.2483677124744308e-13 -6.3381248857367624e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -37.184377683135537 -0.15174942855100154 -0.82235128182648487 ;
	setAttr ".bps" -type "matrix" 0.99997091310744279 -0.0076271186608801176 -2.4446590585203154e-15 0
		 0.006812063263297646 0.89311120285631806 -0.4497843651424952 0 0.0034305587247526266 0.44977128231299207 0.89313718144155374 0
		 -0.11544599999999998 0.13101400000000019 -0.13380600000000004 1;
	setAttr ".sd" 1;
	setAttr ".typ" 4;
createNode joint -n "toesRGT_bind_jnt" -p "footRGT_bind_jnt";
	rename -uid "FC59A68A-4326-E5DA-6C56-82A130EF4ACA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -1.103769505839125e-05 -4.6843000795911696 2.7055059239611268e-06 ;
	setAttr ".r" -type "double3" -2.6001966324093584e-14 1.3914926731402574e-15 -1.3865230564505018e-13 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yxz";
	setAttr ".jo" -type "double3" -63.847232765595635 -1.6861104490142538 -0.34099311739127502 ;
	setAttr ".bps" -type "matrix" 0.99958066308065874 0.00029738189782712102 0.028955302782694047 0
		 0.028956829854641278 -0.010265529621693026 -0.99952794903712205 0 4.9255304696016466e-15 0.9999472638422453 -0.010269836143143418 0
		 -0.11644799999999995 -0.00031008499999990446 -0.06766909999999994 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode joint -n "toesTipRGT_bind_jnt" -p "toesRGT_bind_jnt";
	rename -uid "1084272A-400B-9718-27C0-D4931F041184";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 6.8864055711159722e-06 -6.2898359551960414 -1.2733025874650528e-07 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
	setAttr ".jo" -type "double3" -89.411571388849296 0 1.6593360855281567 ;
	setAttr ".bps" -type "matrix" 1 -4.9234704854739242e-15 3.677613769070831e-16 0 -4.9233733622479273e-15 -1 6.5399075044325627e-16 0
		 3.697735104205981e-16 -5.9501015226004483e-16 -1.0000000000000002 0 -0.12216499999999998 0.0017167300000000829 0.12967700000000004 1;
	setAttr ".sd" 1;
	setAttr ".typ" 5;
createNode transform -n "rig_grp";
	rename -uid "8D3B0D6C-4CD4-FF88-2CCB-DCAD8EB14499";
createNode transform -n "placement_Zro_grp" -p "rig_grp";
	rename -uid "0F74D13F-4647-E6CC-3126-2287565AC10F";
createNode transform -n "placement_ctrl" -p "placement_Zro_grp";
	rename -uid "545848AF-4432-9782-9053-C092EB875966";
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
	setAttr -k on ".IK_FK_Arm_L" 1;
	setAttr -k on ".IK_FK_Arm_R" 1;
	setAttr -k on ".IK_FK_Leg_Vis";
	setAttr -k on ".IK_FK_Leg_L";
	setAttr -k on ".IK_FK_Leg_R";
	setAttr -cb on ".____Prop____";
	setAttr -k on ".Prop_Ctrl_Vis";
createNode nurbsCurve -n "placement_ctrlShape" -p "placement_ctrl";
	rename -uid "86A34072-4E1B-6956-BE39-9982665A8B4F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 25 0 no 3
		26 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		26
		-23.790145979559021 0 -23.790145979558993
		-23.790145979559021 0 -23.790145979558993
		-11.895072989779495 0 -35.685218969338486
		-23.790145979558989 0 -35.685218969338486
		0 0 -59.475364948897493
		23.790145979558989 0 -35.685218969338486
		11.895072989779495 0 -35.685218969338486
		23.790145979558989 0 -23.620971073729415
		35.685218969338486 0 -11.895072989779495
		35.685218969338486 0 -23.790145979558989
		59.475364948897493 0 0
		35.685218969338486 0 23.790145979558989
		35.685218969338486 0 11.895072989779495
		23.790145979559021 0 23.790145979558993
		11.895072989779495 0 35.685218969338486
		23.790145979558989 0 35.685218969338486
		0 0 59.475364948897493
		-23.790145979558989 0 35.685218969338486
		-11.895072989779495 0 35.685218969338486
		-23.790145979559021 0 23.790145979558993
		-35.685218969338486 0 11.895072989779495
		-35.685218969338486 0 23.790145979558989
		-59.475364948897493 0 0
		-35.685218969338486 0 -23.790145979558989
		-35.685218969338486 0 -11.895072989779495
		-23.790145979559021 0 -23.790145979558993
		;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0 ;
createNode transform -n "fly_Zro_grp" -p "placement_ctrl";
	rename -uid "5341A656-4FAD-9950-F250-BBB3E30769C2";
createNode transform -n "fly_ctrl" -p "fly_Zro_grp";
	rename -uid "DBE4FEFD-4908-8FD1-3894-B3A26DDC572F";
createNode nurbsCurve -n "fly_ctrlShape" -p "fly_ctrl";
	rename -uid "03D901DF-4BDE-C2C7-2A13-59AE07F4E64B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 47 0 no 3
		48 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
		48
		-27.789325629522217 0 0
		-27.789325629522217 0 0
		-27.447176194585833 0 -4.3472046501962645
		-26.429224199452662 0 -8.58736133352898
		-24.760460418186341 0 -12.616078909613115
		-22.482037985927988 0 -16.334141514641587
		-19.650027011484674 0 -19.650027011484674
		-16.334141514641587 0 -22.482037985927988
		-12.616078909613115 0 -24.760460418186341
		-8.58736133352898 0 -26.429224199452662
		-4.3472046501962645 0 -27.447176194585833
		0 0 -27.789325629522217
		0 0 -27.789325629522217
		0 0 -27.789325629522217
		4.3472046501962645 0 -27.447176194585833
		8.58736133352898 0 -26.429224199452662
		12.616078909613115 0 -24.760460418186341
		16.334141514641587 0 -22.482037985927988
		19.650027011484674 0 -19.650027011484674
		22.482037985927988 0 -16.334141514641587
		24.760460418186341 0 -12.616078909613115
		26.429224199452662 0 -8.58736133352898
		27.447176194585833 0 -4.3472046501962645
		27.789325629522217 0 0
		27.789325629522217 0 0
		27.789325629522217 0 0
		27.447176194585833 0 4.3472046501962645
		26.429224199452662 0 8.58736133352898
		24.760460418186341 0 12.616078909613115
		22.482037985927988 0 16.334141514641587
		19.650027011484674 0 19.650027011484674
		16.334141514641587 0 22.482037985927988
		12.616078909613115 0 24.760460418186341
		8.58736133352898 0 26.429224199452662
		4.3472046501962645 0 27.447176194585833
		0 0 27.789325629522217
		0 0 27.789325629522217
		0 0 27.789325629522217
		-4.3472046501962645 0 27.447176194585833
		-8.58736133352898 0 26.429224199452662
		-12.616078909613115 0 24.760460418186341
		-16.334141514641587 0 22.482037985927988
		-19.650027011484674 0 19.650027011484674
		-22.482037985927988 0 16.334141514641587
		-24.760460418186341 0 12.616078909613115
		-26.429224199452662 0 8.58736133352898
		-27.447176194585833 0 4.3472046501962645
		-27.789325629522217 0 0
		;
createNode transform -n "null_IK_jnt_grp" -p "fly_ctrl";
	rename -uid "D33FD67E-4D05-29A2-0F37-C6BA6E768BB7";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "hips_null_grp" -p "null_IK_jnt_grp";
	rename -uid "B45F8DEF-45EB-4349-D447-C8BFD1A2D59E";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "shoulderLFT_null_grp" -p "null_IK_jnt_grp";
	rename -uid "3FB20869-4110-D26B-F687-A3B8A96FDBB9";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "shoulderRGT_null_grp" -p "null_IK_jnt_grp";
	rename -uid "276F9C7B-4384-91D8-16D1-8CA97354DC81";
	setAttr ".rp" -type "double3" 0 0 -4.3418649306032033e-13 ;
	setAttr ".sp" -type "double3" 0 0 -4.3418649306032033e-13 ;
createNode transform -n "IK_ctrl_grp" -p "fly_ctrl";
	rename -uid "AA099E2E-43B2-C3DC-5833-0BA0CEC2A48B";
createNode transform -n "prop_ctrl_grp" -p "fly_ctrl";
	rename -uid "19B49103-4438-DDFE-F0C0-848C47A1F1EA";
createNode transform -n "null_FK_jnt_grp" -p "fly_ctrl";
	rename -uid "BF303290-4CD5-6879-6268-D9B73F5ECEAF";
createNode transform -n "NOTOUCH_grp" -p "fly_ctrl";
	rename -uid "86F36D6E-4DA8-6BEE-F514-798F3A08D40A";
createNode transform -n "TMP_GRP" -p "rig_grp";
	rename -uid "8BB072EA-42A0-DFDF-E624-879B3802BF8F";
	setAttr ".v" no;
createNode transform -n "head_Zro_grp" -p "TMP_GRP";
	rename -uid "BBB17FBD-4A00-AA6C-B4CD-02AFDC41D2E3";
createNode transform -n "head_ctrl" -p "head_Zro_grp";
	rename -uid "29EE34A2-4F27-64BC-9457-DA8BC036F1A2";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" -1.3940650888790894e-23 -5.836450831691236e-14 -7.2955635396140418e-15 ;
	setAttr ".sp" -type "double3" -1.3940650888790894e-23 -5.836450831691236e-14 -7.2955635396140418e-15 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "head_ctrlShape" -p "head_ctrl";
	rename -uid "41E86ABC-400D-3A91-D560-27A591A918FA";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.8893787476918255e-16 11.178789222906167 0.021841441128560079
		-2.9251351819219744e-16 9.3361761571151778 -7.0945263580745017
		-2.9251281724169734e-16 0.33595469566019626 -9.5914562036159641
		-2.9251281724169734e-16 -7.4335402406957742 -7.0945263580745017
		-4.8517064936418692e-16 -9.9314126865397387 0.00024214905716435139
		1.0851857795149401e-14 -9.5673159918497745 6.510463409396487
		8.311027498527734e-15 -0.69899280595957547 9.068846441174621
		4.1425352389958571e-15 8.7823998211741259 5.8288337476847678
		-4.8893787476918255e-16 11.178789222906167 0.021841441128560079
		6.5360524304417291 9.3333181144904369 0.010327827225954374
		9.8040786456626083 0.33595469566019548 -3.7232200691627288e-15
		6.5360524304417291 -7.4359860624039005 0.003549924567438619
		-4.8517064936418692e-16 -9.9314126865397387 0.00024214905716435139
		-6.5360524304417291 -7.4359860624039005 0.003549924567438619
		-9.8040786456626083 0.33595469566019548 -3.7232200691627288e-15
		-6.5360524304417291 9.3333175442661584 0.010327827225954374
		-4.8893787476918255e-16 11.178789222906167 0.021841441128560079
		;
createNode transform -n "head_Gimbal_ctrl" -p "head_ctrl";
	rename -uid "34AA5B03-4B71-8C1A-8CCD-35B02B60BC64";
	setAttr ".rp" -type "double3" -1.3940650888790894e-23 -5.836450831691236e-14 -7.2955635396140418e-15 ;
	setAttr ".sp" -type "double3" -1.3940650888790894e-23 -5.836450831691236e-14 -7.2955635396140418e-15 ;
createNode nurbsCurve -n "head_Gimbal_ctrlShape" -p "head_Gimbal_ctrl";
	rename -uid "78242533-4A46-AE3A-2378-C0B35B141920";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.1559719564490276e-16 9.501970839470232 0.018565224959274974
		-2.4863649255446549e-16 7.9357497335478904 -6.0303474043633276
		-2.4863589674654039e-16 0.28556149131115799 -8.1527377730735715
		-2.4863589674654039e-16 -6.3185092045914164 -6.0303474043633276
		-4.1239505405065649e-16 -8.4417007835587849 0.0002058266985886043
		9.2240791237858933e-15 -8.1322185930723183 5.5338938979870127
		7.0643733716574767e-15 -0.59414388506564786 7.7085194749984263
		3.5211549510553806e-15 7.4650398479979962 4.9545086855320521
		-4.1559719564490276e-16 9.501970839470232 0.018565224959274974
		5.555644565875471 7.9333203973168622 0.0087786531420601249
		8.3334668488132166 0.28556149131115738 -4.259071589730427e-15
		5.555644565875471 -6.3205881530433246 0.0030174358823217319
		-4.1239505405065649e-16 -8.4417007835587849 0.0002058266985886043
		-5.555644565875471 -6.3205881530433246 0.0030174358823217319
		-8.3334668488132166 0.28556149131115738 -4.259071589730427e-15
		-5.555644565875471 7.9333199126262253 0.0087786531420601249
		-4.1559719564490276e-16 9.501970839470232 0.018565224959274974
		;
createNode transform -n "neck_Zro_grp" -p "TMP_GRP";
	rename -uid "B42CB66B-4CC5-D348-E787-99B0A6F1DAA4";
createNode transform -n "neck_ctrl" -p "neck_Zro_grp";
	rename -uid "0370C93C-4AA5-7E12-072D-5BB0B8FD9C48";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" -1.7431519705689263e-21 0 0 ;
	setAttr ".sp" -type "double3" -1.7431519705689263e-21 0 0 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "neck_ctrlShape" -p "neck_ctrl";
	rename -uid "0CEC9B0A-4FED-5B98-7931-93AEB6B2534C";
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
	rename -uid "02AEC970-4B9F-DA50-075F-FEBCC8B634D3";
	setAttr ".rp" -type "double3" -1.7431519705689263e-21 0 0 ;
	setAttr ".sp" -type "double3" -1.7431519705689263e-21 0 0 ;
createNode nurbsCurve -n "neck_Gimbal_ctrlShape" -p "neck_Gimbal_ctrl";
	rename -uid "90EA3AF7-4C65-4844-96A3-AEAEA01F5884";
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
	rename -uid "3FCE7892-4F40-CBD3-A8DD-1FB448A13392";
createNode transform -n "upperChest_ctrl" -p "upperChest_Zro_grp";
	rename -uid "411C3CFA-4910-CA03-01CC-84852759DAAE";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
	setAttr ".sp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "upperChest_ctrlShape" -p "upperChest_ctrl";
	rename -uid "B797AC09-4C6C-81F4-FBDF-2D9A4E54BB95";
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
	rename -uid "CA3E4FFD-4B2F-F520-E62D-6FB8FB825734";
	setAttr ".rp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
	setAttr ".sp" -type "double3" 3.7745837261011702e-24 0 2.2798636061293881e-16 ;
createNode nurbsCurve -n "upperChest_Gimbal_ctrlShape" -p "upperChest_Gimbal_ctrl";
	rename -uid "E8336A04-4946-820F-24F4-DA90B0DFBB0C";
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
createNode transform -n "chest_Zro_grp" -p "TMP_GRP";
	rename -uid "AB10000D-417D-A16F-A1F2-6C87AEF091D1";
	setAttr ".rp" -type "double3" -2.0882749074111216e-15 0 0 ;
	setAttr ".sp" -type "double3" -2.0882749074111216e-15 0 0 ;
createNode transform -n "chest_ctrl" -p "chest_Zro_grp";
	rename -uid "1FEB1877-474B-9480-1B8B-BC81F51E31DB";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -2.0882741302869769e-15 -7.295563539614045e-15 6.8395908183881637e-16 ;
	setAttr ".sp" -type "double3" -2.0882741302869769e-15 -7.295563539614045e-15 6.8395908183881637e-16 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "chest_ctrlShape" -p "chest_ctrl";
	rename -uid "B056A45D-4654-96D9-B946-A39B4B798B6D";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-10.756930400799558 1.729680105035128 -8.1002521789207265
		-10.756930400799558 1.729680105035128 8.1002521789207282
		10.756930400799554 1.729680105035128 8.1002521789207282
		10.756930400799554 1.729680105035128 -8.1002521789207265
		-10.756930400799558 1.729680105035128 -8.1002521789207265
		-10.756930400799558 -1.7296801050351427 -8.1002521789207265
		-10.756930400799558 -1.7296801050351427 8.1002521789207282
		10.756930400799554 -1.7296801050351427 8.1002521789207282
		10.756930400799554 1.729680105035128 8.1002521789207282
		-10.756930400799558 1.729680105035128 8.1002521789207282
		-10.756930400799558 -1.7296801050351427 8.1002521789207282
		-10.756930400799558 -1.7296801050351427 -8.1002521789207265
		10.756930400799554 -1.7296801050351427 -8.1002521789207265
		10.756930400799554 1.729680105035128 -8.1002521789207265
		10.756930400799554 1.729680105035128 8.1002521789207282
		10.756930400799554 -1.7296801050351427 8.1002521789207282
		10.756930400799554 -1.7296801050351427 -8.1002521789207265
		;
createNode nurbsCurve -n "chest_ctrlShape1" -p "chest_ctrl";
	rename -uid "FEDF6110-4723-960B-6C63-0CA1FBF353CB";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		-2.0882741302869773e-15 -7.295563539614045e-15 -0.31207744970271345
		-2.2942168575237516e-15 -4.6312748951000086e-14 -12.154371202063583
		-3.4568847696825764e-16 2.9251305628634716 -12.154371202063583
		-4.242745238079249e-15 2.9251305628634716 -18.004632327790659
		-8.1398019991902452e-15 -2.9251305628635782 -18.004632327790659
		-4.242745238079249e-15 -2.9251305628635782 -12.154371202063583
		-2.2942168575237516e-15 -4.6312748951000086e-14 -12.154371202063583
		;
createNode transform -n "chest_Gimbal_ctrl" -p "chest_ctrl";
	rename -uid "15C41DA8-43D5-663E-3918-8AB77EFC532A";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -2.0882741302869769e-15 -7.295563539614045e-15 6.8395908183881637e-16 ;
	setAttr ".sp" -type "double3" -2.0882741302869769e-15 -7.295563539614045e-15 6.8395908183881637e-16 ;
createNode nurbsCurve -n "chest_Gimbal_ctrlShape" -p "chest_Gimbal_ctrl";
	rename -uid "D9754687-492E-314C-0A3D-7CA7D1F471BD";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-9.1433908406796238 1.4702280892798574 -6.8852143520826168
		-9.1433908406796238 1.4702280892798574 6.8852143520826194
		9.143390840679622 1.4702280892798574 6.8852143520826194
		9.143390840679622 1.4702280892798574 -6.8852143520826168
		-9.1433908406796238 1.4702280892798574 -6.8852143520826168
		-9.1433908406796238 -1.4702280892798723 -6.8852143520826168
		-9.1433908406796238 -1.4702280892798723 6.8852143520826194
		9.143390840679622 -1.4702280892798723 6.8852143520826194
		9.143390840679622 1.4702280892798574 6.8852143520826194
		-9.1433908406796238 1.4702280892798574 6.8852143520826194
		-9.1433908406796238 -1.4702280892798723 6.8852143520826194
		-9.1433908406796238 -1.4702280892798723 -6.8852143520826168
		9.143390840679622 -1.4702280892798723 -6.8852143520826168
		9.143390840679622 1.4702280892798574 -6.8852143520826168
		9.143390840679622 1.4702280892798574 6.8852143520826194
		9.143390840679622 -1.4702280892798723 6.8852143520826194
		9.143390840679622 -1.4702280892798723 -6.8852143520826168
		;
createNode transform -n "spine_Zro_grp" -p "TMP_GRP";
	rename -uid "3B1F0A4C-4829-272A-9720-0EB6011157E3";
createNode transform -n "spine_ctrl" -p "spine_Zro_grp";
	rename -uid "41EBA297-4971-7CB0-9B13-4A9BF40E0480";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 3.3800256886112989e-07 -1.4591127079228087e-14 -9.1194544245175523e-16 ;
	setAttr ".sp" -type "double3" 3.3800256886112989e-07 -1.4591127079228087e-14 -9.1194544245175523e-16 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "spine_ctrlShape" -p "spine_ctrl";
	rename -uid "FB7DD388-46B7-B604-6154-6289FCC12CCF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-10.756929988088729 1.7296805696478803 -8.10025217892073
		-10.756929988088729 1.7296805696478803 8.10025217892073
		10.756930813510367 1.7296796404223602 8.10025217892073
		10.756930813510367 1.7296796404223602 -8.10025217892073
		-10.756929988088729 1.7296805696478803 -8.10025217892073
		-10.756930137505229 -1.7296796404223895 -8.10025217892073
		-10.756930137505229 -1.7296796404223895 8.10025217892073
		10.756930664093868 -1.7296805696479092 8.10025217892073
		10.756930813510367 1.7296796404223602 8.10025217892073
		-10.756929988088729 1.7296805696478803 8.10025217892073
		-10.756930137505229 -1.7296796404223895 8.10025217892073
		-10.756930137505229 -1.7296796404223895 -8.10025217892073
		10.756930664093868 -1.7296805696479092 -8.10025217892073
		10.756930813510367 1.7296796404223602 -8.10025217892073
		10.756930813510367 1.7296796404223602 8.10025217892073
		10.756930664093868 -1.7296805696479092 8.10025217892073
		10.756930664093868 -1.7296805696479092 -8.10025217892073
		;
createNode nurbsCurve -n "spine_ctrlShape1" -p "spine_ctrl";
	rename -uid "95E4456F-4E38-FDB2-AF8C-FDBEA09614B7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 6 0 no 3
		7 0 1 2 3 4 5 6
		7
		3.3800256886113036e-07 -1.4591127079228134e-14 -0.31207744970271423
		3.3800256865518584e-07 -5.3608312481719104e-14 -12.154371202063585
		4.6434465221358235e-07 2.925130562863461 -12.154371202063585
		4.6434464831652564e-07 2.925130562863461 -18.004632327790663
		2.1166048119973042e-07 -2.9251305628635822 -18.004632327790663
		2.1166048509678711e-07 -2.9251305628635822 -12.154371202063585
		3.3800256865518584e-07 -5.3608312481719104e-14 -12.154371202063585
		;
createNode transform -n "spine_Gimbal_ctrl" -p "spine_ctrl";
	rename -uid "497F529D-45E9-FDB6-1B08-3E824BCF6B56";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 3.3800256886112989e-07 -1.4591127079228087e-14 -9.1194544245175523e-16 ;
	setAttr ".sp" -type "double3" 3.3800256886112989e-07 -1.4591127079228087e-14 -9.1194544245175523e-16 ;
createNode nurbsCurve -n "spine_Gimbal_ctrlShape" -p "spine_Gimbal_ctrl";
	rename -uid "94A64493-4B31-BCAA-3C46-9D85FA349505";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-9.1433904391750325 1.4702284842006959 -6.8852143520826194
		-9.1433904391750325 1.4702284842006959 6.8852143520826194
		9.1433912421841974 1.470227694359004 6.8852143520826194
		9.1433912421841974 1.470227694359004 -6.8852143520826194
		-9.1433904391750325 1.4702284842006959 -6.8852143520826194
		-9.1433905661790593 -1.4702276943590333 -6.8852143520826194
		-9.1433905661790593 -1.4702276943590333 6.8852143520826194
		9.1433911151801706 -1.4702284842007252 6.8852143520826194
		9.1433912421841974 1.470227694359004 6.8852143520826194
		-9.1433904391750325 1.4702284842006959 6.8852143520826194
		-9.1433905661790593 -1.4702276943590333 6.8852143520826194
		-9.1433905661790593 -1.4702276943590333 -6.8852143520826194
		9.1433911151801706 -1.4702284842007252 -6.8852143520826194
		9.1433912421841974 1.470227694359004 -6.8852143520826194
		9.1433912421841974 1.470227694359004 6.8852143520826194
		9.1433911151801706 -1.4702284842007252 6.8852143520826194
		9.1433911151801706 -1.4702284842007252 -6.8852143520826194
		;
createNode transform -n "hips_Zro_grp" -p "TMP_GRP";
	rename -uid "E0E3F96B-4F29-9816-CAC7-79B15FB50E00";
createNode transform -n "hips_ctrl" -p "hips_Zro_grp";
	rename -uid "E4D8854E-4DEF-71A6-D6FE-EB82E142D823";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
	setAttr ".sp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "hips_ctrlShape" -p "hips_ctrl";
	rename -uid "CC2A84D6-4C74-43B4-777F-9BB294183130";
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
		12.150110714722597 -1.1825015589624794 -0.34463613519830766
		11.725473400877952 -1.1825015404009878 -3.4572299092015171
		10.512393122941694 -1.1825014873755642 -6.2149411290357728
		8.5914265475889167 -1.1825014034074377 -8.3355044424183298
		6.0699271934589927 -1.1825012931891952 -9.673401270693331
		3.1412970065920236 -1.1825011651746935 -10.341329847926154
		-9.7302171270950447e-07 -1.1825010278641865 -10.538819620923542
		-8.6955670885177917e-07 1.1845021606351984 -10.538819620923549
		3.1412971100570366 1.1845020233246915 -10.34132984792616
		6.0699272969239848 1.18450189531019 -9.6734012706933399
		8.5914266510539257 1.1845017850919475 -8.3355044424183333
		10.512393226406704 1.184501701123821 -6.2149411290357754
		11.725473504342963 1.1845016480983936 -3.4572299092015188
		12.150110818187608 1.1845016295369055 -0.34463613519830777
		12.150110714722597 -1.1825015589624794 -0.34463613519830766
		11.725473945101045 -1.1825015404010115 2.7679561428409745
		10.5123941493391 -1.182501487375609 5.525675685363713
		8.5914279447572106 -1.1825014034074988 7.6462366505360055
		6.0699288245539895 -1.1825012931892664 8.9841491873752286
		3.141298754470025 -1.1825011651747699 9.652062269216124
		8.0939427313538595e-07 -1.1825010278642645 9.8496410393042986
		-3.1412971702271952 -1.1825008905537577 9.6520628184581785
		-6.0699273570927508 -1.1825007625392598 8.9841502486752809
		-8.5914267112240221 -1.1825006523210098 7.6462381527089924
		-10.512393286576563 -1.1825005683528909 5.525677523409156
		-11.725473564513534 -1.1825005153274597 2.7679581929880777
		-12.15011087835801 -1.182500496765968 -0.34463401080529199
		-12.150110774893013 1.1845026917334134 -0.3446340108052921
		-11.725474005271602 1.184502673171949 -3.4572278590544077
		-10.512394209508971 1.1845026201465392 -6.2149392909903316
		-8.591428004927316 1.1845025361784363 -8.3355029402453482
		-6.0699288847227635 1.1845024259601966 -9.6734002093932876
		-3.1412988146401952 1.1845022979457001 -10.341329298684105
		-8.6955670885177917e-07 1.1845021606351984 -10.538819620923549
		-9.7302171270950447e-07 -1.1825010278641865 -10.538819620923542
		-3.1412989181051967 -1.1825008905536813 -10.3413292986841
		-6.0699289881877618 -1.1825007625391886 -9.6734002093932805
		-8.5914281083923161 -1.1825006523209487 -8.3355029402453447
		-10.512394312973967 -1.1825005683528422 -6.2149392909903289
		-11.7254741087366 -1.1825005153274359 -3.4572278590544059
		-12.15011087835801 -1.182500496765968 -0.34463401080529199
		-12.150110774893013 1.1845026917334134 -0.3446340108052921
		-11.725473461048535 1.1845026731719255 2.7679581929880794
		-10.512393183111566 1.1845026201464941 5.5256775234091622
		-8.591426607759022 1.1845025361783752 7.646238152708996
		-6.0699272536277498 1.1845024259601251 8.9841502486752844
		-3.1412970667621929 1.1845022979456272 9.6520628184581838
		9.1285927699311252e-07 1.1845021606351205 9.8496410393043039
		8.0939427313538595e-07 -1.1825010278642645 9.8496410393042986
		9.1285927699311252e-07 1.1845021606351205 9.8496410393043039
		3.141298857935038 1.1845020233246151 9.6520622692161311
		6.0699289280189825 1.1845018953101185 8.9841491873752322
		8.5914280482222196 1.1845017850918826 7.64623665053601
		10.512394252804109 1.184501701123776 5.5256756853637183
		11.725474048566056 1.1845016480983737 2.7679561428409762
		12.150110818187608 1.1845016295369055 -0.34463613519830777
		;
createNode transform -n "hips_Gimbal_ctrl" -p "hips_ctrl";
	rename -uid "4E194393-4B44-2B2A-D0CB-C09C1A47FA39";
	setAttr ".rp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
	setAttr ".sp" -type "double3" 4.3484947321498653e-22 1.4591127079228087e-14 -1.7098977045970409e-16 ;
createNode nurbsCurve -n "hips_Gimbal_ctrlShape" -p "hips_Gimbal_ctrl";
	rename -uid "348D556B-47F0-B779-44D6-089B25417AC4";
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
		10.327594107514209 -1.0051263251181055 -0.2929407149185615
		9.9666523907462583 -1.0051263093408374 -2.9386454228212893
		8.9355341545004396 -1.0051262642692274 -5.2826999596804063
		7.3027125654505793 -1.0051261928963198 -7.0851787760555789
		5.1594381144401433 -1.0051260992108135 -8.2223910800893325
		2.6701024556032196 -1.0051259903984873 -8.7901303707372307
		-8.2706845580307873e-07 -1.0051258736845565 -8.95799667778501
		-7.391232025240121e-07 1.0068268365399209 -8.9579966777850171
		2.6701025435484809 1.0068267198259897 -8.790130370737236
		5.1594382023853873 1.0068266110136637 -8.2223910800893378
		7.3027126533958349 1.0068265173281574 -7.0851787760555824
		8.9355342424456996 1.0068264459552501 -5.282699959680409
		9.96665247869152 1.0068264008836367 -2.938645422821291
		10.327594195459467 1.0068263851063717 -0.29294071491856161
		10.327594107514209 -1.0051263251181055 -0.2929407149185615
		9.9666528533358889 -1.0051263093408576 2.3527627214148281
		8.9355350269382345 -1.0051262642692655 4.6968243325591557
		7.3027137530436299 -1.0051261928963717 6.4993011529556046
		5.1594395008708913 -1.0051260992108744 7.6365268092689442
		2.6701039412995211 -1.0051259903985523 8.2042529288337054
		6.8798513216507802e-07 -1.0051258736846227 8.3721948834086533
		-2.6701025946931156 -1.005125756970692 8.2042533956894541
		-5.1594382535288377 -1.0051256481583686 7.6365277113739891
		-7.3027127045404177 -1.0051255544728561 6.4993024298026425
		-8.9355342935900772 -1.0051254830999552 4.696825894897783
		-9.9666525298365052 -1.0051254380283385 2.3527644640398662
		-10.327594246604308 -1.0051254222510706 -0.29293890918449822
		-10.327594158659062 1.0068272879734037 -0.29293890918449828
		-9.9666529044808598 1.0068272721961589 -2.9386436801962468
		-8.9355350780826264 1.0068272271245602 -5.2826983973417816
		-7.302713804188218 1.006827155751673 -7.0851774992085463
		-5.1594395520143479 1.0068270620661692 -8.2223901779842947
		-2.6701039924441652 1.0068269532538472 -8.7901299038814891
		-7.391232025240121e-07 1.0068268365399209 -8.9579966777850171
		-8.2706845580307873e-07 -1.0051258736845565 -8.95799667778501
		-2.6701040803894172 -1.0051257569706269 -8.7901299038814837
		-5.1594396399595981 -1.005125648158308 -8.2223901779842876
		-7.3027138921334673 -1.0051255544728042 -7.0851774992085428
		-8.9355351660278721 -1.0051254830999137 -5.2826983973417789
		-9.9666529924261091 -1.0051254380283183 -2.938643680196245
		-10.327594246604308 -1.0051254222510706 -0.29293890918449822
		-10.327594158659062 1.0068272879734037 -0.29293890918449828
		-9.9666524418912559 1.0068272721961387 2.3527644640398675
		-8.9355342056448315 1.0068272271245222 4.6968258948977875
		-7.3027126165951675 1.0068271557516211 6.4993024298026478
		-5.1594381655835875 1.0068270620661086 7.6365277113739918
		-2.6701025067478641 1.0068269532537852 8.2042533956894577
		7.7593038544414581e-07 1.0068268365398547 8.3721948834086586
		6.8798513216507802e-07 -1.0051258736846227 8.3721948834086533
		7.7593038544414581e-07 1.0068268365398547 8.3721948834086586
		2.6701040292447824 1.0068267198259251 8.2042529288337107
		5.1594395888161353 1.0068266110136028 7.6365268092689478
		7.3027138409888854 1.0068265173281024 6.4993011529556091
		8.9355351148834927 1.0068264459552116 4.6968243325591601
		9.9666529412811471 1.0068264008836199 2.3527627214148294
		10.327594195459467 1.0068263851063717 -0.29294071491856161
		;
createNode transform -n "cog_Zro_grp" -p "TMP_GRP";
	rename -uid "F0D90FF1-4401-31CA-8F32-5EBB73C6A767";
createNode transform -n "cog_ctrl" -p "cog_Zro_grp";
	rename -uid "C568FB86-42E9-FF0A-A983-53ADE435DC3B";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "cog_ctrlShape" -p "cog_ctrl";
	rename -uid "BF563640-4AC5-03B0-D793-B1BB159B1E0B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		6.9350305473516292 7.2955635396140418e-15 -5.9279253187277083
		17.565554576323617 3.8998341041713749 -5.9279253187277083
		17.565554576323617 3.8998341041713749 5.9279253187277083
		6.9350305473516292 7.2955635396140418e-15 5.9279253187277083
		6.9107592988742903 7.2955635396140418e-15 8.3312845701520786
		-6.9107592988742903 7.2955635396140418e-15 8.3312845701520786
		-6.9350305473516292 7.2955635396140418e-15 5.9279253187277083
		-17.565554576323617 3.8998341041713749 5.9279253187277083
		-17.565554576323617 3.8998341041713749 -5.9279253187277083
		-6.9350305473516292 7.2955635396140418e-15 -5.9279253187277083
		-6.9107592988742903 7.2955635396140418e-15 -8.3312845701520786
		6.9107592988742903 7.2955635396140418e-15 -8.3312845701520786
		6.9350305473516292 7.2955635396140418e-15 -5.9279253187277083
		;
createNode transform -n "cog_Gimbal_ctrl" -p "cog_ctrl";
	rename -uid "70E93552-4298-C643-C86B-19B8A97D88D6";
	setAttr ".rp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" -4.3484947321498643e-22 7.2955635396140418e-15 0 ;
createNode nurbsCurve -n "cog_Gimbal_ctrlShape" -p "cog_Gimbal_ctrl";
	rename -uid "2FC0D544-4D43-D142-2557-05B21E0ED37A";
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
createNode transform -n "upperArmLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "F03345BB-475E-2533-DA77-CF8F70BC072F";
createNode transform -n "upperArmLFT_FK_ctrl" -p "upperArmLFT_FK_Zro_grp";
	rename -uid "D6019351-4F3E-E751-2B49-94BEEE21C669";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" -4.029018738133086e-09 1.9283122858460053e-09 1.5009892426401923e-10 ;
	setAttr ".sp" -type "double3" -4.029018738133086e-09 1.9283122858460053e-09 1.5009892426401923e-10 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "upperArmLFT_FK_ctrlShape" -p "upperArmLFT_FK_ctrl";
	rename -uid "F3B10A76-4983-B72E-40E8-F3BD42366041";
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
	rename -uid "30F49D79-4C71-71A2-BB8B-ABBA65C0BEBB";
	setAttr ".rp" -type "double3" -4.029018738133086e-09 1.9283122858460048e-09 1.5009892426401928e-10 ;
	setAttr ".sp" -type "double3" -4.029018738133086e-09 1.9283122858460048e-09 1.5009892426401928e-10 ;
createNode nurbsCurve -n "upperArmLFT_FK_Gimbal_ctrlShape" -p "upperArmLFT_FK_Gimbal_ctrl";
	rename -uid "D724996E-45F2-EE5D-792F-B88609C956DE";
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
	rename -uid "D43ADEEC-4DD9-DB15-7FB4-A382E3B418D0";
createNode transform -n "lowerArmLFT_FK_ctrl" -p "lowerArmLFT_FK_Zro_grp";
	rename -uid "0C9C449A-4A72-701E-0A8B-01AB1FDE394A";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167833e-10 ;
	setAttr ".sp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167833e-10 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmLFT_FK_ctrlShape" -p "lowerArmLFT_FK_ctrl";
	rename -uid "F52C0443-440A-A8A5-64EA-4AB025E274CA";
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
	rename -uid "56012897-411E-2DB8-AAF0-94A25311C90D";
	setAttr ".rp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167836e-10 ;
	setAttr ".sp" -type "double3" -4.0289603736247711e-09 1.930581206106826e-09 -1.1750781804167836e-10 ;
createNode nurbsCurve -n "lowerArmLFT_FK_Gimbal_ctrlShape" -p "lowerArmLFT_FK_Gimbal_ctrl";
	rename -uid "F8B95E16-40F8-55A2-5DB4-A59652035CE8";
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
	rename -uid "6563268E-4D6E-2340-CBE0-169940C48707";
createNode transform -n "handLFT_FK_ctrl" -p "handLFT_FK_Zro_grp";
	rename -uid "6A52FE9E-48B5-D4EC-EBB5-16BD3672C79F";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
	setAttr ".sp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handLFT_FK_ctrlShape" -p "handLFT_FK_ctrl";
	rename -uid "D8621922-459A-120D-C00C-FDAB40EB20CE";
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
	rename -uid "A6A07659-4D9C-A1AC-825B-1EB76D6B0093";
	setAttr ".rp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
	setAttr ".sp" -type "double3" -4.1710487691222945e-09 1.9305739105432853e-09 1.4529749503169293e-08 ;
createNode nurbsCurve -n "handLFT_FK_Gimbal_ctrlShape" -p "handLFT_FK_Gimbal_ctrl";
	rename -uid "6690985C-4DBF-DC64-C1E0-698D8B229E5B";
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
createNode transform -n "toesLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "EA37E50B-4924-5308-D063-AEB385DB6A16";
createNode transform -n "toesLFT_FK_ctrl" -p "toesLFT_FK_Zro_grp";
	rename -uid "BDF42208-4500-91BB-9DB5-0EB73218511F";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 3.551952682345486e-07 2.0514950947787896e-08 2.3847975888064485e-08 ;
	setAttr ".sp" -type "double3" 3.551952682345486e-07 2.0514950947787896e-08 2.3847975888064485e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "toesLFT_FK_ctrlShape" -p "toesLFT_FK_ctrl";
	rename -uid "325D0E4B-47BF-42D0-9FE8-34A2A25FDEA3";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.8013809190361956 -1.2788720844251347 -0.78104857751220758
		-0.11703715556323878 -1.6714387578856686 0.5255731160490017
		3.2217542535787733 -1.1414091398302115 -0.32291860242772619
		7.0929416015415869 -1.053037891921458 -0.028520748845951131
		5.0412256213204483 0.84930924901644222 -4.9195154369219294
		0.45595482991456393 1.9020971034106844 -8.0799252333754641
		-3.9934768040881705 0.64311483973566808 -5.6067103741810076
		-6.2835974071747618 -1.3583238248999026 -1.0459632114761224
		-2.8013809190361956 -1.2788720844251347 -0.78104857751220758
		-0.11703715556323878 -1.6714387578856686 0.5255731160490017
		3.2217542535787733 -1.1414091398302115 -0.32291860242772619
		;
createNode transform -n "toesLFT_FK_Gimbal_ctrl" -p "toesLFT_FK_ctrl";
	rename -uid "87207FAE-4850-A69A-F30A-CCAC636012A9";
	setAttr ".rp" -type "double3" 3.5519526823454855e-07 2.0514950947787896e-08 2.3847975888064475e-08 ;
	setAttr ".sp" -type "double3" 3.5519526823454855e-07 2.0514950947787896e-08 2.3847975888064475e-08 ;
createNode nurbsCurve -n "toesLFT_FK_Gimbal_ctrlShape" -p "toesLFT_FK_Gimbal_ctrl";
	rename -uid "E0B6F007-4AF3-880E-D826-2D8E02412279";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.3811737279014764 -1.0870412686841215 -0.66389128730818014
		-0.09948152894946273 -1.4207229411255753 0.44673715221884774
		2.7384911688212474 -0.97019776577843742 -0.27448080848637085
		6.0290004145896381 -0.89508220505599678 -0.024242632941862075
		4.2850418314016716 0.72191286474121852 -4.1815881178064451
		0.38756165870666942 1.6167825409763243 -6.8679364447919475
		-3.3944552301956548 0.54664761685256047 -4.7657038144766597
		-5.3410577428192578 -1.1545752480876743 -0.88906872617750743
		-2.3811737279014764 -1.0870412686841215 -0.66389128730818014
		-0.09948152894946273 -1.4207229411255753 0.44673715221884774
		2.7384911688212474 -0.97019776577843742 -0.27448080848637085
		;
createNode transform -n "footLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "2B922308-43D7-DFE8-34EA-4DB5CDDFC82D";
createNode transform -n "footLFT_FK_ctrl" -p "footLFT_FK_Zro_grp";
	rename -uid "464D82B5-4169-AB38-9E43-CCA1EB50FCC3";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -2.1085844389029747e-07 2.9710690976484702e-08 -3.2627855343808004e-09 ;
	setAttr ".sp" -type "double3" -2.1085844389029747e-07 2.9710690976484702e-08 -3.2627855343808004e-09 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "footLFT_FK_ctrlShape" -p "footLFT_FK_ctrl";
	rename -uid "ABFAFB2B-4A9D-42F2-AD40-32945E8890B5";
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
createNode transform -n "footLFT_FK_Gimbal_ctrl" -p "footLFT_FK_ctrl";
	rename -uid "5303DDAC-4DD4-2ED6-96ED-14998477CA86";
	setAttr ".rp" -type "double3" -2.1085844389029744e-07 2.9710690976484702e-08 -3.2627855343807988e-09 ;
	setAttr ".sp" -type "double3" -2.1085844389029744e-07 2.9710690976484702e-08 -3.2627855343807988e-09 ;
createNode nurbsCurve -n "footLFT_FK_Gimbal_ctrlShape" -p "footLFT_FK_Gimbal_ctrl";
	rename -uid "9D1F7B82-4BE3-51E2-2A02-7A9269EB4A38";
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
createNode transform -n "lowerLegLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "4415BC16-483F-37F4-B0C3-EDA7EC52087D";
createNode transform -n "lowerLegLFT_FK_ctrl" -p "lowerLegLFT_FK_Zro_grp";
	rename -uid "2C990628-4ACE-F844-4CF3-228781E4D157";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376631e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerLegLFT_FK_ctrlShape" -p "lowerLegLFT_FK_ctrl";
	rename -uid "81BD09CE-408D-0B61-CC1C-818F125BA951";
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
createNode transform -n "lowerLegLFT_FK_Gimbal_ctrl" -p "lowerLegLFT_FK_ctrl";
	rename -uid "534AC83C-4ADA-8A91-7440-62B4E6974920";
	setAttr ".rp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
	setAttr ".sp" -type "double3" 1.598697630791713e-07 9.5466185703494727e-07 -9.3445004450376645e-08 ;
createNode nurbsCurve -n "lowerLegLFT_FK_Gimbal_ctrlShape" -p "lowerLegLFT_FK_Gimbal_ctrl";
	rename -uid "5E944450-4AE6-FDB1-8FB7-C6B6755679CD";
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
createNode transform -n "upperLegLFT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "B7FB64B2-493E-44E1-EE7A-54A138B44843";
createNode transform -n "upperLegLFT_FK_ctrl" -p "upperLegLFT_FK_Zro_grp";
	rename -uid "5BE7DCCD-4419-BEC3-FCFD-53AC4F686193";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.0789374222733081e-09 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "upperLegLFT_FK_ctrlShape" -p "upperLegLFT_FK_ctrl";
	rename -uid "BFE00A2D-4B8C-2AD0-DD14-258084F020D0";
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
createNode transform -n "upperLegLFT_FK_Gimbal_ctrl" -p "upperLegLFT_FK_ctrl";
	rename -uid "D24EBAEC-423B-B130-280C-EFA5EADDD31C";
	setAttr ".rp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
	setAttr ".sp" -type "double3" -1.5222328840497446e-07 4.3423579393537678e-07 5.078937422273309e-09 ;
createNode nurbsCurve -n "upperLegLFT_FK_Gimbal_ctrlShape" -p "upperLegLFT_FK_Gimbal_ctrl";
	rename -uid "3EBB763D-47BA-3DD9-FF76-A4A7EFE4A6C7";
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
createNode transform -n "shoulderRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "0604FA9E-49D8-A5A3-4083-418811901C18";
createNode transform -n "shoulderRGT_FK_ctrl" -p "shoulderRGT_FK_Zro_grp";
	rename -uid "2AEAC485-4211-F6BA-3CBB-3E8470729297";
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
	rename -uid "74184176-4FF0-D9B9-4A14-D7888BEF090D";
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
	rename -uid "3AF697EB-49B2-1C6C-196C-E7A1927065A4";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -1.2579117320701207e-05 0.00020498838092367557 2.2795634506863234e-07 ;
	setAttr ".sp" -type "double3" -1.2579117320701207e-05 0.00020498838092367557 2.2795634506863234e-07 ;
createNode nurbsCurve -n "shoulderRGT_FK_Gimbal_ctrlShape" -p "shoulderRGT_FK_Gimbal_ctrl";
	rename -uid "429227EB-4A9F-25F3-EA03-6097743FD94B";
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
	rename -uid "D136B94A-435A-3A4F-6430-DCBA3E9668B2";
createNode transform -n "shoulderLFT_FK_ctrl" -p "shoulderLFT_FK_Zro_grp";
	rename -uid "19436D1C-4B99-A5E3-66A2-86BFC1C4B572";
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
	rename -uid "4E69BFFB-4D2A-0B10-4C85-458772E239CA";
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
	rename -uid "2A83D830-4765-99E2-E58C-02BB1DADA041";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" 8.6215869296654414e-09 -5.266550590230743e-09 -5.8162966094266901e-09 ;
	setAttr ".sp" -type "double3" 8.6215869296654414e-09 -5.266550590230743e-09 -5.8162966094266901e-09 ;
createNode nurbsCurve -n "shoulderLFT_FK_Gimbal_ctrlShape" -p "shoulderLFT_FK_Gimbal_ctrl";
	rename -uid "6B03350F-4D04-8224-0BBD-9C9432DBD5A7";
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
	rename -uid "51FC8884-4B22-D03E-4511-9180E7E2A121";
createNode transform -n "lowerArmRGT_prop_ctrl" -p "lowerArmRGT_prop_Zro_grp";
	rename -uid "9C5BD46A-446E-D72E-6C0F-44AED87867ED";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 -1.4591127079228084e-14 0 ;
	setAttr ".sp" -type "double3" 0 -1.4591127079228084e-14 0 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmRGT_prop_ctrlShape" -p "lowerArmRGT_prop_ctrl";
	rename -uid "68473AB5-40B2-5EF1-2235-CF95762AA888";
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
	rename -uid "67BD8753-4EDA-E0F8-1054-E496762DE846";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 -1.4591127079228084e-14 0 ;
	setAttr ".sp" -type "double3" 0 -1.4591127079228084e-14 0 ;
createNode nurbsCurve -n "lowerArmRGT_prop_Gimbal_ctrlShape" -p "lowerArmRGT_prop_Gimbal_ctrl";
	rename -uid "EDD7D9E3-4054-59E1-B374-C5B5E778EBBD";
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
	rename -uid "EB95E574-4108-3AB2-9215-1480B5B7F8CB";
createNode transform -n "handRGT_prop_ctrl" -p "handRGT_prop_Zro_grp";
	rename -uid "CD977C2F-4AB0-3F9F-786F-09A9F4E417F2";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 1.0838178593707361e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707361e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handRGT_prop_ctrlShape" -p "handRGT_prop_ctrl";
	rename -uid "AF782C8B-4C21-E50B-939F-1290C1DF14E8";
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
	rename -uid "4E6CBBF0-47A0-CB36-10E6-9381517FB91E";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 1.0838178593707364e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707364e-06 6.610100112573357e-07 8.4711813295484447e-08 ;
createNode nurbsCurve -n "handRGT_prop_Gimbal_ctrlShape" -p "handRGT_prop_Gimbal_ctrl";
	rename -uid "5910BD8C-426A-B9B4-6E9B-2ABA21F26830";
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
	rename -uid "678E62F4-457C-3871-E105-C8A1CF540D96";
createNode transform -n "lowerArmLFT_prop_ctrl" -p "lowerArmLFT_prop_Zro_grp";
	rename -uid "9DA2D7BC-444F-B351-67DB-3B963C47D63B";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 0 9.1194544245175543e-16 ;
	setAttr ".sp" -type "double3" 0 0 9.1194544245175543e-16 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmLFT_prop_ctrlShape" -p "lowerArmLFT_prop_ctrl";
	rename -uid "D9E203EA-4A55-3AB0-5770-7A96B7C7F91B";
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
	rename -uid "83E8C81A-4DB8-22E2-472E-45BAF166C02E";
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" 0 0 9.1194544245175543e-16 ;
	setAttr ".sp" -type "double3" 0 0 9.1194544245175543e-16 ;
createNode nurbsCurve -n "lowerArmLFT_prop_Gimbal_ctrlShape" -p "lowerArmLFT_prop_Gimbal_ctrl";
	rename -uid "5F9C274E-46D5-0891-B163-5ABDADD77052";
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
	rename -uid "43D21894-4047-E4C2-6BE3-018E399BA00D";
createNode transform -n "handLFT_prop_ctrl" -p "handLFT_prop_Zro_grp";
	rename -uid "62434F51-4119-5FCC-A796-C390E15CD174";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.0838178593707357e-06 6.6101001125733549e-07 8.4711813181491256e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707357e-06 6.6101001125733549e-07 8.4711813181491256e-08 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handLFT_prop_ctrlShape" -p "handLFT_prop_ctrl";
	rename -uid "85647262-4605-7758-A845-3FBE603D0895";
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
	rename -uid "B61C7739-41C9-3F1E-58DC-DAA796994A38";
	setAttr ".rp" -type "double3" 1.0838178593707353e-06 6.6101001125733539e-07 8.4711813181491256e-08 ;
	setAttr ".sp" -type "double3" 1.0838178593707353e-06 6.6101001125733539e-07 8.4711813181491256e-08 ;
createNode nurbsCurve -n "handLFT_prop_Gimbal_ctrlShape" -p "handLFT_prop_Gimbal_ctrl";
	rename -uid "FF81FEFA-44D6-621E-88F8-0088B4008849";
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
	rename -uid "9D353319-43F1-4D0D-EED7-FDA065319F00";
createNode transform -n "upperArmRGT_FK_ctrl" -p "upperArmRGT_FK_Zro_grp";
	rename -uid "ED0B14AC-4097-40B3-F562-708BBB1CB17D";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	addAttr -ci true -sn "localWorld" -ln "localWorld" -min 0 -max 1 -at "double";
	setAttr ".rp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
	setAttr ".sp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
	setAttr -k on ".gimbal_controller";
	setAttr -k on ".localWorld";
createNode nurbsCurve -n "upperArmRGT_FK_ctrlShape" -p "upperArmRGT_FK_ctrl";
	rename -uid "77AA05A4-48D0-902A-D0A3-F19EAE6C2291";
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
	rename -uid "0865FAC3-4298-5C87-9B62-6EA407D75C61";
	setAttr ".rp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
	setAttr ".sp" -type "double3" 0.00017478231753142152 -1.3118636314053601e-05 -2.4005129075104061e-07 ;
createNode nurbsCurve -n "upperArmRGT_FK_Gimbal_ctrlShape" -p "upperArmRGT_FK_Gimbal_ctrl";
	rename -uid "70018891-4CC8-D64F-55B1-ABBB3E0CD2AC";
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
	rename -uid "3C60C834-4FA4-EA10-816B-02B50314C668";
createNode transform -n "lowerArmRGT_FK_ctrl" -p "lowerArmRGT_FK_Zro_grp";
	rename -uid "D3EB78B1-4382-8F50-F369-F6BF28406013";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerArmRGT_FK_ctrlShape" -p "lowerArmRGT_FK_ctrl";
	rename -uid "9B2A76EC-4041-9D32-2741-A9A89C95E7F7";
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
	rename -uid "3C93D9E8-4D2A-C4C3-4F80-CA8E40B63691";
	setAttr ".rp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 1.053243779851661e-05 1.0888508543495367e-06 ;
createNode nurbsCurve -n "lowerArmRGT_FK_Gimbal_ctrlShape" -p "lowerArmRGT_FK_Gimbal_ctrl";
	rename -uid "0BD1AE3E-43EA-7F90-EE0B-F59E2C83CC6C";
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
	rename -uid "F8D95BC9-4707-A462-90F1-2EBA9AF5D0E3";
createNode transform -n "handRGT_FK_ctrl" -p "handRGT_FK_Zro_grp";
	rename -uid "88B1BF0B-4994-D2E6-0AB9-CD920E036051";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "handRGT_FK_ctrlShape" -p "handRGT_FK_ctrl";
	rename -uid "4063656A-4AB3-73DB-FF6E-25A18415F443";
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
	rename -uid "737C4930-4018-409A-9421-58B27EB4B9CD";
	setAttr ".rp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
	setAttr ".sp" -type "double3" 0.00017478220554087339 2.361659351010784e-05 3.6496127738663754e-07 ;
createNode nurbsCurve -n "handRGT_FK_Gimbal_ctrlShape" -p "handRGT_FK_Gimbal_ctrl";
	rename -uid "0AEC8857-4D73-50C5-9B77-2B93A27F9454";
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
createNode transform -n "upperLegRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "5DA48D52-4A34-EAE9-8860-289AEA74B835";
createNode transform -n "upperLegRGT_FK_ctrl" -p "upperLegRGT_FK_Zro_grp";
	rename -uid "A4CAA5BF-4BE0-502B-1530-0299AEEB9738";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
	setAttr ".sp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "upperLegRGT_FK_ctrlShape" -p "upperLegRGT_FK_ctrl";
	rename -uid "849AA3D7-494F-013A-E90C-038D6409DE6B";
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
createNode transform -n "upperLegRGT_FK_Gimbal_ctrl" -p "upperLegRGT_FK_ctrl";
	rename -uid "C7759672-470F-9210-2CC8-869654DF6F56";
	setAttr ".rp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
	setAttr ".sp" -type "double3" 2.405294685595171e-05 2.577723629258088e-05 3.014970126169598e-07 ;
createNode nurbsCurve -n "upperLegRGT_FK_Gimbal_ctrlShape" -p "upperLegRGT_FK_Gimbal_ctrl";
	rename -uid "0ABB106F-44AA-B493-3E82-ADAB298974BC";
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
createNode transform -n "lowerLegRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "9D4377AA-49A9-29B3-1D2B-12B703CC0EFB";
	setAttr ".rp" -type "double3" 0 -1.139931803064694e-16 0 ;
	setAttr ".sp" -type "double3" 1.8238908849035105e-15 -1.139931803064694e-16 0 ;
createNode transform -n "lowerLegRGT_FK_ctrl" -p "lowerLegRGT_FK_Zro_grp";
	rename -uid "B62194D9-4B8E-4403-4443-D89EE9ECE432";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr ".sp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "lowerLegRGT_FK_ctrlShape" -p "lowerLegRGT_FK_ctrl";
	rename -uid "3A3E637F-49B2-8DDD-6DB0-8081E6CE1D35";
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
createNode transform -n "lowerLegRGT_FK_Gimbal_ctrl" -p "lowerLegRGT_FK_ctrl";
	rename -uid "6B1FDEE4-4EC1-03CC-2862-E19F57E87A4B";
	setAttr ".rp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
	setAttr ".sp" -type "double3" -4.5448144511414495e-06 -2.0514169914051596e-05 1.8268356565952132e-06 ;
createNode nurbsCurve -n "lowerLegRGT_FK_Gimbal_ctrlShape" -p "lowerLegRGT_FK_Gimbal_ctrl";
	rename -uid "3FE7F207-4540-A1CF-7717-C1B683F814B5";
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
createNode transform -n "footRGT_FK_Zro_grp" -p "TMP_GRP";
	rename -uid "8AAC72F1-4EC1-AD5B-2227-E9894A93D5DD";
createNode transform -n "footRGT_FK_ctrl" -p "footRGT_FK_Zro_grp";
	rename -uid "127554D3-449F-15E3-EB1F-7B98AF559F04";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
	setAttr ".sp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "footRGT_FK_ctrlShape" -p "footRGT_FK_ctrl";
	rename -uid "9A634B37-41A7-A7D7-E7D4-649B40986B17";
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
	rename -uid "541CB33B-420E-DC17-3B93-F5913264B72E";
	setAttr ".rp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
	setAttr ".sp" -type "double3" 1.1197432075701437e-05 -1.8084145699554467e-05 -8.6680080718816275e-06 ;
createNode nurbsCurve -n "footRGT_FK_Gimbal_ctrlShape" -p "footRGT_FK_Gimbal_ctrl";
	rename -uid "F0F79316-43B7-1167-C02F-FDAD1A244A18";
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
	rename -uid "1C14B52E-4399-8A16-CEA5-B6835A174113";
createNode transform -n "toesRGT_FK_ctrl" -p "toesRGT_FK_Zro_grp";
	rename -uid "79B1CB00-49C3-006E-384F-E7B617693DB5";
	addAttr -ci true -sn "gimbal_controller" -ln "gimbal_controller" -min 0 -max 1 
		-en "off:on" -at "enum";
	setAttr ".rp" -type "double3" 1.7181603029265618e-05 -2.352728918573141e-06 1.1684328747871983e-06 ;
	setAttr ".sp" -type "double3" 1.7181603029265618e-05 -2.352728918573141e-06 1.1684328747871983e-06 ;
	setAttr -k on ".gimbal_controller";
createNode nurbsCurve -n "toesRGT_FK_ctrlShape" -p "toesRGT_FK_ctrl";
	rename -uid "9E43C812-4A15-B7FB-C8BE-C58493307598";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.8013984558348 1.2788697522111758 0.78104976979194884
		0.11705469236132696 1.6714364256717038 -0.52557192376820205
		-3.2217367167803452 1.1414068076162529 0.32291979470984589
		-7.0929240647432801 1.0530355597074987 0.028521941129597491
		-5.0412080845202016 -0.8493115812303994 4.9195166292047663
		-0.45593729311307868 -1.9020994356246377 8.0799264256565078
		3.9934943408886747 -0.64311717194962459 5.6067115664602909
		6.2836149439734772 1.3583214926859442 1.0459644037544893
		2.8013984558348 1.2788697522111758 0.78104976979194884
		0.11705469236132696 1.6714364256717038 -0.52557192376820205
		-3.2217367167803452 1.1414068076162529 0.32291979470984589
		;
createNode transform -n "toesRGT_FK_Gimbal_ctrl" -p "toesRGT_FK_ctrl";
	rename -uid "706DF14E-4FAA-383C-8459-94AB9582426B";
	setAttr ".rp" -type "double3" 1.7181603029265618e-05 -2.352728918573141e-06 1.1684328747871983e-06 ;
	setAttr ".sp" -type "double3" 1.7181603029265618e-05 -2.352728918573141e-06 1.1684328747871983e-06 ;
createNode nurbsCurve -n "toesRGT_FK_Gimbal_ctrlShape" -p "toesRGT_FK_Gimbal_ctrl";
	rename -uid "953EE885-4158-6755-B59B-908C679EE9D8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.3811912647000346 1.0870389364701618 0.66389247958808772
		0.099499065747582313 1.4207206089116107 -0.44673595993804061
		-2.7384736320228393 0.97019543356447713 0.2744820007683002
		-6.028982877791333 0.89507987284203605 0.024243825225089083
		-4.2850242946017163 -0.72191519695517736 4.1815893100889818
		-0.38754412190566245 -1.6167848731902794 6.8679376370729628
		3.3944727669958286 -0.54664994906651865 4.7657050067561784
		5.3410752796179102 1.1545729158737148 0.88906991845624705
		2.3811912647000346 1.0870389364701618 0.66389247958808772
		0.099499065747582313 1.4207206089116107 -0.44673595993804061
		-2.7384736320228393 0.97019543356447713 0.2744820007683002
		;
createNode transform -n "TMP_Hand_ctrl" -p "TMP_GRP";
	rename -uid "FE515E1E-4BDF-76A6-6F62-6784190250CB";
createNode transform -n "pinky01LFT_Zro_grp" -p "TMP_Hand_ctrl";
	rename -uid "0879AABE-46DB-A56F-4FB9-4D881926B372";
createNode transform -n "pinky01LFT_ctrl" -p "pinky01LFT_Zro_grp";
	rename -uid "2A880329-4199-9196-099E-4FA9A6984917";
	setAttr ".rp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
createNode nurbsCurve -n "pinky01LFT_ctrlShape" -p "pinky01LFT_ctrl";
	rename -uid "5BFC451C-4B41-22C7-E0A1-DABE6766A9A6";
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
	rename -uid "05B02BAF-4334-5FA8-E0A1-25A73EE35A0F";
createNode transform -n "pinky02LFT_ctrl" -p "pinky02LFT_Zro_grp";
	rename -uid "E89FC7F5-4472-2A10-7EA7-48B6791FB141";
	setAttr ".rp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
createNode nurbsCurve -n "pinky02LFT_ctrlShape" -p "pinky02LFT_ctrl";
	rename -uid "09C94248-4BFF-33A3-BA94-93815C8C703B";
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
	rename -uid "DFBCA9E3-4428-4C3A-D6EE-F3AAD2FE346E";
createNode transform -n "pinky03LFT_ctrl" -p "pinky03LFT_Zro_grp";
	rename -uid "5A5DD400-4A38-8E35-8565-F68B9CF38DA1";
	setAttr ".rp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
createNode nurbsCurve -n "pinky03LFT_ctrlShape" -p "pinky03LFT_ctrl";
	rename -uid "66A450B9-41BB-F930-DCFD-618C1A3972CD";
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
	rename -uid "E77DF96D-402C-9E40-7B7F-3FA6272E9A9A";
createNode transform -n "ring01LFT_ctrl" -p "ring01LFT_Zro_grp";
	rename -uid "3E1B1103-4740-F1B3-195C-619607E9112A";
	setAttr ".rp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
createNode nurbsCurve -n "ring01LFT_ctrlShape" -p "ring01LFT_ctrl";
	rename -uid "4CAB4585-4F98-31CE-689A-6EA75BD4F6DA";
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
	rename -uid "B5C054DB-4D16-49F8-A801-E6992333298D";
createNode transform -n "ring02LFT_ctrl" -p "ring02LFT_Zro_grp";
	rename -uid "D69F0CA2-4D0F-868F-E5CB-688AD87D0030";
	setAttr ".rp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
createNode nurbsCurve -n "ring02LFT_ctrlShape" -p "ring02LFT_ctrl";
	rename -uid "1B8B63AA-4411-0593-BC5A-7F8E28705E4E";
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
	rename -uid "0CA52BC2-43A8-FBDC-2623-1097D795A551";
createNode transform -n "ring03LFT_ctrl" -p "ring03LFT_Zro_grp";
	rename -uid "E6655EDE-483A-71CC-E96A-0BB02928DAA4";
	setAttr ".rp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
createNode nurbsCurve -n "ring03LFT_ctrlShape" -p "ring03LFT_ctrl";
	rename -uid "5760BC59-4DAF-B385-2270-5299E1DBCF45";
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
	rename -uid "04D94ABB-4CE8-42F6-A319-039A7A1EFC12";
createNode transform -n "pinky01RGT_ctrl" -p "pinky01RGT_Zro_grp";
	rename -uid "3D47301F-405C-541F-9B6F-F48FF880962C";
	setAttr ".rp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
createNode nurbsCurve -n "pinky01RGT_ctrlShape" -p "pinky01RGT_ctrl";
	rename -uid "C35F5206-4AD6-3721-B25A-B6996603FBC0";
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
	rename -uid "975E7484-4B1B-9F00-9905-3CB27789BC56";
createNode transform -n "pinky02RGT_ctrl" -p "pinky02RGT_Zro_grp";
	rename -uid "D3493C57-42C6-A337-AEF5-5AA40F8912E6";
	setAttr ".rp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
createNode nurbsCurve -n "pinky02RGT_ctrlShape" -p "pinky02RGT_ctrl";
	rename -uid "9C11D116-4970-3EB7-B91F-8A9BE34E68E7";
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
	rename -uid "065B9FCC-4ED5-7C27-B872-9AA559388796";
createNode transform -n "pinky03RGT_ctrl" -p "pinky03RGT_Zro_grp";
	rename -uid "3A74A92F-4ADF-3793-829D-488CC15E17FE";
	setAttr ".rp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
createNode nurbsCurve -n "pinky03RGT_ctrlShape" -p "pinky03RGT_ctrl";
	rename -uid "9B14253E-409F-5D32-FF20-40B3F0B4B19B";
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
	rename -uid "C1C00ED1-4AC4-1701-C0D8-E4B534FA32D0";
createNode transform -n "ring01RGT_ctrl" -p "ring01RGT_Zro_grp";
	rename -uid "A2732F70-4630-FBD1-F2D3-1FABCE8D09FE";
	setAttr ".rp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581023e-09 2.3704890964184737e-09 2.1376199063230155e-08 ;
createNode nurbsCurve -n "ring01RGT_ctrlShape" -p "ring01RGT_ctrl";
	rename -uid "853AAAFC-45F5-F5B0-1FED-65826701F1FF";
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
	rename -uid "8AEEF81B-4B0D-118B-2123-D2AAD528945B";
createNode transform -n "ring02RGT_ctrl" -p "ring02RGT_Zro_grp";
	rename -uid "C4422635-464B-1813-CB48-16ABE802C1DF";
	setAttr ".rp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708351e-09 1.1073023951337703e-09 2.3646241928889774e-08 ;
createNode nurbsCurve -n "ring02RGT_ctrlShape" -p "ring02RGT_ctrl";
	rename -uid "ED02CA14-4861-4138-A3B4-F38257C789F8";
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
	rename -uid "C0E4811A-4EDB-1343-712D-FFB3ADCC8E28";
createNode transform -n "ring03RGT_ctrl" -p "ring03RGT_Zro_grp";
	rename -uid "1468D9A6-495F-8E15-3AC4-068D1A88F139";
	setAttr ".rp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885375e-09 1.1072659173160717e-09 2.5430766408906243e-08 ;
createNode nurbsCurve -n "ring03RGT_ctrlShape" -p "ring03RGT_ctrl";
	rename -uid "54103443-4E79-60A9-FDC4-52AA4ABA6193";
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
	rename -uid "A4EAB1B9-4E9F-A54F-ACA5-909DD926FB9D";
createNode transform -n "index01RGT_ctrl" -p "index01RGT_Zro_grp";
	rename -uid "D6E7E9E3-451C-B887-E529-5A820843CCC7";
	setAttr ".rp" -type "double3" -0.00023490122594700306 -5.3593224903946879e-05 1.8251019008019369e-06 ;
	setAttr ".sp" -type "double3" -0.00023490122594700306 -5.3593224903946879e-05 1.8251019008019369e-06 ;
createNode nurbsCurve -n "index01RGT_ctrlShape" -p "index01RGT_ctrl";
	rename -uid "EE2EBA2E-4EE2-F020-0B26-14AAE4EB3C3C";
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
	rename -uid "89BE8F7A-4384-87FE-0BAF-93B2CBCCD823";
	setAttr ".rp" -type "double3" 0 -7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" 0 -7.2955635396140418e-15 0 ;
createNode transform -n "index02RGT_ctrl" -p "index02RGT_Zro_grp";
	rename -uid "C71CDB09-40AC-5535-77FA-4F94079D0E05";
	setAttr ".rp" -type "double3" 0.00012120864448241608 4.9428310970557256e-05 2.8805443260338447e-06 ;
	setAttr ".sp" -type "double3" 0.00012120864448241608 4.9428310970557256e-05 2.8805443260338447e-06 ;
createNode nurbsCurve -n "index02RGT_ctrlShape" -p "index02RGT_ctrl";
	rename -uid "DB14865A-46E3-15C0-0BA7-E0B53C36EE8A";
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
	rename -uid "EC068E97-44DC-B042-31BE-9C89CFF3F0F4";
createNode transform -n "index03RGT_ctrl" -p "index03RGT_Zro_grp";
	rename -uid "1D78E931-4EAA-781D-C337-6BB8AB81C18F";
	setAttr ".rp" -type "double3" -0.00013322877243714874 -8.7433801653780712e-05 -6.0350929155347919e-06 ;
	setAttr ".sp" -type "double3" -0.00013322877243714874 -8.7433801653780712e-05 -6.0350929155347919e-06 ;
createNode nurbsCurve -n "index03RGT_ctrlShape" -p "index03RGT_ctrl";
	rename -uid "410955BA-49C9-E9F1-0BA3-1097392DDE0D";
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
	rename -uid "0DFAAEB0-4B10-B5AB-3B82-069A67729A0D";
createNode transform -n "middle01RGT_ctrl" -p "middle01RGT_Zro_grp";
	rename -uid "2B2A9F95-464F-E9B6-F06B-17BB1E8239D3";
	setAttr ".rp" -type "double3" 0.00023128282937934106 3.7202749990716172e-05 -1.2259477520336723e-06 ;
	setAttr ".sp" -type "double3" 0.00023128282937934106 3.7202749990716172e-05 -1.2259477520336723e-06 ;
createNode nurbsCurve -n "middle01RGT_ctrlShape" -p "middle01RGT_ctrl";
	rename -uid "57C11F3A-40D1-3E13-E0A2-2FA02E056466";
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
	rename -uid "67F7F6C9-47B2-A03E-6B29-2EA90AE1A41C";
	setAttr ".sp" -type "double3" 0 0 1.139931803064694e-16 ;
createNode transform -n "middle02RGT_ctrl" -p "middle02RGT_Zro_grp";
	rename -uid "0CAA52CC-4121-D6EA-D923-8DB6C6A031AF";
	setAttr ".rp" -type "double3" 0.00013552500442800012 4.0882473702030109e-05 9.0693690630569376e-07 ;
	setAttr ".sp" -type "double3" 0.00013552500442800012 4.0882473702030109e-05 9.0693690630569376e-07 ;
createNode nurbsCurve -n "middle02RGT_ctrlShape" -p "middle02RGT_ctrl";
	rename -uid "810BB8BE-40C1-06DE-1082-D89F1B73C0BD";
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
	rename -uid "4A7D9C10-42F6-9423-E655-028DBC8C5CF0";
createNode transform -n "middle03RGT_ctrl" -p "middle03RGT_Zro_grp";
	rename -uid "7D844626-43E1-C497-7CB2-F78721773CE6";
	setAttr ".rp" -type "double3" 0.00015678857867411686 3.9471195304878039e-05 8.6916177143620969e-07 ;
	setAttr ".sp" -type "double3" 0.00015678857867411686 3.9471195304878039e-05 8.6916177143620969e-07 ;
createNode nurbsCurve -n "middle03RGT_ctrlShape" -p "middle03RGT_ctrl";
	rename -uid "93EB554F-4687-887A-5623-24B790FE7B01";
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
	rename -uid "0975D626-47A2-55A2-2AAA-54A72B18E448";
createNode transform -n "index01LFT_ctrl" -p "index01LFT_Zro_grp";
	rename -uid "81371226-4185-F310-B029-AD924840AD2B";
	setAttr ".rp" -type "double3" -3.9950505942926481e-09 -1.1811334981546642e-09 2.1372413805684899e-08 ;
	setAttr ".sp" -type "double3" -3.9950505942926481e-09 -1.1811334981546642e-09 2.1372413805684899e-08 ;
createNode nurbsCurve -n "index01LFT_ctrlShape" -p "index01LFT_ctrl";
	rename -uid "B4C96CAF-4260-DE48-5135-8586816776B8";
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
	rename -uid "1E9350CA-4539-2815-E32B-D299AD2C6365";
createNode transform -n "index02LFT_ctrl" -p "index02LFT_Zro_grp";
	rename -uid "F3EC6FE5-4B41-AC04-00F9-B48ED9FADCF5";
	setAttr ".rp" -type "double3" -3.7897534362879109e-09 -1.9532922954056448e-09 2.3670962945943756e-08 ;
	setAttr ".sp" -type "double3" -3.7897534362879109e-09 -1.9532922954056448e-09 2.3670962945943756e-08 ;
createNode nurbsCurve -n "index02LFT_ctrlShape" -p "index02LFT_ctrl";
	rename -uid "1292EB81-4C9A-4C28-0703-6E9F182339C7";
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
	rename -uid "5D76C40C-4943-180B-BEBA-BABBD43037F9";
createNode transform -n "index03LFT_ctrl" -p "index03LFT_Zro_grp";
	rename -uid "DEDB0FDC-4DB1-BE17-F02A-DAAB192BE6E6";
	setAttr ".rp" -type "double3" -3.4316579955094944e-09 -3.7519414424075356e-09 2.4841952076989769e-08 ;
	setAttr ".sp" -type "double3" -3.4316579955094944e-09 -3.7519414424075356e-09 2.4841952076989769e-08 ;
createNode nurbsCurve -n "index03LFT_ctrlShape" -p "index03LFT_ctrl";
	rename -uid "107B59AA-49F5-B87B-FAF3-7299EB33C622";
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
	rename -uid "FCB55BAD-4BD0-5C93-3EA6-13BD4A690CD9";
createNode transform -n "middle01LFT_ctrl" -p "middle01LFT_Zro_grp";
	rename -uid "5E0BDC6B-460B-3D27-111E-62A053A5B0FC";
	setAttr ".rp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
	setAttr ".sp" -type "double3" -4.6139332493581072e-09 2.3704890964184737e-09 2.1376199063230152e-08 ;
createNode nurbsCurve -n "middle01LFT_ctrlShape" -p "middle01LFT_ctrl";
	rename -uid "B148913D-4863-6CB0-97AD-6E8D7D2D6AF0";
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
	rename -uid "E904D705-4C64-A168-CD80-C4B2B5BBB34F";
createNode transform -n "middle02LFT_ctrl" -p "middle02LFT_Zro_grp";
	rename -uid "4D8E147F-4D8A-D6E5-62A4-DA8BF4CFCC49";
	setAttr ".rp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
	setAttr ".sp" -type "double3" -4.6575315370708393e-09 1.1073023951337703e-09 2.3646241928889777e-08 ;
createNode nurbsCurve -n "middle02LFT_ctrlShape" -p "middle02LFT_ctrl";
	rename -uid "DEDDCD43-4DF6-A2B8-802D-88917E8DE5E7";
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
	rename -uid "304E2EC0-4AA1-42CF-7289-9E8EBCF439D2";
createNode transform -n "middle03LFT_ctrl" -p "middle03LFT_Zro_grp";
	rename -uid "B58C59AE-4BE4-B562-3811-3E9213A17B9D";
	setAttr ".rp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
	setAttr ".sp" -type "double3" -4.6760768595885384e-09 1.1072659173160719e-09 2.5430766408906247e-08 ;
createNode nurbsCurve -n "middle03LFT_ctrlShape" -p "middle03LFT_ctrl";
	rename -uid "DD0353AD-4521-36CD-6C22-E4B9FDCEED18";
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
	rename -uid "94CDD7CB-4679-53AC-9E05-3CA9333FB9DE";
createNode transform -n "thumb01LFT_ctrl" -p "thumb01LFT_Zro_grp";
	rename -uid "8D7E8245-43DE-78C5-2CE9-A8AE74A0E804";
	setAttr ".rp" -type "double3" -2.9439203906321374e-09 5.3528230229434663e-09 1.6710627530155718e-08 ;
	setAttr ".sp" -type "double3" -2.9439203906321374e-09 5.3528230229434663e-09 1.6710627530155718e-08 ;
createNode nurbsCurve -n "thumb01LFT_ctrlShape" -p "thumb01LFT_ctrl";
	rename -uid "A11383BD-4CE6-237B-9062-8C8ECEFDB9B9";
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
	rename -uid "7F3ACA62-4127-B93C-017D-28B304AF4298";
createNode transform -n "thumb02LFT_ctrl" -p "thumb02LFT_Zro_grp";
	rename -uid "85B083A2-472B-5778-6932-6BAE3A5A81B1";
	setAttr ".rp" -type "double3" -1.9689266880710376e-09 3.0822041497437502e-09 1.9249309745344834e-08 ;
	setAttr ".sp" -type "double3" -1.9689266880710376e-09 3.0822041497437502e-09 1.9249309745344834e-08 ;
createNode nurbsCurve -n "thumb02LFT_ctrlShape" -p "thumb02LFT_ctrl";
	rename -uid "72B60B3F-4519-1FFA-F885-7A89BE6AF575";
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
	rename -uid "1880589C-4EBF-3917-2997-B389D41570ED";
createNode transform -n "thumb03LFT_ctrl" -p "thumb03LFT_Zro_grp";
	rename -uid "2E190C34-4E16-870C-BF3E-1BBD9BE99DB0";
	setAttr ".rp" -type "double3" -1.4237729981369182e-09 3.082281665106359e-09 2.0678795283726441e-08 ;
	setAttr ".sp" -type "double3" -1.4237729981369182e-09 3.082281665106359e-09 2.0678795283726441e-08 ;
createNode nurbsCurve -n "thumb03LFT_ctrlShape" -p "thumb03LFT_ctrl";
	rename -uid "10B3ECF3-4F37-A4FB-47B7-D8A1B0A66563";
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
	rename -uid "2DEC57AE-4BFD-ABCC-D57A-8F8C93FDA872";
	setAttr ".sp" -type "double3" 0 0 -3.6477817698070209e-15 ;
createNode transform -n "thumb01RGT_ctrl" -p "thumb01RGT_Zro_grp";
	rename -uid "A476EC75-4397-C408-E135-F0995B078197";
	setAttr ".rp" -type "double3" -0.00021786125293844945 -0.00011590463622923497 6.1617136254591963e-05 ;
	setAttr ".sp" -type "double3" -0.00021786125293844945 -0.00011590463622923497 6.1617136254591963e-05 ;
createNode nurbsCurve -n "thumb01RGT_ctrlShape" -p "thumb01RGT_ctrl";
	rename -uid "FB62D9EA-475D-E410-0B53-3E835E8B932F";
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
	rename -uid "256B11D2-46BE-14E7-4244-E0B8D6C93D84";
	setAttr ".sp" -type "double3" 0 -3.6477817698070209e-15 0 ;
createNode transform -n "thumb02RGT_ctrl" -p "thumb02RGT_Zro_grp";
	rename -uid "D00A7C8A-4B25-9CBA-E861-F9B2E8977AEE";
	setAttr ".rp" -type "double3" -1.1832315067075544e-05 1.9991630574129766e-05 -9.6300105969357936e-06 ;
	setAttr ".sp" -type "double3" -1.1832315067075544e-05 1.9991630574129766e-05 -9.6300105969357936e-06 ;
createNode nurbsCurve -n "thumb02RGT_ctrlShape" -p "thumb02RGT_ctrl";
	rename -uid "9F60A8E1-4AAE-F48E-32A3-55AB534FD048";
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
	rename -uid "DE148F19-4949-2CF6-26D8-BE8CF9F110C2";
	setAttr ".rp" -type "double3" 0 7.2955635396140418e-15 0 ;
	setAttr ".sp" -type "double3" 0 7.2955635396140418e-15 0 ;
createNode transform -n "thumb03RGT_ctrl" -p "thumb03RGT_Zro_grp";
	rename -uid "010E7C98-4435-FEDA-D8EC-3DA824FF00F1";
	setAttr ".rp" -type "double3" 6.9766701120598681e-05 4.7022710770836411e-05 -1.8964515567285252e-05 ;
	setAttr ".sp" -type "double3" 6.9766701120598681e-05 4.7022710770836411e-05 -1.8964515567285252e-05 ;
createNode nurbsCurve -n "thumb03RGT_ctrlShape" -p "thumb03RGT_ctrl";
	rename -uid "B64C6C12-4362-C628-B7C1-A4A6ECA38BB7";
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
	rename -uid "997FE7E7-4B64-E743-85C1-F0B6D5933960";
	setAttr ".v" no;
createNode transform -n "ankleRGT_IK_Zro_grp" -p "TMP_NULL_GRP";
	rename -uid "43CC2E68-4FF9-BA40-DE83-1FB5EFFCCD34";
createNode transform -n "fingerRGT_Zro_grp" -p "TMP_NULL_GRP";
	rename -uid "7B0EEF82-4897-E603-2EF4-1CB641E55207";
createNode transform -n "fingerLFT_Zro_grp" -p "TMP_NULL_GRP";
	rename -uid "2F106D07-4E9B-D2E3-DB9D-E3B6AA1717C2";
createNode transform -n "ankleLFT_IK_Zro_grp" -p "TMP_NULL_GRP";
	rename -uid "7B28B0FB-4A2F-7806-529E-34831963C40F";
createNode transform -n "TMP_FOOT_IK_GRP" -p "TMP_GRP";
	rename -uid "34E80ABD-4C03-BB30-BD4C-1482F442A071";
createNode transform -n "footLFT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "0E9D0608-4483-6CE6-E0DD-14AE2FC9E5DF";
createNode transform -n "footLFT_IK_ctrl" -p "footLFT_IK_Zro_grp";
	rename -uid "8D9B24A3-419B-78F3-A553-30BC4B4E1B6E";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "long";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "footLFT_IK_ctrlShape" -p "footLFT_IK_ctrl";
	rename -uid "458172C5-45C2-0625-8EFD-94BC5950C6C6";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-4.0960694513635634 -0.23477914568496866 11.322544424071589
		4.9260926068219639 -0.23477914568496866 11.322544424071589
		4.9260926068219648 -0.23477914568496866 -9.1831269598373275
		-4.0960694513635634 -0.23477914568496866 -9.1831269598373275
		-4.0960694513635634 -0.23477914568496866 11.322544424071589
		;
createNode transform -n "footRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "5EC54C6F-4323-5EFD-DE51-C1A596B571AD";
createNode transform -n "footRGT_IK_ctrl" -p "footRGT_IK_Zro_grp";
	rename -uid "3E5C12F4-4D81-2615-7722-93B7AC5AFA9C";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "long";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "footRGT_IK_ctrlShape" -p "footRGT_IK_ctrl";
	rename -uid "56D51C78-40C9-64E6-8BDB-C89DCC974A48";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-4.9249185169061906 -0.23477914568496866 11.322544424071589
		4.0972435412793358 -0.23477914568496866 11.322544424071589
		4.0972435412793375 -0.23477914568496866 -9.1831269598373275
		-4.9249185169061906 -0.23477914568496866 -9.1831269598373275
		-4.9249185169061906 -0.23477914568496866 11.322544424071589
		;
createNode transform -n "ballRollLFT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "19045265-4291-DCC1-2516-8395389D1C56";
	setAttr ".rp" -type "double3" -1.4591127079228084e-14 -8.0882035414427014e-11 0.38628396632014506 ;
	setAttr ".sp" -type "double3" -1.4591127079228084e-14 -8.0882035414427014e-11 0.38628396632014506 ;
createNode transform -n "ballRollLFT_IK_ctrl" -p "ballRollLFT_IK_Zro_grp";
	rename -uid "2A1D0525-41B6-1BBC-74E3-A2A168C20DA1";
	setAttr ".rp" -type "double3" -1.4591127079228084e-14 -8.0881055785533766e-11 0.38628396632014522 ;
	setAttr ".sp" -type "double3" -1.4591127079228084e-14 -8.0881055785533766e-11 0.38628396632014522 ;
createNode nurbsCurve -n "ballRollLFT_IK_ctrlShape" -p "ballRollLFT_IK_ctrl";
	rename -uid "713E6937-4C8C-B0F4-F981-82801E7A1D84";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		4.3119453842682412e-10 4.9653157993342578 -6.517158080122992
		4.3119454625916557e-10 5.0486107421997355 -7.1218317321503735
		4.3119456192280846e-10 4.7485088337059471 -7.6627892455621716
		4.311945775857576e-10 4.1372790623956703 -7.7581535652119964
		4.3119458541671208e-10 3.598318279628161 -7.4716408297154251
		4.3119457758437041e-10 3.5150233367626909 -6.8669671776880552
		4.3119456192072769e-10 3.815125245256481 -6.3260096642762615
		4.3119454625777849e-10 4.4263550165667551 -6.2306453446264314
		4.3119453842682412e-10 4.9653157993342578 -6.517158080122992
		0.54346466473582489 4.7374828793832418 -6.6762385383883984
		0.8151969968881394 4.2818170394812096 -6.9943994549192086
		0.54346466473582489 3.8261511995791766 -7.3125603714500187
		4.3119458541671208e-10 3.598318279628161 -7.4716408297154251
		-0.54346466387343684 3.8261511995791766 -7.3125603714500187
		-0.81519699602575213 4.2818170394812096 -6.9943994549192086
		-0.54346466387343684 4.7374828793832418 -6.6762385383883984
		4.3119453842682412e-10 4.9653157993342578 -6.517158080122992
		;
createNode transform -n "ballRollRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "82DA65B2-4371-009B-3064-60A78BB72E2C";
	setAttr -av ".v";
	setAttr ".rp" -type "double3" 1.1881178110669878e-06 3.02971286574604e-08 0.38628357138129193 ;
	setAttr ".sp" -type "double3" 1.1881178110669878e-06 3.02971286574604e-08 0.38628357138129193 ;
createNode transform -n "ballRollRGT_IK_ctrl" -p "ballRollRGT_IK_Zro_grp";
	rename -uid "2E9B8643-49C5-C624-C9DF-659394EDA845";
	setAttr ".rp" -type "double3" 1.1881178128908787e-06 3.0297127633302924e-08 0.38628357138129182 ;
	setAttr ".sp" -type "double3" 1.1881178128908787e-06 3.0297127633302924e-08 0.38628357138129182 ;
createNode nurbsCurve -n "ballRollRGT_IK_ctrlShape" -p "ballRollRGT_IK_ctrl";
	rename -uid "2EE5F3C3-4DCF-1C2E-0263-C3827046DFA0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 22;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		1.1881178112849991e-06 -4.9652233445793961 7.2898090632860839
		1.1881178113175258e-06 -5.0485066603770896 7.8944845292615984
		1.1881178113825773e-06 -4.7483944996139602 8.4354365924177674
		1.1881178114476273e-06 -4.1371631439451608 8.5307894097106995
		1.1881178114801515e-06 -3.5982080699315051 8.2442663839597348
		1.1881178114476248e-06 -3.5149247541338178 7.639590917984231
		1.1881178113825735e-06 -3.8150369148969516 7.098638854828069
		1.188117811317523e-06 -4.426268270565747 7.0032860375351307
		1.1881178112849991e-06 -4.9652233445793961 7.2898090632860839
		-0.54346347618682012 -4.7373874654714152 7.4488852833983605
		-0.81519580833913441 -4.2817157072554499 7.7670377236229085
		-0.54346347618681989 -3.8260439490394855 8.085190163847459
		1.1881178114801515e-06 -3.5982080699315051 8.2442663839597348
		0.54346585242244194 -3.8260439490394855 8.085190163847459
		0.81519818457475746 -4.2817157072554499 7.7670377236229085
		0.54346585242244172 -4.7373874654714152 7.4488852833983605
		1.1881178112849991e-06 -4.9652233445793961 7.2898090632860839
		;
createNode transform -n "toesRollLFT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "707C7548-4D00-EC6E-D8C9-28A9B5946CA0";
	setAttr ".rp" -type "double3" -1.2767236194324574e-14 7.1245737691543378e-16 1.2974012902154537 ;
	setAttr ".sp" -type "double3" -1.2767236194324574e-14 7.1245737691543378e-16 1.2974012902154537 ;
createNode transform -n "toesRollLFT_IK_ctrl" -p "toesRollLFT_IK_Zro_grp";
	rename -uid "255C4E3C-4FD4-6D7B-1C9E-30B399ED82E8";
	setAttr ".rp" -type "double3" -1.0943345309421062e-14 2.493600819204018e-15 1.2974012902154537 ;
	setAttr ".sp" -type "double3" -1.0943345309421062e-14 2.493600819204018e-15 1.2974012902154537 ;
	setAttr ".hdl" -type "double3" -2.1316282072803005e-16 4.8572257327350599e-17 0.025271771183207087 ;
createNode nurbsCurve -n "toesRollLFT_IK_ctrlShape" -p "toesRollLFT_IK_ctrl";
	rename -uid "7EC71E07-4E73-5175-661E-628CBC183C0E";
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
createNode transform -n "toesRollRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "FAE22C04-457C-2138-274E-6086CB44B81E";
	setAttr ".rp" -type "double3" 1.1881178101550423e-06 3.0378010915517757e-08 1.2974008952765999 ;
	setAttr ".sp" -type "double3" 1.1881178101550423e-06 3.0378010915517757e-08 1.2974008952765999 ;
createNode transform -n "toesRollRGT_IK_ctrl" -p "toesRollRGT_IK_Zro_grp";
	rename -uid "27376607-4092-708D-D6D9-71B311BC43EE";
	setAttr ".rp" -type "double3" 1.1881178101550423e-06 3.0378008956259975e-08 1.2974008952765999 ;
	setAttr ".sp" -type "double3" 1.1881178101550423e-06 3.0378008956259975e-08 1.2974008952765999 ;
	setAttr ".hdl" -type "double3" 2.3143064264985471e-08 5.9172601193924201e-10 0.025271763490287074 ;
createNode nurbsCurve -n "toesRollRGT_IK_ctrlshape" -p "toesRollRGT_IK_ctrl";
	rename -uid "2DA1E161-4C99-CE7B-B7D5-39AC9BF6923E";
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
createNode transform -n "heelRollLFT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "38CADFD5-462A-B68B-9A98-B8BE293A8760";
	setAttr ".rp" -type "double3" 1.7804609897635273e-14 -2.9980837649287912e-05 -1.966978232882344 ;
	setAttr ".sp" -type "double3" 1.7804609897635273e-14 -2.9980837649287912e-05 -1.966978232882344 ;
createNode transform -n "heelRollLFT_IK_ctrl" -p "heelRollLFT_IK_Zro_grp";
	rename -uid "D11CEC96-48C1-BBAC-064E-44841DAF2427";
	setAttr ".rp" -type "double3" 1.9628500782578596e-14 -2.9980837649287912e-05 -1.966978232882344 ;
	setAttr ".sp" -type "double3" 1.9628500782578596e-14 -2.9980837649287912e-05 -1.966978232882344 ;
	setAttr ".hdl" -type "double3" 3.8233889867979948e-16 -5.8398960650629661e-07 -0.038314301210149608 ;
createNode nurbsCurve -n "heelRollLFT_IK_ctrlShape" -p "heelRollLFT_IK_ctrl";
	rename -uid "293B61D2-410C-C207-E234-0F97BB002948";
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
createNode transform -n "heelRollRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "465629B2-449E-0AC4-C234-8484C33C39C8";
	setAttr ".rp" -type "double3" 1.1881177855325323e-06 -2.9950459638372393e-05 -1.9669786278212016 ;
	setAttr ".sp" -type "double3" 1.1881177855325323e-06 -2.9950459638372393e-05 -1.9669786278212016 ;
createNode transform -n "heelRollRGT_IK_ctrl" -p "heelRollRGT_IK_Zro_grp";
	rename -uid "110CE710-4BB8-ED34-E74B-1094A60C2EA7";
	setAttr ".rp" -type "double3" 1.1881177827966961e-06 -2.9950459638372393e-05 -1.966978627821202 ;
	setAttr ".sp" -type "double3" 1.1881177827966961e-06 -2.9950459638372393e-05 -1.966978627821202 ;
	setAttr ".hdl" -type "double3" 2.3143063732078749e-08 -5.8339788045619345e-07 -0.038314308903069694 ;
createNode nurbsCurve -n "heelRollRGT_IK_ctrlShape" -p "heelRollRGT_IK_ctrl";
	rename -uid "7546D20E-4880-F371-58E6-6C8E4036983E";
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
createNode transform -n "footInLFT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "420B6E74-4AE8-4506-CA3E-F29496CFE8E0";
	setAttr ".rp" -type "double3" 0.5782442789967831 5.5414489490621868e-11 1.0082424592654509e-15 ;
	setAttr ".sp" -type "double3" 0.5782442789967831 5.5414489490621868e-11 1.0082424592654509e-15 ;
createNode transform -n "footInLFT_IK_ctrl" -p "footInLFT_IK_Zro_grp";
	rename -uid "97A02F01-4B3E-F95D-0544-11BE415FBB60";
	setAttr ".rp" -type "double3" 0.57824427899678266 5.5414489490621868e-11 1.0652390494199298e-15 ;
	setAttr ".sp" -type "double3" 0.57824427899678266 5.5414489490621868e-11 1.0652390494199298e-15 ;
	setAttr ".hdl" -type "double3" 0.011263482792111677 1.0794056620744286e-12 2.0749538107740686e-17 ;
createNode nurbsCurve -n "footInLFT_IK_ctrlShape" -p "footInLFT_IK_ctrl";
	rename -uid "E042AF84-42BE-CD5E-5BE1-B1A3CC3911C9";
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
createNode transform -n "footInRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "26654CAD-4EA0-2E35-7D9D-B492C6D23021";
	setAttr ".rp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
	setAttr ".sp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
createNode transform -n "footInRGT_IK_ctrl" -p "footInRGT_IK_Zro_grp";
	rename -uid "E9D5EED6-4A7E-186D-7CFC-B2A319309B79";
	setAttr ".rp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
	setAttr ".sp" -type "double3" -0.57824309087896997 3.0433426651808789e-08 -3.9493885454013262e-07 ;
	setAttr ".hdl" -type "double3" -0.011263459649047363 5.9280548005136158e-10 -7.6929200229473111e-09 ;
createNode nurbsCurve -n "footInRGT_IK_ctrlShape" -p "footInRGT_IK_ctrl";
	rename -uid "AC407C02-4EAF-EF83-5D9B-6FA3EBF42849";
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
createNode transform -n "footOutLFT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "197A1D3F-4A71-1F8E-0CB0-EF8B1B4BF070";
	setAttr ".rp" -type "double3" -0.41504239050203406 -1.3009206668331607e-10 3.645632475272038e-05 ;
	setAttr ".sp" -type "double3" -0.41504239050203406 -1.3009206668331607e-10 3.645632475272038e-05 ;
createNode transform -n "footOutLFT_IK_ctrl" -p "footOutLFT_IK_Zro_grp";
	rename -uid "180DDA6C-4621-F971-45BD-F2BAC79A8545";
	setAttr ".rp" -type "double3" -0.41504239050203356 -1.3009220917479147e-10 3.6456324751829809e-05 ;
	setAttr ".sp" -type "double3" -0.41504239050203356 -1.3009220917479147e-10 3.6456324751829809e-05 ;
	setAttr ".hdl" -type "double3" -0.0080845120189119261 -2.5340352038938364e-12 7.1012407977175118e-07 ;
createNode nurbsCurve -n "footOutLFT_IK_ctrlShape" -p "footOutLFT_IK_ctrl";
	rename -uid "8E2C409C-42CE-39F0-3A09-DA8E4A64E42A";
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
createNode transform -n "footOutRGT_IK_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "50C04DF4-4DF7-B7BA-E5E5-BAAA8923C06F";
	setAttr ".rp" -type "double3" 0.4150435786198432 3.024792013933845e-08 3.6061385896740926e-05 ;
	setAttr ".sp" -type "double3" 0.4150435786198432 3.024792013933845e-08 3.6061385896740926e-05 ;
createNode transform -n "footOutRGT_IK_ctrl" -p "footOutRGT_IK_Zro_grp";
	rename -uid "A00D5EF6-4C6B-A7C8-0472-9EB68C1BCC22";
	setAttr ".rp" -type "double3" 0.4150435786198432 3.0247920196335039e-08 3.6061385895850355e-05 ;
	setAttr ".sp" -type "double3" 0.4150435786198432 3.0247920196335039e-08 3.6061385895850355e-05 ;
	setAttr ".hdl" -type "double3" 0.0080845351619761811 5.8919204392246585e-10 7.0243115972076775e-07 ;
createNode nurbsCurve -n "footOutRGT_IK_ctrlShape" -p "footOutRGT_IK_ctrl";
	rename -uid "378ED230-4ED5-A0D4-B322-FD99D06DE970";
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
createNode transform -n "legRGT_pov_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "434245D6-49E8-42C7-B82A-47AC963EF93E";
createNode transform -n "legRGT_pov_ctrl" -p "legRGT_pov_Zro_grp";
	rename -uid "3E4A2AA6-4256-8AF1-B008-B890DE78D3D6";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "legRGT_pov_ctrlShape" -p "legRGT_pov_ctrl";
	rename -uid "06AF6B66-4695-42FE-8049-05AF232AD01C";
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
createNode transform -n "legLFT_pov_Zro_grp" -p "TMP_FOOT_IK_GRP";
	rename -uid "D75C8A64-495F-A882-82FB-B883DB4FDD72";
createNode transform -n "legLFT_pov_ctrl" -p "legLFT_pov_Zro_grp";
	rename -uid "837DD42F-4416-D434-CCF7-AA9BBDA52EA6";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "legLFT_pov_ctrlShape" -p "legLFT_pov_ctrl";
	rename -uid "4531991E-42E6-6989-FF22-699CD67DF3AA";
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
createNode transform -n "TMP_ARM_IK_GRP" -p "TMP_GRP";
	rename -uid "79D8F424-49A1-B2E8-37AC-02880DCF487A";
createNode transform -n "armLFT_pov_Zro_grp" -p "TMP_ARM_IK_GRP";
	rename -uid "5F369FC9-4FDC-9BDF-6AA3-97A69EF216B6";
createNode transform -n "armLFT_pov_ctrl" -p "armLFT_pov_Zro_grp";
	rename -uid "1AE1ED03-424A-1848-6E8F-A089932E613F";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "armLFT_pov_ctrlShape" -p "armLFT_pov_ctrl";
	rename -uid "372EAEBA-4738-5F47-46FA-389092BBA4C7";
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
	rename -uid "FA9F29E9-4B32-0228-8E3F-BC88C9C7DF14";
createNode transform -n "armRGT_pov_ctrl" -p "armRGT_pov_Zro_grp";
	rename -uid "9DE0CD9A-4387-375D-1EF9-389DC3A06394";
	addAttr -ci true -k true -sn "localWorld" -ln "localWorld" -dv 1 -min 0 -max 1 
		-at "float";
	setAttr -k on ".localWorld" 0;
createNode nurbsCurve -n "armRGT_pov_ctrlShape" -p "armRGT_pov_ctrl";
	rename -uid "B73A1FA4-4533-7EC5-4602-258E6CE6FB2D";
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
	rename -uid "140D8B76-46B6-B2F8-2A08-9F948BCDE823";
createNode transform -n "handLFT_IK_ctrl" -p "handLFT_IK_Zro_grp";
	rename -uid "07E36218-468D-3AFE-F115-EDB8D919AB84";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "long";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr ".rp" -type "double3" -7.2955635396140418e-15 0 -3.6477817698070209e-15 ;
	setAttr ".sp" -type "double3" -7.2955635396140418e-15 0 -3.6477817698070209e-15 ;
	setAttr -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "handLFT_IK_ctrlShape" -p "handLFT_IK_ctrl";
	rename -uid "C6C692AB-4E40-7E8F-1850-40BBC59B893D";
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
	rename -uid "170CA921-47F6-E84F-5FD8-89B425B128D8";
createNode transform -n "handRGT_IK_ctrl" -p "handRGT_IK_Zro_grp";
	rename -uid "DCD9E6DB-4732-C542-6DFC-95866C54932A";
	addAttr -ci true -sn "___Extra___" -ln "___Extra___" -min 0 -max 0 -at "long";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "long";
	addAttr -ci true -sn "upStretch" -ln "upStretch" -min 0 -at "double";
	addAttr -ci true -sn "lowStretch" -ln "lowStretch" -min 0 -at "double";
	setAttr ".rp" -type "double3" 0 0 -4.5597272122587763e-15 ;
	setAttr ".sp" -type "double3" 0 0 -4.5597272122587763e-15 ;
	setAttr -k on ".___Extra___";
	setAttr -k on ".autoStretch";
	setAttr -k on ".upStretch";
	setAttr -k on ".lowStretch";
createNode nurbsCurve -n "handRGT_IK_ctrlShape" -p "handRGT_IK_ctrl";
	rename -uid "742624EB-4892-F88D-7BA5-FF847DF55B3B";
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
createNode transform -n "ExtraJoint_grp";
	rename -uid "7F396B04-47C1-5CF1-7E39-AFA1C5E6E437";
createNode joint -n "legLFT_pov_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "92FEF5C5-42C8-99CB-778F-C99390D8A8C7";
	setAttr ".t" -type "double3" 3.7627532482147217 16.370561599731445 16.727309320818584 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
createNode joint -n "armLFT_pov_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "5C95751B-4C60-6508-45AE-2B89F136F99D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 11.979297637939453 39.147418975830078 -23.810523305829257 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99815258060496437 8.9981312040783247e-10 0.060757105194783181 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 -0.060757105194783181 -5.4770116136011496e-11 0.99815258060496437 0
		 40.855079650878928 143.65834045410159 -6.71590328216549 1;
createNode joint -n "footOutLFT_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "1A2E1439-4F9B-7A4E-71DA-FB96E835BA0E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0.80967496019160778 0 -2.1581717074742239 ;
	setAttr ".r" -type "double3" 7.4554438061015243e-12 -2.3257709045378353e-15 3.6278201835441728e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -143.04244682007266 -89.939871926385095 143.34685053745474 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 5.9861612194955782e-12 5.111894414711049e-10 0
		 -5.9861846382625039e-12 1 1.7526591289396265e-11 0 -5.1118943973638142e-10 -1.7526646800547496e-11 0.99999999999999989 0
		 16.819365761636323 0.031779869297748675 2.6550645431123487 1;
createNode joint -n "heelRollLFT_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "ADA5A342-4EB5-81BD-D204-3FA5719D7E52";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 3.6977084403800062 0 -6.4108818111795225 ;
	setAttr ".r" -type "double3" 9.5230279818046558e-15 -2.7638251444335982e-14 -3.3332213061737656e-12 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0.037803946417466247 180.16384236523669 3.6054842493210453 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 5.9861612194955782e-12 5.111894414711049e-10 0
		 -5.9861846382625039e-12 1 1.7526591289396265e-11 0 -5.1118943973638142e-10 -1.7526646800547496e-11 0.99999999999999989 0
		 16.819365761636323 0.031779869297748675 2.6550645431123487 1;
createNode joint -n "footInLFT_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "787F2252-45FF-F482-7691-1EB5DB15795E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 6.7295400344062024 0 -2.1531853149534581 ;
	setAttr ".r" -type "double3" -3.336401860855229e-12 1.9083328088782123e-14 3.4986101496098132e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 53.70959801008128 89.939871926394588 -36.653149450581616 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 5.9861612194955782e-12 5.111894414711049e-10 0
		 -5.9861846382625039e-12 1 1.7526591289396265e-11 0 -5.1118943973638142e-10 -1.7526646800547496e-11 0.99999999999999989 0
		 16.819365761636323 0.031779869297748675 2.6550645431123487 1;
createNode joint -n "armRGT_pov_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "B44D4528-4EDD-D728-CE02-A3857D0A7FD6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -11.979307174682617 39.147552490234375 -23.810523986816406 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.99815258060496437 8.9981312040783247e-10 0.060757105194783181 0
		 -9.0147846190489121e-10 0.99999999999999989 -1.1032841307212495e-15 0 -0.060757105194783181 -5.4770116136011496e-11 0.99815258060496437 0
		 40.855079650878928 143.65834045410159 -6.71590328216549 1;
createNode joint -n "legRGT_pov_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "1FA869B0-41A7-188B-31E9-868FC2D70809";
	setAttr ".t" -type "double3" -3.7627651691436768 16.370548248291016 16.727318193485647 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "none";
createNode joint -n "footOutRGT_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "D24B6FE1-43EC-45BE-8E90-7F80DC963C31";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -0.809675 0 -2.15817 ;
	setAttr ".r" -type "double3" 7.4554438061015243e-12 -2.3257709045378353e-15 3.6278201835441728e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 36.957553179935033 89.939871926385095 -143.34685053744255 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 5.9861612194955782e-12 5.111894414711049e-10 0
		 -5.9861846382625039e-12 1 1.7526591289396265e-11 0 -5.1118943973638142e-10 -1.7526646800547496e-11 0.99999999999999989 0
		 16.819365761636323 0.031779869297748675 2.6550645431123487 1;
createNode joint -n "footInRGT_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "4C45CBD1-410C-F4F7-6500-C7B51346F360";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -6.72954 0 -2.15319 ;
	setAttr ".r" -type "double3" -3.336401860855229e-12 1.9083328088782123e-14 3.4986101496098132e-14 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" -126.29040198992833 -89.939871926394559 36.653149450589432 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 5.9861612194955782e-12 5.111894414711049e-10 0
		 -5.9861846382625039e-12 1 1.7526591289396265e-11 0 -5.1118943973638142e-10 -1.7526646800547496e-11 0.99999999999999989 0
		 16.819365761636323 0.031779869297748675 2.6550645431123487 1;
createNode joint -n "heelRollRGT_tmpJnt" -p "ExtraJoint_grp";
	rename -uid "7870391F-4136-09F2-12E6-C19D823D43B5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -3.69771 0 -6.41088 ;
	setAttr ".r" -type "double3" 9.5230279818046558e-15 -2.7638251444335982e-14 -3.3332213061737656e-12 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jot" -type "string" "yzx";
	setAttr ".jo" -type "double3" 0.037803946417340417 0.16384236523669146 176.39451575067898 ;
	setAttr ".bps" -type "matrix" 0.99999999999999989 5.9861612194955782e-12 5.111894414711049e-10 0
		 -5.9861846382625039e-12 1 1.7526591289396265e-11 0 -5.1118943973638142e-10 -1.7526646800547496e-11 0.99999999999999989 0
		 16.819365761636323 0.031779869297748675 2.6550645431123487 1;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "1FF06188-422E-0A85-CA1A-F4A9BAAF5036";
	setAttr -s 11 ".lnk";
	setAttr -s 11 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "7BD3B3A8-4699-FFC4-6C22-6B82701B2A1A";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "B9882B5B-48D1-7470-8DBD-60A4A3553926";
createNode displayLayerManager -n "layerManager";
	rename -uid "89636D45-431A-2EF1-1409-969CED281886";
	setAttr ".cdl" 2;
	setAttr -s 3 ".dli[1:2]"  1 2;
createNode displayLayer -n "defaultLayer";
	rename -uid "B1A35177-4224-F203-8EFF-91AC71EAA857";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "2758FA3E-45D5-5285-C6D5-589C92B61921";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "53520F64-4990-6C24-E771-3FBF09A9E4D1";
	setAttr ".g" yes;
createNode shadingEngine -n "m_0000_heroA_rarity1_1_helmSG";
	rename -uid "DFC59066-461D-845F-1878-92A9883F0DEA";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "416CB093-4051-48A9-D839-DE8B1FBFD512";
createNode shadingEngine -n "m_0000_heroA_rarity1_1_helmSG1";
	rename -uid "1BCB76BA-4FEC-90BB-D9B9-058210E81148";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "F4441672-43F6-8EE1-5B9C-5C9F8D0965D0";
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "0C9AD4AA-46D5-7184-9292-7FB9B0D04A44";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 1 -ast 0 -aet 1 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "1993C0AA-4BC1-40AE-303E-3CAB306D69E8";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -467.85712426617113 -161.90475547124495 ;
	setAttr ".tgi[0].vh" -type "double2" 448.80950597543642 170.23808847344139 ;
createNode objectSet -n "textureEditorIsolateSelectSet";
	rename -uid "3E37ED2F-487B-0947-0E49-A7A87E771C1C";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "0C6AAFCF-4231-1EF6-EC09-1ABE36ABED3C";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -133.33332803514296 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
createNode shadingEngine -n "lambert4SG";
	rename -uid "D6B5EEB8-45AA-8FFB-D931-A9A706D0138E";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "F5AF9386-4EE5-733E-0D1D-CEA2D784A0B5";
createNode shadingEngine -n "lambert5SG";
	rename -uid "F4ACBC87-4501-0965-FEE5-A6AAC2DA705D";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "F6D2AACB-4DA8-F4D9-9F4B-5E8D7B1A2200";
createNode shadingEngine -n "pasted__m_0000_heroA_rarity1_1_helmSG";
	rename -uid "FB04AD3C-496F-3CA6-A6FD-2C9075ECBF8C";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "pasted__materialInfo1";
	rename -uid "DDEC474F-4D48-1B83-1457-A8BB25F62B64";
createNode shadingEngine -n "pasted__m_0000_heroA_rarity1_1_helmSG1";
	rename -uid "A7CB5CA8-4C20-F509-E1D9-80AC6D065A53";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "pasted__materialInfo2";
	rename -uid "D58A2C2F-47B2-A800-E211-98BED19F9E52";
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "762EE1AE-4337-D9B2-CB3D-8EA0E98A5EFD";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -467.85712426617113 -161.90475547124495 ;
	setAttr ".tgi[0].vh" -type "double2" 448.80950597543642 170.23808847344139 ;
createNode objectSet -n "pasted__textureEditorIsolateSelectSet";
	rename -uid "FD74CFA8-4BCE-7108-D1FA-C5B159BD14FB";
	setAttr ".ihi" 0;
	setAttr ".fo" yes;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "51414FF2-45AB-DF74-9482-57BF5659045E";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -133.33332803514296 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
createNode shadingEngine -n "lambert6SG";
	rename -uid "B09CE437-4ECC-B679-BCBD-D28CEF0C7165";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo5";
	rename -uid "373C4F52-46DC-FE7A-C510-10B4F6EE08FC";
createNode shadingEngine -n "lambert7SG";
	rename -uid "9BE4E303-485A-DC7D-5896-73861EA61951";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo6";
	rename -uid "8D83A836-4DF4-F391-4EE6-11B8E19396F9";
createNode shadingEngine -n "blinn1SG";
	rename -uid "A6CEF750-4421-0D16-069D-428BEFFFABF0";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo7";
	rename -uid "50E0EB73-4065-1E48-4767-9AACED3C4E72";
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "07F6F504-4B13-9C27-0CAB-FF9649CF074D";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -622.61902287839052 -395.23807953274502 ;
	setAttr ".tgi[0].vh" -type "double2" 592.85711929911758 413.09522168030884 ;
createNode animCurveUU -n "leg_FK_visibility1";
	rename -uid "CF02C176-4720-0DE6-FB9B-15828A30262C";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  0 1 1 0 2 1;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "2FD933D4-48D4-D193-C7FA-AFAF17CCA3E7";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -330.95236780151544 -133.33332803514296 ;
	setAttr ".tgi[0].vh" -type "double2" 317.85713022663526 338.09522466054096 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo2";
	rename -uid "4F452178-47F2-5976-53D3-3B8DFB726611";
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
createNode animCurveUU -n "hand_FK_visibility1";
	rename -uid "C113A03B-4984-04F9-559E-4B9AD5DD28FC";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  0 1 1 0 2 1;
createNode animCurveUU -n "leg_IK_visibility1";
	rename -uid "B527AB31-47D9-4235-9EEF-309700AAC459";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  0 1 1 1 2 0;
createNode animCurveUU -n "hand_IK_visibility1";
	rename -uid "4EBFDCDB-49DA-4A67-DD95-3BB5216303B2";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  0 1 1 1 2 0;
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
	setAttr -av -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -cb on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 11 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
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
	setAttr -cb on ".mwc";
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
	setAttr -k on ".mcfr" 30;
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
	setAttr -k on ".hwfr" 30;
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "Root.s" "hips_bind_jnt.is";
connectAttr "hips_bind_jnt.s" "spine_bind_jnt.is";
connectAttr "spine_bind_jnt.s" "chest_bind_jnt.is";
connectAttr "chest_bind_jnt.s" "upperChest_bind_jnt.is";
connectAttr "upperChest_bind_jnt.s" "shoulderLFT_bind_jnt.is";
connectAttr "shoulderLFT_bind_jnt.s" "upperArmLFT_bind_jnt.is";
connectAttr "upperArmLFT_bind_jnt.s" "lowerArmLFT_bind_jnt.is";
connectAttr "lowerArmLFT_bind_jnt.s" "handLFT_bind_jnt.is";
connectAttr "handLFT_bind_jnt.s" "thumb01LFT_bind_jnt.is";
connectAttr "thumb01LFT_bind_jnt.s" "thumb02LFT_bind_jnt.is";
connectAttr "thumb02LFT_bind_jnt.s" "thumb03LFT_bind_jnt.is";
connectAttr "handLFT_bind_jnt.s" "index01LFT_bind_jnt.is";
connectAttr "index01LFT_bind_jnt.s" "index02LFT_bind_jnt.is";
connectAttr "index02LFT_bind_jnt.s" "index03LFT_bind_jnt.is";
connectAttr "handLFT_bind_jnt.s" "middle01LFT_bind_jnt.is";
connectAttr "middle01LFT_bind_jnt.s" "middle02LFT_bind_jnt.is";
connectAttr "middle02LFT_bind_jnt.s" "middle03LFT_bind_jnt.is";
connectAttr "handLFT_bind_jnt.s" "ring01LFT_bind_jnt.is";
connectAttr "ring01LFT_bind_jnt.s" "ring02LFT_bind_jnt.is";
connectAttr "ring02LFT_bind_jnt.s" "ring03LFT_bind_jnt.is";
connectAttr "handLFT_bind_jnt.s" "pinky01LFT_bind_jnt.is";
connectAttr "pinky01LFT_bind_jnt.s" "pinky02LFT_bind_jnt.is";
connectAttr "pinky02LFT_bind_jnt.s" "pinky03LFT_bind_jnt.is";
connectAttr "handLFT_bind_jnt.s" "handLFT_prop_jnt.is";
connectAttr "lowerArmLFT_bind_jnt.s" "lowerArmLFT_prop_jnt.is";
connectAttr "shoulderLFT_bind_jnt.s" "upperArmArmorLFT_bind_jnt.is";
connectAttr "upperChest_bind_jnt.s" "shoulderRGT_bind_jnt.is";
connectAttr "shoulderRGT_bind_jnt.s" "upperArmRGT_bind_jnt.is";
connectAttr "upperArmRGT_bind_jnt.s" "lowerArmRGT_bind_jnt.is";
connectAttr "lowerArmRGT_bind_jnt.s" "handRGT_bind_jnt.is";
connectAttr "handRGT_bind_jnt.s" "thumb01RGT_bind_jnt.is";
connectAttr "thumb01RGT_bind_jnt.s" "thumb02RGT_bind_jnt.is";
connectAttr "thumb02RGT_bind_jnt.s" "thumb03RGT_bind_jnt.is";
connectAttr "handRGT_bind_jnt.s" "index01RGT_bind_jnt.is";
connectAttr "index01RGT_bind_jnt.s" "index02RGT_bind_jnt.is";
connectAttr "index02RGT_bind_jnt.s" "index03RGT_bind_jnt.is";
connectAttr "handRGT_bind_jnt.s" "middle01RGT_bind_jnt.is";
connectAttr "middle01RGT_bind_jnt.s" "middle02RGT_bind_jnt.is";
connectAttr "middle02RGT_bind_jnt.s" "middle03RGT_bind_jnt.is";
connectAttr "handRGT_bind_jnt.s" "ring01RGT_bind_jnt.is";
connectAttr "ring01RGT_bind_jnt.s" "ring02RGT_bind_jnt.is";
connectAttr "ring02RGT_bind_jnt.s" "ring03RGT_bind_jnt.is";
connectAttr "handRGT_bind_jnt.s" "pinky01RGT_bind_jnt.is";
connectAttr "pinky01RGT_bind_jnt.s" "pinky02RGT_bind_jnt.is";
connectAttr "pinky02RGT_bind_jnt.s" "pinky03RGT_bind_jnt.is";
connectAttr "handRGT_bind_jnt.s" "handRGT_prop_jnt.is";
connectAttr "lowerArmRGT_bind_jnt.s" "lowerArmRGT_prop_jnt.is";
connectAttr "shoulderRGT_bind_jnt.s" "upperArmArmorRGT_bind_jnt.is";
connectAttr "upperChest_bind_jnt.s" "neck_bind_jnt.is";
connectAttr "neck_bind_jnt.s" "head_bind_jnt.is";
connectAttr "hips_bind_jnt.s" "upperLegLFT_bind_jnt.is";
connectAttr "upperLegLFT_bind_jnt.s" "lowerLegLFT_bind_jnt.is";
connectAttr "lowerLegLFT_bind_jnt.s" "footLFT_bind_jnt.is";
connectAttr "footLFT_bind_jnt.s" "toesLFT_bind_jnt.is";
connectAttr "toesLFT_bind_jnt.s" "toesTipLFT_bind_jnt.is";
connectAttr "hips_bind_jnt.s" "upperLegRGT_bind_jnt.is";
connectAttr "upperLegRGT_bind_jnt.s" "lowerLegRGT_bind_jnt.is";
connectAttr "lowerLegRGT_bind_jnt.s" "footRGT_bind_jnt.is";
connectAttr "footRGT_bind_jnt.s" "toesRGT_bind_jnt.is";
connectAttr "toesRGT_bind_jnt.s" "toesTipRGT_bind_jnt.is";
connectAttr "head_ctrl.gimbal_controller" "head_Gimbal_ctrlShape.v";
connectAttr "neck_ctrl.gimbal_controller" "neck_Gimbal_ctrlShape.v";
connectAttr "upperChest_ctrl.gimbal_controller" "upperChest_Gimbal_ctrlShape.v";
connectAttr "chest_ctrl.gimbal_controller" "chest_Gimbal_ctrlShape.v";
connectAttr "spine_ctrl.gimbal_controller" "spine_Gimbal_ctrlShape.v";
connectAttr "hips_ctrl.gimbal_controller" "hips_Gimbal_ctrlShape.v";
connectAttr "cog_ctrl.gimbal_controller" "cog_Gimbal_ctrlShape.v";
connectAttr "hand_FK_visibility1.o" "upperArmLFT_FK_Zro_grp.v";
connectAttr "upperArmLFT_FK_ctrl.gimbal_controller" "upperArmLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "hand_FK_visibility1.o" "lowerArmLFT_FK_Zro_grp.v";
connectAttr "lowerArmLFT_FK_ctrl.gimbal_controller" "lowerArmLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "hand_FK_visibility1.o" "handLFT_FK_Zro_grp.v";
connectAttr "handLFT_FK_ctrl.gimbal_controller" "handLFT_FK_Gimbal_ctrlShape.v";
connectAttr "leg_FK_visibility1.o" "toesLFT_FK_Zro_grp.v";
connectAttr "toesLFT_FK_ctrl.gimbal_controller" "toesLFT_FK_Gimbal_ctrlShape.v";
connectAttr "leg_FK_visibility1.o" "footLFT_FK_Zro_grp.v";
connectAttr "footLFT_FK_ctrl.gimbal_controller" "footLFT_FK_Gimbal_ctrlShape.v";
connectAttr "leg_FK_visibility1.o" "lowerLegLFT_FK_Zro_grp.v";
connectAttr "lowerLegLFT_FK_ctrl.gimbal_controller" "lowerLegLFT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "leg_FK_visibility1.o" "upperLegLFT_FK_Zro_grp.v";
connectAttr "upperLegLFT_FK_ctrl.gimbal_controller" "upperLegLFT_FK_Gimbal_ctrlShape.v"
		;
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
connectAttr "hand_FK_visibility1.o" "upperArmRGT_FK_Zro_grp.v";
connectAttr "upperArmRGT_FK_ctrl.gimbal_controller" "upperArmRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "hand_FK_visibility1.o" "lowerArmRGT_FK_Zro_grp.v";
connectAttr "lowerArmRGT_FK_ctrl.gimbal_controller" "lowerArmRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "hand_FK_visibility1.o" "handRGT_FK_Zro_grp.v";
connectAttr "handRGT_FK_ctrl.gimbal_controller" "handRGT_FK_Gimbal_ctrlShape.v";
connectAttr "leg_FK_visibility1.o" "upperLegRGT_FK_Zro_grp.v";
connectAttr "upperLegRGT_FK_ctrl.gimbal_controller" "upperLegRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "leg_FK_visibility1.o" "lowerLegRGT_FK_Zro_grp.v";
connectAttr "lowerLegRGT_FK_ctrl.gimbal_controller" "lowerLegRGT_FK_Gimbal_ctrlShape.v"
		;
connectAttr "leg_FK_visibility1.o" "footRGT_FK_Zro_grp.v";
connectAttr "footRGT_FK_ctrl.gimbal_controller" "footRGT_FK_Gimbal_ctrlShape.v";
connectAttr "leg_FK_visibility1.o" "toesRGT_FK_Zro_grp.v";
connectAttr "toesRGT_FK_ctrl.gimbal_controller" "toesRGT_FK_Gimbal_ctrlShape.v";
connectAttr "leg_IK_visibility1.o" "footLFT_IK_Zro_grp.v";
connectAttr "leg_IK_visibility1.o" "footRGT_IK_Zro_grp.v";
connectAttr "leg_IK_visibility1.o" "legRGT_pov_Zro_grp.v";
connectAttr "leg_IK_visibility1.o" "legLFT_pov_Zro_grp.v";
connectAttr "hand_IK_visibility1.o" "armLFT_pov_Zro_grp.v";
connectAttr "hand_IK_visibility1.o" "armRGT_pov_Zro_grp.v";
connectAttr "hand_IK_visibility1.o" "handLFT_IK_Zro_grp.v";
connectAttr "hand_IK_visibility1.o" "handRGT_IK_Zro_grp.v";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "m_0000_heroA_rarity1_1_helmSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "m_0000_heroA_rarity1_1_helmSG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pasted__m_0000_heroA_rarity1_1_helmSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "pasted__m_0000_heroA_rarity1_1_helmSG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert6SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert7SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "m_0000_heroA_rarity1_1_helmSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "m_0000_heroA_rarity1_1_helmSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pasted__m_0000_heroA_rarity1_1_helmSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "pasted__m_0000_heroA_rarity1_1_helmSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert6SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert7SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "blinn1SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "m_0000_heroA_rarity1_1_helmSG.msg" "materialInfo1.sg";
connectAttr "m_0000_heroA_rarity1_1_helmSG1.msg" "materialInfo2.sg";
connectAttr "lambert4SG.msg" "materialInfo3.sg";
connectAttr "lambert5SG.msg" "materialInfo4.sg";
connectAttr "pasted__m_0000_heroA_rarity1_1_helmSG.msg" "pasted__materialInfo1.sg"
		;
connectAttr "pasted__m_0000_heroA_rarity1_1_helmSG1.msg" "pasted__materialInfo2.sg"
		;
connectAttr "lambert6SG.msg" "materialInfo5.sg";
connectAttr "lambert7SG.msg" "materialInfo6.sg";
connectAttr "blinn1SG.msg" "materialInfo7.sg";
connectAttr "placement_ctrl.IK_FK_Leg_Vis" "leg_FK_visibility1.i";
connectAttr "lowerLegLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[0].dn"
		;
connectAttr "footRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[1].dn"
		;
connectAttr "leg_IK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[2].dn"
		;
connectAttr "upperLegRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[3].dn"
		;
connectAttr "leg_FK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[4].dn"
		;
connectAttr "footLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[5].dn"
		;
connectAttr "toesLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[6].dn"
		;
connectAttr "footRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[7].dn"
		;
connectAttr "upperLegLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[8].dn"
		;
connectAttr "legLFT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[9].dn"
		;
connectAttr "placement_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[10].dn"
		;
connectAttr "legRGT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[11].dn"
		;
connectAttr "lowerLegRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[1].ni[12].dn"
		;
connectAttr "lowerArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[0].dn"
		;
connectAttr "handRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[1].dn"
		;
connectAttr "upperArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[2].dn"
		;
connectAttr "hand_FK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[3].dn"
		;
connectAttr "hand_IK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[2].ni[4].dn"
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
connectAttr "leg_FK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[1].dn"
		;
connectAttr "toesLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[2].dn"
		;
connectAttr "lowerArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[3].dn"
		;
connectAttr "footLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[4].dn"
		;
connectAttr "legRGT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[5].dn"
		;
connectAttr "lowerLegRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[6].dn"
		;
connectAttr "lowerArmRGT_prop_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[8].dn"
		;
connectAttr "handRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[9].dn"
		;
connectAttr "handRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[10].dn"
		;
connectAttr "handLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[12].dn"
		;
connectAttr "footLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[14].dn"
		;
connectAttr "handLFT_prop_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[15].dn"
		;
connectAttr "footRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[16].dn"
		;
connectAttr "upperLegRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[17].dn"
		;
connectAttr "handRGT_prop_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[18].dn"
		;
connectAttr "handLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[20].dn"
		;
connectAttr "hand_FK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[22].dn"
		;
connectAttr "placement_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[3].ni[23].dn"
		;
connectAttr "lowerArmRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[0].dn"
		;
connectAttr "placement_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[1].dn"
		;
connectAttr "leg_FK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[2].dn"
		;
connectAttr "toesLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[3].dn"
		;
connectAttr "lowerArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[4].dn"
		;
connectAttr "footLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[5].dn"
		;
connectAttr "legRGT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[6].dn"
		;
connectAttr "lowerLegRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[7].dn"
		;
connectAttr "handRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[8].dn"
		;
connectAttr "handRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[9].dn"
		;
connectAttr "handLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[10].dn"
		;
connectAttr "upperArmLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[11].dn"
		;
connectAttr "footLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[12].dn"
		;
connectAttr "lowerLegLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[13].dn"
		;
connectAttr "footRGT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[14].dn"
		;
connectAttr "hand_IK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[15].dn"
		;
connectAttr "upperLegRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[16].dn"
		;
connectAttr "upperArmRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[17].dn"
		;
connectAttr "armLFT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[18].dn"
		;
connectAttr "footRGT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[19].dn"
		;
connectAttr "upperLegLFT_FK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[20].dn"
		;
connectAttr "handLFT_IK_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[21].dn"
		;
connectAttr "hand_FK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[22].dn"
		;
connectAttr "legLFT_pov_Zro_grp.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[23].dn"
		;
connectAttr "placement_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[24].dn"
		;
connectAttr "leg_IK_visibility1.msg" "MayaNodeEditorSavedTabsInfo2.tgi[4].ni[25].dn"
		;
connectAttr "chest_Gimbal_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[5].ni[0].dn"
		;
connectAttr "chest_Gimbal_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo2.tgi[5].ni[1].dn"
		;
connectAttr "spine_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[5].ni[2].dn";
connectAttr "spine_Gimbal_ctrlShape.msg" "MayaNodeEditorSavedTabsInfo2.tgi[5].ni[3].dn"
		;
connectAttr "chest_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[5].ni[4].dn";
connectAttr "spine_Gimbal_ctrl.msg" "MayaNodeEditorSavedTabsInfo2.tgi[5].ni[5].dn"
		;
connectAttr "placement_ctrl.IK_FK_Arm_Vis" "hand_FK_visibility1.i";
connectAttr "placement_ctrl.IK_FK_Leg_Vis" "leg_IK_visibility1.i";
connectAttr "placement_ctrl.IK_FK_Arm_Vis" "hand_IK_visibility1.i";
connectAttr "m_0000_heroA_rarity1_1_helmSG.pa" ":renderPartition.st" -na;
connectAttr "m_0000_heroA_rarity1_1_helmSG1.pa" ":renderPartition.st" -na;
connectAttr "lambert4SG.pa" ":renderPartition.st" -na;
connectAttr "lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "pasted__m_0000_heroA_rarity1_1_helmSG.pa" ":renderPartition.st" -na
		;
connectAttr "pasted__m_0000_heroA_rarity1_1_helmSG1.pa" ":renderPartition.st" -na
		;
connectAttr "lambert6SG.pa" ":renderPartition.st" -na;
connectAttr "lambert7SG.pa" ":renderPartition.st" -na;
connectAttr "blinn1SG.pa" ":renderPartition.st" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of PH_tmpRig.ma
