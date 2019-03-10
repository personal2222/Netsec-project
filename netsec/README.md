#netsec build

Manages the build, launch, and cleanup for postgres

## Install
1. Make sure you have docker installed
2. Add NETSEC_PG_PASS to .bash_profile
3. `sh netsec.sh install` from the netsect project dir
4. `netsec build` to build postgres service
5. `netsec clean -v` to shutdown service, clean context, and remove volumes
