App.Player = DS.Model.extend({
    persona_name : DS.attr('string'),
    steam_id : DS.attr('string'),
    real_name : DS.attr('string'),
    registration : DS.attr(),
    avatar : DS.attr('string'),
    updated : DS.attr()
});