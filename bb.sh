#!/bin/sh

git clone https://devportal.kaonrms.com/konnect/core/devicefront/df-acs-engine.git
cd df-acs-engine
git checkout -b release-hellotv
git pull origin release-hellotv
echo '' >> README.md
git add .
git commit -m 'Teamcity test'
git push -u origin release-hellotv

