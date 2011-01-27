
(function ($){

    var moveBetweenSelect = function (sourceId, targetId) {
        var target = $('#' + targetId);

        $('#' + sourceId + ' :selected').each(function(count, selected) {
            var node = $(selected);

            node.remove();
            node.appendTo(target);
        });
    };

    $(document).ready(function(){

        $('.zeam-form').submit(function() {
            $(this).find('.field-plone-multi-select').each(
                function(count, node) {
                    var selectedId = $(node).attr('id') + '-selected';
                    var allOptions = [];

                    $('#' + selectedId + ' option').each(function(count, option) {
                        allOptions[count] = $(option).attr('value');
                    });
                    $('#' + selectedId).val(allOptions);
                });
        });

        $('.zeam-form .field-plone-multi-select').each(function(count, node) {
            var nodeId = $(node).attr('id');
            var selectedId = nodeId + '-selected';
            var availableId = nodeId + '-available';

            $('#' + nodeId + '-add').click(function() {
                moveBetweenSelect(availableId, selectedId);
                return false;
            });
            $('#' + nodeId + '-remove').click(function() {
                moveBetweenSelect(selectedId, availableId);
                return false;
            });
        });

        // On list widget, add class allowMultiSubmit
        $('.zeam-form input.field-list-add-line').addClass('allowMultiSubmit');
        $('.zeam-form input.field-list-remove-line').addClass('allowMultiSubmit');
        $('.zeam-form button.field-list-move-up').addClass('allowMultiSubmit');
        $('.zeam-form button.field-list-move-down').addClass('allowMultiSubmit');
    });

})(jQuery);
