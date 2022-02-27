
jQuery(document).ready(function($) {
    'use strict';

    // ============================================================== 
    // Notification list
    // ============================================================== 
    if ($(".notification-list").length) {

        $('.notification-list').slimScroll({
            height: '250px'
        });

    }

    // ============================================================== 
    // Menu Slim Scroll List
    // ============================================================== 


    if ($(".menu-list").length) {
        $('.menu-list').slimScroll({

        });
    }

    // ============================================================== 
    // Sidebar scrollnavigation 
    // ============================================================== 

    if ($(".sidebar-nav-fixed a").length) {
        $('.sidebar-nav-fixed a')
            // Remove links that don't actually link to anything

            .click(function(event) {
                // On-page links
                if (
                    location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
                    location.hostname == this.hostname
                ) {
                    // Figure out element to scroll to
                    var target = $(this.hash);
                    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                    // Does a scroll target exist?
                    if (target.length) {
                        // Only prevent default if animation is actually gonna happen
                        event.preventDefault();
                        $('html, body').animate({
                            scrollTop: target.offset().top - 90
                        }, 1000, function() {
                            // Callback after animation
                            // Must change focus!
                            var $target = $(target);
                            $target.focus();
                            if ($target.is(":focus")) { // Checking if the target was focused
                                return false;
                            } else {
                                $target.attr('tabindex', '-1'); // Adding tabindex for elements not focusable
                                $target.focus(); // Set focus again
                            };
                        });
                    }
                };
                $('.sidebar-nav-fixed a').each(function() {
                    $(this).removeClass('active');
                })
                $(this).addClass('active');
            });

    }

    // ============================================================== 
    // tooltip
    // ============================================================== 
    if ($('[data-toggle="tooltip"]').length) {
            
            $('[data-toggle="tooltip"]').tooltip()

        }

     // ============================================================== 
    // popover
    // ============================================================== 
       if ($('[data-toggle="popover"]').length) {
            $('[data-toggle="popover"]').popover()

    }
     // ============================================================== 
    // Chat List Slim Scroll
    // ============================================================== 
        

        if ($('.chat-list').length) {
            $('.chat-list').slimScroll({
            color: 'false',
            width: '100%'


        });
    }
    // ============================================================== 
    // dropzone script
    // ============================================================== 

 //     if ($('.dz-clickable').length) {
 //            $(".dz-clickable").dropzone({ url: "/file/post" });
 // }


var i=1;
var content = document.getElementById('assign_calss_teacher').innerHTML;


$("#add").on("click", function(){

    if($(".parent-container").children().length>=0){
        i++;
        var content = "<div class='container'><button type='button' class='btn btn-danger'id='remove'>X</button><div class='form-row'><div class='col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12 mb-2'><label for='validationCustom03'>Class</label><select class='form-control' id='input-select id_class_id' name='class_id[]'><option>Select</option><option>L.K.G</option></select></div><div class='col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12 mb-2'><label  >Section</label><select class='form-control' id='input-select id='id_section_id' name='section_id[]'><option>Select</option><option>A</option></select></div><div class='col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12 mb-2'><label >Subject</label><select class='form-control' id='input-select id_subject_id' name='subject_id[]'><option>Select</option><option>English</option></select></div><div class='col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12 mb-2'><label for='ClassTeacher'>Class Teacher</label><br><label class='custom-control custom-radio custom-control-inline'><input type='radio' id='id_is_class_teacher' value='yes' name='is_class_teacher[]"+i+"'  class='custom-control-input'><span class='custom-control-label'>Yes</span></label><label class='custom-control custom-radio custom-control-inline'><input type='radio' value='no' id='id_is_class_teacher' name='is_class_teacher[]"+i+"' checked='' class='custom-control-input'><span class='custom-control-label'>No</span></label></div></div></div>";
        $(".parent-container").append(content);
     }
  /*if($(".parent-container").children().length == 5){
    $("#add").hide();http://192.168.1.66:8000/school/add_exam#
  }*/
});

$(".parent-container").on("click", "#remove", function(){
    i--;
    $(this).parent().remove(); 
    $("#add").show();
});

    /*$('#dateyear').datepicker({
        changeYear: true,
        changeMonth: true,
        dateFormat: 'dd-M-yy',
        showButtonPanel: true,
        closeText: 'Close',
        defaultDate: null,
        beforeShow: function( input ) {
         
        },
        onSelect: function () {

          
            
          },
    });*/

});

 // AND OF JQUERY


// $(function() {
//     "use strict";


    

   // var monkeyList = new List('test-list', {
    //    valueNames: ['name']

     // });
  // var monkeyList = new List('test-list-2', {
    //    valueNames: ['name']

   // });



   
   

// });

