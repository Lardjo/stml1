/**
 * Created by Konstantin on 25.03.14.
 */
App.PlayersController = Ember.ArrayController.extend({
  sortProperties: ['win_rate'],
  sortAscending: false
});