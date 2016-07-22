# --------------------------------------------------------------
#  aliases and other shorcuts
# --------------------------------------------------------------

alias l='ls -CF'
alias la='ls -aCF'
alias ll='ls -l'
alias lla='ls -al'
alias ltr='ls -ltr'

# alias sv='${HOME}/bin/set_dyn_view.pl'

[[ -x /usr/bin/emacs-nox ]]      && alias enox='emacs-nox'
[[ -x /usr/bin/emacs24-nox ]]    && alias enox='emacs24-nox'
[[ -x /usr/bin/emacs-24.3-nox ]] && alias enox='emacs-24.3-nox'

alias e='enox'

alias d='docker'
alias dr='docker run'
alias di='docker images'
alias dp='docker ps'
alias dcp='docker-compose'

alias g='git'
alias vir='vi -R'

# --------------------------------------------------------------
# eof
#