Ember.Handlebars.helper('date', function(date) {
    return moment(date['$date']).format('MMMM D, YYYY');
});