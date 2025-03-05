# Steps to Define Custom Permissions

    ## 1. Add a Meta Class to Your Model:
        - Inside the Meta class, define the permissions attribute as a list of tuples.

    ## 2. Specify Custom Permissions:
        - Each tuple in the permissions list should contain two strings:
            - The permission codename (a unique identifier for the permission).
            - The permission name (a human-readable description of the permission).

    ## 3. Run Migrations:
        - After defining custom permissions, create and apply migrations to update the database.