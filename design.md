# DESIGN

## Language?

    * python
    * c#
    * c++
    * javascript
      * react
      * angular 

## v1: Console App

    * visualize in console?
      * redraw screen after events?
      * 2 teams: enemies on left, allies on right
      * redraw()
        * after each turn
      * classic rectangles
        * 1/3rd allies (right)
        * 2/3rds enemies (left, middle)
      * formation
        * front, back
        * 4 rows


## Characters

    * properties
      * hp
      * mp
      * speed
      * sprite
      * stagger gauge
        * phases
          * buildup
            * gauge fills up
          * staggered
            * notification: STAGGER!
            * gauge depletes
              * timer
              * reset ATB to zero; pause

## Commands

    * properties
      * close range, long range
      * resource
        * mp
          * amount
          * none (physical)

## ATB System

    * time
      * what library
    * During action: active or pause?