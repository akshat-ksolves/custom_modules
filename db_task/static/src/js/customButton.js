/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { registry } from '@web/core/registry';
import { listView } from '@web/views/list/list_view';
import { ListController } from '@web/views/list/list_controller';
import { useService } from "@web/core/utils/hooks";

export class ExportRecords extends ListController{

    setup(){
        super.setup();
        console.log("Hello")
        this.orm = useService("orm");
       this.actionService = useService("action");
    }

    async changeState(){
         alert("Hello.....Method Called");
         var resIds = await this.getSelectedResIds();
         console.log(resIds);
         var keys = Object.keys(this.model.config.activeFields)
         await this.orm.call("res.partner", "test_function", [resIds, keys])
         .then((data)=>{
         console.log(data, typeof(data))
//            this.actionService.doAction({...data});
    })
    }
}

registry.category('views').add('export_records',{
    ...listView,
    Controller: ExportRecords,
})