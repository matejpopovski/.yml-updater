# .yml-updater

Recently, the company DBT introduced a change in the .yml file structure, renaming "tests:" to "data_tests:". To adapt to this update in a data pipelining project that uses DBT, I developed a Python script that automatically renamed all instances of "tests:" to "data_tests:" within every .yml file. This automation ensured consistency with the new structure, saving significant time and enhancing the efficiency of our pipeline maintenance.
