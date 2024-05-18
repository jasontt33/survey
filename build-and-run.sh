#!/bin/bash


docker build -t survey .


docker run -p 5000:5000 survey
