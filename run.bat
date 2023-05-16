cd %~dp0
set name=geomod

CALL conda activate %name%
CALL jupyter book build .
CALL ghp-import -n -p -f _build/html
CALL conda env export -n %name% > %name%.yaml