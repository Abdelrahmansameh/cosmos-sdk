#!/usr/bin/env python3

from . import lib


def process_raw_genesis(genesis, parsed_args):
    # update genesis with breaking changes
    genesis['consensus_params']['block'] = genesis['consensus_params']['block_size']
    del genesis['consensus_params']['block_size']

    # Add subkey list to each account
    for acc in genesis['accounts']:
        acc['subkeys'] = []

    # Set new chain ID and genesis start time
    genesis['chain_id'] = parsed_args.chain_id.strip()
    genesis['genesis_time'] = parsed_args.start_time

    return genesis


if __name__ == '__main__':
    parser = lib.init_default_argument_parser(
        prog_desc='Adding subkey to accounts in genesis.json',
        default_chain_id='cosmoshub-n',
        default_start_time='2019-02-11T12:00:00Z',
    )
    lib.main(parser, process_raw_genesis)
