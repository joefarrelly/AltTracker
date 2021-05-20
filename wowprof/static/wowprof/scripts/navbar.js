$(function() {
    $('#alts-table td:nth-child(6)').each(function(index) {
        var classColor = ['Warrior','Paladin','Hunter','Rogue','Priest','Shaman','Mage','Warlock','Monk','Druid','DemonHunter','DeathKnight'];
        var tempclassName = $(this).text();
        var className = tempclassName.replace(/\s+/g, '');
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        // console.log(tempMo2);
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                // $(this).addClass(classColor[i]);
                // for (var j = 1; j < 4; j++) {
                    // console.log($(this).parent("tr")[0].cells[j]);
                    //console.log($(this));
                    //console.log($(this).parent("tr"));
                var counter = 0
                    // console.log($(this).parent("tr").children());
                    // $(this).parent("tr").children().addClass(classColor[i]);
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 0 && counter < 6) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
                    // console.log($(this).parent("tr")[0].cells[j]); //.eq(j));
                    // $(this).parent("tr")[0].cells[j];
                // }
                // for (var j = 0; j < 3; j++) {
                //     tempRow[j].addClass(classColor[i]);
                // }
                // $(this).parent("tr").addClass(classColor[i]);
            }
        }
    });
});

$(function() {
    $('#alts-table td:nth-child(9)').each(function(index) {
        var classColor = ['Yes','No'];
        var className = $(this).text();
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        // console.log(tempMo2);
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                // $(this).addClass(classColor[i]);
                // for (var j = 1; j < 4; j++) {
                    // console.log($(this).parent("tr")[0].cells[j]);
                    //console.log($(this));
                    //console.log($(this).parent("tr"));
                var counter = 0
                    // console.log($(this).parent("tr").children());
                    // $(this).parent("tr").children().addClass(classColor[i]);
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 6 && counter < 9) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
                    // console.log($(this).parent("tr")[0].cells[j]); //.eq(j));
                    // $(this).parent("tr")[0].cells[j];
                // }
                // for (var j = 0; j < 3; j++) {
                //     tempRow[j].addClass(classColor[i]);
                // }
                // $(this).parent("tr").addClass(classColor[i]);
            }
        }
    });
});

$(function() {
    $('#req-alts-table td:nth-child(4)').each(function(index) {
        var classColor = ['Warrior','Paladin','Hunter','Rogue','Priest','Shaman','Mage','Warlock','Monk','Druid','DemonHunter','DeathKnight'];
        var tempclassName = $(this).text();
        var className = tempclassName.replace(/\s+/g, '');
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        // console.log(tempMo2);
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                // $(this).addClass(classColor[i]);
                // for (var j = 1; j < 4; j++) {
                    // console.log($(this).parent("tr")[0].cells[j]);
                    //console.log($(this));
                    //console.log($(this).parent("tr"));
                var counter = 0
                    // console.log($(this).parent("tr").children());
                    // $(this).parent("tr").children().addClass(classColor[i]);
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 0 && counter < 4) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
                    // console.log($(this).parent("tr")[0].cells[j]); //.eq(j));
                    // $(this).parent("tr")[0].cells[j];
                // }
                // for (var j = 0; j < 3; j++) {
                //     tempRow[j].addClass(classColor[i]);
                // }
                // $(this).parent("tr").addClass(classColor[i]);
            }
        }
    });
});

$(function() {
    $('.prof-req-alts-table td:nth-child(4)').each(function(index) {
        var classColor = ['Warrior','Paladin','Hunter','Rogue','Priest','Shaman','Mage','Warlock','Monk','Druid','DemonHunter','DeathKnight'];
        var tempclassName = $(this).text();
        var className = tempclassName.replace(/\s+/g, '');
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        // console.log(tempMo2);
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                // $(this).addClass(classColor[i]);
                // for (var j = 1; j < 4; j++) {
                    // console.log($(this).parent("tr")[0].cells[j]);
                    //console.log($(this));
                    //console.log($(this).parent("tr"));
                var counter = 0
                    // console.log($(this).parent("tr").children());
                    // $(this).parent("tr").children().addClass(classColor[i]);
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 0 && counter < 4) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
                    // console.log($(this).parent("tr")[0].cells[j]); //.eq(j));
                    // $(this).parent("tr")[0].cells[j];
                // }
                // for (var j = 0; j < 3; j++) {
                //     tempRow[j].addClass(classColor[i]);
                // }
                // $(this).parent("tr").addClass(classColor[i]);
            }
        }
    });
});

// $(function() {
//     // console.log(data);
//     // var newData = JSON.parse(data);
//     $('.alt-profession-table td:nth-child(3)').each(function(){
//         // console.log($(this));
//         // console.log(this);
//         // console.log($(this).children());
//         $(this).children().each(function() {
//             console.log($(this).attr("href"));
//         })
//         console.log($(this).prev()[0].innerText);
//         console.log(data);
//         // console.log(data);
//         // this.href += 'anID';
//     })
// })

// $(function() {
//     $('#alts-table tr').each(function(index) {
//         console.log($(this));
//     })
// })


