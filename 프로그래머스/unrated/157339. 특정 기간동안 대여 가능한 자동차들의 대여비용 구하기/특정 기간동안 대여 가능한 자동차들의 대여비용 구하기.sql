# -- 코드를 입력하세요
SELECT a.CAR_ID, a.CAR_TYPE, ROUND(30 * a.DAILY_FEE * (100 - c.DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS a JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS c
    ON a.CAR_TYPE = c.CAR_TYPE
WHERE a.CAR_ID NOT IN (SELECT CAR_ID
                      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                      WHERE END_DATE >= '2022-11-01'
                      AND START_DATE < '2022-12-01')
AND a.CAR_TYPE IN ('세단', 'SUV')
AND c.DURATION_TYPE = '30일 이상'
GROUP BY a.CAR_ID
HAVING FEE BETWEEN 500000 AND 1999999
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC