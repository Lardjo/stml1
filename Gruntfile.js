module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
            dist: {
                options: {
                    style: 'compact'
                },
                files: {
                    'statsmile/web/static/css/app.css': 'statsmile/web/frontend/scss/app.scss'
                }
            }
        },

        emberTemplates: {
            compile: {
                options: {
                    templateBasePath: /statsmile\/web\/frontend\/js\/app\/templates\//
                },
                files: {
                    'statsmile/web/static/js/templates.js': 'statsmile/web/frontend/js/app/templates/**/*.hbs'
                }
            }
        },

        concat: {
            libs: {
                src: [
                    'statsmile/web/frontend/js/libs/jquery-2.1.0.min.js',
                    'statsmile/web/frontend/js/libs/bootstrap.min.js',
                    'statsmile/web/frontend/js/libs/handlebars-v1.3.0.js',
                    'statsmile/web/frontend/js/libs/ember-1.4.0.js',
                    'statsmile/web/frontend/js/libs/showdown.js',
                    'statsmile/web/frontend/js/libs/moment.min.js',
                    'statsmile/web/frontend/js/libs/toastr.min.js',
                    'statsmile/web/frontend/js/libs/dota.js'
                ],
                dest: 'statsmile/web/static/js/libs.js'
            },
            app: {
                src: 'statsmile/web/frontend/js/app/**/*.js',
                dest: 'statsmile/web/static/js/app.js'
            }
        },

        /*uglify: {
            options: {
                mangle: false
            },
            my_target: {
                files: {
                    'statsmile/web/static/js/libs.min.js': ['statsmile/web/static/js/libs.js']
                }
            }
        },*/

        watch: {
            sass: {
                files: [
                    'statsmile/web/frontend/scss/*.scss',
                    'statsmile/web/frontend/scss/app/*.scss',
                ],
                tasks: ['sass']
            },
            emberTemplates: {
                files: 'statsmile/web/frontend/js/app/templates/**/*.hbs',
                tasks: ['emberTemplates']
            },
            concat: {
                files: [
                    'statsmile/web/frontend/js/**/*.js',
                    '!statsmile/web/static/js/app.js',
                    '!statsmile/web/static/js/libs.js',
                    '!statsmile/web/static/js/templates.js'
                ],
                tasks: ['concat']
            }
        }
  });

    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-sass');
    /*grunt.loadNpmTasks('grunt-contrib-uglify');*/
    grunt.loadNpmTasks('grunt-ember-templates');

    // Default task(s).
    grunt.registerTask('default', ['sass', 'concat', 'emberTemplates']);
};