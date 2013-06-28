$(function() {
    var data = {{ data }};
    $.plot("#placeholder", [data]);
});
/*
$(function() {
    var d2 = [[0, 3], [4, 8], [8, 5], [9, 13]];
    
    $.plot("#placeholder", [ "{{ x }}" ]);

    
    //var data = [
    //        {label: "foo", data: [[0, 1], [1, 2], [0, 1], [3, 4]]},
    //        {label: "bar", data: [[0, 3], [4, 8], [8, 5], [9, 13]]}
    //    ];

    //$.plot("#placeholder", data); 
});
*/

