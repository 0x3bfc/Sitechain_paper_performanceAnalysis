#!/bin/bash
nohup bash -c 'for i in {$1..$2}; do ./simulate.sh ; done' &
nohup bash -c 'for i in {$1..$2}; do ./simulate.sh ; done' &
echo $_
