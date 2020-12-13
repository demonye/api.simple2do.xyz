#!/bin/bash

cat <<EOF >image_detail.json
{
    "ImageURI": "$1:$(cat VERSION)"
}
EOF
