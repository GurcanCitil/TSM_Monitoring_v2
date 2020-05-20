$(document).ready(function() {
    var table = $('#example').DataTable( {
        "scrollY": "200px",
        "paging": false
    } );

    $('a.toggle-vis').on( 'click', function (e) {
        e.preventDefault();

        var column = table.column( $(this).attr('data-column') );

        column.visible( ! column.visible() );
    } );
} );