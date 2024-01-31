/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { ListController } from '@web/views/list/list_controller';
import { useService } from "@web/core/utils/hooks";

export class CustomButton extends ListController {
    setup(){
        super.setup();
        console.log("Hello")
        this.orm = useService("orm");
    }
    async changeState(){
         alert("Hello.....Method Called");
//         debugger;
         var resIds = await this.getSelectedResIds();
         console.log(resIds);
         let data = this.orm.call("device.assignment", "changeState", [resIds]);
         console.log(data)
    }
}
registry.category('views').add('changeStateButton',{
    ...listView,
    Controller: CustomButton,
})