
## Analysis of Random-Restart and First-Choice Hill Climbing Algorithms for N-Queens Problem
##### March 2024
##### ChineduA-source

 ## Random-Restart Hill Climbing

## Random-Restart Hill Climbing - Run 1:
- **Final Board Configuration:**
    ```
    . . Q . . . . .
    . . . . Q . . .
    . Q . . . . . .
    . . . . . . . Q
    . . . . . Q . .
    . . . Q . . . .
    . . . . . . Q .
    Q . . . . . . .
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 0.01757025718688965 seconds
- 

## Random-Restart Hill Climbing - Run 2 :
- **Final Board Configuration:**
    ```
     . . . . . Q . .
    . . Q . . . . .
    . . . . . . Q .
    . Q . . . . . .
    . . . . . . . Q
    . . . . Q . .
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 0.03177595138549805 seconds


## Random-Restart Hill Climbing - Run 3:
- **Final Board Configuration:**
    ```
    . Q . . . . . .
    . . . . . Q . .
    . . . . . . . Q
    . . Q . . . . .
    Q . . . . . . .
    . . . Q . . . .
    . . . . . . Q .
    . . . . Q . . .
    ```

- **Number of Attacking Pairs:** 0
- **Total Time:** 0.004366874694824219 seconds


## Random-Restart Hill Climbing - Run 4:
- **Final Board Configuration:**
    ```
    . . Q . . . . .
    . . . . . Q . .
    . . . . . . . Q
    Q . . . . . . .
    . . . . Q . . .
    . . . . . . Q .
    . Q . . . . . .
    . . . Q . . . .
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 0.01612687110900879

## Random-Restart Hill Climbing - Run 5:
- **Final Board Configuration:**
    ```
   . . . . . Q . .
    . . Q . . . . .
    . . . . . . Q .
    . Q . . . . . .
    . . . Q . . . .
    . . . . . . . Q
    Q . . . . . . .
    . . . . Q . . . 
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 0.12845706939697266 seconds

## Random-Restart Hill Climbing - Run 6 :
- **Final Board Configuration:**
    ```
    . Q . . . . . .
    . . . . . . . Q
    . . . . . Q . .
    Q . . . . . . .
    . . Q . . . . .
    . . . . Q . . .
    . . . . . . Q .
    . . . Q . . . .
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 

## Random-Restart Hill Climbing - Run 7:
- **Final Board Configuration:**
    ```
   
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 

## Random-Restart Hill Climbing - Run 8:
- **Final Board Configuration:**
    ```
   
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 


## Random-Restart Hill Climbing - Run 9:
- **Final Board Configuration:**
    ```
   
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 


## Random-Restart Hill Climbing - Run 10:
- **Final Board Configuration:**
    ```
   
    ```
- **Number of Attacking Pairs:** 0
- **Total Time:** 


## Random-Restart Hill Climbing Avgs:
- **Average time taken for 10 runs:** 0.05892345905303955 seconds
- **Average number of attacking pairs in final states:** 0.0


### Which algorithm is faster? Why?


### Conculsion 

Although First-Choice Hill Climbing evaluates fewer neighbors and eliminates the need for several restarts, it is generally faster in conclusion. If a good local minimum is discovered early on, it can converge to a solution rapidly. In certain situations, nevertheless, it might not be able to locate the global optimum. Random-Restart Hill Climbing, on the other hand, may take longer since it resets several times, but because it explores different configurations, it has a higher chance of discovering the global optimum.

Generally speaking, First-Choice Hill Climbing is faster if speed is your only concern. Random-Restart Hill Climbing, on the other hand, might take a little longer but has a higher likelihood of success if you're seeking for a higher probability of discovering the best answer.

