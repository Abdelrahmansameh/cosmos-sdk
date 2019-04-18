#!/bin/bash

cd $HOME

sudo rm -rf .gaiacli .gaiad

gaiad init --chain-id=BC Blockchain

echo "Adding validator, normal_user, restricted_user"
gaiacli keys add validator
gaiacli keys add normal_user
gaiacli keys add restricted_user

gaiad add-genesis-account $(gaiacli keys show validator -a) 1000000000stake,1000000000validatortoken
gaiad add-genesis-account $(gaiacli keys show normal_user -a) 10000uatom
gaiad add-genesis-account $(gaiacli keys show restricted_user -a)

gaiad gentx --name validator

gaiad collect-gentxs > /dev/null

echo "Installation finished. Run 'gaiad start' to start"
