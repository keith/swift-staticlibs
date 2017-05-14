#!/bin/bash

set -e
set -o pipefail
set -u

xcodebuild \
  -workspace PodsDependencies.xcworkspace \
  -scheme PodsDependencies \
  -sdk iphonesimulator \
  -derivedDataPath build \
  -showBuildSettings \
  2> /dev/null \
  | grep -E "^\s*CONFIGURATION_BUILD_DIR\s*=" \
  | awk '{ print $3; }'
