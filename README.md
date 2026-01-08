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
