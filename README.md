# Graph Analysis 
Graph Analysis Implementation 

## Dependency
The implementation requires networkx 1.11 package

## Repo Structure
The repo structure is :

    ├── README.md 
    ├── run.sh
    ├── src
    │     └── __init__.py
    │     └── rollingMedian.py
    │     └── utils.py
    │     └── window.py
    ├── unittest
    ├── venmo_input
    │   └── venmo-trans.txt
    ├── venmo_output
    │   └── output.txt
    └── insight_testsuite
           ├── run_tests.sh
           └── tests
                └── test-1-venmo-trans
                │   ├── venmo_input
                │   │   └── venmo-trans.txt
                │   └── venmo_output
                │       └── output.txt
                └── test-null-insertion
                │   ├── venmo_input
                │   │   └── venmo-trans.txt
                │   └── venmo_output
                │       └── output.txt
                └── test-multi-insertions
                    ├── venmo_input
                    │   └── venmo-trans.txt
                    └── venmo_output
                        └── output.txt

## Usage
Use ./run.sh to run rollingMedian.py file with given input in venmo\_input/ folder.

Use ./unittest/run\_test.sh to run unittest python scripts. 


