Ember.Handlebars.helper('format-duration', function(date){
    return moment.unix(date).utc().format('H:m:ss');
});

Ember.Handlebars.helper('format-time-date', function(date){
    return moment.unix(date).utc().format('MMM D, YYYY');
});

Ember.Handlebars.helper('format-time-time-gmt', function(date){
    return moment.unix(date).utc().format('HH:mm');
});

Ember.Handlebars.helper('first-blood', function(time){
    return moment.unix(time).utc().format('m:ss');
});

Ember.Handlebars.helper('date', function(date){
    return moment(date['$date']).format('MMM D, YYYY H:m:ss Z');
});

Ember.Handlebars.helper('ranked', function(lobby_type) {
    if (lobby_type == 7) {
        return 'Ranked';
    } else {
        return 'Unranked';
    }
});

Ember.Handlebars.helper('lobby', function(lobby_type) {
    if (lobby_type in lobbies) {
        return lobbies[lobby_type]['name'];
    } else {
        return 'Unknown';
    }
});

Ember.Handlebars.helper('game-mode', function(game_mode) {
    if (game_mode in game_modes) {
        return game_modes[game_mode]['name'];
    } else {
        return 'Unknown';
    }
});

Ember.Handlebars.helper('cluster', function(cluster_id) {
    if (cluster_id in clusters) {
        return clusters[cluster_id]['name'];
    } else {
        return 'Unknown';
    }
});

Ember.Handlebars.helper('item', function(item_id) {
    if (item_id in items) {
        return new Ember.Handlebars.SafeString(
            "<img src='/static/images/items/" + items[item_id]['avatar'] + ".png' />"
        );
    } else {
        return new Ember.Handlebars.SafeString(
            "<img src='/static/images/items/default.png' />"
        );
    }
});

Ember.Handlebars.helper('hero', function(hero_id) {
    if (hero_id in heroes) {
        return new Ember.Handlebars.SafeString(
            "<div class='hero-cont' data-toggle='tooltip' data-placement='left' title='"+ heroes[hero_id]['name'] +"'><img src='/static/images/heroes/" + heroes[hero_id]['avatar'] + ".png' /></div>"
        );
    } else {
        return new Ember.Handlebars.SafeString(
            "<div class='hero-cont' data-toggle='tooltip' data-placement='left' title='"+ heroes[hero_id]['name'] +"'><img src='/static/images/heroes/default.png' data-toggle='tooltip' data-placement='left' title='Unknown' /></div>"
        );
    }
});

Ember.Handlebars.helper('progress-kills', function(kills, deaths, assists) {
    var progress = 0;
    var sum = kills + deaths + assists;
    if (sum > 0) {
        progress = (kills * 100 / sum).toFixed(4);
    }
    return new Handlebars.SafeString(
      "<div class='progress-bar progress-bar-success' style='width:" + progress + "%'>" + kills + "</div>"
    );
});

Ember.Handlebars.helper('progress-deaths', function(kills, deaths, assists) {
    var progress = 0;
    var sum = kills + deaths + assists;
    if (sum > 0) {
        progress = (deaths * 100 / sum).toFixed(4);
    }
    return new Handlebars.SafeString(
        "<div class='progress-bar progress-bar-danger' style='width:" + progress + "%'>" + deaths + "</div>"
    );
});

Ember.Handlebars.helper('progress-assists', function(kills, deaths, assists) {
    var progress = 0;
    var sum = kills + deaths + assists;
    if (sum > 0) {
        progress = (assists * 100 / sum).toFixed(4);
    }
    return new Handlebars.SafeString(
        "<div class='progress-bar progress-bar-warning' style='width:" + progress + "%'>" + assists + "</div>"
    );
});