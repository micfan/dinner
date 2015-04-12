/**
 * Created by MXW on 2015/3/11.
 */

//随机数的产生有没有更巧妙的方法
//分数增加动画效果

(function(global){
    global.main2048 = {
        newgame: newgame,
        init: init,
        updateBoardView: updateBoardView,
        generateOneNumber: generateOneNumber
    };

    var board = new Array();
    var score = 0;
    var hasConflicted = new Array();
    var support = global.support2048;
    var showAnimation = global.showanimation2048;
    var times;

    //touchstart → touchend
    var startx = 0;
    var starty = 0;
    var endx = 0;
    var endy = 0;

    $(document).ready(function(){
        prepareForMobile();
        newgame();
        $("#newgamebutton").click(function(){
            newgame();
        });
    });

    function prepareForMobile(){

        if(documentWidth > 600){
            gridContainerWidth = 500;
            cellSideLength = 100;
            cellSpace = 20;
        }

        var gridContainer = $('#grid-container');
        var gridCell = $('.grid-cell');
        gridContainer.css({
            'width': gridContainerWidth - 2 * cellSpace,
            'height': gridContainerWidth - 2 * cellSpace,
            'padding': cellSpace,
            'border-radius': 0.02 * gridContainerWidth
        });

        gridCell.css({
            'width': cellSideLength,
            'height': cellSideLength,
            'border-radius': 0.02 * cellSideLength
        });
    }

    function newgame(){
        //初始化棋盘格
        init();
        //在随机两个格子生产数字
        //生成2个随机数
        generateOneNumber();
        generateOneNumber();
    }

    function isgameover(){
        if(support.noSpace(board) && support.noMove(board)){
            gameover();
        }

        if(score == 2048){
            alert("You win");
        }
    }

    function gameover(){
        alert("game over !!!");
    }

    function init(){
        //小格子位置
        for(var i = 0; i < 4; i++)
            for(var j = 0; j < 4; j++){
                var gridCeil = $("#grid-cell-" + i + "-" + j);
                gridCeil.css('top', support.getPosTop(i, j));
                gridCeil.css('left', support.getPosLeft(i, j));
            }
        // board是一个一维数组，声明成二维数组
        for(var i = 0; i < 4; i++){
            board[i] = new Array();
            hasConflicted[i] = new Array();
            //初始化值
            for(var j = 0; j < 4; j++){
                board[i][j] = 0;
                hasConflicted[i][j] = false;
            }
        }
        updateBoardView();
        score = 0;
    }

    function updateBoardView(){
        //    number-cell声明(数字)
        $(".number-cell").remove();
        for(var i = 0; i < 4; i++)
            for(var j = 0; j < 4; j++){
                $("#grid-container").append('<div class="number-cell" id="number-cell-' + i + '-' + j + '"><div>');
                var theNumberCell = $("#number-cell-" + i + "-" + j);
                if(board[i][j] == 0){
                    theNumberCell.css('width', '0px');
                    theNumberCell.css('height', '0px');
                    theNumberCell.css('top', support.getPosTop(i, j) + cellSideLength / 2);
                    theNumberCell.css('left', support.getPosTop(i, j) + cellSideLength / 2);
                }
                else{
                    theNumberCell.css('width', cellSideLength);
                    theNumberCell.css('height', cellSideLength);
                    theNumberCell.css('top', support.getPosTop(i, j));
                    theNumberCell.css('left', support.getPosLeft(i, j));
                    theNumberCell.css('background-color', support.getNumberBackgroundColor(board[i][j]));
                    theNumberCell.css('color', support.getNumberColor(board[i][j]));
                    theNumberCell.text(board[i][j]);
                }
                hasConflicted[i][j] = false;
            }
        $('.number-cell').css({
            'line-height': cellSideLength+'px',
            'font-size': 0.6 * cellSideLength+'px'
        });
    }

    function generateOneNumber(){
        if(support.noSpace(board))
            return false;
        //随机一个位置
        //要显示的是整数
        //Math.random产生0~1之间的浮点数
        //Math.floor下取整，生成0, 1, 2, 3
        var randx = parseInt(Math.floor(Math.random() * 4));
        var randy = parseInt(Math.floor(Math.random() * 4));
        times = 0;

        /*
        while(true){
            if(board[randx][randy] == 0)
                break;
            randx = parseInt(Math.floor(Math.random() * 4));
            randy = parseInt(Math.floor(Math.random() * 4));
        }
        */

        while(times < 50){
            if(board[randx][randy] == 0)
                break;
            randx = parseInt(Math.floor(Math.random() * 4));
            randy = parseInt(Math.floor(Math.random() * 4));

            times++;
        }
        if(times == 50){
            for(var i = 0; i < 4; i++)
                for(var j = 0; j < 4; j++){
                    if(board[i][j] == 0){
                        randx = i;
                        randy = j;
                        break;
                    }
                }
        }

        //随机一个数字
        var randNumber = Math.random() < 0.5 ? 2 : 4;
        //在随机位置显示随机数字
        board[randx][randy] = randNumber;
        showAnimation.showNumberWithAnimation(randx, randy, randNumber);
        return true;
    }

    $(document).keydown(function(event){
        switch(event.keyCode){
            case 37://left
                event.preventDefault();
                if(moveLeft()){
                    setTimeout(generateOneNumber, 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
                break;
            case 38://up
                event.preventDefault();
                if(moveUp()){
                    setTimeout(generateOneNumber, 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
                break;
            case 39://right
                event.preventDefault();
                if(moveRight()){
                    setTimeout(generateOneNumber, 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
                break;
            case 40://down
                event.preventDefault();
                if(moveDown()){
                    setTimeout(generateOneNumber, 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
                break;
            default://default
                break;
        }
    });

    document.addEventListener('touchstart', function(event){
        // event存储了和事件相关的信息
        // touches[0]单点触控
        startx = event.touches[0].pageX;
        starty = event.touches[0].pageY;
    });

    document.addEventListener('touchmove', function(event){
        event.preventDefault();
    });

    document.addEventListener('touchend', function(event){
        // event存储了和事件相关的信息
        endx = event.changedTouches[0].pageX;
        endy = event.changedTouches[0].pageY;

        var deltax = endx - startx;
        var deltay = endy - starty;

        if(Math.abs(deltax) < 0.3 * documentWidth && Math.abs(deltay) < 0.3 * documentWidth)
            return;

        //x放向，deltax > deltay
        if(Math.abs(deltax) >= Math.abs(deltay)){
            if(deltax > 0){
                // move right
                if(moveRight()){
                    setTimeout(generateOneNumber(), 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
            }
            else{
                // move left
                if(moveLeft()){
                    setTimeout(generateOneNumber(), 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
            }
        }
        //y
        else{
            if(deltay > 0){
                // move down
                if(moveDown()){
                    setTimeout(generateOneNumber(), 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
            }
            else{
                // move up
                if(moveUp()){
                    setTimeout(generateOneNumber(), 210);
                    setTimeout(isgameover(), 300);
                }else{
                    isgameover();
                }
            }
        }
    });

    function moveLeft() {
        //判断当前的局势是否可以移动
        if (!support.canMoveLeft(board))
            return false;

        //真正的moveLeft.对每一个数字的左侧位置进行判断，看是否可能为落脚点
        //1.落脚位置是否为空？(i, j) = 0 没有数字
        //2.落脚位置数字和待判定元素数字相等
        //3.移动路径中是否有障碍物
        for (var i = 0; i < 4; i++)
            for (var j = 1; j < 4; j++){
                //当前职位不为零
                if (board[i][j] != 0) {
                    //(i,j)所有的左侧元素(i,k)
                    for (var k = 0; k < j; k++) {
                        // 左侧位置没有数字, 没有障碍物
                        // board[i][k] == 0表示(i,j)
                        // 1和3
                        if (board[i][k] == 0 && support.noBlockHorizontal(i, k, j, board)) {
                            //move
                            showAnimation.showMoveAnimation(i, j, i, k);
                            //add
                            board[i][k] = board[i][j];
                            board[i][j] = 0;
                            continue;
                        }
                        // 2和3
                        //!hasConflicted没有发生碰撞(对要移要的位置进行判断)
                        else if (board[i][k] == board[i][j] && support.noBlockHorizontal(i, k, j, board) && !hasConflicted[i][k]) {
                            //move
                            showAnimation.showMoveAnimation(i, j, i, k);
                            // 左侧位置有数字，和带移动数字一样
                            // add
                            board[i][k] += board[i][j];
                            board[i][j] = 0;
                            //add score
                            score += board[i][k];
                            showAnimation.updateScore(score);
                            hasConflicted[i][k] = true;
                            continue;
                        }
                    }
                }
            }
        setTimeout(updateBoardView(), 200);
        return true;
    }

    function moveUp(){
        if(!support.canMoveUp(board))
            return false;

        for(var i = 1; i < 4; i++)
            for(var j = 0; j < 4; j++){
                if(board[i][j] != 0){
                    for(var k = 0; k < i; k++){
                        if(board[k][j] == 0 && support.noBlockVertical(j, k, i, board)){
                            showAnimation.showMoveAnimation(i, j, k, j);
                            board[k][j] = board[i][j];
                            board[i][j] = 0;
                            continue;
                        }
                        else if(board[k][j] == board[i][j] && support.noBlockVertical(j, k, i, board) && !hasConflicted[k][j]){
                            showAnimation.showMoveAnimation(i, j, k, j);
                            board[k][j] += board[i][j];
                            board[i][j] = 0;
                            //add score
                            score += board[k][j];
                            showAnimation.updateScore(score);
                            hasConflicted[k][j] = true;
                            continue;
                        }
                    }
                }
            }
        setTimeout(updateBoardView, 200);
        return true;
    }

    function moveRight(){
        if(!support.canMoveRight(board))
            return false;

        for(var i = 0; i < 4; i++)
            for(var j = 2; j >= 0; j--){
                if(board[i][j] != 0){
                    for(var k = 3; k > j; k--){
                        // 当前位置右边位置的数字board[i][k] == 0
                        if(board[i][k] == 0 && support.noBlockHorizontal(i, j, k, board)){
                            showAnimation.showMoveAnimation(i, j, i, k);
                            board[i][k] = board[i][j];
                            board[i][j] = 0;
                            continue;
                        }
                        else if(board[i][k] == board[i][j] && support.noBlockHorizontal(i, j, k, board)  && !hasConflicted[i][k]){
                            showAnimation.showMoveAnimation(i, j, i, k);
                            board[i][k] += board[i][j];
                            board[i][j] = 0;
                            //add score
                            score += board[i][k];
                            showAnimation.updateScore(score);
                            hasConflicted[i][k] = true;
                            continue;
                        }
                    }
                }
            }
        setTimeout(updateBoardView, 200);
        return true;
    }

    function moveDown(){
        if(!support.canMoveDown(board))
            return false;

        for(var i = 2; i >= 0; i--)
            for(var j = 0; j < 4; j++){
                if(board[i][j] != 0){
                    for(var k = 3; k > i; k--){
                        if(board[k][j] == 0 && support.noBlockVertical(j, i, k, board)){
                            showAnimation.showMoveAnimation(i, j, k, j);
                            board[k][j] = board[i][j];
                            board[i][j] = 0;
                            continue;
                        }
                        else if(board[k][j] == board[i][j] && support.noBlockVertical(j, i, k, board) && !hasConflicted[k][j]){
                            showAnimation.showMoveAnimation(i, j, k, j);
                            board[k][j] += board[i][j];
                            board[i][j] = 0;
                            //add score
                            score += board[k][j];
                            showAnimation.updateScore(score);
                            hasConflicted[k][j] = true;
                            continue;
                        }
                    }
                }
            }
        setTimeout(updateBoardView, 200);
        return true;
    }
})(window);