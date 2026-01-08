Breadth First search BFS

        CREATE empty queue Q
        CREATE empty set Visited
        ADD StartNode to Visited
        ENQUEUE StartNode into Q

        WHILE Q is not empty DO
            CurrentNode ← DEQUEUE Q
            VISIT CurrentNode

            FOR each Neighbor of CurrentNode in Graph DO
                IF Neighbor not in Visited THEN
                    ADD Neighbor to Visited
                    ENQUEUE Neighbor into Q
                END IF
            END FOR
        END WHILE


Depth first search

    CREATE empty set Visited
    CALL DFS_Visit(StartNode)
    DFS_Visit(Node)
        ADD Node to Visited
        VISIT Node
        FOR each Neighbor of Node in Graph DO
            IF Neighbor not in Visited THEN
                CALL DFS_Visit(Neighbor)
            END IF
        END FOR
    END DFS_Visit
