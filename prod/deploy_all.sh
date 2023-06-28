

DEPLOYMENT=prod
VALUE_ROOT="./deploy"
CHART_NAME="$VALUE_ROOT/$DEPLOYMENT/k8s/helm/guruchart"

deploy_service(){
  SERVICE_NAME=$1
  NAMESPACE_SUFFIX=$2
  NAMESPACE=$3

  # Generating namespace if not specified
  if [ -z "$NAMESPACE" ] || [ "$NAMESPACE" = None ]
  then NAMESPACE="guru-$NAMESPACE_SUFFIX"
  fi

  # Identifying YML file
  YML="$SERVICE_NAME-values.yaml"
  VALUES="$VALUE_ROOT/$DEPLOYMENT/$NAMESPACE_SUFFIX/$YML"

  echo "Deploying $SERVICE_NAME in namespace $NAMESPACE using values from $VALUES"

#   helm install "$SERVICE_NAME-test" --namespace $NAMESPACE --dry-run --debug $CHART_NAME --values $VALUES

  # helm install --name $SERVICE_NAME --namespace $NAMESPACE --dry-run --debug $CHART_NAME --values $VALUES --set service.type=LoadBalancer
#  helm del "$SERVICE_NAME" --namespace "$NAMESPACE"

  # Should the pods be recreated always?
  helm upgrade "$SERVICE_NAME" --namespace "$NAMESPACE" --install "$CHART_NAME" --values "$VALUES"
  echo
  echo
  echo
}


#deploy_service core-platform platforms guru-platforms
#deploy_service user-platform platforms
#deploy_service event-publisher-platform platforms
#deploy_service event-subscriber-platform platforms
#deploy_service lab-event-subscriber-platform platforms
#
##deploy_service content-service services jio-bhaaratai-covid
##deploy_service disease-risk-service services
##deploy_service image-classifier-service services
#deploy_service information-extractor-service services
#deploy_service rf-covid-lh-interface-service services
#
#deploy_service ai-tools-ui uis jio-bhaaratai-covid
##deploy_service disease-risk-ui uis
#deploy_service portal-ui uis
##deploy_service metabase-ui uis
#deploy_service covid-app-ui uis
