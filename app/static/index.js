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
