#!/bin/bash

my_fcn() {
    for i in 0 1 2
    do
        for j in 0 1 2 3
        do
            for k in 1 2 3 4 5 6
            do
                python my_copy.py i j k
            done
        done
    done
}
