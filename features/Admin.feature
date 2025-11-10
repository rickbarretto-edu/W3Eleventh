Feature: Admin Management

    Scenario: Registering a New Admin
        Given I am an Admin 
            And I want to register a new admin
        When I register the admin
        Then the new admin should be registered successfully

    Scenario: Listing All Admins
        Given I am an Admin 
            And there are multiple admins registered
        When I list all admins
        Then I should see the list of all registered admins

    Scenario: Verifying Admin Privileges
        Given I am a user
        When I try to access admin functionalities
        Then the admin privileges should be verified for me
