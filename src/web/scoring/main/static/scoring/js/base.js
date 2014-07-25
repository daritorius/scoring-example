Score = window.Score || {};
Score.data = Score.data || {};

Score.data.index = {

    score: '',
    scoreUrl: '',

    init: function () {
        this.initRandomScore();
        this.initUserScore();
        this.initScoreForm();
        this.initFormValidation();
        this.initFacebookBut();
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

    initUserScore: function () {
        var self = this;
        var g2 = new JustGage({
            id: "randomGauge2",
            value: self.score,
            min: -300,
            max: 300,
            levelColors: [
                "#ec2026",
                "#f58120",
                "#9bd241"
            ]
        });
    },

    initScoreForm: function () {
        $('.rateme').on('click', function (e) {
            e.preventDefault();
            $('.hide-this').fadeOut('400', function () {
                $('.show-this').fadeIn('400');
            });
        });
    },

    initFormValidation: function () {
        var self = this;

        $('.rateme2').on('click', function (e) {
            e.preventDefault();
            var inputVal1 = $('#userName');
            var inputVal2 = $('#userName2');
            var inputVal3 = $('#userName3');
            var inputVal4 = $('#userBirthday');

            var inputVal11 = inputVal1.val();
            var inputVal22 = inputVal2.val();
            var inputVal33 = inputVal3.val();
            var inputVal44 = inputVal4.val();

            if (inputVal11 != "" && inputVal22 != "" && inputVal33 != "" && inputVal44 != "") {
                $('.ui-state-error').fadeOut('400');
                $('.show-this').fadeOut('400', function () {
                var data = {name: inputVal11, name2: inputVal22, name3: inputVal33, date: inputVal44 };
                    $.ajax({
//                        url: self.scoreUrl,
                        data: data,
                        beforeSend: function () {
                            $('.ajax img').show();
                        },
                        success: function () {
                            $('.ajax img').hide();
                            $('.show-this2').fadeIn('400');
                            $('#message_sent').fadeIn();
                        }
                    });
                });
            }
            else {
                $('.ui-state-error').fadeIn('400');
            }
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
