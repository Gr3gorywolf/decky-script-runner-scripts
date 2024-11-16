#!/bin/bash
: '
----------metadata---------
title: Install Missing Interpreters
description: Installs ruby, php and nodejs
image:
author: Gr3gorywolf
version: 1.0.0
root: true
----------metadata---------
'
# Enable read-write mode on the system
echo "Enabling read-write mode..."
sudo steamos-readonly disable

#populate holo
sudo pacman-key --populate holo

#initializing keyring
sudo pacman-key --init

# Install Node.js and npm
echo "Installing Node.js and npm..."
sudo pacman -S --noconfirm nodejs npm

# Install Ruby
echo "Installing Ruby..."
sudo pacman -S --noconfirm ruby

# Install PHP
echo "Installing PHP..."
sudo pacman -S --noconfirm php

# Re-enable read-only mode on the system for stability
echo "Re-enabling read-only mode..."
sudo steamos-readonly enable

# Verify the installations
echo "Verifying installations..."
echo "Node.js version: $(node -v)"
echo "npm version: $(npm -v)"
echo "Ruby version: $(ruby -v)"
echo "PHP version: $(php -v)"

echo "Installation complete!"