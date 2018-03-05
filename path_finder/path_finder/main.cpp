//
//  main.cpp
//  path_finder
//
//  Created by Aleksandar Babunovic on 2018-03-03.
//  Copyright © 2018 Aleksandar Babunovic. All rights reserved.
//
#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;


#include "lib/Node.h"
#include "lib/Point2D.h"

void toCharArray(string, char*);

int main(int argc, const char * argv[]) {
    Point2D* pos = new Point2D(1,4);
    Node* n = new Node(nullptr, "Test", *pos);
    std::cout << n->getName();

    return 0;
}

void toCharArray(string str, char* result){
    strcpy(result, str.c_str());
}
