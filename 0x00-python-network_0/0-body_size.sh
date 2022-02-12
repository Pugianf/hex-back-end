#!/bin/bash
#Display the size od the bosy of the response
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
