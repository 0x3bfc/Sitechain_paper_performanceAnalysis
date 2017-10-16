#!/bin/bash
nohup bash -c 'for i in {1..50} ; do ./star.sh $i ; done'&
nohup bash -c 'for i in {51..100} ; do ./star.sh $i ; done'&
nohup bash -c 'for i in {101..150} ; do ./star.sh $i ; done'&
nohup bash -c 'for i in {151..200} ; do ./star.sh $i ; done'&
nohup bash -c 'for i in {201..250} ; do ./star.sh $i ; done'&
