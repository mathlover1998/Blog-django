
$(document).ready(function() {
    $('.email').on('focus', function() {
      $(this).addClass('warning');
      $(this).after('<div class="warning-message">Note: Your email will be used for your username</div>');
    });
  
    $('.email').on('blur', function() {
      $(this).removeClass('warning');
      $(this).next('.warning-message').remove();
    });
  });