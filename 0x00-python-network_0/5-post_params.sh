#!/bin/bash
# Takes a URL, sends a POST request to the passed URL, and displays the reponse's body
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" $1
