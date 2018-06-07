var gulp = require('gulp');
var notify = require("gulp-notify");

gulp.task('copyJquery',function(){
    gulp.src('./bower_components/sbadmin/vendor/jquery/jquery.min.js')
        .pipe(gulp.dest('./static/vendor/js/'));
    gulp.src('./bower_components/sbadmin/vendor/jquery-easing/jquery.easing.min.js')
        .pipe(gulp.dest('./static/vendor/js/'));
});

gulp.task('copyFontAwesome',function(){
    gulp.src('./bower_components/sbadmin/vendor/font-awesome/fonts/*')
        .pipe(gulp.dest('./static/vendor/fonts'));
    gulp.src('./bower_components/sbadmin/vendor/font-awesome/fonts/*')
        .pipe(gulp.dest('./static/vendor/css/fonts'));
    gulp.src('./bower_components/sbadmin/vendor/font-awesome/css/font-awesome.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
});

gulp.task('sbAdmin',function(){
    gulp.src('./bower_components/sbadmin/css/sb-admin.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
    gulp.src('./bower_components/sbadmin/js/sb-admin.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
    gulp.src('./bower_components/sbadmin/js/sb-admin-charts.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
    gulp.src('./bower_components/sbadmin/js/sb-admin-datatables.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
});

gulp.task('momentJs',function(){
    gulp.src('./bower_components/momentjs/min/moment.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
});

gulp.task('bootstrap',function(){
    gulp.src('./bower_components/bootstrap/dist/css/bootstrap.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
//    gulp.src('./bower_components/sbadmin/vendor/datatables/dataTables.bootstrap4.css')
//        .pipe(gulp.dest('./static/vendor/css'));
    gulp.src('./bower_components/sbadmin/vendor/bootstrap/js/bootstrap.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
//    gulp.src('./bower_components/sbadmin/vendor/bootstrap/js/bootstrap.bundle.min.js')
//        .pipe(gulp.dest('./static/vendor/js'));
});


gulp.task('select2',function(){
    gulp.src('./bower_components/select2/dist/js/select2.min.js')
        .pipe(gulp.dest('./static/vendor/js'));
    gulp.src('./bower_components/select2/dist/css/select2.min.css')
        .pipe(gulp.dest('./static/vendor/css'));
});


gulp.task('default', ['copyJquery','copyFontAwesome','sbAdmin','momentJs','select2','bootstrap'],
function() {
    notify({message: 'Ready for distribution!'})
});