App.Player = DS.Model.extend({
    persona_name : DS.attr(),
    avatar       : DS.attr(),
    profile_url  : DS.attr(),
    steam_id     : DS.attr(),
    real_name    : DS.attr(),
    badges       : DS.attr(),
    registration : DS.attr()
});