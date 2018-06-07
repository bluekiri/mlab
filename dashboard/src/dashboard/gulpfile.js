var gulp = require('gulp');
var notify = require("gulp-notify");

gulp.task('jquery',function(){
    gulp.src('./bower_components/jquery/dist/jquery.min.js')
        .pipe(gulp.dest('./static/vendor/js/'));
    gulp.src('./bower_components/jquery-ui/jquery-ui.min.js')
        .pipe(gulp.dest('./static/vendor/js/'));

    gulp.src('./bower_components/jquery-sparkline/dist/jquery.sparkline.min.js')
        .pipe(gulp.dest('./static/vendor/js/'));

    gulp.src('./bower_components/jquery-knob/dist/jquery.knob.min.js')
        .pipe(gulp.dest('./static/vendor/js/'));
    gulp.src('./bower_components/jquery-slimscroll/jquery.slimscroll.min.js')
        .pipe(gulp.dest('./static/vendor/js/'));

});

gulp.task('fontAwesomeAndIcons',function(){
    gulp.src('./bower_components/font-awesome/css/font-awesome.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
    gulp.src('./bower_components/font-awesome/fonts/*')
        .pipe(gulp.dest('./static/vendor/fonts'));
    gulp.src('./bower_components/Ionicons/css/ionicons.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
});

gulp.task('adminLte',function(){
    gulp.src('./bower_components/admin-lte/dist/css/AdminLTE.min.css')
        .pipe(gulp.dest('./static/vendor/css'));

    gulp.src('./bower_components/admin-lte/dist/css/skins/_all-skins.min.css')
        .pipe(gulp.dest('./static/vendor/css/skins'));
});

gulp.task('plugins',function(){
    gulp.src('./bower_components/admin-lte/plugins/**/*')
        .pipe(gulp.dest('./static/vendor/plugins/'));

    gulp.src('./bower_components/morris.js/morris.css')
        .pipe(gulp.dest('./static/vendor/plugins/morris/'));
    gulp.src('./bower_components/morris.js/morris.min.js')
        .pipe(gulp.dest('./static/vendor/plugins/morris/'));

    gulp.src('./bower_components/bootstrap-datepicker/dist/css/bootstrap-datepicker3.css')
        .pipe(gulp.dest('./static/vendor/plugins/datepicker/'));

    gulp.src('./bower_components/bootstrap-daterangepicker/daterangepicker.css')
        .pipe(gulp.dest('./static/vendor/plugins/daterangepicker/'));
});

gulp.task('bootstrap',function(){
    gulp.src('./bower_components/bootstrap/dist/css/bootstrap.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
    gulp.src('./bower_components/bootstrap/dist/js/bootstrap.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
});


gulp.task('select2',function(){
    gulp.src('./bower_components/select2/dist/js/select2.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
    gulp.src('./bower_components/select2/dist/css/select2.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
});
gulp.task('raphael',function(){
    gulp.src('./bower_components/raphael/raphael.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
});

gulp.task('moment',function(){
    gulp.src('./bower_components/moment/min/moment.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
});


gulp.task('fastclick',function(){
    gulp.src('./bower_components/fastclick/lib/fastclick.js')
        .pipe(gulp.dest('./static/vendor/js'));
});

gulp.task('default', ['jquery','fontAwesomeAndIcons','adminLte','plugins','bootstrap','select2','raphael','moment','fastclick'],
function() {
    notify({message: 'Ready for distribution!'})
});