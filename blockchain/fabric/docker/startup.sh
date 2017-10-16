#!/bin/bash
echo $(date +%s) > outputs/file_$1.txt
peer chaincode invoke -n mycc -c '{"Args":["set", "a", "20"]}' -C myc
echo $(date +%s) >> outputs/file_$1.txt
