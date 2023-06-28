<ai guru dev istio old>
curl --location --request GET 'http://13.71.58.152/user-platform/get_survey_result?source_user_id=tQ4Yi4OntU5CmYQdwtR1jgIYlsE1cGYzURXRSKlFXzKpWinzgWjr%2BslFqE5MEb5RGXt7ymsexrQ%2B7vu/oEagGUQ1Jes4tZItRU7PFD3F2Ebk0lkBnHtCJNDGzguLvFOJHLzidv59c/kLrK3gNkdOTzAFkYNVpFreUGmQVTrw5d8%3D&source_id=emp_xp&business_id=Y/Eje5mYOU7I13oUop5pVv6LmQ9MHrWUf2jdXBSK9aK8GxySdjRhS06luYtQrtdDDc9xfGd1bpyL2seCUkjNwlJtJRHKRPAeQMvJ41hmT1P44Zo6GLiTqP6N8Um0iXti7CcxVdD8Yjg2Wm7%2BIuqH1skOJReDpWuT2fUnBszFeEM%3D&source_relation=Father&source_user_relation_id=null' \
--header 'Ocp-Apim-Subscription-Key: {{Ocp-Apim-Subscription-Key}}'

Prod test API working Playbook
1. Check if istio is working at k8s level
<istio NodePort> istio ingress NodePort IP
<k8s worker with istio port 80>
curl --location --request GET 'http://10.161.38.33:32130/user-platform/get_survey_result?source_user_id=tQ4Yi4OntU5CmYQdwtR1jgIYlsE1cGYzURXRSKlFXzKpWinzgWjr%2BslFqE5MEb5RGXt7ymsexrQ%2B7vu/oEagGUQ1Jes4tZItRU7PFD3F2Ebk0lkBnHtCJNDGzguLvFOJHLzidv59c/kLrK3gNkdOTzAFkYNVpFreUGmQVTrw5d8%3D&source_id=emp_xp&business_id=Y/Eje5mYOU7I13oUop5pVv6LmQ9MHrWUf2jdXBSK9aK8GxySdjRhS06luYtQrtdDDc9xfGd1bpyL2seCUkjNwlJtJRHKRPAeQMvJ41hmT1P44Zo6GLiTqP6N8Um0iXti7CcxVdD8Yjg2Wm7%2BIuqH1skOJReDpWuT2fUnBszFeEM%3D&source_relation=Father&source_user_relation_id=null'
curl --location --request GET 'http://10.161.38.33:32130/user-platform/health'

curl --location --request GET 'http://10.161.38.23:32130/user-platform/get_survey_result?source_user_id=tQ4Yi4OntU5CmYQdwtR1jgIYlsE1cGYzURXRSKlFXzKpWinzgWjr%2BslFqE5MEb5RGXt7ymsexrQ%2B7vu/oEagGUQ1Jes4tZItRU7PFD3F2Ebk0lkBnHtCJNDGzguLvFOJHLzidv59c/kLrK3gNkdOTzAFkYNVpFreUGmQVTrw5d8%3D&source_id=emp_xp&business_id=Y/Eje5mYOU7I13oUop5pVv6LmQ9MHrWUf2jdXBSK9aK8GxySdjRhS06luYtQrtdDDc9xfGd1bpyL2seCUkjNwlJtJRHKRPAeQMvJ41hmT1P44Zo6GLiTqP6N8Um0iXti7CcxVdD8Yjg2Wm7%2BIuqH1skOJReDpWuT2fUnBszFeEM%3D&source_relation=Father&source_user_relation_id=null'
curl --location --request GET 'http://10.161.38.23:32130/user-platform/health'
# curl --location --request GET 'http://10.161.38.23:32130/core-platform/knowlake/list_entity_details/?class=state&language=English'


1.5 Check if LB in front of istio is working
10.161.38.65:80
curl --location --request GET 'http://10.161.38.65/user-platform/health'

2. Check if API-M is working
API-M public: 104.211.139.121, private: 10.161.38.197
# curl --location --request GET 'http://apim.sit.health.jiolabs.com/user-platform/get_survey_result?source_user_id=tQ4Yi4OntU5CmYQdwtR1jgIYlsE1cGYzURXRSKlFXzKpWinzgWjr%2BslFqE5MEb5RGXt7ymsexrQ%2B7vu/oEagGUQ1Jes4tZItRU7PFD3F2Ebk0lkBnHtCJNDGzguLvFOJHLzidv59c/kLrK3gNkdOTzAFkYNVpFreUGmQVTrw5d8%3D&source_id=emp_xp&business_id=Y/Eje5mYOU7I13oUop5pVv6LmQ9MHrWUf2jdXBSK9aK8GxySdjRhS06luYtQrtdDDc9xfGd1bpyL2seCUkjNwlJtJRHKRPAeQMvJ41hmT1P44Zo6GLiTqP6N8Um0iXti7CcxVdD8Yjg2Wm7%2BIuqH1skOJReDpWuT2fUnBszFeEM%3D&source_relation=Father&source_user_relation_id=null' \
# --header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' -vvv

