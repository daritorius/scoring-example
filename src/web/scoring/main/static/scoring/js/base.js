Score = window.Score || {};
Score.data = Score.data || {};

Score.data.index = {

    score: '',
    scoreUrl: '',

    init: function () {
        this.initRandomScore();
//        this.initUserScore();
        this.initScoreForm();
        this.initFormValidation();
//        this.initFacebookBut();
    },

    initRandomScore: function () {
        var g = new JustGage({
            id: "randomGauge",
            value: getRandomInt(-300, 300),
            min: -300,
            max: 300,
            levelColors: [
                "#ec2026",
                "#f58120",
                "#9bd241"
            ]
        });
        setInterval(function () {
            g.refresh(getRandomInt(-300, 300));
        }, 2500);
    },

//    initUserScore: function () {
//        var self = this;
//        var g2 = new JustGage({
//            id: "randomGauge2",
//            value: self.score,
//            min: -300,
//            max: 300,
//            levelColors: [
//                "#ec2026",
//                "#f58120",
//                "#9bd241"
//            ]
//        });
//    },

    initScoreForm: function () {
        var self = this;
        $('.rateme').on('click', function (e) {
            e.preventDefault();
            $('.hide-this').fadeOut('400', function () {
                self.initMaskBirthday();
                $('.show-this').fadeIn('400');
            });
        });
    },

    initFormValidation: function () {
        var self = this;

        $('.rateme2').on('click', function (e) {
            e.preventDefault();
            var inputVal1 = $('#id_profile_third_name');
            var inputVal2 = $('#id_profile_first_name');
            var inputVal3 = $('#id_profile_second_name');
            var inputVal4 = $('#id_profile_birthday');

            var inputVal11 = inputVal1.val();
            var inputVal22 = inputVal2.val();
            var inputVal33 = inputVal3.val();
            var inputVal44 = inputVal4.val();

            if (inputVal11 != "" && inputVal22 != "" && inputVal33 != "" && inputVal44 != "") {
                $('.ui-state-error').fadeOut('400');
                $('.show-this').fadeOut('400', function () {
                    var data = $('.fill-scoring-data').serializeArray();
                    $.ajax({
                        url: self.scoreUrl,
                        type: 'post',
                        data: data,
                        beforeSend: function () {
                            $('.ajax img').show();
                        },
                        success: function (data) {
                            $('.ajax img').hide();
                            if (data.errors) {
                                $.each(data.errors, function (index, value) {
                                    var string = '<li><span class="error-title">' + value[1][1] + ':</span> ' + value[1][0] + '</li>';
                                    $('.list-errors').append(string);
                                });
                            } else {
                                $('.user-rating').html(data.score.rating);
                                $('.user-score').html(data.score.score);
                                self.initUserRate(parseInt(data.score.score));
                                $('.show-this2').fadeIn('400');
                                $('#message_sent').fadeIn();
                            }
                        },
                        statusCode: {
                            500: function() {
                                $('.ajax img').hide();
                                $('.hide-this').fadeOut('400', function () {
                                    $('.show-this').fadeIn('400');
                                });
                                $('.ui-state-error').fadeIn('400');
                            }
                        }
                    });
                });
            }
            else {
                $('.ui-state-error').fadeIn('400');
            }
        });
    },

    initMaskBirthday: function () {
        $("#id_profile_birthday").mask("99-99-9999");
    },

    initUserRate: function(score) {
        var g2 = new JustGage({
            id: "randomGauge2",
            value: score,
            min: -300,
            max: 300,
            levelColors: [
                "#ec2026",
                "#f58120",
                "#9bd241"
            ]
        });
    },

    initFacebookBut: function () {
        $('.rfacebook-but').on('click', function (e) {
            e.preventDefault();
        });
    }
};

$(function () {
    Score.data.index.init();
});
