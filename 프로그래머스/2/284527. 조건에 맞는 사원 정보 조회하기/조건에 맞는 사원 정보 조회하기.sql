SELECT HG.SCORE, HG.EMP_NO, HE.EMP_NAME, HE.POSITION, HE.EMAIL
FROM (SELECT EMP_NO, SUM(SCORE) AS SCORE
     FROM HR_GRADE
     GROUP BY EMP_NO, YEAR
     ORDER BY SCORE DESC
     LIMIT 1) HG
JOIN HR_EMPLOYEES HE ON HG.EMP_NO = HE.EMP_NO