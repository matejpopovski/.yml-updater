# .yml-updater

DBT™ is a SQL-first transformation workflow that lets teams quickly and collaboratively deploy analytics code following software engineering best practices like modularity, portability, CI/CD, and documentation.

Recently, the company DBT introduced a change in the .yml file structure, renaming "tests:" to "data_tests:". To adapt to this update in a data pipelining project that uses DBT, I developed a Python script that automatically renames all instances of "tests:" to "data_tests:" within every .yml file. This automation ensured consistency with the new structure, saving significant time and enhancing the efficiency of our pipeline maintenance.
