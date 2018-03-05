//
//  Node.h
//  path_finder
//
//  Created by Aleksandar Babunovic on 2018-03-05.
//  Copyright © 2018 Aleksandar Babunovic. All rights reserved.
//

#ifndef Node_h
#define Node_h

#include "Point2D.h"

class Node {
private:
    Node** neighbours;
    char* name;
    Point2D pos;
    
    
public:
    Node(Node**, char*, Point2D);
    ~Node();
    Node** getNeighbours();
    char* getName();
};

#endif /* Node_h */
