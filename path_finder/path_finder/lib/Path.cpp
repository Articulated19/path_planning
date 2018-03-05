//
//  Path.cpp
//  path_finder
//
//  Created by Aleksandar Babunovic on 2018-03-05.
//  Copyright © 2018 Aleksandar Babunovic. All rights reserved.
//

#include <stdio.h>
#include "Path.h"

Path::Path(){
    
}

Path::~Path(){
    
}

Path::Path(int capacity){
    
}

int Path::path_length(){
    return length;
}

double Path::getCost(){
    return cost;
}

void Path::addNode(Node*){
    
}

Path Path::addNodeAndClone(Node*){
    
    return (*this);
}
