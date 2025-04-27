package main

import (
  "fmt"
  "log"
  "context"
  "os"

  "github.com/urfave/cli/v3"
)

func getprs() {
  fmt.Println("get-prs function!")
}

func main() {
    cmd := &cli.Command{
            Commands: []*cli.Command{
                {
                  Name:    "github",
                  Aliases: []string{"gh"},
                  Usage:   "tasks related to github",
                  Commands: []*cli.Command{
                    {
                      Name: "get-prs",
                      Aliases: []string{"prs"},
                      Usage: "Gets a list of open PRs",
                      Flags: []cli.Flag{
                        &cli.BoolFlag{Name: "format", Aliases: []string{"f"}},
                      },
                      Action: func (ctx context.Context, cmd *cli.Command) error{
                        getprs()
                        return nil
                      },
                    },
                  },
                },
            },
          }
    if err := cmd.Run(context.Background(), os.Args); err != nil {
        log.Fatal(err)
    }
}
