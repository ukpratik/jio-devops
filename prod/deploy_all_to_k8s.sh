# echo "deploying all ai_guru services on kubernetes"

# echo "Deploying core-platform"
# # helm install --name core-platform-test --namespace guru-platforms --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/core-platform-values.yaml # --set service.type=LoadBalancer
# # helm install --name core-platform --namespace guru-platforms ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/core-platform-values.yaml
# helm upgrade core-platform --namespace guru-platforms --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/platforms/core-platform-values.yaml

# echo "Deploying user-platform"
# # helm install --name user-platform-test --namespace guru-platforms --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/user-platform-values.yaml # --set service.type=LoadBalancer
# # helm install --name user-platform --namespace guru-platforms ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/user-platform-values.yaml
# helm upgrade user-platform --namespace guru-platforms --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/platforms/user-platform-values.yaml

# echo "Deploying event-publisher-platform"
# # helm install --name event-publisher-platform-test --namespace guru-platforms --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/event-publisher-platform-values.yaml # --set service.type=LoadBalancer
# # helm install --name event-publisher-platform --namespace guru-platforms ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/event-publisher-platform-values.yaml
# # helm upgrade event-publisher-platform --install --recreate-pods --namespace guru-platforms ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/event-publisher-platform-values.yaml
# helm upgrade event-publisher-platform --namespace guru-platforms --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/platforms/event-publisher-platform-values.yaml

# echo "Deploying event-subscriber-platform"
# # helm install --name event-subscriber-platform-test --namespace guru-platforms --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/event-subscriber-platform-values.yaml # --set service.type=LoadBalancer
# # helm install --name event-subscriber-platform --namespace guru-platforms ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/event-subscriber-platform-values.yaml
# helm upgrade event-subscriber-platform --namespace guru-platforms --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/platforms/event-subscriber-platform-values.yaml

# echo "Deploying lab-event-subscriber-platform"
# # helm install --name lab-event-subscriber-platform-test --namespace guru-platforms --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/lab-event-subscriber-platform-values.yaml # --set service.type=LoadBalancer
# # helm install --name lab-event-subscriber-platform --namespace guru-platforms ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/platforms/lab-event-subscriber-platform-values.yaml
# helm upgrade lab-event-subscriber-platform --namespace guru-platforms --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/platforms/lab-event-subscriber-platform-values.yaml


# ## temporary solution
# helm upgrade event-subscriber-platform-5 --namespace guru-platforms --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/platforms/event-subscriber-platform-values-5.yaml

# helm upgrade lab-event-subscriber-platform-5 --namespace guru-platforms --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/platforms/lab-event-subscriber-platform-values-5.yaml
# ## temporary end




# echo "Deploying content-service"
# # helm install --name content-service-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/content-service-values.yaml # --set service.type=LoadBalancer
# # helm install --name content-service --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/content-service-values.yaml
# helm upgrade content-service --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/services/content-service-values.yaml

# echo "Deploying disease-risk-service"
# # helm install --name disease-risk-service-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/disease-risk-service-values.yaml # --set service.type=LoadBalancer
# # helm install --name disease-risk-service --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/disease-risk-service-values.yaml
# helm upgrade disease-risk-service --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/services/disease-risk-service-values.yaml

# echo "Deploying image-classifier-service"
# # helm install --name image-classifier-service-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/image-classifier-service-values.yaml # --set service.type=LoadBalancer
# # helm install --name image-classifier-service --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/image-classifier-service-values.yaml
# helm upgrade image-classifier-service --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/services/image-classifier-service-values.yaml

# echo "Deploying information-extractor-service"
# # helm install --name information-extractor-service-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/information-extractor-service-values.yaml # --set service.type=LoadBalancer
# # helm install --name information-extractor-service --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/information-extractor-service-values.yaml
# helm upgrade information-extractor-service --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/services/information-extractor-service-values.yaml

# echo "Deploying rf-covid-lh-interface-service"
# # helm install --name rf-covid-lh-interface-service-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/rf-covid-lh-interface-service-values.yaml # --set service.type=LoadBalancer
# # helm install --name rf-covid-lh-interface-service --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/services/rf-covid-lh-interface-service-values.yaml
# helm upgrade rf-covid-lh-interface-service --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/services/rf-covid-lh-interface-service-values.yaml

# echo "Deploying ai-tools-ui"
# # helm install --name ai-tools-ui-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/ai-tools-ui-values.yaml # --set service.type=LoadBalancer
# # helm install --name ai-tools-ui --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/ai-tools-ui-values.yaml
# helm upgrade ai-tools-ui --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/uis/ai-tools-ui-values.yaml

# echo "Deploying cept-ui"
# # helm install --name cept-ui-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/cept-ui-values.yaml # --set service.type=LoadBalancer
# # helm install --name cept-ui --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/cept-ui-values.yaml
# helm upgrade cept-ui --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/uis/cept-ui-values.yaml

# echo "Deploying disease-risk-ui"
# # helm install --name disease-risk-ui-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/disease-risk-ui-values.yaml # --set service.type=LoadBalancer
# # helm install --name disease-risk-ui --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/disease-risk-ui-values.yaml
# helm upgrade disease-risk-ui --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/uis/disease-risk-ui-values.yaml

# echo "Deploying portal-ui"
# # helm install --name portal-ui-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/portal-ui-values.yaml # --set service.type=LoadBalancer
# # helm install --name portal-ui --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/portal-ui-values.yaml
# helm upgrade portal-ui --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/uis/portal-ui-values.yaml

# echo "Deploying metabase-ui"
# # helm install --name metabase-ui-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/metabase-ui-values.yaml # --set service.type=LoadBalancer
# # helm install --name metabase-ui --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/metabase-ui-values.yaml
# helm upgrade metabase-ui --namespace jio-bhaaratai-covid --install ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/uis/metabase-ui-values.yaml

# echo "Deploying covid-app-ui"
# # helm install --name covid-app-ui-test --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/covid-app-ui-values.yaml # --set service.type=LoadBalancer
# # helm install --name covid-app-ui --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/covid-app-ui-values.yaml
# # helm upgrade covid-app-ui --install --recreate-pods --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# # 	--values ./deploy/prod/uis/covid-app-ui-values.yaml
# helm upgrade covid-app-ui --namespace jio-bhaaratai-covid ./deploy/prod/k8s/helm/guruchart \
# 	--values ./deploy/prod/uis/covid-app-ui-values.yaml
