//---------------------------------------------------------------------
// inv.networksegmentprofile Model
//---------------------------------------------------------------------
// Copyright (C) 2007-2017 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.inv.networksegmentprofile.Model");

Ext.define("NOC.inv.networksegmentprofile.Model", {
    extend: "Ext.data.Model",
    rest_url: "/inv/networksegmentprofile/",

    fields: [
        {
            name: "id",
            type: "string"
        },
        {
            name: "name",
            type: "string"
        },
        {
            name: "mac_discovery_interval",
            type: "int",
            defaultValue: 86400
        },
        {
            name: "autocreated_profile",
            type: "string"
        },
        {
            name: "enable_lost_redundancy",
            type: "boolean"
        },
        {
            name: "topology_methods",
            type: "auto"
        },
        {
            name: "management_vlan",
            type: "int",
            allowNull: true
        },
        {
            name: "multicast_vlan",
            type: "int",
            allowNull: true
        },
        {
            name: "mac_restrict_to_management_vlan",
            type: "boolean"
        },
        {
            name: "description",
            type: "string"
        },
        {
            name: "profile",
            type: "string"
        },
        {
            name: "profile__label",
            type: "string",
            persist: false
        },
        {
            name: "horizontal_transit_policy",
            type: "string"
        }
    ]
});
