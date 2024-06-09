#!/bin/sh

sudo docker volume create media_volume
sudo docker volume create data_volume
sudo docker network create app_net
