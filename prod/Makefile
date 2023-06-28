deploy_all_databases:
	echo "todo"

apply_guru_gateway:
	kubectl apply -f ./networking/guru-gateway.yaml

get_istio_ingress_ip:
	kubectl get svc istio-ingressgateway -n istio-system








set_docker_registry_secret:
	kubectl create secret docker-registry azure-container-repo --docker-server=guruartifacts.azurecr.io --docker-username=guruartifacts --docker-password=zo8sAObBAq/Q9iEMa+TAR42=Ly8yYytp

dev_test_content_service_helm:
	helm install --name content-service --namespace jio-bhaaratai-covid --dry-run --debug ./deploy/dev/kubernetes/helm/guruchart \
	--values ./deploy/dev/kubernetes/helm/content-service-values.yaml # --set service.type=LoadBalancer

dev_run_content_service_helm:
	helm install --name content-service --namespace jio-bhaaratai-covid ./deploy/dev/kubernetes/helm/guruchart \
	--values ./deploy/dev/kubernetes/helm/content-service-values.yaml # --set service.type=LoadBalancer


dev_upgrade_content_service_helm:
	helm upgrade content-service --install --recreate-pods --namespace jio-bhaaratai-covid ./deploy/dev/kubernetes/helm/guruchart \
	--values ./deploy/dev/kubernetes/helm/content-service-values.yaml # --set service.type=LoadBalancer

dev_del_content_service_helm:
	helm del --purge content-service

dev_apply_guru_gateway:
	kubectl apply -f ./deploy/dev/kubernetes/networking/guru-gateway.yaml
	#  samples/bookinfo/networking/bookinfo-gateway.yaml

dev_apply_content_service_destination_rule:
	kubectl apply -f ./deploy/dev/kubernetes/networking/content-service-destination-rule.yaml

get_istio_ingress_ip:
	kubectl get svc istio-ingressgateway -n istio-system

dev_install_my_service_helm:
	helm install --name weather-service --namespace jio-bhaaratai-covid ./deploy/dev/kubernetes/helm/guruchart \
	--values ./deploy/dev/kubernetes/helm/weather-service-values.yaml

dev_upgrade_my_service_helm:
	helm upgrade guru-platform --install --recreate-pods --namespace jio-bhaaratai-covid ./deploy/dev/kubernetes/helm/guruchart \
	--values ./deploy/dev/kubernetes/helm/guru-platform-values.yaml # --set service.type=LoadBalancer



dev_kubectl_apply_notif_service:
	kubectl apply -f ./deploy/dev/kubernetes/notif-service-onLB.yml

deploy_all_service_to_k8s:
	./deploy/dev/kubernetes/deploy_all_services_to_k8s.sh

dev_create_mongo:
	kubectl -n guru-db apply -f ./deploy/dev/kubernetes/db/mongo.yaml

dev_delete_mongo:
	kubectl -n guru-db delete -f ./deploy/dev/kubernetes/db/mongo.yaml
