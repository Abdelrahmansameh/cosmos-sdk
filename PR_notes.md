notes concerning pull request
Hackathon Cosmos/Tendermint - Team SubK

# Gaia
- auto installer Hackathon-Gaia/shell.py
  (not production ready but might be a good feature to add)
- cmd/gaia/app/genesis.go
  probably to be stashed - replacing BaseAccount by SubKeyAccount

# Errors
- 2 new errors codes, idk if it should be standard so some errors

# Auth
everything else

# Missing
RemoveOld we need to reset daily each Transaction Fee Used to 0
however we have issues interacting with the store

# cobra
GetAccountCmd should work
the stringer currently prints only the number of keys,
but we can print each subkey stringer by changing to %v
TODO provide CLI for
add subk
show metadata
revoke subk


# tests

