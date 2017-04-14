$(document).ready(function() 
{
    function update_list(content)
    {
        var html = "";

        for (index = 0; index < content.length; ++index)
        {
            var element = content[index];
            html += '<tr>';
            html +=     '<td>';
            html +=          element['sentence'];
            html +=     '</td>';
            html +=     '<td>';
            html +=          element['person'];
            html +=     '</td>';
            html +=     '<td>';
            html +=          element['date'];
            html +=     '</td>';
            html +=     '<td>';
            html +=          '<span class="glyphicon glyphicon-remove" style="cursor: pointer; cursor: hand;" id="delete_' + index + '"></span>';
            html +=     '</td>';
            html +=     '<td>';
            html +=          element['vote'] + '&nbsp;&nbsp;<span class="glyphicon glyphicon-thumbs-up" style="cursor: pointer; cursor: hand;" id="vote_' + index + '"></span>';
            html +=     '</td>';
            html += '</tr>';
        }
        $("#list").html(html);
    }

    function display_popup(style, message)
    {
        $('#popup').fadeIn(0);
        $("#popup").html('<div class="alert alert-' + style + '">' + message + ' </div>');
        $('#popup').delay(2000).fadeOut(500);
    }

    /** GET **/

    $.ajax({
        url: '/sentences',
        type: 'GET',
        success: function(result) 
        {
            update_list(jQuery.parseJSON(result));
        }
    });

    /** DELETE **/

    $(document).on('click','.glyphicon-remove', function()
    {
        var sentence_id = $(this).attr('id').replace('delete_', '');

        $.ajax({
            url: '/sentences',
            type: 'DELETE',
            data: {"id": sentence_id},
            success: function(result) 
            {
                update_list(jQuery.parseJSON(result));
            },
            error : function(result) 
            {
                display_popup('danger', 'Erreur sur suppression');
            }
        });

        return false;
    });

    /** PATCH **/

    $(document).on('click','.glyphicon-thumbs-up', function()
    {
        var sentence_id = $(this).attr('id').replace('vote_', '');

        $.ajax({
            url: '/sentences',
            type: 'GET',
            success: function(result) 
            {
                current_vote = Number(jQuery.parseJSON(result)[sentence_id]['vote']);

                $.ajax({
                    url: '/sentences',
                    type: 'PATCH',
                    data: {"id": sentence_id, "vote" : current_vote + 1},
                    success: function(result) 
                    {
                        update_list(jQuery.parseJSON(result));
                        display_popup('success', 'Votre vote a bien été pris en compte');
                    },
                    error : function(result) 
                    {
                        display_popup('danger', 'Erreur sur vote');
                    }
                });
            },
            error : function(result) 
            {
                display_popup('danger', 'Erreur sur vote');
            }
        });

        return false;
    });

    /** POST **/

    $('#button').click(function(e)
    {
        e.preventDefault();

        $.ajax({
            url: '/sentences',
            type: 'POST',
            data: { sentence : $("#sentence").val(), 
                    person   : $("#person").val(), 
                    date     : $("#date").val()},
            success: function(result) 
            {
                $("#sentence").val("");
                $("#person").val("");
                $("#date").val("");
                display_popup('success', 'Citation ajoutee avec success');
                update_list(jQuery.parseJSON(result));
            },
            error : function(result) 
            {
                display_popup('danger', 'Erreur sur ajout');
            }
        });
    });
});