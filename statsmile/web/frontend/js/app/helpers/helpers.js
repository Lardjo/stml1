Ember.Handlebars.helper('date-short', function(date){
    return moment.unix(date).utc().format('H:mm:ss');
});

Ember.Handlebars.helper('date-full', function(date){
    return moment.unix(date).utc().format('MMM D, YYYY');
});

Ember.Handlebars.helper('date', function(date){
    return moment(date['$date']).format('MMM D, YYYY H:m:ss Z');
});

Ember.Handlebars.helper('lobby', function(lobby_type) {
    if (lobby_type in lobbies) {
        return lobbies[lobby_type]['name'];
    } else {
        return 'Unknown';
    }
});

Ember.Handlebars.helper('mode', function(game_mode) {
    if (game_mode in game_modes) {
        return game_modes[game_mode]['name'];
    } else {
        return 'Unknown';
    }
});

Ember.Handlebars.helper('server', function(cluster) {
    if (cluster in clusters) {
        return clusters[cluster]['name'];
    } else {
        return 'Unknown';
    }
});