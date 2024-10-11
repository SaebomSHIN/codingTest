SELECT TITLE, GB.BOARD_ID, REPLY_ID, GR.WRITER_ID, GR.CONTENTS, DATE_FORMAT(GR.CREATED_DATE, "%Y-%m-%d") CREATED_DATE
FROM USED_GOODS_BOARD GB JOIN USED_GOODS_REPLY GR
USING(BOARD_ID)
WHERE GB.CREATED_DATE LIKE "2022-10-%"
ORDER BY GR.CREATED_DATE, TITLE;