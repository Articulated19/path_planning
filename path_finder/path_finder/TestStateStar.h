//
//  TestStateStar.h
//  path_finder
//
//  Created by Aleksandar Babunovic on 2018-03-05.
//  Copyright © 2018 Aleksandar Babunovic. All rights reserved.
//

#ifndef TestStateStar_h
#define TestStateStar_h

#include "TestCases.h"

class TestStateStar{
private:
    TestCases tests;
    
public:
    void runAllTests();
    void runTest(int);
};


#endif /* TestStateStar_h */
