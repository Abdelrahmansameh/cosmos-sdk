package cli

import (
	"fmt"

    "github.com/cosmos/cosmos-sdk/client/context"
    "github.com/cosmos/cosmos-sdk/codec"
	"github.com/cosmos/cosmos-sdk/x/auth"
	"github.com/spf13/cobra"
)


func GetCmdAddSubKey(cdc *codec.Codec) *cobra.Command {
    return &cobra.Command{
        Use: "addsubkey [account] [dailyfeeallowance] [optional:routes]",
        Short: "adds subkey to account with maximum dailyfee",
        Args: cobra.MinimumNArgs(1),
        RunE: func(cmd *cobra.Command, args []string) error {
            // do something
			return nil
		},
    }
}

func GetCmdShowSubKey(cdc *codec.Codec) *cobra.Command {
    return &cobra.Command{
        Use: "subkey [acc] [subkeyidx]",
        Short: "shows metadata about subkey",
        RunE: func(cmd *cobra.Command, args []string) error {
            // assert valid
            // print it (can probably use stringer with %v)
			return nil
		},
    }
}

func GetCmdRevokeSubKey(cdc *codec.Codec) *cobra.Command {
    return &cobra.Command{
        Use: "revoke [account] [subkeyindex]",
        Short: "revokes subkey"
        Args: cobra.ValidArgs(2),
        RunE: func(cmd *cobra.Command, args []string) error {
            // check not revoked
            // revokeit
            // success
			return nil
		},
    }
}

