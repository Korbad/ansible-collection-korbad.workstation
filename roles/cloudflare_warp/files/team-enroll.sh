#!/bin/bash

warp-cli --accept-tos teams-enroll kor-team 

status=$(warp-cli --accept-tos status | grep Disconnected | awk '{print $3}')

echo -n "Waiting for the registration of device to Cloudflare Warp."

while [[ "$status" != "Disconnected" ]]
do
    echo -n "."
    sleep 5
    status=$(warp-cli --accept-tos status | grep Disconnected | awk '{print $3}')

done

echo \n

if [[ "$status" == "" ]]
then

    echo "Register Device Failed."
    echo $(warp-cli --accept-tos status | grep Status)

elif [[ $status == "Disconnected" ]]
then

    warp-cli connect > /dev/null

    status=$(warp-cli --accept-tos status | grep Connected | awk '{print $3}')

    while [[ "$status" != "Connected" ]]
    do

        sleep 5
        echo "Connecting.."
        status=$(warp-cli --accept-tos status | grep Connected | awk '{print $3}')

    done

    echo $(warp-cli --accept-tos status | grep Status)

fi
