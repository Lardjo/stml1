window.App = Ember.Application.create({
    LOG_TRANSITIONS: true
});
App.ApplicationAdapter = DS.RESTAdapter.extend();
App.ApplicationSerializer = DS.RESTSerializer.extend({
  primaryKey: 'match_id'
});