/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";
import { booleanField, BooleanField } from "@web/views/fields/boolean/boolean_field";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { useRecordObserver } from "@web/model/relational_model/utils";
import { Component, useState, onPatched, onRendered, onWillRender} from "@odoo/owl";

export class newBooleanToggleField extends BooleanField {
    static template = "hospital_management_system.DemoTemplateBooleanToggle";

    static props = {
        ...BooleanField.props,
        autosave: { type: Boolean, optional: true },
    };

       async onClick(event){

        var val = $('#newToggleButtonField').is(':checked') ? true:false;

        if (val === true){
            console.log(val);
            $("#newToggleButtonField").css("backgroundColor", "blue");
        }
        else if(val === false){
            console.log(val);
             $('#newToggleButtonField').css("backgroundColor", "orange");
        }

        this.props.state.value = val;
        const changes = { [this.props.name]: val };
        await this.props.record.update(changes, { save: this.props.autosave });
        }


    setup(){
//        alert("Setup Method Called");

        this.props.state = useState({value:this.props.record.data[this.props.name]});

        console.log('Hello');

//        onMounted(() => {
//            console.log("On Render Called");
//       });
    };
}

export const newbooleanToggleField = {
    ...booleanField,
    component: newBooleanToggleField,
    displayName: _t("Toggle"),
    supportedOptions: [
        {
            label: _t("Autosave"),
            name: "autosave",
            type: "boolean",
            default: true,
            help: _t(
                "If checked, the record will be saved immediately when the field is modified."
            ),
        },
    ],
    extractProps({ options }, dynamicInfo) {
        return {
            autosave: "autosave" in options ? Boolean(options.autosave) : true,
            readonly: dynamicInfo.readonly,
        };
    },
};

registry.category("fields").add("new_boolean_toggle", newbooleanToggleField);


// if (val){
//            event.target.style.backgroundColor = 'Blue';
//            event.target.value = 'on';
//            this.state.value = false;
//        }
//        else{
//            event.target.backgroundColor = 'red';
//            event.target.value = 'off';
//            this.state.value = true;
//        }