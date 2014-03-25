var attr = DS.attr();

App.Match = DS.Model.extend({
    cluster          : attr,
    game_mode        : attr,
    first_blood_time : attr,
    start_time       : attr,
    radiant_win      : attr,
    duration         : attr,
    players          : attr
});