3. Check if APP Gateway is working
private: , public: 20.40.9.82 - api.prod.health.jio.com
# HTTP
# curl --location --request GET 'http://20.40.9.82/user-platform/health' \
# --header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' -H 'Host: api.prod.health.jio.com'
# curl --location --request GET 'http://20.40.9.82/user-platform/get_survey_result?source_user_id=tQ4Yi4OntU5CmYQdwtR1jgIYlsE1cGYzURXRSKlFXzKpWinzgWjr%2BslFqE5MEb5RGXt7ymsexrQ%2B7vu/oEagGUQ1Jes4tZItRU7PFD3F2Ebk0lkBnHtCJNDGzguLvFOJHLzidv59c/kLrK3gNkdOTzAFkYNVpFreUGmQVTrw5d8%3D&source_id=emp_xp&business_id=Y/Eje5mYOU7I13oUop5pVv6LmQ9MHrWUf2jdXBSK9aK8GxySdjRhS06luYtQrtdDDc9xfGd1bpyL2seCUkjNwlJtJRHKRPAeQMvJ41hmT1P44Zo6GLiTqP6N8Um0iXti7CcxVdD8Yjg2Wm7%2BIuqH1skOJReDpWuT2fUnBszFeEM%3D&source_relation=Father&source_user_relation_id=null' \
# --header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' -H 'Host: api.prod.health.jio.com'
# curl --location --request GET 'http://api.prod.health.jio.com/user-platform/health' \
# --header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' -vvv
# curl --location --request GET 'http://api.prod.health.jio.com/user-platform/get_survey_result?source_user_id=tQ4Yi4OntU5CmYQdwtR1jgIYlsE1cGYzURXRSKlFXzKpWinzgWjr%2BslFqE5MEb5RGXt7ymsexrQ%2B7vu/oEagGUQ1Jes4tZItRU7PFD3F2Ebk0lkBnHtCJNDGzguLvFOJHLzidv59c/kLrK3gNkdOTzAFkYNVpFreUGmQVTrw5d8%3D&source_id=emp_xp&business_id=Y/Eje5mYOU7I13oUop5pVv6LmQ9MHrWUf2jdXBSK9aK8GxySdjRhS06luYtQrtdDDc9xfGd1bpyL2seCUkjNwlJtJRHKRPAeQMvJ41hmT1P44Zo6GLiTqP6N8Um0iXti7CcxVdD8Yjg2Wm7%2BIuqH1skOJReDpWuT2fUnBszFeEM%3D&source_relation=Father&source_user_relation_id=null' \
# --header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' -vvv

HTTPS
curl --location --request GET 'https://api.prod.health.jio.com/user-platform/health' \
--header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' -vvv
curl --location --request GET 'https://api.prod.health.jio.com/user-platform/get_survey_result?source_user_id=tQ4Yi4OntU5CmYQdwtR1jgIYlsE1cGYzURXRSKlFXzKpWinzgWjr%2BslFqE5MEb5RGXt7ymsexrQ%2B7vu/oEagGUQ1Jes4tZItRU7PFD3F2Ebk0lkBnHtCJNDGzguLvFOJHLzidv59c/kLrK3gNkdOTzAFkYNVpFreUGmQVTrw5d8%3D&source_id=emp_xp&business_id=Y/Eje5mYOU7I13oUop5pVv6LmQ9MHrWUf2jdXBSK9aK8GxySdjRhS06luYtQrtdDDc9xfGd1bpyL2seCUkjNwlJtJRHKRPAeQMvJ41hmT1P44Zo6GLiTqP6N8Um0iXti7CcxVdD8Yjg2Wm7%2BIuqH1skOJReDpWuT2fUnBszFeEM%3D&source_relation=Father&source_user_relation_id=null' \
--header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' -vvv

# Prod test Webpage working Playbook
1. Check if covid-app-ui is working at k8s level
curl http://10.161.38.33:30834/
curl http://10.161.38.23:30531/

2. Check if nginx is working
curl http://10.161.38.33:32238/
curl http://10.161.38.23:32238/

3. Check if APP Gateway is working
healthhub.jio.com - private: , public: 20.40.8.89
# curl http://10.160.1.55/
# curl http://covid.sit.health.jiolabs.com/
# curl https://covid.sit.health.jiolabs.com/



