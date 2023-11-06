#!/bin/bash

set -e

list=(
  "devicefront/mtp-xmpp"
  "devicefront/df-mqtt-broker"
  "devicefront/df-root"
  "devicefront/cwmp-parser"
  "devicefront/df-acs-engine"
  "devicefront/df-api"
  "scheduler/krms-scheduler"
  "cs/krms-service-watcher"
  "back-end/fe-admin"
  "back-end/krms-fe-ws"
  "back-end/krms-fe-auth"
  "fe-device-api"
  "fe-device-api"
  "sfg/sfg-provisioning"
  "sfg/sfg-management"
  "sfg/sfg-general"
  "sfg/sfg-diagnostics"
  "sfg/sfg-network"
  "sfg/sfg-wifi"
  "sfg/sfg-app"
  "sfg/sfg-av"
  "sfg/sfg-firmware"
  "sfg/sfg-root"
  "service-group/sg-event"
  "service-group/sg-api"
  "service-group/sg-analytics"
  "service-group/sg-task"
  "service-group/sg-event-profile"
  "task/task-executor"
  "task/task-handler"
  "etisalat/etisalat-fe-web"
  "back-end/etisalat-fe-api"
  "back-end/etisalat-fe-partner-api"
)

read -p "> 서비스명 검색 (fe, sg, sg-api, ...): " svc
echo "-----"

declare -A map
CNT=0

for item in "${list[@]}"; do
  if [[ $item == *"$svc"* ]]; then
    CNT=$(($CNT+1))
    printf "%s. %s\n" $CNT $item
    map[$CNT]=$item
  fi
done

echo "-----"
read -p "> 다운로드 하려는 이미지 번호 입력: " ans

if [[ ! $ans =~ ^[0-9]+$ ]] ; then
    echo "숫자가 아님."
    exit
fi
if [[ $ans -gt ${#map[@]} ]]
  then
    echo "번호를 잘못 입력."
    exit
fi

img=${map[${ans}]}

if [[ $img == *"etisalat"* ]]; then
  project_name=krms3.1-aws-etisalat-stage
else
  project_name=krms3.1-aws-core
fi

docker pull harbor-repo.com:10443/$project_name/$img:latest
docker tag harbor-repo.com:10443/$project_name/$img:latest localhost/$project_name/$img:latest

output=${img#*/}
docker save -o $output.tar localhost/$project_name/$img:latest
chown krms:krms $output.tar
gzip $output.tar

echo "-----"
echo "> 이미지 저장완료: $output.tar.gz"
echo "> 이미지명: localhost/$project_name/$img:latest"
echo "-----"

