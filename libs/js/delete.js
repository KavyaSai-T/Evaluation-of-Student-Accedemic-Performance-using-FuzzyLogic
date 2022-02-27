jQuery( document ).ready(function( $ ) {
         
    var loadForm = function () {
    var btn = jQuery(this);
    jQuery.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        jQuery("#modal-book").modal("show");
      },
      success: function (data) {
        jQuery("#modal-book .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = jQuery(this);
    jQuery.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          jQuery("#book-table tbody").html(data.html_book_list);
          jQuery("#modal-book").modal("hide");
          window.location.reload(window.location.href);
        }
        else {
          jQuery("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

    jQuery(".js-delete-book").click(loadForm);
    jQuery("#modal-book").on("submit", ".js-book-delete-form", saveForm);
    jQuery(".accordion-heading").click(function(){
    jQuery(this).find('i').toggleClass('fa-chevron-up');
    jQuery(this).find('i').toggleClass('fa-chevron-down');
    jQuery(this).parent().siblings().find(".accordion-content").slideUp();
    jQuery(this).parent().siblings().find(".fa-chevron-up").removeClass('fa-chevron-up').addClass('fa-chevron-down');
    jQuery(this).next(".accordion-content").slideToggle();
  });
  
});
