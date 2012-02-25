heroku-app README
==================

Getting Started
---------------

- cd <directory containing this file>

- heroku create --stack cedar

- heroku addons:add shared-database

- git push heroku master

- heroku run 'python -m herokuapp.scripts.populate'
