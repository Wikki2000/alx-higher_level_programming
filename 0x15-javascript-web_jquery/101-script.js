$(document).ready(function () {

  // Add Item
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  // Remove Item
  $('DIV#remove_item').click(function () {
    $('UL.my_list').children().last().remove();
    // Alternatively use: $('UL.my_list li:last-child').remove();
  });

  // Clear list
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
