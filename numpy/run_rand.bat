rem@echo off
Setlocal EnableDelayedExpansion

set prefix=0000
set count=4
set prefix_threshold=10

for /l %%x in (1, 1, 100) do (
    if %%x == !prefix_threshold! ( set prefix=!prefix:~0,-1!
        set /a prefix_threshold*=10 )
    echo prefix_threshold = !prefix_threshold!
    call python rand.py %%x > !prefix!%%x.txt
    )
    
endlocal