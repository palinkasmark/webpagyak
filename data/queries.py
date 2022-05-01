from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_all_shows_with_episodes_number():
    return data_manager.execute_select("SELECT shows.id, shows.title,  count(episode_number) \
        FROM shows \
        inner join seasons on seasons.show_id = shows.id \
        inner join episodes on episodes.season_id = seasons.show_id \
        group by shows.id, shows.title;")
