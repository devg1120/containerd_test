nerdctl  ps -a
nerdctl  rm -vf $(docker ps -aq)
nerdctl  ps -a
