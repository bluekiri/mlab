var gulp = require('gulp');
var notify = require("gulp-notify");

gulp.task('copyJquery',function(){
    gulp.src('./bower_components/jquery/dist/jquery.min.js')
        .pipe(gulp.dest('./static/js/'));
});

gulp.task('copyFontAwesome',function(){
    gulp.src('./bower_components/font-awesome/fonts/*')
        .pipe(gulp.dest('./static/fonts'));
    gulp.src('./bower_components/font-awesome/css/font-awesome.min.css')
        .pipe(gulp.dest('./static/css/main'));
});

gulp.task('sbAdmin2',function(){
    gulp.src('./bower_components/startbootstrap-sb-admin-2-blackrockdigital/dist/css/*')
        .pipe(gulp.dest('./static/css/main'));
    gulp.src('./bower_components/startbootstrap-sb-admin-2-blackrockdigital/dist/js/*')
        .pipe(gulp.dest('./static/js'));
});

gulp.task('momentJs',function(){
    gulp.src('./bower_components/momentjs/min/moment.min.js')
        .pipe(gulp.dest('./static/js'));
});


gulp.task('select2',function(){
    gulp.src('./bower_components/select2/dist/js/select2.min.js')
        .pipe(gulp.dest('./static/js'));
    gulp.src('./bower_components/select2/dist/css/select2.min.css')
        .pipe(gulp.dest('./static/css/main'));
});


gulp.task('default', ['copyJquery','copyFontAwesome','sbAdmin2','momentJs','select2'], function() {
    notify({message: 'Ready for distribution!'})
});