ESS link for Check your symptomsTake a self-test and diagnose your symptoms for Covid-19.healthhub.jio.com​
https://healthhub.jio.com/workflow?workflow_id=covid_survey_v3&source_id=emp_xp&business_id=cKHt5E3Sbv404m8Vf4r60phixqPX3pEEkzlDwzB1HBv0GGe5p10btdiJX1aN4146TuHFF%2FJ9qbTuzJxU9De1GIaepS%2BIu0dlCqOKM81PuQEZQfJnzFWSi6nsWFkzE0r6Y2KNmF0KsAAbeBUoniL4QlSfuKo9izXuu5Aa4gZ67bY%3D&source_user_id=gyTkhLRbGQ0Y%2Bkp%2FnE2gZepLv0zn%2FaECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG%2F0CGHQaEvqGBhaokDDFvugsBJNyG%2FyhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl%2FqKX%2F4DnJdeb%2BBdVhOyw1CfC2Bi9QmSdrjEzY%3D&latitude=&longitude=&source_relation=Self&source_user_relation_id=null&source_age_years=36&source_gender=Male&phone=HSRx/3PuI3LgK61dJbQPlDWXw0xTgHBjgBtTm8LzV3Axk1ade1wFN6/ZhF1gEI9RJX91yT9k4G4Tf5ceYPDutuVtVgrkABX6DiAaDWQwT3uT4ogYYhCtM1NBcWtSYUWIgk8yx0v0/3eo/lx/dsLDdElfuGphtmcuXWvF8Pt5zW8=&dob=RmqfxJnNkEUmAWLkHK9NO1R5dlLdR4vEbara6QZh8NkaOZOxMpKk9+SWwoMtU27RKygcfNs1fJn+Lg4iQgvtJibEQLdlFlAGlwrU2BrgyHzs6Epx515JxkVyNPNPQ/GXO9iAt1yHpC041/TSdbL1N1DhWWFGylHl/Ubz8oCvfTU=
    
This API to test whether it got updated
curl --location --request GET 'https://api.prod.health.jio.com/user-platform/get_survey_result?source_user_id=gyTkhLRbGQ0Y%2Bkp%2FnE2gZepLv0zn%2FaECXmhzrMVAfYtksOwHoRiN4xiaeErd1k16yXCAG%2F0CGHQaEvqGBhaokDDFvugsBJNyG%2FyhILa0odX4tLCy7JY81jiM8bGsV1NYIIIoSl%2FqKX%2F4DnJdeb%2BBdVhOyw1CfC2Bi9QmSdrjEzY%3D&source_id=emp_xp&business_id=cKHt5E3Sbv404m8Vf4r60phixqPX3pEEkzlDwzB1HBv0GGe5p10btdiJX1aN4146TuHFF%2FJ9qbTuzJxU9De1GIaepS%2BIu0dlCqOKM81PuQEZQfJnzFWSi6nsWFkzE0r6Y2KNmF0KsAAbeBUoniL4QlSfuKo9izXuu5Aa4gZ67bY%3D&source_relation=Self&source_user_relation_id=null' \
--header 'Ocp-Apim-Subscription-Key: 444da0cf60df4c49b11b4ff5d3dfbe50' \
--data-raw ''




# Elasticsearch test
# Elasticsearch-Kibana
curl -u covidefkapp:J20d50app http://10.161.38.4:9200/_cluster/health
curl -u covidefkapp:J20d50app http://10.161.38.5:9200/_cluster/health
curl -u covidefkapp:J20d50app http://10.161.38.6:9200/_cluster/health
curl -u covidefkapp:J20d50app http://10.161.38.7:9200/_cluster/health
curl -u covidefkapp:J20d50app http://10.161.38.8:9200/_cluster/health
curl -u covidefkapp:J20d50app http://10.161.38.9:9200/_cluster/health

http://10.161.38.4:5601
# Elasticsearch
curl -u JMM_devops:D#L.C[t9qWlP<Pf http://10.161.38.10:9200/_cluster/health
curl -u JMM_devops:D#L.C[t9qWlP<Pf http://10.161.38.11:9200/_cluster/health
curl -u JMM_devops:D#L.C[t9qWlP<Pf http://10.161.38.12:9200/_cluster/health
curl -u JMM_devops:D#L.C[t9qWlP<Pf http://10.161.38.13:9200/_cluster/health
curl -u JMM_devops:D#L.C[t9qWlP<Pf http://10.161.38.14:9200/_cluster/health
curl -u JMM_devops:D#L.C[t9qWlP<Pf http://10.161.38.15:9200/_cluster/health
