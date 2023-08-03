/* selecting  all shows contained in hbtn_0d_tvshows
 that have at least one genre linked */
SELECT tv_show.title, tv_show_genre.genre_id
FROM tv_shows INNER  JOIN tv_show_genres
ON tv_show_id = tv_show_genre_id
ORDER BY tv_show_genres.genre_id
