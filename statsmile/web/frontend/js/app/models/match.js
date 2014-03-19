App.Match = DS.Model.extend({
    radiant_win : DS.attr('boolean'),
    duration    : DS.attr('number'),
    start_time  : DS.attr('number'),
    cluster     : DS.attr('number'),
    first_blood_time : DS.attr('number'),
    lobby_type       : DS.attr('number'),
    game_mode        : DS.attr('number'),
    players          : DS.attr()
});