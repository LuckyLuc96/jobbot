#!/bin/bash
set -o noclobber
echo Setting up the default variables..
printf 'profile_path = "/home/%s/.mozilla/firefox/SeeInstructionsToCreateANewProfile"\ngeckodriver_path = "/home/%s/.cache/selenium/geckodriver/linux64/0.34.0/geckodriver"\n' "$USER" "$USER" > profilenames.py
