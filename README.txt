heroku-app README
==================

Getting Started
---------------

- cd <directory containing this file>

- heroku create --stack cedar

- heroku addons:add shared-database

- git push heroku master

Caveat
------

Current branch can't work on Heroku by the stack issue.
Use master branch until the issue solved.
