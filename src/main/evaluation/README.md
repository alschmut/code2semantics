### Evaluation Model Structue

```
SurveyModel
	DataSetModel
		ParticipantModel
			ExperienceModel
		FileModel
			ContextIdentifierModel
			IdentifierModel
```

#### Example json
```
[
	{
		"participant": {
			"work_path": "SE",
			"experience_in_years": {
				"min": 0,
				"max": 2
			},
			"clean_code_practicioner": "Always"
		},
		files: {
			"file1": {
				"semantic_context_identifier": {
					"one": "Name1",
					"two": "Name2",
					"three": "Name3"
				},
				"class_name_describes_context": 2,
				"identifier_list": [
					{
						"name": "name1"
						"type": "class",
						"usefulness": 3
					},
					{
						"name": "name2"
						"type": "method",
						"usefulness": 2
					},
					{
						"name": "name3"
						"type": "variable",
						"usefulness": 2
					}
				]
			}
		}
	}
]
```