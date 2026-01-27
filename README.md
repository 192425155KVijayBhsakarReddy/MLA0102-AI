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

UCS
	
	INSERT (0, Start) into PQ      // (cost, node)
	WHILE PQ not empty DO
    (Cost, Node) ← REMOVE node with minimum cost from PQ
    IF Node = Goal THEN
        PRINT "Goal Reached with cost", Cost
        EXIT
    END IF
   	 IF Node not in Visited THEN
       	 ADD Node to Visited
       	 FOR each Neighbor of Node DO
           	 INSERT (Cost + EdgeCost, Neighbor) into PQ
       	 END FOR
    	END IF
	END WHILE
    
Water Jug problem

        CREATE queue Q
        CREATE set Visited

        ENQUEUE (0,0)
        ADD (0,0) to Visited

        WHILE Q not empty DO
            (x,y) ← DEQUEUE Q

            IF x = Target OR y = Target THEN
                PRINT "Target Reached"
                EXIT
            END IF

        GENERATE possible states
            ADD unvisited states to Q
        END WHILE

        PRINT "Target Not Possible"  
GBFS

	CREATE priority queue PQ
	INSERT Start using heuristic

	WHILE PQ not empty DO
    	Node ← REMOVE lowest heuristic node
    	PRINT Node
    	IF Node = Goal THEN EXIT
    	INSERT neighbors into PQ
	END WHILE
A* Search

		CREATE priority queue PQ
	INSERT (f=0, Start)

	WHILE PQ not empty DO
   	 Node ← REMOVE node with lowest f
   	 IF Node = Goal THEN
        PRINT "Goal Reached"
        EXIT
   	 END IF
   	 	FOR each Neighbor DO
       	 g ← path cost
       	 f ← g + heuristic
       	 INSERT Neighbor into PQ
    	END FOR
	END WHILE
