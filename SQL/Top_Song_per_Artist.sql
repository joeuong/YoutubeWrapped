-- Create a Common Table Expression (CTE) named RANKEDSONGS
WITH RANKEDSONGS AS (
    -- Select the artist, title, count of listens, and assign a row number within each artist's group
    SELECT
        MI.G_ARTIST AS ARTIST,           -- Alias for artist column
        MI.G_TITLE AS TITLE,             -- Alias for title column
        COUNT(LH.SONG_URL) AS NUM,       -- Count of listens for each song
        ROW_NUMBER() OVER(PARTITION BY MI.G_ARTIST ORDER BY COUNT(LH.SONG_URL) DESC) AS RN
    FROM
        LISTEN_HISTORY LH
    JOIN
        MUSIC_INFO_GOOGLE_ONLY MI ON LH.SONG_URL = MI.SONG_URL
    GROUP BY
        MI.G_ARTIST,                     -- Group by artist
        MI.G_TITLE                       -- Group by title
)

-- Select the artist, title, and count of listens from the RANKEDSONGS CTE
SELECT
    ARTIST,
    TITLE,
    NUM
FROM
    RANKEDSONGS
WHERE
    RN = 1                               -- Filter only rows with row number = 1 (top song for each artist)

-- Order the final results by the count of listens in descending order
ORDER BY 
    NUM DESC;
