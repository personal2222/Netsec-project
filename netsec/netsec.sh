#!/usr/bin/env bash

# [TBU] error logging

# check for install
if [[ $1 == 'install' ]]
then
    chmod +x netsec.sh
    ln -sf $PWD/netsec.sh /usr/local/bin/netsec
    exit
fi

# check for help
if [[ $1 == '-h' || $# -eq 0 ]]
then
    echo -e "netsec: manages build, launch, and cleanup of postgres services\n"
    echo -e "usage: netsec COMMAND [OPTIONS]\n"

    echo "commands:"
    echo -e "\tbuild\tbuilds and launches services"
    echo -e "\tclean\tshuts down services and cleans up\n"

    echo "options:"
    echo -e "\t-i\tenter psql after launching services"
    echo -e "\t-v\tremove volumes after shutting down services"
    echo -e "\t-h\tdisplays help information\n"

    exit
fi

step=1

echo "[${step}] loading config vals..."
source config.sh
echo "[${step}] ...finished loading config vals"
(( step++ ))

if [[ $1 == 'build' ]]
then
    # load pg password at runtime
    echo POSTGRES_PASSWORD=${NETSEC_PG_PASS} >> pg-vars.env

    # build and launch pg service
    echo "[${step}] building services..."
    docker-compose up -d
    echo "[${step}] ...finished building services"
    (( step++ ))

    # check the db
    if [[ $2 == '-i' ]]
    then
        echo "[${step}] waiting for db to finish startup..."
        sleep 2s
        echo "[${step}] ...connecting to psql"
        docker exec -it pgdock_pgdb_1 psql -d pgnetsec -U pguser
        (( step++ ))
    fi

    # removes pg password after launch
    echo "[${step}] cleaning tmps..."
    sed -i.bak '$ d' pg-vars.env && rm pg-vars.env.bak
    echo "[${step}] ...finished cleaning tmps"
    (( step++ ))

    echo "build complete"
elif [[ $1 == 'clean' ]]
then
    # remove container and network
    if [[ $(docker container ls -a | grep -c $container_name) -ge 1 ]]
    then
        echo "[${step}] shuting down services..."
        docker-compose down
        echo "[${step}] ...services shut down"
        (( step++ ))
    fi

    # remove volume
    if [[ $2 == '-v' && $(docker volume ls | grep -c $volume_name) -ge 1 ]]
    then
        echo "[${step}] removing volumes..."
        docker volume rm $volume_name
        echo "[${step}] volumes removed..."
        (( step++ ))
    fi

    echo "netsec all clean"
    exit
fi
