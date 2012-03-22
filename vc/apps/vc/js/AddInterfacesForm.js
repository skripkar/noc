//---------------------------------------------------------------------
// Add Interfaces window
//---------------------------------------------------------------------
// Copyright (C) 2007-2012 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.vc.vc.AddInterfacesForm");

Ext.define("NOC.vc.vc.AddInterfacesForm", {
    extend: "Ext.Window",
    requires: [
        "NOC.sa.managedobject.LookupField"
    ],
    autoShow: true,
    closable: true,
    maximizable: true,
    modal: true,
    vc: null,
    width: 600,
    height: 400,
    autoScroll: true,

    initComponent: function() {
        var me = this;
        me.store = Ext.create("NOC.vc.vc.AddInterfacesStore");
        Ext.apply(me, {
            title: Ext.String.format("Add interfaces to VC {0} ({1})",
                                     me.vc.name, me.vc.l1),
            items: [
                {
                    xtype: "gridpanel",
                    itemId: "grid",
                    store: me.store,
                    columns: [
                        {
                            header: "Managed Object",
                            dataIndex: "managed_object",
                            editor: "sa.managedobject.LookupField",
                            renderer: NOC.render.Lookup("managed_object")
                        },
                        {
                            header: "Interface",
                            dataIndex: "interface",
                            editor: "textfield"
                        },
                        {
                            header: "Description",
                            dataIndex: "description",
                            flex: 1,
                            editor: "textfield"
                        }, /*,
                        {
                            header: "Tag",
                            dataIndex: "tagged",
                            width: 35,
                            editor: "checkboxfield",
                            renderer: NOC.render.Bool
                        },*/
                        {
                            xtype: "actioncolumn",
                            width: 20,
                            items: [{
                                icon: "/static/img/fam/silk/delete.png",
                                tooltip: "Delete",
                                handler: function(grid, rowIndex, colIndex) {
                                    grid.getStore().removeAt(rowIndex);
                                }
                            }]
                        }
                    ],
                    selType: "rowmodel",
                    plugins: [
                        Ext.create("Ext.grid.plugin.RowEditing", {
                            clicksToEdit: 1
                        })
                    ],
                    listeners: {
                        validateedit: function(editor, e) {
                            // @todo: Bring to plugin
                            var form = editor.editor.getForm();
                            // Process comboboxes
                            form.getFields().each(function(field) {
                                e.record.set(field.name, field.getValue());
                                if(Ext.isDefined(field.getLookupData))
                                    e.record.set(field.name + "__label",
                                                 field.getLookupData());
                                });
                        }
                    },
                    tbar: [
                        {
                            text: "Apply",
                            iconCls: "icon_tick",
                            scope: me,
                            handler: me.applyChanges
                        }
                    ]
                }
            ]
        });
        me.callParent();
    },
    // Run tasks
    applyChanges: function() {
        var me = this,
            mo = {};
        // Prepare data
        me.store.each(function(r) {
            var managed_object = r.get("managed_object"),
                interface = r.get("interface"),
                description = r.get("description");
            if(managed_object && interface) {
                var s = {
                    interface: interface,
                    untagged: me.vc.l1
                };
                if(description)
                    s.description = description;
                if(mo[managed_object])
                    mo[managed_object] = mo[managed_object].concat([s]);
                else
                    mo[managed_object] = [s];
            }
        }, me);
        // Run tasks
        me.mo = mo;
        me.runTasks();
    },
    runTasks: function() {
        var me = this;
        if(me.mo) {
            for(var o in me.mo) {
                NOC.mrt({
                    url: "/vc/vc/mrt/set_switchport/",
                    selector: o,
                    mapParams: {
                        configs: me.mo[o]
                    },
                    scope: me,
                    success: me.processTaskResult,
                    failure: function() {
                        NOC.error("Failed to apply VC settings");
                    }
                });
                break;
            }
        } else {
            Ext.info("All interface settings are applied successfully");
            me.close();
        }
    },
    // Process MRT result
    processTaskResult: function(result) {
        var me = this;
        console.log(result);
        Ext.each(result, function(r) {
            if(r.status) {
                // Filter out successfull objects
                me.store.filterBy(function(record, id) {
                    return record.get("managed_object") != r.object_id;
                });
            } else {
                // Write Error Message
                var m = r.result.text;
                me.store.each(function(record) {
                    if((record.get("managed_object") == r.object_id) &&
                        record.get("interface")) {
                        record.set("error", m);
                    }
                });
            }
            delete me.mo[r.object_id];
        });
        // me.runTasks();
        console.log(me.store);
    }
});
