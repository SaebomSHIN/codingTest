SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE 
    NAME LIKE '%Lucy%' 
    OR NAME = 'Ella' 
    OR NAME = 'Pickle' 
    OR NAME = 'Rogan' 
    OR NAME = 'Sabrina' 
    OR NAME LIKE '%Mitty%'
ORDER BY ANIMAL_ID ASC;