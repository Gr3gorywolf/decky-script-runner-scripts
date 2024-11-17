#!/bin/bash
: '
----------metadata---------
title: Install Common Nodejs Packages 
description:[Requires node] Install common nodejs packages such as expressjs, node-fetch, joi, socket.io, lodash, and cheerio and axios
image:
author: Gr3gorywolf
version: 1.0.0
root: false
----------metadata---------
'
echo "Installing common nodejs dependencies"
npm install express node-fetch joi socket.io lodash cheerio axios
echo "Common dependencies installed"