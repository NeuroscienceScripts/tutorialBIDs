This folder contains scripts for TBSS analysis.

Most scripts have the following code block: 
```
if [[ $i -lt 10 ]];
then
        sub='sub-00'$i

elif [[ $i -lt 100 ]]
then
        sub='sub-0'$i
else
        sub='sub-'$i
fi
```
    
This assumes your subject folders are all 3 characters long (ie. 001 for subject 1).  If this isn't your setup, remove the code block and replace it with "sub=i"
        
      

