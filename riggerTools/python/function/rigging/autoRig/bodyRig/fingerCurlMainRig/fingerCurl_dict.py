
# plan to use dict on finger curl


curlRoll_dict = 	{ 		'behiveType' 		: 'constance'
							'fingerName'		:	('thumb','index','middle','ring','pinky')	,
							'ctrlNumber' 		:	[01,02,03]									,
							'axis'				:	'X' 										,
							'dimentsion'		:	'rotate'									,
							'side'				:   'LFT'		,
							'ampValue'			:	 ( 0.1,0.1,0.1,0.1,0.1 )								 }


curlRelax_dict = 	{ 		'behiveType' 		: 'exponencial'
							'fingerName'		:	('thumb','index','middle','ring','pinky')	,
							'ctrlNumber' 		:	[01,02,03]									,
							'axis'				:	'X' 										,
							'dimentsion'		:	'rotate'									,
							'side'				:   'LFT'		,
							'ampValue'			:	 ( 0.1,0.2,0.3,0.4,0.5 )								 }


curlSpread_dict = 	{ 		'behiveType' 		: 'constance'
							'fingerName'		:	('thumb','index','middle','ring','pinky')	,
							'ctrlNumber' 		:	[01]									,
							'axis'				:	'Z' 										,
							'dimentsion'		:	'rotate'									,
							'side'				:   'LFT'		,
							'ampValue'			:	 ( 0.1,0.2,0.3,0.4,0.5 )								 }