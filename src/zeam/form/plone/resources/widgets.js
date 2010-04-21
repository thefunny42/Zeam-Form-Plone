

function moveBetweenSelect(sourceId, targetId) {
    var target = jq('#' + targetId);

    jq('#' + sourceId + ' :selected').each(function(count, selected) {
        var node = jq(selected);

        node.remove();
        node.appendTo(target);
    });
};


jq(document).ready(function(){

    jq('.zeam-form').submit(function() {
        jq(this).find('.field-plone-multi-select').each(
            function(count, node) {
                var selectedId = jq(node).attr('id') + '-selected';
                var allOptions = [];
                jq('#' + selectedId + ' option').each(function(count, option) {
                    allOptions[count] = jq(option).attr('value');
                });
                jq('#' + selectedId).val(allOptions);
            });
    });

    jq('.zeam-form .field-plone-multi-select').each(function(count, node) {
        var nodeId = jq(node).attr('id');
        var selectedId = nodeId + '-selected';
        var availableId = nodeId + '-available';

        jq('#' + nodeId + '-add').click(function() {
            moveBetweenSelect(availableId, selectedId);
            return false;
        });
        jq('#' + nodeId + '-remove').click(function() {
            moveBetweenSelect(selectedId, availableId);
            return false;
        });
    });
});
