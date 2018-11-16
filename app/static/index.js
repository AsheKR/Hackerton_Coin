$(function() {
  $('#select-coin').click(function() {
    $target = $('#select-coin-menu')
    $target.css('display', 'flex')
  })

  $('.black_out').click(function() {
    $target = $('#select-coin-menu')
    $target.css('display', 'none')
  })
})

var globalVar = (function() {
	var _fiveSc		    = 0,
      _selectCoinId = null;

	var setFiveSc = function(fiveSc) {
		_fiveSc = fiveSc;
	}

	var getFiveSc = function() {
		return _fiveSc;
	}

  var setSelectCoinId = function(selectCoinId) {
    _selectCoinId = selectCoinId
  }

  var getSelectCoinId = function() {
    return _selectCoinId
  }

	return {
		setFiveSc			  : setFiveSc,
		getFiveSc			  : getFiveSc,
    setSelectCoinId : setSelectCoinId,
    getSelectCoinId : getSelectCoinId
	}
}())

var ChangeHtml = {
    init : function() {
      this.call_ajax()
    },

    change_html : function(data) {
    $target = $('#select-coin-menu')

    $coin_text = $('.coin_text p')
    $before_coin_value = $('.before_coin_value p')
    $current_coin_value =$('.current_coin_value p')

    $arrow = $('.fas')

    $percent = $('.right_coin_percent p')

    $body = $('body')
    console.log($body)

    $coin_text.text(data.coin.get_name_display)
    $before_coin_value.text('Before Price: ' + data.before_value.toLocaleString())
    $current_coin_value.text('Current Price: ' + data.now_value.toLocaleString())
    $percent.text(data.percent + '%')

    $arrow.removeClass('fa-sort-down')
    $arrow.removeClass('fa-sort-up')

    if (data.percent > 0) {
        $arrow.addClass('fa-sort-up')
        $arrow.css('color', 'blue')
        $percent.css('color', 'blue')
    }else {
        $arrow.addClass('fa-sort-down')
        $arrow.css('color', 'red')
        $percent.css('color', 'red')
    }
    $body.css('background-image', 'url("'+data.img_path+'")')
  },

  interval_set : function() {
      globalVar.setFiveSc(setInterval(this.call_ajax, 10000))
  },

  call_ajax : function() {
    var selectCoinId = $('.coin_pk_list:checked').attr('id')

    if (selectCoinId == null) {
      selectCoinId = 2
    }

    if (globalVar.getSelectCoinId() != selectCoinId) {
      globalVar.setSelectCoinId(selectCoinId)
      if (globalVar.getFiveSc()) {
          clearInterval(globalVar.getFiveSc())
      }
      ChangeHtml.interval_set()
    }

    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/apis/list/"+selectCoinId+'/',
        success: function(data) {
          ChangeHtml.change_html(data)
          console.log(data)
        }
    })
  }
}