function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("alts-table");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (x.innerText.toLowerCase() > y.innerText.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerText.toLowerCase() < y.innerText.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function sortTableNum(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("alts-table");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (parseInt(x.innerText) > parseInt(y.innerText)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (parseInt(x.innerText) < parseInt(y.innerText)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function sortTableSpecial(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("alts-table");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}


//var coll = document.getElementsByClassName("subnavbtn");
//var i;

//for (i = 0; i < coll.length; i++) {
//   coll[i].addEventListener("click", function () {
//        this.classList.toggle("active");
//        var content = this.nextElementSibling;
//        if (content.style.display === "block") {
//            content.style.display = "none";
//        } else {
//            content.style.display = "block";
//        }
//    });
//} 



/*function boost(evt, boostType) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(boostType).style.display = "block";
    evt.currentTarget.className += " active";
} */


//function deleteBoost() {
//    if (confirm("Are you sure you wanna delete dis ting")) {
//        alert("Boost ID ting has been deleted succesffuly");
//    } else {
//        alert("Boost has not been deleted");
//    }
//}

//$(document).on('click', '#confirm-delete', function () {
//    return confirm('Are you sure you want to delete this?');
//})


//function confirmDeleteBoost() {
//    return confirm('Are you sure you want to delete the selected boost?')
//}

//function confirmDeleteAccount() {
//    return confirm('Are you sure you want to delete the selected account?')
//}

//function submitEditForms() {
//    document.getElementById("edit-user-form").submit();
//    document.getElementById("edit-user-role-form").submit();
//    document.getElementById("edit-advertiser-form").submit();
//   document.getElementById("edit-booster-form").submit();
//}


/*$(document).ready(function () {
    // all custom jQuery will go here
    $("#boost-options-table tr:gt(0)").click(function () {
        $(this).addClass('selected').siblings().removeClass('selected');
        var value = $(this).find('td:first').html();
        document.getElementById("id_boostId").value = value;
        //var finalrow = []
        //var row = document.getElementsByClassName('selected');
        //var temprow = row[0].children;
        //for (var i = 0; i < temprow.length; i++) {
        //    var tempval = temprow[i].textContent;
        //    finalrow.push(tempval);
        //}
        //console.log(finalrow);

        $('#delete-boost-button').removeAttr('disabled');
    });
    $("#accounts-table tr:gt(0)").click(function () {
        $(this).addClass('selected').siblings().removeClass('selected');
        var value = $(this).find('td:first').html();
        var tempVal = document.getElementsByName("userId");
        for (var i = 0; i < tempVal.length; i++) {
            tempVal[i].value = value;
        }
        $('#delete-account-button').removeAttr('disabled');
        $('#edit-account-button').removeAttr('disabled');

    });

    $(".delete-boost-form").submit(function () {
        if (confirm('Are you sure you want to delete the selected boost?')) {
            alert("Selected boost has been deleted successfully!");
            return true;
        } else {
            return false;
        }
    });

    $(".delete-account-form").submit(function () {
        if (confirm('Are you sure you want to delete the selected account?')) {
            alert("Selected account has been deleted successfully!");
            return true;
        } else {
            return false;
        }
    });

    $("#edit-account-form").submit(function() {
        alert("Account has been updated successfully!");
        return true;
    })

    $('#id_role-userRole').on('change', function () {
        $('#id_advRank').change();
        $('#id_advertiser-advRank').change();
        if (this.value === 'User') {
            $("#userData").show();
            $("#userRoleData").show();
            $("#advertiserData").hide();
            $("#boosterData").hide();
            $("#advertiserData :input").prop("disabled", true);
            $("#boosterData :input").prop("disabled", true);
        } else if (this.value === 'Advertiser') {
            $("#userData").show();
            $("#userRoleData").show();
            $("#advertiserData").show();
            $("#boosterData").hide();
            $("#advertiserData :input").prop("disabled", false);
            $("#boosterData :input").prop("disabled", true);
        } else if (this.value === 'Booster') {
            $("#userData").show();
            $("#userRoleData").show();
            $("#advertiserData").show();
            $("#boosterData").show();
            $("#advertiserData :input").prop("disabled", false);
            $("#boosterData :input").prop("disabled", false);
        }
    });
    $('#id_role-userRole').change();

    $('#id_advRank').on('change', function () {
        $("#id_advCommission").val(this.value * 0.04);
    });

    $('#id_advertiser-advRank').on('change', function () {
        $("#id_advertiser-advCommission").val(this.value * 0.04);
    });
    //$('#id_advRank').change();//////////////////////////////////////////////////////////////////////////

    //      $.ajax({
    //            url: 'ajax/deleted_boost/',
    //            data: {
    //                'boostId': boostId
    //            },
    //            dataType: 'json',
    //            success: function (data) {
    // do some big tings
    //            }
    //        });

});*/
//$('.ok').on('click', function (e) {
//    alert($("#table tr.selected td:first").html());
//});




// function doSomething() {
//     // alert("I'm done resizing for the moment");
//     image = document.getElementById('character-image')
//     width = window.innerWidth;
//     // alert(width)
//     temp = width / -4
//     // alert(temp)
//     temp = temp + 'px'
//     // alert(temp)
//     image.style.marginTop = temp;
// };

// var resizeTimer;
// $(window).resize(function() {
//     clearTimeout(resizeTimer);
//     resizeTimer = setTimeout(doSomething, 500);
// });

