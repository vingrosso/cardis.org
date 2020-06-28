# cardis.org
Cardis conference public web site


# Notes for testing locally

## Install jekyll and dependencies
gem install github-pages jekyll bundler
bundle update
bundle install


## Build locally (and rebuild on change)
bundle exec jekyll build  --watch & 

## Test locally (spawns a web server) 
bundle exec jekyll serve

