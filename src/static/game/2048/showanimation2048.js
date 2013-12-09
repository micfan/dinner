/**
 * Created by MXW on 2015/3/11.
 */
(function(global){

    global.showanimation2048 = {
        showNumberWithAnimation: showNumberWithAnimation,
        showMoveAnimation: showMoveAnimation,
        updateScore: updateScore
    };

    var support = global.support2048;

    function showNumberWithAnimation(i, j, randNumber){
        var numberCell = $("#number-cell-" + i + "-" + j);

        numberCell.css('background', support.getNumberBackgroundColor(randNumber));
        numberCell.css('color', support.getNumberColor(randNumber));
        numberCell.text(randNumber);

        numberCell.animate({
            width: cellSideLength,
            height: cellSideLength,
            top: support.getPosTop(i, j),
            left: support.getPosLeft(i, j)
        }, 50);
    }

    function showMoveAnimation(fromx, fromy, tox, toy){
        var numberCell = $("#number-cell-" + fromx + "-" + fromy);
        numberCell.animate({
            top: support.getPosTop(tox, toy),
            left: support.getPosLeft(tox, toy)
        }, 200);
    }

    function updateScore(score){
        $('#score').text(score);
    }

})(window);
