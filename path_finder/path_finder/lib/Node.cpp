//
//  Node.cpp
//  path_finder
//
//  Created by Aleksandar Babunovic on 2018-03-03.
//  Copyright © 2018 Aleksandar Babunovic. All rights reserved.
//

#include "Node.h"



Node::Node(Node** neighbours, char* name, Point2D pos){
    this->neighbours = neighbours;
    this->name = name;
    this->pos = pos;
}

Node::~Node(){
    delete neighbours;
}

Node** Node::getNeighbours(){
    return neighbours;
}

char* Node::getName(){
    return name;
}
