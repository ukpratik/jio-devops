from locust import HttpLocust, TaskSet, task

class CovidTasks(TaskSet):
  # @task
  # def get_testing_centres(self):
  #     self.client.get(
  #       url = "https://ai-guru.azure-api.net/dev/core-platform/knowlake/list_entity_details/?class=healthcareestablishment&language=English&state=Maharashtra",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="Get Testing Centers",
  #     )

  # @task
  # def get_states(self):
  #     self.client.get(
  #       url = "https://ai-guru.azure-api.net/dev/core-platform/knowlake/list_entity_details/?class=state&language=English",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="Get States",
  #     )

  # @task
  # def get_config_for_app(self):
  #     self.client.get(
  #       url = "https://ai-guru.azure-api.net/dev/core-platform/localisation/get_config/?app_id=covid19aicoe",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="Get Config for app",
  #     )

  # @task
  # def get_localisation_string_with_params(self):
  #     self.client.get(
  #       url = "https://ai-guru.azure-api.net/dev/core-platform/localisation/get_localisation/?app_id=covid19aicoe&language=English",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="Get Localisation String With Params",
  #     )

  # @task
  # def list_faqs(self):
  #     self.client.get(
  #       url = "https://ai-guru.azure-api.net/dev/core-platform/knowlake/healthcare_knowledge/healthcare_knowledge.models.knowledge.DiseaseFAQ/list_entities/?f={%22disease%22:%225e6b533c66c3573280f13435%22}",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="List FAQs",
  #     )

  @task
  def get_workflow_template(self):
      self.client.get(
        url = "https://api.prod.health.jio.com/core-platform/query/get_worflow_template/?language=English&workflow_id=covid_survey_v3",
        data = {},
        headers = {
          'Ocp-Apim-Subscription-Key': '444da0cf60df4c49b11b4ff5d3dfbe50'
        },
        name="Get Workflow Template",
      )

  @task
  def compute_risk(self):
      self.client.post(
        url = "https://api.prod.health.jio.com/core-platform/query/compute_risk/",
        json = {
            "source_user_id": "gyTkhLRbGQ0Y+kp/nE2gZepLv0zn/aECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG/0CGHQaEvqGBhaokDDFvugsBJNyG/yhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl/qKX/4DnJdeb+BdVhOyw1CfC2Bi9QmSdrjEzY=",
            "workflow_id": "covid_survey_v3",
            "language": "English",
            "workflow_responses": [
                {
                    "question_id": "5e78c9799f6f26e9cd6bf910",
                    "question_text": "For whom are you taking this test?",
                    "name": "relation",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e78bce0c894d976c7469b46",
                            "name": "For yourself",
                            "preferred_term": "For yourself",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": None,
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e73802a279319e40b728f76",
                    "question_text": "What is your gender?",
                    "name": "gender",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e73666041e0346babab1f26",
                            "name": "Male",
                            "preferred_term": "Male",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": None,
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e9b28cff422694ccf811e27",
                    "question_text": "Please enter your age in years.",
                    "name": "enter age",
                    "selection_type": "Number",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        36
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e9b2980f422694ccf811e28",
                    "question_text": "Do you currently have any of these health conditions?",
                    "name": "health conditions v2",
                    "selection_type": "Multi-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e982eb77ccd367c8a97e2b9",
                            "name": "No existing conditions",
                            "preferred_term": "No existing conditions",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": None,
                            "clear_others": True
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e9b2a49f422694ccf811e2a",
                    "question_text": "Have you or someone in your family staying with you came in close contact with a laboratory confirmed COVID-19 patient in the last 14 days?",
                    "name": "contact with covid patient",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e734824cbb526bf0acaff1a",
                            "name": "No",
                            "preferred_term": "No",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": "YesNo",
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e9b2a82f422694ccf811e2b",
                    "question_text": "Have you or someone in your family staying with you attended a large gathering/ in a migration centre in the last 14 days?",
                    "name": "attended large gathering",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e734824cbb526bf0acaff1a",
                            "name": "No",
                            "preferred_term": "No",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": "YesNo",
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e9b2adef422694ccf811e2c",
                    "question_text": "Are you currently working for essential services in public exposed places (such as hospitals, retail outlets, delivery services)",
                    "name": "you work for essential services",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e734824cbb526bf0acaff1a",
                            "name": "No",
                            "preferred_term": "No",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": "YesNo",
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e9b2b0ef422694ccf811e2d",
                    "question_text": "Is someone in your family staying with you currently working for essential services in public exposed places (such as hospitals, retail outlets, delivery services)",
                    "name": "family member works for essential services",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e734824cbb526bf0acaff1a",
                            "name": "No",
                            "preferred_term": "No",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": "YesNo",
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5e9b2ba1f422694ccf811e2e",
                    "question_text": "Are you having one or more of the following symptoms?",
                    "name": "primary covid symptoms",
                    "selection_type": "Multi-Select",
                    "option_type": "None",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5e73682541e0346babab1f32",
                            "name": "None of the above",
                            "preferred_term": "None",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": None,
                            "clear_others": True
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5ee743e6431f87dd4875cfb8",
                    "question_text": "What is your current status in Arogya Setu?",
                    "name": "aarogya setu status",
                    "selection_type": "Single-Select",
                    "option_type": "None",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5ee7426b431f87dd4875cfae",
                            "name": "green",
                            "preferred_term": "Green",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": None,
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5ee7444f431f87dd4875cfb9",
                    "question_text": "Do you currently stay in containment zone?",
                    "name": "containment zone",
                    "selection_type": "Single-Select",
                    "option_type": "None",
                    "dependencies": [
                        {
                            "question": "5ee743e6431f87dd4875cfb8",
                            "condition": "absent",
                            "options": [
                                "5ee742b5431f87dd4875cfb1"
                            ]
                        }
                    ],
                    "options": [
                        {
                            "id": "5e734824cbb526bf0acaff1a",
                            "name": "No",
                            "preferred_term": "No",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": "YesNo",
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                },
                {
                    "question_id": "5ee744f7431f87dd4875cfba",
                    "question_text": "Did you or any persons staying with you visit any of these places during the last 3 days?",
                    "name": "visited outdoor places covid v3",
                    "selection_type": "Multi-Select",
                    "option_type": "None",
                    "dependencies": [],
                    "options": [
                        {
                            "id": "5ee742fc431f87dd4875cfb3",
                            "name": "Public market",
                            "preferred_term": "Public market",
                            "type": "CommonEntity.QuestionnaireOption",
                            "image": None,
                            "video": None,
                            "description": None,
                            "option_type": None,
                            "clear_others": False
                        }
                    ],
                    "play_audio": False,
                    "multimedia": []
                }
            ],
            "source_id": "emp_xp"
        },
        headers = {
          'Content-Type': 'application/json',
          'Ocp-Apim-Subscription-Key': '444da0cf60df4c49b11b4ff5d3dfbe50'
        },
        name="Compute Risk",
      )

  @task
  def get_covid_19_risk(self):
      self.client.get(
        url="https://api.prod.health.jio.com/user-platform/get_survey_result?source_user_id=gyTkhLRbGQ0Y%2Bkp%2FnE2gZepLv0zn%2FaECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG%2F0CGHQaEvqGBhaokDDFvugsBJNyG%2FyhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl%2FqKX%2F4DnJdeb%2BBdVhOyw1CfC2Bi9QmSdrjEzY%3D&source_id=emp_xp&business_id=cKHt5E3Sbv404m8Vf4r60phixqPX3pEEkzlDwzB1HBv0GGe5p10btdiJX1aN4146TuHFF%2FJ9qbTuzJxU9De1GIaepS%2BIu0dlCqOKM81PuQEZQfJnzFWSi6nsWFkzE0r6Y2KNmF0KsAAbeBUoniL4QlSfuKo9izXuu5Aa4gZ67bY%3D&source_relation=Self&source_user_relation_id=null",
        headers={
          'Content-Type': 'application/json',
          'Ocp-Apim-Subscription-Key': '444da0cf60df4c49b11b4ff5d3dfbe50'
        },
        name="Get Covid 19 Risk",
      )

  # @task
  # def get_disease_stats_india(self):
  #     self.client.get(
  #       url = "https://ai-guru.azure-api.net/dev/information-extractor-service/covid19/india",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="Get Disease Stats India",
  #     )

  # @task
  # def get_disease_stats_world(self):
  #     self.client.get(
  #       url = "https://ai-guru.azure-api.net/dev/information-extractor-service/covid19/world",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="Get disease Stats World",
  #     )

  # @task
  # def send_events(self):
  #     self.client.post(
  #       url = "https://ai-guru-event.azure-api.net/dev/event-publisher-platform/api/event",
  #       data = "{\n    \"event\": {\n        \"datetime\": \"18/03/2020, 10:42:25\",\n        \"event_name\": \"answered_question_test_1\",\n        \"source_id\": \"jiohealthhub\",\n        \"source_user_id\": \"3hejkr3\",\n        \"user_id\": \"u328jd3923\",\n        \"latitude\": 19.036566,\n        \"longitude\": 72.930641,\n        \"event_data\": {\n            \"language\": \"English\",\n            \"question_text\": \"How you doin?\",\n            \"question_id\": \"5e67c58ce5eb884dfaa92f84\",\n            \"response_id\": \"5e4f3e97d9e7ecaa967f060a\",\n            \"response_text\": \"No\"\n        }\n    }\n}",
  #       headers = {
  #         'Content-Type': 'application/json',
  #         'Ocp-Apim-Subscription-Key': '1afb760338734db4a0629981b3f3b310'
  #       },
  #       name="Send Events",
  #     )

  # @task
  # def get_covid_webpage(self):
  #     self.client.get(
  #       url = "https://dev-covid.bhaarat.ai",
  #       data = {},
  #       headers = {
  #         'Ocp-Apim-Subscription-Key': 'd3ea324bcbe24211a0750a8371df2fd2'
  #       },
  #       name="Get covid webpage",
  #     )

  @task
  def covid_survey_event(self):
      self.client.post(
        url = "https://api.prod.health.jio.com/event-publisher-platform/api/event",
        json = {
          "event": {
            "datetime": "21/07/2020 06:47:12 PM",
            "source_id": "emp_xp",
            "source_user_id": "gyTkhLRbGQ0Y+kp/nE2gZepLv0zn/aECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG/0CGHQaEvqGBhaokDDFvugsBJNyG/yhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl/qKX/4DnJdeb+BdVhOyw1CfC2Bi9QmSdrjEzY=",
            "business_id": "cKHt5E3Sbv404m8Vf4r60phixqPX3pEEkzlDwzB1HBv0GGe5p10btdiJX1aN4146TuHFF/J9qbTuzJxU9De1GIaepS+Iu0dlCqOKM81PuQEZQfJnzFWSi6nsWFkzE0r6Y2KNmF0KsAAbeBUoniL4QlSfuKo9izXuu5Aa4gZ67bY=",
            "latitude": None,
            "longitude": None,
            "event_name": "symptom_inference",
            "event_data": {
              "language": "English",
              "question_id": "covid_19_risk",
              "question_text": "covid_19_risk",
              "response_id": "5e738214279319e40b728f83",
              "response_text": "Low Risk",
              "risk_name": "low-risk",
              "action_category": None,
              "workflow_responses": {
                "source_user_id": "gyTkhLRbGQ0Y+kp/nE2gZepLv0zn/aECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG/0CGHQaEvqGBhaokDDFvugsBJNyG/yhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl/qKX/4DnJdeb+BdVhOyw1CfC2Bi9QmSdrjEzY=",
                "workflow_id": "covid_survey_v3",
                "language": "English",
                "workflow_responses": [
                  {
                    "question_id": "5e78c9799f6f26e9cd6bf910",
                    "question_text": "For whom are you taking this test?",
                    "name": "relation",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e78bce0c894d976c7469b46",
                        "name": "For yourself",
                        "preferred_term": "For yourself",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": None,
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e73802a279319e40b728f76",
                    "question_text": "What is your gender?",
                    "name": "gender",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e73666041e0346babab1f26",
                        "name": "Male",
                        "preferred_term": "Male",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": None,
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e9b28cff422694ccf811e27",
                    "question_text": "Please enter your age in years.",
                    "name": "enter age",
                    "selection_type": "Number",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      36
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e9b2980f422694ccf811e28",
                    "question_text": "Do you currently have any of these health conditions?",
                    "name": "health conditions v2",
                    "selection_type": "Multi-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e982eb77ccd367c8a97e2b9",
                        "name": "No existing conditions",
                        "preferred_term": "No existing conditions",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": None,
                        "clear_others": True
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e9b2a49f422694ccf811e2a",
                    "question_text": "Have you or someone in your family staying with you came in close contact with a laboratory confirmed COVID-19 patient in the last 14 days?",
                    "name": "contact with covid patient",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e734824cbb526bf0acaff1a",
                        "name": "No",
                        "preferred_term": "No",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": "YesNo",
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e9b2a82f422694ccf811e2b",
                    "question_text": "Have you or someone in your family staying with you attended a large gathering/ in a migration centre in the last 14 days?",
                    "name": "attended large gathering",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e734824cbb526bf0acaff1a",
                        "name": "No",
                        "preferred_term": "No",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": "YesNo",
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e9b2adef422694ccf811e2c",
                    "question_text": "Are you currently working for essential services in public exposed places (such as hospitals, retail outlets, delivery services)",
                    "name": "you work for essential services",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e734824cbb526bf0acaff1a",
                        "name": "No",
                        "preferred_term": "No",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": "YesNo",
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e9b2b0ef422694ccf811e2d",
                    "question_text": "Is someone in your family staying with you currently working for essential services in public exposed places (such as hospitals, retail outlets, delivery services)",
                    "name": "family member works for essential services",
                    "selection_type": "Single-Select",
                    "option_type": "Any",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e734824cbb526bf0acaff1a",
                        "name": "No",
                        "preferred_term": "No",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": "YesNo",
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5e9b2ba1f422694ccf811e2e",
                    "question_text": "Are you having one or more of the following symptoms?",
                    "name": "primary covid symptoms",
                    "selection_type": "Multi-Select",
                    "option_type": "None",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5e73682541e0346babab1f32",
                        "name": "None of the above",
                        "preferred_term": "None",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": None,
                        "clear_others": True
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5ee743e6431f87dd4875cfb8",
                    "question_text": "What is your current status in Arogya Setu?",
                    "name": "aarogya setu status",
                    "selection_type": "Single-Select",
                    "option_type": "None",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5ee7426b431f87dd4875cfae",
                        "name": "green",
                        "preferred_term": "Green",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": None,
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5ee7444f431f87dd4875cfb9",
                    "question_text": "Do you currently stay in containment zone?",
                    "name": "containment zone",
                    "selection_type": "Single-Select",
                    "option_type": "None",
                    "dependencies": [
                      {
                        "question": "5ee743e6431f87dd4875cfb8",
                        "condition": "absent",
                        "options": [
                          "5ee742b5431f87dd4875cfb1"
                        ]
                      }
                    ],
                    "options": [
                      {
                        "id": "5e734824cbb526bf0acaff1a",
                        "name": "No",
                        "preferred_term": "No",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": "YesNo",
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  },
                  {
                    "question_id": "5ee744f7431f87dd4875cfba",
                    "question_text": "Did you or any persons staying with you visit any of these places during the last 3 days?",
                    "name": "visited outdoor places covid v3",
                    "selection_type": "Multi-Select",
                    "option_type": "None",
                    "dependencies": [],
                    "options": [
                      {
                        "id": "5ee742fc431f87dd4875cfb3",
                        "name": "Public market",
                        "preferred_term": "Public market",
                        "type": "CommonEntity.QuestionnaireOption",
                        "image": None,
                        "video": None,
                        "description": None,
                        "option_type": None,
                        "clear_others": False
                      }
                    ],
                    "play_audio": False,
                    "multimedia": []
                  }
                ],
                "source_id": "emp_xp"
              },
              "source_relation": "Self",
              "source_user_relation_id": "None",
              "source_age_years": "36",
              "source_gender": "Male"
            }
          },
          "source_id": "emp_xp"
        },
        headers = {
          'Ocp-Apim-Subscription-Key': '444da0cf60df4c49b11b4ff5d3dfbe50'
        },
        name="Survey Event",
      )

  @task
  def covid_survey_event_no_change(self):
    self.client.post(
      url="https://api.prod.health.jio.com/event-publisher-platform/api/event",
      json={
          "event": {
              "datetime": "22/07/2020 04:54:47 PM",
              "source_id": "emp_xp",
              "source_user_id": "gyTkhLRbGQ0Y+kp/nE2gZepLv0zn/aECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG/0CGHQaEvqGBhaokDDFvugsBJNyG/yhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl/qKX/4DnJdeb+BdVhOyw1CfC2Bi9QmSdrjEzY=",
              "business_id": "cKHt5E3Sbv404m8Vf4r60phixqPX3pEEkzlDwzB1HBv0GGe5p10btdiJX1aN4146TuHFF/J9qbTuzJxU9De1GIaepS+Iu0dlCqOKM81PuQEZQfJnzFWSi6nsWFkzE0r6Y2KNmF0KsAAbeBUoniL4QlSfuKo9izXuu5Aa4gZ67bY=",
              "latitude": None,
              "longitude": None,
              "event_name": "symptom_inference_no_change",
              "event_data": {
                  "language": "English",
                  "question_id": "covid_19_risk",
                  "question_text": "covid_19_risk",
                  "workflow_responses": {
                      "language": "English",
                      "source_id": "emp_xp",
                      "source_user_id": "gyTkhLRbGQ0Y+kp/nE2gZepLv0zn/aECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG/0CGHQaEvqGBhaokDDFvugsBJNyG/yhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl/qKX/4DnJdeb+BdVhOyw1CfC2Bi9QmSdrjEzY=",
                      "workflow_id": "covid_survey_v3_no_change",
                      "workflow_responses": [
                          {
                              "question_id": "5ee743e6431f87dd4875cfb8",
                              "question_text": "What is your current status in Arogya Setu?",
                              "name": "aarogya setu status",
                              "selection_type": "Single-Select",
                              "option_type": "None",
                              "dependencies": [],
                              "options": [
                                  {
                                      "id": "5ee7426b431f87dd4875cfae",
                                      "name": "green",
                                      "preferred_term": "Green",
                                      "type": "CommonEntity.QuestionnaireOption",
                                      "image": None,
                                      "video": None,
                                      "description": None,
                                      "option_type": None,
                                      "clear_others": False
                                  }
                              ],
                              "play_audio": False,
                              "multimedia": []
                          },
                          {
                              "question_id": "5ee7444f431f87dd4875cfb9",
                              "question_text": "Do you currently stay in containment zone?",
                              "name": "containment zone",
                              "selection_type": "Single-Select",
                              "option_type": "None",
                              "dependencies": [
                                  {
                                      "question": "5ee743e6431f87dd4875cfb8",
                                      "condition": "absent",
                                      "options": [
                                          "5ee742b5431f87dd4875cfb1"
                                      ]
                                  }
                              ],
                              "options": [
                                  {
                                      "id": "5e734824cbb526bf0acaff1a",
                                      "name": "No",
                                      "preferred_term": "No",
                                      "type": "CommonEntity.QuestionnaireOption",
                                      "image": None,
                                      "video": None,
                                      "description": None,
                                      "option_type": "YesNo",
                                      "clear_others": False
                                  }
                              ],
                              "play_audio": False,
                              "multimedia": []
                          },
                          {
                              "question_id": "5ee744f7431f87dd4875cfba",
                              "question_text": "Did you or any persons staying with you visit any of these places during the last 3 days?",
                              "name": "visited outdoor places covid v3",
                              "selection_type": "Multi-Select",
                              "option_type": "None",
                              "dependencies": [],
                              "options": [
                                  {
                                      "id": "5ee7434d431f87dd4875cfb6",
                                      "name": "Shopping mall",
                                      "preferred_term": "Shopping mall",
                                      "type": "CommonEntity.QuestionnaireOption",
                                      "image": None,
                                      "video": None,
                                      "description": None,
                                      "option_type": None,
                                      "clear_others": False
                                  }
                              ],
                              "play_audio": False,
                              "multimedia": []
                          }
                      ]
                  },
                  "source_relation": "Sister",
                  "source_user_relation_id": "01",
                  "source_age_years": "32",
                  "source_gender": "Female"
              }
          },
          "source_id": "emp_xp"
      },
      headers={
        'Ocp-Apim-Subscription-Key': '444da0cf60df4c49b11b4ff5d3dfbe50'
      },
      name="Survey Event No Change",
    )


class CovidWarmer(HttpLocust):
  task_set = CovidTasks
  min_wait = 1000
  max_wait = 3000


# from locust import HttpLocust, TaskSet, task

# class ElbTasks(TaskSet):
#   @task
#   def status(self):
#       self.client.get("/status")

#   @task
#   def status1(self):
#       self.client.get("/status1")

# class ElbWarmer(HttpLocust):
#   task_set = ElbTasks
#   min_wait = 1000
#   max_wait = 3000
