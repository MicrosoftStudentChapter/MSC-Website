(function($) {
    var slide = function(ele,options) {
        var $ele = $(ele);
      
        var setting = {
        		
            speed: 1000,
           
            interval: 2000,
            
        };
       
        $.extend(true, setting, options);
    
        var states = [
            // { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 2, width: 120, height: 150, top: 69, left: 134, $opacity: 0.2 },
            { $zIndex: 3, width: 130, height: 170, top: 59, left: 0, $opacity: 0.4 },
            { $zIndex: 4, width: 170, height: 218, top: 35, left: 110, $opacity: 0.7 },
            { $zIndex: 5, width: 224, height: 288, top: 0, left: 263, $opacity: 1 },
            { $zIndex: 4, width: 170, height: 218, top: 35, left: 470, $opacity: 0.7 },
            { $zIndex: 3, width: 130, height: 170, top: 59, left: 620, $opacity: 0.4 },
            { $zIndex: 2, width: 120, height: 150, top: 69, left: 500, $opacity: 0.2 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 },
            { $zIndex: 1, width: 100, height: 120, top: 79, left: 154, $opacity: 0.1 }
        ];

        var $lis = $ele.find('li');
        var timer = null;

        
        $ele.find('.hi-next').on('click', function() {
            next();
        });
        $ele.find('.hi-prev').on('click', function() {
            prev();
        });
        $ele.on('mouseenter', function() {
            clearInterval(timer);
            timer = null;
        }).on('mouseleave', function() {
            autoPlay();
        });

        $lis.on('click', function(){
            console.log(this.style.left);
            if(this.style.left < "110px")
            {
                prev();
                prev();
            }
            else if(this.style.left < "230px")
            {
                prev();
            }
            else if(this.style.left ==="470px")
            {
                next();
            }
            else if(this.style.left === "620px")
            {
                next();
                next();
            }
        });

        move();
        autoPlay();

      
        function move() {
            $lis.each(function(index, element) {
                var state = states[index];
                $(element).css('zIndex', state.$zIndex).finish().animate(state, setting.speed).find('img').css('opacity', state.$opacity);
            });
        }

        function next() {
           
            states.unshift(states.pop());
            move();
        }

        function prev()
        {
            states.push(states.shift());
            move();
        }

        function autoPlay() {
            timer = setInterval(next, setting.interval);
        }
    }

    $.fn.hiSlide = function(options) {
        $(this).each(function(index, ele) {
            slide(ele,options);
        });
        return this;
    }
})(jQuery);
