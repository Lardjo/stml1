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

Ember.Handlebars.helper('ranked', function(lobby_type) {
    if (lobby_type == 7) {
        return 'Ranked';
    } else {
        return 'Unranked';
    }
});

Ember.Handlebars.helper('lobby', function(lobby_type) {

    var lobbies = {
            0: {'name' : 'Public'},
            1: {'name' : 'Practice'},
            2: {'name' : 'Tournament'},
            3: {'name' : 'Tutorial'},
            4: {'name' : 'Co-op With Bots'},
            5: {'name' : 'Team match'},
            6: {'name' : 'Solo Queue'},
            7: {'name' : 'Ranked'}
    };

    if (lobby_type in lobbies) {
        return lobbies[lobby_type]['name'];
    } else {
        return 'Unknown';
    }
});

Ember.Handlebars.helper('game-mode', function(game_mode) {

    var mode = {
        0: {'name': 'Unknown'},
        1: {'name': 'All Pick'},
        2: {'name': 'Captains Mode'},
        3: {'name': 'Random Draft'},
        4: {'name': 'Single Draft'},
        5: {'name': 'All Random'},
        7: {'name': 'Diretide'},
        9: {'name': 'Greeviling'},
        12: {'name': 'Least Played'},
        13: {'name': 'Limited Hero'},
        14: {'name': 'Compendium Matchmaking'},
        15: {'name': 'The Year Beast'}, /*Wraith-Night*/
        16: {'name': 'Captains Draft'},
        17: {'name': 'Balanced Draft'},
        18: {'name': 'Ability Draft'}
    };

    if (game_mode in mode) {
        return mode[game_mode]['name'];
    } else {
        return 'Unknown';
    }
});

Ember.Handlebars.helper('cluster', function(cluster_id) {

    var cluster = {
        0: {'name': 'Unknown'},
        111: {'name': 'US West'},
        112: {'name': 'US West'},
        114: {'name': 'US West'},
        121: {'name': 'US East'},
        122: {'name': 'US East'},
        123: {'name': 'US East'},
        124: {'name': 'US East'},
        131: {'name': 'Europe'},
        132: {'name': 'Europe'},
        133: {'name': 'Europe'},
        134: {'name': 'Europe'},
        135: {'name': 'Europe'},
        136: {'name': 'Europe'},
        142: {'name': 'Hong Kong'},
        143: {'name': 'Hong Kong'},
        151: {'name': 'China'},
        152: {'name': 'China'},
        153: {'name': 'China'},
        161: {'name': 'Japan'},
        163: {'name': 'China'},
        171: {'name': 'Australia'},
        191: {'name': 'Europe East'},
        181: {'name': 'Russia'},
        182: {'name': 'Russia'},
        183: {'name': 'Russia'},
        184: {'name': 'Russia'},
        185: {'name': 'Russia'},
        186: {'name': 'Russia'},
        200: {'name': 'South America'},
        204: {'name': 'South America'},
        211: {'name': 'South Africa'},
        212: {'name': 'South Africa'},
        213: {'name': 'South Africa'},
        221: {'name': 'China'},
        222: {'name': 'China'}
    };

    if (cluster_id in cluster) {
        return cluster[cluster_id]['name'];
    } else {
        return 'Unknown';
    }
});
