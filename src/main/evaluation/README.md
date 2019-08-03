### Evaluation Model Structue

```
SurveyModel
	DataSetModel
		ParticipantModel
			ExperienceModel
		FileModel
			ContextIdentifierModel
			FileContextModel
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
				"method_names": {
					"name1": {
						"usefulness": "Very",
						"numeric": 3
					}
				},
				"variable_names": {
					"name1": {
						"usefulness": "Very",
						"numeric": 3
					}
				},
				"class_names": {
					"name1": {
						"usefulness": "Very",
						"numeric": 3
					}
				},
				"file_context": {
					"class_name_describes_context": "Moderately",
					"numeric": 2
				}
			}
		}
	}
]
```