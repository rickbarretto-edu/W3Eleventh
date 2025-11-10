Feature: Trade Cards

    Scenario: Accepted Trade
        Given a Trader A owning Card X
            And a Trader B owning Card Y
            And the Trader A has Trader B address
        When Trader A proposes to trade Card X for Card Y to Trader B
            And Trader B accepts the trade proposal
        Then Trader A should own Card Y but not Card X
            And Trader B should own Card X but not Card Y

    Scenario: Rejected Trade
        Given a Trader A owning Card X
            And a Trader B owning Card Y
            And the Trader A has Trader B address
        When Trader A proposes to trade Card X for Card Y to Trader B
            And Trader B rejects the trade proposal
        Then Trader A should still own Card X
            And Trader B should still own Card Y
