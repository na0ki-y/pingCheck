# IP addrese(zsh)
 ` ` `
$ifconfig en0 | awk '$1 == "inet" {print $2}'
 ` ` `



zsh ./demon_checer/checker.sh