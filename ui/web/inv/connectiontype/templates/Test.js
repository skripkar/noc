!function(){var n=Handlebars.template,e=NOC.templates.inv_connectiontype=NOC.templates.inv_connectiontype||{};e.Test=n({1:function(n,e,a,t,l){var r,o,s=null!=e?e:{};return'    <tr><th colspan="4">Gender \''+n.escapeExpression((o=null!=(o=a.gender||(null!=e?e.gender:e))?o:a.helperMissing,"function"==typeof o?o.call(s,{name:"gender",hash:{},data:l}):o))+"' can be connected to:</th></tr>\n    <tr><th>Gender</th><th>Connection Type</th><th>Reason</th><th>Description</th></tr>\n"+(null!=(r=a.each.call(s,null!=e?e.records:e,{name:"each",hash:{},fn:n.program(2,l,0),inverse:n.noop,data:l}))?r:"")},2:function(n,e,a,t,l){var r,o=null!=e?e:{},s=a.helperMissing,c="function",h=n.escapeExpression;return"        <tr>\n            <td>"+h((r=null!=(r=a.gender||(null!=e?e.gender:e))?r:s,typeof r===c?r.call(o,{name:"gender",hash:{},data:l}):r))+"</td>\n            <td>"+h((r=null!=(r=a.name||(null!=e?e.name:e))?r:s,typeof r===c?r.call(o,{name:"name",hash:{},data:l}):r))+"</td>\n            <td>"+h((r=null!=(r=a.reason||(null!=e?e.reason:e))?r:s,typeof r===c?r.call(o,{name:"reason",hash:{},data:l}):r))+"</td>\n            <td>"+h((r=null!=(r=a.description||(null!=e?e.description:e))?r:s,typeof r===c?r.call(o,{name:"description",hash:{},data:l}):r))+"</td>\n        </tr>\n"},compiler:[7,">= 4.0.0"],main:function(n,e,a,t,l){var r,o,s=null!=e?e:{};return"<h1>Possible connections for type "+n.escapeExpression((o=null!=(o=a.name||(null!=e?e.name:e))?o:a.helperMissing,"function"==typeof o?o.call(s,{name:"name",hash:{},data:l}):o))+'</h1>\n<table border="1">\n'+(null!=(r=a.each.call(s,null!=e?e.data:e,{name:"each",hash:{},fn:n.program(1,l,0),inverse:n.noop,data:l}))?r:"")+"</table>\n"},useData:!0})}();Ext.define("NOC.inv.connectiontype.templates.Test", {});