#!/bin/bash

sort log.txt | uniq | sponge log.txt
