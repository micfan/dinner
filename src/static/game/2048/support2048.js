/**
 * Created by MXW on 2015/3/11.
 */

//20px + 120px * n
(function(global){

    global.support2048 = {
        getPosTop: getPosTop,
        getPosLeft: getPosLeft,
        getNumberBackgroundColor: getNumberBackgroundColor,
        getNumberColor: getNumberColor,
        noSpace: noSpace,
        canMoveLeft: canMoveLeft,
        canMoveUp: canMoveUp,
        canMoveRight: canMoveRight,
        canMoveDown: canMoveDown,
        noBlockHorizontal: noBlockHorizontal,
        noBlockVertical: noBlockVertical,
        noMove: noMove
    };

    // 获得现在运行的屏幕的宽度
    documentWidth = window.screen.availWidth;

    //游戏大方框的宽度
    gridContainerWidth = 0.92 * documentWidth;
    // 每个小格子
    cellSideLength = 0.18 * documentWidth;
    // 每个小格子间的宽度
    cellSpace = 0.04 * documentWidth;

    function getPosTop(i, j){
        return cellSpace + i * (cellSpace + cellSideLength);
    }

    function getPosLeft(i, j){
        return cellSpace + j * (cellSpace + cellSideLength);
    }

    function getNumberBackgroundColor(number){
        switch(number){
            case 2: return "#eee4da"; break;
            case 4: return "#ede0c8"; break;
            case 8: return "#f2b179"; break;
            case 16: return "#f59563"; break;
            case 32: return "#f67c5f"; break;
            case 64: return "#f65e3b"; break;
            case 128: return "#edcf72"; break;
            case 256: return "#edcc61"; break;
            case 512: return "#9c0"; break;
            case 1024: return "#33b5e5"; break;
            case 2048: return "#09c"; break;
            case 4096: return "#a6c"; break;
            case 8192: return "#93e"; break;
        }
        return 'black';
    }

    function getNumberColor(number){
        if(number < 4)
            return "#776e65";

        return 'white';
    }

    function noSpace(board){
        for(var i = 0; i < 4; i++)
            for(var j = 0; j < 4; j++){
                if(board[i][j] == 0)
                    return false;
            }
        return true;
    }

    function canMoveLeft(board){
        //左边是否没有数字？
        //左边数字时候和自己相等？
        for(var i = 0; i < 4; i++)
            for(var j = 1; j < 4; j++)
                if(board[i][j] != 0)
                    if(board[i][j-1] == 0 || board[i][j-1] == board[i][j])
                        return true;

        return false;
    }

    function canMoveUp(board){
        for(var i = 1; i < 4; i++)
            for(var j = 0; j < 4; j++)
                if(board[i][j] != 0)
                    if(board[i-1][j] == 0 || board[i-1][j] == board[i][j])
                        return true;

        return false;
    }

    function canMoveRight(board){
        for(var i = 0; i < 4; i++)
            for(var j = 0; j < 3; j++)
                if(board[i][j] != 0)
                    if(board[i][j+1] == 0 || board[i][j+1] == board[i][j])
                        return true;

        return false;
    }

    function canMoveDown(board){
        for(var i = 0; i < 3; i++)
            for(var j = 0; j < 4; j++)
                if(board[i][j] != 0)
                    if(board[i+1][j] == 0 || board[i+1][j] == board[i][j])
                        return true;

        return false;
    }

    function noBlockHorizontal(row, col1, col2, board){
        for(var i = col1 + 1; i < col2; i++){
            if(board[row][i] != 0)
                return false;
        }
        return true;
    }

    function noBlockVertical(col, row1, row2, board){
        for(var i = row1 + 1; i < row2; i++){
            if(board[i][col] != 0)
                return false;
        }
        return true;
    }

    function noMove(board){
        if(canMoveLeft(board) || canMoveRight(board) || canMoveUp(board) || canMoveDown(board)){
            return false;
        }
        return true;
    }
})(window);