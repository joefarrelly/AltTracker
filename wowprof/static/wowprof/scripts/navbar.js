var ajax_count = (ajax_count == null ? 0: ajax_count)
var ajax_queue = (ajax_queue == null ? []: ajax_queue);
// var ajax_count = 0;
// var ajax_queue = [];

function ajax_refresh_character(row, name, realm) {
    row.find('i').addClass('fa-spin');
    console.log(name + '-' + realm);
    console.log('doing ajax');
    $.ajax({
        url: "/wowprof/refresh_character/",
        dataType: "json",
        data: {
            "name": name,
            "realm": realm
        },
        success: function(data) {
            row.find('i').removeClass('fa-spin');
            row.find('td:eq(9)').html(data.last_updated);
            row.find('td:eq(8) a').text(data.gear);
            row.find('td:eq(6) a').text(data.prof1);
            row.find('td:eq(7) a').text(data.prof2);
            row.find('td:eq(2)').html(data.level);
            row.find('button').prop('disabled', false);
            $('#ajax-test').prop('disabled', false);
            if (data.prof1_href == '') {
                row.find('td:eq(6) a').removeAttr('href');
            } else {
                row.find('td:eq(6) a').prop('href', data.prof1_href);
            };
            if (data.prof2_href == '') {
                row.find('td:eq(7) a').removeAttr('href');
            } else {
                row.find('td:eq(7) a').prop('href', data.prof2_href);
            };
        }
    });
}

function fetcher() {
    while (ajax_count != null && ajax_count < 1 && ajax_queue != null && ajax_queue.length && ajax_queue.length > 0) {
        $("#ajax-test").prop('disabled', true);
        ajax_count++;
        console.log("incrementing pending ajax requests counter by 1.");
        ajax_queue.shift().call();
    };
    setTimeout(fetcher);
}
fetcher();

$(document).ajaxComplete(function() {
    if (ajax_count && ajax_count > 0) {
        ajax_count--;
        console.log("decrementing pending ajax requests counter by 1.");
    }
    console.log('ajax complete')
});

$(document).ready(function() {
    $("#ajax-test").on("click", function(){
        $('#alts-table td:nth-child(11) button').each(function(index) {
            var row = $(this).parent().parent();
            row.find('button').prop('disabled', true);
            ajax_queue.push(function() { ajax_refresh_character(row, row.find('td:eq(3)').text(), row.find('td:eq(4)').text()) });
        });
    });
    $('#alts-table td:nth-child(11) button').on('click', function() {
        var row = $(this).parent().parent();
        row.find('button').prop('disabled', true);
        ajax_queue.push(function() { ajax_refresh_character(row, row.find('td:eq(3)').text(), row.find('td:eq(4)').text()) });
    })
});


// alt tracker home table
$(function() {
    $('#alts-table td:nth-child(6)').each(function(index) {
        var classColor = ['Warrior','Paladin','Hunter','Rogue','Priest','Shaman','Mage','Warlock','Monk','Druid','DemonHunter','DeathKnight'];
        var tempclassName = $(this).text();
        var className = tempclassName.replace(/\s+/g, '');
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                var counter = 0
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 0 && counter < 6) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
            }
        }
    });
});

// checker table
$(function() {
    $('#alts-checker-table td:nth-child(6)').each(function(index) {
        var classColor = ['Warrior','Paladin','Hunter','Rogue','Priest','Shaman','Mage','Warlock','Monk','Druid','DemonHunter','DeathKnight'];
        var tempclassName = $(this).text();
        var className = tempclassName.replace(/\s+/g, '');
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                var counter = 0
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 0 && counter < 6) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
            }
        }
    });
});

// garrison
$(function() {
    $('#alts-checker-table td:nth-child(8)').each(function(index) {
        var classColor = ['Level3','Level2', 'Level1', 'NotBuilt'];
        var tempclassName = $(this).text();
        var className = tempclassName.replace(/\s+/g, '');
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                var counter = 0
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 6 && counter < 8) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
            }
        }
    });
});

// mage tower
$(function() {
    $('#alts-checker-table td:nth-child(9)').each(function(index) {
        var classColor = ['Yes','No'];
        var className = $(this).text();
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                var counter = 0
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 7 && counter < 9) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
            }
        }
    });
});

// shadowmourne
$(function() {
    $('#alts-checker-table td:nth-child(10)').each(function(index) {
        var classColor = ['Yes','No','Quest'];
        var className = $(this).text();
        var tempMo = $(this).parent("tr");
        var tempMo2 = tempMo[0].cells;
        for (var i = 0; i < classColor.length; i++) {
            if (className === classColor[i]) {
                var counter = 0
                $(this).parent("tr").children().each(function(index) {
                    if (counter > 8 && counter < 10) {
                        $(this).addClass(classColor[i]);
                    }
                    counter++;
                })
            }
        }
    });
});

$(document).ready(function () {
    // Tooltips
    $('.tooltip-wrapper').each(function () {
        if (typeof $('#' + $(this).data('tooltip-wrapper')).html() !== 'undefined') {
            $(this).tooltip(
            {
                html: true,
                title: $('#' + $(this).data('tooltip-wrapper')).html()
            });
        };
    });
});

$(document).ready(function () {
                $('th').each(function (col) {
                    $(this).hover(
                            function () {
                                $(this).addClass('focus');
                            },
                            function () {
                                $(this).removeClass('focus');
                            }
                    );
                    $(this).click(function () {
                        if ($(this).is('.asc')) {
                            $(this).removeClass('asc');
                            $(this).addClass('desc selected');
                            sortOrder = -1;
                        } else {
                            $(this).addClass('asc selected');
                            $(this).removeClass('desc');
                            sortOrder = 1;
                        }
                        $(this).siblings().removeClass('asc selected');
                        $(this).siblings().removeClass('desc selected');
                        var arrData = $('table').find('tbody >tr:has(td)').get();
                        arrData.sort(function (a, b) {
                            var val1 = $(a).children('td').eq(col).text().toUpperCase();
                            var val2 = $(b).children('td').eq(col).text().toUpperCase();
                            if ($.isNumeric(val1) && $.isNumeric(val2))
                                return sortOrder == 1 ? val1 - val2 : val2 - val1;
                            else
                                return (val1 < val2) ? -sortOrder : (val1 > val2) ? sortOrder : 0;
                        });
                        $.each(arrData, function (index, row) {
                            $('tbody').append(row);
                        });
                    });
                });
            });

// alt tracker home table
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

// alt checker table
function sortTableChecker(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("alts-checker-table");
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
