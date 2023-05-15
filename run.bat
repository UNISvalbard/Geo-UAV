cd %~dp0
CALL conda activate
CALL mamba activate geomod
CALL jupyter book build .
CALL ghp-import -n -p -f _build/html