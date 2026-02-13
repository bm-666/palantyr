import {UIContainerStatus} from "../model";
import { UI_STATUS_COLOR } from "./container.ui";

export function StatusDot({status}: {status: UIContainerStatus}) {
    return (
        <span
        className={`w-2.5 h-2.5 rounded-full ${UI_STATUS_COLOR[status]}`}
        />
        
    );
}
